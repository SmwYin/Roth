# Project overview: Roth

**COMPLETE — 293/293 declaration assessments complete.**

## Executive summary

Roth formalizes Roth’s theorem through characteristic-free Hasse derivatives, Wronskians, coefficient bounds, weighted indices, lattice counting, auxiliary polynomials and the final rational-approximation contradiction. This review assesses correctness of the retained interfaces and mathlib contribution potential; production Lean sources and pinned versions are unchanged.

Keep coherent differential and determinant APIs separate from scalar storage/construction aliases. The strongest upstream candidates are the multivariate Hasse operator and substantive laws, multivariate Taylor identities, coefficient estimates, determinant bounds, coefficient decomposition and arithmetic descent. A NO contribution verdict identifies existing API or a short composition; it does not by itself recommend deleting useful local notation.

Generality and representation changes require their exact verified bridges: characteristic-zero converse results retain their hypotheses; coefficient l1 size is distinct from a coefficient maximum; real-valued index and supremum definitions retain zero/default and mixed-zero-weight conventions. Generic construction primitives do not automatically replace a complete project theorem.

All applicable per-declaration reports, exact executed scratch sources, successful and rejected native receipts, searches, root acceptance and evidence manifests are retained. Private declarations use the explicit B1 prefilter with native/source/caller verification; their full public contribution searches are not claimed. Optional ask_chatgpt_math was unavailable, and local search-index failures are not absence evidence.

## Statistics

- Production Lean source files:14; physical Lean lines:4874; canonical written declarations:293 (28 definitions,191 theorems,74 lemmas).
- Visibility:215 public,78 private. Completed assessments:293; unfinished:0.
- Completed verdicts: BORDERLINE-needs-human:100, NO-composable-from-mathlib:20, NO-mathlib-has-it:46, SKIP:78, YES-add-as-is:14, YES-but-generalise-first:35.
- Source/pin preservation:17 hashes unchanged. Native whole293 direct graph:740 body and291 type references to canonical project declarations; cross-file279 body and110 type references across31 module pairs.
- Semantic comparisons among completed declarations:42778; all unique expected pairs present. All42,778 project pairs covered.

## Part 1: Declaration inventory

Full native types and source-faithful mathematical fields follow. Lexical references, native direct references and explanatory dependencies are separate scopes. Fourteen older kind-only type fields and fifteen mathematical-argument descriptions have separately preserved repair provenance; historical accepted packages remain immutable. Usage counts do not establish external or implicit simp/generated/transitive deadness.

### Roth.lean

Completed assessments: 0/0.

No written declarations: this is the aggregate import module.

#### File structural summary

- Written declarations: 0; kinds: {}
- **Key API (at least three lexical callers)**: []
- **Unused in file (observation)**: []
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Box.lean

Completed assessments: 14/14.

#### def Roth.box

Type:

```lean
{σ : Type u} → [Fintype σ] → [DecidableEq σ] → (σ → ℕ) → Finset (σ →₀ ℕ)
```

- **What**: This defines the finite set of natural multi-indices bounded by r in every coordinate.
- **How**: piFinset of ranges mapped through inverse finite-function/Finsupp equivalence.
- **Hypotheses**: Fintype σ and DecidableEq σ for literal enumeration; both mechanically weakenable noncomputably; r : σ → ℕ; no positivity or nonempty assumption
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.mem_box`, `Roth.card_box`
- **Used by other files (lexical)**: `Roth.sum_box_prod_pow_le_aux`, `Roth.abs_eval_le`, `Roth.card_filter_box_fiber_aux`, `Roth.card_filter_box_last`, `Roth.filter_weight_le_eq_empty`, `Roth.card_filter_fiber_eq`, `Roth.card_filter_weight_le_of_le_sqrt_aux`, `Roth.card_filter_weight_le_succ_aux`, `Roth.card_filter_weight_le`, `Roth.abs_eval_lt_of_le_index`, `Roth.mul_card_filter_weight_le_aux`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `MvPolynomial.eq_sum_box_hasseDeriv`, `MvPolynomial.eval_eq_sum_box`
- **Visibility**: public
- **Lines**: 47–48; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.box.md).

#### def Roth.weight

Type:

```lean
{σ : Type u} → [Fintype σ] → (σ → ℕ) → (σ →₀ ℕ) → ℝ
```

- **What**: Real reciprocal-parameter weight of a natural multi-index.
- **How**: Full ambient finite sum of d_j/r_j; totalized division permits zero denominators.
- **Hypotheses**: Finite variable enumeration, natural parameter vector and natural Finsupp; no positivity or DecidableEq.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.weight_nonneg`, `Roth.weight_zero`, `Roth.weight_add`, `Roth.weight_eq_zero_iff`, `Roth.weight_single`, `Roth.weight_le_card`, `Roth.weight_mul_left`, `Roth.weight_le_degree_div`, `Roth.weight_mapDomain`
- **Used by other files (lexical)**: `Roth.index`, `Roth.index_le_weight`, `Roth.exists_weight_eq_index`, `Roth.le_index_iff`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.weight_eq_finsuppWeight_div`, `Roth.index_mul_left_weights`, `Roth.index_unique`, `Roth.filter_weight_le_eq_empty`, `Roth.card_filter_fiber_eq`, `Roth.card_filter_weight_le_of_le_sqrt_aux`, `Roth.card_filter_weight_le_succ_aux`, `Roth.card_filter_weight_le`, `Roth.abs_prod_pow_le_rpow_of_le_weight`, `Roth.le_index_of_forall_eval_eq_zero`, `Roth.exists_hasseDeriv_eval_ne_zero`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.mul_card_filter_weight_le_aux`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `Roth.sum_max_sub_le_index_det`, `Roth.weight_le_delta_aux`
- **Visibility**: public
- **Lines**: 71–71; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight.md).

#### theorem Roth.mem_box

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : DecidableEq σ] {r : σ → ℕ} {d : σ →₀ ℕ},
  d ∈ box r ↔ ∀ (j : σ), d j ≤ r j
```

- **What**: Membership in the finite box iff coordinatewise natural bounds.
- **How**: Transport equivalence membership, Cartesian product membership, natural range successor bound.
- **Hypotheses**: σ universe polymorphic; Fintype σ; DecidableEq σ; r : σ → ℕ; d : σ →₀ ℕ
- **Uses from project (lexical body)**: `Roth.box`
- **Project references in type**: `Roth.box`
- **Native direct body references**: `Roth.box`
- **Native direct type references**: `Roth.box`
- **Used by in file (lexical)**: `Roth.card_le_card_box`
- **Used by other files (lexical)**: `Roth.abs_eval_le`, `Roth.card_filter_box_fiber_aux`, `Roth.card_filter_box_last`, `Roth.abs_eval_lt_of_le_index`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `MvPolynomial.eq_sum_box_hasseDeriv`
- **Visibility**: public
- **Lines**: 51–52; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.mem_box.md).

#### theorem Roth.card_box

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : DecidableEq σ] (r : σ → ℕ),
  (box r).card = ∏ j : σ, (r j + 1)
```

- **What**: Counts bounded natural multi-indices as product of coordinate sizes.
- **How**: Map cardinality, dependent finite-product cardinality, natural range cardinality.
- **Hypotheses**: Universe-polymorphic σ; Fintype σ; DecidableEq σ parent-interface; arbitrary r:σ→ℕ.
- **Uses from project (lexical body)**: `Roth.box`
- **Project references in type**: `Roth.box`
- **Native direct body references**: `Roth.box`
- **Native direct type references**: `Roth.box`
- **Used by in file (lexical)**: `Roth.card_le_card_box`
- **Used by other files (lexical)**: `Roth.card_filter_weight_le_of_le_sqrt_aux`, `Roth.abs_eval_lt_of_le_index`
- **Visibility**: public
- **Lines**: 57–58; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_box.md).

#### theorem Roth.card_le_card_box

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ} {s : Finset (σ →₀ ℕ)},
  (∀ d ∈ s, ∀ (j : σ), d j ≤ r j) → s.card ≤ ∏ j : σ, (r j + 1)
```

- **What**: Distinct natural multiindices bounded coordinatewise by r have cardinality at most product(rj+1).
- **How**: Containment in finite coordinate product, or independent injective Fin-valued tuple representation.
- **Hypotheses**: arbitrary universe polymorphic σ; Fintype σ; r:σ→ℕ; s:Finset(σ→₀ℕ); ∀d∈s,j,dj≤rj; no public DecidableEq
- **Uses from project (lexical body)**: `Roth.card_box`, `Roth.mem_box`
- **Project references in type**: []
- **Native direct body references**: `Roth.box`, `Roth.card_box`, `Roth.mem_box`
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.abs_coeff_det_hasseDeriv_le`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
- **Visibility**: public
- **Lines**: 65–68; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_le_card_box.md).

#### theorem Roth.weight_nonneg

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ), 0 ≤ weight r d
```

- **What**: Every natural multi-index has nonnegative real reciprocal-parameter weight, allowing zero parameters.
- **How**: Finite sum of nonnegative quotients; natural-cast nonnegativity supplies both coordinates.
- **Hypotheses**: arbitrary universe-polymorphic type sigma; Fintype sigma; r:sigma to Nat; d:sigma finitely supported Nat; no positivity premise
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.weight`
- **Native direct body references**: []
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_nonneg`, `Roth.filter_weight_le_eq_empty`, `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 75–76; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_nonneg.md).

#### theorem Roth.weight_zero

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ), weight r 0 = 0
```

- **What**: The zero natural multi-index has real weight zero for any natural parameter family.
- **How**: Finite sum of zeros using cast-zero and zero-division; source simp [weight].
- **Hypotheses**: Arbitrary σ with Fintype; No positive/nonzero denominator or DecidableEq premise
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 80–81; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_zero.md).

#### theorem Roth.weight_add

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) (d e : σ →₀ ℕ),
  weight r (d + e) = weight r d + weight r e
```

- **What**: Real reciprocal-denominator weight is additive in natural exponent vectors.
- **How**: Nat.cast_add, add_div, and Finset.sum_add_distrib; independently verified explicit term.
- **Hypotheses**: Universe-polymorphic σ, Fintype σ, r : σ → ℕ, d e : σ →₀ ℕ; no positivity or DecidableEq.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.card_filter_fiber_eq`, `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 85–86; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_add.md).

#### theorem Roth.weight_eq_zero_iff

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ},
  (∀ (j : σ), 0 < r j) → ∀ {d : σ →₀ ℕ}, weight r d = 0 ↔ d = 0
```

- **What**: Positive reciprocal natural weights detect exactly the zero natural multi-index.
- **How**: Finite nonnegative sum zero iff every quotient zero, nonzero denominators and natural casts, finsupp extensionality.
- **Hypotheses**: Fintype σ fixed by parent; positivity globally can localize to d.support (verified); no DecidableEq.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_eq_zero_iff`
- **Visibility**: public
- **Lines**: 91–93; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_zero_iff.md).

#### theorem Roth.weight_single

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) (j : σ) (n : ℕ),
  weight r (Finsupp.single j n) = ↑n / ↑(r j)
```

- **What**: A single-coordinate multi-index has weight n/r j, with real division.
- **How**: Unfold finite weighted sum, evaluate the single coordinate; independently checked support-sum composition uses four distinct facts including cast-zero and zero-division.
- **Hypotheses**: Universe-polymorphic sigma with Fintype; r:sigma→Nat, j:sigma, n:Nat. No DecidableEq or denominator positivity.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.card_filter_fiber_eq`, `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 96–98; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_single.md).

#### theorem Roth.weight_le_card

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ} {d : σ →₀ ℕ},
  (∀ (j : σ), d j ≤ r j) → weight r d ≤ ↑(Fintype.card σ)
```

- **What**: A bounded normalized natural multi-index has real weight at most the number of variables.
- **How**: Bound each nonnegative-denominator ratio by one and sum.
- **Hypotheses**: Fintype variable type, natural denominators and finitely supported natural coefficients; all coordinates bounded. No strict positivity or public DecidableEq.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.weight`
- **Native direct body references**: []
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_le_card`
- **Visibility**: public
- **Lines**: 103–106; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_le_card.md).

#### theorem Roth.weight_mul_left

Type:

```lean
{σ : Type u} → [Fintype σ] → {l : ℕ} → (r : σ → ℕ) → (d : σ →₀ ℕ) → Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / ↑l
```

- **What**: Uniformly multiplying denominator parameters divides monomial weight by that scale.
- **How**: Cast product, distribute division over sum, reassociate division, commute denominator factors.
- **Hypotheses**: Finite variable enumeration; arbitrary natural scale and parameter family including zeros; no positivity or DecidableEq.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_mul_left_weights`
- **Visibility**: public
- **Lines**: 110–112; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_mul_left.md).

#### theorem Roth.weight_le_degree_div

Type:

```lean
∀ {σ : Type u} [Fintype σ] {r : σ → ℕ} {m : ℕ}, 0 < m → (∀ j : σ, m ≤ r j) → ∀ d : σ →₀ ℕ, Roth.weight r d ≤ (Finsupp.degree d : ℝ) / (m : ℝ)
```

- **What**: Bounds a multi-index reciprocal weight by total degree divided by a positive common lower bound on denominators.
- **How**: Rewrite degree as coordinate sum, cast and distribute division; use sum monotonicity and division antitonicity in positive denominators.
- **Hypotheses**: Fintype variable enumeration; natural denominators; positive natural m; all r_j at least m; natural finitely supported multi-index. No DecidableEq needed.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 118–122; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_le_degree_div.md).

#### theorem Roth.weight_mapDomain

Type:

```lean
∀ {σ : Type u_3} [Fintype σ] {τ : Type u_4} [Fintype τ] {f : σ → τ}, Function.Injective f → ∀ (r : τ → ℕ) (d : σ →₀ ℕ), Roth.weight r (Finsupp.mapDomain f d) = Roth.weight (r ∘ f) d
```

- **What**: Weighted evaluation of a multi-index is preserved by injective relabelling with pulled-back denominator parameters; actually arbitrary maps work.
- **How**: Original proof applies sum_mapDomain_index_inj then normalizes Finsupp.sum to the finite ambient sum. Re-aimed proof is exact existing linearCombination_mapDomain.
- **Hypotheses**: Fintype σ and Fintype τ required by fixed parent weight interface; Injective f removable, natively verified; no DecidableEq, positivity, or nonzero denominator assumptions
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_rename`, `Roth.card_filter_fiber_eq`, `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 127–130; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_mapDomain.md).

#### File structural summary

- Written declarations: 14; kinds: {'def': 2, 'theorem': 12}
- **Key API (at least three lexical callers)**: `Roth.box`, `Roth.mem_box`, `Roth.card_box`, `Roth.weight`, `Roth.weight_nonneg`, `Roth.weight_add`, `Roth.weight_mapDomain`
- **Unused in file (observation)**: `Roth.card_le_card_box`, `Roth.weight_nonneg`, `Roth.weight_zero`, `Roth.weight_add`, `Roth.weight_eq_zero_iff`, `Roth.weight_single`, `Roth.weight_le_card`, `Roth.weight_mul_left`, `Roth.weight_le_degree_div`, `Roth.weight_mapDomain`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/CoeffNorm.lean

Completed assessments: 26/26.

#### def Roth.normOne

Type:

```lean
∀ {σ : Type u_1}, MvPolynomial σ ℤ → ℝ
```

- **What**: Coefficient ℓ¹ norm / length of an integer multivariate polynomial: finite sum of real absolute coefficient values.
- **How**: One support sum; definitionally equal to P.coeff.sum (fun _ z : ℤ ↦ |(z : ℝ)|), existing Finsupp.sum.
- **Hypotheses**: Arbitrary universe-polymorphic variable type σ and integer-coefficient polynomial; no Fintype, DecidableEq, nonzero or degree hypotheses.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.normOne_nonneg`, `Roth.normOne_eq_sum_of_support_subset`, `Roth.normOne_monomial`, `Roth.normOne_zero`, `Roth.abs_coeff_le_normOne`, `Roth.normOne_add_le`, `Roth.normOne_neg`, `Roth.normOne_sum_le`, `Roth.normOne_mul_le`, `Roth.normOne_prod_le`, `Roth.normOne_le_card_mul`, `Roth.normOne_det_le`, `Roth.normOne_hasseDeriv_le`, `Roth.abs_coeff_det_hasseDeriv_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 47–47; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne.md).

#### def Roth.diag

Type:

```lean
∀ {σ : Type u_1}, MvPolynomial σ ℤ → Polynomial ℤ
```

- **What**: Diagonal specialization: replace all variables by a common polynomial indeterminate, adding coefficients when total exponents collide.
- **How**: One existing MvPolynomial.aeval application to constant Polynomial.X, exact rfl recovery. Alternative rename-to-PUnit then uniqueAlgEquiv is proved equal, not claimed defeq.
- **Hypotheses**: Arbitrary variable type σ and integer polynomial; no finiteness, DecidableEq, nonzero or degree assumptions.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.diag_eq_sum`, `Roth.abs_coeff_diag_le`, `Roth.natDegree_diag_le`, `Roth.eval_diag`, `Roth.diag_sub`
- **Used by other files (lexical)**: `Roth.exists_ne_modByMonic_eq`, `Roth.eval_hasseDeriv_sub_eq_zero`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- **Visibility**: public
- **Lines**: 161–161; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.diag.md).

#### theorem Roth.normOne_nonneg

Type:

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ), 0 ≤ Roth.normOne P
```

- **What**: Nonnegativity of integer polynomial coefficient ℓ¹ norm.
- **How**: Finite sum of nonnegative real absolute values; exactly Finset.sum_nonneg + abs_nonneg.
- **Hypotheses**: Arbitrary universe-polymorphic variable type and polynomial. No Fintype, DecidableEq, nonzero, degree or sign assumptions.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: []
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_prod_le`, `Roth.normOne_det_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 50–51; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_nonneg.md).

#### theorem Roth.normOne_eq_sum_of_support_subset

Type:

```lean
∀ {σ : Type u_1} {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)}, P.support ⊆ s → Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)|
```

- **What**: Coefficient ℓ¹ norm can be computed on any finite superset of polynomial support.
- **How**: Add only terms whose coefficient is zero; existing Finsupp.sum_of_support_subset specializes exactly after Int.cast_zero and abs_zero.
- **Hypotheses**: Arbitrary universe-polymorphic variable type; implicit integer polynomial and finite exponent set; support inclusion. No finite-variable, degree, norm-instance, sign or nonzero assumptions.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: []
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_monomial`, `Roth.normOne_add_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 54–56; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_eq_sum_of_support_subset.md).

#### theorem Roth.normOne_monomial

Type:

```lean
∀ {σ : Type u_1} (e : σ →₀ ℕ) (c : ℤ), Roth.normOne (MvPolynomial.monomial e c) = |(c : ℝ)|
```

- **What**: Coefficient ℓ¹ norm of a monomial is the absolute value of its coefficient, including zero.
- **How**: Single nonzero position, or empty support when coefficient zero; existing sum_monomial_eq applies directly with absolute-value cast size and explicit zero normalization.
- **Hypotheses**: Arbitrary universe-polymorphic variable type σ, exponent e : σ →₀ ℕ and c : ℤ. No finite variable, degree, coefficient nonzero or positivity hypotheses.
- **Uses from project (lexical body)**: `Roth.normOne_eq_sum_of_support_subset`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`, `Roth.normOne_eq_sum_of_support_subset`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_mul_le`, `Roth.normOne_prod_le`, `Roth.normOne_hasseDeriv_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 59–62; proof/body length 4 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_monomial.md).

#### theorem Roth.normOne_zero

Type:

```lean
∀ {σ : Type u_1}, Roth.normOne (0 : MvPolynomial σ ℤ) = 0
```

- **What**: The zero integer multivariate polynomial has coefficient ℓ¹ norm zero.
- **How**: Empty coefficient support; direct existing Finsupp.sum_zero_index specialization is definitionally the project statement.
- **Hypotheses**: Only arbitrary universe-polymorphic σ. No Fintype, DecidableEq, degree, positivity or size-zero assumption.
- **Uses from project (lexical body)**: `Roth.normOne`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_sum_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 66–67; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_zero.md).

#### theorem Roth.abs_coeff_le_normOne

Type:

```lean
∀ {σ : Type u_2} (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ Roth.normOne P
```

- **What**: Every integer multivariate polynomial coefficient has absolute real value bounded by its coefficient ℓ1 sum.
- **How**: Direct Finsupp.single_eval_le_sum specialization, g z = |(z : ℝ)|; zero and nonnegativity are elementary abs facts.
- **Hypotheses**: No explicit hypotheses or typeclasses on σ; σ universe-polymorphic, P and d arbitrary. Integer coefficients and real output fixed by normOne.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: []
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.abs_coeff_det_hasseDeriv_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 71–73; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_le_normOne.md).

#### theorem Roth.normOne_add_le

Type:

```lean
∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q
```

- **What**: The coefficient absolute sum of P+Q is bounded by the sum of their coefficient lengths.
- **How**: Pad all three coefficient sums to the union of supports and sum the scalar absolute-value triangle inequality.
- **Hypotheses**: Arbitrary variable type σ; two integer polynomials P,Q. No finite-variable, degree, sign or coefficient-bound premise. Parent fixes integer coefficients and real-valued absolute sum.
- **Uses from project (lexical body)**: `Roth.normOne_eq_sum_of_support_subset`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`, `Roth.normOne_eq_sum_of_support_subset`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_sum_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 77–83; proof/body length 7 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_add_le.md).

#### theorem Roth.normOne_neg

Type:

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ), Roth.normOne (-P) = Roth.normOne P
```

- **What**: Negating an integer multivariate polynomial preserves its coefficient l1 length.
- **How**: Negation preserves support and absolute values; existing Finsupp negation reindexing supplies the abstract law.
- **Hypotheses**: Arbitrary σ and integer polynomial P, no additional assumptions. Parent fixes coefficient/output types.
- **Uses from project (lexical body)**: `Roth.normOne`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_det_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 86–87; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_neg.md).

#### theorem Roth.normOne_sum_le

Type:

```lean
∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ), Roth.normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, Roth.normOne (f i)
```

- **What**: The coefficient ℓ1 size of a finite sum of integer multivariate polynomials is bounded by the sum of the coefficient sizes.
- **How**: Finset.le_sum_of_subadditive applied to normOne using project normOne_zero and normOne_add_le.
- **Hypotheses**: Arbitrary variable type σ, family index ι, finite set s and polynomial family f; no Fintype, DecidableEq, degree or coefficient bound assumptions.
- **Uses from project (lexical body)**: `Roth.normOne`, `Roth.normOne_add_le`, `Roth.normOne_zero`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`, `Roth.normOne_add_le`, `Roth.normOne_zero`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_mul_le`, `Roth.normOne_det_le`, `Roth.normOne_hasseDeriv_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 90–92; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_sum_le.md).

#### theorem Roth.normOne_mul_le

Type:

```lean
∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.normOne (P * Q) ≤ Roth.normOne P * Roth.normOne Q
```

- **What**: Coefficient L1 size of a product is at most the product of sizes.
- **How**: Expand convolution, apply finite triangle twice and monomial size, then factor double scalar sum.
- **Hypotheses**: Arbitrary variable type σ and integer polynomials P,Q; no additional hypotheses.
- **Uses from project (lexical body)**: `Roth.normOne`, `Roth.normOne_monomial`, `Roth.normOne_sum_le`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`, `Roth.normOne_monomial`, `Roth.normOne_sum_le`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_prod_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 96–102; proof/body length 7 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_mul_le.md).

#### theorem Roth.normOne_prod_le

Type:

```lean
∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ), Roth.normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, Roth.normOne (f i)
```

- **What**: Coefficient L1 of a finite product is bounded by the product of coefficient L1 sizes.
- **How**: Existing Finset nonnegative submultiplicative-map induction, using project nonnegative/unit/binary witnesses.
- **Hypotheses**: Arbitrary variable and index types σ,ι; any finite s and polynomial family f; ℤ/ℝ fixed by normOne.
- **Uses from project (lexical body)**: `Roth.normOne`, `Roth.normOne_monomial`, `Roth.normOne_mul_le`, `Roth.normOne_nonneg`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`, `Roth.normOne_monomial`, `Roth.normOne_mul_le`, `Roth.normOne_nonneg`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.normOne_det_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 105–108; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_prod_le.md).

#### theorem Roth.normOne_le_card_mul

Type:

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) {B : ℝ}, (∀ (d : σ →₀ ℕ), |((P.coeff d : ℤ) : ℝ)| ≤ B) → Roth.normOne P ≤ (P.support.card : ℝ) * B
```

- **What**: Coefficient ℓ¹ sum bounded by support size times uniform coefficient bound.
- **How**: Direct specialization of Finset.sum_le_card_nsmul; unfold normOne and rewrite nsmul_eq_mul.
- **Hypotheses**: Arbitrary variable type; integer coefficients and real bound fixed by normOne interface; global coefficient bound can weaken to support-only.
- **Uses from project (lexical body)**: `Roth.normOne`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.abs_coeff_det_hasseDeriv_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 113–115; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_le_card_mul.md).

#### theorem Roth.normOne_det_le

Type:

```lean
∀ {σ : Type u_1} {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ}, (∀ μ ν, Roth.normOne (M μ ν) ≤ C) → Roth.normOne M.det ≤ ↑l.factorial * C ^ l
```

- **What**: Bounds coefficient L1 size of an l×l polynomial determinant by l! C^l.
- **How**: Leibniz expansion, subadditive finite sum, sign invariance, submultiplicative finite product, entrywise monotonicity, count permutations.
- **Hypotheses**: Arbitrary variables σ and l; all entries size≤C; C unrestricted; includes empty matrix.
- **Uses from project (lexical body)**: `Roth.normOne`, `Roth.normOne_neg`, `Roth.normOne_nonneg`, `Roth.normOne_prod_le`, `Roth.normOne_sum_le`
- **Project references in type**: `Roth.normOne`
- **Native direct body references**: `Roth.normOne`, `Roth.normOne_neg`, `Roth.normOne_nonneg`, `Roth.normOne_prod_le`, `Roth.normOne_sum_le`
- **Native direct type references**: `Roth.normOne`
- **Used by in file (lexical)**: `Roth.abs_coeff_det_hasseDeriv_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 119–128; proof/body length 9 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_det_le.md).

#### theorem Roth.abs_coeff_hasseDeriv_le

Type:

```lean
∀ {σ : Type u_1} [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}, (∀ j, MvPolynomial.degreeOf j P ≤ r j) → ∀ {B : ℝ}, (∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B) → ∀ e, |(((MvPolynomial.hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B
```

- **What**: Every coefficient of a multivariate Hasse derivative is bounded by 2^(sum coordinate degree bounds) times an input coefficient bound.
- **How**: Coefficient extraction has one preimage e+d; split membership in input support, bound binomial product, multiply coefficient bound, handle zero coefficients.
- **Hypotheses**: Arbitrary finite variable type; integer polynomial; coordinate degree bounds r; real coefficient bound B; no B≥0 assumption because hB implies it.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_le_two_pow`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_le_two_pow`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.abs_eval_iterated_hasseDeriv_lt_aux`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
- **Visibility**: public
- **Lines**: 134–143; proof/body length 8 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_hasseDeriv_le.md).

#### theorem Roth.normOne_hasseDeriv_le

Type:

```lean
∀ {σ : Type u_2} [inst : Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) → normOne ((hasseDeriv d) P) ≤ (2 ^ ∑ j, r j) * normOne P
```

- **What**: Hasse derivative has coefficient ℓ¹ size at most 2 to sum of coordinate degree bounds times original size.
- **How**: Expand derivative into monomials, apply finite triangle inequality, bound each binomial product and sum.
- **Hypotheses**: Fintype σ; arbitrary derivative multi-index; integer polynomial with degreeOf j P ≤ r j.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff_le_two_pow`, `MvPolynomial.hasseDeriv_apply`, `Roth.normOne`, `Roth.normOne_monomial`, `Roth.normOne_sum_le`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.normOne`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_le_two_pow`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_apply`, `Roth.normOne`, `Roth.normOne_monomial`, `Roth.normOne_sum_le`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.normOne`
- **Used by in file (lexical)**: `Roth.abs_coeff_det_hasseDeriv_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 148–157; proof/body length 9 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_hasseDeriv_le.md).

#### theorem Roth.diag_eq_sum

Type:

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ),
  Roth.diag P = ∑ k ∈ P.support, (monomial (Finsupp.degree k)) (P.coeff k)
```

- **What**: Diagonal substitution sends each coefficient monomial to a univariate monomial at total degree.
- **How**: Unfold diag/aeval, use eval₂_eq, collapse product of powers, identify total exponent and polynomial monomial.
- **Hypotheses**: Arbitrary variable type σ and integer polynomial P; no finiteness, degree, or nonzero hypotheses.
- **Uses from project (lexical body)**: `Roth.diag`
- **Project references in type**: `Roth.diag`
- **Native direct body references**: `Roth.diag`
- **Native direct type references**: `Roth.diag`
- **Used by in file (lexical)**: `Roth.abs_coeff_diag_le`, `Roth.natDegree_diag_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 164–168; proof/body length 4 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.diag_eq_sum.md).

#### theorem Roth.abs_coeff_diag_le

Type:

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) {B : ℝ},
  (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) → ∀ (n : ℕ), |↑((Roth.diag P).coeff n)| ≤ ↑P.support.card * B
```

- **What**: Each coefficient after identifying all variables is bounded by input support cardinality times a uniform input coefficient bound.
- **How**: Expand diagonal polynomial into monomials; coefficient linearity and integer cast give finite sum; triangle inequality and sum≤card·B finish, treating off-degree terms as zero.
- **Hypotheses**: Arbitrary σ, integer polynomial P, real B with every input coefficient bounded in cast absolute value, arbitrary output index n; hB implies B≥0.
- **Uses from project (lexical body)**: `Roth.diag_eq_sum`
- **Project references in type**: `Roth.diag`
- **Native direct body references**: `Roth.diag`, `Roth.diag_eq_sum`
- **Native direct type references**: `Roth.diag`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
- **Visibility**: public
- **Lines**: 174–179; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_le.md).

#### theorem Roth.natDegree_diag_le

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ}, (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) → (Roth.diag P).natDegree ≤ ∑ j, r j
```

- **What**: Diagonal substitution has degree at most the sum of coordinate degree bounds.
- **How**: Expand into monomials and sum exponent bounds; independently verified existing aeval total-degree route with multiset-count bridge.
- **Hypotheses**: arbitrary variable universe σ; Fintype σ for sum; P integer polynomial; r natural coordinate bounds; ∀j, degreeOf j P≤r j
- **Uses from project (lexical body)**: `Roth.diag_eq_sum`
- **Project references in type**: `Roth.diag`
- **Native direct body references**: `Roth.diag`, `Roth.diag_eq_sum`
- **Native direct type references**: `Roth.diag`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
- **Visibility**: public
- **Lines**: 183–189; proof/body length 6 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.natDegree_diag_le.md).

#### theorem Roth.eval_diag

Type:

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) (x : ℝ), Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (Roth.diag P)) = MvPolynomial.eval (fun _ ↦ x) (MvPolynomial.map (Int.castRingHom ℝ) P)
```

- **What**: Evaluation of diagonal substitution equals evaluation at the diagonal tuple after coefficient cast.
- **How**: Original polynomial induction; exact replacement specializes existing comp_aeval_apply and transports eval/map into aeval.
- **Hypotheses**: σ arbitrary Type*; P arbitrary integer multivariate polynomial; x arbitrary real; no hypotheses/Fintype.
- **Uses from project (lexical body)**: `Roth.diag`
- **Project references in type**: `Roth.diag`
- **Native direct body references**: `Roth.diag`
- **Native direct type references**: `Roth.diag`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 193–196; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.eval_diag.md).

#### theorem Roth.diag_sub

Type:

```lean
∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.diag (P - Q) = Roth.diag P - Roth.diag Q
```

- **What**: Diagonal substitution preserves subtraction.
- **How**: One generic map_sub application to MvPolynomial.aeval.
- **Hypotheses**: Arbitrary variable type; integer coefficients fixed by parent diag; two arbitrary polynomials.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.diag`
- **Native direct body references**: []
- **Native direct type references**: `Roth.diag`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.eval_hasseDeriv_sub_eq_zero`
- **Visibility**: public
- **Lines**: 199–200; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.diag_sub.md).

#### theorem Roth.geom_sum_le_one_add_pow

Type:

```lean
∀ {t : ℝ}, 0 ≤ t → ∀ (r : ℕ), ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r
```

- **What**: Nonnegative finite geometric sum bounded by binomial power.
- **How**: Expand using add_pow and compare positive-binomial-coefficient summands.
- **Hypotheses**: t nonnegative; natural r. Real ambient type weakens to Semiring/PartialOrder/IsOrderedRing.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.sum_box_prod_pow_le_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 205–211; proof/body length 6 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.geom_sum_le_one_add_pow.md).

#### theorem Roth.sum_box_prod_pow_le_aux

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) {B : ℝ},
  0 ≤ B → ∀ (x : σ → ℝ), ∑ k ∈ Roth.box r, B * ∏ j, |x j| ^ k j ≤ B * ∏ j, (1 + |x j|) ^ r j
```

- **What**: The weighted sum of products of absolute powers over a rectangular box is bounded by the corresponding binomial product.
- **How**: Factors the box sum using Finset.prod_univ_sum and applies geom_sum_le_one_add_pow independently in each coordinate.
- **Hypotheses**: A finite variable enumeration, a nonnegative common factor B, natural degree bounds, and real coordinates. Native original/replay types have no external DecidableEq or nonzero assumptions.
- **Uses from project (lexical body)**: `Roth.box`, `Roth.geom_sum_le_one_add_pow`
- **Project references in type**: `Roth.box`
- **Native direct body references**: `Roth.box`, `Roth.geom_sum_le_one_add_pow`
- **Native direct type references**: `Roth.box`
- **Used by in file (lexical)**: `Roth.abs_eval_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 214–218; proof/body length 4 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_box_prod_pow_le_aux.md).

#### theorem Roth.abs_eval_le

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    ∀ {B : ℝ},
      (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
        ∀ (x : σ → ℝ), |(MvPolynomial.eval x) ((MvPolynomial.map (Int.castRingHom ℝ)) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j
```

- **What**: An integer multivariate polynomial with common absolute coefficient bound B and coordinate degrees at most r has value at x at most B times the product of (1+|x_j|)^r_j.
- **How**: Expand evaluation, take the finite-sum triangle inequality, enlarge support to Roth.box using monomial_le_degreeOf and Roth.mem_box, and apply private Roth.sum_box_prod_pow_le_aux to factor the geometric majorant.
- **Hypotheses**: A finite variable type, an integer polynomial, coordinate natural degree bounds, a common real absolute coefficient bound, and any real evaluation point; B≥0 follows from hB at zero.
- **Uses from project (lexical body)**: `Roth.box`, `Roth.mem_box`, `Roth.sum_box_prod_pow_le_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.box`, `Roth.mem_box`, `Roth.sum_box_prod_pow_le_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.abs_eval_iterated_hasseDeriv_lt_aux`
- **Visibility**: public
- **Lines**: 223–239; proof/body length 15 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_le.md).

#### theorem Roth.degreeOf_det_hasseDeriv_le

Type:

```lean
∀ {σ : Type u_1} {l : ℕ} (E : Fin l → Fin l → σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}, (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) → ∀ (j : σ), MvPolynomial.degreeOf j (Matrix.of fun μ ν ↦ (MvPolynomial.hasseDeriv (E μ ν)) P).det ≤ l * r j
```

- **What**: A determinant of l×l Hasse derivatives of a polynomial of coordinate degrees ≤r has coordinate degrees ≤l*r.
- **How**: Expand determinant; degree of sum bounded by supremum; constants do not increase degree; products bounded by sums; Hasse derivatives do not increase coordinate degrees.
- **Hypotheses**: Arbitrary σ, l, E and P over ℤ; global coordinate upper bound hP; no nonzero, finite-variable or derivative-order restriction.
- **Uses from project (lexical body)**: `MvPolynomial.degreeOf_hasseDeriv_le`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.exists_det_eq_mul`
- **Visibility**: public
- **Lines**: 245–253; proof/body length 7 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_det_hasseDeriv_le.md).

#### theorem Roth.abs_coeff_det_hasseDeriv_le

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {l : ℕ} (E : Fin l → Fin l → σ →₀ ℕ)
  (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    ∀ {B : ℝ},
      0 ≤ B →
        (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
          ∀ (d : σ →₀ ℕ),
            |↑((Matrix.of fun μ ν ↦ (MvPolynomial.hasseDeriv (E μ ν)) P).det.coeff d)| ≤
              (∏ j, (↑(r j) + 1)) ^ l * ↑l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)
```

- **What**: Every coefficient of an l×l determinant of arbitrary Hasse derivatives of P is bounded by N^l*l!*B^l*2^(S*l), N=∏(rj+1), S=∑rj.
- **How**: Apply abs_coeff_le_normOne, normOne_det_le and normOne_hasseDeriv_le; normOne_le_card_mul and card_le_card_box control the input size before scalar normalization.
- **Hypotheses**: Arbitrary finite variable type, natural matrix size including0, arbitrary derivative-index array and exponent; degree and coefficient bounds; explicit hB0 is redundant.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_le_normOne`, `Roth.card_le_card_box`, `Roth.normOne`, `Roth.normOne_det_le`, `Roth.normOne_hasseDeriv_le`, `Roth.normOne_le_card_mul`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_le_normOne`, `Roth.card_le_card_box`, `Roth.normOne`, `Roth.normOne_det_le`, `Roth.normOne_hasseDeriv_le`, `Roth.normOne_le_card_mul`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_det_le`
- **Visibility**: public
- **Lines**: 258–272; proof/body length 11 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_det_hasseDeriv_le.md).

#### File structural summary

- Written declarations: 26; kinds: {'def': 2, 'theorem': 24}
- **Key API (at least three lexical callers)**: `Roth.normOne`, `Roth.normOne_monomial`, `Roth.normOne_sum_le`, `Roth.diag`
- **Unused in file (observation)**: `Roth.abs_coeff_hasseDeriv_le`, `Roth.abs_coeff_diag_le`, `Roth.natDegree_diag_le`, `Roth.eval_diag`, `Roth.diag_sub`, `Roth.abs_eval_le`, `Roth.degreeOf_det_hasseDeriv_le`, `Roth.abs_coeff_det_hasseDeriv_le`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/GenWronskian.lean

Completed assessments: 19/19.

#### def Roth.genWronskian

Type:

```lean
∀ {K : Type u_1} [Field K] {σ : Type u_2} {l : ℕ}, (Fin l → σ →₀ ℕ) → (Fin l → MvPolynomial σ K) → MvPolynomial σ K
```

- **What**: Generalized Hasse Wronskian of a finite polynomial family, with selected row multiorders.
- **How**: Determinant of the square matrix (μ,ν) ↦ hasseDeriv (D μ) (φ ν).
- **Hypotheses**: Field K (can weaken to CommRing); arbitrary variables σ, no Fintype parameter; finite square family Fin l, can generalize to arbitrary Fintype index with DecidableEq; no independence, order bound, nonemptiness or characteristic restriction
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`
- **Project references in type**: []
- **Native direct body references**: `MvPolynomial.hasseDeriv`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.genWronskian_eq_zero_of_not_linearIndependent`, `Roth.wronskian_kronecker_eq_sum_aux`, `Roth.exists_genWronskian_ne_zero`
- **Used by other files (lexical)**: `Roth.det_hasseDeriv_separated`, `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Visibility**: public
- **Lines**: 32–34; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.genWronskian.md).

#### def Roth.kronecker

Type:

```lean
∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ], ℕ → MvPolynomial σ K →ₐ[K] Polynomial K
```

- **What**: Chosen-enumeration Kronecker power substitution from multivariate to univariate polynomials.
- **How**: Existing MvPolynomial.aeval with generator j mapped to Polynomial.X ^ k ^ rank(j).
- **Hypotheses**: Field K, definition weakens to CommSemiring; Fintype σ supplies chosen enumeration; explicit weights require no finite variable type; k arbitrary natural; no degree/injectivity/characteristic hypotheses
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.kronecker_monomial`, `Roth.coeff_kronecker`, `Roth.kronecker_eq_zero_iff`, `Roth.linearIndependent_kronecker`, `Roth.kronHasse`, `Roth.derivative_kronHasse_aux`, `Roth.hasseDeriv_kronecker_mem`, `Roth.exists_hasseDeriv_kronecker_eq_sum`, `Roth.wronskian_kronecker_eq_sum_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 53–54; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronecker.md).

#### def Roth.kroneckerExp

Type:

```lean
∀ {σ : Type u_1} [Fintype σ], ℕ → (σ →₀ ℕ) → ℕ
```

- **What**: Natural positional exponent sum for Kronecker substitution under the chosen finite enumeration.
- **How**: Sums d j * k ^ rank(j); existing Finsupp.weight specializes with power weights, independently of any coefficient field.
- **Hypotheses**: Fintype σ supplies finite summation and chosen equivFin enumeration; k arbitrary natural, d finitely supported natural exponent vector; No K, Field K, l, characteristic, base lower bound, or digit bound in elaborated type
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.kronecker_monomial`, `Roth.kroneckerExp_injOn`, `Roth.coeff_kronecker`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 57–57; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp.md).

#### def Roth.kronHasse

Type:

```lean
{K : Type u_1} →
  [inst : Field K] → {σ : Type u_2} → [Fintype σ] → ℕ → (σ →₀ ℕ) → MvPolynomial σ K → Polynomial K
```

- **What**: Composes a multivariate Hasse derivative with Kronecker substitution, as a polynomial-valued function.
- **How**: Composes hasseDeriv pointwise with kronecker; represented as a function into univariate polynomials.
- **Hypotheses**: A field, a finite variable enumeration, a base, and a derivative multi-index. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.kronecker`
- **Project references in type**: []
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.kronecker`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.kronSpan`, `Roth.derivative_kronHasse_aux`, `Roth.hasseDeriv_kronecker_mem`, `Roth.exists_hasseDeriv_kronecker_eq_sum`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 145–146; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronHasse.md).

#### def Roth.kronSpan

Type:

```lean
{K : Type u_1} →
  [inst : Field K] →
    {σ : Type u_2} → [Fintype σ] → ℕ → ℕ → Submodule (Polynomial K) (MvPolynomial σ K → Polynomial K)
```

- **What**: The polynomial-module span of substituted Hasse operators with total order at most the natural bound.
- **How**: Uses Submodule.span of the image of kronHasse over the degree-bounded exponent set.
- **Hypotheses**: A field, finite variable enumeration, and natural base and order bound. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- **Uses from project (lexical body)**: `Roth.kronHasse`
- **Project references in type**: []
- **Native direct body references**: `Roth.kronHasse`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.derivative_mem_kronSpan`, `Roth.hasseDeriv_kronecker_mem`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 149–151; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronSpan.md).

#### theorem Roth.genWronskian_eq_zero_of_not_linearIndependent

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} {l : ℕ} (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ K}, ¬LinearIndependent K φ → Roth.genWronskian D φ = 0
```

- **What**: Linearly dependent polynomial families have zero generalized Hasse Wronskian for every row multi-index.
- **How**: Extract a nontrivial constant relation, transport through each linear Hasse operator, and apply the domain matrix kernel criterion.
- **Hypotheses**: Field K; arbitrary σ, no Fintype/Finite assumption; D : Fin l → σ →₀ ℕ; φ : Fin l → MvPolynomial σ K; ¬LinearIndependent K φ
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`
- **Project references in type**: `Roth.genWronskian`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.genWronskian`
- **Native direct type references**: `Roth.genWronskian`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 41–49; proof/body length 8 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.genWronskian_eq_zero_of_not_linearIndependent.md).

#### theorem Roth.kronecker_monomial

Type:

```lean
∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) (a : K), Roth.kronecker k (MvPolynomial.monomial d a) = Polynomial.C a * Polynomial.X ^ Roth.kroneckerExp k d
```

- **What**: Computes the image of a coefficient-bearing monomial under geometric-power Kronecker substitution.
- **How**: Specializes MvPolynomial.aeval_monomial and normalizes product of powers to a power with weighted-sum exponent.
- **Hypotheses**: Field K and Fintype σ belong to fixed parent interfaces; Arbitrary natural k and finitely supported natural d; arbitrary a; No lower-base bound, digit bound, CharZero or l parameter
- **Uses from project (lexical body)**: `Roth.kronecker`, `Roth.kroneckerExp`
- **Project references in type**: `Roth.kronecker`, `Roth.kroneckerExp`
- **Native direct body references**: `Roth.kronecker`, `Roth.kroneckerExp`
- **Native direct type references**: `Roth.kronecker`, `Roth.kroneckerExp`
- **Used by in file (lexical)**: `Roth.coeff_kronecker`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 60–63; proof/body length 3 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronecker_monomial.md).

#### theorem Roth.kroneckerExp_injOn

Type:

```lean
∀ {σ : Type u} [Fintype σ] {k : ℕ}, 1 < k → Set.InjOn (Roth.kroneckerExp k) {d | ∀ j : σ, d j < k}
```

- **What**: Uniqueness of bounded positional natural exponent vectors under Kronecker weighted sum.
- **How**: Convert enumerated Finsupp digits to List.ofFn, identify weighted sum with Nat.ofDigits, apply equal-length digit uniqueness, and transport list equality back.
- **Hypotheses**: Arbitrary universe σ, Fintype σ supplies canonical enumeration; Natural k and 1<k; hk verified removable even at original interface; Coordinate digits strictly less than k; no coefficient field or family-size parameter
- **Uses from project (lexical body)**: `Roth.kroneckerExp`
- **Project references in type**: `Roth.kroneckerExp`
- **Native direct body references**: `Roth.kroneckerExp`
- **Native direct type references**: `Roth.kroneckerExp`
- **Used by in file (lexical)**: `Roth.coeff_kronecker`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 69–82; proof/body length 13 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp_injOn.md).

#### theorem Roth.coeff_kronecker

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {k : ℕ},
  1 < k →
    ∀ {P : MvPolynomial σ K},
      (∀ (j : σ), MvPolynomial.degreeOf j P < k) →
        ∀ {d : σ →₀ ℕ}, (∀ (j : σ), d j < k) → ((Roth.kronecker k) P).coeff (Roth.kroneckerExp k d) = P.coeff d
```

- **What**: Bounded Kronecker substitution preserves each admissible monomial coefficient.
- **How**: Expand P.as_sum through kronecker_monomial, then use Finset.sum_eq_single and kroneckerExp_injOn to isolate the uniquely encoded bounded exponent.
- **Hypotheses**: Field K; Fintype sigma; 1 < k; each partial degree of P < k; each entry of d < k
- **Uses from project (lexical body)**: `Roth.kroneckerExp_injOn`, `Roth.kronecker_monomial`
- **Project references in type**: `Roth.kronecker`, `Roth.kroneckerExp`
- **Native direct body references**: `Roth.kronecker`, `Roth.kroneckerExp`, `Roth.kroneckerExp_injOn`, `Roth.kronecker_monomial`
- **Native direct type references**: `Roth.kronecker`, `Roth.kroneckerExp`
- **Used by in file (lexical)**: `Roth.kronecker_eq_zero_iff`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 88–100; proof/body length 12 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_kronecker.md).

#### theorem Roth.kronecker_eq_zero_iff

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {k : ℕ},
  1 < k → ∀ {P : MvPolynomial σ K}, (∀ (j : σ), MvPolynomial.degreeOf j P < k) → ((Roth.kronecker k) P = 0 ↔ P = 0)
```

- **What**: The Kronecker substitution detects zero under individual-degree bounds.
- **How**: Every support exponent lies in the bounded radix box; coefficient recovery prevents cancellation. Reverse direction is map_zero.
- **Hypotheses**: Field K; Fintype σ; k : ℕ; 1 < k; P : MvPolynomial σ K; ∀ j, degreeOf j P < k
- **Uses from project (lexical body)**: `Roth.coeff_kronecker`
- **Project references in type**: `Roth.kronecker`
- **Native direct body references**: `Roth.coeff_kronecker`, `Roth.kronecker`, `Roth.kroneckerExp`
- **Native direct type references**: `Roth.kronecker`
- **Used by in file (lexical)**: `Roth.linearIndependent_kronecker`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 106–111; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronecker_eq_zero_iff.md).

#### theorem Roth.linearIndependent_kronecker

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {l k : ℕ},
  1 < k →
    ∀ {φ : Fin l → MvPolynomial σ K},
      (∀ (ν : Fin l) (j : σ), MvPolynomial.degreeOf j (φ ν) < k) →
        LinearIndependent K φ → LinearIndependent K fun ν ↦ (Roth.kronecker k) (φ ν)
```

- **What**: Kronecker substitution preserves linear independence of a family whose individual variable degrees are below the base.
- **How**: Pull scalar relations back using degree-bounded zero detection. Verified alternate proof puts the family span inside AddMonoidAlgebra.supported, uses restricted monomial-evaluation injectivity, then existing LinearIndependent.map_injOn.
- **Hypotheses**: coefficients: Field K in current parent interface; CommSemiring after reaim; variables: Fintype σ for chosen enumeration; arbitrary σ with weights or explicit e:σ≃Fin n; family: Fin l current; arbitrary index verified; base: 1<k current; hypothesis removable in support-based proof; bounds: ∀i j, degreeOf j (φ i)<k, or support containment in separated S; independence: LinearIndependent coefficients φ remains essential
- **Uses from project (lexical body)**: `Roth.kronecker_eq_zero_iff`
- **Project references in type**: `Roth.kronecker`
- **Native direct body references**: `Roth.kronecker`, `Roth.kronecker_eq_zero_iff`
- **Native direct type references**: `Roth.kronecker`
- **Used by in file (lexical)**: `Roth.exists_genWronskian_ne_zero`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 117–127; proof/body length 9 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_kronecker.md).

#### theorem Roth.derivative_aeval

Type:

```lean
@Roth.derivative_aeval : ∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] (γ : σ → Polynomial K)
  (P : MvPolynomial σ K),
  Polynomial.derivative ((MvPolynomial.aeval γ) P) =
    ∑ j, Polynomial.derivative (γ j) * (MvPolynomial.aeval γ) ((MvPolynomial.pderiv j) P)
```

- **What**: Algebraic multivariate chain rule for polynomial coordinate substitution.
- **How**: Polynomial induction on constants, addition and multiplication by one variable; simplification uses Leibniz.
- **Hypotheses**: Field K (verified weakenable to CommSemiring R); Fintype σ for the univ-sum spelling; Arbitrary γ : σ → Polynomial K and P : MvPolynomial σ K; No CharZero or l parameter
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.derivative_kronHasse_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 133–142; proof/body length 8 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.derivative_aeval.md).

#### lemma Roth.derivative_kronHasse_aux

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] (k : ℕ) (d : σ →₀ ℕ),
  (fun P ↦ Polynomial.derivative (Roth.kronHasse✝ k d P)) =
    ∑ j,
      (Polynomial.derivative (Polynomial.X ^ k ^ ↑((Fintype.equivFin σ) j)) * Polynomial.C ↑(d j + 1)) •
        Roth.kronHasse✝ k (d + Finsupp.single j 1)
```

- **What**: Differentiating a substituted Hasse operator is a polynomial-coefficient sum of next-order substituted Hasse operators.
- **How**: Combines derivative_aeval with pderiv_hasseDeriv, moving the scalar coefficient through kronecker.
- **Hypotheses**: A field, finite variable enumeration, and arbitrary base and derivative exponent. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- **Uses from project (lexical body)**: `MvPolynomial.pderiv_hasseDeriv`, `Roth.derivative_aeval`, `Roth.kronHasse`, `Roth.kronecker`
- **Project references in type**: `Roth.kronHasse`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.pderiv_hasseDeriv`, `Roth.derivative_aeval`, `Roth.kronHasse`
- **Native direct type references**: `Roth.kronHasse`
- **Used by in file (lexical)**: `Roth.derivative_mem_kronSpan`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 153–160; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.derivative_kronHasse_aux.md).

#### lemma Roth.derivative_mem_kronSpan

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K},
  F ∈ Roth.kronSpan✝ k μ → (fun P ↦ Polynomial.derivative (F P)) ∈ Roth.kronSpan✝ k (μ + 1)
```

- **What**: Ordinary differentiation sends every operator in the order-mu substituted Hasse span into the order-(mu+1) span.
- **How**: Uses Submodule.span_induction: derivative_kronHasse_aux handles generators; sums are preserved; Polynomial.derivative_mul handles scalar multiplication, and span_mono embeds old-order operators.
- **Hypotheses**: A field and finite variable enumeration; the operator lies in kronSpan k μ. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- **Uses from project (lexical body)**: `Roth.derivative_kronHasse_aux`, `Roth.kronSpan`
- **Project references in type**: `Roth.kronSpan`
- **Native direct body references**: `Roth.derivative_kronHasse_aux`, `Roth.kronHasse`, `Roth.kronSpan`
- **Native direct type references**: `Roth.kronSpan`
- **Used by in file (lexical)**: `Roth.hasseDeriv_kronecker_mem`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 162–188; proof/body length 25 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.derivative_mem_kronSpan.md).

#### lemma Roth.hasseDeriv_kronecker_mem

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] [CharZero K] (k μ : ℕ),
  (fun P ↦ (Polynomial.hasseDeriv μ) ((Roth.kronecker k) P)) ∈ Roth.kronSpan✝ k μ
```

- **What**: Every univariate Hasse derivative of the Kronecker substitution operator lies in the corresponding bounded substituted-Hasse span.
- **How**: Inducts on μ, starts with the zero multi-index generator, uses derivative_mem_kronSpan, and divides by the nonzero successor integer via Polynomial.hasseDeriv_comp.
- **Hypotheses**: Characteristic zero field and a finite variable enumeration. Actual kernel type retains Field, Fintype sigma and CharZero; no positive-base or positive-order premise.
- **Uses from project (lexical body)**: `Roth.derivative_mem_kronSpan`, `Roth.kronHasse`, `Roth.kronSpan`, `Roth.kronecker`
- **Project references in type**: `Roth.kronSpan`, `Roth.kronecker`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero`, `Roth.derivative_mem_kronSpan`, `Roth.kronHasse`, `Roth.kronSpan`, `Roth.kronecker`
- **Native direct type references**: `Roth.kronSpan`, `Roth.kronecker`
- **Used by in file (lexical)**: `Roth.exists_hasseDeriv_kronecker_eq_sum`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 190–205; proof/body length 15 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_kronecker_mem.md).

#### theorem Roth.exists_hasseDeriv_kronecker_eq_sum

Type:

```lean
@Roth.exists_hasseDeriv_kronecker_eq_sum : ∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] [CharZero K] (k μ : ℕ), ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ K, Polynomial.hasseDeriv μ (Roth.kronecker k P) = ∑ d ∈ s, c d * Roth.kronecker k (MvPolynomial.hasseDeriv d P)
```

- **What**: Uniform finite polynomial linear combination of substituted multivariate Hasse derivatives of order at most μ for a Kronecker pullback.
- **How**: Extract supported Finsupp coefficients from private order-filtered span membership; membership uses derivative stability, induction and successor-scalar division.
- **Hypotheses**: Field K and CharZero K in original; Fintype σ fixes concrete Kronecker enumeration; arbitrary natural k and μ; no k>1, degree bounds or l
- **Uses from project (lexical body)**: `Roth.hasseDeriv_kronecker_mem`, `Roth.kronHasse`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.kronecker`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.hasseDeriv_kronecker_mem`, `Roth.kronHasse`, `Roth.kronecker`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.kronecker`
- **Used by in file (lexical)**: `Roth.exists_genWronskian_ne_zero`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 214–221; proof/body length 6 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_kronecker_eq_sum.md).

#### theorem Roth.det_sum_rows

Type:

```lean
@Roth.det_sum_rows {l : ℕ} {A : Type u_3} [CommRing A] {ι : Type u_4} (s : Fin l → Finset ι)
  (c : Fin l → ι → A) (N : Fin l → ι → Fin l → A) :
  (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det =
    ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det
```

- **What**: Expand determinant whose rows are finite linear combinations into finite choices, weighted by coefficient products.
- **How**: Specialize existing multilinear finite-sum law, extract simultaneous scalars, normalize function/matrix/scalar representations.
- **Hypotheses**: CommRing A; arbitrary A, no field/domain/characteristic condition; Fin l square matrix; arbitrary summand type ι; finite support per row; arbitrary s,c,N with no nonempty/nonzero assumptions
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.wronskian_kronecker_eq_sum_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 228–236; proof/body length 6 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.det_sum_rows.md).

#### lemma Roth.wronskian_kronecker_eq_sum_aux

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] {l : ℕ} (k : ℕ) (φ : Fin l → MvPolynomial σ K) (s : Fin l → Finset (σ →₀ ℕ))
  (c : Fin l → (σ →₀ ℕ) → Polynomial K),
  (∀ (μ ν : Fin l),
      (Polynomial.hasseDeriv ↑μ) ((Roth.kronecker k) (φ ν)) =
        ∑ d ∈ s μ, c μ d * (Roth.kronecker k) ((hasseDeriv d) (φ ν))) →
    (Roth.wronskian fun ν ↦ (Roth.kronecker k) (φ ν)) =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Roth.kronecker k) (Roth.genWronskian f φ)
```

- **What**: Expands the Wronskian after Kronecker substitution as a finite polynomial-coefficient sum of substituted generalized Wronskians, given the derivative-row expansions.
- **How**: Uses det_sum_rows and compatibility AlgHom.map_det to move Kronecker substitution through the determinant.
- **Hypotheses**: A field, finite variable enumeration, and supplied finite expansion formulas for each univariate derivative row. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.det_sum_rows`, `Roth.genWronskian`, `Roth.kronecker`, `Roth.wronskian`, `Roth.wronskianMatrix`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.genWronskian`, `Roth.kronecker`, `Roth.wronskian`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.det_sum_rows`, `Roth.genWronskian`, `Roth.kronecker`, `Roth.wronskian`, `Roth.wronskianMatrix`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.genWronskian`, `Roth.kronecker`, `Roth.wronskian`
- **Used by in file (lexical)**: `Roth.exists_genWronskian_ne_zero`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 238–245; proof/body length 4 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_kronecker_eq_sum_aux.md).

#### theorem Roth.exists_genWronskian_ne_zero

Type:

```lean
@Roth.exists_genWronskian_ne_zero.{u_1, u_2} {K : Type u_1} [Field K] {σ : Type u_2} {l : ℕ} [Finite σ] [CharZero K]
  {φ : Fin l → MvPolynomial σ K} (h : LinearIndependent K φ) :
  ∃ D, (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧ Roth.genWronskian D φ ≠ 0
```

- **What**: A linearly independent finite family of multivariate polynomials has a nonzero Hasse Wronskian with total derivative order at most each row index.
- **How**: Choose bounded Kronecker substitutions using exists_hasseDeriv_kronecker_eq_sum; combine linearIndependent_kronecker with wronskian_ne_zero_of_linearIndependent, and expand via wronskian_kronecker_eq_sum_aux to contradict vanishing of every candidate determinant.
- **Hypotheses**: Field K; CharZero K: essential for bounded row-order theorem; Finite σ: removable by verified finite-support restriction/rename proof; φ : Fin l → MvPolynomial σ K; LinearIndependent K φ; no positive l or nonempty σ assumption
- **Uses from project (lexical body)**: `Roth.exists_hasseDeriv_kronecker_eq_sum`, `Roth.linearIndependent_kronecker`, `Roth.wronskian_kronecker_eq_sum_aux`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Project references in type**: `Roth.genWronskian`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.exists_hasseDeriv_kronecker_eq_sum`, `Roth.genWronskian`, `Roth.kronecker`, `Roth.linearIndependent_kronecker`, `Roth.wronskian`, `Roth.wronskian_kronecker_eq_sum_aux`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Native direct type references**: `Roth.genWronskian`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Visibility**: public
- **Lines**: 254–270; proof/body length 15 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_genWronskian_ne_zero.md).

#### File structural summary

- Written declarations: 19; kinds: {'def': 5, 'theorem': 10, 'lemma': 4}
- **Key API (at least three lexical callers)**: `Roth.genWronskian`, `Roth.kronecker`, `Roth.kroneckerExp`, `Roth.kronHasse`
- **Unused in file (observation)**: `Roth.genWronskian_eq_zero_of_not_linearIndependent`, `Roth.exists_genWronskian_ne_zero`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/HasseDeriv.lean

Completed assessments: 25/25.

#### def MvPolynomial.hasseCoeff

Type:

```lean
@MvPolynomial.hasseCoeff.{u} :
  {σ : Type u} → (σ →₀ ℕ) → (σ →₀ ℕ) → ℕ
```

- **What**: Defines the coordinatewise binomial coefficient for two finitely supported natural multi-indices, multiplying only over the differentiation index support.
- **How**: Uses Finsupp.prod with Nat.choose; omitted coordinates contribute choose(k,0)=1, so the finite-support presentation gives the full multivariate binomial factor.
- **Hypotheses**: An arbitrary variable type and two natural-valued finitely supported multi-indices; no finiteness or coefficient-ring assumption.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseDeriv_apply`, `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff_eq_prod`, `MvPolynomial.hasseDeriv_zero_apply`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseCoeff_mul_hasseCoeff`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.hasseCoeff_mul_succ`, `MvPolynomial.hasseDeriv_monomial_mul`, `MvPolynomial.hasseDeriv_single_aeval_X`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`, `MvPolynomial.hasseCoeff_le_two_pow`
- **Used by other files (lexical)**: `Roth.abs_coeff_hasseDeriv_le`, `MvPolynomial.hasseCoeff_single_add_eq`
- **Visibility**: public
- **Lines**: 50–50; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff.md).

#### def MvPolynomial.hasseDeriv

Type:

```lean
MvPolynomial.hasseDeriv.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
    [CommSemiring R] (d : σ →₀ ℕ) :
    MvPolynomial σ R →ₗ[R] MvPolynomial σ R
```

- **What**: Defines the divided multivariate derivative as a coefficient-linear endomorphism, lowering every exponent by the selected multi-index.
- **How**: Extends the monomial rule by Finsupp.lsum and AddMonoidAlgebra.coeffLinearEquiv; the natural binomial factor is cast into the coefficient semiring.
- **Hypotheses**: Arbitrary variables and coefficients in a commutative semiring; no characteristic-zero or finite-variable assumption.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`
- **Project references in type**: []
- **Native direct body references**: `MvPolynomial.hasseCoeff`
- **Native direct type references**: []
- **Used by in file (lexical)**: `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseDeriv_apply`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply`, `MvPolynomial.hasseDeriv_zero`, `MvPolynomial.hasseDeriv_C`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `MvPolynomial.hasseDeriv_monomial_mul`, `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.hasseDeriv_single_aeval_X`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`, `MvPolynomial.factorial_smul_hasseDeriv_single`
- **Used by other files (lexical)**: `Roth.abs_coeff_hasseDeriv_le`, `Roth.normOne_hasseDeriv_le`, `Roth.degreeOf_det_hasseDeriv_le`, `Roth.abs_coeff_det_hasseDeriv_le`, `Roth.genWronskian`, `Roth.genWronskian_eq_zero_of_not_linearIndependent`, `Roth.kronHasse`, `Roth.exists_hasseDeriv_kronecker_eq_sum`, `Roth.wronskian_kronecker_eq_sum_aux`, `Roth.mem_support_taylor_iff`, `Roth.index_le_weight`, `Roth.exists_weight_eq_index`, `Roth.le_index_iff`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.index_unique`, `Roth.abs_eval_lt_of_le_index`, `Roth.exists_ne_modByMonic_eq`, `Roth.eval_hasseDeriv_sub_eq_zero`, `Roth.le_index_of_forall_eval_eq_zero`, `Roth.exists_hasseDeriv_eval_ne_zero`, `Roth.abs_eval_iterated_hasseDeriv_lt_aux`, `Roth.exists_hasseDeriv_index_eval_bound_aux`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.main_lemma`, `Roth.hasseDeriv_rename_mul_aeval`, `Roth.det_hasseDeriv_separated`, `Roth.exists_rat_factors_det_hasseDeriv_aux`, `Roth.exists_det_eq_mul`, `MvPolynomial.coeff_taylor_monomial_single_add_aux`, `MvPolynomial.coeff_taylor_monomial_aux`, `MvPolynomial.coeff_taylor`, `MvPolynomial.eq_sum_box_hasseDeriv`, `MvPolynomial.eval_eq_sum_box`, `Roth.sum_max_sub_le_index_det`, `Roth.index_det_le`, `Roth.mapped_det_ne_zero_aux`
- **Visibility**: public
- **Lines**: 57–60; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv.md).

#### theorem MvPolynomial.hasseDeriv_monomial

Type:

```lean
{σ R : Type*} [CommSemiring R] (d k : σ →₀ ℕ) (a : R) : hasseDeriv d (monomial k a) = monomial (k-d) ((hasseCoeff d k : R)*a)
```

- **What**: Computes the Hasse derivative of a scalar monomial.
- **How**: Evaluates the Finsupp.lsum defining hasseDeriv on the single coefficient supported at the input exponent.
- **Hypotheses**: A commutative coefficient semiring, any differentiation and monomial indices, and any scalar.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_C`, `MvPolynomial.hasseDeriv_monomial_mul`
- **Used by other files (lexical)**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`
- **Visibility**: public
- **Lines**: 66–68; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial.md).

#### theorem MvPolynomial.hasseDeriv_apply

Type:

```lean
{σ : Type u} {R : Type v} [CommSemiring R] (d : σ →₀ ℕ) (P : MvPolynomial σ R) : hasseDeriv d P = ∑ k ∈ P.support, monomial (k-d) ((hasseCoeff d k : R) * P.coeff k)
```

- **What**: Expands a multivariate Hasse derivative as the finite sum of the differentiated monomials of its input.
- **How**: Evaluates the defining Finsupp.lsum on the coefficient vector and exposes the polynomial support sum.
- **Hypotheses**: A commutative coefficient semiring, arbitrary variable type, differentiation multiindex and polynomial; no proposition hypotheses.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.normOne_hasseDeriv_le`
- **Visibility**: public
- **Lines**: 73–75; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_apply.md).

#### theorem MvPolynomial.hasseCoeff_eq_zero_iff

Type:

```lean
∀ {σ : Type*} (d k : σ →₀ ℕ), hasseCoeff d k = 0 ↔ ¬d ≤ k
```

- **What**: The natural multi-index binomial factor is zero exactly outside the coordinatewise exponent interval.
- **How**: Generic product-zero criterion, scalar choose-zero criterion, supported order and negation normalization.
- **Hypotheses**: Arbitrary variable type and two natural finitely supported indices; no coefficient classes.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseCoeff`
- **Native direct body references**: `MvPolynomial.hasseCoeff`
- **Native direct type references**: `MvPolynomial.hasseCoeff`
- **Used by in file (lexical)**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_C`
- **Used by other files (lexical)**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`
- **Visibility**: public
- **Lines**: 80–82; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_zero_iff.md).

#### theorem MvPolynomial.coeff_hasseDeriv

Type:

```lean
For arbitrary variable/coefficient types and CommSemiring R, d,e:σ→₀ℕ, P:MvPolynomial σ R: coeff e (hasseDeriv d P) = (hasseCoeff d (e+d):R) * coeff (e+d) P.
```

- **What**: Computes each coefficient of a multivariate Hasse derivative as one shifted input coefficient multiplied by its natural binomial factor.
- **How**: Induct on the polynomial with MvPolynomial.induction_on'; use hasseDeriv_monomial and hasseCoeff_eq_zero_iff to separate reconstructed exponents from out-of-range vanishing, then distribute across addition.
- **Hypotheses**: Arbitrary variable type and commutative coefficient semiring, finite natural derivative/output multiindices and arbitrary polynomial; no finite-variable, field, characteristic, domain or nontriviality hypotheses.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.hasseDeriv_monomial`
- **Project references in type**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`
- **Native direct type references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `MvPolynomial.hasseDeriv_zero_apply`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`
- **Used by other files (lexical)**: `Roth.abs_coeff_hasseDeriv_le`
- **Visibility**: public
- **Lines**: 89–100; proof/body length 11 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_hasseDeriv.md).

#### theorem MvPolynomial.hasseCoeff_eq_prod

Type:

```lean
For any variable type σ with Fintype σ and d,k:σ→₀ℕ, hasseCoeff d k = ∏j, Nat.choose (k j) (d j). No coefficient type R or semiring assumption occurs in the actual type.
```

- **What**: Replaces the support product of coordinatewise binomial coefficients by the full product over finite variables.
- **How**: Specializes Finsupp.prod_fintype with the unit condition Nat.choose_zero_right; exactly two mathlib calls.
- **Hypotheses**: Arbitrary universe-polymorphic variable type, finite enumeration and two natural multiindices. No dominance, field, characteristic, nontriviality, nonempty or coefficient-ring assumption.
- **Uses from project (lexical body)**: []
- **Project references in type**: `MvPolynomial.hasseCoeff`
- **Native direct body references**: []
- **Native direct type references**: `MvPolynomial.hasseCoeff`
- **Used by in file (lexical)**: `MvPolynomial.hasseCoeff_le_two_pow`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 106–107; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_prod.md).

#### theorem MvPolynomial.hasseDeriv_zero_apply

Type:

```lean
For arbitrary types σ,R with CommSemiring R and P:MvPolynomial σ R, MvPolynomial.hasseDeriv 0 P = P.
```

- **What**: The multivariate Hasse derivative of order zero fixes every polynomial.
- **How**: Coefficient extensionality and coeff_hasseDeriv reduce to zero-index support product one; independently verified expanded lsum normalization also works.
- **Hypotheses**: Arbitrary universe-polymorphic variable/coefficient types, CommSemiring coefficients, arbitrary polynomial; no finiteness, characteristic, domain, nonzero or decidable equality assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `MvPolynomial.hasseDeriv_zero`
- **Used by other files (lexical)**: `Roth.index_eq_zero_iff`
- **Visibility**: public
- **Lines**: 112–114; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero_apply.md).

#### theorem MvPolynomial.hasseDeriv_zero

Type:

```lean
For arbitrary types σ,R with CommSemiring R, MvPolynomial.hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R).
```

- **What**: The zero-order multivariate Hasse derivative is the identity linear operator.
- **How**: Current term applies LinearMap.ext to project hasseDeriv_zero_apply. Independently checked coefficient proof and mathlib-only reconstructed construction normalization establish the same bundled equality.
- **Hypotheses**: Arbitrary universe-polymorphic variable and coefficient types, CommSemiring coefficients; no finiteness, decidability, characteristic, domain or nontriviality assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv_zero_apply`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 120–121; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero.md).

#### theorem MvPolynomial.hasseDeriv_C

Type:

```lean
∀ {σ R : Type*} [CommSemiring R] {d : σ →₀ ℕ}, d ≠ 0 → ∀ a : R, MvPolynomial.hasseDeriv d (MvPolynomial.C a) = 0
```

- **What**: Every nonzero-order multivariate Hasse derivative annihilates scalar constant polynomials.
- **How**: Rewrite constant as exponent-zero monomial, apply project Hasse monomial rule, kill binomial factor by nonzero order and simplify. Independent raw construction proof verified using typed Finsupp.lsum_single.
- **Hypotheses**: Arbitrary universes/variables; CommSemiring fixed parent floor; implicit finite natural multi-index d, essential d ≠ 0, arbitrary scalar a. No characteristic or nontriviality assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.hasseDeriv_monomial`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `MvPolynomial.coeff_taylor_monomial_aux`
- **Visibility**: public
- **Lines**: 126–128; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_C.md).

#### theorem MvPolynomial.hasseDeriv_map

Type:

```lean
theorem: ∀ f : R →+* S, ∀ d P, hasseDeriv d (map f P) = map f (hasseDeriv d P)
```

- **What**: Hasse derivatives commute with arbitrary coefficient ring homomorphisms.
- **How**: Coefficient extensionality, coefficient Hasse/map formulas, preservation of natural-number casts and multiplication.
- **Hypotheses**: Arbitrary variable type; independent commutative semirings R/S; any ring hom, multi-index and polynomial.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.eval_hasseDeriv_sub_eq_zero`, `Roth.exists_hasseDeriv_index_eval_bound_aux`, `Roth.exists_rat_factors_det_hasseDeriv_aux`, `Roth.mapped_det_ne_zero_aux`, `Roth.index_le_lem6`
- **Visibility**: public
- **Lines**: 134–137; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_map.md).

#### theorem MvPolynomial.hasseDeriv_rename

Type:

```lean
theorem: ∀ hf : Function.Injective f, ∀ d P, hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P)
```

- **What**: Hasse derivatives commute with injective variable renaming when the multi-index is transported along the same injection.
- **How**: Monomial/additive induction; binomial product transport and mapDomain truncated subtraction compatibility.
- **Hypotheses**: Independent arbitrary variable types σ/τ, CommSemiring R, any injective f, finite multi-index d and polynomial P.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.hasseDeriv_rename_mul_aeval`
- **Visibility**: public
- **Lines**: 143–151; proof/body length 7 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_rename.md).

#### lemma MvPolynomial.hasseCoeff_mul_hasseCoeff

Type:

```lean
private lemma hasseCoeff_mul_hasseCoeff (f d e : σ →₀ ℕ) :
    hasseCoeff d (f + d) * hasseCoeff e (f + d + e) =
      hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e)); section {σ : Type*}; no coefficient-ring assumption
```

- **What**: Proves the multiplicative binomial identity underlying composition of divided derivatives.
- **How**: Enlarges four Finsupp products to the union of the two differentiation supports using Finsupp.prod_of_support_subset, distributes products, then applies Nat.choose_mul coordinatewise and Nat.choose_symm_add.
- **Hypotheses**: Three natural finitely supported multi-indices; no coefficient-ring assumption.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseCoeff`
- **Native direct body references**: `MvPolynomial.hasseCoeff`
- **Native direct type references**: `MvPolynomial.hasseCoeff`
- **Used by in file (lexical)**: `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseCoeff_mul_succ`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 153–168; proof/body length 14 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_hasseCoeff.md).

#### theorem MvPolynomial.hasseDeriv_hasseDeriv

Type:

```lean
∀ {σ R : Type*} [CommSemiring R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R), hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P
```

- **What**: Composing Hasse derivatives adds orders with product-binomial scalar.
- **How**: Coefficient comparison plus finite-support product Nat.choose_mul cocycle.
- **Hypotheses**: MAXIMALLY GENERAL for pinned canonical interface: CommSemiring, arbitrary variable types, indices and polynomial; literal Semiring parent fails.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff_mul_hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`
- **Used by other files (lexical)**: `Roth.index_sub_weight_le_index_hasseDeriv`
- **Visibility**: public
- **Lines**: 175–179; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv.md).

#### theorem MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint

Type:

```lean
∀ {σ R : Type*} [CommSemiring R] {d e : σ →₀ ℕ}, Disjoint d.support e.support → ∀ P : MvPolynomial σ R, hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P
```

- **What**: Hasse derivatives in disjoint variable supports compose with no binomial scalar.
- **How**: General iterativity then support-disjoint finite-product factors equal1.
- **Hypotheses**: MAXIMALLY GENERAL for geometric support-separation corollary; scalar-cast-one criterion verified strictly weaker in characteristic2 and already subsumed by unrestricted parent law.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv_hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.hasseDeriv_rename_mul_aeval`
- **Visibility**: public
- **Lines**: 185–189; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint.md).

#### lemma MvPolynomial.hasseCoeff_mul_succ

Type:

```lean
private lemma hasseCoeff_mul_succ (j : σ) (d e : σ →₀ ℕ) :
    hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) =
      (d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d); section {σ : Type*}, no coefficient-ring assumption
```

- **What**: Proves the single-coordinate successor form of the binomial composition identity.
- **How**: Specializes hasseCoeff_mul_hasseCoeff to the one-coordinate multi-index and simplifies the single-support binomial factors.
- **Hypotheses**: Natural finitely supported indices and a distinguished variable; no ring assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseCoeff`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_hasseCoeff`
- **Native direct type references**: `MvPolynomial.hasseCoeff`
- **Used by in file (lexical)**: `MvPolynomial.pderiv_hasseDeriv`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 191–195; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_succ.md).

#### theorem MvPolynomial.pderiv_hasseDeriv

Type:

```lean
∀ {σ R : Type*} [CommSemiring R] (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R), pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P
```

- **What**: Ordinary partial differentiation increments the Hasse multi-order with its necessary successor scalar.
- **How**: Coefficient extensionality and product-binomial successor recurrence.
- **Hypotheses**: MAXIMALLY GENERAL for canonical pinned polynomial/pderiv interface; arbitrary variables, semiring, order and input. Literal Semiring parent fails.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff_mul_succ`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_succ`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `MvPolynomial.factorial_smul_hasseDeriv_single`
- **Used by other files (lexical)**: `Roth.derivative_kronHasse_aux`
- **Visibility**: public
- **Lines**: 200–205; proof/body length 5 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.pderiv_hasseDeriv.md).

#### theorem MvPolynomial.degreeOf_hasseDeriv_le

Type:

```lean
theorem: coordinate natural degree nonincrease under arbitrary-order multivariate Hasse derivative
```

- **What**: deg_j Δ_dP ≤deg_jP for arbitrary σ and commutative semiring R, including zero.
- **How**: A nonzero output coefficient at m implies a nonzero input coefficient at m+d; apply coordinate-degree support bound.
- **Hypotheses**: arbitrary σ,R; CommSemiring R parent interface; j:σ; d:σ→₀ℕ; arbitrary P; no finiteness/characteristic/nonzero conditions
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.degreeOf_det_hasseDeriv_le`, `Roth.abs_eval_iterated_hasseDeriv_lt_aux`, `Roth.exists_hasseDeriv_index_eval_bound_aux`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
- **Visibility**: public
- **Lines**: 210–214; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_hasseDeriv_le.md).

#### theorem MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt

Type:

```lean
theorem: coordinate degree below multi-index implies multivariate Hasse derivative zero
```

- **What**: If degreeOf j P < d j for any coordinate j, Δ_dP=0.
- **How**: Each derivative coefficient comes from exponent e+d, excluded from input support by the strict degree bound.
- **Hypotheses**: arbitrary σ,R with CommSemiring R; j:σ,d:σ→₀ℕ,P arbitrary; degreeOf j P < d j
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.le_index_of_forall_eval_eq_zero`, `MvPolynomial.degreeOf_taylor_le`, `MvPolynomial.eq_sum_box_hasseDeriv`
- **Visibility**: public
- **Lines**: 219–223; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt.md).

#### lemma MvPolynomial.hasseDeriv_monomial_mul

Type:

```lean
private lemma hasseDeriv_monomial_mul {d a : σ →₀ ℕ} (ha : ∀ j ∈ d.support, a j = 0) (c : R)
    (g : MvPolynomial σ R) : hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g; section {σ R : Type*} [CommSemiring R]
```

- **What**: A scalar monomial supported away from the differentiation coordinates passes unchanged through the Hasse derivative of a product.
- **How**: Additive monomial induction and hasseDeriv_monomial reduce to exponent subtraction; a coordinate split proves a+b-d=a+(b-d), while the support-disjoint condition preserves hasseCoeff.
- **Hypotheses**: Commutative coefficients and a monomial exponent that vanishes on the differentiation support.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv_monomial`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 225–237; proof/body length 12 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial_mul.md).

#### theorem MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] {d : σ →₀ ℕ} {f g : MvPolynomial σ R},
  (∀ j ∈ d.support, degreeOf j f = 0) → (hasseDeriv d) (f * g) = f * (hasseDeriv d) g
```

- **What**: A factor independent of all variables in d.support passes through the canonical multi-index Hasse derivative.
- **How**: Expand f into monomials; degree-zero gives exponent zero in differentiated variables; prove monomial compatibility then extend by linearity.
- **Hypotheses**: arbitrary variable type and coefficient type; CommSemiring R; d finitely supported natural multi-index; forall j in d.support, degreeOf j f=0
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv_monomial_mul`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial_mul`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.hasseDeriv_rename_mul_aeval`
- **Visibility**: public
- **Lines**: 243–247; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero.md).

#### theorem MvPolynomial.hasseDeriv_single_aeval_X

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (j : σ) (n : ℕ) (f : Polynomial R),
  (hasseDeriv (Finsupp.single j n)) ((Polynomial.aeval (X j)) f) =
    (Polynomial.aeval (X j)) ((Polynomial.hasseDeriv n) f)
```

- **What**: The coordinate embedding of univariate polynomials intertwines Hasse derivatives.
- **How**: Additive/monomial induction; alternatively existing monomial-basis extensionality and closing definition simp.
- **Hypotheses**: arbitrary sigma and R universes; CommSemiring R; j : sigma; n : Nat; f : Polynomial R
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.hasseDeriv_rename_mul_aeval`
- **Visibility**: public
- **Lines**: 253–260; proof/body length 6 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_single_aeval_X.md).

#### theorem MvPolynomial.uniqueAlgEquiv_hasseDeriv

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] [inst_1 : Unique σ] (n : ℕ)
  (P : MvPolynomial σ R),
  (uniqueAlgEquiv R σ) ((hasseDeriv (Finsupp.single default n)) P) = (Polynomial.hasseDeriv n) ((uniqueAlgEquiv R σ) P)
```

- **What**: Canonical identification of a singleton-variable polynomial algebra commutes with every Hasse derivative.
- **How**: Coefficient extensionality and singleton-binomial normalization; isolated raw basis proof also closes by definitions.
- **Hypotheses**: CommSemiring R; Unique σ
- **Uses from project (lexical body)**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_unique`
- **Visibility**: public
- **Lines**: 266–271; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.uniqueAlgEquiv_hasseDeriv.md).

#### theorem MvPolynomial.hasseCoeff_le_two_pow

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ},
  (∀ (j : σ), k j ≤ r j) → hasseCoeff d k ≤ 2 ^ ∑ j : σ, r j
```

- **What**: The natural binomial factor of a multivariate Hasse derivative is bounded by two to the sum of a degree box.
- **How**: Expand finite product, bound choose coordinatewise, lift through product monotonicity and normalize product of powers.
- **Hypotheses**: Fintype σ; d,k : σ →₀ ℕ; r : σ → ℕ; ∀ j,k j ≤ r j
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff_eq_prod`
- **Project references in type**: `MvPolynomial.hasseCoeff`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_eq_prod`
- **Native direct type references**: `MvPolynomial.hasseCoeff`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.abs_coeff_hasseDeriv_le`, `Roth.normOne_hasseDeriv_le`
- **Visibility**: public
- **Lines**: 276–280; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_le_two_pow.md).

#### theorem MvPolynomial.factorial_smul_hasseDeriv_single

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (j : σ) (n : ℕ) (P : MvPolynomial σ R),
  ↑n.factorial • (hasseDeriv (Finsupp.single j n)) P = (⇑(pderiv j))^[n] P
```

- **What**: n! times coordinate Hasse derivative equals iterated partial differentiation over any commutative semiring.
- **How**: Induct on order using scalar compatibility and pderiv_hasseDeriv recurrence.
- **Hypotheses**: Arbitrary σ,R, CommSemiring R, coordinate j, natural order n and polynomial P.
- **Uses from project (lexical body)**: `MvPolynomial.pderiv_hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero`, `MvPolynomial.pderiv_hasseDeriv`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 286–292; proof/body length 6 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.factorial_smul_hasseDeriv_single.md).

#### File structural summary

- Written declarations: 25; kinds: {'def': 2, 'theorem': 20, 'lemma': 3}
- **Key API (at least three lexical callers)**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`
- **Unused in file (observation)**: `MvPolynomial.hasseDeriv_apply`, `MvPolynomial.hasseDeriv_zero`, `MvPolynomial.hasseDeriv_C`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.hasseDeriv_single_aeval_X`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`, `MvPolynomial.hasseCoeff_le_two_pow`, `MvPolynomial.factorial_smul_hasseDeriv_single`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Index.lean

Completed assessments: 19/19.

#### def Roth.index

Type:

```lean
{σ : Type u_1} → [Fintype σ] → MvPolynomial σ ℝ → (σ → ℝ) → (σ → ℕ) → ℝ
```

- **What**: Minimum reciprocal-parameter weight of the Taylor support, with zero polynomial and zero denominators projected to the project real-valued convention.
- **How**: sInf of weight image of translated polynomial support. More general existing AddMonoidAlgebra.infDegree computes that finite minimum in WithTop ℝ; untopD 0 restores the project zero convention.
- **Hypotheses**: Fintype σ is required by Roth.weight global sum, avoidable by Finsupp weighting.; P and α real-valued, r natural-valued; no nonzero/positive premises on the definition.
- **Uses from project (lexical body)**: `MvPolynomial.taylor`, `Roth.weight`
- **Project references in type**: []
- **Native direct body references**: `MvPolynomial.taylor`, `Roth.weight`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.index_le_weight`, `Roth.exists_weight_eq_index`, `Roth.le_index_iff`, `Roth.index_nonneg`, `Roth.index_eq_zero_iff`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.le_index_sum`, `Roth.index_eq_weightedOrder_div`, `Roth.index_mul`, `Roth.index_prod`, `Roth.index_neg`, `Roth.index_C_mul`, `Roth.index_mul_left_weights`, `Roth.index_rename`, `Roth.index_le_card`, `Roth.index_unique`
- **Used by other files (lexical)**: `Roth.abs_eval_lt_of_le_index`, `Roth.le_index_of_forall_eval_eq_zero`, `Roth.exists_hasseDeriv_eval_ne_zero`, `Roth.exists_hasseDeriv_index_eval_bound_aux`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.main_lemma`, `Roth.indexSet`, `Roth.index_le_Θ`, `Roth.Θ_le_of_forall_index_le`, `Roth.index_unique_le_log_div`, `Roth.sum_max_sub_le_index_det`, `Roth.index_separated_mul_le_aux`, `Roth.index_det_le`, `Roth.index_le_lem6`
- **Visibility**: public
- **Lines**: 58–59; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index.md).

#### lemma Roth.mem_support_taylor_iff

Type:

```lean
∀ {σ : Type u_1} {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ},
  d ∈ ((MvPolynomial.taylor α) P).support ↔ (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0
```

- **What**: Taylor support membership is equivalent to nonvanishing of the corresponding Hasse derivative at the center.
- **How**: Combines mem_support_iff with the project coeff_taylor identity.
- **Hypotheses**: A real polynomial and point; no finiteness of the variable type. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_taylor`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Used by in file (lexical)**: `Roth.index_le_weight`, `Roth.exists_weight_eq_index`, `Roth.le_index_iff`, `Roth.index_le_card`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 62–64; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.mem_support_taylor_iff.md).

#### theorem Roth.index_le_weight

Type:

```lean
Roth.index_le_weight.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ}
  (h : (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0) : Roth.index P α r ≤ Roth.weight r d
```

- **What**: Nonzero evaluated Hasse coefficient bounds the point index above by its weight.
- **How**: csInf_le on the finite image of Taylor support, using the private coefficient membership equivalence.
- **Hypotheses**: arbitrary σ with Fintype σ; real polynomial P and center α; natural parameters r, including zero entries; multi-index d with eval α (hasseDeriv d P) ≠ 0; no P≠0 or positivity assumptions
- **Uses from project (lexical body)**: `MvPolynomial.taylor`, `Roth.mem_support_taylor_iff`, `Roth.weight`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`, `Roth.mem_support_taylor_iff`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.le_index_iff`, `Roth.index_eq_zero_iff`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.index_eq_weightedOrder_div`, `Roth.index_unique`
- **Used by other files (lexical)**: `Roth.abs_eval_lt_of_le_index`
- **Visibility**: public
- **Lines**: 69–72; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_le_weight.md).

#### theorem Roth.exists_weight_eq_index

Type:

```lean
Roth.exists_weight_eq_index.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ)
  (r : σ → ℕ) : ∃ d, (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0 ∧ Roth.weight r d = Roth.index P α r
```

- **What**: A nonzero polynomial has an evaluated Hasse derivative whose weight attains its index.
- **How**: Set.Nonempty.csInf_mem on finite nonempty weighted Taylor support, then private coefficient/support equivalence.
- **Hypotheses**: σ : Type u with Fintype σ; P : MvPolynomial σ ℝ with P≠0; α : σ→ℝ; r : σ→ℕ, allowing zeros; no positivity assumption
- **Uses from project (lexical body)**: `MvPolynomial.taylor`, `Roth.mem_support_taylor_iff`, `Roth.weight`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`, `Roth.index`, `Roth.mem_support_taylor_iff`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.index_eq_zero_iff`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.index_le_card`
- **Used by other files (lexical)**: `Roth.exists_hasseDeriv_eval_ne_zero`
- **Visibility**: public
- **Lines**: 76–81; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_weight_eq_index.md).

#### theorem Roth.le_index_iff

Type:

```lean
Roth.le_index_iff.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ {α : σ → ℝ} {r : σ → ℕ} {c : ℝ}, c ≤ Roth.index P α r ↔ ∀ (d : σ →₀ ℕ), (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0 → c ≤ Roth.weight r d
```

- **What**: A lower bound for a nonzero polynomial's weighted index at a point is equivalent to a common lower bound for all nonvanishing Hasse-derivative weights.
- **How**: Forward transitivity with index_le_weight; reverse conditional infimum introduction on translated support using coeff_taylor.
- **Hypotheses**: Fintype variables and real coefficients fixed by parent index/weight; P nonzero needed for zero-default real projection; no positive-r assumption.
- **Uses from project (lexical body)**: `Roth.index_le_weight`, `Roth.mem_support_taylor_iff`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`, `Roth.index`, `Roth.index_le_weight`, `Roth.mem_support_taylor_iff`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.le_index_sum`, `Roth.index_eq_weightedOrder_div`, `Roth.index_unique`
- **Used by other files (lexical)**: `Roth.le_index_of_forall_eval_eq_zero`
- **Visibility**: public
- **Lines**: 85–90; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.le_index_iff.md).

#### theorem Roth.index_nonneg

Type:

```lean
Roth.index_nonneg.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ), 0 ≤ Roth.index P α r
```

- **What**: The weighted index at any real point is nonnegative, including zero polynomial and zero denominator parameters.
- **How**: Real.sInf_nonneg applied to the image of translated coefficient support; all rational weights are nonnegative.
- **Hypotheses**: Fintype variables fixed by Roth.weight and Roth.index; no nonvanishing, positive denominator, nonempty variable or DecidableEq hypotheses.
- **Uses from project (lexical body)**: `Roth.weight_nonneg`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.taylor`, `Roth.weight`, `Roth.weight_nonneg`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: `Roth.index_eq_zero_iff`
- **Used by other files (lexical)**: `Roth.Θ_nonneg`, `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 93–94; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_nonneg.md).

#### theorem Roth.index_eq_zero_iff

Type:

```lean
Roth.index_eq_zero_iff.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) : Roth.index P α r = 0 ↔ (MvPolynomial.eval α) P ≠ 0
```

- **What**: A nonzero polynomial has weighted index0 at a point iff its evaluation there is nonzero, for positive natural denominator parameters.
- **How**: Attain the support minimum; nonnegative positive weights have zero only at exponent0; Hasse derivative0 is identity. Converse uses weight0 and nonnegativity.
- **Hypotheses**: Fintype σ: fixed parent global sum; hP: essential under default0; actual zero-polynomial counterexample; hr: essential for uniform iff; actual Unit X and Bool mixedzero polynomial counterexamples; α: arbitrary center; empty σ allowed
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv_zero_apply`, `Roth.exists_weight_eq_index`, `Roth.index_le_weight`, `Roth.index_nonneg`, `Roth.weight_eq_zero_iff`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero`, `Roth.exists_weight_eq_index`, `Roth.index`, `Roth.index_le_weight`, `Roth.index_nonneg`, `Roth.weight`, `Roth.weight_eq_zero_iff`, `Roth.weight_zero`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: `Roth.index_prod`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 98–105; proof/body length 7 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_eq_zero_iff.md).

#### theorem Roth.index_sub_weight_le_index_hasseDeriv

Type:

```lean
Roth.index_sub_weight_le_index_hasseDeriv.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ} (hk : (MvPolynomial.hasseDeriv k) P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : Roth.index P α r - Roth.weight r k ≤ Roth.index ((MvPolynomial.hasseDeriv k) P) α r
```

- **What**: Applying a nonzero Hasse derivative decreases weighted vanishing index by at most the weight of its multi-order.
- **How**: Choose an attaining derivative; composition gives a nonzero shifted coefficient; compare the original minimum and use additive weights.
- **Hypotheses**: Finite variable interface, real coefficients, nonzero Hasse derivative. Natural denominators may be zero. Expanded new theorem uses arbitrary sigma, CommRing coefficients and shift-compatible real degree.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv_hasseDeriv`, `Roth.exists_weight_eq_index`, `Roth.index_le_weight`, `Roth.weight_add`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv`, `Roth.exists_weight_eq_index`, `Roth.index`, `Roth.index_le_weight`, `Roth.weight`, `Roth.weight_add`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.exists_hasseDeriv_index_eval_bound_aux`, `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 109–114; proof/body length 4 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_sub_weight_le_index_hasseDeriv.md).

#### theorem Roth.le_index_sum

Type:

```lean
Roth.le_index_sum.{u_1, u_2} : ∀ {σ : Type u_1} [inst : Fintype σ] {ι : Type u_2} {s : Finset ι}
  {f : ι → MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ},
  ∑ i ∈ s, f i ≠ 0 → ∀ {c : ℝ}, (∀ i ∈ s, f i ≠ 0 → c ≤ Roth.index (f i) α r) → c ≤ Roth.index (∑ i ∈ s, f i) α r
```

- **What**: A common lower bound for the indices of nonzero summands is a lower bound for their nonzero finite sum.
- **How**: For every nonzero Hasse coefficient of the sum, map_sum and exists_ne_zero_of_sum_ne_zero select a nonzero summand coefficient; its assumed index bound controls the weight.
- **Hypotheses**: Finite variable interface, real coefficients, arbitrary finite summation type, nonzero sum, common bound for nonzero summands. Natural denominator weights may vanish; no positivity premise.
- **Uses from project (lexical body)**: `Roth.le_index_iff`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.le_index_iff`, `Roth.weight`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 118–125; proof/body length 6 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.le_index_sum.md).

#### theorem Roth.weight_eq_finsuppWeight_div

Type:

```lean
∀ {σ : Type u} [Fintype σ] {r : σ → ℕ}, (∀ j, 0 < r j) → ∀ d : σ →₀ ℕ, Roth.weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ↑(∏ i, r i)
```

- **What**: Clear reciprocal natural parameter denominators using D=∏r.
- **How**: Expand weights, cast exact natural quotients, distribute division, cancel nonzero D.
- **Hypotheses**: Fintype σ; globally positive natural r; arbitrary finitely supported natural d.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: `Roth.index_eq_weightedOrder_div`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 130–137; proof/body length 7 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_finsuppWeight_div.md).

#### theorem Roth.index_eq_weightedOrder_div

Type:

```lean
Roth.index_eq_weightedOrder_div.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ}
  (hr : ∀ (j : σ), 0 < r j) (α : σ → ℝ) :
  Roth.index P α r =
    ↑(MvPowerSeries.weightedOrder (fun j ↦ (∏ i, r i) / r j) ↑((MvPolynomial.taylor α) P)).toNat / ↑(∏ i, r i)
```

- **What**: Identifies reciprocal-weight point index with natural weightedOrder of translated polynomial divided by common denominator.
- **How**: Finite order attained coefficient gives upper index bound; all support coefficients and weightedOrder_le give lower bound after denominator clearing and finite toNat monotonicity.
- **Hypotheses**: σ: Type*, Fintype for original full-product interface; P: real multivariate polynomial; hP: P≠0 is removable, verified exact formula allP; r: natural reciprocal denominators; hr: all positive; uniform removal false for mixedzero weights; α: real center
- **Uses from project (lexical body)**: `MvPolynomial.coeff_taylor`, `MvPolynomial.taylor`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight_eq_finsuppWeight_div`
- **Project references in type**: `MvPolynomial.taylor`, `Roth.index`
- **Native direct body references**: `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`, `Roth.index`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight`, `Roth.weight_eq_finsuppWeight_div`
- **Native direct type references**: `MvPolynomial.taylor`, `Roth.index`
- **Used by in file (lexical)**: `Roth.index_mul`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 143–158; proof/body length 13 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_eq_weightedOrder_div.md).

#### theorem Roth.index_mul

Type:

```lean
Roth.index_mul.{u_1} {σ : Type u_1} [Fintype σ] {P Q : MvPolynomial σ ℝ} (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → ℝ)
  {r : σ → ℕ} (hr : ∀ (j : σ), 0 < r j) : Roth.index (P * Q) α r = Roth.index P α r + Roth.index Q α r
```

- **What**: The point index of the product of two nonzero real multivariate polynomials is the sum of the indices.
- **How**: Clear positive reciprocal denominators to natural weights, translate and coerce into multivariate power series, invoke existing weightedOrder_mul, and project finite ENat values through toNat and real scaling.
- **Hypotheses**: σ/Fintype and ℝ are fixed parent-interface constraints. hP and hQ are necessary uniformly under real default-zero index; both zero-factor counterexamples compiled. hr is removable: D=∏ max 1 (r i) is positive and D/0=0 provides the natural weight for a zero reciprocal denominator.
- **Uses from project (lexical body)**: `MvPolynomial.taylor`, `Roth.index_eq_weightedOrder_div`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.taylor`, `Roth.index`, `Roth.index_eq_weightedOrder_div`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: `Roth.index_prod`
- **Used by other files (lexical)**: `Roth.index_separated_mul_le_aux`
- **Visibility**: public
- **Lines**: 162–170; proof/body length 8 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_mul.md).

#### theorem Roth.index_prod

Type:

```lean
Roth.index_prod.{u_1, u_2} {σ : Type u_1} [Fintype σ] {ι : Type u_2} (s : Finset ι) {f : ι → MvPolynomial σ ℝ}
  (hf : ∀ i ∈ s, f i ≠ 0) (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ (j : σ), 0 < r j) :
  Roth.index (∏ i ∈ s, f i) α r = ∑ i ∈ s, Roth.index (f i) α r
```

- **What**: The index of a finite product of nonzero real multivariate polynomials equals the sum of their indices at a common point and reciprocal weights.
- **How**: Finset induction: index of one is zero; apply the binary index_mul law to the inserted factor and remaining nonzero product, then the induction hypothesis.
- **Hypotheses**: σ/Fintype, ℝ and reciprocal natural r belong to the fixed parent interface. ι is arbitrary and s finite; f unrestricted. hf is necessary uniformly because index zero defaults to zero. hr is removable, verified through the all-r binary law and a direct index-one simplification.
- **Uses from project (lexical body)**: `Roth.index_eq_zero_iff`, `Roth.index_mul`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `Roth.index`, `Roth.index_eq_zero_iff`, `Roth.index_mul`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 175–187; proof/body length 11 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_prod.md).

#### theorem Roth.index_neg

Type:

```lean
Roth.index_neg.{u_1} {σ : Type u_1} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (-P) α r = Roth.index P α r
```

- **What**: Negating a polynomial preserves its index at any center and natural weight vector, including zero cases.
- **How**: Taylor map_neg preserves coefficient support via support_neg; identical weighted support infima.
- **Hypotheses**: Fintype variable index fixed by parent; arbitrary P, α, r; no positivity/nonzero assumptions.
- **Uses from project (lexical body)**: `Roth.index`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.taylor`, `Roth.index`, `Roth.weight`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 190–192; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_neg.md).

#### theorem Roth.index_C_mul

Type:

```lean
Roth.index_C_mul.{u_1} {σ : Type u_1} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (MvPolynomial.C c * P) α r = Roth.index P α r
```

- **What**: Nonzero constant multiplication preserves the weighted Taylor index, including zero polynomials and zero weights.
- **How**: Taylor multiplication and constant compatibility reduce to support_smul_eq.
- **Hypotheses**: Fintype fixed by parent; c≠0 essential uniformly by P=X guard; P, α and r arbitrary.
- **Uses from project (lexical body)**: `MvPolynomial.taylor_C`, `Roth.index`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.taylor`, `MvPolynomial.taylor_C`, `Roth.index`, `Roth.weight`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.sum_max_sub_le_index_det`
- **Visibility**: public
- **Lines**: 195–197; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_C_mul.md).

#### theorem Roth.index_mul_left_weights

Type:

```lean
Roth.index_mul_left_weights.{u_1} {σ : Type u_1} [Fintype σ] {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
  (Roth.index P α fun j ↦ l * r j) = Roth.index P α r / ↑l
```

- **What**: Scaling all natural denominator parameters by l divides the polynomial index by l, including l=0.
- **How**: Normalize the image of weighted Taylor support by weight_mul_left, then Real.sInf_smul_of_nonneg. Generic re-aim is map_finset_inf on infDegree.
- **Hypotheses**: Arbitrary σ : Type u with Fintype, real polynomial P and center α, r : σ→ℕ, l : ℕ. No positivity/nonzero premises.
- **Uses from project (lexical body)**: `MvPolynomial.taylor`, `Roth.index`, `Roth.weight`, `Roth.weight_mul_left`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.taylor`, `Roth.index`, `Roth.weight`, `Roth.weight_mul_left`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_separated_mul_le_aux`
- **Visibility**: public
- **Lines**: 200–207; proof/body length 7 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_mul_left_weights.md).

#### theorem Roth.index_rename

Type:

```lean
Roth.index_rename.{u_1, u_2} {σ : Type u_1} [Fintype σ] {τ : Type u_2} [Fintype τ] {f : σ → τ}
  (hf : Function.Injective f) (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) :
  Roth.index ((MvPolynomial.rename f) P) α r = Roth.index P (α ∘ f) (r ∘ f)
```

- **What**: Injective variable renaming preserves the centered weighted polynomial index after pulling back center and denominator weights.
- **How**: Commute translation with rename, identify support image under mapDomain, preserve weights and take the same finite-support minimum.
- **Hypotheses**: Finite σ,τ in current parent interface; f injective; arbitrary P, α, r with zero polynomial/denominators allowed. Injection prevents cancellation; all other constraints are parent formation.
- **Uses from project (lexical body)**: `MvPolynomial.taylor_rename`, `Roth.index`, `Roth.weight_mapDomain`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.taylor`, `MvPolynomial.taylor_rename`, `Roth.index`, `Roth.weight`, `Roth.weight_mapDomain`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.indexSet_comp_subset`, `Roth.index_separated_mul_le_aux`
- **Visibility**: public
- **Lines**: 212–219; proof/body length 6 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_rename.md).

#### theorem Roth.index_le_card

Type:

```lean
Roth.index_le_card.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ {r : σ → ℕ}, (∀ j, MvPolynomial.degreeOf j P ≤ r j) → ∀ α : σ → ℝ, Roth.index P α r ≤ ↑(Fintype.card σ)
```

- **What**: Coordinate degree bounds by denominator parameters imply index at most number of variables.
- **How**: Choose a nonzero Taylor coefficient attaining the minimum; compare its coordinates with Taylor degrees and original degree bounds; sum quotients bounded by one.
- **Hypotheses**: Fintype σ, real P, arbitrary center α, natural denominators r, hP≠0, coordinate degree bounds. hP independently verified droppable under project real-default0 convention; not droppable under canonical∞.
- **Uses from project (lexical body)**: `MvPolynomial.degreeOf_taylor_le`, `Roth.exists_weight_eq_index`, `Roth.mem_support_taylor_iff`, `Roth.weight_le_card`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.degreeOf_taylor_le`, `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`, `Roth.exists_weight_eq_index`, `Roth.index`, `Roth.mem_support_taylor_iff`, `Roth.weight`, `Roth.weight_le_card`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.indexSet_bddAbove`, `Roth.Θ_le_card`
- **Visibility**: public
- **Lines**: 224–229; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_le_card.md).

#### theorem Roth.index_unique

Type:

```lean
@Roth.index_unique : ∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : Unique σ] {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ (α : σ → ℝ) (r : σ → ℕ), Roth.index P α r = ↑(Polynomial.rootMultiplicity (α default) ((MvPolynomial.uniqueAlgEquiv ℝ σ) P)) / ↑(r default)
```

- **What**: In one variable the normalized polynomial index equals root multiplicity divided by the denominator.
- **How**: Use uniqueAlgEquiv_hasseDeriv and Polynomial.taylor_coeff to identify Hasse evaluations with Taylor coefficients; Polynomial.rootMultiplicity_eq_natTrailingDegree, index_le_weight and le_index_iff compare both bounds using the least nonzero coefficient.
- **Hypotheses**: Fintype σ: fixed weight/index interface; derivable from Unique; Unique σ: exactly one variable and uniqueAlgEquiv; P ≠ 0: removable under zero projection; independently verified; α arbitrary; r natural including zero; no positivity/domain/characteristic-zero assumption
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`, `Roth.index`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_unique_le_log_div`
- **Visibility**: public
- **Lines**: 234–251; proof/body length 16 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_unique.md).

#### File structural summary

- Written declarations: 19; kinds: {'def': 1, 'lemma': 1, 'theorem': 17}
- **Key API (at least three lexical callers)**: `Roth.index`, `Roth.mem_support_taylor_iff`, `Roth.index_le_weight`, `Roth.exists_weight_eq_index`, `Roth.le_index_iff`, `Roth.index_nonneg`
- **Unused in file (observation)**: `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.le_index_sum`, `Roth.index_prod`, `Roth.index_neg`, `Roth.index_C_mul`, `Roth.index_mul_left_weights`, `Roth.index_rename`, `Roth.index_le_card`, `Roth.index_unique`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Lattice.lean

Completed assessments: 13/13.

#### theorem Roth.sqrt_one_sub_inv_lt

Type:

```lean
Roth.sqrt_one_sub_inv_lt {m : ℕ} (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √↑m < lam) : √(1 - 1 / ↑m) < 1 - lam⁻¹ ^ 2
```

- **What**: Strict square-root bound by an inverse-square threshold for a dimension parameter.
- **How**: Square the positive λ bound, compare reciprocals, reduce sqrt inequality to a polynomial inequality.
- **Hypotheses**: m : ℕ; 2 ≤ m; lam : ℝ; 2 * √(m : ℝ) < lam
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.sum_inv_lt`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 29–38; proof/body length 9 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sqrt_one_sub_inv_lt.md).

#### lemma Roth.inv_add_inv_le

Type:

```lean
∀ {lam x : ℝ},
  2 < lam → 0 ≤ x → x ≤ 2 → (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1)
```

- **What**: Bounds the sum of two complementary reciprocal terms by twice the endpoint harmonic factor.
- **How**: Combines reciprocals with inv_add_inv, clears positive denominators, and uses x(2−x)≥0.
- **Hypotheses**: Real λ greater than two and x in the closed interval [0,2]. The exact type is over real numbers and natural grid sizes as printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.sum_inv_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 40–45; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.inv_add_inv_le.md).

#### lemma Roth.sum_inv_le

Type:

```lean
∀ {r : ℕ},
  1 ≤ r →
    ∀ {lam : ℝ}, 2 < lam → ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ ≤ (↑r + 1) * (lam / (lam ^ 2 - 1))
```

- **What**: Bounds the reciprocal arithmetic-grid sum by (r+1)*lambda/(lambda^2-1), using complementary-term pairing.
- **How**: Pairs each term j with r−j using inv_add_inv_le and Finset.sum_range_reflect, then divides the paired-sum estimate by two.
- **Hypotheses**: Positive natural r and real λ greater than two. The exact type is over real numbers and natural grid sizes as printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.inv_add_inv_le`
- **Project references in type**: []
- **Native direct body references**: `Roth.inv_add_inv_le`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.sum_inv_lt`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 47–61; proof/body length 14 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_le.md).

#### theorem Roth.sum_inv_lt

Type:

```lean
Roth.sum_inv_lt {r m : ℕ} (hr : 1 ≤ r) (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √↑m < lam) : ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ < lam⁻¹ * (√(↑m - 1))⁻¹ * √↑m * (↑r + 1)
```

- **What**: Strict bound for reciprocal arithmetic-grid sum by (r+1)√m/(λ√(m−1)), for r≥1,m≥2,λ>2√m.
- **How**: Apply sum_inv_le for the paired endpoint bound, use sqrt_one_sub_inv_lt for the strict comparison, and normalize the square-root quotient with Real.sqrt_div'.
- **Hypotheses**: r,m:ℕ; 1≤r; 2≤m; lam:ℝ; 2√m<lam
- **Uses from project (lexical body)**: `Roth.sqrt_one_sub_inv_lt`, `Roth.sum_inv_le`
- **Project references in type**: []
- **Native direct body references**: `Roth.sqrt_one_sub_inv_lt`, `Roth.sum_inv_le`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.card_filter_weight_le_succ_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 68–90; proof/body length 21 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_lt.md).

#### lemma Roth.extend_apply_castSucc

Type:

```lean
∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ) (j : Fin m),
  (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i) j.castSucc = d j
```

- **What**: Extending a vector by a last coordinate preserves all earlier coordinates.
- **How**: Finsupp.mapDomain_apply_of_injective computes the embedded earlier coordinate and the disjoint single last-coordinate contribution vanishes.
- **Hypotheses**: A finite coordinate set Fin m, a finitely supported vector, and a natural last coordinate. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.card_filter_box_fiber_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 92–94; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_castSucc.md).

#### lemma Roth.extend_apply_last

Type:

```lean
∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ),
  (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i) (Fin.last m) = i
```

- **What**: Extending a vector by a last coordinate assigns that last coordinate its prescribed value.
- **How**: Finsupp.mapDomain_of_notMem_range makes the embedded vector vanish at Fin.last.
- **Hypotheses**: A vector on Fin m and an arbitrary natural last coordinate. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.card_filter_box_fiber_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 96–98; proof/body length 2 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_last.md).

#### lemma Roth.card_filter_box_fiber_aux

Type:

```lean
∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
  [inst : DecidablePred p] {i : ℕ},
  i ≤ r (Fin.last m) →
    {d ∈ Roth.box (r ∘ Fin.castSucc) | p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}.card =
      {d ∈ Finset.filter p (Roth.box r) | d (Fin.last m) = i}.card
```

- **What**: A fixed last-coordinate fiber of a filtered rectangular box has the same cardinality as the smaller box filtered after extension by that coordinate.
- **How**: Constructs a Finset.card_bij with extension, proves coordinate bounds using extend_apply_castSucc/extend_apply_last, and reconstructs the inverse by restriction to earlier coordinates.
- **Hypotheses**: A natural rectangular box, a decidable predicate, and a last coordinate within its bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.extend_apply_castSucc`, `Roth.extend_apply_last`, `Roth.mem_box`
- **Project references in type**: `Roth.box`
- **Native direct body references**: `Roth.box`, `Roth.extend_apply_castSucc`, `Roth.extend_apply_last`
- **Native direct type references**: `Roth.box`
- **Used by in file (lexical)**: `Roth.card_filter_box_last`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 100–124; proof/body length 21 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_fiber_aux.md).

#### theorem Roth.card_filter_box_last

Type:

```lean
∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
  [inst : DecidablePred p],
  (Finset.filter p (Roth.box r)).card =
    ∑ i ∈ Finset.range (r (Fin.last m) + 1),
      {d ∈ Roth.box (r ∘ Fin.castSucc) | p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}.card
```

- **What**: Count a filtered bounded natural multi-index box by last-coordinate sections.
- **How**: Existing finite fibre cardinality theorem; mem_box range containment; private bijection identifies each smaller filtered box.
- **Hypotheses**: m natural, arbitrary natural coordinate bounds r, arbitrary full-vector predicate p, DecidablePred p. No positivity or nonempty hypothesis.
- **Uses from project (lexical body)**: `Roth.card_filter_box_fiber_aux`, `Roth.mem_box`
- **Project references in type**: `Roth.box`
- **Native direct body references**: `Roth.box`, `Roth.card_filter_box_fiber_aux`
- **Native direct type references**: `Roth.box`
- **Used by in file (lexical)**: `Roth.card_filter_weight_le_succ_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 131–141; proof/body length 8 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_last.md).

#### lemma Roth.filter_weight_le_eq_empty

Type:

```lean
∀ {m : ℕ} (r : Fin m → ℕ) {lam : ℝ},
  ↑m < lam → {d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2} = ∅
```

- **What**: The weighted filtered box is empty when lambda is greater than the dimension.
- **How**: Combines weight_nonneg with the strictly negative threshold to contradict membership.
- **Hypotheses**: Natural rectangular bounds and λ greater than the dimension; no positivity of coordinate bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.weight_nonneg`
- **Project references in type**: `Roth.box`, `Roth.weight`
- **Native direct body references**: `Roth.box`, `Roth.weight`, `Roth.weight_nonneg`
- **Native direct type references**: `Roth.box`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.card_filter_weight_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 143–145; proof/body length 1 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.filter_weight_le_eq_empty.md).

#### lemma Roth.card_filter_fiber_eq

Type:

```lean
∀ {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ),
  ↑{d ∈ Roth.box (r ∘ Fin.castSucc) |
          Roth.weight r (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last n) i) ≤
            (↑(n + 1) - lam) / 2}.card =
    ↑{d ∈ Roth.box (r ∘ Fin.castSucc) |
          Roth.weight (r ∘ Fin.castSucc) d ≤ (↑n - (lam - 1 + 2 * ↑i / ↑(r (Fin.last n)))) / 2}.card
```

- **What**: Rewrites the weighted last-coordinate fiber as a smaller box with lambda shifted by the last-coordinate contribution.
- **How**: Uses weight_add, weight_mapDomain and weight_single, then rearranges the real expression.
- **Hypotheses**: Natural box bounds, real λ, and any chosen last coordinate. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.weight_add`, `Roth.weight_mapDomain`, `Roth.weight_single`
- **Project references in type**: `Roth.box`, `Roth.weight`
- **Native direct body references**: `Roth.box`, `Roth.weight`, `Roth.weight_add`, `Roth.weight_mapDomain`, `Roth.weight_single`
- **Native direct type references**: `Roth.box`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.card_filter_weight_le_succ_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 147–156; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_fiber_eq.md).

#### lemma Roth.card_filter_weight_le_of_le_sqrt_aux

Type:

```lean
∀ (m : ℕ) (r : Fin m → ℕ) {lam : ℝ},
  0 < lam →
    lam ≤ 2 * √↑m → ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2}.card ≤ 2 * √↑m / lam * ∏ j, (↑(r j) + 1)
```

- **What**: Bounds the weighted-filter cardinality by the lattice estimate directly when positive lambda is at most twice the square root of the dimension.
- **How**: Applies Finset.card_filter_le, card_box, and observes 2√m/λ≥1.
- **Hypotheses**: Positive λ at most 2√m; natural box bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.box`, `Roth.card_box`
- **Project references in type**: `Roth.box`, `Roth.weight`
- **Native direct body references**: `Roth.box`, `Roth.card_box`, `Roth.weight`
- **Native direct type references**: `Roth.box`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.card_filter_weight_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 158–164; proof/body length 5 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_of_le_sqrt_aux.md).

#### lemma Roth.card_filter_weight_le_succ_aux

Type:

```lean
∀ {n : ℕ} (r : Fin (n + 1) → ℕ),
  0 < r (Fin.last n) →
    0 < n →
      ∀ {lam : ℝ},
        2 * √↑(n + 1) < lam →
          (∀ {t : ℝ},
              0 < t →
                ↑{d ∈ Roth.box (r ∘ Fin.castSucc) | Roth.weight (r ∘ Fin.castSucc) d ≤ (↑n - t) / 2}.card ≤
                  2 * √↑n / t * ∏ j, (↑((r ∘ Fin.castSucc) j) + 1)) →
            ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑(n + 1) - lam) / 2}.card ≤ 2 * √↑(n + 1) / lam * ∏ j, (↑(r j) + 1)
```

- **What**: Carries the weighted lattice estimate from the smaller box to a positive last-coordinate extension in the large-lambda regime.
- **How**: Uses card_filter_box_last and card_filter_fiber_eq, applies the lower-dimensional bound in every fiber, then sum_inv_lt controls the reciprocals and Fin.prod_univ_castSucc restores the box product.
- **Hypotheses**: At least two coordinates, positive last-coordinate bound, λ>2√(n+1), and the full positive-parameter induction hypothesis for the smaller box. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.box`, `Roth.card_filter_box_last`, `Roth.card_filter_fiber_eq`, `Roth.sum_inv_lt`, `Roth.weight`
- **Project references in type**: `Roth.box`, `Roth.weight`
- **Native direct body references**: `Roth.box`, `Roth.card_filter_box_last`, `Roth.card_filter_fiber_eq`, `Roth.sum_inv_lt`, `Roth.weight`
- **Native direct type references**: `Roth.box`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.card_filter_weight_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 166–195; proof/body length 25 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_succ_aux.md).

#### theorem Roth.card_filter_weight_le

Type:

```lean
∀ (m : ℕ) (r : Fin m → ℕ),
  (∀ (j : Fin m), 0 < r j) →
    ∀ {lam : ℝ},
      0 < lam → ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2}.card ≤ 2 * √↑m / lam * ∏ j, (↑(r j) + 1)
```

- **What**: Lemma8: lower-tail count of normalized natural lattice vectors in a finite positive rectangular box is at most2sqrt(m)/lambda times total cardinality.
- **How**: Induct on dimension; filter_weight_le_eq_empty handles zero and one-dimensional empty cases, card_filter_weight_le_of_le_sqrt_aux handles the trivial count regime, and card_filter_weight_le_succ_aux combines the fibre bound with induction.
- **Hypotheses**: m natural includes0; r:Fin m→Nat; every rj positive; lambda real strictly positive. Both positivity premises essential by native counterexamples.
- **Uses from project (lexical body)**: `Roth.card_filter_weight_le_of_le_sqrt_aux`, `Roth.card_filter_weight_le_succ_aux`, `Roth.filter_weight_le_eq_empty`
- **Project references in type**: `Roth.box`, `Roth.weight`
- **Native direct body references**: `Roth.box`, `Roth.card_filter_weight_le_of_le_sqrt_aux`, `Roth.card_filter_weight_le_succ_aux`, `Roth.filter_weight_le_eq_empty`, `Roth.weight`
- **Native direct type references**: `Roth.box`, `Roth.weight`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.mul_card_filter_weight_le_aux`
- **Visibility**: public
- **Lines**: 202–218; proof/body length 15 lines.
- **Notes**: N; o;  ; s; o; r; r; y; ,;  ; T; O; D; O; ,;  ; o; r;  ; s; e; t; _; o; p; t; i; o; n;  ; i; n;  ; t; h; i; s;  ; d; e; c; l; a; r; a; t; i; o; n; .
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le.md).

#### File structural summary

- Written declarations: 13; kinds: {'theorem': 4, 'lemma': 9}
- **Key API (at least three lexical callers)**: []
- **Unused in file (observation)**: `Roth.card_filter_weight_le`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/LeanEval.lean

Completed assessments: 4/4.

#### def LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine

Type:

```lean
ℝ → Prop
```

- **What**: Uniform positive strict rational-approximation lower bound at every exponent2+epsilon; includes exact approximants and therefore implies irrationality.
- **How**: Quantified arithmetic predicate; no proof. Native generic bridge uses bounded-denominator finiteness, positive finite minimum and exponent-gap absorption.
- **Hypotheses**: x : ℝ; no algebraicity or external irrationality assumption
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`, `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 16–18; proof/body length 2 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine.md).

#### lemma LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux

Type:

```lean
∀ {x κ : ℝ},
  Irrational x → (Roth.approxSet x κ).Finite → ∃ (C : ℝ), 0 < C ∧ ∀ (p q : ℤ), 0 < q → C / ↑q ^ κ < |x - ↑p / ↑q|
```

- **What**: For an irrational real x and any real exponent kappa, finiteness of the exceptional approximation pairs gives one positive uniform strict lower-bound constant for all integer numerators and positive integer denominators.
- **How**: Minimize the scaled error over the finite exceptional set augmented by a fixed pair using Set.exists_min_image; take half its minimum and half of one, treating exceptional and nonexceptional pairs separately.
- **Hypotheses**: Irrational real and finiteness of the approximation set for the chosen real exponent. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.approxSet`
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 20–39; proof/body length 18 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux.md).

#### theorem LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff

Type:

```lean
∀ {x : ℝ},
  Irrational x →
    (LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2)
```

- **What**: For an irrational real number, uniform positive lower bounds at every exponent2+epsilon are equivalent to an upper bound2 on all exponents having infinitely many unreduced approximation pairs.
- **How**: Uses Roth.eventually_div_rpow_lt to absorb a positive constant into an epsilon half-gap, removes finitely many bounded-denominator pairs with Roth.approxSet_den_le_finite, and uses the private finite-positive-minimum helper for the reverse implication.
- **Hypotheses**: The original has Irrational x; fresh all-real proof derives it from either side and removes that binder. Real powers and positive denominators remain.
- **Uses from project (lexical body)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`, `Roth.approxSet_den_le_finite`, `Roth.eventually_div_rpow_lt`
- **Project references in type**: `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`, `Roth.approxSet`
- **Native direct body references**: `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`, `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`, `Roth.approxSet`, `Roth.approxSet_den_le_finite`, `Roth.eventually_div_rpow_lt`
- **Native direct type references**: `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`, `Roth.approxSet`
- **Used by in file (lexical)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 42–56; proof/body length 14 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff.md).

#### theorem LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth

Type:

```lean
∀ (x : ℝ), Irrational x → IsAlgebraic ℤ x → LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x
```

- **What**: Every irrational algebraic real has a positive uniform rational-approximation lower bound at every exponent2+epsilon.
- **How**: Transport algebraicity from integer to rational scalars, apply project Roth.roth, and use the finite-exception/positive-minimum equivalence isDiophantine_iff.
- **Hypotheses**: Real x; Irrational x is essential for uniform bound; IsAlgebraic ℤ x, equivalent to IsAlgebraic ℚ x
- **Uses from project (lexical body)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`, `Roth.roth`
- **Project references in type**: `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`
- **Native direct body references**: `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`, `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`, `Roth.approxSet`, `Roth.roth`
- **Native direct type references**: `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 61–64; proof/body length 2 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth.md).

#### File structural summary

- Written declarations: 4; kinds: {'def': 1, 'lemma': 1, 'theorem': 2}
- **Key API (at least three lexical callers)**: []
- **Unused in file (observation)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Main.lean

Completed assessments: 23/23.

#### def Roth.approxSet

Type:

```lean
ℝ → ℝ → Set (ℤ × ℕ)
```

- **What**: The set of unreduced integer/natural pairs whose positive supplied denominator gives strict real-power approximation error to α.
- **How**: Construct the pair set by conjunction of denominator positivity and the absolute-error bound, preserving the denominator rather than quotienting by rational equality.
- **Hypotheses**: Arbitrary real α and κ. No irrationality, algebraicity or exponent positivity assumption is part of the definition.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.approxSet_den_le_finite`, `Roth.reduction`, `Roth.approxSet_num_den_mem_aux`, `Roth.exists_reduced_approx`, `Roth.exists_approximants`, `Roth.exists_roth_approximants_aux`, `Roth.roth_of_isIntegral`, `Roth.roth`
- **Used by other files (lexical)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`, `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`
- **Visibility**: public
- **Lines**: 55–56; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.approxSet.md).

#### theorem Roth.exists_nat_mul_isIntegral

Type:

```lean
∀ {α : ℝ}, IsAlgebraic ℚ α → ∃ (M : ℕ), 0 < M ∧ IsIntegral ℤ (↑M * α)
```

- **What**: Every real number algebraic over Q has a positive natural multiple integral over Z, including0 and rational numbers.
- **How**: Transfer Q algebraicity to Z, choose a nonzero integral scalar multiple, replace its sign using natAbs. Existing exists_nsmul_eq and canonical natDenominator provide stronger direct APIs.
- **Hypotheses**: Only IsAlgebraic Q alpha; no irrationality, nonzero alpha, order or topology is mathematically necessary.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.reduction`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 62–66; proof/body length 4 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_nat_mul_isIntegral.md).

#### theorem Roth.approxSet_den_le_finite

Type:

```lean
∀ (α κ : ℝ) (Q₀ : ℕ), {hq : ℤ × ℕ | hq ∈ Roth.approxSet α κ ∧ hq.2 ≤ Q₀}.Finite
```

- **What**: For every real center and real exponent, only finitely many supplied positive integer-denominator approximating pairs have denominator at most a fixed natural bound.
- **How**: Contain pairs in a finite rectangle: Finset.single_le_sum bounds the error radii, triangle inequality bounds numerator size, and Int.le_ceil converts the real bound into a finite integer interval.
- **Hypotheses**: Arbitrary real α and κ, arbitrary natural Q. No irrationality, algebraicity, positivity ofκ, or coprimality. Positive supplied denominator is part of approxSet.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.reduction`, `Roth.exists_reduced_approx`
- **Used by other files (lexical)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`
- **Visibility**: public
- **Lines**: 73–96; proof/body length 24 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.approxSet_den_le_finite.md).

#### theorem Roth.eventually_div_rpow_lt

Type:

```lean
∀ {M κ κ' : ℝ}, κ' < κ → ∃ (Q₀ : ℕ), ∀ (q : ℕ), Q₀ < q → M / ↑q ^ κ < 1 / ↑q ^ κ'
```

- **What**: A fixed real amplitude is eventually absorbed by a strict real exponent gap on natural denominators.
- **How**: Compose real-power divergence with natural casts, extract a tail, then normalize using positivity and rpow_sub.
- **Hypotheses**: κprime < κ; M arbitrary real; exponents arbitrary real
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.reduction`, `Roth.exists_reduced_approx`
- **Used by other files (lexical)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`
- **Visibility**: public
- **Lines**: 103–110; proof/body length 7 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.eventually_div_rpow_lt.md).

#### theorem Roth.reduction

Type:

```lean
∀ {α : ℝ},
  Irrational α →
    IsAlgebraic ℚ α →
      ∀ {κ : ℝ},
        2 < κ →
          (Roth.approxSet α κ).Infinite →
            ∃ (α' : ℝ) (κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧ (Roth.approxSet α' κ').Infinite
```

- **What**: An infinite approximation counterexample above exponent2 transfers from an irrational real algebraic number to an irrational real algebraic integer, with a potentially smaller exponent still above2.
- **How**: Choose a positive integral multiple with exists_nat_mul_isIntegral; eventually_div_rpow_lt absorbs numerator scaling at the midpoint exponent. Remove the finite bounded-denominator slice, map (h,q) to (M*h,q) injectively, and compare errors.
- **Hypotheses**: Irrational α, algebraicity over Q, exponent κ>2, and infinitely many unreduced integer/natural pairs satisfying the fixed unit-constant approximation bound.
- **Uses from project (lexical body)**: `Roth.approxSet_den_le_finite`, `Roth.eventually_div_rpow_lt`, `Roth.exists_nat_mul_isIntegral`
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`, `Roth.approxSet_den_le_finite`, `Roth.eventually_div_rpow_lt`, `Roth.exists_nat_mul_isIntegral`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.roth`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 118–134; proof/body length 15 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.reduction.md).

#### theorem Roth.exists_monic_aeval_eq_zero

Type:

```lean
∀ {α : ℝ},
  IsIntegral ℤ α → ∃ (f : Polynomial ℤ), f.Monic ∧ (Polynomial.aeval α) f = 0 ∧ 2 ≤ f.natDegree
```

- **What**: Every integral real number has a monic integer annihilator of degree at least two; witness may be reducible and nonminimal.
- **How**: Extract a monic annihilator from integrality and multiply by X squared. Monicity is preserved, evaluation remains zero, and the degree increases by two.
- **Hypotheses**: Only integrality over ℤ; no irrationality. Nontrivial coefficient ring supports degree inflation in the general form.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_roth_parameters_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 142–147; proof/body length 5 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_monic_aeval_eq_zero.md).

#### theorem Roth.approxSet_num_den_mem_aux

Type:

```lean
∀ {α κ : ℝ},
  0 ≤ κ → ∀ {h : ℤ} {q : ℕ}, (h, q) ∈ Roth.approxSet α κ → ((↑h / ↑q).num, (↑h / ↑q).den) ∈ Roth.approxSet α κ
```

- **What**: Reducing a rational approximation to its canonical numerator and denominator preserves membership in approxSet for nonnegative approximation exponent.
- **How**: Use Rat.den_dvd to bound its reduced denominator and monotonicity of the nonnegative-exponent reciprocal power; Rat.cast_def identifies its value.
- **Hypotheses**: Nonnegative exponent and an approximation pair with positive denominator. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.exists_reduced_approx`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 149–156; proof/body length 7 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.approxSet_num_den_mem_aux.md).

#### theorem Roth.exists_reduced_approx

Type:

```lean
∀ {α : ℝ},
  Irrational α →
    ∀ {κ : ℝ},
      0 < κ → (Roth.approxSet α κ).Infinite → ∀ (Q₀ : ℕ), ∃ hq ∈ Roth.approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 ↑hq.2
```

- **What**: Infinitely many fixed-quality approximating pairs to an irrational real yield reduced approximants beyond every natural denominator threshold.
- **How**: Canonicalize rational values; bounded reduced denominator would give finite image; positive irrational error and power decay make each original rational-value fiber finite; finite-fiber criterion contradicts supplied infinity.
- **Hypotheses**: Irrational α; real exponentκ; 0<κ currently, independently droppable; infinite approxSet α κ; arbitrary natural thresholdQ₀
- **Uses from project (lexical body)**: `Roth.approxSet`, `Roth.approxSet_den_le_finite`, `Roth.approxSet_num_den_mem_aux`, `Roth.eventually_div_rpow_lt`
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`, `Roth.approxSet_den_le_finite`, `Roth.approxSet_num_den_mem_aux`, `Roth.eventually_div_rpow_lt`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.exists_approximants`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 164–189; proof/body length 24 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_reduced_approx.md).

#### theorem Roth.exists_m

Type:

```lean
∀ {n : ℕ} {κ : ℝ},
  2 < κ → ∃ (m : ℕ), 16 * n ^ 2 < m ∧ 4 * ↑n * √↑m < ↑m ∧ 2 * ↑m / (↑m - 4 * ↑n * √↑m) < κ
```

- **What**: Chooses a natural dimension m satisfying a large-square bound, a positive denominator bound and exponent quotient<κ for any n, including0.
- **How**: Choose natural s beyond ceiling4κn/(κ−2) plus4n+1, setm=s²; square-root cancellation and positive-denominator multiplication prove the three inequalities.
- **Hypotheses**: n:ℕ arbitrary, including0; κ:ℝ with2<κ
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_roth_parameters_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 196–218; proof/body length 22 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_m.md).

#### theorem Roth.exists_delta

Type:

```lean
∀ {n m : ℕ},
  16 * n ^ 2 < m →
    ∀ {κ : ℝ},
      2 * ↑m / (↑m - 4 * ↑n * √↑m) < κ →
        ∃ (δ : ℝ),
          0 < δ ∧
            δ < 1 / ↑m ∧
              Roth.eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2 ∧
                ↑m * (1 + 4 * δ) / (Roth.gam δ n m - Roth.eta δ m) < κ
```

- **What**: Chooses δ>0 below1/m with both the strict eta/square-root envelope and the gamma-minus-eta quotient bound, given the fixed dimension and strict limiting quotient slack.
- **How**: Reuse exists_delta_bound for an interval including0, prove continuity of the rpow/gamma/eta quotient at0 using the positive gap, obtain a metric radius, and choose a positive point below both radii.
- **Hypotheses**: Natural n,m with16*n²<m; n=0 allowed; m is consequently positive.; Real κ satisfying2m/(m-4n√m)<κ; no separate κ>2 premise.
- **Uses from project (lexical body)**: `Roth.eta`, `Roth.eta_lt_gam_iff`, `Roth.exists_delta_bound`, `Roth.gam`, `Roth.lam`
- **Project references in type**: `Roth.eta`, `Roth.gam`
- **Native direct body references**: `Roth.eta`, `Roth.eta_lt_gam_iff`, `Roth.exists_delta_bound`, `Roth.gam`, `Roth.lam`
- **Native direct type references**: `Roth.eta`, `Roth.gam`
- **Used by in file (lexical)**: `Roth.exists_roth_parameters_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 227–249; proof/body length 20 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_delta.md).

#### theorem Roth.exists_approximants

Type:

```lean
∀ {α : ℝ},
  Irrational α →
    ∀ {κ : ℝ},
      0 < κ →
        (Roth.approxSet α κ).Infinite →
          ∀ (m : ℕ) [inst : NeZero m] {δ : ℝ} (L : ℝ),
            ∃ (h : Fin m → ℤ) (q : Fin m → ℕ),
              (∀ (j : Fin m), (h j, q j) ∈ Roth.approxSet α κ) ∧
                (∀ (j : Fin m), IsCoprime (h j) ↑(q j)) ∧
                  (∀ (j : Fin m), 1 < q j) ∧
                    L < Real.log ↑(q 0) ∧ ∀ (i j : Fin m), ↑i + 1 = ↑j → 2 / δ * Real.log ↑(q i) < Real.log ↑(q j)
```

- **What**: Selects a nonempty finite family of reduced approximants with q>1, arbitrary strict initial log threshold and consecutive log-gap factor2/δ; δ may be any real.
- **How**: Use exists_reduced_approx as an unbounded-denominator selector, recurse beyond ceil(exp L) initially and beyond each powered denominator, then transport strict denominator bounds through Real.lt_log_of_rpow_lt.
- **Hypotheses**: Irrational real α, positive κ and infinitely many pairs in approxSet α κ in current signature; positivity ofκ verified removable.; Nonzero natural m; arbitrary realδ andL.
- **Uses from project (lexical body)**: `Roth.approxSet`, `Roth.exists_reduced_approx`
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`, `Roth.exists_reduced_approx`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.exists_roth_approximants_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 256–275; proof/body length 16 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_approximants.md).

#### theorem Roth.exists_degrees

Type:

```lean
∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
  0 < δ →
    δ ≤ 1 →
      ∀ {q : Fin m → ℕ},
        (∀ (j : Fin m), 1 < q j) →
          (∀ (i j : Fin m), ↑i + 1 = ↑j → 2 / δ * Real.log ↑(q i) ≤ Real.log ↑(q j)) →
            ∃ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) ∧
                (∀ (j : Fin m), 10 / δ < ↑(r j)) ∧
                  (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ < ↑(r i)) ∧
                    (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) ∧
                      ∀ (j : Fin m), ↑(r j) * Real.log ↑(q j) < (1 + δ / 10) * (↑(r 0) * Real.log ↑(q 0))
```

- **What**: Choose positive natural degrees, larger than10/δ, with strict adjacent ratio and simultaneous weak-lower/strict-upper balanced logarithmic products.
- **How**: Use exists_nat_gt above a finite supremum, then Nat.le_ceil and Nat.ceil_lt_add_one on ceil(s*log(q0)/log(qj)); positivity transports bounds and the factor2 preserves strict separation.
- **Hypotheses**: Nonzero finite dimension, δ>0 with original δ≤1, denominators qj>1 and weak adjacent logarithm growth2/δ.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_roth_approximants_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 282–317; proof/body length 31 lines.
- **Notes**: proof/body >30 lines
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_degrees.md).

#### theorem Roth.one_le_prod_pow_mul_abs_eval

Type:

```lean
∀ {m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ},
  (∀ (j : Fin m), degreeOf j Q ≤ r j) →
    ∀ (h : Fin m → ℤ) {q : Fin m → ℕ},
      (∀ (j : Fin m), 0 < q j) →
        (eval fun (j : Fin m) ↦ ↑(h j) / ↑(q j)) ((map (Int.castRingHom ℝ)) Q) ≠ 0 →
          1 ≤ (∏ j : Fin m, ↑(q j) ^ r j) * |(eval fun (j : Fin m) ↦ ↑(h j) / ↑(q j)) ((map (Int.castRingHom ℝ)) Q)|
```

- **What**: A nonzero integer multivariate polynomial value at rational coordinates has absolute value at least the reciprocal of the product of denominators raised to coordinate degree bounds.
- **How**: Constructs the integer numerator N by summing cleared monomials; MvPolynomial.monomial_le_degreeOf bounds exponents and MvPolynomial.eval_eq' identifies its cast with the scaled evaluation. Nonvanishing and Int.one_le_abs then give the lower bound.
- **Hypotheses**: Integer coefficients; coordinate degree bounds r; positive natural denominators; nonzero evaluation. No coprimality, algebraicity, irrationality, nonempty dimension or positive degree hypothesis.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.one_lt_roth_eval_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 324–344; proof/body length 18 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.one_le_prod_pow_mul_abs_eval.md).

#### lemma Roth.abs_prod_pow_le_rpow_of_le_weight

Type:

```lean
∀ {m : ℕ} [inst : NeZero m] {r q : Fin m → ℕ},
  (∀ (j : Fin m), 0 < q j) →
    ∀ {κ : ℝ},
      0 ≤ κ →
        ∀ {x : Fin m → ℝ},
          (∀ (j : Fin m), |x j| ≤ 1 / ↑(q j) ^ κ) →
            (∀ (j : Fin m), ↑(q 0) ^ (↑(r 0) / ↑(r j)) ≤ ↑(q j)) →
              ∀ (d : Fin m →₀ ℕ) {c : ℝ}, c ≤ Roth.weight r d → |∏ j : Fin m, x j ^ d j| ≤ ↑(q 0) ^ (-↑(r 0) * c * κ)
```

- **What**: Converts coordinatewise rational-approximation errors and denominator growth into decay of a monomial controlled by its weighted degree.
- **How**: Compare products coordinatewise, use Real.rpow_le_rpow_of_nonpos for denominator growth, combine exponents with Real.rpow_sum_of_pos and use the weight cutoff.
- **Hypotheses**: Nonzero dimension, positive denominators, nonnegative approximation exponent and coordinate error/denominator-growth bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: `Roth.abs_eval_lt_of_le_index`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 347–371; proof/body length 22 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_prod_pow_le_rpow_of_le_weight.md).

#### theorem Roth.abs_eval_lt_of_le_index

Type:

```lean
∀ {m : ℕ} [inst : NeZero m] {Q : MvPolynomial (Fin m) ℝ} {r : Fin m → ℕ},
  (∀ (j : Fin m), degreeOf j Q ≤ r j) →
    ∀ {α c : ℝ},
      c ≤ Roth.index Q (fun (x : Fin m) ↦ α) r →
        ∀ {h : Fin m → ℤ} {q : Fin m → ℕ},
          (∀ (j : Fin m), 0 < q j) →
            ∀ {κ : ℝ},
              0 ≤ κ →
                (∀ (j : Fin m), |α - ↑(h j) / ↑(q j)| ≤ 1 / ↑(q j) ^ κ) →
                  (∀ (j : Fin m), ↑(q 0) ^ (↑(r 0) / ↑(r j)) ≤ ↑(q j)) →
                    ∀ {C : ℝ},
                      (∀ (i : Fin m →₀ ℕ), |(eval fun (x : Fin m) ↦ α) ((hasseDeriv i) Q)| < C) →
                        |(eval fun (j : Fin m) ↦ ↑(h j) / ↑(q j)) Q| <
                          (∏ j : Fin m, (↑(r j) + 1)) * C * ↑(q 0) ^ (-↑(r 0) * c * κ)
```

- **What**: Strict quantitative Taylor upper estimate from index lower bound, uniform Hasse derivative coefficient bound and approximation/denominator growth.
- **How**: Expand over degree box, discard low-weight nonzero coefficients via index, bound error products by real-power decay, then sum strict termwise bounds over a nonempty box.
- **Hypotheses**: argument: m, NeZero m, Fin m; verdict: generalize; evidence: Finite σ possibly empty in own generic/cost_bound; NeZero required only by original distinguished coordinate0.; argument: Q real coefficients; verdict: generalize; evidence: NormedField and NormedCommRing + NormOneClass shifted polynomial expansion tested; project Hasse/index remains real-specific, not falsely claimed ported.; argument: r natural coordinate degrees, hd; verdict: retain box, abstract expansion also possible; evidence: Natural exponents/degree upper bounds give finite box and cardinal product. Arbitrary s.Nonempty works for expansion form; no positive degree condition.; argument: α common center; verdict: generalize; evidence: Arbitrary a:σ→ℝ or K in generic proof.; argument: c, hidx; verdict: semantic cost lower bound; evidence: Nonzero expansion coefficients imply c≤Σ μj*dj; original recovery rescales c to r0*c*κ and uses index_le_weight. No Q≠0.; argument: h integral numerator; verdict: remove representation; evidence: Arbitrary x:σ→ℝ/K; exact h/q evaluation recovered.; argument: q positive natural, hq; verdict: abstract to b≥1 and radii; evidence: b≥1 supplies positive base and exponent monotonicity; coordinate radius b^(-μj) need only satisfy actual error bound.; argument: κ nonnegative, happ, hqr; verdict: replace by semantic cost/radius bounds; evidence: Original bridge proven using Real.rpow_le_rpow_of_nonpos; μ arbitrary real in generic, no positivity assumption needed beyond actual error bound.; argument: C and all-index hC; verdict: localize; evidence: Only d∈box r needed; box nonempty by0; C>0 derived rather than hypothesized.
- **Uses from project (lexical body)**: `MvPolynomial.eval_eq_sum_box`, `MvPolynomial.hasseDeriv`, `Roth.abs_prod_pow_le_rpow_of_le_weight`, `Roth.box`, `Roth.card_box`, `Roth.index_le_weight`, `Roth.mem_box`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`
- **Native direct body references**: `MvPolynomial.eval_eq_sum_box`, `MvPolynomial.hasseDeriv`, `Roth.abs_prod_pow_le_rpow_of_le_weight`, `Roth.box`, `Roth.card_box`, `Roth.index`, `Roth.index_le_weight`, `Roth.mem_box`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`
- **Used by in file (lexical)**: `Roth.one_lt_roth_eval_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 380–407; proof/body length 21 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_lt_of_le_index.md).

#### lemma Roth.exists_roth_parameters_aux

Type:

```lean
∀ {α κ : ℝ},
  IsIntegral ℤ α →
    2 < κ →
      ∃ (f : Polynomial ℤ) (A : ℝ) (m : ℕ) (δ : ℝ),
        f.Monic ∧
          (Polynomial.aeval α) f = 0 ∧
            1 ≤ A ∧
              (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) ∧
                2 ≤ m ∧
                  0 < δ ∧
                    δ < 1 / ↑m ∧
                      Roth.eta δ m + 2 * (1 + 3 * δ) * ↑f.natDegree * √↑m < ↑m / 2 ∧
                        ↑m * (1 + 4 * δ) / (Roth.gam δ f.natDegree m - Roth.eta δ m) < κ
```

- **What**: Packages a monic integer equation, coefficient bound, dimension and small positive delta satisfying the numerical constraints for the final contradiction.
- **How**: Use exists_monic_aeval_eq_zero, bound all coefficients by their absolute sum plus one, and combine exists_m with exists_delta.
- **Hypotheses**: Real algebraic integer and exponent above two. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.exists_delta`, `Roth.exists_m`, `Roth.exists_monic_aeval_eq_zero`
- **Project references in type**: `Roth.eta`, `Roth.gam`
- **Native direct body references**: `Roth.eta`, `Roth.exists_delta`, `Roth.exists_m`, `Roth.exists_monic_aeval_eq_zero`, `Roth.gam`
- **Native direct type references**: `Roth.eta`, `Roth.gam`
- **Used by in file (lexical)**: `Roth.roth_of_isIntegral`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 410–426; proof/body length 13 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_roth_parameters_aux.md).

#### lemma Roth.exists_roth_approximants_aux

Type:

```lean
∀ {α κ : ℝ},
  Irrational α →
    0 < κ →
      (Roth.approxSet α κ).Infinite →
        ∀ (m : ℕ) [inst : NeZero m] {δ : ℝ},
          0 < δ →
            δ ≤ 1 →
              ∀ (A : ℝ),
                ∃ (h : Fin m → ℤ) (q : Fin m → ℕ) (r : Fin m → ℕ),
                  (∀ (j : Fin m), (h j, q j) ∈ Roth.approxSet α κ) ∧
                    (∀ (j : Fin m), IsCoprime (h j) ↑(q j)) ∧
                      (∀ (j : Fin m), 1 < q j) ∧
                        (∀ (j : Fin m), 0 < r j) ∧
                          3 ≤ r (Fin.rev 0) ∧
                            (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ ≤ ↑(r i)) ∧
                              (∀ (j : Fin m), r j ≤ r 0) ∧
                                2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) <
                                    δ ^ 2 * Real.log ↑(q 0) ∧
                                  (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) ∧
                                    ∀ (j : Fin m), ↑(r j) * Real.log ↑(q j) < (1 + δ / 10) * (↑(r 0) * Real.log ↑(q 0))
```

- **What**: Packages reduced approximants with rapidly growing denominators and compatible positive antitone degrees, including all ratio and logarithmic bounds used later.
- **How**: Combine exists_approximants with exists_degrees; use Fin.antitone_iff_succ_le to derive monotonicity and strengthen the final degree bound.
- **Hypotheses**: Irrational number, positive exponent, infinite approximation set, nonzero dimension and positive delta at most one. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.exists_approximants`, `Roth.exists_degrees`
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`, `Roth.exists_approximants`, `Roth.exists_degrees`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.roth_of_isIntegral`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 429–450; proof/body length 15 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_roth_approximants_aux.md).

#### lemma Roth.one_lt_roth_eval_bound_aux

Type:

```lean
∀ {α κ : ℝ} {f : Polynomial ℤ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      ∀ {A : ℝ},
        (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
          ∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
            0 ≤ δ →
              δ ≤ 1 / ↑m →
                ∀ {r : Fin m → ℕ},
                  (∀ (j : Fin m), 0 < r j) →
                    3 ≤ r (Fin.rev 0) →
                      (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ ≤ ↑(r i)) →
                        ∀ {q : Fin m → ℕ},
                          (∀ (j : Fin m), 0 < q j) →
                            0 ≤ κ →
                              ∀ {h : Fin m → ℤ},
                                (∀ (j : Fin m), |α - ↑(h j) / ↑(q j)| ≤ 1 / ↑(q j) ^ κ) →
                                  (∀ (j : Fin m), IsCoprime (h j) ↑(q j)) →
                                    2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤
                                        δ ^ 2 * Real.log ↑(q 0) →
                                      (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                                        1 <
                                          (∏ j : Fin m, ↑(q j) ^ r j) *
                                            ((∏ j : Fin m, (↑(r j) + 1)) *
                                                ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ^ (1 + 3 * δ) *
                                              ↑(q 0) ^ (-↑(r 0) * (Roth.gam δ f.natDegree m - Roth.eta δ m) * κ))
```

- **What**: Combines the nonzero integer-value lower bound with the Taylor upper bound for the auxiliary polynomial, giving a strict scalar product bound greater than1.
- **How**: Apply main_lemma, derive denominator-growth powers via Real.rpow_le_iff_le_log, then combine one_le_prod_pow_mul_abs_eval with abs_eval_lt_of_le_index.
- **Hypotheses**: Monic integer equation, coefficient bounds, positive degrees/denominators, small delta, coprime approximants, nonnegative exponent and numerical parameter bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.abs_eval_lt_of_le_index`, `Roth.main_lemma`, `Roth.one_le_prod_pow_mul_abs_eval`
- **Project references in type**: `Roth.eta`, `Roth.gam`, `Roth.mainCoeffBound`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.abs_eval_lt_of_le_index`, `Roth.eta`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`, `Roth.main_lemma`, `Roth.one_le_prod_pow_mul_abs_eval`
- **Native direct type references**: `Roth.eta`, `Roth.gam`, `Roth.mainCoeffBound`
- **Used by in file (lexical)**: `Roth.roth_of_isIntegral`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 453–478; proof/body length 16 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.one_lt_roth_eval_bound_aux.md).

#### lemma Roth.roth_product_bound_aux

Type:

```lean
∀ {m : ℕ} [inst : NeZero m] {α A δ : ℝ},
  0 ≤ δ →
    0 ≤ A →
      ∀ {q r : Fin m → ℕ},
        0 < r 0 →
          (∀ (j : Fin m), r j ≤ r 0) →
            2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑(q 0) →
              0 < ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ∧
                ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ≤ ↑(q 0) ^ (δ * ↑(r 0)) ∧
                  ∏ j : Fin m, (↑(r j) + 1) < ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ^ δ
```

- **What**: Bounds the natural-floor coefficient scale from above and away from zero, and bounds the product of degree factors strictly by its delta power.
- **How**: Use four_lt_rpow and sqrt_lt_floor for the coefficient scale; bound each degree-plus-one by two to the maximal degree and apply three_small_factors.
- **Hypotheses**: Nonzero dimension, nonnegative delta/coefficient bound, positive maximal first degree and combined logarithmic bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.four_lt_rpow`, `Roth.sqrt_lt_floor`, `Roth.three_small_factors`
- **Project references in type**: `Roth.mainCoeffBound`
- **Native direct body references**: `Roth.four_lt_rpow`, `Roth.mainCoeffBound`, `Roth.sqrt_lt_floor`, `Roth.three_small_factors`
- **Native direct type references**: `Roth.mainCoeffBound`
- **Used by in file (lexical)**: `Roth.roth_of_isIntegral`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 481–502; proof/body length 17 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.roth_product_bound_aux.md).

#### lemma Roth.roth_log_bound_aux

Type:

```lean
∀ {m : ℕ} [inst : NeZero m],
  2 ≤ m →
    ∀ {δ G κ B : ℝ},
      δ ≤ 1 →
        ∀ {q r : Fin m → ℕ},
          (∀ (j : Fin m), 1 < q j) →
            (∀ (j : Fin m), ↑(r j) * Real.log ↑(q j) < (1 + δ / 10) * (↑(r 0) * Real.log ↑(q 0))) →
              0 < B →
                B ≤ ↑(q 0) ^ (δ * ↑(r 0)) →
                  ∏ j : Fin m, (↑(r j) + 1) < B ^ δ →
                    1 <
                        (∏ j : Fin m, ↑(q j) ^ r j) *
                          ((∏ j : Fin m, (↑(r j) + 1)) * B ^ (1 + 3 * δ) * ↑(q 0) ^ (-↑(r 0) * G * κ)) →
                      G * κ < ↑m * (1 + 4 * δ)
```

- **What**: From the strict scalar evaluation product bound and balanced denominator logarithms, deduces G*kappa<m*(1+4delta).
- **How**: Use Real.log_mul, Real.log_prod and Real.log_rpow, bound the denominator-log sum by balanced products, and combine the coefficient/degree-factor estimates.
- **Hypotheses**: Dimension at least two, delta at most one, denominators above one, positive coefficient scale, balanced logarithmic bounds and explicit product expression above one. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.roth_of_isIntegral`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 505–541; proof/body length 32 lines.
- **Notes**: proof/body >30 lines
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.roth_log_bound_aux.md).

#### theorem Roth.roth_of_isIntegral

Type:

```lean
∀ {α : ℝ}, Irrational α → IsIntegral ℤ α → ∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite → κ ≤ 2
```

- **What**: Roth’s theorem for irrational real algebraic integers: infinitely many integer/natural pair approximations force exponent at most2.
- **How**: Choose monic equation, m and δ via exists_roth_parameters_aux; choose reduced approximants and balanced degrees; combine main_lemma, cleared-denominator integer lower bound and Taylor upper bound; roth_log_bound_aux contradicts the exponent gap.
- **Hypotheses**: Real α irrational; α integral over ℤ; Approximation set of positive-denominator integer/natural pairs infinite at real exponent κ
- **Uses from project (lexical body)**: `Roth.eta_lt_gam_iff`, `Roth.exists_roth_approximants_aux`, `Roth.exists_roth_parameters_aux`, `Roth.one_lt_roth_eval_bound_aux`, `Roth.roth_log_bound_aux`, `Roth.roth_product_bound_aux`
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`, `Roth.eta`, `Roth.eta_lt_gam_iff`, `Roth.exists_roth_approximants_aux`, `Roth.exists_roth_parameters_aux`, `Roth.gam`, `Roth.mainCoeffBound`, `Roth.one_lt_roth_eval_bound_aux`, `Roth.roth_log_bound_aux`, `Roth.roth_product_bound_aux`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.roth`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 547–563; proof/body length 16 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.roth_of_isIntegral.md).

#### theorem Roth.roth

Type:

```lean
∀ {α : ℝ}, Irrational α → IsAlgebraic ℚ α → ∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite → κ ≤ 2
```

- **What**: Roth’s theorem for irrational real algebraic numbers: infinitely many unreduced positive-denominator pair approximations force exponent at most2.
- **How**: Assume κ>2, clear denominators to obtain a positive integer multiple of α integral over ℤ, absorb that factor by lowering κ to κ′∈(2,κ), then contradict the integral Roth theorem. Its underlying multivariate auxiliary-polynomial argument compares integral lower and Taylor upper bounds.
- **Hypotheses**: Irrational real α; α algebraic over ℚ; Infinite set of integer/natural pairs with q>0 and |α−h/q|<q^(−κ), arbitrary real κ
- **Uses from project (lexical body)**: `Roth.reduction`, `Roth.roth_of_isIntegral`
- **Project references in type**: `Roth.approxSet`
- **Native direct body references**: `Roth.approxSet`, `Roth.reduction`, `Roth.roth_of_isIntegral`
- **Native direct type references**: `Roth.approxSet`
- **Used by in file (lexical)**: `Roth.roth_rat`
- **Used by other files (lexical)**: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`
- **Visibility**: public
- **Lines**: 573–577; proof/body length 4 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.roth.md).

#### theorem Roth.roth_rat

Type:

```lean
∀ {α : ℝ},
  Irrational α → IsAlgebraic ℚ α → ∀ {κ : ℝ}, {x : ℚ | |α - ↑x| < 1 / ↑x.den ^ κ}.Infinite → κ ≤ 2
```

- **What**: Infinitely many distinct rational approximations to an irrational algebraic real, measured by reduced denominator, force exponent at most two.
- **How**: Inject rationals into numerator/denominator pairs via Rat.ext; Rat.cast_def identifies their real error, allowing Roth.roth to bound the exponent.
- **Hypotheses**: Real target irrational and algebraic over the rationals, real exponent, infinitely many rational values satisfying the strict unit-coefficient estimate.
- **Uses from project (lexical body)**: `Roth.roth`
- **Project references in type**: []
- **Native direct body references**: `Roth.approxSet`, `Roth.roth`
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 581–586; proof/body length 5 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.roth_rat.md).

#### File structural summary

- Written declarations: 23; kinds: {'def': 1, 'theorem': 16, 'lemma': 6}
- **Key API (at least three lexical callers)**: `Roth.approxSet`, `Roth.approxSet_den_le_finite`, `Roth.eventually_div_rpow_lt`
- **Unused in file (observation)**: `Roth.roth_rat`
- **Proofs over 30 lines**: `Roth.exists_degrees`, `Roth.roth_log_bound_aux`
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/MainLemma.lean

Completed assessments: 38/38.

#### def Roth.lam

Type:

```lean
ℝ → ℕ → ℕ → ℝ
```

- **What**: Defines the explicit real cutoff λ(δ,n,m)=4(1+3δ)n√m chosen in Roth’s auxiliary-polynomial construction.
- **How**: Forms the delta-dependent coefficient-loss factor 1+3δ, scales it by four and the polynomial degree, and multiplies by the square root of the number of variables. The choice converts the lattice-count factor 2√m/λ into the half-budget bound needed for pigeonholing.
- **Hypotheses**: Any real δ and natural degree n and dimension m; no positivity hypotheses. The definition is total, including δ<0 and n=0 or m=0.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.gam`, `Roth.eta_lt_gam_iff`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`
- **Used by other files (lexical)**: `Roth.exists_delta`
- **Visibility**: public
- **Lines**: 60–60; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.lam.md).

#### def Roth.gam

Type:

```lean
ℝ → ℕ → ℕ → ℝ
```

- **What**: Defines gamma as half the dimension minus half of lambda, the high-index threshold in the Roth main lemma.
- **How**: Uses the chosen loss Roth.lam, subtracts it from the real dimension and divides by two.
- **Hypotheses**: An arbitrary real δ and natural n,m; no sign or nonzero hypotheses. Positivity is proved separately in the admissible parameter range.
- **Uses from project (lexical body)**: `Roth.lam`
- **Project references in type**: []
- **Native direct body references**: `Roth.lam`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.eta_lt_gam_iff`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.main_lemma`
- **Used by other files (lexical)**: `Roth.exists_delta`, `Roth.exists_roth_parameters_aux`, `Roth.one_lt_roth_eval_bound_aux`
- **Visibility**: public
- **Lines**: 63–63; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.gam.md).

#### def Roth.eta

Type:

```lean
ℝ → ℕ → ℝ
```

- **What**: Defines the chosen dyadic small-index error eta(δ,m)=10^m δ^((1/2)^m) used in the main lemma index gap.
- **How**: Multiplies ten to the natural dimension by a real power whose exponent is the dimension-th power of one half.
- **Hypotheses**: Arbitrary real δ and natural m; no sign, positivity, or nonzero assumptions. The iterated nonnegative-root interpretation requires δ≥0.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_delta_bound`, `Roth.eta_lt_gam_iff`, `Roth.theta_lt_eta_of_sq_log_bound_aux`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.main_lemma`
- **Used by other files (lexical)**: `Roth.exists_delta`, `Roth.exists_roth_parameters_aux`, `Roth.one_lt_roth_eval_bound_aux`
- **Visibility**: public
- **Lines**: 66–66; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.eta.md).

#### def Roth.mainCoeffBound

Type:

```lean
ℝ → ℕ → ℕ → ℕ
```

- **What**: Chooses the natural coefficient cutoff B₁=⌊q₁^(δr₁)⌋ for the main lemma counting argument.
- **How**: Applies the existing natural floor to a real power with exponent δ times the natural degree cast to ℝ.
- **Hypotheses**: Any real δ and natural q₁,r₁, with no positivity hypotheses; zero exponent yields1 even at q₁=0, whereas q₁>1,r₁>0,δ<0 yields0.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.mul_log_div_two_lt_log_mainCoeffBound`, `Roth.three_small_factors`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.main_lemma`
- **Used by other files (lexical)**: `Roth.one_lt_roth_eval_bound_aux`, `Roth.roth_product_bound_aux`
- **Visibility**: public
- **Lines**: 69–69; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.mainCoeffBound.md).

#### def Roth.boxFamily

Type:

```lean
{σ : Type u_1} → (σ → ℕ) → ℕ → Set (MvPolynomial σ ℤ)
```

- **What**: Integer multivariate polynomials with coordinate degrees bounded by r and every coefficient in [0,B], including zero.
- **How**: Form a Set by combining coordinate-degree bounds and coefficient interval membership.
- **Hypotheses**: Arbitrary variable type, natural coordinate bounds and natural coefficient bound; no finite-support or positivity premise.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.boxFamily_eq_image_finsupp_aux`, `Roth.boxFamily_finite`, `Roth.ncard_boxFamily`, `Roth.exists_ne_modByMonic_eq`, `Roth.sub_mem_RSet`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 275–276; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.boxFamily.md).

#### theorem Roth.exists_delta_bound

Type:

```lean
∀ {n m : ℕ},
  16 * n ^ 2 < m →
    ∃ (δ₀ : ℝ), 0 < δ₀ ∧ ∀ (δ : ℝ), 0 ≤ δ → δ ≤ δ₀ → δ < 1 / ↑m ∧ Roth.eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2
```

- **What**: For each fixed natural m>16n², a positive δ₀ makes δ<1/m and η(δ,m)+2(1+3δ)n√m<m/2 hold simultaneously for every δ in the closed interval [0,δ₀].
- **How**: Derive the strict square-root gap at zero using Real.lt_sqrt_of_sq_lt; apply Real.continuousAt_rpow_const and ContinuousAt.eventually_lt, extract a radius with Metric.eventually_nhds_iff, then shrink it by a half-minimum.
- **Hypotheses**: A nonnegative natural degree parameter n, with n=0 allowed.; A fixed natural dimension m strictly greater than sixteen times the square of n; this strict threshold is verified necessary and sufficient for the closed-interval conclusion.
- **Uses from project (lexical body)**: `Roth.eta`
- **Project references in type**: `Roth.eta`
- **Native direct body references**: `Roth.eta`
- **Native direct type references**: `Roth.eta`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.exists_delta`
- **Visibility**: public
- **Lines**: 77–93; proof/body length 16 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_delta_bound.md).

#### theorem Roth.eta_lt_gam_iff

Type:

```lean
∀ (δ : ℝ) (n m : ℕ),
  Roth.eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2 ↔ Roth.eta δ m < Roth.gam δ n m
```

- **What**: The numerical small-delta inequality (30) is equivalent to eta being smaller than gamma.
- **How**: Unfold gamma and lambda, distribute division over subtraction, and collect the scalar factor: half of the lambda term is the error term in (30).
- **Hypotheses**: No sign, nonzero-dimension, or degree assumptions: delta is any real and n,m are arbitrary naturals.
- **Uses from project (lexical body)**: `Roth.gam`, `Roth.lam`
- **Project references in type**: `Roth.eta`, `Roth.gam`
- **Native direct body references**: []
- **Native direct type references**: `Roth.eta`, `Roth.gam`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.exists_delta`, `Roth.roth_of_isIntegral`
- **Visibility**: public
- **Lines**: 100–102; proof/body length 2 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.eta_lt_gam_iff.md).

#### lemma Roth.sqrt_lt_nat_floor_aux

Type:

```lean
∀ {X : ℝ}, 2 ≤ X → √X < ↑⌊X⌋₊
```

- **What**: For a real X at least2, its square root is strictly below the natural floor.
- **How**: Use Nat.le_floor and Nat.lt_floor_add_one to compare squares via Real.sqrt_lt'.
- **Hypotheses**: Real input at least two. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.sqrt_lt_floor`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 104–106; proof/body length 2 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.sqrt_lt_nat_floor_aux.md).

#### theorem Roth.sqrt_lt_floor

Type:

```lean
∀ {X : ℝ}, 2 ≤ X → √X < ↑⌊X⌋₊ ∧ ↑⌊X⌋₊ ≤ X
```

- **What**: For real X at least two, the natural floor cast to real lies strictly above sqrt X and at most X.
- **How**: The private lower proof uses the unit floor gap and floor at least two to obtain X < floor(X)^2, then square-root order; the upper bound is Nat.floor_le.
- **Hypotheses**: X is real; 2 ≤ X; sharp by verified iff
- **Uses from project (lexical body)**: `Roth.sqrt_lt_nat_floor_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.sqrt_lt_nat_floor_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.mul_log_div_two_lt_log_mainCoeffBound`, `Roth.three_small_factors`
- **Used by other files (lexical)**: `Roth.roth_product_bound_aux`
- **Visibility**: public
- **Lines**: 115–116; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sqrt_lt_floor.md).

#### theorem Roth.four_lt_rpow

Type:

```lean
∀ {δ : ℝ}, 0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ → 3 ≤ δ ^ 2 * Real.log ↑q₁ → 4 < ↑q₁ ^ (δ * ↑r₁)
```

- **What**: Nonnegative δ, positive natural degree r and 3≤δ²logq imply q^(δr)>4.
- **How**: Derive q≥2, prove log2<3/4 from a quadratic exponential estimate, compare squares to get log4<δlogq, enlarge by r≥1, then use Real.lt_rpow_of_log_lt.
- **Hypotheses**: δ : ℝ; 0≤δ; q₁ r₁ : ℕ; 0<r₁; 3≤δ²*Real.log q₁
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_of_log_bound_aux`
- **Used by other files (lexical)**: `Roth.roth_product_bound_aux`
- **Visibility**: public
- **Lines**: 122–141; proof/body length 19 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.four_lt_rpow.md).

#### theorem Roth.mul_log_div_two_lt_log_mainCoeffBound

Type:

```lean
∀ {δ : ℝ} {q₁ r₁ : ℕ},
  2 ≤ ↑q₁ ^ (δ * ↑r₁) → δ * ↑r₁ * Real.log ↑q₁ / 2 < Real.log ↑(Roth.mainCoeffBound δ q₁ r₁)
```

- **What**: For X=q₁^(δr₁) at least two, half of δr₁ log q₁ is strictly below the logarithm of the natural coefficient floor.
- **How**: Apply log monotonicity to Roth.sqrt_lt_floor, then rewrite log of sqrt and log of a positive-base real power; hX supplies all signs.
- **Hypotheses**: δ is real; q₁,r₁ are natural numbers.; The sole explicit condition is 2 ≤ (q₁ : ℝ) ^ (δ * r₁); separate delta/degree/base positivity assumptions are unnecessary.
- **Uses from project (lexical body)**: `Roth.mainCoeffBound`, `Roth.sqrt_lt_floor`
- **Project references in type**: `Roth.mainCoeffBound`
- **Native direct body references**: `Roth.mainCoeffBound`, `Roth.sqrt_lt_floor`
- **Native direct type references**: `Roth.mainCoeffBound`
- **Used by in file (lexical)**: `Roth.three_small_factors`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 149–154; proof/body length 5 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.mul_log_div_two_lt_log_mainCoeffBound.md).

#### lemma Roth.two_lt_rpow_aux

Type:

```lean
∀ {δ : ℝ},
  0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ → Real.log 2 < δ ^ 2 * Real.log ↑q₁ → 2 < ↑q₁ ^ (δ * ↑r₁)
```

- **What**: A nonnegative delta and a positive natural degree turn log2<delta squared times logq into2<q to the delta-degree power.
- **How**: Use a squared comparison to deduce delta times log denominator exceeds log2, then apply Real.lt_rpow_of_log_lt.
- **Hypotheses**: Nonnegative delta, positive degree and squared-delta log bound greater than log2. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.three_small_factors`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 156–170; proof/body length 14 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.two_lt_rpow_aux.md).

#### theorem Roth.three_small_factors

Type:

```lean
∀ {δ : ℝ},
  0 ≤ δ →
    ∀ {m q₁ r₁ : ℕ},
      0 < r₁ →
        ∀ {A α : ℝ},
          0 ≤ A →
            2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑q₁ →
              2 ^ (m * r₁) < ↑(Roth.mainCoeffBound δ q₁ r₁) ^ δ ∧
                (1 + A) ^ (m * r₁) < ↑(Roth.mainCoeffBound δ q₁ r₁) ^ δ ∧
                  (1 + |α|) ^ (m * r₁) < ↑(Roth.mainCoeffBound δ q₁ r₁) ^ δ
```

- **What**: A non-strict logarithmic budget gives three strict small-factor bounds against the delta power of the natural coefficient floor, including zero variables.
- **How**: Use Roth.two_lt_rpow_aux and Roth.sqrt_lt_floor to secure the floor bound; multiply Roth.mul_log_div_two_lt_log_mainCoeffBound by positive delta, then apply Real.lt_rpow_of_log_lt and allocate the logarithmic budget to each factor.
- **Hypotheses**: δ≥0; m,q₁,r₁ natural; r₁>0; A≥0; α arbitrary real.; 2m+1+2m log(1+A)+2m log(1+|α|)≤δ² log q₁; strict budget is unnecessary; m=0 is permitted.
- **Uses from project (lexical body)**: `Roth.mainCoeffBound`, `Roth.mul_log_div_two_lt_log_mainCoeffBound`, `Roth.sqrt_lt_floor`, `Roth.two_lt_rpow_aux`
- **Project references in type**: `Roth.mainCoeffBound`
- **Native direct body references**: `Roth.mainCoeffBound`, `Roth.mul_log_div_two_lt_log_mainCoeffBound`, `Roth.sqrt_lt_floor`, `Roth.two_lt_rpow_aux`
- **Native direct type references**: `Roth.mainCoeffBound`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux`
- **Used by other files (lexical)**: `Roth.roth_product_bound_aux`
- **Visibility**: public
- **Lines**: 180–210; proof/body length 27 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.three_small_factors.md).

#### lemma Roth.exists_norm_coeff_reduction_aux

Type:

```lean
∀ {R : Type u_1} [inst : SeminormedRing R] {f P : Polynomial R} {A C : ℝ},
  (∀ (i : ℕ), ‖f.coeff i‖ ≤ A) →
    (∀ (i : ℕ), ‖P.coeff i‖ ≤ C) →
      ∀ {s : ℕ},
        P.natDegree ≤ s →
          f ≠ 1 →
            P %ₘ f ≠ P →
              0 < f.natDegree ∧
                f.natDegree ≤ s ∧
                  ∃ (Q : Polynomial R), Q.natDegree ≤ s - 1 ∧ (∀ (i : ℕ), ‖Q.coeff i‖ ≤ (1 + A) * C) ∧ P %ₘ f = Q %ₘ f
```

- **What**: Whenever P %ₘ f differs from P and f is not1, one leading-term elimination lowers the degree ceiling, multiplies the coefficient budget by1+A, and preserves the remainder; monicity is derived.
- **How**: Inspect Polynomial.divModByMonicAux to identify leading-term elimination, use Polynomial.div_wf_lemma for degree descent and norm_sub_le for coefficients.
- **Hypotheses**: Seminormed ring, coefficient bounds, bounded input degree, divisor not one and remainder different from input. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.norm_coeff_modByMonic_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 212–243; proof/body length 28 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_norm_coeff_reduction_aux.md).

#### theorem Roth.norm_coeff_modByMonic_le

Type:

```lean
∀ {R : Type u_1} [inst : SeminormedRing R] {f : Polynomial R} {A : ℝ},
  (∀ (i : ℕ), ‖f.coeff i‖ ≤ A) →
    ∀ (P : Polynomial R) {C : ℝ},
      (∀ (i : ℕ), ‖P.coeff i‖ ≤ C) →
        ∀ {s : ℕ}, P.natDegree ≤ s → ∀ (i : ℕ), ‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C
```

- **What**: Every coefficient of the monic-division remainder is bounded by (1+A)^(s+1-f.natDegree) C, with natural subtraction saturating at zero.
- **How**: Strong degree induction combines private exists_norm_coeff_reduction_aux with Polynomial.div_wf_lemma: one leading-term elimination lowers degree and multiplies a coefficient bound by at most 1+A.
- **Hypotheses**: An arbitrary seminormed ring, coefficient bounds A and C for f and P, and P.natDegree≤s; no monicity, nontriviality or sign premises.
- **Uses from project (lexical body)**: `Roth.exists_norm_coeff_reduction_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.exists_norm_coeff_reduction_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 252–269; proof/body length 16 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.norm_coeff_modByMonic_le.md).

#### lemma Roth.boxFamily_eq_image_finsupp_aux

Type:

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [inst : Finite ↑(Function.support r)] (B : ℕ),
  Roth.boxFamily r B =
    AddMonoidAlgebra.ofCoeff '' ↑((Finset.Iic (Finsupp.ofSupportFinite r ⋯)).finsupp fun (x : σ →₀ ℕ) ↦ Finset.Icc 0 ↑B)
```

- **What**: With finitely supported degree bounds, the integer polynomial box family is exactly the image of the finite Finsupp family with monomials in Iic(r) and coefficients in the integer interval[0,B].
- **How**: Compare coefficient-array support using Finset.mem_finsupp_iff and degreeOf_le_iff; outside the box all coefficients vanish.
- **Hypotheses**: Only finitely many variables have positive degree bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.boxFamily`
- **Native direct body references**: `Roth.boxFamily`
- **Native direct type references**: `Roth.boxFamily`
- **Used by in file (lexical)**: `Roth.boxFamily_finite`, `Roth.ncard_boxFamily`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 280–297; proof/body length 15 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.boxFamily_eq_image_finsupp_aux.md).

#### theorem Roth.boxFamily_finite

Type:

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ), (Roth.boxFamily r B).Finite
```

- **What**: Integer multivariate polynomials whose coordinate degrees have finitely supported bounds and whose coefficients lie in [0,B] form a finite set, even for an infinite ambient variable type.
- **How**: Rewrite by Roth.boxFamily_eq_image_finsupp_aux to the image of a finite coefficient-array box, then use Finset.finite_toSet and Set.Finite.image.
- **Hypotheses**: Only finitely many variable degree bounds are nonzero. No finiteness of the ambient variable type or positivity of B is required.
- **Uses from project (lexical body)**: `Roth.boxFamily_eq_image_finsupp_aux`
- **Project references in type**: `Roth.boxFamily`
- **Native direct body references**: `Roth.boxFamily`, `Roth.boxFamily_eq_image_finsupp_aux`
- **Native direct type references**: `Roth.boxFamily`
- **Used by in file (lexical)**: `Roth.exists_ne_modByMonic_eq`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 301–305; proof/body length 4 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.boxFamily_finite.md).

#### theorem Roth.ncard_boxFamily

Type:

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ),
  (Roth.boxFamily r B).ncard = (B + 1) ^ ∏ᶠ (j : σ), (r j + 1)
```

- **What**: The family of integer polynomials with finitely supported coordinate degree bounds and coefficients in [0,B] has exactly (B+1) raised to the number of admissible monomials elements.
- **How**: Transport the coefficient-choice Finset.finsupp through injective ofCoeff, use Finset.card_finsupp and Finsupp.card_Iic, then identify the finite support product with finprod.
- **Hypotheses**: Arbitrary variable type; natural bounds r and B; only Function.support r must be finite. No positivity, nonempty variable type, or Fintype sigma is needed.
- **Uses from project (lexical body)**: `Roth.boxFamily_eq_image_finsupp_aux`
- **Project references in type**: `Roth.boxFamily`
- **Native direct body references**: `Roth.boxFamily`, `Roth.boxFamily_eq_image_finsupp_aux`
- **Native direct type references**: `Roth.boxFamily`
- **Used by in file (lexical)**: `Roth.exists_ne_modByMonic_eq`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 311–318; proof/body length 7 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.ncard_boxFamily.md).

#### lemma Roth.floor_rpow_count_lt_aux

Type:

```lean
∀ {x c : ℝ}, 0 < x → 1 ≤ c → ↑(2 * ⌊x ^ c⌋₊ + 1) < (x + 1) ^ (2 * c)
```

- **What**: For x>0 and c>=1 the integer coefficient count2 floor(x^c)+1 is strictly smaller than(x+1)^(2c).
- **How**: Use Real.add_rpow_le_rpow_add, Nat.floor_le and a positive-square comparison.
- **Hypotheses**: Positive base and real exponent at least one. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.pigeonhole_count`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 320–327; proof/body length 7 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.floor_rpow_count_lt_aux.md).

#### theorem Roth.pigeonhole_count

Type:

```lean
∀ {B : ℝ},
  0 < B → ∀ {c : ℝ}, 1 ≤ c → ∀ {n D N : ℕ}, 0 < N → c * ↑n * ↑D ≤ ↑N / 2 → ↑(2 * ⌊B ^ c⌋₊ + 1) ^ (n * D) < (B + 1) ^ N
```

- **What**: A strict upper bound for the number of integer remainder-coefficient arrays: for B>0,c≥1 and c n D≤N/2 with N>0, (2 floor(B^c)+1)^(nD)<(B+1)^N.
- **How**: Uses floor_rpow_count_lt_aux to bound one coefficient count by (B+1)^(2c), then pow_lt_pow_left₀, Real.rpow_mul_natCast and exponent monotonicity; handles nD=0 using one_lt_pow₀.
- **Hypotheses**: B>0 gives positive real-power base and B+1>1.; c≥1 supplies power superadditivity in the floor-count helper.; N>0 retains strictness in the zero-dimensional case.; c n D≤N/2 is the weak exponent budget; n,D may be zero.
- **Uses from project (lexical body)**: `Roth.floor_rpow_count_lt_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.floor_rpow_count_lt_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 334–349; proof/body length 15 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.pigeonhole_count.md).

#### theorem Roth.exists_ne_modByMonic_eq

Type:

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ) {f : Polynomial ℤ},
  f.Monic →
    ∀ (J : Finset (σ →₀ ℕ)) (C : ℕ),
      (∀ W ∈ Roth.boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(Roth.diag ((hasseDeriv j) W) %ₘ f).coeff i| ≤ ↑C) →
        ↑(2 * C + 1) ^ (f.natDegree * J.card) < (↑B + 1) ^ ∏ᶠ (j : σ), (r j + 1) →
          ∃ W' ∈ Roth.boxFamily r B,
            ∃ W'' ∈ Roth.boxFamily r B,
              W' ≠ W'' ∧ ∀ j ∈ J, Roth.diag ((hasseDeriv j) W') %ₘ f = Roth.diag ((hasseDeriv j) W'') %ₘ f
```

- **What**: Two distinct integer box polynomials share every selected diagonal Hasse derivative remainder when a strict coefficient-array budget is smaller than the box family.
- **How**: Encode each polynomial by the J × Fin natDegree remainder coefficients in a finite integer interval; use Fintype.exists_ne_map_eq_of_card_lt, ncard_boxFamily, and Polynomial.sum_modByMonic_coeff to recover full remainders. Finite support is only needed by the original counting proof, not by the result: the revised proof splits support finiteness and, in the infinite case, finprod=1 allows the zero-degree constant subfamily to supply a collision.
- **Hypotheses**: Original has arbitrary σ, finitely supported natural r, natural B,C, monic integer f, finite J, low remainder-coefficient bounds and a strict real budget. Finite support of r is superfluous: full unchanged conclusion compiles after deleting only that premise.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.boxFamily`, `Roth.boxFamily_finite`, `Roth.diag`, `Roth.ncard_boxFamily`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.boxFamily`, `Roth.diag`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.boxFamily`, `Roth.boxFamily_finite`, `Roth.diag`, `Roth.ncard_boxFamily`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.boxFamily`, `Roth.diag`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 359–379; proof/body length 15 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_ne_modByMonic_eq.md).

#### theorem Roth.sub_mem_RSet

Type:

```lean
∀ {σ : Type u_1} {r : σ → ℕ} {B : ℕ} {W' W'' : MvPolynomial σ ℤ},
  W' ∈ Roth.boxFamily r B → W'' ∈ Roth.boxFamily r B → W' ≠ W'' → W' - W'' ∈ Roth.RSet (↑B) r
```

- **What**: The difference of distinct integer polynomials in the nonnegative coefficient box is nonzero, has the same coordinate degree bounds, and has absolute coefficients bounded by B.
- **How**: Combine sub_ne_zero, coordinate-degree subadditivity/max_le, and the interval diameter theorem abs_sub_le_of_nonneg_of_le after coefficient and cast transport.
- **Hypotheses**: An arbitrary variable type, arbitrary natural degree bounds and natural B, two boxFamily memberships, and distinctness; no finiteness or positivity assumptions.
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.RSet`, `Roth.boxFamily`
- **Native direct body references**: `Roth.boxFamily`
- **Native direct type references**: `Roth.RSet`, `Roth.boxFamily`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 388–394; proof/body length 5 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sub_mem_RSet.md).

#### theorem Roth.eval_hasseDeriv_sub_eq_zero

Type:

```lean
∀ {σ : Type u_1} {S : Type u_2} [inst : CommRing S] {f : Polynomial ℤ} {α : S},
  (Polynomial.aeval α) f = 0 →
    ∀ {W' W'' : MvPolynomial σ ℤ} {j : σ →₀ ℕ},
      Roth.diag ((hasseDeriv j) W') %ₘ f = Roth.diag ((hasseDeriv j) W'') %ₘ f →
        (eval fun (x : σ) ↦ α) ((hasseDeriv j) ((map (Int.castRingHom S)) (W' - W''))) = 0
```

- **What**: If selected diagonal Hasse derivatives of two integer polynomials have equal remainders modulo f, their mapped difference has that Hasse derivative vanishing at every constant point given by a root of f.
- **How**: Equal remainders make the diagonal derivative difference divisible by f using dvd_modByMonic_iff_dvd and sub_modByMonic. Evaluation kills this multiple by aeval_eq_zero_of_dvd_aeval_eq_zero; Hasse coefficient transport and evaluation composition identify the multivariate value.
- **Hypotheses**: Arbitrary variable type and commutative target ring S, arbitrary f over integers and root alpha, two arbitrary polynomials and a finite multiindex with equal diagonal remainders. No monicity, finite variable, characteristic, nontriviality or degree assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.diag`, `Roth.diag_sub`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.diag`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.diag`, `Roth.diag_sub`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.diag`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 402–411; proof/body length 7 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.eval_hasseDeriv_sub_eq_zero.md).

#### theorem Roth.le_index_of_forall_eval_eq_zero

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 →
    ∀ {r : σ → ℕ},
      (∀ (j : σ), degreeOf j P ≤ r j) →
        ∀ (α : σ → ℝ) {c : ℝ},
          (∀ (d : σ →₀ ℕ), (∀ (j : σ), d j ≤ r j) → Roth.weight r d < c → (eval α) ((hasseDeriv d) P) = 0) →
            c ≤ Roth.index P α r
```

- **What**: For a nonzero real multivariate polynomial within coordinate degree bounds, vanishing of the in-box Hasse derivatives strictly below a real weight cutoff forces the index to be at least that cutoff.
- **How**: A nonzero evaluated Hasse derivative cannot exceed a coordinate degree. Apply the project le_index_iff characterization and contrapose the strict cutoff condition; excessive orders vanish by hasseDeriv_eq_zero_of_degreeOf_lt.
- **Hypotheses**: P is nonzero; index of zero is defined as 0.; Every coordinate degree is bounded by r.; Only derivative orders in the box and of weight strictly less than c must vanish.; The existing index/weight interface requires Fintype σ; α and c are arbitrary and r may contain zeros.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `Roth.le_index_iff`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `Roth.index`, `Roth.le_index_iff`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 419–425; proof/body length 4 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.le_index_of_forall_eval_eq_zero.md).

#### theorem Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul

Type:

```lean
∀ {K : Type u_1} [inst : Semifield K] [inst_1 : LinearOrder K] [IsStrictOrderedRing K]
  [ExistsAddOfLE K] {δ m L : K}, 0 < 2 * m + 1 → δ * m < 1 → 2 * m + 1 ≤ δ ^ 2 * L → m * (2 * m + 1) / δ < L
```

- **What**: Transfers the quadratic budget 2m+1≤δ²L and δm<1 into m(2m+1)/δ<L in an ordered semifield.
- **How**: Derive δ≠0, multiply by its positive square, normalize the rational expression, apply mul_lt_of_lt_one_left, then the budget.
- **Hypotheses**: Semifield, LinearOrder, IsStrictOrderedRing, ExistsAddOfLE; 0<2m+1; δm<1; 2m+1≤δ²L. No δ>0 or m≥0 assumed.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 433–443; proof/body length 9 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul.md).

#### theorem Roth.exists_hasseDeriv_eval_ne_zero

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 →
    ∀ (α : σ → ℝ) (r : σ → ℕ) {c : ℝ},
      Roth.index P α r < c → ∃ (k : σ →₀ ℕ), Roth.weight r k < c ∧ (eval α) ((hasseDeriv k) P) ≠ 0
```

- **What**: A nonzero polynomial with index below c has a nonvanishing Hasse derivative of weight below c.
- **How**: Take a derivative attaining the minimum and transfer the strict inequality along its weight equality.
- **Hypotheses**: Fintype σ for existing weight/index signatures; P ≠ 0 essential because index0=0; α arbitrary; r : σ → ℕ includes zero entries; strict index P α r < c
- **Uses from project (lexical body)**: `Roth.exists_weight_eq_index`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.exists_weight_eq_index`, `Roth.index`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.exists_hasseDeriv_index_eval_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 454–457; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_eval_ne_zero.md).

#### lemma Roth.abs_eval_iterated_hasseDeriv_lt_aux

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {B α β : ℝ}
  {s : ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) →
    0 < B →
      ∑ j : σ, r j ≤ s →
        2 ^ s < β →
          (1 + |α|) ^ s ≤ β →
            (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
              ∀ (i k : σ →₀ ℕ),
                |(eval fun (x : σ) ↦ α) ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) P)))| <
                  β * (β * B) * β
```

- **What**: Bounds every evaluated iterated Hasse derivative of an integer polynomial by beta cubed times the original coefficient bound, from coordinate degrees and a common exponential bound.
- **How**: Combine abs_coeff_hasseDeriv_le twice with abs_eval_le, rewrite products using Finset.prod_pow_eq_pow_sum and bound total degrees by the chosen size.
- **Hypotheses**: Finite variables, bounded degrees/coefficient size, positive coefficient bound and bounds for powers of two and one plus the point absolute value. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.abs_eval_le`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.abs_eval_le`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `Roth.exists_auxiliary_polynomial_of_log_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 459–475; proof/body length 13 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_iterated_hasseDeriv_lt_aux.md).

#### lemma Roth.exists_hasseDeriv_index_eval_bound_aux

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {α z : σ → ℝ}
  {C γ c : ℝ},
  P ≠ 0 →
    (∀ (j : σ), degreeOf j P ≤ r j) →
      (∀ (i k : σ →₀ ℕ), |(eval α) ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) P)))| < C) →
        γ ≤ Roth.index ((map (Int.castRingHom ℝ)) P) α r →
          Roth.index ((map (Int.castRingHom ℝ)) P) z r < c →
            ∃ (Q : MvPolynomial σ ℤ),
              Q ≠ 0 ∧
                (∀ (j : σ), degreeOf j Q ≤ r j) ∧
                  γ - c < Roth.index ((map (Int.castRingHom ℝ)) Q) α r ∧
                    (eval z) ((map (Int.castRingHom ℝ)) Q) ≠ 0 ∧
                      ∀ (i : σ →₀ ℕ), |(eval α) ((hasseDeriv i) ((map (Int.castRingHom ℝ)) Q))| < C
```

- **What**: Selects one nonzero integer Hasse derivative that is nonvanishing at a second point, loses less than a specified cutoff in its index at the first point, and retains all derivative evaluation bounds.
- **How**: Choose k with exists_hasseDeriv_eval_ne_zero, set Q to its derivative and apply index_sub_weight_le_index_hasseDeriv with hasseDeriv_map.
- **Hypotheses**: Nonzero integral polynomial with degree bounds, high first index, low second index and uniform iterated derivative bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.exists_hasseDeriv_eval_ne_zero`, `Roth.index_sub_weight_le_index_hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`
- **Native direct body references**: `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.exists_hasseDeriv_eval_ne_zero`, `Roth.index`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`
- **Used by in file (lexical)**: `Roth.main_lemma`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 477–495; proof/body length 11 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_index_eval_bound_aux.md).

#### lemma Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {f : Polynomial ℤ} {P : MvPolynomial σ ℤ}
  {r : σ → ℕ} {A B : ℝ},
  (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
    (∀ (k : σ), degreeOf k P ≤ r k) →
      (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
        ∀ (j : σ →₀ ℕ) (i : ℕ),
          |↑((Roth.diag ((hasseDeriv j) P) %ₘ f).coeff i)| ≤
            (1 + A) ^ (∑ k : σ, r k + 1 - f.natDegree) * (↑(∏ k : σ, (r k + 1)) * ((2 ^ ∑ k : σ, r k) * B))
```

- **What**: Bounds a coefficient of a diagonalized Hasse derivative modulo an integer polynomial using the divisor coefficient bound, degree sum, box size, and the original coefficient bound.
- **How**: Combine card_le_card_box, abs_coeff_diag_le and abs_coeff_hasseDeriv_le, then apply norm_coeff_modByMonic_le and natDegree_diag_le.
- **Hypotheses**: Finite variables, degree bounds and coefficient bounds for the input and divisor. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_diag_le`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.card_le_card_box`, `Roth.diag`, `Roth.natDegree_diag_le`, `Roth.norm_coeff_modByMonic_le`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.diag`
- **Native direct body references**: `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_diag_le`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.card_le_card_box`, `Roth.diag`, `Roth.natDegree_diag_le`, `Roth.norm_coeff_modByMonic_le`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.diag`
- **Used by in file (lexical)**: `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 497–513; proof/body length 13 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux.md).

#### lemma Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {f : Polynomial ℤ} {P : MvPolynomial σ ℤ}
  {r : σ → ℕ} {A B β : ℝ} {s : ℕ},
  (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
    (∀ (k : σ), degreeOf k P ≤ r k) →
      (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
        ∑ k : σ, r k ≤ s →
          2 ^ s ≤ β →
            (1 + A) ^ s ≤ β → ∀ (j : σ →₀ ℕ) (i : ℕ), |(Roth.diag ((hasseDeriv j) P) %ₘ f).coeff i| ≤ ↑⌊B * β ^ 3⌋₊
```

- **What**: Bounds integer remainder coefficients of diagonal Hasse derivatives by the natural floor of B times beta cubed under common exponential bounds.
- **How**: Use abs_coeff_diag_hasseDeriv_modByMonic_le_aux, bound box cardinality by a power of two, handle zero-degree/nonmonic divisors and convert with Int.le_floor.
- **Hypotheses**: Finite variables; total degree bound, divisor/input coefficient bounds and common growth-factor bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, `Roth.diag`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.diag`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, `Roth.diag`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.diag`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 515–548; proof/body length 30 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux.md).

#### lemma Roth.exists_mem_RSet_le_index_aux

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {f : Polynomial ℤ} {α : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      ∀ (r : σ → ℕ) (B C : ℕ) (J : Finset (σ →₀ ℕ)) {γ : ℝ},
        (∀ W ∈ Roth.boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(Roth.diag ((hasseDeriv j) W) %ₘ f).coeff i| ≤ ↑C) →
          ↑(2 * C + 1) ^ (f.natDegree * J.card) < (↑B + 1) ^ ∏ k : σ, (r k + 1) →
            (∀ (d : σ →₀ ℕ), (∀ (k : σ), d k ≤ r k) → Roth.weight r d < γ → d ∈ J) →
              ∃ P ∈ Roth.RSet (↑B) r, γ ≤ Roth.index ((map (Int.castRingHom ℝ)) P) (fun (x : σ) ↦ α) r
```

- **What**: Uses a strict finite remainder count to construct a nonzero integer box polynomial whose index at the diagonal root is at least an arbitrary real cutoff.
- **How**: Use exists_ne_modByMonic_eq, subtract via sub_mem_RSet, then apply le_index_of_forall_eval_eq_zero using eval_hasseDeriv_sub_eq_zero.
- **Hypotheses**: Monic integer equation for the point, remainder coefficient/count bounds, and derivative set covering all low-weight box indices. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.eval_hasseDeriv_sub_eq_zero`, `Roth.exists_ne_modByMonic_eq`, `Roth.le_index_of_forall_eval_eq_zero`, `Roth.sub_mem_RSet`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.boxFamily`, `Roth.diag`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.boxFamily`, `Roth.diag`, `Roth.eval_hasseDeriv_sub_eq_zero`, `Roth.exists_ne_modByMonic_eq`, `Roth.index`, `Roth.le_index_of_forall_eval_eq_zero`, `Roth.sub_mem_RSet`, `Roth.weight`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.boxFamily`, `Roth.diag`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 550–567; proof/body length 12 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_mem_RSet_le_index_aux.md).

#### lemma Roth.mul_card_filter_weight_le_aux

Type:

```lean
∀ {m : ℕ},
  0 < m →
    ∀ (r : Fin m → ℕ),
      (∀ (j : Fin m), 0 < r j) →
        ∀ (a : ℝ), a * ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - 4 * a * √↑m) / 2}.card ≤ ↑(∏ j : Fin m, (r j + 1)) / 2
```

- **What**: For arbitrary real scale a, bounds a times the number of lattice indices below the corresponding centered cutoff by half the coordinate box cardinality.
- **How**: For positive scale apply card_filter_weight_le and cancel the square-root factors; for nonpositive scale compare signs directly.
- **Hypotheses**: Positive dimension and positive degree vector; arbitrary real scale. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.card_filter_weight_le`
- **Project references in type**: `Roth.box`, `Roth.weight`
- **Native direct body references**: `Roth.box`, `Roth.card_filter_weight_le`, `Roth.weight`
- **Native direct type references**: `Roth.box`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 569–579; proof/body length 9 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.mul_card_filter_weight_le_aux.md).

#### lemma Roth.exists_mem_RSet_le_index_of_rpow_bound_aux

Type:

```lean
∀ {f : Polynomial ℤ} {α A : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
        ∀ {m : ℕ},
          0 < m →
            ∀ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) →
                ∀ {c β : ℝ} {B s : ℕ},
                  0 < B →
                    ∑ j : Fin m, r j ≤ s →
                      (1 + A) ^ s ≤ β →
                        ↑B * β ^ 3 ≤ ↑B ^ c →
                          ∃ P ∈ Roth.RSet (↑B) r,
                            (↑m - 4 * c * ↑f.natDegree * √↑m) / 2 ≤
                              Roth.index ((map (Int.castRingHom ℝ)) P) (fun (x : Fin m) ↦ α) r
```

- **What**: Constructs a bounded nonzero integer polynomial of high diagonal-root index from a power-based coefficient budget and positive coordinate degree bounds.
- **How**: Derive exponent positivity, obtain floor bounds with abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux, bound the derivative count using mul_card_filter_weight_le_aux and pigeonhole_count, then apply exists_mem_RSet_le_index_aux.
- **Hypotheses**: Monic equation, positive dimension/degrees/coefficient bound and compatible coefficient-growth estimates. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`, `Roth.box`, `Roth.boxFamily`, `Roth.diag`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.mem_box`, `Roth.mul_card_filter_weight_le_aux`, `Roth.pigeonhole_count`, `Roth.weight`
- **Project references in type**: `Roth.RSet`, `Roth.index`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`, `Roth.box`, `Roth.boxFamily`, `Roth.diag`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.mem_box`, `Roth.mul_card_filter_weight_le_aux`, `Roth.pigeonhole_count`, `Roth.weight`
- **Native direct type references**: `Roth.RSet`, `Roth.index`
- **Used by in file (lexical)**: `Roth.exists_mem_RSet_le_index_of_log_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 581–616; proof/body length 31 lines.
- **Notes**: proof/body >30 lines
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_mem_RSet_le_index_of_rpow_bound_aux.md).

#### lemma Roth.exists_mem_RSet_le_index_of_log_bound_aux

Type:

```lean
∀ {f : Polynomial ℤ} {α A : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
        ∀ {m q₁ r₁ : ℕ},
          0 < m →
            ∀ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) →
                ∑ j : Fin m, r j ≤ m * r₁ →
                  ∀ {δ : ℝ},
                    0 ≤ δ →
                      2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) ≤ δ ^ 2 * Real.log ↑q₁ →
                        ∃ P ∈ Roth.RSet (↑(Roth.mainCoeffBound δ q₁ r₁)) r,
                          Roth.gam δ f.natDegree m ≤ Roth.index ((map (Int.castRingHom ℝ)) P) (fun (x : Fin m) ↦ α) r
```

- **What**: Specializes the power-budget construction to the logarithmic Roth parameters and obtains index at least gamma with the natural-floor coefficient bound.
- **How**: Use three_small_factors and four_lt_rpow to establish the coefficient growth needed by exists_mem_RSet_le_index_of_rpow_bound_aux; unfold gam and lam.
- **Hypotheses**: Monic integer equation, bounded coefficients, positive dimension/degrees, total degree bound and nonnegative delta with logarithmic bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `Roth.four_lt_rpow`, `Roth.gam`, `Roth.lam`, `Roth.mainCoeffBound`, `Roth.three_small_factors`
- **Project references in type**: `Roth.RSet`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`
- **Native direct body references**: `Roth.RSet`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `Roth.four_lt_rpow`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`, `Roth.three_small_factors`
- **Native direct type references**: `Roth.RSet`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`
- **Used by in file (lexical)**: `Roth.exists_auxiliary_polynomial_of_log_bound_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 618–641; proof/body length 19 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_mem_RSet_le_index_of_log_bound_aux.md).

#### lemma Roth.exists_auxiliary_polynomial_of_log_bound_aux

Type:

```lean
∀ {f : Polynomial ℤ} {α A : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
        ∀ {m q₁ r₁ : ℕ},
          0 < m →
            ∀ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) →
                ∑ j : Fin m, r j ≤ m * r₁ →
                  ∀ {δ : ℝ},
                    0 ≤ δ →
                      2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑q₁ →
                        ∃ P ∈ Roth.RSet (↑q₁ ^ (δ * ↑r₁)) r,
                          Roth.gam δ f.natDegree m ≤ Roth.index ((map (Int.castRingHom ℝ)) P) (fun (x : Fin m) ↦ α) r ∧
                            ∀ (i k : Fin m →₀ ℕ),
                              |(eval fun (x : Fin m) ↦ α)
                                    ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) P)))| <
                                ↑(Roth.mainCoeffBound δ q₁ r₁) ^ (1 + 3 * δ)
```

- **What**: Produces an auxiliary polynomial with high diagonal-root index, a real-power coefficient bound, and uniform evaluated double-Hasse-derivative height bounds.
- **How**: Obtain the polynomial from exists_mem_RSet_le_index_of_log_bound_aux, use three_small_factors and abs_eval_iterated_hasseDeriv_lt_aux, and increase the floor coefficient bound to its real power.
- **Hypotheses**: Monic integer equation, bounded coefficients, positive degree vector, total degree bound and combined logarithmic condition. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.abs_eval_iterated_hasseDeriv_lt_aux`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.mainCoeffBound`, `Roth.three_small_factors`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.abs_eval_iterated_hasseDeriv_lt_aux`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`, `Roth.three_small_factors`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`
- **Used by in file (lexical)**: `Roth.exists_auxiliary_polynomial_with_index_gap_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 643–669; proof/body length 20 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_auxiliary_polynomial_of_log_bound_aux.md).

#### lemma Roth.theta_lt_eta_of_sq_log_bound_aux

Type:

```lean
∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
  0 ≤ δ →
    δ * ↑m ≤ 1 →
      ∀ {r q : Fin m → ℕ},
        3 ≤ r (Fin.rev 0) →
          (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ ≤ ↑(r i)) →
            2 * ↑m + 1 ≤ δ ^ 2 * Real.log ↑(q 0) →
              (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < Roth.eta δ m
```

- **What**: Converts the square-logarithm and adjacent-degree hypotheses into the strict bound Theta<eta for the chosen real coefficient power.
- **How**: Rewrite the positive dimension as a successor, derive delta positivity and the Lemma7 logarithm bound, and specialize Θ_lt.
- **Hypotheses**: Nonzero dimension, nonnegative delta with delta times dimension at most one, last degree at least three and ratio/balancing/logarithmic hypotheses. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.eta`, `Roth.Θ_lt`
- **Project references in type**: `Roth.eta`, `Roth.Θ`
- **Native direct body references**: `Roth.eta`, `Roth.Θ`, `Roth.Θ_lt`
- **Native direct type references**: `Roth.eta`, `Roth.Θ`
- **Used by in file (lexical)**: `Roth.exists_auxiliary_polynomial_with_index_gap_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 671–690; proof/body length 15 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_eta_of_sq_log_bound_aux.md).

#### lemma Roth.exists_auxiliary_polynomial_with_index_gap_aux

Type:

```lean
∀ {α : ℝ} {f : Polynomial ℤ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      ∀ {A : ℝ},
        (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
          ∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
            0 ≤ δ →
              δ ≤ 1 / ↑m →
                ∀ {r : Fin m → ℕ},
                  3 ≤ r (Fin.rev 0) →
                    (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ ≤ ↑(r i)) →
                      ∀ {q : Fin m → ℕ},
                        2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑(q 0) →
                          (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                            ∃ W ∈ Roth.RSet (↑(q 0) ^ (δ * ↑(r 0))) r,
                              Roth.gam δ f.natDegree m - Roth.eta δ m + Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r <
                                  Roth.index ((map (Int.castRingHom ℝ)) W) (fun (x : Fin m) ↦ α) r ∧
                                ∀ (i k : Fin m →₀ ℕ),
                                  |(eval fun (x : Fin m) ↦ α)
                                        ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) W)))| <
                                    ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ^ (1 + 3 * δ)
```

- **What**: Combines the high-index auxiliary polynomial with Theta<eta to obtain the strict index gap needed to select the final nonvanishing derivative.
- **How**: Derive antitone positive degrees and their total bound, use exists_auxiliary_polynomial_of_log_bound_aux, then compare Θ with eta via theta_lt_eta_of_sq_log_bound_aux.
- **Hypotheses**: Monic integer equation, nonzero dimension, bounded coefficients, nonnegative small delta and the displayed degree/logarithmic inequalities. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.exists_auxiliary_polynomial_of_log_bound_aux`, `Roth.theta_lt_eta_of_sq_log_bound_aux`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.eta`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`, `Roth.Θ`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.eta`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`, `Roth.theta_lt_eta_of_sq_log_bound_aux`, `Roth.Θ`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.eta`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`, `Roth.Θ`
- **Used by in file (lexical)**: `Roth.main_lemma`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 692–725; proof/body length 24 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_auxiliary_polynomial_with_index_gap_aux.md).

#### theorem Roth.main_lemma

Type:

```lean
∀ {α : ℝ} {f : Polynomial ℤ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      ∀ {A : ℝ},
        (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
          ∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
            0 ≤ δ →
              δ ≤ 1 / ↑m →
                ∀ {r : Fin m → ℕ},
                  3 ≤ r (Fin.rev 0) →
                    (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ ≤ ↑(r i)) →
                      ∀ {q : Fin m → ℕ},
                        2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑(q 0) →
                          (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                            ∀ {h : Fin m → ℤ},
                              (∀ (j : Fin m), IsCoprime (h j) ↑(q j)) →
                                ∃ (Q : MvPolynomial (Fin m) ℤ),
                                  Q ≠ 0 ∧
                                    (∀ (j : Fin m), degreeOf j Q ≤ r j) ∧
                                      Roth.gam δ f.natDegree m - Roth.eta δ m <
                                          Roth.index ((map (Int.castRingHom ℝ)) Q) (fun (x : Fin m) ↦ α) r ∧
                                        (eval fun (j : Fin m) ↦ ↑(h j) / ↑(q j)) ((map (Int.castRingHom ℝ)) Q) ≠ 0 ∧
                                          ∀ (i : Fin m →₀ ℕ),
                                            |(eval fun (x : Fin m) ↦ α)
                                                  ((hasseDeriv i) ((map (Int.castRingHom ℝ)) Q))| <
                                              ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ^ (1 + 3 * δ)
```

- **What**: Roth Lemma9: constructs a nonzero integer box polynomial with strict index above gamma-eta at the diagonal algebraic point, nonzero value at a coprime rational tuple, and a uniform bound on all diagonal Hasse derivatives. The current weak hypotheses do not claim gamma-eta>0.
- **How**: Pigeonhole bounded remainder observations yields a sharp-B nonzero difference with high algebraic index; the project uniform Theta bound gives low rational index; a Hasse derivative below an intermediate cutoff preserves degree, nonzero rational value, the strict algebraic index gap and all derivative bounds.
- **Hypotheses**: Real root of any monic integer polynomial; coefficient bound A; Nonzero dimension m;0<=delta<=1/m;last degree>=3;consecutive ratio bound; Weak square-log threshold and balanced denominator-degree logarithms; Integer numerator/natural denominator tuple with coordinatewise coprimality
- **Uses from project (lexical body)**: `Roth.eta`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.exists_hasseDeriv_index_eval_bound_aux`, `Roth.gam`, `Roth.index`, `Roth.index_le_Θ`, `Roth.Θ`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.eta`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.eta`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.exists_hasseDeriv_index_eval_bound_aux`, `Roth.gam`, `Roth.index`, `Roth.index_le_Θ`, `Roth.mainCoeffBound`, `Roth.Θ`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.eta`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.one_lt_roth_eval_bound_aux`
- **Visibility**: public
- **Lines**: 735–760; proof/body length 15 lines.
- **Notes**:
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/Roth.main_lemma.md).

#### File structural summary

- Written declarations: 38; kinds: {'def': 5, 'theorem': 17, 'lemma': 16}
- **Key API (at least three lexical callers)**: `Roth.lam`, `Roth.gam`, `Roth.eta`, `Roth.mainCoeffBound`, `Roth.sqrt_lt_floor`, `Roth.three_small_factors`, `Roth.boxFamily`
- **Unused in file (observation)**: `Roth.exists_delta_bound`, `Roth.eta_lt_gam_iff`, `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`, `Roth.main_lemma`
- **Proofs over 30 lines**: `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Separation.lean

Completed assessments: 27/27.

#### def Roth.coeffNone

Type:

```lean
Roth.coeffNone.{u_1, u_2} : {τ : Type u_1} → {R : Type u_2} → [CommSemiring R] → MvPolynomial (Option τ) R → ℕ → MvPolynomial τ R
```

- **What**: Extract the coefficient polynomial of a distinguished variable power.
- **How**: Apply MvPolynomial.optionEquivLeft, then Polynomial.coeff.
- **Hypotheses**: τ: Arbitrary type, no Fintype/DecidableEq; R: CommSemiring, no field/domain/nontriviality; P: Arbitrary polynomial; ν: Arbitrary natural exponent
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.coeff_coeffNone`, `Roth.eq_sum_X_none_pow_mul_coeffNone`, `Roth.degreeOf_coeffNone_le`, `Roth.coeff_rename_mul_aeval`, `Roth.eq_sum_aeval_basis_coeffNone_aux`, `Roth.exists_coeffNone_basis_aux`, `Roth.exists_separated_representation`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 80–81; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeffNone.md).

#### theorem Roth.eq_mapDomain_some_add_single

Type:

```lean
@Roth.eq_mapDomain_some_add_single : ∀ {τ : Type u_1} (d : Option τ →₀ ℕ),
  d = Finsupp.mapDomain some d.some + Finsupp.single none (d none)
```

- **What**: Rebuild an Option-indexed natural multi-index from restriction and distinguished coordinate.
- **How**: Pointwise extensionality, two Option cases, mapDomain evaluation.
- **Hypotheses**: τ : Type u_1; d : Option τ →₀ ℕ; no Fintype, DecidableEq, or coefficient-ring instance
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.eq_sum_X_none_pow_mul_coeffNone`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 57–61; proof/body length 4 lines.
- **Notes**:
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.eq_mapDomain_some_add_single.md).

#### lemma Roth.coeff_X_none_pow_mul_rename

Type:

```lean
∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (ν : ℕ) (Q : MvPolynomial τ R) (e : Option τ →₀ ℕ),
  (MvPolynomial.X none ^ ν * (MvPolynomial.rename some) Q).coeff e = if e none = ν then Q.coeff e.some else 0
```

- **What**: The coefficient of X none ^ ν times rename some Q at e is Q.coeff e.some when e none = ν, and zero otherwise.
- **How**: Transport by optionEquivLeft and use Polynomial.coeff_monomial after identifying the renamed polynomial with a constant polynomial.
- **Hypotheses**: Commutative semiring coefficients and arbitrary variables. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.eq_sum_X_none_pow_mul_coeffNone`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 64–76; proof/body length 12 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_X_none_pow_mul_rename.md).

#### theorem Roth.coeff_coeffNone

Type:

```lean
@Roth.coeff_coeffNone : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ)
  (d : τ →₀ ℕ), (Roth.coeffNone P ν).coeff d = P.coeff (Finsupp.mapDomain some d + Finsupp.single none ν)
```

- **What**: Extracting exponent d from the coefficient polynomial at distinguished exponent ν recovers the original coefficient at those combined exponents.
- **How**: Unfold coeffNone, rewrite optionEquivLeft_coeff_coeff, normalize the Option multi-index pointwise.
- **Hypotheses**: τ : Type u_1, R : Type u_2; CommSemiring R; P : MvPolynomial (Option τ) R; ν : ℕ; d : τ →₀ ℕ; No Fintype τ or DecidableEq τ
- **Uses from project (lexical body)**: `Roth.coeffNone`
- **Project references in type**: `Roth.coeffNone`
- **Native direct body references**: `Roth.coeffNone`
- **Native direct type references**: `Roth.coeffNone`
- **Used by in file (lexical)**: `Roth.eq_sum_X_none_pow_mul_coeffNone`, `Roth.coeff_rename_mul_aeval`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 85–91; proof/body length 6 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_coeffNone.md).

#### theorem Roth.eq_sum_X_none_pow_mul_coeffNone

Type:

```lean
@Roth.eq_sum_X_none_pow_mul_coeffNone : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (P : MvPolynomial (Option τ) R) {n : ℕ},
  MvPolynomial.degreeOf none P ≤ n →
    P = ∑ ν ∈ Finset.range (n + 1), MvPolynomial.X none ^ ν * (MvPolynomial.rename some) (Roth.coeffNone P ν)
```

- **What**: Expand an Option-variable polynomial with distinguished-variable degree at most n into powers0 through n with polynomial coefficients in the remaining variables.
- **How**: Source proof compares monomial coefficients, separates the matching distinguished exponent, and uses hn to kill out-of-range coefficients. Canonical refactor transports existing polynomial finite expansion through optionEquivLeft.
- **Hypotheses**: τ : Type u_1, R : Type u_2; CommSemiring R; P : MvPolynomial (Option τ) R; n : ℕ; degreeOf none P ≤ n; No Fintype τ or DecidableEq τ
- **Uses from project (lexical body)**: `Roth.coeff_X_none_pow_mul_rename`, `Roth.coeff_coeffNone`, `Roth.eq_mapDomain_some_add_single`
- **Project references in type**: `Roth.coeffNone`
- **Native direct body references**: `Roth.coeffNone`, `Roth.coeff_X_none_pow_mul_rename`, `Roth.coeff_coeffNone`, `Roth.eq_mapDomain_some_add_single`
- **Native direct type references**: `Roth.coeffNone`
- **Used by in file (lexical)**: `Roth.exists_separated_representation`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 98–109; proof/body length 10 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_X_none_pow_mul_coeffNone.md).

#### theorem Roth.degreeOf_coeffNone_le

Type:

```lean
@Roth.degreeOf_coeffNone_le : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (P : MvPolynomial (Option τ) R)
  (ν : ℕ) (j : τ), MvPolynomial.degreeOf j (Roth.coeffNone P ν) ≤ MvPolynomial.degreeOf (some j) P
```

- **What**: Coefficient extraction in one distinguished variable cannot increase the degree in any remaining variable.
- **How**: Rewrite the coordinate degree bound as support-wise bounds; insert the distinguished exponent using optionEquivLeft support membership; bound that monomial exponent and normalize its some-coordinate.
- **Hypotheses**: τ : Type u_1; R : Type u_2; CommSemiring R; P : MvPolynomial (Option τ) R; ν : ℕ; j : τ; No Fintype, DecidableEq, nonzero, domain, characteristic or exponent bound assumptions
- **Uses from project (lexical body)**: []
- **Project references in type**: `Roth.coeffNone`
- **Native direct body references**: `Roth.coeffNone`
- **Native direct type references**: `Roth.coeffNone`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 114–117; proof/body length 3 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_coeffNone_le.md).

#### theorem Roth.coeff_rename_mul_aeval

Type:

```lean
@Roth.coeff_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (U : MvPolynomial τ R)
  (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ),
  ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V).coeff
      (Finsupp.mapDomain some a + Finsupp.single none b) =
    U.coeff a * V.coeff b
```

- **What**: A coefficient of a product of polynomials in separate variable blocks is the product of the two corresponding coefficients.
- **How**: Transport through optionEquivLeft to a univariate polynomial over MvPolynomial τ R; normalize rename to C and aeval to map, then extract the two coefficients.
- **Hypotheses**: τ arbitrary Type u_1; R arbitrary Type u_2 with CommSemiring R; U : MvPolynomial τ R; V : Polynomial R; a : τ →₀ ℕ; b : ℕ; No Fintype/DecidableEq/domain/nonzero/characteristic assumptions
- **Uses from project (lexical body)**: `Roth.coeffNone`, `Roth.coeff_coeffNone`
- **Project references in type**: []
- **Native direct body references**: `Roth.coeffNone`, `Roth.coeff_coeffNone`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_int_polynomial_of_primitive_factor_aux`
- **Used by other files (lexical)**: `Roth.index_det_le`
- **Visibility**: public
- **Lines**: 123–132; proof/body length 8 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_rename_mul_aeval.md).

#### theorem Roth.aeval_X_eq_rename

Type:

```lean
Roth.aeval_X_eq_rename : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} (i : σ) (f : Polynomial R),
  (Polynomial.aeval (MvPolynomial.X i)) f =
    (MvPolynomial.rename fun x ↦ i) ((MvPolynomial.uniqueAlgEquiv R Unit).symm f)
```

- **What**: Embedding a univariate polynomial at a selected multivariate coordinate equals renaming its Unit-variable presentation.
- **How**: Applies AlgHom.congr_fun to existing Polynomial.toMvPolynomial_eq_rename_comp; no project proof dependencies.
- **Hypotheses**: R : Type u_1; CommSemiring R; sigma : Type u_2; i : sigma; f : Polynomial R; no finiteness/DecidableEq/domain assumptions
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.hasseDeriv_rename_mul_aeval`, `Roth.degreeOf_rename_mul_aeval`, `Roth.degreeOf_none_rename_mul_aeval`
- **Used by other files (lexical)**: `Roth.index_separated_mul_le_aux`, `Roth.mapped_det_ne_zero_aux`
- **Visibility**: public
- **Lines**: 137–140; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.aeval_X_eq_rename.md).

#### theorem Roth.hasseDeriv_rename_mul_aeval

Type:

```lean
@Roth.hasseDeriv_rename_mul_aeval.{u_1,
    u_2} : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring.{u_2} R] (d : Finsupp.{u_1, 0} τ ℕ) (ν : ℕ)
  (U : MvPolynomial.{u_1, u_2} τ R) (V : Polynomial.{u_2} R),
  Eq.{max (u_1 + 1) (u_2 + 1)}
    ((MvPolynomial.hasseDeriv.{u_1, u_2}
        (HAdd.hAdd.{u_1, u_1, u_1} (Finsupp.mapDomain.{u_1, u_1, 0} some.{u_1} d)
          (Finsupp.single.{u_1, 0} none.{u_1} ν)))
      (HMul.hMul.{max u_1 u_2, max u_1 u_2, max u_1 u_2} ((MvPolynomial.rename.{u_1, u_1, u_2} some.{u_1}) U)
        ((Polynomial.aeval.{u_2, max u_1 u_2} (MvPolynomial.X.{u_2, u_1} none.{u_1})) V)))
    (HMul.hMul.{max u_1 u_2, max u_1 u_2, max u_1 u_2}
      ((MvPolynomial.rename.{u_1, u_1, u_2} some.{u_1}) ((MvPolynomial.hasseDeriv.{u_1, u_2} d) U))
      ((Polynomial.aeval.{u_2, max u_1 u_2} (MvPolynomial.X.{u_2, u_1} none.{u_1}))
        ((Polynomial.hasseDeriv.{u_2} ν) V)))
```

- **What**: Hasse differentiation of a product in disjoint variable blocks acts on each factor separately.
- **How**: Split the derivative multi-index into disjoint supports via hasseDeriv_hasseDeriv_of_disjoint; hasseDeriv_mul_of_degreeOf_eq_zero pulls out inactive factors, and hasseDeriv_single_aeval_X plus hasseDeriv_rename transport the two derivatives.
- **Hypotheses**: arbitrary independent variable/coefficient universes; CommSemiring R; d : τ →₀ ℕ; ν : ℕ; U : MvPolynomial τ R; V : Polynomial R; no Fintype, DecidableEq, characteristic, field, domain or nonzero assumptions
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_single_aeval_X`, `Roth.aeval_X_eq_rename`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_single_aeval_X`, `Roth.aeval_X_eq_rename`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `Roth.det_hasseDeriv_separated`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 146–165; proof/body length 17 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_rename_mul_aeval.md).

#### theorem Roth.coeff_uniqueAlgEquiv_symm

Type:

```lean
Roth.coeff_uniqueAlgEquiv_symm : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} [inst_1 : Unique σ]
  (f : Polynomial R) (n : ℕ), ((MvPolynomial.uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n
```

- **What**: The coefficient at singleton exponent n in the inverse singleton-variable polynomial equivalence is the ordinary nth coefficient.
- **How**: Specialize the existing arbitrary-exponent mathlib coefficient law and evaluate the finitely supported singleton at its own index.
- **Hypotheses**: R and σ independently universe-polymorphic; CommSemiring R and Unique σ; arbitrary f and natural n. No Fintype, DecidableEq, domain or nonzero premise.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 169–171; proof/body length 2 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_uniqueAlgEquiv_symm.md).

#### theorem Roth.degreeOf_uniqueAlgEquiv_symm

Type:

```lean
@Roth.degreeOf_uniqueAlgEquiv_symm : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} [inst_1 : Unique σ]
  (f : Polynomial R), MvPolynomial.degreeOf default ((MvPolynomial.uniqueAlgEquiv R σ).symm f) = f.natDegree
```

- **What**: Identifies the degree in the unique variable of the inverse uniqueAlgEquiv image with the original polynomial natDegree, including zero.
- **How**: Two coefficient-support inequalities using mathlib coeff_uniqueAlgEquiv_symm directly; independent structural proof uses a newly proved optionSubtypeNe/optionEquivLeft normalization and existing degreeOf_eq_natDegree plus injective map degree.
- **Hypotheses**: Universe-polymorphic CommSemiring R and Unique sigma; arbitrary polynomial; no nonzero, finite, DecidableEq, domain or field hypotheses.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.degreeOf_none_rename_mul_aeval`
- **Used by other files (lexical)**: `Roth.index_separated_mul_le_aux`
- **Visibility**: public
- **Lines**: 174–185; proof/body length 11 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_uniqueAlgEquiv_symm.md).

#### theorem Roth.degreeOf_rename_mul_aeval

Type:

```lean
@Roth.degreeOf_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommRing R] [IsDomain R]
  (U : MvPolynomial τ R) {V : Polynomial R},
  V ≠ 0 →
    ∀ (j : τ),
      MvPolynomial.degreeOf (some j) ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V) =
        MvPolynomial.degreeOf j U
```

- **What**: Multiplication by a nonzero univariate factor in a disjoint variable preserves every old-variable partial degree, allowing the other factor to be zero.
- **How**: Split U=0; use degreeOf_mul_eq, injective rename preservation and singleton-renaming normalization to show the other factor contributes zero.
- **Hypotheses**: arbitrary τ and R universes; CommRing R; IsDomain R; U arbitrary including zero; V≠0; j:τ; no Fintype/DecidableEq assumptions
- **Uses from project (lexical body)**: `Roth.aeval_X_eq_rename`
- **Project references in type**: []
- **Native direct body references**: `Roth.aeval_X_eq_rename`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_det_eq_mul`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 197–208; proof/body length 10 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_rename_mul_aeval.md).

#### theorem Roth.degreeOf_none_rename_mul_aeval

Type:

```lean
@Roth.degreeOf_none_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommRing R] [IsDomain R]
  {U : MvPolynomial τ R},
  U ≠ 0 →
    ∀ (V : Polynomial R),
      MvPolynomial.degreeOf none ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V) =
        V.natDegree
```

- **What**: The none-variable degree of a separated product U(x_τ)V(x_none) equals V.natDegree for U≠0, including V=0.
- **How**: Source uses degreeOf_mul_eq, zero degree of renamed U and singleton-variable degree bridge; verified alternative uses optionEquivLeft and constant multiplication natDegree.
- **Hypotheses**: Arbitrary τ,R; CommRing+IsDomain; U≠0; arbitrary V. Verified weakening CommSemiring+NoZeroDivisors and point-local leading-coefficient nonannihilation.
- **Uses from project (lexical body)**: `Roth.aeval_X_eq_rename`, `Roth.degreeOf_uniqueAlgEquiv_symm`
- **Project references in type**: []
- **Native direct body references**: `Roth.aeval_X_eq_rename`, `Roth.degreeOf_uniqueAlgEquiv_symm`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_det_eq_mul`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 213–226; proof/body length 12 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_none_rename_mul_aeval.md).

#### lemma Roth.linearIndependent_coordinate_polynomials_aux

Type:

```lean
∀ {R : Type u_3} {M : Type u_4}
  [inst : CommRing R] [inst_1 : AddCommMonoid M] [inst_2 : Module R M] {n l : ℕ} (v : Fin (n + 1) → M)
  (b : Module.Basis (Fin l) R ↥(Submodule.span R (Set.range v))),
  LinearIndependent R fun ρ ↦ ∑ ν, Polynomial.C ((b.repr ⟨v ν, ⋯⟩) ρ) * Polynomial.X ^ ↑ν
```

- **What**: Coordinate polynomials obtained by writing a finite spanning family in an arbitrary finite basis are linearly independent.
- **How**: A vanishing polynomial combination gives coefficient identities; form a linear functional and use LinearMap.ext_on on the spanning family, then evaluate it on basis vectors.
- **Hypotheses**: Module over a commutative ring with a finite indexed spanning family and basis. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_separated_representation`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 235–262; proof/body length 24 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_coordinate_polynomials_aux.md).

#### lemma Roth.eq_sum_aeval_basis_coeffNone_aux

Type:

```lean
∀ {τ : Type u_1} {R : Type u_3}
  [inst : CommSemiring R] {P : MvPolynomial (Option τ) R} {n l : ℕ},
  P = ∑ ν, MvPolynomial.X none ^ ↑ν * (MvPolynomial.rename some) (Roth.coeffNone P ↑ν) →
    ∀ (b : Module.Basis (Fin l) R ↥(Submodule.span R (Set.range fun ν ↦ Roth.coeffNone P ↑ν))),
      P =
        ∑ ρ,
          (Polynomial.aeval (MvPolynomial.X none))
              (∑ ν, Polynomial.C ((b.repr ⟨Roth.coeffNone P ↑ν, ⋯⟩) ρ) * Polynomial.X ^ ↑ν) *
            (MvPolynomial.rename some) ↑(b ρ)
```

- **What**: The separated expansion of a polynomial can be regrouped in any chosen basis of the span of its coefficient polynomials.
- **How**: Expand each coefficient with Module.Basis.sum_repr, exchange finite sums, and transport scalars through evaluation and renaming.
- **Hypotheses**: Commutative semiring, an existing coefficient expansion and a basis of its span. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.coeffNone`
- **Project references in type**: `Roth.coeffNone`
- **Native direct body references**: `Roth.coeffNone`
- **Native direct type references**: `Roth.coeffNone`
- **Used by in file (lexical)**: `Roth.exists_separated_representation`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 265–288; proof/body length 17 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_aeval_basis_coeffNone_aux.md).

#### lemma Roth.exists_coeffNone_basis_aux

Type:

```lean
∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {P : MvPolynomial (Option τ) K},
  P ≠ 0 →
    ∀ {n : ℕ},
      P = ∑ ν : Fin (n + 1), MvPolynomial.X none ^ ↑ν * (MvPolynomial.rename some) (Roth.coeffNone P ↑ν) →
        ∃ (l : ℕ) (b :
          Module.Basis (Fin l) K ↥(Submodule.span K (Set.range fun (ν : Fin (n + 1)) ↦ Roth.coeffNone P ↑ν))),
          1 ≤ l ∧ l ≤ n + 1 ∧ ∀ (ρ : Fin l) (j : τ), MvPolynomial.degreeOf j ↑(b ρ) ≤ MvPolynomial.degreeOf (some j) P
```

- **What**: The coefficient-polynomial span of a nonzero separated expansion has a finite basis of positive size at most n+1, whose members satisfy the original individual degree bounds.
- **How**: Use Module.finBasis on the finite coefficient span, derive positive finrank from nonzero expansion, and contain the span in restrictSupport to retain degree bounds.
- **Hypotheses**: Field coefficients, nonzero polynomial, finite distinguished-variable expansion. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.coeffNone`
- **Project references in type**: `Roth.coeffNone`
- **Native direct body references**: `Roth.coeffNone`
- **Native direct type references**: `Roth.coeffNone`
- **Used by in file (lexical)**: `Roth.exists_separated_representation`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 291–316; proof/body length 22 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_coeffNone_basis_aux.md).

#### theorem Roth.exists_separated_representation

Type:

```lean
∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {P : MvPolynomial (Option τ) K},
  P ≠ 0 →
    ∀ {n : ℕ},
      MvPolynomial.degreeOf none P ≤ n →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ n + 1 ∧
              ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
                LinearIndependent K φ ∧
                  LinearIndependent K ψ ∧
                    (∀ (ν : Fin l), (φ ν).natDegree ≤ n) ∧
                      (∀ (ν : Fin l) (j : τ), MvPolynomial.degreeOf j (ψ ν) ≤ MvPolynomial.degreeOf (some j) P) ∧
                        P =
                          ∑ ν : Fin l, (Polynomial.aeval (MvPolynomial.X none)) (φ ν) * (MvPolynomial.rename some) (ψ ν)
```

- **What**: Every nonzero polynomial in one distinguished and arbitrary remaining variables has a bounded separated decomposition with both factor families linearly independent.
- **How**: Expand coefficients by eq_sum_X_none_pow_mul_coeffNone, choose a bounded basis with exists_coeffNone_basis_aux, prove coordinate independence via linearIndependent_coordinate_polynomials_aux, and reconstruct with eq_sum_aeval_basis_coeffNone_aux.
- **Hypotheses**: τ : Type* arbitrary; K : Type* with Field K; P ≠ 0; degreeOf none P ≤ n
- **Uses from project (lexical body)**: `Roth.coeffNone`, `Roth.eq_sum_X_none_pow_mul_coeffNone`, `Roth.eq_sum_aeval_basis_coeffNone_aux`, `Roth.exists_coeffNone_basis_aux`, `Roth.linearIndependent_coordinate_polynomials_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.coeffNone`, `Roth.eq_sum_X_none_pow_mul_coeffNone`, `Roth.eq_sum_aeval_basis_coeffNone_aux`, `Roth.exists_coeffNone_basis_aux`, `Roth.linearIndependent_coordinate_polynomials_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 325–344; proof/body length 15 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_separated_representation.md).

#### theorem Roth.det_hasseDeriv_separated

Type:

```lean
∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {l : ℕ} (D : Fin l → τ →₀ ℕ)
  (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
  (Matrix.of fun (μ ν : Fin l) ↦
        (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν))
          (∑ ρ : Fin l, (Polynomial.aeval (X none)) (φ ρ) * (rename some) (ψ ρ))).det =
    (rename some) (genWronskian D ψ) * (Polynomial.aeval (X none)) (wronskian φ)
```

- **What**: The mixed Hasse derivative determinant of a separated polynomial sum is the product of the embedded generalized and univariate Hasse Wronskians.
- **How**: Use hasseDeriv_rename_mul_aeval to identify the derivative matrix as an embedded product; Matrix.det_mul, Matrix.det_transpose and AlgHom.map_det then give the two determinant factors.
- **Hypotheses**: Arbitrary variable type τ; no Fintype or DecidableEq τ survives elaboration; Field K is required by existing named Wronskian parents, while expanded identity verifies over CommRing; Any l including0, arbitrary D and families φ/ψ; no independence, characteristic, nonzero or order-bound premise
- **Uses from project (lexical body)**: `Roth.genWronskian`, `Roth.hasseDeriv_rename_mul_aeval`, `Roth.wronskian`, `Roth.wronskianMatrix`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.genWronskian`, `Roth.wronskian`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.genWronskian`, `Roth.hasseDeriv_rename_mul_aeval`, `Roth.wronskian`, `Roth.wronskianMatrix`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.genWronskian`, `Roth.wronskian`
- **Used by in file (lexical)**: `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 351–366; proof/body length 11 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.det_hasseDeriv_separated.md).

#### theorem Roth.exists_sum_mul_eq_gcd

Type:

```lean
∀ {ι : Type u_2} (s : Finset ι) (u : ι → ℤ), ∃ (z : ι → ℤ), ∑ i ∈ s, z i * u i = s.gcd u
```

- **What**: The gcd of finitely many integers is an integer linear combination of the family.
- **How**: Specialize Finset.gcd_eq_sum_mul to integers; reverse equality and commute factors.
- **Hypotheses**: arbitrary universe-polymorphic index type ι; s : Finset ι; u : ι → ℤ; no nonemptiness, nonzero or coprimality assumptions
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_int_eq_of_gcd_eq_one`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 374–376; proof/body length 2 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_sum_mul_eq_gcd.md).

#### theorem Roth.exists_nat_smul_eq_map

Type:

```lean
∀ {σ : Type u_2} (G : MvPolynomial σ ℚ),
  ∃ (N : ℕ) (U : MvPolynomial σ ℤ), 0 < N ∧ (map (Int.castRingHom ℚ)) U = ↑N • G
```

- **What**: Clears all rational coefficients of an arbitrary multivariate polynomial by a positive natural scalar.
- **How**: Take the product of coefficient denominators on finite support using Finset.dvd_prod_of_mem; Rat.den_mul_eq_num supplies integer scaled coefficients and Rat.den_pos ensures a positive common denominator, then reconstruct by coefficient extensionality.
- **Hypotheses**: Only σ : Type* and G : MvPolynomial σ ℚ; no finite/decidable/nonzero assumptions.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_primitive_smul_eq`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 380–400; proof/body length 20 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_nat_smul_eq_map.md).

#### theorem Roth.exists_primitive_smul_eq

Type:

```lean
∀ {σ : Type u_2} {G : MvPolynomial σ ℚ},
  G ≠ 0 →
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ),
      g ≠ 0 ∧ (map (Int.castRingHom ℚ)) U = g • G ∧ (U.support.gcd fun (d : σ →₀ ℕ) ↦ U.coeff d) = 1
```

- **What**: Every nonzero rational multivariate polynomial admits a nonzero rational scalar multiple which has integral coefficients with normalized coefficient gcd one.
- **How**: Clear denominators; Finset.extract_gcd; reconstruct divided coefficients as a polynomial; prove nonzero gcd, coefficient scaling and support equality.
- **Hypotheses**: Arbitrary universe-polymorphic variable type σ, no Fintype/Finite/DecidableEq instances.; G : MvPolynomial σ ℚ, G ≠ 0 essential.
- **Uses from project (lexical body)**: `Roth.exists_nat_smul_eq_map`
- **Project references in type**: []
- **Native direct body references**: `Roth.exists_nat_smul_eq_map`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_int_factors`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 406–438; proof/body length 31 lines.
- **Notes**: proof/body >30 lines
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_primitive_smul_eq.md).

#### theorem Roth.exists_int_eq_of_gcd_eq_one

Type:

```lean
∀ {ι : Type u_2} {s : Finset ι} {u : ι → ℤ},
  s.gcd u = 1 → ∀ {v : ℚ}, (∀ a ∈ s, ∃ (z : ℤ), ↑(u a) * v = ↑z) → ∃ (z : ℤ), v = ↑z
```

- **What**: A finite gcd-one integer family detects integrality of a rational scalar from integrality of all selected products.
- **How**: Use exists_sum_mul_eq_gcd for finite Bezout coefficients, choose integer product witnesses, and distribute their weighted sum with Finset.sum_mul to construct the integer scalar witness.
- **Hypotheses**: arbitrary index type ι; finite subset s; integer coefficient family u; s.gcd u = 1; each (u a : ℚ) * v has an integer witness for a∈s
- **Uses from project (lexical body)**: `Roth.exists_sum_mul_eq_gcd`
- **Project references in type**: []
- **Native direct body references**: `Roth.exists_sum_mul_eq_gcd`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_int_polynomial_of_primitive_factor_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 443–454; proof/body length 11 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_int_eq_of_gcd_eq_one.md).

#### lemma Roth.rescale_separated_factor_aux

Type:

```lean
∀ {τ : Type u_1} {K : Type u_2} [inst : Field K]
  {U' U : MvPolynomial τ K} {V' : Polynomial K} {F : MvPolynomial (Option τ) K} {g : K},
  g ≠ 0 →
    U = g • U' →
      F = (rename some) U' * (Polynomial.aeval (X none)) V' →
        F = (rename some) U * (Polynomial.aeval (X none)) (Polynomial.C g⁻¹ * V')
```

- **What**: A nonzero scalar can be transferred from the multivariate separated factor to the univariate factor by multiplying the latter by the reciprocal constant polynomial.
- **How**: Move scalar constants through renaming and evaluation and cancel the scalar with its inverse.
- **Hypotheses**: Field coefficients; nonzero scale; a given separated factorization. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_int_factors`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 457–463; proof/body length 3 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.rescale_separated_factor_aux.md).

#### lemma Roth.exists_int_polynomial_of_primitive_factor_aux

Type:

```lean
∀ {τ : Type u_1} {U : MvPolynomial τ ℤ} {V' : Polynomial ℚ} {F : MvPolynomial (Option τ) ℤ},
  U.support.gcd ⇑U.coeff = 1 →
    (map (Int.castRingHom ℚ)) F = (rename some) ((map (Int.castRingHom ℚ)) U) * (Polynomial.aeval (X none)) V' →
      ∃ (V : Polynomial ℤ), Polynomial.map (Int.castRingHom ℚ) V = V'
```

- **What**: When an integer multivariate polynomial is a separated product of an integer factor with coefficient gcd one and a rational univariate factor, the univariate factor has integer coefficients.
- **How**: Extract every product coefficient with coeff_rename_mul_aeval and use exists_int_eq_of_gcd_eq_one; Polynomial.mem_map_range assembles the integral factor.
- **Hypotheses**: Primitive integral ordinary-variable factor and integral separated product. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.coeff_rename_mul_aeval`, `Roth.exists_int_eq_of_gcd_eq_one`
- **Project references in type**: []
- **Native direct body references**: `Roth.coeff_rename_mul_aeval`, `Roth.exists_int_eq_of_gcd_eq_one`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_int_factors`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 466–478; proof/body length 9 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_int_polynomial_of_primitive_factor_aux.md).

#### theorem Roth.exists_int_factors

Type:

```lean
∀ {τ : Type u_1} {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ},
  U' ≠ 0 →
    V' ≠ 0 →
      ∀ {F : MvPolynomial (Option τ) ℤ},
        (map (Int.castRingHom ℚ)) F = (rename some) U' * (Polynomial.aeval (X none)) V' →
          ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ),
            U ≠ 0 ∧
              V ≠ 0 ∧
                F = (rename some) U * (Polynomial.aeval (X none)) V ∧
                  (∀ (j : τ), degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree
```

- **What**: Descend a nonzero separated rational factorization of an integer polynomial to integer factors, preserving all factor degrees.
- **How**: Roth.exists_primitive_smul_eq supplies a primitive scalar representative; Roth.rescale_separated_factor_aux transfers the inverse scalar to the right factor; Roth.exists_int_polynomial_of_primitive_factor_aux descends its coefficients. MvPolynomial.map_injective descends equality; degrees_map_of_injective/degreeOf_C_mul and Polynomial.natDegree_map_eq_of_injective/natDegree_C_mul transport all degrees.
- **Hypotheses**: Arbitrary variable type τ; no Fintype or DecidableEq.; Nonzero U′ and V′.; Exact mapped factorization of integral F.
- **Uses from project (lexical body)**: `Roth.exists_int_polynomial_of_primitive_factor_aux`, `Roth.exists_primitive_smul_eq`, `Roth.rescale_separated_factor_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.exists_int_polynomial_of_primitive_factor_aux`, `Roth.exists_primitive_smul_eq`, `Roth.rescale_separated_factor_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_det_eq_mul`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 485–505; proof/body length 16 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_int_factors.md).

#### lemma Roth.exists_rat_factors_det_hasseDeriv_aux

Type:

```lean
∀ {τ : Type u_1} [Finite τ] {P : MvPolynomial (Option τ) ℤ},
  P ≠ 0 →
    ∀ {n : ℕ},
      degreeOf none P ≤ n →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ n + 1 ∧
              ∃ (D : Fin l → τ →₀ ℕ),
                (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧
                  ∃ (U : MvPolynomial τ ℚ) (V : Polynomial ℚ),
                    U ≠ 0 ∧
                      V ≠ 0 ∧
                        (map (Int.castRingHom ℚ))
                            (Matrix.of fun (μ ν : Fin l) ↦
                                (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) P).det =
                          (rename some) U * (Polynomial.aeval (X none)) V
```

- **What**: A nonzero integer polynomial has a nonzero separated rational factorization of a finite Hasse-derivative determinant, with the determinant size and derivative orders bounded by the distinguished-variable degree.
- **How**: Apply exists_separated_representation over the rationals, choose differential operators with exists_genWronskian_ne_zero, and use det_hasseDeriv_separated with ordinary Wronskian nonvanishing.
- **Hypotheses**: Finitely many ordinary variables; nonzero integer polynomial with distinguished degree bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.det_hasseDeriv_separated`, `Roth.exists_genWronskian_ne_zero`, `Roth.exists_separated_representation`, `Roth.genWronskian`, `Roth.wronskian`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.det_hasseDeriv_separated`, `Roth.exists_genWronskian_ne_zero`, `Roth.exists_separated_representation`, `Roth.genWronskian`, `Roth.wronskian`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `Roth.exists_det_eq_mul`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 510–534; proof/body length 20 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_rat_factors_det_hasseDeriv_aux.md).

#### theorem Roth.exists_det_eq_mul

Type:

```lean
∀ {τ : Type u_1} [Finite τ] {P : MvPolynomial (Option τ) ℤ},
  P ≠ 0 →
    ∀ {r : Option τ → ℕ},
      (∀ (j : Option τ), degreeOf j P ≤ r j) →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ r none + 1 ∧
              ∃ (D : Fin l → τ →₀ ℕ),
                (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧
                  ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ),
                    U ≠ 0 ∧
                      V ≠ 0 ∧
                        (∀ (j : τ), degreeOf j U ≤ l * r (some j)) ∧
                          V.natDegree ≤ l * r none ∧
                            (Matrix.of fun (μ ν : Fin l) ↦
                                  (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) P).det =
                              (rename some) U * (Polynomial.aeval (X none)) V
```

- **What**: A nonzero integer polynomial admits an order-bounded mixed Hasse-derivative determinant that factors into nonzero integer polynomials in disjoint variable groups, with l and both individual degree bounds.
- **How**: exists_rat_factors_det_hasseDeriv_aux uses exists_separated_representation, exists_genWronskian_ne_zero, wronskian_ne_zero_of_linearIndependent and det_hasseDeriv_separated; exists_int_factors descends to integers; degreeOf_rename_mul_aeval, degreeOf_none_rename_mul_aeval and degreeOf_det_hasseDeriv_le prove the bounds.
- **Hypotheses**: τ : Type*; Finite τ in original; verified arbitrary ambient τ; P ≠ 0; r : Option τ → ℕ; ∀ j, degreeOf j P ≤ r j; original coefficients ℤ; verified CommRing/IsDomain/NormalizedGCDMonoid/CharZero R
- **Uses from project (lexical body)**: `Roth.degreeOf_det_hasseDeriv_le`, `Roth.degreeOf_none_rename_mul_aeval`, `Roth.degreeOf_rename_mul_aeval`, `Roth.exists_int_factors`, `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.degreeOf_det_hasseDeriv_le`, `Roth.degreeOf_none_rename_mul_aeval`, `Roth.degreeOf_rename_mul_aeval`, `Roth.exists_int_factors`, `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_le_lem6`
- **Visibility**: public
- **Lines**: 542–559; proof/body length 12 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_det_eq_mul.md).

#### File structural summary

- Written declarations: 27; kinds: {'def': 1, 'theorem': 19, 'lemma': 7}
- **Key API (at least three lexical callers)**: `Roth.coeffNone`, `Roth.aeval_X_eq_rename`
- **Unused in file (observation)**: `Roth.degreeOf_coeffNone_le`, `Roth.coeff_uniqueAlgEquiv_symm`, `Roth.exists_det_eq_mul`
- **Proofs over 30 lines**: `Roth.exists_primitive_smul_eq`
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Taylor.lean

Completed assessments: 22/22.

#### def MvPolynomial.taylor

Type:

```lean
{σ : Type u_1} → {R : Type u_2} → [CommSemiring R] → (σ → R) → MvPolynomial σ R →ₐ[R] MvPolynomial σ R
```

- **What**: Translation of multivariate polynomials by a constant vector, P(X+α).
- **How**: Universal algebra evaluation at X j + C (α j).
- **Hypotheses**: Arbitrary independent variable/coefficient universes, commutative coefficient semiring, arbitrary translation vector; no finiteness or characteristic restrictions.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `MvPolynomial.taylor_apply`, `MvPolynomial.taylor_X`, `MvPolynomial.taylor_C`, `MvPolynomial.taylor_monomial`, `MvPolynomial.coeff_taylor_monomial_single_add_aux`, `MvPolynomial.coeff_taylor_monomial_aux`, `MvPolynomial.coeff_taylor`, `MvPolynomial.eval_taylor`, `MvPolynomial.taylor_taylor`, `MvPolynomial.taylor_zero`, `MvPolynomial.taylor_map`, `MvPolynomial.taylor_rename`, `MvPolynomial.degreeOf_taylor_le`, `MvPolynomial.taylor_neg_taylor`, `MvPolynomial.taylor_injective`, `MvPolynomial.taylor_eq_zero_iff`, `MvPolynomial.eq_sum_box_hasseDeriv`
- **Used by other files (lexical)**: `Roth.index`, `Roth.mem_support_taylor_iff`, `Roth.index_le_weight`, `Roth.exists_weight_eq_index`, `Roth.index_eq_weightedOrder_div`, `Roth.index_mul`, `Roth.index_mul_left_weights`
- **Visibility**: public
- **Lines**: 42–43; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md).

#### theorem MvPolynomial.taylor_apply

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (P : MvPolynomial σ R), (MvPolynomial.taylor α) P = (MvPolynomial.aeval fun j ↦ MvPolynomial.X j + MvPolynomial.C (α j)) P
```

- **What**: Applying polynomial translation is substitution of X j + C (α j).
- **How**: Kernel reflexivity after unfolding the local taylor definition; no theorem calls.
- **Hypotheses**: Arbitrary independent variable/coefficient universes; commutative coefficient semiring; arbitrary α and P.
- **Uses from project (lexical body)**: []
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 46–47; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_apply.md).

#### theorem MvPolynomial.taylor_X

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (j : σ), (MvPolynomial.taylor α) (MvPolynomial.X j) = MvPolynomial.X j + MvPolynomial.C (α j)
```

- **What**: Translation sends the generator X j to X j plus the constant α j.
- **How**: Direct existing MvPolynomial.aeval_X theorem application after definitional reduction of the parent taylor; one existing-law call, no closing simp required.
- **Hypotheses**: Arbitrary independent variable and coefficient universes, CommSemiring R, arbitrary α : σ → R and j : σ.
- **Uses from project (lexical body)**: []
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: []
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 51–51; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_X.md).

#### theorem MvPolynomial.taylor_C

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (a : R), (MvPolynomial.taylor α) (MvPolynomial.C a) = MvPolynomial.C a
```

- **What**: Translation fixes constant polynomials.
- **How**: One existing-law specialization MvPolynomial.algHom_C _ _.
- **Hypotheses**: Arbitrary variable type σ, commutative coefficient semiring R, translation vector α, scalar a; no finiteness/nonzero/characteristic constraints.
- **Uses from project (lexical body)**: []
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_C_mul`
- **Visibility**: public
- **Lines**: 55–55; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_C.md).

#### theorem MvPolynomial.taylor_monomial

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α : σ → R) (k : σ →₀ ℕ) (a : R), (MvPolynomial.taylor α) ((MvPolynomial.monomial k) a) = MvPolynomial.C a * k.prod (fun j n ↦ (MvPolynomial.X j + MvPolynomial.C (α j)) ^ n)
```

- **What**: Translation of a monomial is its coefficient times the product of translated coordinate powers.
- **How**: One direct application of existing MvPolynomial.aeval_monomial.
- **Hypotheses**: Arbitrary variable/coefficient universes; CommSemiring R; arbitrary shift α, finite natural exponent k, coefficient a.
- **Uses from project (lexical body)**: []
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: []
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.eq_sum_box_hasseDeriv`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 59–61; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_monomial.md).

#### lemma MvPolynomial.coeff_aeval_X_mul

Type:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (i : σ) (f : R[X]) (B : MvPolynomial σ R),
  (∀ e ∈ B.support, e i = 0) →
    ∀ (d : σ →₀ ℕ), ((Polynomial.aeval (X i)) f * B).coeff d = f.coeff (d i) * B.coeff (Finsupp.erase i d)
```

- **What**: Computes the coefficient of the product of a univariate polynomial in one variable and a multivariate polynomial independent of that variable.
- **How**: Expands Polynomial.eval₂_eq_sum and coeff_monomial_mul', then Finset.sum_eq_single selects the only possible univariate exponent; the support-independence hypothesis kills every other summand.
- **Hypotheses**: Arbitrary variable type and commutative semiring; second factor has zero selected-coordinate exponent throughout its support. No finiteness or nonzero assumptions.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 63–80; proof/body length 15 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_aeval_X_mul.md).

#### lemma MvPolynomial.hasseCoeff_single_add_eq

Type:

```lean
∀ {σ : Type u_2} {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 → ∀ (d : σ →₀ ℕ), hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (Finsupp.erase i d) k'
```

- **What**: Splits a multivariate binomial factor into one coordinate's binomial coefficient and the factor on the erased multi-index.
- **How**: Uses Finsupp.mul_prod_erase' to extract the selected coordinate; all other coordinates are unchanged because the added one-coordinate term vanishes there.
- **Hypotheses**: Arbitrary variable type and natural finitely supported indices; residual exponent k′ has zero selected coordinate. No coefficient semiring or finite-variable assumption.
- **Uses from project (lexical body)**: `MvPolynomial.hasseCoeff`
- **Project references in type**: `MvPolynomial.hasseCoeff`
- **Native direct body references**: `MvPolynomial.hasseCoeff`
- **Native direct type references**: `MvPolynomial.hasseCoeff`
- **Used by in file (lexical)**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 82–90; proof/body length 8 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_single_add_eq.md).

#### lemma MvPolynomial.prod_pow_single_add_tsub

Type:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 →
    ∀ (d : σ →₀ ℕ),
      ((Finsupp.single i n + k' - d).prod fun j e ↦ α j ^ e) =
        α i ^ (n - d i) * (k' - Finsupp.erase i d).prod fun j e ↦ α j ^ e
```

- **What**: Factors the evaluation of a lowered single-coordinate-plus-residual monomial into the selected coordinate power and the erased residual product.
- **How**: Coordinate extensionality identifies the truncated exponent subtraction; Finsupp.prod_add_index' and pow_add split the resulting product.
- **Hypotheses**: Original: arbitrary variables and commutative semiring; residual coordinate k′ i=0. Verified same proof under only CommMonoid for values, no semiring operations needed.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 92–99; proof/body length 6 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.prod_pow_single_add_tsub.md).

#### lemma MvPolynomial.coeff_taylor_monomial_single_add_aux

Type:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (a : R) {i : σ} (n : ℕ) {k : σ →₀ ℕ},
  k i = 0 →
    (∀ (d : σ →₀ ℕ), ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))) →
      ∀ (d : σ →₀ ℕ),
        ((taylor α) ((monomial (Finsupp.single i n + k)) a)).coeff d =
          (eval α) ((hasseDeriv d) ((monomial (Finsupp.single i n + k)) a))
```

- **What**: Proves the coefficient Taylor identity for a monomial after adding one new coordinate, assuming the identity for the residual monomial.
- **How**: Separate residual-variable support with coeff_aeval_X_mul, apply Polynomial.coeff_X_add_C_pow to the one-variable factor, and combine hasseCoeff_single_add_eq with prod_pow_single_add_tsub.
- **Hypotheses**: Arbitrary variables and commutative semiring; residual exponent zero in selected coordinate; induction hypothesis for all residual coefficients; n and a unrestricted.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_aeval_X_mul`, `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.hasseCoeff_single_add_eq`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.prod_pow_single_add_tsub`, `MvPolynomial.taylor`, `MvPolynomial.taylor_X`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.coeff_aeval_X_mul`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_eq_zero_iff`, `MvPolynomial.hasseCoeff_single_add_eq`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.prod_pow_single_add_tsub`, `MvPolynomial.taylor`, `MvPolynomial.taylor_X`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.coeff_taylor_monomial_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 101–118; proof/body length 14 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_single_add_aux.md).

#### lemma MvPolynomial.coeff_taylor_monomial_aux

Type:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (d k : σ →₀ ℕ) (a : R),
  ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))
```

- **What**: Proves the coefficient Taylor identity for every monomial over arbitrary commutative semirings.
- **How**: Inducts on the finitely supported exponent; constant base cases use scalar homomorphism/derivative rules, coordinate extension uses private induction-step helper.
- **Hypotheses**: Arbitrary variable type and commutative semiring; arbitrary translation, coefficient and multi-indices, with no support/degree/nonzero/finite-variable assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`, `MvPolynomial.hasseDeriv_C`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.coeff_taylor_monomial_single_add_aux`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_C`, `MvPolynomial.hasseDeriv_zero`, `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.coeff_taylor`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 120–129; proof/body length 9 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_aux.md).

#### theorem MvPolynomial.coeff_taylor

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R), (MvPolynomial.taylor α P).coeff d = MvPolynomial.eval α (MvPolynomial.hasseDeriv d P)
```

- **What**: The coefficient of a translated multivariate polynomial is its Hasse derivative evaluated at the translation point.
- **How**: Additive polynomial induction and a separately verified monomial binomial-coefficient calculation; native direct-constant audit excludes circular target use.
- **Hypotheses**: σ,R arbitrary independent universes; CommSemiring R; no Fintype, DecidableEq, Nontrivial, domain or characteristic assumptions; arbitrary α,d,P
- **Uses from project (lexical body)**: `MvPolynomial.coeff_taylor_monomial_aux`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.coeff_taylor_monomial_aux`, `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.degreeOf_taylor_le`, `MvPolynomial.eq_sum_box_hasseDeriv`
- **Used by other files (lexical)**: `Roth.mem_support_taylor_iff`, `Roth.index_eq_weightedOrder_div`
- **Visibility**: public
- **Lines**: 134–138; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor.md).

#### theorem MvPolynomial.eval_taylor

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α x : σ → R) (P : MvPolynomial σ R), eval x (taylor α P) = eval (fun j ↦ x j + α j) P
```

- **What**: Evaluating a translated polynomial at x equals evaluating the original at x+α.
- **How**: Generic eval_assoc plus add, variable, and constant evaluation normalization; one closing simp.
- **Hypotheses**: CommSemiring R; arbitrary independent-universe σ,R; no finite or degree assumptions
- **Uses from project (lexical body)**: `MvPolynomial.taylor`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 141–143; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_taylor.md).

#### theorem MvPolynomial.taylor_taylor

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α β : σ → R) (P : MvPolynomial σ R), taylor α (taylor β P) = taylor (fun j ↦ α j + β j) P
```

- **What**: Two constant polynomial translations compose by adding their translation vectors.
- **How**: Generic comp_aeval_apply followed by normalization of evaluation on variable plus constant, associativity, and constant-map additivity.
- **Hypotheses**: CommSemiring R; arbitrary independent-universe σ,R; no finite variables, degree bound, characteristic, decidable equality, or nonzero condition
- **Uses from project (lexical body)**: `MvPolynomial.taylor`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.taylor_neg_taylor`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 146–148; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_taylor.md).

#### theorem MvPolynomial.taylor_zero

Type:

```lean
∀ {σ : Type u_3} {R : Type u_4} [CommSemiring R] (P : MvPolynomial σ R), (MvPolynomial.taylor fun x ↦ 0) P = P
```

- **What**: Zero translation fixes every multivariate polynomial.
- **How**: Normalize each generator X j+C 0 to X j, then apply aeval_X_left_apply.
- **Hypotheses**: Arbitrary variable type σ, coefficient commutative semiring R, and polynomial P; no other hypotheses.
- **Uses from project (lexical body)**: `MvPolynomial.taylor`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 152–153; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_zero.md).

#### theorem MvPolynomial.taylor_map

Type:

```lean
∀ {σ : Type u} {R : Type v} [CommSemiring R] {S : Type w} [CommSemiring S] (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R), MvPolynomial.taylor (fun j ↦ f (α j)) (MvPolynomial.map f P) = MvPolynomial.map f (MvPolynomial.taylor α P)
```

- **What**: Translation commutes with coefficient change, mapping the translation vector as well as the polynomial.
- **How**: Generic substitution-map naturality followed by normalization of mapped generators using map_add/map_X/map_C.
- **Hypotheses**: Arbitrary independent-universe variable/source/target types, commutative semirings R and S, arbitrary unital semiring homomorphism f, translation vector and polynomial. No injectivity, characteristic or finite-variable conditions.
- **Uses from project (lexical body)**: `MvPolynomial.taylor`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 157–159; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_map.md).

#### theorem MvPolynomial.taylor_rename

Type:

```lean
∀ {σ : Type u} {R : Type v} [CommSemiring R] {τ : Type w} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R), MvPolynomial.taylor α (MvPolynomial.rename f P) = MvPolynomial.rename f (MvPolynomial.taylor (α ∘ f) P)
```

- **What**: Translation commutes with arbitrary variable renaming, restricting the shift along the variable map.
- **How**: Generic aevaluation/renaming composition, then normalization of shifted generators.
- **Hypotheses**: Arbitrary independent-universe σ,τ,R; CommSemiring R; arbitrary map f including noninjective, arbitrary α,P. No finiteness/characteristic/nonzero assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.taylor`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_rename`
- **Visibility**: public
- **Lines**: 164–166; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_rename.md).

#### theorem MvPolynomial.degreeOf_taylor_le

Type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α : σ → R) (j : σ) (P : MvPolynomial σ R), MvPolynomial.degreeOf j (MvPolynomial.taylor α P) ≤ MvPolynomial.degreeOf j P
```

- **What**: Constant coordinate translation does not increase degree in any chosen variable.
- **How**: An exponent above the original coordinate degree has zero Hasse derivative, hence zero translated coefficient; apply the support characterization of degree.
- **Hypotheses**: Arbitrary independent-universe σ,R; CommSemiring R; arbitrary shift, variable and polynomial. No finiteness, nonzero, domain or characteristic restriction.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `MvPolynomial.taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.index_le_card`
- **Visibility**: public
- **Lines**: 170–173; proof/body length 3 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_taylor_le.md).

#### theorem MvPolynomial.taylor_neg_taylor

Type:

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), MvPolynomial.taylor (fun j ↦ -α j) (MvPolynomial.taylor α P) = P
```

- **What**: Translating a polynomial and translating back by the negative vector returns the original polynomial.
- **How**: Substitution composition adds the shift vectors; additive cancellation and zero-translation identity then give the result.
- **Hypotheses**: Arbitrary independent-universe variable and coefficient types, commutative coefficient ring, every shift and polynomial. No finiteness, nonzero, field or characteristic assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.taylor_taylor`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`, `MvPolynomial.taylor_taylor`, `MvPolynomial.taylor_zero`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.taylor_injective`, `MvPolynomial.eq_sum_box_hasseDeriv`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 182–184; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_neg_taylor.md).

#### theorem MvPolynomial.taylor_injective

Type:

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A), Function.Injective (MvPolynomial.taylor α : MvPolynomial σ A → MvPolynomial σ A)
```

- **What**: Translation by any coefficient vector is injective on formal multivariate polynomials over a commutative ring.
- **How**: Apply generic Function.LeftInverse.injective to opposite-shift cancellation.
- **Hypotheses**: Arbitrary independent-universe variables and coefficients, CommRing, every shift. No finiteness, field, domain, characteristic or nontriviality hypotheses.
- **Uses from project (lexical body)**: `MvPolynomial.taylor_neg_taylor`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`, `MvPolynomial.taylor_neg_taylor`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: `MvPolynomial.taylor_eq_zero_iff`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 187–188; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_injective.md).

#### theorem MvPolynomial.taylor_eq_zero_iff

Type:

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), MvPolynomial.taylor α P = 0 ↔ P = 0
```

- **What**: Formal multivariate polynomial translation reflects zero; current ring hypothesis can be weakened to CommSemiring.
- **How**: Original proof derives zero reflection from inverse-based injectivity. Verified stronger proof chooses a maximal supported exponent, whose Hasse derivative is its nonzero constant coefficient, contradicting zero translate.
- **Hypotheses**: Arbitrary independent-universe variables and coefficients, shift and polynomial. CommRing currently, verified CommSemiring replacement; no finite/domain/characteristic/nontrivial assumptions.
- **Uses from project (lexical body)**: `MvPolynomial.taylor_injective`
- **Project references in type**: `MvPolynomial.taylor`
- **Native direct body references**: `MvPolynomial.taylor`, `MvPolynomial.taylor_injective`
- **Native direct type references**: `MvPolynomial.taylor`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 192–193; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_eq_zero_iff.md).

#### theorem MvPolynomial.eq_sum_box_hasseDeriv

Type:

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A), (∀ j, MvPolynomial.degreeOf j P ≤ r j) → P = ∑ d ∈ Roth.box r, MvPolynomial.C (MvPolynomial.eval α (MvPolynomial.hasseDeriv d P)) * ∏ j, (MvPolynomial.X j - MvPolynomial.C (α j)) ^ d j
```

- **What**: Reconstructs a polynomial from Hasse derivative values at a center as a finite sum of products of powers of X minus that center over a bounding coordinate box.
- **How**: Coefficient extensionality and coeff_taylor identify translated coefficients; hasseDeriv_eq_zero_of_degreeOf_lt kills out-of-box terms, and taylor_neg_taylor plus taylor_monomial transport back.
- **Hypotheses**: Arbitrary commutative coefficient ring, finite variable enumeration, arbitrary center and polynomial, natural coordinatewise degree bounds. Explicit DecidableEq can be removed using scoped Classical and propositional instance transport.
- **Uses from project (lexical body)**: `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `MvPolynomial.taylor`, `MvPolynomial.taylor_monomial`, `MvPolynomial.taylor_neg_taylor`, `Roth.box`, `Roth.mem_box`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.box`
- **Native direct body references**: `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `MvPolynomial.taylor`, `MvPolynomial.taylor_monomial`, `MvPolynomial.taylor_neg_taylor`, `Roth.box`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.box`
- **Used by in file (lexical)**: `MvPolynomial.eval_eq_sum_box`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 197–213; proof/body length 15 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.eq_sum_box_hasseDeriv.md).

#### theorem MvPolynomial.eval_eq_sum_box

Type:

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A), (∀ j, MvPolynomial.degreeOf j P ≤ r j) → MvPolynomial.eval x P = ∑ d ∈ Roth.box r, MvPolynomial.eval α (MvPolynomial.hasseDeriv d P) * ∏ j, (x j - α j) ^ d j
```

- **What**: Evaluates a polynomial as a finite Hasse Taylor expansion about an arbitrary center, over its coordinate degree-bounding box.
- **How**: Apply the evaluation ring homomorphism to eq_sum_box_hasseDeriv and distribute over finite sums, products, powers, variables and constants; no repeated binomial proof. Strongest scalar-extension form additionally transports degree via support_map_subset and Hasse evaluation via hasseDeriv_map/eval₂_eq_eval_map.
- **Hypotheses**: Arbitrary commutative coefficient ring and finite variable type, arbitrary center/point/polynomial, natural coordinate bounds with each degree bounded. Explicit DecidableEq removable through scoped Classical and propositional original-instance recovery.
- **Uses from project (lexical body)**: `MvPolynomial.eq_sum_box_hasseDeriv`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.box`
- **Native direct body references**: `MvPolynomial.eq_sum_box_hasseDeriv`, `MvPolynomial.hasseDeriv`, `Roth.box`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.box`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.abs_eval_lt_of_le_index`
- **Visibility**: public
- **Lines**: 217–220; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_eq_sum_box.md).

#### File structural summary

- Written declarations: 22; kinds: {'def': 1, 'theorem': 16, 'lemma': 5}
- **Key API (at least three lexical callers)**: `MvPolynomial.taylor`, `MvPolynomial.coeff_taylor`
- **Unused in file (observation)**: `MvPolynomial.taylor_apply`, `MvPolynomial.taylor_C`, `MvPolynomial.eval_taylor`, `MvPolynomial.taylor_zero`, `MvPolynomial.taylor_map`, `MvPolynomial.taylor_rename`, `MvPolynomial.degreeOf_taylor_le`, `MvPolynomial.taylor_eq_zero_iff`, `MvPolynomial.eval_eq_sum_box`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Theta.lean

Completed assessments: 50/50.

#### def Roth.RSet

Type:

```lean
{σ : Type u_1} → ℝ → (σ → ℕ) → Set (MvPolynomial σ ℤ)
```

- **What**: Nonzero integer multivariate polynomials with individual degrees bounded by r and every real-cast coefficient absolute value bounded by B.
- **How**: Constructs a Set by conjoining nonzero, degreeOf bounds, and all coefficient absolute-value bounds. The degree component is equivalent to the carrier of MvPolynomial.restrictSupport ℤ {d | ∀ j, d j ≤ r j}; this needs degreeOf_le_iff plus quantifier reordering, not a definitional replacement of the whole set.
- **Hypotheses**: Arbitrary universe-polymorphic σ, B : ℝ, r : σ → ℕ; no Fintype, DecidableEq, positivity, or finite-support assumption is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.indexSet`, `Roth.one_mem_RSet`, `Roth.index_le_Θ`, `Roth.Θ_le_of_forall_index_le`, `Roth.index_separated_mul_le_aux`, `Roth.index_det_le`, `Roth.index_le_lem6`
- **Used by other files (lexical)**: `Roth.sub_mem_RSet`, `Roth.exists_mem_RSet_le_index_aux`, `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`
- **Visibility**: public
- **Lines**: 56–57; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.RSet.md).

#### def Roth.indexSet

Type:

```lean
{σ : Type u_1} → [Fintype σ] → ℝ → (σ → ℕ) → (σ → ℕ) → Set ℝ
```

- **What**: Set of all real polynomial indices from nonzero integer polynomials with each degree and every coefficient bounded, evaluated at coordinatewise coprime integer numerators over fixed natural denominators.
- **How**: Two independent bounded existential choices are exactly Set.image2 of the index-evaluation map over RSet and the coprime numerator set. Native bridge is rfl; the expanded index infDegree bridge requires finite-order normalization.
- **Hypotheses**: Arbitrary universe-polymorphic σ, Fintype σ, B : ℝ, q r : σ → ℕ. No captured DecidableEq, positivity, nonempty variable type, positive denominators or weights.
- **Uses from project (lexical body)**: `Roth.RSet`, `Roth.index`
- **Project references in type**: []
- **Native direct body references**: `Roth.RSet`, `Roth.index`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.Θ`, `Roth.indexSet_nonempty`, `Roth.indexSet_bddAbove`, `Roth.indexSet_comp_subset`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 62–64; proof/body length 2 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.indexSet.md).

#### def Roth.Θ

Type:

```lean
{σ : Type u_1} → [Fintype σ] → ℝ → (σ → ℕ) → (σ → ℕ) → ℝ
```

- **What**: Real supremum of weighted indices over nonzero integer polynomials with individual degree/coefficient bounds and all coprime numerator vectors at fixed natural denominators.
- **How**: Exactly SupSet.sSup applied to indexSet; independently re-aimed to sSup of Set.image2 with full index map, and freshly normalized to infDegree/Finsupp.weight/aeval with untopD0.
- **Hypotheses**: Universe-polymorphic σ, Fintype σ, B : ℝ, q r : σ → ℕ. No captured DecidableEq, positivity or nonempty variable condition.
- **Uses from project (lexical body)**: `Roth.indexSet`
- **Project references in type**: []
- **Native direct body references**: `Roth.indexSet`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.index_le_Θ`, `Roth.Θ_nonneg`, `Roth.Θ_le_card`, `Roth.Θ_le_of_forall_index_le`, `Roth.Θ_mono`, `Roth.Θ_equiv`, `Roth.Θ_unique_le`, `Roth.lem6Φ`, `Roth.Θ_option_le`, `Roth.theta_scaled_unique_le_aux`, `Roth.theta_prefix_lt_aux`, `Roth.theta_lt_base_aux`, `Roth.theta_phi_lt_aux`, `Roth.theta_lt_succ_aux`, `Roth.theta_lt_of_large_delta_aux`, `Roth.Θ_lt`
- **Used by other files (lexical)**: `Roth.theta_lt_eta_of_sq_log_bound_aux`, `Roth.exists_auxiliary_polynomial_with_index_gap_aux`, `Roth.main_lemma`
- **Visibility**: public
- **Lines**: 68–68; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ.md).

#### def Roth.lem6M

Type:

```lean
ℕ → ℕ → ℝ → ℕ → ℝ
```

- **What**: Auxiliary coefficient envelope M=(r₁+1)^(pl) l! B^l 2^(plr₁) for Roth Lemma6.
- **How**: One arithmetic expression using natural casts, powers, factorial and multiplication.
- **Hypotheses**: p,r₁,l natural; B arbitrary real; no positivity, finiteness or DecidableEq assumptions.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.one_le_lem6M`, `Roth.index_det_le`, `Roth.index_le_lem6`, `Roth.Θ_option_le`, `Roth.lem6M_lt`, `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 270–271; proof/body length 1 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.lem6M.md).

#### def Roth.lem6Φ

Type:

```lean
{τ : Type u_2} → [Fintype τ] → (Option τ → ℕ) → (Option τ → ℕ) → ℝ → ℕ → ℝ
```

- **What**: Auxiliary Phi of Roth Lemma6: sum of extremal polynomial indices in distinguished and complementary variables with common coefficient bound and scaled degree vectors.
- **How**: Adds two real suprema; both complete arithmetic input sets and totalized real sSup conventions independently verified.
- **Hypotheses**: τ arbitrary finite type; q,r:Option τ→ℕ; M:ℝ;l:ℕ. No DecidableEq, positivity or nonempty hypotheses.
- **Uses from project (lexical body)**: `Roth.Θ`
- **Project references in type**: []
- **Native direct body references**: `Roth.Θ`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.index_separated_mul_le_aux`, `Roth.index_det_le`, `Roth.index_le_lem6`, `Roth.Θ_option_le`, `Roth.theta_lt_succ_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 275–276; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.lem6Φ.md).

#### theorem Roth.one_mem_RSet

Type:

```lean
∀ {σ : Type u_1} {B : ℝ}, 1 ≤ B → ∀ (r : σ → ℕ), 1 ∈ Roth.RSet B r
```

- **What**: Constant integer polynomial1 belongs to the complete nonzero degree-bounded coefficient-bounded family if1≤B.
- **How**: Local classical simplification using MvPolynomial.coeff_one and MvPolynomial.degreeOf_one=0, nonzero1 and0≤1≤B. Independent full arithmetic, generic normed-ring and exact Int specialization proofs verified.
- **Hypotheses**: σ arbitrary universe-polymorphic type; B real; r:σ→ℕ;1≤B necessary and sufficient. No Fintype, DecidableEq, positive degree or nonempty variable hypotheses.
- **Uses from project (lexical body)**: `Roth.RSet`
- **Project references in type**: `Roth.RSet`
- **Native direct body references**: []
- **Native direct type references**: `Roth.RSet`
- **Used by in file (lexical)**: `Roth.indexSet_nonempty`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 73–75; proof/body length 3 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.one_mem_RSet.md).

#### theorem Roth.indexSet_nonempty

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ},   1 ≤ B → ∀ (q r : σ → ℕ), (Roth.indexSet B q r).Nonempty
```

- **What**: For B≥1 the bounded integer polynomial index family is nonempty.
- **How**: Use polynomial1, whose degrees vanish and coefficients are bounded, and numerators constantly1, coprime to arbitrary q.
- **Hypotheses**: σ arbitrary universe; Fintype required by unchanged index parent; B:ℝ;1≤B; q r:σ→ℕ arbitrary including zeros; no DecidableEq
- **Uses from project (lexical body)**: `Roth.one_mem_RSet`
- **Project references in type**: `Roth.indexSet`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.one_mem_RSet`
- **Native direct type references**: `Roth.indexSet`
- **Used by in file (lexical)**: `Roth.Θ_le_of_forall_index_le`, `Roth.Θ_mono`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 80–81; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.indexSet_nonempty.md).

#### theorem Roth.indexSet_bddAbove

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (B : ℝ) (q : σ → ℕ) {r : σ → ℕ},
  BddAbove (Roth.indexSet B q r)
```

- **What**: The real index family of degree/coefficient-bounded nonzero integer polynomials at coprime rational numerator choices is bounded above by cardσ.
- **How**: Choose cardσ, unpack family witnesses, transfer nonzero and degrees through integer-real coefficient map, apply project index_le_card. Generic image2 packaging independently verified.
- **Hypotheses**: Arbitrary universe σ with Fintype; arbitrary real B; natural vectors q,r. No positivity, 1≤B, DecidableEq or nonempty-family premise.
- **Uses from project (lexical body)**: `Roth.index_le_card`
- **Project references in type**: `Roth.indexSet`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.index_le_card`
- **Native direct type references**: `Roth.indexSet`
- **Used by in file (lexical)**: `Roth.index_le_Θ`, `Roth.Θ_mono`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 87–93; proof/body length 7 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.indexSet_bddAbove.md).

#### theorem Roth.index_le_Θ

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} {q r : σ → ℕ} {R : MvPolynomial σ ℤ},
  R ∈ Roth.RSet B r →
    ∀ {h : σ → ℤ},
      (∀ (j : σ), IsCoprime (h j) ↑(q j)) →
        Roth.index ((map (Int.castRingHom ℝ)) R) (fun (j : σ) ↦ ↑(h j) / ↑(q j)) r ≤ Roth.Θ B q r
```

- **What**: Every admissible polynomial index at a coprime rational point is at most Θ.
- **How**: Apply le_csSup with project indexSet_bddAbove and the explicit polynomial/numerator membership witness.
- **Hypotheses**: Fintype σ; R∈RSet B r; each h j coprime to q j. No DecidableEq, positivity of q or r, or 1≤B.
- **Uses from project (lexical body)**: `Roth.indexSet_bddAbove`
- **Project references in type**: `Roth.RSet`, `Roth.index`, `Roth.Θ`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.indexSet_bddAbove`
- **Native direct type references**: `Roth.RSet`, `Roth.index`, `Roth.Θ`
- **Used by in file (lexical)**: `Roth.index_separated_mul_le_aux`
- **Used by other files (lexical)**: `Roth.main_lemma`
- **Visibility**: public
- **Lines**: 99–102; proof/body length 1 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_le_Θ.md).

#### theorem Roth.Θ_nonneg

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ}, 0 ≤ Roth.Θ B q r
```

- **What**: The polynomial-index supremum Θ is nonnegative for every coefficient bound, denominator and natural weight vector.
- **How**: Real.sSup_nonneg applied to pointwise nonnegative index values; independent verification expands real support infimum, finite sums and natural ratios.
- **Hypotheses**: σ : Type u; Fintype σ; B : ℝ arbitrary; q r : σ → ℕ arbitrary; no additional proof premises
- **Uses from project (lexical body)**: `Roth.index_nonneg`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.index_nonneg`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.index_le_lem6`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 107–110; proof/body length 4 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_nonneg.md).

#### theorem Roth.Θ_le_card

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ},
  Roth.Θ B q r ≤ ↑(Fintype.card σ)
```

- **What**: The supremum of all admissible polynomial indices is bounded by the number of variables, for every real coefficient bound and all natural denominator/weight vectors.
- **How**: Apply Real.sSup_le with nonnegative cardinality; destruct each admissible index, transport nonzero and coordinate degrees through the injective integer-to-real coefficient map, then apply project index_le_card.
- **Hypotheses**: Fintype σ; arbitrary B:ℝ and q,r:σ→ℕ. No DecidableEq, nonempty σ, B≥1, q>0 or r>0 assumptions. Hidden degree bounds matter; nonzero can be dropped only for a separately enlarged family under real-default0 index convention.
- **Uses from project (lexical body)**: `Roth.index_le_card`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.index_le_card`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_lt_of_large_delta_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 114–119; proof/body length 6 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_card.md).

#### theorem Roth.Θ_le_of_forall_index_le

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ},
  1 ≤ B →
    ∀ {q r : σ → ℕ} {c : ℝ},
      (∀ R ∈ Roth.RSet B r,
          ∀ (h : σ → ℤ),
            (∀ (j : σ), IsCoprime (h j) ↑(q j)) →
              Roth.index ((map (Int.castRingHom ℝ)) R) (fun (j : σ) ↦ ↑(h j) / ↑(q j)) r ≤ c) →
        Roth.Θ B q r ≤ c
```

- **What**: A supplied common upper bound on all admissible polynomial indices bounds their supremum Θ.
- **How**: Apply csSup_le to the nonempty family from hB; destruct existential indexSet witnesses and apply hc.
- **Hypotheses**: Universe-polymorphic σ with Fintype; B real with 1≤B; arbitrary natural q,r; arbitrary real c; hc is the full pointwise upper bound. No DecidableEq, positive r, or positive q required.
- **Uses from project (lexical body)**: `Roth.indexSet_nonempty`
- **Project references in type**: `Roth.RSet`, `Roth.index`, `Roth.Θ`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.indexSet_nonempty`
- **Native direct type references**: `Roth.RSet`, `Roth.index`, `Roth.Θ`
- **Used by in file (lexical)**: `Roth.Θ_unique_le`, `Roth.Θ_option_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 124–129; proof/body length 4 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_of_forall_index_le.md).

#### theorem Roth.Θ_mono

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B B' : ℝ},
  1 ≤ B → B ≤ B' → ∀ (q : σ → ℕ) {r : σ → ℕ}, Roth.Θ B q r ≤ Roth.Θ B' q r
```

- **What**: The supremum of polynomial indices is monotone in the coefficient bound B.
- **How**: Apply csSup_le_csSup to the larger bounded family and smaller nonempty family; reuse the same polynomial/numerator witnesses and enlarge their coefficient bound by transitivity.
- **Hypotheses**: σ : Type*; [Fintype σ]; B B′ : ℝ; hB : 1 ≤ B; hBB′ : B ≤ B′; q r : σ → ℕ; no positivity assumptions; No DecidableEq instance in elaborated type
- **Uses from project (lexical body)**: `Roth.indexSet_bddAbove`, `Roth.indexSet_nonempty`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.indexSet_bddAbove`, `Roth.indexSet_nonempty`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_scaled_unique_le_aux`, `Roth.theta_prefix_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 134–138; proof/body length 4 lines.
- **Notes**:
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_mono.md).

#### lemma Roth.indexSet_comp_subset

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {τ : Type u_2}
  [inst_1 : Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ), Roth.indexSet B (q ∘ ⇑e) (r ∘ ⇑e) ⊆ Roth.indexSet B q r
```

- **What**: Renaming variables along an equivalence carries every admissible polynomial index into the corresponding family with the renamed denominator and weight vectors.
- **How**: Rename polynomial and numerator witnesses, preserve coefficients through coeff_rename_mapDomain, and use index_rename to preserve index.
- **Hypotheses**: Finite variable types and a bijection between them. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.index_rename`
- **Project references in type**: `Roth.indexSet`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.indexSet`, `Roth.index_rename`
- **Native direct type references**: `Roth.indexSet`
- **Used by in file (lexical)**: `Roth.Θ_equiv`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 141–154; proof/body length 13 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.indexSet_comp_subset.md).

#### theorem Roth.Θ_equiv

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {τ : Type u_2} [inst_1 : Fintype τ] (e : σ ≃ τ) (B : ℝ)
  (q r : τ → ℕ), Roth.Θ B (q ∘ ⇑e) (r ∘ ⇑e) = Roth.Θ B q r
```

- **What**: The supremum of bounded integral polynomial indices at reduced rational points is invariant under bijective variable renaming.
- **How**: Rename each polynomial, transport its nonzero/degree/coefficient bounds and coprime numerator vector, use index_rename, repeat with inverse equivalence, then congrArg sSup.
- **Hypotheses**: Arbitrary universe-polymorphic finite variable types, an equivalence e, B real, q/r natural vectors; no DecidableEq or positivity premise.
- **Uses from project (lexical body)**: `Roth.indexSet_comp_subset`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.indexSet`, `Roth.indexSet_comp_subset`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_lt_succ_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 159–163; proof/body length 4 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_equiv.md).

#### lemma Roth.isPrimitive_linear

Type:

```lean
∀ {h : ℤ} {q : ℕ},
  IsCoprime h ↑q → (Polynomial.C ↑q * Polynomial.X - Polynomial.C h).IsPrimitive
```

- **What**: If an integer numerator h and natural denominator q are coprime, the polynomial qX-h is primitive over the integers.
- **How**: Any common coefficient divisor divides the constant and linear coefficient, so coprimality makes it a unit.
- **Hypotheses**: Coprime integer numerator and natural denominator. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_eq_pow_mul_of_rootMultiplicity`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 167–173; proof/body length 6 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.isPrimitive_linear.md).

#### lemma Roth.isPrimitive_pow

Type:

```lean
∀ {p : Polynomial ℤ}, p.IsPrimitive → ∀ (t : ℕ), (p ^ t).IsPrimitive
```

- **What**: Every natural power of a primitive integer polynomial is primitive.
- **How**: Induct on the exponent using Polynomial.isPrimitive_one and primitive-product closure.
- **Hypotheses**: Primitive integer polynomial. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.exists_eq_pow_mul_of_rootMultiplicity`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 175–177; proof/body length 1 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.isPrimitive_pow.md).

#### theorem Roth.exists_eq_pow_mul_of_rootMultiplicity

Type:

```lean
∀ {R : Polynomial ℤ} {h : ℤ} {q : ℕ},
  0 < q →
    IsCoprime h ↑q →
      ∃ (Q : Polynomial ℤ),
        R =
          (Polynomial.C ↑q * Polynomial.X - Polynomial.C h) ^
              Polynomial.rootMultiplicity (↑h / ↑q) (Polynomial.map (Int.castRingHom ℚ) R) *
            Q
```

- **What**: An integer polynomial is divisible over the integers by the reduced linear root factor to its rational root multiplicity.
- **How**: Prove linear-factor-power primitive, normalize its rational image to a nonzero scalar times the monic root factor, then combine Gauss divisibility descent with pow_rootMultiplicity_dvd.
- **Hypotheses**: R : Polynomial ℤ (zero allowed), h : ℤ, q : ℕ, 0 < q and IsCoprime h ↑q. Native type has no ambient finiteness instances and no nonzero-polynomial premise.
- **Uses from project (lexical body)**: `Roth.isPrimitive_linear`, `Roth.isPrimitive_pow`
- **Project references in type**: []
- **Native direct body references**: `Roth.isPrimitive_linear`, `Roth.isPrimitive_pow`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.pow_rootMultiplicity_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 184–199; proof/body length 13 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_eq_pow_mul_of_rootMultiplicity.md).

#### theorem Roth.pow_rootMultiplicity_le

Type:

```lean
∀ {R : Polynomial ℤ},
  R ≠ 0 →
    ∀ {h : ℤ} {q : ℕ},
      0 < q →
        IsCoprime h ↑q →
          ∀ {B : ℝ},
            |↑R.leadingCoeff| ≤ B →
              ↑q ^ Polynomial.rootMultiplicity (↑h / ↑q) (Polynomial.map (Int.castRingHom ℚ) R) ≤ B
```

- **What**: Reduced rational-root denominator to its multiplicity is bounded by absolute integer polynomial leading coefficient, hence by B.
- **How**: Apply exists_eq_pow_mul_of_rootMultiplicity, then Polynomial.leadingCoeff_mul and Polynomial.leadingCoeff_pow; Int.one_le_abs bounds the nonzero residual integer leading coefficient and yields the numerical denominator-power bound.
- **Hypotheses**: R≠0; q>0 (removable numerically); IsCoprime h ↑q (IsRelPrime equivalent over ℤ); absolute leading coefficient≤B
- **Uses from project (lexical body)**: `Roth.exists_eq_pow_mul_of_rootMultiplicity`
- **Project references in type**: []
- **Native direct body references**: `Roth.exists_eq_pow_mul_of_rootMultiplicity`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.index_unique_le_log_div`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 206–220; proof/body length 13 lines.
- **Notes**:
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.pow_rootMultiplicity_le.md).

#### lemma Roth.index_unique_le_log_div

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : Unique σ] {B : ℝ}
  {q r : σ → ℕ},
  1 < q default →
    ∀ {R : MvPolynomial σ ℤ},
      R ≠ 0 →
        |↑((uniqueAlgEquiv ℤ σ) R).leadingCoeff| ≤ B →
          ∀ {h : σ → ℤ},
            IsCoprime (h default) ↑(q default) →
              Roth.index ((map (Int.castRingHom ℝ)) R) (fun j ↦ ↑(h j) / ↑(q j)) r ≤
                Real.log B / (↑(r default) * Real.log ↑(q default))
```

- **What**: For a nonzero one-variable integer polynomial and a reduced rational evaluation point with denominator greater than one, its weighted index is at most log B divided by the weighted logarithm of that denominator, provided its absolute leading coefficient is bounded by B.
- **How**: Use index_unique, transport root multiplicities between rational and real maps, apply pow_rootMultiplicity_le, and take logarithms.
- **Hypotheses**: Singleton finite variable type; denominator greater than one; nonzero polynomial with bounded leading coefficient and coprime numerator. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.index_unique`, `Roth.pow_rootMultiplicity_le`
- **Project references in type**: `Roth.index`
- **Native direct body references**: `Roth.index`, `Roth.index_unique`, `Roth.pow_rootMultiplicity_le`
- **Native direct type references**: `Roth.index`
- **Used by in file (lexical)**: `Roth.Θ_unique_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 223–250; proof/body length 24 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_unique_le_log_div.md).

#### theorem Roth.Θ_unique_le

Type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : Unique σ] {B : ℝ},
  1 ≤ B →
    ∀ {q : σ → ℕ}, 1 < q default → ∀ {r : σ → ℕ}, Roth.Θ B q r ≤ Real.log B / (↑(r default) * Real.log ↑(q default))
```

- **What**: The extremal one-variable weighted index of bounded integer polynomials at reduced rational points of denominator q>1 is at most log B/(r log q).
- **How**: Use Θ_le_of_forall_index_le with index_unique_le_log_div: primitive rational-root factorization gives q^t≤|lc R|≤B, logarithm monotonicity gives t/r≤log B/(r log q), and csSup_le bounds the supremum.
- **Hypotheses**: A singleton variable type, B≥1, natural denominator q>1, natural weight r (zero allowed); the family quantifies nonzero degree/coefficient-bounded integer polynomials and reduced numerators.
- **Uses from project (lexical body)**: `Roth.index_unique_le_log_div`, `Roth.Θ_le_of_forall_index_le`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.RSet`, `Roth.index_unique_le_log_div`, `Roth.Θ_le_of_forall_index_le`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_scaled_unique_le_aux`, `Roth.theta_lt_base_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 256–260; proof/body length 3 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_unique_le.md).

#### theorem Roth.one_le_lem6M

Type:

```lean
∀ (p r₁ : ℕ) {B : ℝ}, 1 ≤ B → ∀ (l : ℕ), 1 ≤ Roth.lem6M p r₁ B l
```

- **What**: The explicit Lemma6 coefficient envelope M is at least one whenever B is at least one, including zero values of p,r₁,l.
- **How**: Unfold lem6M; lower-bound all four factors by one using natural-cast nonnegativity, power monotonicity and factorial positivity; combine with three multiplication lower bounds.
- **Hypotheses**: p,r₁,l natural, B real, hB:1≤B. No variable-type, Fintype or DecidableEq parameters survive elaboration.
- **Uses from project (lexical body)**: `Roth.lem6M`
- **Project references in type**: `Roth.lem6M`
- **Native direct body references**: `Roth.lem6M`
- **Native direct type references**: `Roth.lem6M`
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 279–285; proof/body length 7 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.one_le_lem6M.md).

#### theorem Roth.floor_sq_div_two_le_sum

Type:

```lean
∀ {a : ℝ}, 0 ≤ a → ↑⌊a⌋₊ ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ↑ν)
```

- **What**: A nonnegative real a has triangular tail sum ∑ν≤floor(a)(a−ν) at least floor(a)²/2.
- **How**: Cast the natural Gauss sum identity into ℝ, distribute the finite sum, and use floor(a)≤a in nonlinear arithmetic.
- **Hypotheses**: a : ℝ; ha : 0 ≤ a; necessary at negative a under natural-floor convention
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 289–296; proof/body length 7 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.floor_sq_div_two_le_sum.md).

#### theorem Roth.sq_div_three_lt_floor_sq_div_two

Type:

```lean
∀ {a : ℝ}, 10 < a → a ^ 2 / 3 < ↑⌊a⌋₊ ^ 2 / 2
```

- **What**: For real a>10, a²/3 is strictly smaller than natural floor(a)²/2.
- **How**: Nonlinear arithmetic from Nat.lt_floor_add_one and natural-floor nonnegativity.
- **Hypotheses**: a:ℝ; ha:10<a; verified sufficient weakening5≤a;4≤a fails at99/20
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 300–302; proof/body length 2 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sq_div_three_lt_floor_sq_div_two.md).

#### lemma Roth.mul_div_two_le_sum_max_aux

Type:

```lean
∀ {θ r : ℝ} {l : ℕ},
  ↑l ≤ θ * r → ↑l * θ / 2 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / r)
```

- **What**: If the natural truncation length l is at most θr, the sum of positive parts max(0,θ−ν/r) over ν<l is at least lθ/2.
- **How**: Treat empty and nonpositive-height cases, then use Finset.sum_range_id_mul_two and bound each positive part below by its residual.
- **Hypotheses**: Truncation length at most height times scale. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.mul_sq_div_three_le_sum_max_aux`, `Roth.min_le_sum_max`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 304–320; proof/body length 16 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.mul_div_two_le_sum_max_aux.md).

#### lemma Roth.mul_sq_div_three_le_sum_max_of_pos_aux

Type:

```lean
∀ {θ r : ℝ},
  0 < r → 0 ≤ θ → ∀ {l : ℕ}, θ * r < ↑l → r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / r)
```

- **What**: For positive real scale r, nonnegative height θ and natural length l strictly greater than θr, the sum of max(0,θ−ν/r) over ν<l is at least rθ²/3.
- **How**: Truncate at the natural floor, evaluate the arithmetic progression via Finset.sum_range_id_mul_two, divide by scale, and enlarge the nonnegative sum.
- **Hypotheses**: Positive real scale, nonnegative height, truncation longer than height times scale. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.mul_sq_div_three_le_sum_max_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 322–345; proof/body length 23 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.mul_sq_div_three_le_sum_max_of_pos_aux.md).

#### lemma Roth.mul_sq_div_three_le_sum_max_aux

Type:

```lean
∀ {θ r : ℝ},
  0 ≤ θ → ∀ {l : ℕ}, θ * r ≤ ↑l → r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / r)
```

- **What**: For nonnegative real height θ and a natural truncation length l at least θr, the positive-part residual sum is at least rθ²/3, including nonpositive scales and the boundary θr=l.
- **How**: Combine mul_sq_div_three_le_sum_max_of_pos_aux with nonpositivity and the boundary case from mul_div_two_le_sum_max_aux.
- **Hypotheses**: Nonnegative height; height times scale no larger than truncation length. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.mul_div_two_le_sum_max_aux`, `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.mul_div_two_le_sum_max_aux`, `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.min_le_sum_max`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 347–355; proof/body length 8 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.mul_sq_div_three_le_sum_max_aux.md).

#### theorem Roth.min_le_sum_max

Type:

```lean
∀ {θ : ℝ} {rp : ℕ} (l : ℕ),
  min (↑l * θ / 2) (↑rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / ↑rp)
```

- **What**: For every real theta and natural scale rp,length l, the positive-part arithmetic-progression sum bounds min(l*theta/2,rp*theta²/3). No source positivity/size premises remain.
- **How**: If theta≤0 use nonnegative sum; otherwise split at l≤theta*rp and combine the linear and quadratic private branch estimates with min_le_left/right. Branch proofs use Gauss summation, cutoff and nonnegative remainders.
- **Hypotheses**: theta:real;rp,l:natural; No positivity or size hypotheses; ambient finite-type/decidable-equality parameters absent from native type.
- **Uses from project (lexical body)**: `Roth.mul_div_two_le_sum_max_aux`, `Roth.mul_sq_div_three_le_sum_max_aux`
- **Project references in type**: []
- **Native direct body references**: `Roth.mul_div_two_le_sum_max_aux`, `Roth.mul_sq_div_three_le_sum_max_aux`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.index_le_lem6`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 362–370; proof/body length 8 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.min_le_sum_max.md).

#### theorem Roth.sum_max_sub_le_index_det

Type:

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → τ →₀ ℕ),
  (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) →
    (Matrix.of fun (μ ν : Fin l) ↦ (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det ≠ 0 →
      ∀ (α : Option τ → ℝ) {r : Option τ → ℕ},
        (∀ (j : Option τ), 0 < r j) →
          ∀ {δ : ℝ},
            (∀ (d : τ →₀ ℕ), Finsupp.degree d ≤ l - 1 → Roth.weight (r ∘ some) d ≤ δ) →
              ∑ ν ∈ Finset.range l, max 0 (Roth.index R α r - ↑ν / ↑(r none)) - ↑l * δ ≤
                Roth.index
                  (Matrix.of fun (μ ν : Fin l) ↦
                      (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det
                  α r
```

- **What**: Bounds the index of a nonzero mixed Hasse derivative determinant below by the positive-part column sum minus lδ.
- **How**: Use index_sub_weight_le_index_hasseDeriv and index_nonneg to bound each nonzero entry by its positive-part column contribution minus δ. Expand with Matrix.det_apply'; index_C_mul removes each permutation sign, index_prod adds the indices of its nonzero entries, and le_index_sum transports their common lower bound to the nonzero determinant.
- **Hypotheses**: Fintype τ; real coefficient/point/index interface; degree(Dμ)≤μ; nonzero determinant; positive natural denominator weights; uniform weight≤δ for every degree≤l−1 multi-index. No l>0 or separate δ≥0 premise.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.index_C_mul`, `Roth.index_nonneg`, `Roth.index_prod`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.le_index_sum`, `Roth.weight_add`, `Roth.weight_mapDomain`, `Roth.weight_nonneg`, `Roth.weight_single`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.index_C_mul`, `Roth.index_nonneg`, `Roth.index_prod`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.le_index_sum`, `Roth.weight`, `Roth.weight_add`, `Roth.weight_mapDomain`, `Roth.weight_nonneg`, `Roth.weight_single`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.weight`
- **Used by in file (lexical)**: `Roth.index_le_lem6`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 376–411; proof/body length 29 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_max_sub_le_index_det.md).

#### lemma Roth.index_separated_mul_le_aux

Type:

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {r : Option τ → ℕ},
  (∀ (j : Option τ), 0 < r j) →
    ∀ {q : Option τ → ℕ} {h : Option τ → ℤ},
      (∀ (j : Option τ), IsCoprime (h j) ↑(q j)) →
        ∀ {M : ℝ} {l : ℕ},
          0 < l →
            ∀ {U : MvPolynomial τ ℤ},
              (U ∈ Roth.RSet M fun j ↦ l * r (some j)) →
                ∀ {V : Polynomial ℤ},
                  V ≠ 0 →
                    V.natDegree ≤ l * r none →
                      (∀ (b : ℕ), |↑(V.coeff b)| ≤ M) →
                        Roth.index ((map (Int.castRingHom ℝ)) ((rename some) U * (Polynomial.aeval (X none)) V))
                            (fun j ↦ ↑(h j) / ↑(q j)) r ≤
                          ↑l * Roth.lem6Φ q r M l
```

- **What**: A separated integer polynomial product with bounded scaled degrees and coefficients has point index at most l times the sum of its distinguished-variable and complementary extremal indices.
- **How**: Convert the univariate factor through uniqueAlgEquiv, use index_mul and index_rename, then index_le_Θ and index_mul_left_weights for both factors.
- **Hypotheses**: Positive degree weights and scale; coprime point; nonzero separated factors with scaled degree and coefficient bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.RSet`, `Roth.aeval_X_eq_rename`, `Roth.degreeOf_uniqueAlgEquiv_symm`, `Roth.index_le_Θ`, `Roth.index_mul`, `Roth.index_mul_left_weights`, `Roth.index_rename`, `Roth.lem6Φ`
- **Project references in type**: `Roth.RSet`, `Roth.index`, `Roth.lem6Φ`
- **Native direct body references**: `Roth.RSet`, `Roth.aeval_X_eq_rename`, `Roth.degreeOf_uniqueAlgEquiv_symm`, `Roth.index`, `Roth.index_le_Θ`, `Roth.index_mul`, `Roth.index_mul_left_weights`, `Roth.index_rename`, `Roth.lem6Φ`, `Roth.Θ`
- **Native direct type references**: `Roth.RSet`, `Roth.index`, `Roth.lem6Φ`
- **Used by in file (lexical)**: `Roth.index_det_le`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 414–450; proof/body length 31 lines.
- **Notes**: proof/body >30 lines
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_separated_mul_le_aux.md).

#### theorem Roth.index_det_le

Type:

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {r : Option τ → ℕ},
  (∀ (j : Option τ), 0 < r j) →
    ∀ {r₁ : ℕ},
      (∀ (j : Option τ), r j ≤ r₁) →
        ∀ {q : Option τ → ℕ} {B : ℝ} {R : MvPolynomial (Option τ) ℤ},
          R ∈ Roth.RSet B r →
            ∀ {h : Option τ → ℤ},
              (∀ (j : Option τ), IsCoprime (h j) ↑(q j)) →
                ∀ {l : ℕ},
                  1 ≤ l →
                    ∀ {D : Fin l → τ →₀ ℕ} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ},
                      U ≠ 0 →
                        V ≠ 0 →
                          (∀ (j : τ), degreeOf j U ≤ l * r (some j)) →
                            V.natDegree ≤ l * r none →
                              (Matrix.of fun μ ν ↦
                                      (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det =
                                  (rename some) U * (Polynomial.aeval (X none)) V →
                                Roth.index
                                    ((map (Int.castRingHom ℝ))
                                      (Matrix.of fun μ ν ↦
                                          (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det)
                                    (fun j ↦ ↑(h j) / ↑(q j)) r ≤
                                  ↑l * Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l
```

- **What**: The real weighted index of an integer mixed-Hasse determinant with a separated factorization is at most l times its two extremal indices at the Lemma6 coefficient envelope.
- **How**: First abs_coeff_det_hasseDeriv_le bounds every determinant coefficient by lem6M. Then coeff_rename_mul_aeval identifies a separated coefficient as one product; Polynomial.leadingCoeff_ne_zero and Int.one_le_abs, together with MvPolynomial.ne_zero_iff, bound both integer factors. Finally index_separated_mul_le_aux uses index_mul, index_rename, index_le_Θ and index_mul_left_weights to obtain l times lem6Φ.
- **Hypotheses**: Finite variable family; positive natural index weights and uniform degree ceiling; RSet input; coprime rational point; positive l; nonzero integer factors, their scaled degree bounds and exact determinant factorization. Verified alternative interfaces remove several redundant hypotheses.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_det_hasseDeriv_le`, `Roth.coeff_rename_mul_aeval`, `Roth.index_separated_mul_le_aux`, `Roth.lem6M`
- **Project references in type**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.index`, `Roth.lem6M`, `Roth.lem6Φ`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.abs_coeff_det_hasseDeriv_le`, `Roth.coeff_rename_mul_aeval`, `Roth.index`, `Roth.index_separated_mul_le_aux`, `Roth.lem6M`, `Roth.lem6Φ`
- **Native direct type references**: `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.index`, `Roth.lem6M`, `Roth.lem6Φ`
- **Used by in file (lexical)**: `Roth.index_le_lem6`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 457–491; proof/body length 25 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_det_le.md).

#### lemma Roth.weight_le_delta_aux

Type:

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {δ : ℝ},
  0 ≤ δ →
    ∀ {r : Option τ → ℕ},
      (∀ (j : τ), ↑(r none) ≤ δ * ↑(r (some j))) →
        ∀ {d : τ →₀ ℕ}, Finsupp.degree d ≤ r none → Roth.weight (r ∘ some) d ≤ δ
```

- **What**: An exponent vector of total degree at most the distinguished natural weight has complementary reciprocal-weight sum at most δ when each complementary weight dominates the distinguished one by the given δ ratio.
- **How**: Split the zero distinguished-weight case using Finsupp.degree_eq_zero_iff. Otherwise use div_le_div_iff₀ for coordinate comparisons, Finset.sum_le_sum and Finsupp.degree_eq_sum to obtain weight ≤ δ times degree divided by the distinguished weight, then apply the degree bound.
- **Hypotheses**: Nonnegative delta and distinguished weight at most delta times every other weight; derivative order at most distinguished weight. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.weight`
- **Project references in type**: `Roth.weight`
- **Native direct body references**: `Roth.weight`
- **Native direct type references**: `Roth.weight`
- **Used by in file (lexical)**: `Roth.index_le_lem6`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 494–508; proof/body length 13 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_le_delta_aux.md).

#### lemma Roth.mapped_det_ne_zero_aux

Type:

```lean
∀ {τ : Type u_2} {R : MvPolynomial (Option τ) ℤ} {l : ℕ}
  {D : Fin l → τ →₀ ℕ} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ},
  U ≠ 0 →
    V ≠ 0 →
      (Matrix.of fun μ ν ↦ (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det =
          (rename some) U * (Polynomial.aeval (X none)) V →
        (Matrix.of fun μ ν ↦
              (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) ((map (Int.castRingHom ℝ)) R)).det ≠
          0
```

- **What**: A Hasse-derivative determinant over the reals is nonzero when its integer precursor factors into nonzero complementary-variable and distinguished-variable integer factors.
- **How**: Use RingHom.map_det and hasseDeriv_map to identify the mapped integer determinant with the real determinant. Apply map_injective, rename_injective, aeval_X_eq_rename and uniqueAlgEquiv injectivity to transport the nonzero separated factors through coefficient maps and variable embeddings.
- **Hypotheses**: Nonzero separated integer factors and a factorization identity. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.aeval_X_eq_rename`
- **Project references in type**: `MvPolynomial.hasseDeriv`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.aeval_X_eq_rename`
- **Native direct type references**: `MvPolynomial.hasseDeriv`
- **Used by in file (lexical)**: `Roth.index_le_lem6`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 511–529; proof/body length 13 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.mapped_det_ne_zero_aux.md).

#### lemma Roth.index_numeric_bound_aux

Type:

```lean
∀ {θ Φ δ rp l : ℝ},
  0 ≤ Φ →
    δ ≤ 1 → 3 ≤ rp → 0 < l → l ≤ rp + 1 → min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ l * (Φ + δ) → θ ≤ 2 * (Φ + √Φ + √δ)
```

- **What**: A real index parameter satisfying the minimum of a linear and quadratic lower estimate against l(Φ+δ) is at most 2(Φ+sqrt Φ+sqrt δ) when Φ is nonnegative, δ≤1, the scale is at least three, and 0<l≤scale+1.
- **How**: Split min_le_iff. Divide the linear branch by positive l and use Real.le_sqrt_self_iff. In the quadratic branch derive 3*l ≤ 4*rp and θ² ≤ 4*(Φ+δ), then combine Real.sq_sqrt, Real.sq_sqrt' and le_of_sq_le_sq with nonnegative square roots; finally add the nonnegative Φ term.
- **Hypotheses**: Nonnegative Phi, delta at most one, scale at least three and positive length at most scale plus one. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.index_le_lem6`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 531–549; proof/body length 17 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_numeric_bound_aux.md).

#### theorem Roth.index_le_lem6

Type:

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {δ : ℝ},
  0 ≤ δ →
    δ ≤ 1 →
      ∀ {r : Option τ → ℕ},
        3 ≤ ↑(r none) →
          (∀ (j : τ), ↑(r none) ≤ δ * ↑(r (some j))) →
            ∀ {r₁ : ℕ},
              (∀ (j : Option τ), r j ≤ r₁) →
                ∀ {q : Option τ → ℕ},
                  (∀ (j : Option τ), 0 < q j) →
                    ∀ {B : ℝ} {R : MvPolynomial (Option τ) ℤ},
                      R ∈ Roth.RSet B r →
                        ∀ {h : Option τ → ℤ},
                          (∀ (j : Option τ), IsCoprime (h j) ↑(q j)) →
                            ∃ l,
                              1 ≤ l ∧
                                l ≤ r none + 1 ∧
                                  Roth.index ((map (Int.castRingHom ℝ)) R) (fun j ↦ ↑(h j) / ↑(q j)) r ≤
                                    2 *
                                      (Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l +
                                          √(Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l) +
                                        √δ)
```

- **What**: For each bounded-height integer polynomial at a coprime rational tuple, some determinant rank1≤l≤r_p+1 gives its weighted index at most2(Φ_l+√Φ_l+√δ).
- **How**: Choose the separated determinant using exists_det_eq_mul. The mapped_det_ne_zero_aux and weight_le_delta_aux helpers feed sum_max_sub_le_index_det, while index_det_le provides its upper index bound. Combine these with min_le_sum_max, Θ_nonneg and index_numeric_bound_aux to obtain the square-root bound.
- **Hypotheses**: Finite complementary variable family;0≤δ≤1;distinguished natural weight≥3 and coordinate ratios;uniform degree ceiling;RSet integer polynomial;coprime numerator tuple;positive denominators retained but unused. The endpoint is freshly verified without denominator positivity and with distinguished weight≥1 via a new stronger finite-sum ingredient.
- **Uses from project (lexical body)**: `MvPolynomial.hasseDeriv_map`, `Roth.exists_det_eq_mul`, `Roth.index`, `Roth.index_det_le`, `Roth.index_numeric_bound_aux`, `Roth.lem6M`, `Roth.lem6Φ`, `Roth.mapped_det_ne_zero_aux`, `Roth.min_le_sum_max`, `Roth.sum_max_sub_le_index_det`, `Roth.weight_le_delta_aux`, `Roth.Θ_nonneg`
- **Project references in type**: `Roth.RSet`, `Roth.index`, `Roth.lem6M`, `Roth.lem6Φ`
- **Native direct body references**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.RSet`, `Roth.exists_det_eq_mul`, `Roth.index`, `Roth.index_det_le`, `Roth.index_numeric_bound_aux`, `Roth.lem6M`, `Roth.lem6Φ`, `Roth.mapped_det_ne_zero_aux`, `Roth.min_le_sum_max`, `Roth.sum_max_sub_le_index_det`, `Roth.weight_le_delta_aux`, `Roth.Θ`, `Roth.Θ_nonneg`
- **Native direct type references**: `Roth.RSet`, `Roth.index`, `Roth.lem6M`, `Roth.lem6Φ`
- **Used by in file (lexical)**: `Roth.Θ_option_le`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 556–587; proof/body length 25 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_le_lem6.md).

#### theorem Roth.Θ_option_le

Type:

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {δ : ℝ},
  0 ≤ δ →
    δ ≤ 1 →
      ∀ {r : Option τ → ℕ},
        3 ≤ ↑(r none) →
          (∀ (j : τ), ↑(r none) ≤ δ * ↑(r (some j))) →
            ∀ {r₁ : ℕ},
              (∀ (j : Option τ), r j ≤ r₁) →
                ∀ {q : Option τ → ℕ},
                  (∀ (j : Option τ), 0 < q j) →
                    ∀ {B : ℝ},
                      1 ≤ B →
                        Roth.Θ B q r ≤
                          2 *
                            (Finset.Icc 1 (r none + 1)).sup' ⋯ fun l ↦
                              Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l +
                                  √(Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l) +
                                √δ
```

- **What**: Lemma6 bounds the supremum of integer-polynomial indices by twice a finite maximum of Φ(l)+√Φ(l)+√δ, reducing the distinguished-variable problem to one variable and the complementary variables.
- **How**: Use Θ_le_of_forall_index_le to pass to each polynomial and numerator tuple. The substantive project theorem index_le_lem6 supplies a rank l in the finite interval; Finset.le_sup' and mul_le_mul_of_nonneg_left then dominate its bound by twice the finite maximum.
- **Hypotheses**: Fintype τ;0≤δ≤1;distinguished natural weight≥3;coordinate degree ratios and uniform degree ceiling;positive natural denominators;B≥1. Fresh whole-module experiments remove denominator positivity and B≥1 and weaken distinguished weight to≥1, with new/project numerical ingredients explicitly retained.
- **Uses from project (lexical body)**: `Roth.index_le_lem6`, `Roth.lem6M`, `Roth.lem6Φ`, `Roth.Θ_le_of_forall_index_le`
- **Project references in type**: `Roth.lem6M`, `Roth.lem6Φ`, `Roth.Θ`
- **Native direct body references**: `Roth.RSet`, `Roth.index`, `Roth.index_le_lem6`, `Roth.lem6M`, `Roth.lem6Φ`, `Roth.Θ_le_of_forall_index_le`
- **Native direct type references**: `Roth.lem6M`, `Roth.lem6Φ`, `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_lt_succ_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 593–603; proof/body length 6 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_option_le.md).

#### lemma Roth.factorial_coefficient_le_two_pow_aux

Type:

```lean
∀ (p r₁ l : ℕ),
  l ≤ 2 ^ r₁ → (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤ 2 ^ ((2 * p + 1) * r₁ * l)
```

- **What**: The non-height factors of the Lemma 6 determinant envelope are bounded by one explicit power of two when l is at most 2 to the degree ceiling.
- **How**: Bound r+1 by two to r and l! by l to l using Nat.lt_two_pow_self and Nat.factorial_le_pow; combine power exponents.
- **Hypotheses**: Determinant size at most two to the maximum degree. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.lem6M_lt`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 609–619; proof/body length 10 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.factorial_coefficient_le_two_pow_aux.md).

#### lemma Roth.two_pow_lt_rpow_aux

Type:

```lean
∀ {p r₁ l : ℕ},
  0 < p →
    ∀ {δ q : ℝ},
      0 < δ →
        0 ≤ q →
          ↑p * (2 * ↑p + 1) / δ ≤ Real.log q → 0 < l * r₁ → 2 ^ ((2 * p + 1) * r₁ * l) < q ^ (δ / ↑p * (↑l * ↑r₁))
```

- **What**: A logarithmic lower bound on a nonnegative real q makes its positive real power strictly exceed the explicit power-of-two combinatorial envelope.
- **How**: Derive q>1 using Real.log_pos_iff, establish log 2<1 with Real.log_lt_sub_one_of_pos, and rearrange the logarithmic lower bound. Rewrite powers through Real.rpow_def_of_pos and use Real.exp_lt_exp after multiplying the exponent comparison by the positive l*r₁.
- **Hypotheses**: Positive dimension, delta and degree-size product; nonnegative base and the stated logarithmic lower bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.lem6M_lt`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 621–644; proof/body length 22 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.two_pow_lt_rpow_aux.md).

#### theorem Roth.lem6M_lt

Type:

```lean
∀ {p : ℕ},
  0 < p →
    ∀ {δ : ℝ},
      0 < δ →
        ∀ {r₁ q₁ : ℕ},
          ↑p * (2 * ↑p + 1) / δ ≤ Real.log ↑q₁ →
            ∀ {l : ℕ}, 1 ≤ l → l ≤ r₁ → Roth.lem6M p r₁ (↑q₁ ^ (δ * ↑r₁)) l < ↑q₁ ^ (δ * (1 + 1 / ↑p) * (↑l * ↑r₁))
```

- **What**: The determinant bound at an exponential coefficient bound is absorbed by a slightly larger denominator power.
- **How**: Bound the natural prefactor using factorial_coefficient_le_two_pow_aux, absorb its power of two with two_pow_lt_rpow_aux, then use Real.rpow_mul_natCast and Real.rpow_add to combine exponents.
- **Hypotheses**: p>0, delta>0, log q at least p(2p+1)/delta, and 1<=l<=r. No inherited typeclasses. Natural q and l<=r are analytically stronger than the compiled real-q/l<=2^r extension with r>0.
- **Uses from project (lexical body)**: `Roth.factorial_coefficient_le_two_pow_aux`, `Roth.lem6M`, `Roth.two_pow_lt_rpow_aux`
- **Project references in type**: `Roth.lem6M`
- **Native direct body references**: `Roth.factorial_coefficient_le_two_pow_aux`, `Roth.lem6M`, `Roth.two_pow_lt_rpow_aux`
- **Native direct type references**: `Roth.lem6M`
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 649–672; proof/body length 22 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.lem6M_lt.md).

#### theorem Roth.lem7_Φ_bound

Type:

```lean
∀ {p : ℕ},
  2 ≤ p →
    ∀ {δ : ℝ},
      0 < δ →
        δ ≤ 1 →
          δ * (1 + 1 / ↑p) + 10 ^ (p - 1) * (δ * (1 + 1 / ↑p)) ^ (1 / 2) ^ (p - 1) <
            3 * 10 ^ (p - 1) * δ ^ (1 / 2) ^ (p - 1)
```

- **What**: Absorb the perturbed delta and its dyadic power into 3 times the dimension-dependent power envelope.
- **How**: Use Real.mul_rpow and Real.rpow_le_rpow_of_exponent_ge/le to bound delta by delta^e and the perturbation by 3/2; use le_self_pow₀ to get 10<=10^(p-1), then linear_combination closes the strict gap.
- **Hypotheses**: p:Nat at least2, delta:Real positive and at most1. No inherited typeclasses. Successfully compiled delta<=2 broadening; delta0 and dimension1 fail, and p2/delta400 refutes removing all upper control.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 678–702; proof/body length 23 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.lem7_Φ_bound.md).

#### theorem Roth.lem7_numeric

Type:

```lean
∀ {p : ℕ},
  2 ≤ p →
    ∀ {δ : ℝ},
      0 < δ →
        δ ≤ 1 →
          ∀ {Φ : ℝ}, Φ ≤ 3 * 10 ^ (p - 1) * δ ^ (1 / 2) ^ (p - 1) → 2 * (Φ + √Φ + √δ) < 10 ^ p * δ ^ (1 / 2) ^ p
```

- **What**: A cap on Φ yields the next dyadic square-root estimate in Roth induction, even for negative Φ.
- **How**: Use Real.rpow_mul_natCast to identify the square of the next dyadic scale, Real.rpow_le_rpow_of_exponent_ge and Real.rpow_le_one to bound sqrt(delta) and the scale, then Real.sqrt_lt' bounds sqrt(Phi) before combining ordered inequalities.
- **Hypotheses**: p≥2,0<δ≤1 and Φ≤3·10^(p-1)δ^(2^(-(p-1))); no Φ nonnegativity, equality allowed in both upper bounds.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 709–740; proof/body length 30 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.lem7_numeric.md).

#### lemma Roth.theta_scaled_unique_le_aux

Type:

```lean
∀ {δ M : ℝ} {q₁ q₂ r₁ r₂ l : ℕ},
  1 < q₁ →
    0 < r₁ →
      0 < l →
        ↑r₁ * Real.log ↑q₁ ≤ ↑r₂ * Real.log ↑q₂ →
          1 ≤ M → M ≤ ↑q₁ ^ (δ * (↑l * ↑r₁)) → (Roth.Θ M (fun x ↦ q₂) fun x ↦ l * r₂) ≤ δ
```

- **What**: A one-variable extremal index at height M is at most δ after scaling its weight by l, when M lies below the first denominator power and weighted denominator logarithms are balanced.
- **How**: Increase the coefficient bound with Θ_mono, apply Θ_unique_le, and compare logarithms using the balanced degree-log product.
- **Hypotheses**: First denominator greater than one, positive first degree and scale, balanced degree-log products and coefficient bounds between one and the target power. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.Θ_mono`, `Roth.Θ_unique_le`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.Θ`, `Roth.Θ_mono`, `Roth.Θ_unique_le`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 742–765; proof/body length 22 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_scaled_unique_le_aux.md).

#### lemma Roth.theta_delta_succ_lt_aux

Type:

```lean
∀ (n : ℕ) {δ : ℝ},
  δ ≤ 1 / (↑n + 1 + 1) → δ * (1 + 1 / (↑n + 1 + 1)) < 1 / (↑n + 1)
```

- **What**: If δ≤1/(n+2), then δ(1+1/(n+2)) is strictly less than 1/(n+1).
- **How**: Multiply the reciprocal bounds and use one_div_mul_cancel plus a strict square inequality.
- **Hypotheses**: Delta bounded by the reciprocal of the successor dimension. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 767–774; proof/body length 7 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_delta_succ_lt_aux.md).

#### lemma Roth.theta_prefix_lt_aux

Type:

```lean
∀ {n : ℕ} {δ ε M : ℝ},
  0 < δ →
    δ ≤ ε →
      ∀ {r q : Fin (n + 2) → ℕ},
        (∀ (j : Fin (n + 2)), r (Fin.last (n + 1)) ≤ r j) →
          3 ≤ ↑(r (Fin.last (n + 1))) →
            (∀ (i : Fin (n + 1)), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
              (↑n + 1 + 1) * (2 * (↑n + 1 + 1) + 1) / δ ≤ Real.log ↑(q 0) →
                (∀ (j : Fin (n + 2)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                  ∀ {l : ℕ},
                    1 ≤ l →
                      1 ≤ M →
                        M ≤ ↑(q 0) ^ (ε * (↑l * ↑(r 0))) →
                          (∀ {r q : Fin (n + 1) → ℕ},
                              3 ≤ ↑(r (Fin.last n)) →
                                (∀ (i : Fin n), ↑(r i.succ) ≤ ε * ↑(r i.castSucc)) →
                                  (↑n + 1) * (2 * (↑n + 1) + 1) / ε ≤ Real.log ↑(q 0) →
                                    (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                                      Roth.Θ (↑(q 0) ^ (ε * ↑(r 0))) q r < 10 ^ (n + 1) * ε ^ (1 / 2) ^ (n + 1)) →
                            (Roth.Θ M (fun j ↦ q j.castSucc) fun j ↦ l * r j.castSucc) <
                              10 ^ (n + 1) * ε ^ (1 / 2) ^ (n + 1)
```

- **What**: The extremal index of the first n+1 coordinates with all weights scaled by l obeys the lower-dimensional induction bound when the height is at most the enlarged denominator power.
- **How**: Use Θ_mono to increase the coefficient bound, apply the supplied induction hypothesis to scaled degrees, and transfer degree ratios and balanced logarithms through Fin.castSucc.
- **Hypotheses**: Positive delta, epsilon at least delta, prefix induction hypothesis, lower last degree, degree ratios/logarithm bounds, positive scale and bounded coefficient parameter. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.Θ_mono`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.Θ`, `Roth.Θ_mono`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 776–816; proof/body length 28 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_prefix_lt_aux.md).

#### lemma Roth.theta_lt_base_aux

Type:

```lean
∀ {δ : ℝ},
  0 < δ →
    δ ≤ 1 → ∀ {r q : Fin 1 → ℕ}, 0 < r 0 → 1 < q 0 → Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ 1 * δ ^ (1 / 2) ^ 1
```

- **What**: In one variable, the extremal index at height q^(δr) is strictly less than 10 times δ to the one-half power, for positive δ≤1, positive weight and denominator greater than one.
- **How**: Apply Θ_unique_le, cancel the positive degree-log denominator, compare delta to its square root and multiply by ten.
- **Hypotheses**: Positive delta at most one, positive degree and denominator greater than one. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.Θ`, `Roth.Θ_unique_le`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.Θ`, `Roth.Θ_unique_le`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.Θ_lt`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 818–831; proof/body length 12 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_base_aux.md).

#### lemma Roth.theta_denominators_one_lt_aux

Type:

```lean
∀ {n : ℕ} {r q : Fin (n + 1) → ℕ},
  0 < r 0 →
    0 < Real.log ↑(q 0) →
      (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) → ∀ (j : Fin (n + 1)), 1 < q j
```

- **What**: If the first natural weight and first denominator logarithm are positive, balancing their product below every other weighted logarithm forces every natural denominator to exceed one.
- **How**: Transfer positivity from the first coordinate through the balancing inequality and use Real.log_pos_iff.
- **Hypotheses**: Positive first degree and first denominator logarithm; balanced degree-log products. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.theta_phi_lt_aux`, `Roth.theta_lt_succ_aux`, `Roth.Θ_lt`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 833–838; proof/body length 4 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_denominators_one_lt_aux.md).

#### lemma Roth.theta_phi_lt_aux

Type:

```lean
∀ {n : ℕ} {δ : ℝ},
  0 < δ →
    δ ≤ 1 / (↑n + 1 + 1) →
      δ < 1 →
        ∀ {r q : Fin (n + 2) → ℕ},
          Antitone r →
            3 ≤ ↑(r (Fin.last (n + 1))) →
              (∀ (i : Fin (n + 1)), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
                (↑n + 1 + 1) * (2 * (↑n + 1 + 1) + 1) / δ ≤ Real.log ↑(q 0) →
                  (∀ (j : Fin (n + 2)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                    (∀ {δ : ℝ},
                        0 < δ →
                          δ ≤ 1 / (↑n + 1) →
                            ∀ {r q : Fin (n + 1) → ℕ},
                              3 ≤ ↑(r (Fin.last n)) →
                                (∀ (i : Fin n), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
                                  (↑n + 1) * (2 * (↑n + 1) + 1) / δ ≤ Real.log ↑(q 0) →
                                    (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                                      Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ (n + 1) * δ ^ (1 / 2) ^ (n + 1)) →
                      ∀ {l : ℕ},
                        l ∈ Finset.Icc 1 (r (Fin.last (n + 1)) + 1) →
                          have M := Roth.lem6M (n + 2) (r 0) (↑(q 0) ^ (δ * ↑(r 0))) l;
                          have Φ :=
                            (Roth.Θ M (fun (x : Unit) ↦ q (Fin.last (n + 1))) fun (x : Unit) ↦
                                l * r (Fin.last (n + 1))) +
                              Roth.Θ M (fun (j : Fin (n + 1)) ↦ q j.castSucc) fun (j : Fin (n + 1)) ↦ l * r j.castSucc;
                          Φ + √Φ + √δ < 10 ^ (n + 2) * δ ^ (1 / 2) ^ (n + 2) / 2
```

- **What**: For every allowed determinant rank, the sum of singleton and prefix extremal indices, plus its square root and sqrt δ, is strictly below half the next-dimensional target.
- **How**: Use lem6M_lt for the coefficient scale, theta_scaled_unique_le_aux for the singleton term, theta_prefix_lt_aux for the prefix, then lem7_Φ_bound and lem7_numeric.
- **Hypotheses**: Small positive delta, antitone degree sequence, minimum last degree, ratios, denominator logarithm growth and the previous-dimensional induction hypothesis. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.lem6M`, `Roth.lem6M_lt`, `Roth.lem7_numeric`, `Roth.lem7_Φ_bound`, `Roth.one_le_lem6M`, `Roth.theta_delta_succ_lt_aux`, `Roth.theta_denominators_one_lt_aux`, `Roth.theta_prefix_lt_aux`, `Roth.theta_scaled_unique_le_aux`
- **Project references in type**: `Roth.lem6M`, `Roth.Θ`
- **Native direct body references**: `Roth.lem6M`, `Roth.lem6M_lt`, `Roth.lem7_numeric`, `Roth.lem7_Φ_bound`, `Roth.one_le_lem6M`, `Roth.theta_delta_succ_lt_aux`, `Roth.theta_denominators_one_lt_aux`, `Roth.theta_prefix_lt_aux`, `Roth.theta_scaled_unique_le_aux`, `Roth.Θ`
- **Native direct type references**: `Roth.lem6M`, `Roth.Θ`
- **Used by in file (lexical)**: `Roth.theta_lt_succ_aux`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 840–889; proof/body length 34 lines.
- **Notes**: proof/body >30 lines
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_phi_lt_aux.md).

#### lemma Roth.theta_lt_succ_aux

Type:

```lean
∀ {n : ℕ} {δ : ℝ},
  0 < δ →
    δ ≤ 1 / (↑n + 1 + 1) →
      ∀ {r q : Fin (n + 2) → ℕ},
        3 ≤ ↑(r (Fin.last (n + 1))) →
          (∀ (i : Fin (n + 1)), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
            (↑n + 1 + 1) * (2 * (↑n + 1 + 1) + 1) / δ ≤ Real.log ↑(q 0) →
              (∀ (j : Fin (n + 2)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                (∀ {δ : ℝ},
                    0 < δ →
                      δ ≤ 1 / (↑n + 1) →
                        ∀ {r q : Fin (n + 1) → ℕ},
                          3 ≤ ↑(r (Fin.last n)) →
                            (∀ (i : Fin n), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
                              (↑n + 1) * (2 * (↑n + 1) + 1) / δ ≤ Real.log ↑(q 0) →
                                (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                                  Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ (n + 1) * δ ^ (1 / 2) ^ (n + 1)) →
                  Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ (n + 2) * δ ^ (1 / 2) ^ (n + 2)
```

- **What**: The lower-dimensional extremal-index induction bound implies the next-dimensional bound in the small-δ regime with decreasing weights and balanced denominator logarithms.
- **How**: Derive positive denominators and antitone degrees; transport through Θ_equiv to Option variables, apply Θ_option_le and bound every finite-supremum term with theta_phi_lt_aux.
- **Hypotheses**: Small positive delta, minimum last degree, adjacent degree ratios, denominator logarithm growth, balanced products and induction hypothesis. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.lem6Φ`, `Roth.theta_denominators_one_lt_aux`, `Roth.theta_phi_lt_aux`, `Roth.Θ_equiv`, `Roth.Θ_option_le`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.lem6M`, `Roth.lem6Φ`, `Roth.theta_denominators_one_lt_aux`, `Roth.theta_phi_lt_aux`, `Roth.Θ`, `Roth.Θ_equiv`, `Roth.Θ_option_le`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.Θ_lt`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 891–930; proof/body length 29 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_succ_aux.md).

#### lemma Roth.theta_lt_of_large_delta_aux

Type:

```lean
∀ {n : ℕ} {δ : ℝ},
  1 / (↑n + 1) ≤ δ →
    ∀ {r q : Fin (n + 1) → ℕ}, Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ (n + 1) * δ ^ (1 / 2) ^ (n + 1)
```

- **What**: When δ≥1/(n+1), the target strict extremal-index bound follows for all natural weights and denominators without growth or balanced-log assumptions.
- **How**: Use Θ_le_card and Nat.lt_two_pow_self to bound the dimension by a power of ten divided by the dimension; Real.self_le_rpow_of_le_one and Real.rpow_le_rpow compare that reciprocal with the delta power.
- **Hypotheses**: Delta at least reciprocal dimension; no denominator or degree positivity needed. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- **Uses from project (lexical body)**: `Roth.Θ`, `Roth.Θ_le_card`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.Θ`, `Roth.Θ_le_card`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: `Roth.Θ_lt`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 932–954; proof/body length 21 lines.
- **Notes**:
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_of_large_delta_aux.md).

#### theorem Roth.Θ_lt

Type:

```lean
∀ (n : ℕ) {δ : ℝ},
  0 < δ →
    ∀ {r q : Fin (n + 1) → ℕ},
      3 ≤ ↑(r (Fin.last n)) →
        (∀ (i : Fin n), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
          (↑n + 1) * (2 * (↑n + 1) + 1) / δ ≤ Real.log ↑(q 0) →
            (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
              Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ (n + 1) * δ ^ (1 / 2) ^ (n + 1)
```

- **What**: Roth Lemma7: under weak degree growth and balanced denominator-log conditions, the supremum of bounded-height integer-polynomial indices is strictly less than10^m δ^(2^-m), for everyδ>0.
- **How**: Induct on dimension, generalizingδ. The base uses theta_lt_base_aux and theta_denominators_one_lt_aux, or theta_lt_of_large_delta_aux. The successor uses theta_lt_succ_aux for smallδ, otherwise theta_lt_of_large_delta_aux. The successor transports by Θ_equiv to Θ_option_le and bounds the finite maximum through theta_phi_lt_aux, lem6M_lt, theta_scaled_unique_le_aux, theta_prefix_lt_aux, theta_delta_succ_lt_aux, lem7_Φ_bound and lem7_numeric.
- **Hypotheses**: n+1 positive finite dimension;δ>0;natural degrees and denominators;last degree≥3;weak adjacent ratios;weak log threshold and balanced weighted logs. Noδ upper bound or explicit denominator positivity. Fresh complete proof permits last degree≥1 via stronger scratch finite-sum/Lemma6 ingredients.
- **Uses from project (lexical body)**: `Roth.theta_denominators_one_lt_aux`, `Roth.theta_lt_base_aux`, `Roth.theta_lt_of_large_delta_aux`, `Roth.theta_lt_succ_aux`
- **Project references in type**: `Roth.Θ`
- **Native direct body references**: `Roth.theta_denominators_one_lt_aux`, `Roth.theta_lt_base_aux`, `Roth.theta_lt_of_large_delta_aux`, `Roth.theta_lt_succ_aux`, `Roth.Θ`
- **Native direct type references**: `Roth.Θ`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: `Roth.theta_lt_eta_of_sq_log_bound_aux`
- **Visibility**: public
- **Lines**: 962–981; proof/body length 16 lines.
- **Notes**:
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_lt.md).

#### File structural summary

- Written declarations: 50; kinds: {'def': 5, 'theorem': 24, 'lemma': 21}
- **Key API (at least three lexical callers)**: `Roth.RSet`, `Roth.indexSet`, `Roth.Θ`, `Roth.lem6M`, `Roth.lem6Φ`, `Roth.theta_denominators_one_lt_aux`
- **Unused in file (observation)**: `Roth.floor_sq_div_two_le_sum`, `Roth.sq_div_three_lt_floor_sq_div_two`, `Roth.Θ_lt`
- **Proofs over 30 lines**: `Roth.index_separated_mul_le_aux`, `Roth.theta_phi_lt_aux`
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.

### Roth/Wronskian.lean

Completed assessments: 13/13.

#### def Roth.wronskianMatrix

Type:

```lean
{K : Type u_1} → [inst : Field K] → {l : ℕ} → (Fin l → K[X]) → Matrix (Fin l) (Fin l) K[X]
```

- **What**: Square matrix of successive univariate Hasse derivatives of a polynomial family.
- **How**: Matrix.of bundles (μ,ν) ↦ Polynomial.hasseDeriv μ (φ ν).
- **Hypotheses**: Universe-polymorphic K with Field K, mechanically weakenable to Semiring.; Implicit length l : ℕ; explicit φ : Fin l → Polynomial K.; No characteristic, independence, nonzero or positive-length assumption.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.wronskian`, `Roth.wronskian_eq_zero_of_not_linearIndependent`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`
- **Used by other files (lexical)**: `Roth.wronskian_kronecker_eq_sum_aux`, `Roth.det_hasseDeriv_separated`
- **Visibility**: public
- **Lines**: 56–57; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskianMatrix.md).

#### def Roth.wronskian

Type:

```lean
@Roth.wronskian : {K : Type u_1} → [inst : Field K] → {l : ℕ} → (Fin l → K[X]) → K[X]
```

- **What**: Determinant of consecutive Hasse derivatives of a finite polynomial family.
- **How**: Matrix.det of Roth.wronskianMatrix; exact expanded mathlib expression verified.
- **Hypotheses**: Field K in unchanged parent interface; implicit l : ℕ, arbitrary including0; explicit φ : Fin l → K[X]
- **Uses from project (lexical body)**: `Roth.wronskianMatrix`
- **Project references in type**: []
- **Native direct body references**: `Roth.wronskianMatrix`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.wronskian_eq_zero_of_not_linearIndependent`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`, `Roth.wronskian_ne_zero_of_linearIndependent`, `Roth.wronskian_eq_zero_iff`
- **Used by other files (lexical)**: `Roth.wronskian_kronecker_eq_sum_aux`, `Roth.det_hasseDeriv_separated`, `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Visibility**: public
- **Lines**: 60–60; proof/body length 1 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian.md).

#### theorem Roth.wronskian_eq_zero_of_not_linearIndependent

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → Polynomial K}, ¬ LinearIndependent K φ → Roth.wronskian φ = 0
```

- **What**: Coefficient-field linear dependence forces zero finite Hasse Wronskian.
- **How**: Extract nontrivial constant relation; Hasse linearity gives nonzero polynomial kernel vector; determinant vanishes. Verified improved four-call column-independence/scalar-restriction proof.
- **Hypotheses**: Field K; finite length l; family φ; ¬ LinearIndependent K φ
- **Uses from project (lexical body)**: `Roth.wronskianMatrix`
- **Project references in type**: `Roth.wronskian`
- **Native direct body references**: `Roth.wronskian`, `Roth.wronskianMatrix`
- **Native direct type references**: `Roth.wronskian`
- **Used by in file (lexical)**: `Roth.wronskian_eq_zero_iff`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 65–72; proof/body length 7 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_of_not_linearIndependent.md).

#### theorem Roth.det_choose_eq

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] (d : Fin l → ℕ), (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : K)).det = (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) * ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i)
```

- **What**: Evaluates the natural-binomial matrix determinant as the Vandermonde difference product divided by the product of row factorials.
- **How**: Proves the entrywise falling-factorial evaluation/row-scaling bridge, then uses det scaling, transpose, existing monic evaluation determinant law and det_vandermonde.
- **Hypotheses**: Field K; CharZero K; arbitrary l and natural tops d. CharZero can be replaced by local factorial nonvanishing; arbitrary CommRing cancellation-free form is also verified.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.wronskian_ne_zero_of_natDegree_injective`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 79–91; proof/body length 10 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.det_choose_eq.md).

#### lemma Roth.coeff_prod_of_natDegree_le'

Type:

```lean
{K : Type*} [Field K] {ι : Type*} (s : Finset ι) (f : ι → K[X]) (n : ι → ℕ) (h : ∀ i ∈ s, (f i).natDegree ≤ n i) : (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i)
```

- **What**: Boundary coefficient of a finite polynomial product with per-factor degree bounds is the product of boundary coefficients.
- **How**: Finite-set induction, two-factor coefficient identity and product-degree bound.
- **Hypotheses**: Field source interface, same proof verified over CommSemiring. Arbitrary ambient indices and per-factor natural bounds on the finite set.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.coeff_wronskian_of_natDegree_injective`
- **Used by other files (lexical)**: []
- **Visibility**: private
- **Lines**: 93–103; proof/body length 9 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_prod_of_natDegree_le'.md).

#### theorem Roth.sum_range_le_sum_of_injective

Type:

```lean
∀ {l : ℕ} (d : Fin l → ℕ), Function.Injective d → (∑ ν : Fin l, (ν : ℕ)) ≤ ∑ ν, d ν
```

- **What**: Any l distinct natural numbers have sum at least 0+1+⋯+(l−1).
- **How**: Embed the finite image into ℤ, apply Finset.sum_range_le_sum at c=0, normalize image cardinality/sums and reflect the inequality through casts.
- **Hypotheses**: {l : ℕ}, d : Fin l → ℕ, Function.Injective d. No coefficient field or characteristic binder.
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 107–114; proof/body length 7 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_range_le_sum_of_injective.md).

#### theorem Roth.coeff_wronskian_of_natDegree_injective

Type:

```lean
∀ {K : Type u} [Field K] {l : ℕ} {φ : Fin l → K[X]}, (Roth.wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) = (∏ ν, (φ ν).leadingCoeff) * (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det
```

- **What**: Computes the coefficient at the top possible degree of a finite polynomial Hasse Wronskian as product of leading coefficients times a binomial determinant.
- **How**: Use coeff_prod_of_natDegree_le' and natDegree_hasseDeriv_le on each permutation product; hasseDeriv_eq_zero_of_lt_natDegree handles excessive orders, then Matrix.det_apply' sums the signed terms.
- **Hypotheses**: Arbitrary polynomial family over a field; no nonzero, distinct-degree, CharZero, independence, or positive-size premise.
- **Uses from project (lexical body)**: `Roth.coeff_prod_of_natDegree_le'`, `Roth.wronskian`, `Roth.wronskianMatrix`
- **Project references in type**: `Roth.wronskian`
- **Native direct body references**: `Roth.coeff_prod_of_natDegree_le'`, `Roth.wronskian`, `Roth.wronskianMatrix`
- **Native direct type references**: `Roth.wronskian`
- **Used by in file (lexical)**: `Roth.wronskian_ne_zero_of_natDegree_injective`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 122–142; proof/body length 19 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_wronskian_of_natDegree_injective.md).

#### theorem Roth.wronskian_ne_zero_of_natDegree_injective

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K]
  {φ : Fin l → K[X]}, (∀ (ν : Fin l), φ ν ≠ 0) → (Function.Injective fun ν ↦ (φ ν).natDegree) → Roth.wronskian φ ≠ 0
```

- **What**: Nonzero polynomials of distinct degrees have nonzero normalized Hasse Wronskian in characteristic zero.
- **How**: One coefficient equals product of leading coefficients times a binomial determinant; Vandermonde gives nonvanishing.
- **Hypotheses**: Field K; CharZero K; all family members nonzero; natural-degree function injective
- **Uses from project (lexical body)**: `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.det_choose_eq`
- **Project references in type**: `Roth.wronskian`
- **Native direct body references**: `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.det_choose_eq`, `Roth.wronskian`
- **Native direct type references**: `Roth.wronskian`
- **Used by in file (lexical)**: `Roth.wronskian_ne_zero_of_linearIndependent`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 148–152; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_natDegree_injective.md).

#### theorem Roth.wronskian_update_sub_smul

Type:

```lean
∀ {K : Type u_1} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l}, ν ≠ ν' → ∀ (c : K), Roth.wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = Roth.wronskian φ
```

- **What**: Subtracting a constant multiple of one distinct family member preserves its Hasse-Wronskian.
- **How**: Identify the updated Hasse matrix entrywise using coefficient linearity, then apply Matrix.det_updateCol_add_smul_self with negative constant scalar.
- **Hypotheses**: Field K fixed by parent interface; distinct Fin l indices; any constant c. No CharZero, independence, degree or nonzero assumptions.
- **Uses from project (lexical body)**: `Roth.wronskianMatrix`
- **Project references in type**: `Roth.wronskian`
- **Native direct body references**: `Roth.wronskian`, `Roth.wronskianMatrix`
- **Native direct type references**: `Roth.wronskian`
- **Used by in file (lexical)**: `Roth.wronskian_ne_zero_of_linearIndependent`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 158–164; proof/body length 6 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_update_sub_smul.md).

#### theorem Roth.linearIndependent_update_sub_smul

Type:

```lean
∀ {K : Type u_1} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l}, ν ≠ ν' → ∀ c : K, LinearIndependent K φ → LinearIndependent K (Function.update φ ν' (φ ν' - Polynomial.C c * φ ν))
```

- **What**: Elementary column subtraction preserves independence of a polynomial family.
- **How**: Rewrite independence as family cardinality equals span finrank; use span_range_update_sub_smul.
- **Hypotheses**: Field K (weakenable to Ring/module); distinct source/destination (necessary uniformly); initial independence (necessary)
- **Uses from project (lexical body)**: []
- **Project references in type**: []
- **Native direct body references**: []
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.sum_natDegree_update_lt`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 170–175; proof/body length 4 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_update_sub_smul.md).

#### theorem Roth.sum_natDegree_update_lt

Type:

```lean
∀ {K : Type u} [Field K] {l : ℕ} {φ : Fin l → K[X]}, LinearIndependent K φ → ∀ {ν ν' : Fin l}, ν ≠ ν' → (φ ν).natDegree = (φ ν').natDegree → ∑ ρ, (Function.update φ ν' (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree < ∑ ρ, (φ ρ).natDegree
```

- **What**: Cancelling equal leading terms strictly lowers the sum of degrees of an independent finite polynomial family.
- **How**: Prove updated difference nonzero, cancel leading coefficients, convert degree to natDegree, apply Finset.sum_lt_sum.
- **Hypotheses**: Field K; LinearIndependent K φ; distinct indices; equal natural degrees
- **Uses from project (lexical body)**: `Roth.linearIndependent_update_sub_smul`
- **Project references in type**: []
- **Native direct body references**: `Roth.linearIndependent_update_sub_smul`
- **Native direct type references**: []
- **Used by in file (lexical)**: `Roth.wronskian_ne_zero_of_linearIndependent`
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 182–200; proof/body length 16 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_natDegree_update_lt.md).

#### theorem Roth.wronskian_ne_zero_of_linearIndependent

Type:

```lean
∀ {K : Type u_2} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, LinearIndependent K φ → Roth.wronskian φ ≠ 0
```

- **What**: The hard implication of the characteristic-zero polynomial Wronskian criterion: a linearly independent finite family has nonzero consecutive Hasse determinant.
- **How**: Strong induction on total natural degree; repeated degrees are removed by constant column shears, reducing to Vandermonde nonvanishing for distinct degrees.
- **Hypotheses**: Field K; CharZero K; φ : Fin l → K[X]; LinearIndependent K φ
- **Uses from project (lexical body)**: `Roth.linearIndependent_update_sub_smul`, `Roth.sum_natDegree_update_lt`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`
- **Project references in type**: `Roth.wronskian`
- **Native direct body references**: `Roth.linearIndependent_update_sub_smul`, `Roth.sum_natDegree_update_lt`, `Roth.wronskian`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`
- **Native direct type references**: `Roth.wronskian`
- **Used by in file (lexical)**: `Roth.wronskian_eq_zero_iff`
- **Used by other files (lexical)**: `Roth.exists_genWronskian_ne_zero`, `Roth.exists_rat_factors_det_hasseDeriv_aux`
- **Visibility**: public
- **Lines**: 205–214; proof/body length 9 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_linearIndependent.md).

#### theorem Roth.wronskian_eq_zero_iff

Type:

```lean
∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, Roth.wronskian φ = 0 ↔ ¬ LinearIndependent K φ
```

- **What**: The n-ary characteristic-zero polynomial Hasse Wronskian vanishes exactly for linearly dependent families.
- **How**: Packages the contrapositive of the project hard implication with the project easy implication; the hard proof uses degree elimination and Vandermonde nonvanishing.
- **Hypotheses**: Field K; CharZero K; φ : Fin l → K[X]
- **Uses from project (lexical body)**: `Roth.wronskian_eq_zero_of_not_linearIndependent`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Project references in type**: `Roth.wronskian`
- **Native direct body references**: `Roth.wronskian`, `Roth.wronskian_eq_zero_of_not_linearIndependent`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Native direct type references**: `Roth.wronskian`
- **Used by in file (lexical)**: []
- **Used by other files (lexical)**: []
- **Visibility**: public
- **Lines**: 219–222; proof/body length 2 lines.
- **Notes**: No set_option, sorry, TODO, or proof over 30 lines in declaration.
- **Verdict**: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_iff.md).

#### File structural summary

- Written declarations: 13; kinds: {'def': 2, 'theorem': 10, 'lemma': 1}
- **Key API (at least three lexical callers)**: `Roth.wronskianMatrix`, `Roth.wronskian`, `Roth.wronskian_ne_zero_of_linearIndependent`
- **Unused in file (observation)**: `Roth.sum_range_le_sum_of_injective`, `Roth.wronskian_eq_zero_iff`
- **Proofs over 30 lines**: []
- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.



## Part 2: Cross-file dependencies

| Caller file | Referenced file | Direct body edges | Direct type edges |
|---|---|---:|---:|
| `Roth/CoeffNorm.lean` | `Roth/Box.lean` | 4 | 1 |
| `Roth/CoeffNorm.lean` | `Roth/HasseDeriv.lean` | 11 | 4 |
| `Roth/GenWronskian.lean` | `Roth/HasseDeriv.lean` | 10 | 2 |
| `Roth/GenWronskian.lean` | `Roth/Wronskian.lean` | 4 | 1 |
| `Roth/Index.lean` | `Roth/Box.lean` | 23 | 5 |
| `Roth/Index.lean` | `Roth/HasseDeriv.lean` | 14 | 5 |
| `Roth/Index.lean` | `Roth/Taylor.lean` | 18 | 2 |
| `Roth/Lattice.lean` | `Roth/Box.lean` | 17 | 12 |
| `Roth/LeanEval.lean` | `Roth/Main.lean` | 6 | 2 |
| `Roth/Main.lean` | `Roth/Box.lean` | 5 | 1 |
| `Roth/Main.lean` | `Roth/HasseDeriv.lean` | 2 | 1 |
| `Roth/Main.lean` | `Roth/Index.lean` | 3 | 1 |
| `Roth/Main.lean` | `Roth/MainLemma.lean` | 19 | 8 |
| `Roth/Main.lean` | `Roth/Taylor.lean` | 1 | 0 |
| `Roth/MainLemma.lean` | `Roth/Box.lean` | 10 | 5 |
| `Roth/MainLemma.lean` | `Roth/CoeffNorm.lean` | 12 | 5 |
| `Roth/MainLemma.lean` | `Roth/HasseDeriv.lean` | 19 | 12 |
| `Roth/MainLemma.lean` | `Roth/Index.lean` | 11 | 9 |
| `Roth/MainLemma.lean` | `Roth/Lattice.lean` | 1 | 0 |
| `Roth/MainLemma.lean` | `Roth/Theta.lean` | 10 | 8 |
| `Roth/Separation.lean` | `Roth/CoeffNorm.lean` | 1 | 0 |
| `Roth/Separation.lean` | `Roth/GenWronskian.lean` | 3 | 1 |
| `Roth/Separation.lean` | `Roth/HasseDeriv.lean` | 9 | 4 |
| `Roth/Separation.lean` | `Roth/Wronskian.lean` | 4 | 1 |
| `Roth/Taylor.lean` | `Roth/Box.lean` | 2 | 2 |
| `Roth/Taylor.lean` | `Roth/HasseDeriv.lean` | 14 | 6 |
| `Roth/Theta.lean` | `Roth/Box.lean` | 6 | 2 |
| `Roth/Theta.lean` | `Roth/CoeffNorm.lean` | 1 | 0 |
| `Roth/Theta.lean` | `Roth/HasseDeriv.lean` | 6 | 3 |
| `Roth/Theta.lean` | `Roth/Index.lean` | 28 | 7 |
| `Roth/Theta.lean` | `Roth/Separation.lean` | 5 | 0 |

The main chain is Hasse/Taylor and coefficient estimates → Wronskian/separation and index/lattice estimates → Theta bound → auxiliary polynomial main lemma → Roth contradiction → LeanEval formulation. Source-import and canonical direct-expression graphs describe different layers.

The default Roth library target does not import Roth.LeanEval. Final validation must run both `lake build` and `lake build Roth.LeanEval`.


## Cross-file interpretation

Hasse/Taylor and coefficient-size API support determinant and index estimates. Wronskian independence feeds separation/Theta; lattice counting bounds the derivative constraints. MainLemma constructs bounded integer candidates, finds remainder collisions, subtracts a nonzero bounded difference, proves root vanishing and selects a nonvanishing derivative at a rational point. Main compares the resulting Taylor upper estimate to an integer-value lower estimate. LeanEval converts finite approximation exceptions into uniform positive constants. These are distinct mathematical stages, not duplicated versions of one theorem.

## Part 3: Mathlib API audit

Completed finding: hasseCoeff uses the existing finite-support product and natural choice
operations. `Finsupp.multinomial` is a different operation and is not a replacement. The
mathlib-only construction compiled without importing the project target.

Completed derivative finding: pinned mathlib has ordinary multivariate `pderiv` and
univariate `Polynomial.hasseDeriv`, but no verified arbitrary-multiindex normalized
operator. Generic coefficient-linear extension constructs it; this is distinct from
a ready-made differential API replacement.

Completed `MvPolynomial.hasseDeriv_monomial`: Existing Finsupp.lsum_single generic evaluation; univariate Polynomial.hasseDeriv_monomial and order-one MvPolynomial.pderiv_monomial are partial analogues, not arbitrary-multiindex replacements.

Completed `MvPolynomial.hasseDeriv_apply`: Direct Finsupp.lsum_apply term accepted for original target. MvPolynomial.sum_def is existing support-sum bridge; Polynomial.hasseDeriv_apply is only univariate analogue.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: Five methods on 3 forms; Finsupp.prod_eq_zero_iff/prod_ne_zero_iff, Nat.choose_eq_zero_iff/choose_ne_zero_iff and Finsupp.le_iff verified at pin; generic simp passes.

Completed `MvPolynomial.coeff_hasseDeriv`: Univariate Polynomial.hasseDeriv_coeff is the direct analogue, not an arbitrary-variable replacement. LaurentSeries coefficient API, coeff_pderiv, lsum and comapDomain building blocks do not alone prove the truncated-subtraction collision/vanishing identity. All five search methods and isolated exact? guard executed; local symbol index unavailable.

Completed `MvPolynomial.hasseCoeff_eq_prod`: All five methods searched concrete/literature and abstract forms. Finsupp.prod_fintype (BigOperators/Finsupp/Basic:63) plus Nat.choose_zero_right (Choose/Basic:56) proves the exact target. Isolated pinned check and complete caller rewrite verified; unavailable local index supplies no absence evidence.

Completed `MvPolynomial.hasseDeriv_zero_apply`: All five methods actually searched current/literature and abstract forms. Polynomial zero laws are univariate analogues, generic reconstruction/lsum laws supply normalization machinery. Guarded mathlib-only reconstruction plus exact?/apply? positive controls and positive candidate signatures verified in pin. Local index unavailable.

Completed `MvPolynomial.hasseDeriv_zero`: All five methods actually searched current, literature and abstract forms. Polynomial.hasseDeriv_zero is an analogous bundled univariate law; LaurentSeries analogue distinct. LinearMap.ext and polynomial reconstruction support normalization, with native pinned positive checks. Local index unavailable.

Completed `MvPolynomial.hasseDeriv_C`: All five actual methods on current/literature/abstract forms. Polynomial.hasseDeriv_C is univariate analogue, pderiv_C ordinary first derivative only. C_apply and lsum_single genuine generic normalization blocks; local factor-zero is new proof, not existing replacement.

Completed `MvPolynomial.hasseDeriv_map`: Pinned Polynomial.hasseDeriv_map and MvPolynomial.pderiv_map are analogues, not all-multiorder arbitrary-variable replacements. Actual raw construction needs monomial calculation and additive induction.

Completed `MvPolynomial.hasseDeriv_rename`: Pinned pderiv_rename is first-order analogue; Finsupp.prod_mapDomain_index_inj/mapDomain_apply_of_injective/mapDomain_tsub supply individual monomial transports, not full Hasse identity.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Applicable private-helper triage: existing Nat.choose_mul/choose_symm_add and Finsupp support-product extension supply the scalar proof. Exact native replay validated. Full public mathlibable search n/a by private prefilter.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: Five actual search methods: univariate Polynomial.hasseDeriv_comp analogue is not arbitrary-variable replacement.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: All five actual methods on current/literature/abstract forms; univariate iteration is analogue only; lattice predicate equivalence verified.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Private specialization of the shared binomial cocycle; native exact-body replay passes. Public mathlibable phase n/a by explicit private prefilter.

Completed `MvPolynomial.pderiv_hasseDeriv`: All five methods on three forms; pinned univariate analogue compiled but does not directly cover arbitrary multivariate inputs.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: Univariate natDegree_hasseDeriv_le exists at HasseDeriv179, generic degreeOf_le_iff/monomial_le_degreeOf support API at Degrees235/268; no arbitrary-variable bridge established.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: Polynomial.hasseDeriv_eq_zero_of_lt_natDegree is univariate analogue; MvPolynomial.notMem_support_of_degreeOf_lt, notMem_support_iff and extensionality are generic blocks. No multivariate normalization supplied by ≤3 existing calls.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Existing polynomial induction/monomial product and support-product congruence prove the separated monomial step; exact native replay verified. Private-prefilter public search n/a.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Univariate hasseDeriv_mul and first-order pderiv_mul are partial analogues; base-R map_smul cannot pass general undifferentiated polynomial factors. No existing multivariate bridge.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: All five methods on current/literature/abstract forms; positive toMvPolynomial and monomial/ext API, no existing Hasse bridge; local indexes unavailable.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: Univariate Hasse and canonical polynomial equivalence exist; no named pinned multivariate compatibility. All five methods on three forms; local index unavailable.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Five actual methods on three forms identify scalar choose bound and generic product/power infrastructure. Four substantive facts needed; local index unavailable.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Polynomial.factorial_smul_hasseDeriv and LaurentSeries.derivative_iterate are analogous different domains; commutative ideal DividedPowers not arbitrary operator composition.

Completed `Roth.box`: Existing Finset.Iic + Finsupp.equivFunOnFinite.symm gives same object; raw mathlib-only native equality/cardinality/sum-product verified.

Completed `Roth.weight`: Exact general existing Finsupp.weight specialized to ℕ scalars and reciprocal real weights; native representation equality verified.

Completed `Roth.mem_box`: Finset.mem_map_equiv, Fintype.mem_piFinset, Finset.mem_range_succ_iff, Finset.mem_Iic, Finsupp.le_def

Completed `Roth.card_box`: Finset.card_map, Fintype.card_piFinset, Finset.card_range, Finsupp.card_Iic, Finsupp.prod_fintype, Nat.card_Iic

Completed `Roth.card_le_card_box`: Five actual search methods on current/standard/abstract forms. Existing generic function-family bound composes in three facts. Original Fin injection uses four domain facts including endpoint conversion; expanded original uses seven. Finsupp.card_Iic gives support product; normalization tested.

Completed `Roth.weight_nonneg`: verdict: NO-composable-from-mathlib; facts: Finset.sum_nonneg, div_nonneg, Nat.cast_nonneg; distinct facts: 3; expanded applications: 4; formal methods times forms: 5 x 3 actual; local-name index unavailable recorded

Completed `Roth.weight_zero`: Finset.sum_eq_zero + Nat.cast_zero + zero_div; bundled Finsupp.weight has generic map_zero.

Completed `Roth.weight_add`: Three existing arithmetic facts compose at current representation; generic map_add already supplies abstract Finsupp.weight additivity after a proved reciprocal-weight bridge.

Completed `Roth.weight_eq_zero_iff`: Finsupp.weight_eq_zero_iff_eq_zero needs canonical order, not applicable directly to ℝ. le_weight_of_ne_zero enables verified new ordered-monoid positive-weight helper.

Completed `Roth.weight_single`: Finsupp.weight_single already supplies arbitrary semiring/module basis evaluation; original finite division sum requires ratio bridge. Finsupp.sum_single_index plus sum_fintype are generic primitives.

Completed `Roth.weight_le_card`: Finset.sum_le_card_nsmul + div_le_one_of_le₀ + Nat.cast_le + Nat.cast_nonneg + nsmul_one. Generic field form uses three facts; original requires casts.

Completed `Roth.weight_mul_left`: Genuine generator-family law supplied by (Finsupp.bilinearCombination R S).map_smul; Finsupp.weight underlying linearCombination. Reciprocal bridge independently compiled.

Completed `Roth.weight_le_degree_div`: Actual Finder/Loogle/LeanSearch/rg/local searches on original, weighted-degree and abstract linearCombination forms. Existing Finsupp.weight/degree relations and sum/division order primitives inspected; no analogous bundled upper-bound hit established.

Completed `Roth.weight_mapDomain`: Finsupp.linearCombination_mapDomain at Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:158 is exact generic analogue on Finsupp.weight; finite sum/division bridge is propositional.

Completed `Roth.wronskianMatrix`: verdict: BORDERLINE-needs-human; building blocks: Matrix.of, Polynomial.hasseDeriv; near matches: Polynomial.wronskian (binary polynomial output), Polynomial.taylor_coeff (evaluated entries), LinearMap.toMatrix (basis-coordinates, not arbitrary-family constructor); gap anchor: Mathlib/RingTheory/Polynomial/Wronskian.lean TODO: define Wronskian for n-tuple, not necessarily two.; formal methods: Finder, Loogle, LeanSearch, rg, local each on current/standard/abstract forms.; local index: unavailable; no absence inference.

Completed `Roth.wronskian`: Binary Polynomial.wronskian exact Fin2 bridge; arbitrary n-tuple TODO pinned. Raw det/of/hasseDeriv three-building-block construction compiled.

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: AlternatingMap.map_linearDependent existing abstract law, Matrix.det_eq_zero_of_not_linearIndependent_cols, LinearIndependent.restrict_scalars', LinearIndependent.of_comp, LinearMap.pi

Completed `Roth.det_choose_eq`: generic law: Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde already exists; native checked one-call abstract form; building blocks: Nat.cast_choose_eq_descPochhammer_div, Matrix.det_mul_column, Matrix.det_transpose, Matrix.det_vandermonde, Polynomial.monic_descPochhammer, Polynomial.descPochhammer_natDegree; private near match: Vandermonde.lean:301 of_eval_descPochhammer_eq_mul_of_choose is private over ℤ; not an accessible replacement; all five methods all three forms: True

Completed `Roth.coeff_prod_of_natDegree_le'`: Public coeff_prod_of_natDegree_le uses one common bound; this variant uses n i. Native signature comparison and replay verified.

Completed `Roth.sum_range_le_sum_of_injective`: replacement: Finset.sum_range_le_sum; path: Mathlib/Algebra/Order/Group/Int/Sum.lean:72; same mathematical law: True; bridge: Nat.castEmbedding + image cardinality + sum_image + Fin.sum_univ_eq_sum_range + Nat.cast_sum + cast order reflection; not defeq and not claimed ≤3 calls.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Five actual methods on current/literature/abstract forms. Binary Wronskian and affine/triangular determinant coefficient candidates are partial matches. Native exact? and simp attempts fail with residual mathematical work.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: Mathlib has binary Polynomial.wronskian, an explicit n-tuple TODO, and generic Matrix.det_vandermonde_ne_zero_iff. All five actual methods searched current/literature/abstract forms; no direct family replacement. Local index unavailable does not prove absence.

Completed `Roth.wronskian_update_sub_smul`: Generic column law exists at Matrix/Determinant/Basic.lean:478. Binary Polynomial.wronskian differs. Three actual direct simpa routes fail; explicit representation bridge verified.

Completed `Roth.linearIndependent_update_sub_smul`: More-general existing linearIndependent_add_smul_iff; generic update bridge and exact old-form polynomial bridge compiled.

Completed `Roth.sum_natDegree_update_lt`: Existing degree_sub_lt_left, cancelLeads natural-degree law, natDegree_lt_natDegree, Finset.sum_lt_sum and sum_update_of_mem. No verified ≤3-call entire original proof.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: Pinned binary Polynomial.wronskian and IsCoprime criterion do not cover arbitrary families. Generic determinant independence changes scalars and does not supply jet-column independence. Wronskian.lean has an explicit n-tuple TODO. All five actual search methods on four forms; isolated exact? failed without timeout.

Completed `Roth.wronskian_eq_zero_iff`: Five actual methods on current, standard and abstract forms. Exact binary IsCoprime.wronskian_eq_zero_iff is a coprime/derivatives-zero theorem, not the n-ary criterion. Pinned TODO explicitly requests n-tuples. Mathlib-only raw iff exact? fails without timeout.

Completed `MvPolynomial.taylor`: aeval/bind₁ yield the exact term; Polynomial.taylorAlgHom and taylorEquiv cover one variable only. Named multivariate shift not located; missing local index is not absence proof.

Completed `MvPolynomial.taylor_apply`: MvPolynomial.aeval supplies the defining substitution; own bridge is reflexive. Pinned Polynomial.taylor_apply is an analogous rfl law on Polynomial/LinearMap, not an exact multivariate hit; aeval_def expands a different layer.

Completed `MvPolynomial.taylor_X`: Existing more general MvPolynomial.aeval_X at Mathlib/Algebra/MvPolynomial/Eval.lean:587; arbitrary commutative R-algebra assignment. eval₂_X is a broader coefficient-map generator rule. Polynomial.taylor_X is only a pinned univariate analogy.

Completed `MvPolynomial.taylor_C`: existing: MvPolynomial.algHom_C; file: Mathlib/Algebra/MvPolynomial/Basic.lean:441; broader: Arbitrary R-algebra homomorphism to any Semiring A with Algebra R A, including noncommutative A; scalar image algebraMap R A a; secondary: MvPolynomial.aeval_C, Polynomial.taylor_C; native: Target exact specialization, isolated arbitrary-AlgHom/raw translation, full copied named caller and target-disabled simp consumers all clean complete

Completed `MvPolynomial.taylor_monomial`: NO-mathlib-has-it: aeval_monomial at Mathlib/Algebra/MvPolynomial/Eval.lean:681; one-call exact target and independent mathlib-only arbitrary-algebra proof checked. Five actual methods × three forms.

Completed `MvPolynomial.coeff_aeval_X_mul`: Private coefficient-convolution reduction using polynomial evaluation sum and coeff_monomial_mul′; no public contribution verdict inferred.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Extracts one factor with Finsupp.mul_prod_erase′, then finite-product congruence; direct project definition hasseCoeff retained. No public mathlibable absence/inclusion claim.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Existing finite-product splitting, powers and coordinate erasure express exact proof; no public contribution verdict under private rule.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Uses Polynomial.coeff_X_add_C_pow and existing monomial/evaluation/multiplication laws plus three separately reviewed private project helpers; not a library-only composition claim.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Finsupp.induction supplies exponent recursion; generic algHom_C handles constants. Direct expression audit maps private replay to canonical61 and confirms no later coeff_taylor use.

Completed `MvPolynomial.coeff_taylor`: existing analogue: Polynomial.taylor_coeff; exact multivariate hit: False; five methods three forms: formal-search.json; composition: No ≤3-call proof demonstrated; tested expanded simp and default exact? leave genuine coefficient normalization.

Completed `MvPolynomial.eval_taylor`: eval_assoc, comp_aeval_apply, eval_eval₂, map_add, eval_X, eval_C

Completed `MvPolynomial.taylor_taylor`: comp_aeval_apply, comp_aeval, map_add, aeval_X, algHom_C, add_assoc, C_add

Completed `MvPolynomial.taylor_zero`: Existing map_zero(C), add_zero, aeval_X_left_apply compose exact old form; structural congrArg×2/funext/Eq.trans×2 explicit. aeval_X_left is bundled canonical identity. Univariate Polynomial.taylor_zero is only analogue.

Completed `MvPolynomial.taylor_map`: map_eval₂ is exact generic substitution law; map_aeval/eval₂_map and Monad.map_bind₁ are related. Original translated-generator normalization is propositional, not a direct exact call. Polynomial.map_taylor is univariate analogue over Semiring.

Completed `MvPolynomial.taylor_rename`: aeval_rename and comp_aeval_apply are exact abstract compatibility laws. Original normalized translation square requires five mathematical facts; not a one-call defeq replacement.

Completed `MvPolynomial.degreeOf_taylor_le`: Existing degreeOf_le_iff and degree bounds on sums/products do not prove the essential translated coefficient vanishing. Polynomial.natDegree_taylor is univariate; aeval_natDegree_le uses total degree and a univariate target.

Completed `MvPolynomial.taylor_neg_taylor`: Univariate Polynomial.taylorEquiv and algEquivAevalXAddC are close analogues, not multivariate replacements. Generic inverse-application law needs an already verified multivariate equivalence.

Completed `MvPolynomial.taylor_injective`: Function.LeftInverse.injective exists but requires the project-specific inverse premise. Polynomial.taylor_injective works over Ring, univariate only. New translation AlgEquiv would supply injectivity generically, after proving its inverse fields.

Completed `MvPolynomial.taylor_eq_zero_iff`: Polynomial.taylor_eq_zero and comp_X_add_C_eq_zero_iff are Semiring/univariate at pinned revision; generic zero-preserving injection iff exists but requires an injectivity premise. New multivariate semiring maximal-support proof is not an existing-call composition.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Polynomial.sum_taylor_eq is univariate CommRing analogue. eval₂_eq supplies arbitrary-variable finite-support reconstruction, but not Hasse coefficient identification or off-box vanishing. Isolated successful support expansion verifies the boundary.

Completed `MvPolynomial.eval_eq_sum_box`: eval₂_eq/aeval_sum/aeval_prod and Polynomial.sum_taylor_eq are generic evaluation/univariate inputs, not multivariate Hasse identity. Isolated support-evaluation via explicit RingHom succeeds but lacks Hasse coefficients and box cutoff.

Completed `Roth.normOne`: Finsupp.sum gives exact scalar construction by rfl. Finsupp WithLp1 dist-to-zero equals it, verified with zipWith/mapRange normalization. Current pinned file has metric structures, not a full normed-group/ring structure. Polynomial.supNorm is univariate maximum, not this sum.

Completed `Roth.diag`: MvPolynomial.aeval (Eval569) gives exact construction; comp_aeval_apply and Polynomial.aeval_X give arbitrary algebra-target evaluation. Existing rename and uniqueAlgEquiv supply alternate bundle. pUnitAlgEquiv deprecated in pinned source, avoided in probes.

Completed `Roth.normOne_nonneg`: Finset.sum_nonneg and abs_nonneg close exact expanded statement; Finsupp.sum_nonneg supplies generalized arbitrary-index ordered-codomain aggregation. No exact generic norm_nonneg application without correct norm structure bridge.

Completed `Roth.normOne_eq_sum_of_support_subset`: Existing same padding theorem Finsupp.sum_of_support_subset at arbitrary index/Zero coefficient/AddCommMonoid codomain; MvPolynomial sum definition provides representation. Finset.sum_subset and coefficient-vanishing give original proof. All5 methods/3forms checked.

Completed `Roth.normOne_monomial`: MvPolynomial.sum_monomial_eq exists in pinned Basic275–278; Finsupp.sum_single_index gives arbitrary Zero coefficient/AddCommMonoid codomain version. All5 methods/3forms actually searched and pinned law signatures compiled.

Completed `Roth.normOne_zero`: Pinned Finsupp.sum_zero_index generated at Algebra/BigOperators/Finsupp/Basic86–88; arbitrary indexed size, Zero coefficients and AddCommMonoid output, no zero-preservation premise. Direct old-interface term and all generic probes freshly compiled. All5 methods/3forms run; Loogle retries retained.

Completed `Roth.abs_coeff_le_normOne`: NO-mathlib-has-it: Finsupp.single_eval_le_sum, Mathlib/Data/Finsupp/Order.lean:165–170; independently pinned type and exact specialization verified. Four external/local formal methods × three forms plus rg on each; current Loogle syntax/rate failures retained and corrected query succeeded.

Completed `Roth.normOne_add_le`: Finsupp.sum_of_support_subset, Finset.sum_add_distrib, Finset.sum_le_sum and abs_add_le give a real common-support proof. sum_add_index requires equality; norm_add_le needs correct bundled structure. WithLp1 Finsupp has metric structure, and two freshly proved bridges recover triangle. No checked≤3-existing-call replacement.

Completed `Roth.normOne_neg`: Finsupp.sum_neg_index generated from prod_neg_index Basic265–268, Int.cast_neg and abs_neg give direct checked composition; Int.cast_zero/abs_zero discharge zero-preservation parameter. Generic norm_neg requires matching norm structure and is not treated as direct project norm law.

Completed `Roth.normOne_sum_le`: Existing Finset.le_sum_of_subadditive supplies finite induction; norm_sum_le needs a seminormed additive group compatible with this coefficient size. Project triangle is not an existing mathlib building block.

Completed `Roth.normOne_mul_le`: Existing convolution expansion, finite sums and scalar size identities; norm_mul_le needs an L1-compatible seminormed multiplication structure absent from tested environment.

Completed `Roth.normOne_prod_le`: Finset.le_prod_of_submultiplicative_of_nonneg already supplies all finite induction. Finset.norm_prod_le requires compatible NormedCommRing and NormOneClass; no raw instance in tested environment.

Completed `Roth.normOne_le_card_mul`: Finset.sum_le_card_nsmul at Algebra/Order/BigOperators/Group/Finset.lean:285 generated from prod_le_pow_card. Current native signature uses Preorder.

Completed `Roth.normOne_det_le`: Matrix.det_le requires multiplicative AbsoluteValue; existing RingSeminorm supports submultiplicativity but searched determinant law missing.

Completed `Roth.abs_coeff_hasseDeriv_le`: Polynomial.hasseDeriv_coeff and norm_nsmul_le cover separate ingredients; no searched multivariate Hasse coefficient-size bound. Isolated raw binomial bound and actual generic operator bound compiled.

Completed `Roth.normOne_hasseDeriv_le`: Five actual methods across current/standard/abstract forms. Existing finite sum/natural binomial facts are building blocks; actual multivariate Hasse operator absent in guarded mathlib-only native environment.

Completed `Roth.diag_eq_sum`: eval₂_eq plus aeval_def, prod_pow_eq_pow_sum, degree_apply, algebraMap_eq, C_mul_X_pow_eq_monomial compile generically. No exact diagonal theorem established; local index unavailable.

Completed `Roth.abs_coeff_diag_le`: Finset.abs_sum_le_sum_abs, Finset.le_sum_of_subadditive, Finset.sum_le_card_nsmul plus polynomial coefficient/evaluation normalization are existing blocks, not an established direct diagonal estimate. New assessment helpers are not mathlib replacements.

Completed `Roth.natDegree_diag_le`: aeval_natDegree_le in RingTheory/Polynomial/Basic:898 is broader substitution theorem; totalDegree_le_degrees_card, sum_count_eq_card, sum_le_sum and degreeOf_def derive its premise. No old-form <=3-call term established.

Completed `Roth.eval_diag`: NO-mathlib-has-it: MvPolynomial.comp_aeval_apply, Mathlib/Algebra/MvPolynomial/Eval.lean:612; hom_eval₂:198, map/eval/aeval transport.

Completed `Roth.diag_sub`: Existing map_sub (generated additive theorem of map_div) already proves this with weaker generic homomorphism assumptions.

Completed `Roth.geom_sum_le_one_add_pow`: Five actual methods on three forms; positive Commute.add_pow, Nat.choose_pos, Nat.mono_cast, sum and order primitives; related Bernoulli/geometric results differ.

Completed `Roth.sum_box_prod_pow_le_aux`: Finset.prod_univ_sum factors the rectangular sum; ordered finite product and nonnegative scalar monotonicity combine the separately assessed geometric bound. Full public contribution search n/a under private prefilter.

Completed `Roth.abs_eval_le`: Prefer eval₂ and existing size-hom classes. AbsoluteValue.eval_mvPolynomial_le is a homogeneous/coefficient-l1/sup bound, not the rectangular common-coefficient bound. GaussNorm estimates concern weighted coefficient suprema, not arbitrary real evaluation.

Completed `Roth.degreeOf_det_hasseDeriv_le`: Existing degreeOf_sum_le, degreeOf_C_mul_le, degreeOf_prod_le and det_apply' supply proof steps, not ≤3-call replacement. Closest natDegree_det_X_add_C_le is affine univariate matrix only.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Matrix.det_le requires multiplicative AbsoluteValue; coefficient length is submultiplicative RingSeminorm. Polynomial.hasseDeriv_coeff is univariate. Finsupp and Finset size inequalities supply steps, not a≤3-call replacement.

Completed `Roth.genWronskian`: Matrix.det and detRowAlternating are outer building blocks; Polynomial.wronskian is pairwise univariate; Polynomial.hasseDeriv univariate. All5 search methods/current,standard,abstract forms run; external/local-index completeness caveats retained.

Completed `Roth.kronecker`: Exact positive existing MvPolynomial.aeval; aeval_monomial and eval₂Hom native checked; unrelated Matrix.kronecker, expand, bind₁ and finSuccEquiv not mistaken for target.

Completed `Roth.kroneckerExp`: Exact positive Finsupp.weight in Mathlib/Data/Finsupp/Weight.lean, weight_eq_sum bridge; underlying Finsupp.linearCombination read and native checked. Five actual search methods on current/standard/abstract; abstract dotted Loogle failure retried successfully, local index unavailable honestly recorded.

Completed `Roth.kronHasse`: A pointwise composition: take one project multivariate Hasse derivative, then project Kronecker substitution. It provides generators for the polynomial-module span. Existing function composition is sufficient for the interface; this prefilter does not assign a separate public contribution verdict. The named private operator and the span have distinct roles.

Completed `Roth.kronSpan`: Existing Submodule.span takes the image of the private substituted Hasse operators whose total order is at most the bound. It organizes the derivative-stability induction and finite span witness. The span and its individual operator generators have distinct roles; no duplicate definition or new instance is introduced.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: det_eq_zero_of_not_linearIndependent_cols + restrict_scalars' + of_comp + LinearMap.pi gives a checked four-call bridge; prebundled map needs three.

Completed `Roth.kronecker_monomial`: All five actual methods on current/standard/abstract forms; pinned aeval_monomial Eval.lean681 is the analogous law for re-aimed parent aeval. Independent map_eq/exp_eq bridges and original-form proof pass.

Completed `Roth.kroneckerExp_injOn`: All5 actual methods on current, standard and weight forms. Nat.injOn_ofDigits is existing list theorem, not the analogous weight theorem. Fresh weighted exact? fails without timeout; searches do not prove absence.

Completed `Roth.coeff_kronecker`: Finsupp.mapDomain_apply' supplies exact abstract coefficient transport; new nondefinitional aeval/mapDomain normalization bridge verified in arbitrary CommSemiring.

Completed `Roth.kronecker_eq_zero_iff`: exact abstract: Finsupp.mapDomain_injOn; alternative: Finsupp.mapDomain_support_of_injOn; normalization: Newly proved weighted aeval/mapDomain bridge; not existing replacement; automatic parent gate: aeval analogous law not established; no blanket NO

Completed `Roth.linearIndependent_kronecker`: existing: LinearIndependent.map_injOn, LinearMap.linearIndependent_iff_of_injOn, AddMonoidAlgebra.supported, AddMonoidAlgebra.mem_supported, Submodule.span_le, Finsupp.mapDomain_injOn; limit: Exact final transport exists, but specialized span-injectivity premise still requires new108–110 proofs. map′ global injectivity is false in two variables.

Completed `Roth.derivative_aeval`: Univariate Derivation.map_aeval and comp_aeval_eq are near misses. MvPolynomial.derivation_ext/mkDerivationEquiv classify derivations but do not state evaluated partial-sum law. Kaehler coordinate theorem requires further pullback/reconstruction.

Completed `Roth.derivative_kronHasse_aux`: This function-valued derivative identity follows pointwise from the project chain rule and the partial/Hasse commutation identity. It supplies the next-order generators in the bounded-span induction. Existing function extensionality and pointwise sums/scalars express the interface; there is no new definition, instance or coercion. It is a live internal recurrence, not a duplicate of the scalar chain rule. The public contribution verdicts of its ingredients remain separate.

Completed `Roth.derivative_mem_kronSpan`: Submodule.span_induction is the existing organizing API. The generator case uses the preceding private derivative recurrence and the bound on total Hasse order; the scalar case uses the polynomial Leibniz rule and inclusion of the old bounded span in the next one. This lifts a generator identity to closure of the whole polynomial-coefficient span. It is distinct from both the generator recurrence and the subsequent Hasse-iteration result. No new definition, class or instance is needed.

Completed `Roth.hasseDeriv_kronecker_mem`: Induction on the univariate Hasse order uses the order-zero span generator and the preceding derivative-span closure. Polynomial.hasseDeriv_comp relates the next Hasse derivative to differentiation, and characteristic zero makes the natural successor scalar invertible in the field. This is a live bridge from ordinary derivative closure to Hasse derivative span membership, not a duplicate of either preceding lemma. Existing span and scalar-restriction APIs supply the interface; no new class or instance is installed.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Polynomial.hasseDeriv_comp is operator composition, not substitution; Finsupp span/extraction API supplies coefficients only after substantive membership. Analytic Faà di Bruno and univariate Taylor API are partial matches.

Completed `Roth.det_sum_rows`: MultilinearMap.map_sum_finset and map_smul_univ provide abstract mathematical content; detRowAlternating supplies determinant witness; explicit normalization bridge checked. One-shot weighted determinant simpa fails, abstract weighted simpa succeeds.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: The supplied uniform derivative-row expansions substitute into the Wronskian matrix. The existing project det_sum_rows helper expands its determinant by row multilinearity, while AlgHom.map_det transports each chosen generalized Wronskian through Kronecker substitution. This is a live application bridge, distinct from the standalone determinant identity and the final nonvanishing theorem. It adds no structure or instance; its private status is appropriate to the project-specific transport.

Completed `Roth.exists_genWronskian_ne_zero`: Pinned pairwise Polynomial.Wronskian TODO explicitly requests n-tuples. Generic matrix determinant nonvanishing and Jacobian criteria do not select bounded derivative rows from coefficient-field independence. All five search methods executed on three forms.

Completed `Roth.sqrt_one_sub_inv_lt`: Real.sqrt_one_add_le supplies the standard tangent estimate; Real.sqrt_lt' and reciprocal comparison supply proof blocks. No ≤3-call exact threshold derivation verified.

Completed `Roth.inv_add_inv_le`: The two reciprocal denominators are positive under the real interval bounds. Existing inv_add_inv and div_le_div_iff reduce the estimate to the nonnegative product x*(2-x). This paired endpoint bound feeds the reflected finite-sum argument, and is distinct from the square-root threshold and the full reciprocal-sum estimate. No new structure or instance is needed.

Completed `Roth.sum_inv_le`: The preceding private complementary-pair bound is summed over the finite grid. Finset.sum_range_reflect identifies the reflected grid sum with the original one, and ordinary finite-sum distribution and arithmetic divide the resulting estimate by two. This upgrades the pointwise pair estimate to the whole reciprocal grid sum, without duplicating the public strict square-root bound.

Completed `Roth.sum_inv_lt`: All five methods on current, convex-endpoint literature and abstract symmetric-pair forms; local index unavailable. Pinned convexOn_zpow, chord and reflection APIs provide partial blocks; no existing ≤3-call replacement established. Three exact? failures not treated as absence proof.

Completed `Roth.extend_apply_castSucc`: Embedding a finitely supported vector along the injective Fin.castSucc map preserves each old coordinate. The added singleton at Fin.last has zero contribution at every castSucc coordinate. Finsupp.mapDomain_apply_of_injective and simplification prove the formula. This complements the last-coordinate helper and supports the filtered-box fiber bijection; it registers no instance or coercion.

Completed `Roth.extend_apply_last`: The image of Fin.castSucc excludes Fin.last, so the embedded finitely supported vector evaluates to zero there. The singleton contributes exactly its stored natural value. Finsupp.mapDomain_of_notMem_range and simplification prove the formula. This complements the castSucc-coordinate helper and supplies the last-coordinate requirement in the filtered-box fiber bijection.

Completed `Roth.card_filter_box_fiber_aux`: Finset.card_bij compares the smaller filtered box with the fixed last-coordinate fiber. Extension preserves all old coordinates and sets the last to i; the bound hi ensures membership. Injectivity follows by restriction to castSucc coordinates. Surjectivity reconstructs the smaller vector with Finsupp.equivFunOnFinite and proves its extension equals the original by Fin.lastCases. This is the geometric fiber-identification step; the public cardinality theorem separately sums the fibers.

Completed `Roth.card_filter_box_last`: Generic fibre theorem exact; filtered-product law closes by card_filter/sum_product simp. Existing snoc cardinality restricts predicate to init, so not exact arbitrary-p duplicate. All5methods on3forms retained.

Completed `Roth.filter_weight_le_eq_empty`: The threshold (m-lambda)/2 is strictly negative when lambda exceeds the dimension. Every natural exponent vector has nonnegative weight, even if some coordinate bounds vanish. Finset.filter_eq_empty_iff and weight_nonneg reduce each hypothetical member to an arithmetic contradiction. This handles the empty tail regime in the main lattice estimate; it is distinct from its small-lambda cardinality bound and inductive step.

Completed `Roth.card_filter_fiber_eq`: Weight additivity, injective mapDomain transport and singleton evaluation split the extended vector weight into the smaller-vector contribution plus i/r_last. An affine rearrangement moves that last-coordinate contribution into the shifted lambda parameter. Finset.filter_congr identifies the predicates before cardinalities are cast to real numbers. No denominator positivity is required for this rearrangement; all box bounds and last coordinates may be zero.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: A filtered box has cardinality at most the whole box by Finset.card_filter_le. card_box supplies the product of side cardinalities. Positive lambda and lambda at most twice the square root of the dimension make the requested prefactor at least one, so multiplying the nonnegative box cardinality gives the bound. This is the direct small-lambda regime, separate from the negative-threshold empty case and the large-lambda induction.

Completed `Roth.card_filter_weight_le_succ_aux`: Count by the last-coordinate fibers, rewrite each weighted predicate with the shifted lambda, and apply the full smaller-box induction hypothesis at each positive shifted parameter. Factor out the smaller-side product and use the harmonic reciprocal-grid estimate sum_inv_lt with positive last side and dimension at least two. Splitting the full product along Fin.castSucc and Fin.last cancels the square-root and side factors. This is the large-lambda inductive case, distinct from the direct small-lambda bound and empty-tail case.

Completed `Roth.card_filter_weight_le`: Five actual methods on current/literature/probability forms; generic cardinality and Chebyshev/variance/uniform APIs are partial matches. Pinned positive signatures and named Chebyshev application checked, no complete original specialization claimed. Bounded exact? nonclosure is not absence proof.

Completed `Roth.index`: existing: AddMonoidAlgebra.infDegree; other positive: MvPowerSeries.weightedOrder; weight: Finsupp.weight; translation: MvPolynomial.aeval; representation bridge: Finite infimum with WithTop and default zero; not definitional equality.; methods: Finder, Loogle, LeanSearch, rg, lean_local_search

Completed `Roth.mem_support_taylor_iff`: A multi-index lies in the Taylor support exactly when its Taylor coefficient is nonzero. mem_support_iff gives the coefficient criterion, and coeff_taylor identifies that coefficient with evaluation of the Hasse derivative. The private bridge is the common support-to-derivative interface for the index bound, attainment, lower-bound characterization and degree estimate. It is distinct from the quantitative inequalities it supports and requires no finite variable-type instance.

Completed `Roth.index_le_weight`: verdict: NO-mathlib-has-it; reaim parent: AddMonoidAlgebra.infDegree; analogous law: Finset.inf_le; projection: WithTop.untopD_le; premise: Finsupp.mem_support_iff; verified native: True

Completed `Roth.exists_weight_eq_index`: verdict: NO-mathlib-has-it; reaim parent: AddMonoidAlgebra.infDegree; analogous law: Finset.exists_mem_eq_inf; premise: nonempty coefficient support; verified native: True

Completed `Roth.le_index_iff`: Finset.le_inf_iff, generated dual at Data/Finset/Lattice/Fold.lean:99, is the exact analogous law for infDegree; Finset.le_inf'_iff at557, coe_inf', untopD_coe and coeff_taylor bridge the old spelling.

Completed `Roth.index_nonneg`: Finite-inf lower-bound introduction Finset.le_inf_iff.mpr already supplies the analogous nonnegativity law on infDegree under support-local nonnegative degrees; Real.sInf_nonneg is exact order-theoretic engine of old proof. Finset.le_inf′_iff, coe_inf′ and WithTop.untopD_coe/top preserve zero-default projection.

Completed `Roth.index_eq_zero_iff`: existing: Finset.inf_eq_bot_iff on AddMonoidAlgebra.infDegree; native: isolated abstract/general real laws; actual parent bridge; nonnegative NNReal recoding; bounded actual replacement; full Index consumer replay; old form call count: more than3 including normalization and project API; not claimed mathlib-only one-call; abstract call count: one finite-inf criterion plus exists_eq_right and Finsupp.mem_support_iff normalization

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: infDegree, weightedOrder and finite infimum APIs exist, but no existing derivative-shift law identified. Univariate natDegree_hasseDeriv_le bounds maximum degree, not vanishing minimum. Twelve actual formal-method requests and pinned rg searches.

Completed `Roth.le_index_sum`: supDegree_sum_le with B:=OrderDual T is definitionally the finite-infDegree sum law (one existing call); Finset.le_inf_iff and trans give a common lower bound. Five actual methods on current, literature and abstract forms; positive candidates verified at pin.

Completed `Roth.weight_eq_finsuppWeight_div`: Finsupp.apply_linearCombination R f w d is existing generic naturality; independently checked cast/scaling specializations and actual denominator bridge.

Completed `Roth.index_eq_weightedOrder_div`: Existing infDegree and weightedOrder are canonical support-minimum constructions; no analogous coe comparison found across five methods×three forms. Native exact?/definition-simp closure probes fail, independent new proof succeeds.

Completed `Roth.index_mul`: Existing MvPowerSeries.weightedOrder_mul verified in isolation at Semiring/NoZeroDivisors generality, arbitrary σ and natural weights. AddMonoidAlgebra.le_infDegree_mul is only an inequality; supDegree_mul additionally requires injective degree. Real-weight component/decomposition infrastructure exists but no analogous general real-weight equality was established.

Completed `Roth.index_prod`: Existing MvPowerSeries.weightedOrder_prod independently verified over arbitrary σ, CommSemiring R, NoZeroDivisors R and Nontrivial R, natural weights, including zero factors. Coercion of polynomial products via coeToMvPowerSeries.ringHom and map_prod verified. Generic infDegree product equality for arbitrary real noninjective weights was not established. Fresh145 isolated IsWeightedHomogeneous.prod signature confirms AddCommMonoid weight target M and CommSemiring coefficients; this closure theorem is not an extremal component identity.

Completed `Roth.index_neg`: Existing AddMonoidAlgebra.supDegree_neg on OrderDual gives exact infDegree negation law. Independent isolated Ring/semilatticeinf/top and projected proof compiled.

Completed `Roth.index_C_mul`: Reaimed infDegree scalar law is core congrArg applied to existing Finsupp.support_smul_eq; independently compiled explicit existing-call term and canonical133 bridge transport.

Completed `Roth.index_mul_left_weights`: map_finset_inf (Data/Finset/Lattice/Fold.lean:93 generated dual) on generic infDegree; Real.sInf_smul_of_nonneg (Basic/Real/Pointwise.lean:41); complete five methods on three forms.

Completed `Roth.index_rename`: NO-composable-from-mathlib on canonical parent infDegree: exact two-call composition support_rename_of_injective + Finset.inf_image; weight normalization via linearCombination_mapDomain and centers via aeval composition. Bridge is not definitional.

Completed `Roth.index_le_card`: All five actual search methods on current/literature/abstract forms. Finset.inf_le exactly supplies canonical witness upper bound; csInf_le, finite-image boundedness, monomial_le_degreeOf, sum_le_sum and div_le_one_of_le₀ are building blocks. Full Taylor-degree/cardinality bound not located.

Completed `Roth.index_unique`: verdict: NO-mathlib-has-it; reaim: Polynomial.rootMultiplicity_eq_natTrailingDegree; path: Mathlib/Algebra/Polynomial/RingDivision.lean:133; methods: Finder, Loogle, LeanSearch, rg, local; old form existing call count: Not <=3; genuine representation normalization required; normalized form existing call count: 1; bridge: Independently checked minimumSupport/taylorMinimum/trailingInf/rootInf/realInfSupport/realRootInf; these are new bridge proofs, not existing declarations.

Completed `Roth.coeffNone`: verdict: NO-composable-from-mathlib; building blocks: MvPolynomial.optionEquivLeft, Polynomial.coeff; modern: Polynomial.lcoeff, Finsupp.comapDomain; calls: 2; formal methods: Finder, Loogle, LeanSearch, rg, local; current, literature, modern and supplementary pullback forms

Completed `Roth.eq_mapDomain_some_add_single`: canonical: Finsupp.optionElim_some; building blocks: Finsupp.optionElim_some, Finsupp.update_eq_add_single, Finsupp.embDomain_some_none; representation: Finsupp.embDomain_eq_mapDomain; old form existing calls: 4; embedding form existing calls: 3

Completed `Roth.coeff_X_none_pow_mul_rename`: The product of a pure power of the distinguished variable and a polynomial in the remaining variables has coefficients selected by the distinguished exponent. The proof moves through optionEquivLeft, computes the univariate monomial coefficient, and returns to the original exponent coordinates. This is a private computational interface for the subsequent coefficient-family expansion; it is distinct from the full expansion and determinant theorems.

Completed `Roth.coeff_coeffNone`: canonical: MvPolynomial.optionEquivLeft_coeff_coeff; canonical path: Mathlib/Algebra/MvPolynomial/Equiv.lean:610; canonical existing calls: 1; old form existing calls: 4; old form ingredients: MvPolynomial.optionEquivLeft_coeff_coeff, Finsupp.update_eq_add_single, Finsupp.embDomain_some_none, Finsupp.embDomain_eq_mapDomain; representation: optionElim versus mapDomain some + single none is propositional normalization, not definitional equality; abstract: Finsupp.comapDomain_apply at Mathlib/Data/Finsupp/Basic.lean:517

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: canonical: Polynomial.as_sum_range_C_mul_X_pow'; canonical path: Mathlib/Algebra/Polynomial/Degree/Support.lean:93; canonical existing calls: 1; degree bridge: MvPolynomial.natDegree_optionEquivLeft; old form existing calls: >3 named ingredients plus genuine normalization proof; not NO-composable; old form ingredients: Polynomial.as_sum_range_C_mul_X_pow', MvPolynomial.natDegree_optionEquivLeft, MvPolynomial.optionEquivLeft, MvPolynomial.optionEquivLeft_symm_X, Polynomial.aevalTower_C, map_sum, map_mul, map_pow, mul_comm; representation: Inverse C/rename and finite sum transport are actual checked proofs, not definitional old-form equality.

Completed `Roth.degreeOf_coeffNone_le`: structural building blocks: MvPolynomial.degreeOf_le_iff, MvPolynomial.monomial_le_degreeOf, MvPolynomial.mem_support_coeff_optionEquivLeft; normalization: Finsupp.optionElim_apply_eq_elim, Option.elim_some; finite analog: MvPolynomial.degreeOf_coeff_finSuccEquiv; finite analog path: Mathlib/Algebra/MvPolynomial/Equiv.lean:834; old form calls: 3 structural calls plus nondefinitional projection rewrite; >3 named dependencies; canonical form calls: Same proof and normalization after replacing coeffNone with Polynomial.coeff of optionEquivLeft; search limitations: Local source search positive but index unavailable; external snapshots may differ. No absence claim inferred from empty queries.

Completed `Roth.coeff_rename_mul_aeval`: existing core: Polynomial.coeff_C_mul, Polynomial.coeff_map, AddMonoidAlgebra.coeff_mul_single_zero; coordinate transport: MvPolynomial.optionEquivLeft_coeff_coeff, Finsupp.update_eq_add_single, Finsupp.embDomain_some_none, Finsupp.embDomain_eq_mapDomain, MvPolynomial.optionEquivLeft_X_none, Polynomial.aeval_algHom_apply, Polynomial.aeval_X_left_eq_map; methods: Finder, Loogle, LeanSearch, rg, local; forms: current, standard, abstract; limits: Initial current Loogle query rejected unknown MvPolynomial.coeff; successful quoted-coeff retry empty. Local index unavailable with source fallback hits, no absence claim. External revisions differ from pinned source.

Completed `Roth.aeval_X_eq_rename`: verdict: NO-mathlib-has-it; existing: Polynomial.toMvPolynomial_eq_rename_comp; path: Mathlib/Algebra/MvPolynomial/Equiv.lean:891; proof: AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f; five methods all three forms: True; local index: unavailable; positive lexical fallback, not absence; pinned native positive: True

Completed `Roth.hasseDeriv_rename_mul_aeval`: verdict: YES-but-generalise-first; cells: 15; partial hits: Polynomial.hasseDeriv_mul, Polynomial.hasseDeriv_map, Polynomial.hasseDeriv_coeff, Polynomial.toMvPolynomial_eq_rename_comp, Polynomial.taylor_mul, Polynomial.taylor_coeff; note: All multivariate Hasse names in the project namespace originate in Roth/HasseDeriv.lean; pinned mathlib supplies univariate API only. Missing multivariate guard compiled in isolated mathlib environment.

Completed `Roth.coeff_uniqueAlgEquiv_symm`: existing: MvPolynomial.coeff_uniqueAlgEquiv_symm; file: Mathlib/Algebra/MvPolynomial/Equiv.lean:115; auxiliary: Finsupp.single_eq_same, Finsupp.unique_single; search: 15 method/form cells plus a repaired Loogle query and rate-limit retry; pinned exact signatures and specialization compiled without Roth imports.

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: verdict: BORDERLINE-needs-human; existing canonical law: MvPolynomial.degreeOf_eq_natDegree; other hits: MvPolynomial.natDegree_optionEquivLeft, MvPolynomial.coeff_uniqueAlgEquiv_symm, Polynomial.natDegree_map_eq_of_injective, MvPolynomial.C_injective, MvPolynomial.degreeOf_eq_sup, Polynomial.supDegree_eq_natDegree; exact target located: False; new bridge required: True; cells: 15; local index: unavailable; source hits checked natively

Completed `Roth.degreeOf_rename_mul_aeval`: verdict: BORDERLINE-needs-human; positive candidates: MvPolynomial.degreeOf_mul_eq, MvPolynomial.degreeOf_rename_of_injective, Polynomial.toMvPolynomial_eq_rename_comp, Polynomial.toMvPolynomial_injective, MvPolynomial.degreeOf_C_mul; search cells: 15; canonical bridge: Actual mathlib aeval/rename bridge replaces Roth.aeval_X_eq_rename; independent-degree normalization remains proof.

Completed `Roth.degreeOf_none_rename_mul_aeval`: All15 methods/forms executed; canonical natDegree_optionEquivLeft, Polynomial.natDegree_C_mul, natDegree_C_mul_of_mul_ne_zero and injective coefficient map degree verified.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: A vanishing linear combination gives one coefficient identity for each member of the spanning family. The corresponding weighted sum of basis coordinate functionals vanishes on that family, hence on its span by LinearMap.ext_on; evaluating on each basis vector forces every scalar coefficient to vanish. This is a live private linear-algebra component of the separated representation, distinct from the basis-existence and polynomial reconstruction helpers.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: Expand each coefficient polynomial in the chosen basis using Module.Basis.sum_repr, substitute into the given coefficient expansion, interchange the finite sums and normalize aeval, renaming and scalar multiplication. This reconstruction identity is distinct from coordinate-polynomial independence and from choosing a bounded basis.

Completed `Roth.exists_coeffNone_basis_aux`: The finitely many coefficient polynomials span a finite-dimensional space. Nonzero input forces at least one nonzero coefficient and thus positive finrank; finrank_range_le_card gives the upper bound. The span lies in a support-restriction submodule by coefficient-support transport, so every basis vector inherits the individual degree bounds. This basis-selection helper is distinct from reconstruction and coordinate-family independence.

Completed `Roth.exists_separated_representation`: formal search cells: 15; supplementary pid cells: 5; existing candidates: Module.finBasis, Module.free_of_finite_type_torsion_free', TensorProduct.exists_sum_tmul_eq, TensorProduct.eq_repr_basis_left, TensorProduct.eq_repr_basis_right, Matrix.exists_rank_normal_form; conclusion: Complete mathlib-only unconditional PID proof, complete rational caller and conditional free-span proof verified; existing finite/free/tensor/rank primitives still require substantive coordinate/degree reconstruction.

Completed `Roth.det_hasseDeriv_separated`: All15 cells executed. Pinned Matrix.det_mul, Matrix.det_transpose and AlgHom.map_det cover only the determinant core; isolated exact generic composition compiles. Binary Polynomial.wronskian and univariate hasseDeriv_mul do not replace the arbitrary-family mixed-variable theorem. Local symbol index unavailable; no universal absence claim.

Completed `Roth.exists_sum_mul_eq_gcd`: existing: Finset.gcd_eq_sum_mul; path: Mathlib/RingTheory/PrincipalIdealDomain.lean:233; normalization: eq_comm, mul_comm; verified: mathlib-only original/generic statements and full sole caller

Completed `Roth.exists_nat_smul_eq_map`: methods: 15; existing: IsLocalization.exists_integer_multiple, IsLocalization.exist_integer_multiples, MvPolynomial.isLocalization; exact replacement: Verified with genuine positivity/cast/scalar normalization; not ≤3 existing calls.; local index: unavailable; not absence evidence

Completed `Roth.exists_primitive_smul_eq`: verdict: YES-but-generalise-first; fifteen actual search cells: True; building blocks: Finset.extract_gcd, Finset.gcd_eq_zero_iff, MvPolynomial.isLocalization, IsLocalization.exists_integer_multiple, IsFractionRing.injective; near misses: Polynomial.primPart/content/IsPrimitive concern univariate polynomials., IsFractionRing.exists_reduced_fraction concerns one fraction., Projectivization.exists_smul_eq_mk_rep does not enforce integral gcd1 coordinates.; composition: No verified ≤3-existing-call composition; polynomial reconstruction, mapped-scalar normalization and support-gcd transport remain genuine proof.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: actual search cells: 15; forms: current, standard, abstract; positive candidates: Finset.gcd_eq_sum_mul, Submodule.mem_of_span_top_of_smul_mem, Submodule.smul_mem_iff_of_isUnit, IsLocalization.IsInteger, IsLocalization.isInteger_smul; exact replacement: False; bridge: Finite gcd to submodule membership is a newly proved linear-combination bridge; existing unit-ideal law has a different premise.

Completed `Roth.rescale_separated_factor_aux`: Use the given scalar rescaling, move constant polynomials through coefficient renaming and polynomial evaluation, commute the four factors, and cancel the scalar with its inverse using the nonzero hypothesis. This scalar compensation identity is distinct from coefficient integrality and degree preservation, and is used by exists_int_factors.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: For each univariate coefficient, coeff_rename_mul_aeval identifies its products with the primitive factor coefficients as integer coefficients of the given product. exists_int_eq_of_gcd_eq_one then gives an integer witness for each coefficient, and Polynomial.mem_map_range assembles the integer polynomial. This coefficient descent is distinct from scalar compensation and from choosing a primitive representative.

Completed `Roth.exists_int_factors`: status: Partial Gauss/localization/reduced-GCD matches, no full target or ≤3-call proof verified.; existing: Polynomial.IsPrimitive.map_mul_mem_lifts_iff, Polynomial.IsPrimitive.mul_map_mem_lifts_iff, Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map, IsLocalization.surj_of_gcd_domain, MvPolynomial.isLocalization; search forms: current, standard, abstract; all five methods executed: True; index caveat: Local index unavailable; fallback hits include scratch project proofs, external versions can differ.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: Map the polynomial injectively to the rationals, apply exists_separated_representation, choose bounded derivative indices using exists_genWronskian_ne_zero, and factor the resulting determinant by det_hasseDeriv_separated. Independent univariate factors give wronskian_ne_zero_of_linearIndependent, while hasseDeriv_map transports the determinant back to the mapped integer determinant. This rational factor construction is distinct from the subsequent integer factor descent.

Completed `Roth.exists_det_eq_mul`: 15 actual search cells; positive univariate Hasse/binary Wronskian/matrix determinant/localization/degree-map building blocks inspected and native checked; no verified ≤3 existing-call replacement. Index unavailable is recorded, not absence.

Completed `Roth.RSet`: methods: 5; forms: 3; cells: 15; verified candidates: MvPolynomial.restrictSupport, MvPolynomial.mem_restrictSupport_iff, MvPolynomial.basisRestrictSupport, MvPolynomial.restrictSupport_add, MvPolynomial.mem_restrictDegree, MvPolynomial.degreeOf_le_iff; limitations: Online revision may differ. Local search reports index unavailable. No complete ≤3 existing-call replacement verified.

Completed `Roth.indexSet`: methods: 5; forms: 3; cells: 15; verified candidates: Set.image2, Set.mem_image2, Set.mem_image2_of_mem, Set.Nonempty.image2, Set.image2_nonempty_iff, Set.image2_subset, Set.forall_mem_image2, Set.image2_congr', AddMonoidAlgebra.infDegree; limitations: Initial standard Loogle sSup query rejected and corrected with SupSet.sSup. Local target index unavailable. Remote indexes may differ from pinned signatures.

Completed `Roth.Θ`: methods: 5; forms: 3; cells: 15; verified candidates: SupSet.sSup, le_csSup, csSup_le, csSup_le_csSup, Real.sSup_nonneg, Real.sSup_le, Real.sSup_empty, Real.sSup_of_not_bddAbove, sSup_image2, csSup_image; limitations: Local symbol index unavailable; online snapshots may differ. Complete-lattice sSup_image2 is not usable directly on real totalized suprema; negative instance guard verifies this.

Completed `Roth.lem6M`: Five methods on current/standard/abstract forms; arithmetic primitives confirmed; no identified existing parameterized bound.

Completed `Roth.lem6Φ`: All15cells; positive generic Add.add(sSup A)(sSup B) exactly3outercalls; expanded arithmetic inputs have morecalls and are not mislabeled.

Completed `Roth.one_mem_RSet`: All15 search cells; pinned degreeOf_one, coeff_one, coeff_one_zero, one_ne_zero, Nat.zero_le, abs_one/zero. Full family not replaced by univariate root or height results. Closing simp is SIMP-COMPOSABLE; no strict≤3existing-call term verified.

Completed `Roth.indexSet_nonempty`: All15 method×form cells: Set.Nonempty.image2 and Set.image2_nonempty_iff independently native verified; local index unavailable disclosed.

Completed `Roth.indexSet_bddAbove`: Set.forall_mem_image2 gives one-call structural predicate transport; constructor yields BddAbove from supplied uniform bound. BddAbove.image2 rejected because monotonicity and bounded ordered source premises differ. No full existing arithmetic theorem established.

Completed `Roth.index_le_Θ`: Pinned le_csSup exactly supplies the abstract membership-to-supremum law; Set.mem_image2_of_mem independently verifies image2 membership.

Completed `Roth.Θ_nonneg`: law: Real.sSup_nonneg; parent: SupSet.sSup; pointwise: Real.sInf_nonneg, Finset.sum_nonneg, div_nonneg, Nat.cast_nonneg; family transport: Set.forall_mem_image2.mpr; defaults: Real.sSup_empty, Real.sSup_of_not_bddAbove; status: 15 search cells and five clean native sets

Completed `Roth.Θ_le_card`: Five actual methods on current, literature and abstract forms. Real.sSup_le exactly covers supremum transport and Set.forall_mem_image2 covers quantifier transport. weightedOrder_le and polynomial degree lemmas are partial building blocks; full degree-normalized uniform bound still uses project index_le_card.

Completed `Roth.Θ_le_of_forall_index_le`: NO-mathlib-has-it: independently verified csSup_le at the exact sSup parent. Old representation uses one mathlib call plus one project nonempty helper and logical witness transport; parent helper is not counted as a mathlib block.

Completed `Roth.Θ_mono`: existing: csSup_le_csSup; path: Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:209; isolated verified: True; bridge: Θ = sSup indexSet is definitional; height-family inclusion is a new explicit project-specific proof, verified separately.; project helpers not mathlib blocks: Roth.indexSet_bddAbove, Roth.indexSet_nonempty

Completed `Roth.indexSet_comp_subset`: Rename the polynomial, transport nonvanishing through injective renaming, degree bounds through the variable equivalence, and coefficient bounds through surjectivity of exponent mapDomain. Compose the numerator vector with the inverse equivalence, preserve its coprimality, then use index_rename and map_rename to identify index values. This is a live private transport component of Θ_equiv, distinct from the final two-sided equality of suprema.

Completed `Roth.Θ_equiv`: Existing congrArg and SupSet Equiv.iSup_congr cover the outer layer. renameEquiv, degreeOf_rename_of_injective, coeff_rename_mapDomain and mapDomain_surjective cover individual transport pieces; full bounded-family preservation still requires new verified glue.

Completed `Roth.isPrimitive_linear`: A scalar dividing every polynomial coefficient divides both the constant coefficient -h and the linear coefficient q. Coprimality forces this scalar to be a unit. This primitive linear-factor fact feeds Gauss descent in exists_eq_pow_mul_of_rootMultiplicity; it is distinct from closure of primitive polynomials under powers.

Completed `Roth.isPrimitive_pow`: Induct on the exponent: the constant polynomial one is primitive, and a successor power is a product of primitive polynomials. This multiplicative closure helper combines with primitive qX-h for the Gauss descent argument. It is distinct from proving that particular linear polynomial primitive.

Completed `Roth.exists_eq_pow_mul_of_rootMultiplicity`: 15 actual method/form cells; partial hits Polynomial.pow_rootMultiplicity_dvd, Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map and integer iff. Pinned native signatures supersede stale Finder/LeanSearch signatures. Default-limit exact? and wildcard failures are rejected search evidence, never absence proofs.

Completed `Roth.pow_rootMultiplicity_le`: Related pow_rootMultiplicity_dvd, Gauss descent, leadingCoeff_dvd_leadingCoeff, den_dvd_of_is_root and Int.natAbs_le_of_dvd_ne_zero verified; no exact retrieved replacement.

Completed `Roth.index_unique_le_log_div`: Identify the one-variable polynomial after injective integer-to-real mapping, transport root multiplicity from rational to real coefficients, and rewrite the unique-variable index as multiplicity divided by its natural weight. Apply pow_rootMultiplicity_le, take logarithms using positivity of the denominator power, then normalize log_pow and divide by positive log q and nonnegative weight. This is the live private logarithmic bridge between the denominator-power coefficient bound and the public one-variable Theta bound; it is distinct from both the algebraic factor theorem and the supremum wrapper.

Completed `Roth.Θ_unique_le`: Pinned csSup_le and log/power laws provide generic packaging; den_dvd_of_is_root only single denominator divisibility. Multiplicity-sensitive integer polynomial bound remains substantive. All five methods on three forms, pinned checks and mathlib-only order/log experiments completed.

Completed `Roth.one_le_lem6M`: Pinned one_le_mul_of_one_le_of_one_le, one_le_pow₀, Nat.factorial_pos and cast laws completely handle elementary arithmetic. List.one_le_prod and Finset.one_le_prod₀ handle the abstract product law. Exact actual formula route needs factor obligations and normalization; no strict≤3 old-form term verified. All15 search cells executed.

Completed `Roth.floor_sq_div_two_le_sum`: All five methods on current/standard/abstract forms. Pinned Gauss sum, finite sum distribution and Nat.floor_le verified. No exact existing replacement or strict three-call existing composition established.

Completed `Roth.sq_div_three_lt_floor_sq_div_two`: All15cells of five methods on current/standard/abstract forms executed. Pinned Nat floor-error/monotonicity and square-monotonicity APIs checked and used. No exact replacement or strict three-existing-call composition established.

Completed `Roth.mul_div_two_le_sum_max_aux`: Handle l=0 and nonpositive θ directly. Otherwise l>0 and l≤θr force r>0. Cast the natural Gauss identity for the sum of ν<l, bound each positive part below by its affine residual, distribute sums and divide by the positive r, then use l≤θr to finish the linear estimate. This is the short-truncation branch used both in the boundary case of mul_sq_div_three_le_sum_max_aux and in min_le_sum_max; it is not the floor-square comparison or the longer quadratic-truncation estimate.

Completed `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`: Set n to the natural floor of θr, use both floor interval inequalities, and cast the Gauss sum identity through n. An explicit nonnegative-remainder identity gives (θr)²/3≤sum(θr−ν) through n. Divide by positive r, bound affine residuals by their positive parts, and enlarge to the longer range using nonnegative summands. This bypasses the strict floor-square FACT and needs no threshold10. It supplies the strict-length branch of mul_sq_div_three_le_sum_max_aux and differs from the short-truncation lθ/2 estimate.

Completed `Roth.mul_sq_div_three_le_sum_max_aux`: If r≤0 the desired lower bound is nonpositive while every summand is nonnegative. For r>0 split θr≤l into strict inequality, handled by mul_sq_div_three_le_sum_max_of_pos_aux, and equality. At equality, use mul_div_two_le_sum_max_aux for lθ/2 and the identity l=θr to compare rθ²/3 with rθ²/2. This closes sign and boundary cases missing from the positive strict-length helper and supplies the quadratic branch of min_le_sum_max.

Completed `Roth.min_le_sum_max`: 15actual cells across current/standard/abstract forms plus qualified Loogle retries. Gauss sum, finite subset sum, min and floor/findGreatest APIs verified. No existing theorem or strict ≤3-existing-call term established; index warming is not absence.

Completed `Roth.sum_max_sub_le_index_det`: Existing det_apply′, finite sums/products, infDegree additive/product inequalities and weightedOrder laws supply primitives; no exact determinant lower estimate located. All15current/standard/abstract search cells plus5infDegree re-aim cells executed. External indexes are not pinned absence proofs.

Completed `Roth.index_separated_mul_le_aux`: Represent the univariate factor as a Unit-variable multivariate polynomial via uniqueAlgEquiv and prove membership in its scaled RSet from the degree and coefficient bounds. Injective coefficient maps and disjoint renamings preserve nonzero factors. Use index_mul and index_rename to split the product index, apply index_le_Θ to both admissible factors, then index_mul_left_weights and positivity of l clear the two divisions. This is the private separated-factor-to-extremal-index bridge used by index_det_le; it is distinct from determinant coefficient bounds and from the Hasse determinant lower estimate.

Completed `Roth.index_det_le`: 20 actual search cells: five methods on current, standard and abstract forms plus parent infDegree re-aim. Pinned Int.one_le_abs and weightedOrder_mul are ingredients, not the complete arithmetic extremal bound; local index warming/error is not absence.

Completed `Roth.weight_le_delta_aux`: If the distinguished weight is zero, the degree bound forces the exponent vector to vanish, and δ nonnegativity closes the result. Otherwise its positivity and the ratio assumption force positive complementary weights. Compare each reciprocal-weight summand using div_le_div_iff₀ and the ratio bound, sum with Finset.sum_le_sum, identify the exponent degree with Finsupp.degree_eq_sum, and finish using the degree bound. This supplies the row-order weight estimate in index_le_lem6 from the determinant derivative-degree bounds; it is distinct from determinant nonvanishing and the final scalar index inequality.

Completed `Roth.mapped_det_ne_zero_aux`: Commute the integer-to-real coefficient map through the determinant using RingHom.map_det and through every Hasse derivative using hasseDeriv_map. Injectivity of the coefficient map reduces nonvanishing to the integer determinant. Substitute the separated factorization, split the nonzero product, and use injective complementary renaming and the aeval_X_eq_rename identification with uniqueAlgEquiv to transport nonvanishing of both factors. This supplies the nonzero determinant premise of sum_max_sub_le_index_det inside index_le_lem6, independently of the row-weight and scalar arithmetic helpers.

Completed `Roth.index_numeric_bound_aux`: Split min_le_iff into a linear and quadratic branch. In the first divide by positive l and compare δ with sqrt δ via Real.le_sqrt_self_iff. In the second derive 3l≤4rp, hence θ²≤4(Φ+δ), use Real.sq_sqrt and the general square-root square identity together with nonnegative square roots to bound θ by 2(sqrt Φ+sqrt δ), and add the nonnegative Φ term. This closes the scalar real estimate in index_le_lem6 after combining determinant lower and upper bounds; it is distinct from nonvanishing and derivative-weight admissibility.

Completed `Roth.index_le_lem6`: Five actual methods on current, literature and abstract forms plus five parent-infDegree reaim searches. Existing weightedOrder multiplication and determinant absolute-value bounds are ingredients, not the complete arithmetic witness/recursive-Θ endpoint; local warming/error and one retried Loogle error are disclosed.

Completed `Roth.Θ_option_le`: 15 actual search cells across current/literature/abstract forms plus5 infDegree/weightedOrder parent reaim cells. Existing csSup_le, Real.sSup_le and Finset.le_sup'_of_le cover the order-only transport, but assume rather than prove the arithmetic pointwise rank witness. Native pinned signatures and independent transport proofs verified; external indexes are revision-distinct and local indexes warming.

Completed `Roth.factorial_coefficient_le_two_pow_aux`: Use Nat.lt_two_pow_self to bound r₁+1 by 2^r₁. Bound l factorial by l^l using Nat.factorial_le_pow, then use l≤2^r₁ and Nat.pow_le_pow_left. Multiply the nonnegative natural bounds and combine the powers with pow_mul and pow_add; polynomial exponent arithmetic gives the final exponent (2p+1)r₁l. This is the combinatorial-envelope stage of lem6M_lt, separate from the strict logarithmic comparison with q.

Completed `Roth.two_pow_lt_rpow_aux`: Positivity of p and δ makes the logarithmic threshold positive, so Real.log_pos_iff yields q>1. Use Real.log_lt_sub_one_of_pos to obtain log 2<1 and rearrange the threshold into 2p+1≤log(q)δ/p. Multiply strictly by the positive natural product l*r₁, rewrite both powers via Real.rpow_def_of_pos and compare exponents using Real.exp_lt_exp. This supplies the strict exponential stage of lem6M_lt after the separate natural factorial envelope bound.

Completed `Roth.lem6M_lt`: Fifteen actual current/standard/abstract search cells plus compiled pinned candidates. Nat.factorial_le_pow and Real log/rpow/exp laws are ingredients; Real.pow_div_factorial_le_exp has factorial in the denominator and is not a replacement. No existing exact replacement established; local index warming and external revision limits are recorded.

Completed `Roth.lem7_Φ_bound`: Fifteen actual current/standard/abstract method cells. Pinned Real.mul_rpow, exponent monotonicity, positivity and le_self_pow₀ compile. No exact replacement established; current semantic Roth hits include unrelated additive-combinatorial results. Local index warming and remote revision differences limit absence conclusions.

Completed `Roth.lem7_numeric`: 15 fresh method/form cells; pinned sqrt/rpow/order ingredients verified. No exact hit or≤3-existing-call proof established; local index warming.

Completed `Roth.theta_scaled_unique_le_aux`: First derive δ≥0 from M≥1, M≤q₁^(δlr₁), q₁>1 and positive lr₁. The balanced logarithms force q₂>1 and r₂>0. Apply Θ_mono to enlarge M, then Θ_unique_le. Rewrite Real.log_rpow, clear the positive scaled-weight logarithm, and use the balanced-log inequality. This is the singleton-factor contribution to theta_phi_lt_aux, distinct from the complementary-prefix induction.

Completed `Roth.theta_delta_succ_lt_aux`: Multiply the upper bound on δ by its positive enlargement factor. Clear the positive n+1 denominator and use one_div_mul_cancel together with the positive square of 1/(n+2) to prove the strict reciprocal gap. This ensures the enlarged error parameter fits the lower-dimensional induction threshold; no lower bound on δ is captured by this helper.

Completed `Roth.theta_prefix_lt_aux`: Use Θ_mono to enlarge the height and identify the first coordinate after Fin.castSucc and natural-weight scaling. Apply the supplied induction hypothesis at ε; verify its last-weight lower bound from the original minimum weight and l≥1, its ratios from δ≤ε, its weaker logarithmic threshold via div_le_div₀, and its balanced products after multiplication by l. This transports the complementary-variable induction stage of theta_phi_lt_aux.

Completed `Roth.theta_lt_base_aux`: Apply Θ_unique_le, compute Real.log_rpow and cancel the positive weight and denominator logarithm to obtain Θ≤δ. Use Real.rpow_le_rpow_of_exponent_ge to compare δ with its one-half power on (0,1], then multiply the positive power by the strict constant factor10. This is the base case of Θ_lt, distinct from the large-δ dimension bound.

Completed `Roth.theta_denominators_one_lt_aux`: The first weighted logarithm is positive. Its lower bound on r_j log(q_j), together with nonnegative natural r_j, forces log(q_j)>0 via pos_of_mul_pos_right. Apply Real.log_pos_iff for the nonnegative natural base and cast back to 1<q_j. This supplies denominator positivity in the singleton, successor and final index estimates.

Completed `Roth.theta_phi_lt_aux`: Derive all weights positive from antitonicity and the last-weight bound, and denominator positivity from theta_denominators_one_lt_aux. Set ε=δ(1+1/(n+2)); use one_le_lem6M and lem6M_lt for the height envelope, theta_scaled_unique_le_aux for the singleton term, and theta_prefix_lt_aux with theta_delta_succ_lt_aux for the induction term. Combine them through lem7_Φ_bound and lem7_numeric to reach the strict half-target. This is the per-rank quantitative stage used after Θ_option_le.

Completed `Roth.theta_lt_succ_aux`: Derive δ<1, antitonicity of r, positive denominators and the distinguished-coordinate ratio. Transport the variables from Fin(n+2) to Option(Fin(n+1)) using Θ_equiv and finSuccEquivLast. Apply Θ_option_le, unfold the two Φ terms and use Finset.sup'_lt_iff; theta_phi_lt_aux bounds every rank. This is the small-error successor branch of Θ_lt.

Completed `Roth.theta_lt_of_large_delta_aux`: Use Θ_le_card for the dimension bound p=n+1. Nat.lt_two_pow_self gives p²<4^p≤10^p, hence p<10^p/p. Bound 1/p by its own exponent-2^(-p) power using Real.self_le_rpow_of_le_one and then by δ to that exponent using Real.rpow_le_rpow. This handles both base and successor large-error branches of Θ_lt.

Completed `Roth.Θ_lt`: All15 actual Finder/Loogle/LeanSearch/rg/local cells on current, literature and abstract forms; external indexes revision-distinct and local warming. Pinned csSup_le/Real.sSup_le/finite strict-sup/weighted-order signatures and actual generic transports compiled. Reconstructed mathlib-only arithmetic endpoint exact? probe did not close. Supremum and weighted-support APIs do not supply its arithmetic uniform-bound premise.

Completed `Roth.lam`: Uses existing Real.sqrt (Mathlib/Analysis/Real/Sqrt.lean), HMul.hMul/HAdd.hAdd and Nat.cast. No existing equivalent named cutoff was verified. Search hits for additive-combinatorics Roth or Dioph are different mathematics. Full isolated formula construction, general scalar representation, normalization and continuity compile using mathlib only.

Completed `Roth.gam`: Real subtraction, division, Nat.cast and Real.sqrt already provide the arithmetic; sub_div supplies an arithmetic normalization identity. No exact semantic gamma hit established by the 15 search cells; local index error/warming does not establish absence.

Completed `Roth.eta`: Uses existing natural power, multiplication, division and Real.rpow. Real.rpow_mul/sqrt_eq_rpow support a new nonnegative iterated-root bridge; NNReal.coe_rpow gives a typed representation bridge. Neither representation is an existing named eta counterpart. All15 formal cells completed; external index revisions differ and local index reported error.

Completed `Roth.mainCoeffBound`: Nat.floor + Real.rpow + multiplication gives strict3 existing-operation construction; checked rfl against original and independently in mathlib-only context. Nat.floor_le/lt_floor_add_one preserve both endpoints; floor_pos and Int.le_floor cover positivity and integral coefficient transport. All15 formal cells run; local symbol index error and external snapshot differences disclosed.

Completed `Roth.boxFamily`: Finset.finsupp/card_finsupp and Finsupp.card_Iic enumerate finite coefficient products; coeffEquiv supplies representation; restrictSupport captures only the degree/support layer. New degree-box coefficient bridge is proved separately.

Completed `Roth.exists_delta_bound`: Existing ContinuousAt.eventually_lt, Real.continuousAt_rpow_const and mem_nhdsGE_iff_exists_Icc_subset cover separate stages. Full fixed-m arithmetic result is not verified as ≤3 existing calls; the complete supplied-event transport is two existing calls.

Completed `Roth.eta_lt_gam_iff`: lt_sub_iff_add_lt is the canonical additive order law. sub_div/div_sub_div_same and mul_div_cancel_left₀ give the normalized scalar version; the exact old spelling also needs coefficient and association normalization.

Completed `Roth.sqrt_lt_nat_floor_aux`: Nat.le_floor gives floorX>=2, while Nat.lt_floor_add_one bounds X<floorX+1. Together these force X<floorX squared. Apply Real.sqrt_lt' with positive floor. This is the strict lower-bound half of the public two-sided floor statement, distinct from Nat.floor_le.

Completed `Roth.sqrt_lt_floor`: Nat.le_floor/Nat.lt_floor_add_one/Real.sqrt_lt' are building blocks; Nat.floor_le supplies upper projection. No certified existing-only at-most-three-call proof of full conjunction.

Completed `Roth.four_lt_rpow`: Existing Real.lt_rpow_of_log_lt transports a supplied logarithmic bound; existing square-order, log monotonicity and quadratic exponential APIs supply primitives. No exact existing numeric premise bridge verified. All15 searches executed; local index errors and exact? timeout inconclusive.

Completed `Roth.mul_log_div_two_lt_log_mainCoeffBound`: Real.log_lt_log, Real.log_sqrt, Real.log_rpow and Real.lt_log_of_rpow_lt provide transport, not the missing root-to-natural-floor inequality. All15 formal cells checked; local index warming limits absence inference.

Completed `Roth.two_lt_rpow_aux`: The threshold forces logq>0 and the natural denominator q>=2. If delta*logq<=log2, squaring this nonnegative inequality and combining logq>=log2 contradicts the delta-squared threshold. Then multiply by the degree>=1 and apply Real.lt_rpow_of_log_lt. This establishes the positive floor-power threshold used in three_small_factors; it differs from the public four-power estimate and from comparing all three small factors.

Completed `Roth.three_small_factors`: Real.lt_rpow_of_log_lt, Real.log_pow, Real.log_rpow, Real.log_nonneg and natural floor lemmas provide constituents. All15 actual formal cells completed; local index error is a limitation. Independent full arithmetic reconstruction is a new proof, not existing mathlib API.

Completed `Roth.exists_norm_coeff_reduction_aux`: Nontriviality follows from the changed remainder. Nonmonic divisors leave P unchanged, so the divisor is monic; the same changed-remainder condition gives P nonzero and divisor degree<=P degree. Define Q by subtracting the leading monomial multiple of f. The division recursion identifies the same remainder, its well-founded degree lemma yields the strict degree drop, and coefficient formulas plus norm_sub_le/norm_mul_le give the new bound. The public coefficient-remainder theorem iterates this step by strong induction; this helper is not itself the full iterated estimate.

Completed `Roth.norm_coeff_modByMonic_le`: Existing division and norm building blocks do not supply the quantitative iteration. CoeffMem gives algebraic submodule membership, not bounds on archimedean size; GaussNorm/supNorm provide alternative representations.

Completed `Roth.boxFamily_eq_image_finsupp_aux`: Map coefficient functions through AddMonoidAlgebra.ofCoeff. In the forward direction monomial_le_degreeOf places each support exponent in Iic of the finite-support degree function. Conversely the support bound implies every coordinate degree bound, and Finset.mem_finsupp_iff gives interval bounds on box monomials; off-box coefficients vanish. This representation is shared by finiteness and exact cardinality, which then use different existing finite-set laws.

Completed `Roth.boxFamily_finite`: Finset.finsupp, Finset.mem_finsupp_iff, Finset.finite_toSet and Set.Finite.image provide enumeration and image finiteness. Set.Finite.pi' and Set.Finite.of_injOn support a newly proved semantic theorem. The project representation helper is not existing mathlib.

Completed `Roth.ncard_boxFamily`: Finset.card_finsupp, Finsupp.card_Iic, Nat.card_Iic, Int.card_Icc, Set.ncard_image_of_injective, Set.ncard_coe_finset and finprod transport are genuine mathlib. The semantic representation bridge is project/new proof. External Polynomial.card_eq_of_natDegree_le_of_coeff_le corresponds to pin Polynomial.ncard_boxPoly, a univariate result.

Completed `Roth.floor_rpow_count_lt_aux`: Real.add_rpow_le_rpow_add gives x^c+1<=(x+1)^c. Rewrite the doubled exponent as a square and use positivity of x^c, the natural-floor upper bound and the expanded square to obtain a strict gap. This is the positive scalar base estimate raised to a positive integer count in pigeonhole_count; its strictness is not the final exponent-budget comparison.

Completed `Roth.pigeonhole_count`: Existing rpow/floor/order primitives are appropriate. No exact existing replacement was verified in all15 search cells; the scalar floor helper and budget theorem in scratch are new proofs, not existing mathlib API.

Completed `Roth.exists_ne_modByMonic_eq`: Existing finite-map collision and low-degree monic remainder reconstruction verified; finite-ring polynomial collision is related but does not apply to integer interval alphabets. Complete original is not <=3 existing mathlib calls. Infinite-source finite-target collision is also already mathlib as Finite.exists_ne_map_eq_of_infinite; all five new abstract-form searches and pinned native checks confirm it. Finprod default semantics do not give a source cardinality for infinite boxFamily.

Completed `Roth.sub_mem_RSet`: Existing degreeOf_sub_le, coeff_sub, sub_ne_zero and generated ordered-group abs_sub_le_of_nonneg_of_le/abs_sub_le_of_le_of_le cover the leaves. No verified exact whole-tuple replacement.

Completed `Roth.eval_hasseDeriv_sub_eq_zero`: Existing eval₂_modByMonic_eq_self_of_root needs no monicity at this pin; aeval_eq_zero_of_dvd_aeval_eq_zero, dvd_modByMonic_iff_dvd and sub_modByMonic supply scalar leaves. Hasse transport is project API, not existing mathlib.

Completed `Roth.le_index_of_forall_eval_eq_zero`: Existing le_of_not_gt is only scalar contraposition. Finset.le_inf_iff/le_inf and AddMonoidAlgebra.infDegree already supply the abstract support lower bound; a three-call bounded-support check compiles once support⊆test-set is given. MvPowerSeries.nat_le_weightedOrder/le_weightedOrder are natural-weight/top-valued alternatives. Project Hasse/Taylor support normalization is still needed for the exact bounded derivative theorem.

Completed `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`: Pinned mul_lt_mul_iff_of_pos_right, sq_pos_of_ne_zero, mul_lt_of_lt_one_left and field_simp support the proof; no exact full implication identified by15cells/compiled exact? probe.

Completed `Roth.exists_hasseDeriv_eval_ne_zero`: NO-mathlib-has-it via re-aim: AddMonoidAlgebra.infDegree is Finset support inf; Finset.inf_lt_iff is exactly its strict-cutoff witness law. Finset.inf'_lt_iff is the real nonempty form. Taylor/Hasse and zero-default bridges remain explicit.

Completed `Roth.abs_eval_iterated_hasseDeriv_lt_aux`: Apply degreeOf_hasseDeriv_le twice, abs_coeff_hasseDeriv_le twice and abs_eval_le. Rewrite the product of identical evaluation factors with Finset.prod_pow_eq_pow_sum, replace the degree sum by s, and combine the two strict powers-of-two estimates with positive B and the non-strict evaluation-factor bound. The sole caller exists_auxiliary_polynomial_of_log_bound_aux chooses beta=B^delta, derives B>0 from a nonzero integer coefficient, and rewrites B*beta^3 as B^(1+3delta). This is an analytic height estimate, not the subsequent Hasse-derivative selection lemma.

Completed `Roth.exists_hasseDeriv_index_eval_bound_aux`: Use exists_hasseDeriv_eval_ne_zero after injectively mapping integer coefficients into the reals. Set Q=hasseDeriv k P; nonvanishing of its evaluation ensures Q is nonzero, degreeOf_hasseDeriv_le preserves coordinate degrees, and index_sub_weight_le_index_hasseDeriv controls index loss. Commute coefficient maps with Hasse derivatives to transfer the supplied double-derivative height bound. The sole main_lemma caller chooses a midpoint cutoff c between the second-point index upper bound Theta and the available first-point gap. This is a selection/transport result, distinct from the numerical estimate supplying the height bound.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`: Combine degreeOf_hasseDeriv_le with card_le_card_box to bound derivative support by the coordinate box. Apply abs_coeff_hasseDeriv_le and abs_coeff_diag_le, then norm_coeff_modByMonic_le with natDegree_diag_le; Int.norm_eq_abs and cast simplifications convert the seminormed-ring result. The sole floor-bound caller next absorbs each of the three multiplicative costs into beta and converts the real bound into an integer floor. This helper retains the precise divisor-degree exponent, unlike that coarser floor bound.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`: Derive beta>=1 from the powers-of-two bound. Bound the box product by 2^(sum r), and invoke the precise preceding coefficient estimate, absorbing the box, Hasse and remainder-elimination factors into beta. Treat divisor natural degree zero separately: monic constant is1 and has zero remainder, while nonmonic modByMonic returns the input and the zero-divisor estimate applies. Finish with Int.natCast_floor_eq_floor and Int.le_floor. The sole rpow-bound existence caller compares this floor with floor(B^c) before pigeonholing; no monicity premise is needed by this bound itself.

Completed `Roth.exists_mem_RSet_le_index_aux`: Apply exists_ne_modByMonic_eq to obtain two distinct box polynomials with matching selected remainders. Their difference belongs to RSet by sub_mem_RSet. Injectivity of the integer-to-real map preserves nonzeroness and coordinate degrees via degrees_map_of_injective; eval_hasseDeriv_sub_eq_zero and le_index_of_forall_eval_eq_zero turn remainder equality into the index lower bound. The sole rpow-bound caller supplies a filtered weight box J containing all indices strictly below the target cutoff. This is the algebraic pigeonhole-to-index step, separate from estimates proving its strict count premise.

Completed `Roth.mul_card_filter_weight_le_aux`: Split on a>0. In the positive branch use card_filter_weight_le with loss4*a*sqrt(m), multiply by a, and clear the nonzero factors using m>0 and Real.sqrt_pos before ring normalization. In the nonpositive branch the left side is nonpositive while the cardinality half is nonnegative. The sole rpow-bound existence caller chooses a=c*f.natDegree to supply the counting-budget premise of pigeonhole_count. This all-real-scale helper is stronger in scope than the positive-scale cancellation probe from the lambda assessment.

Completed `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`: Monicity gives A>=1, hence 2^s<=beta; positivity of m and the degrees gives s>0. The power budget then forces c>=1, allowing pigeonhole_count. Use the floor remainder estimate with Cn=floor(B^c), choose J as the coordinate box filtered by the centered weight cutoff, and get its budget from mul_card_filter_weight_le_aux at a=c*f.natDegree. Feed these into exists_mem_RSet_le_index_aux. The sole log-bound caller specializes c=1+3delta, B=mainCoeffBound and beta=B^delta; this general helper has no gamma or logarithmic hypotheses.

Completed `Roth.exists_mem_RSet_le_index_of_log_bound_aux`: Use monicity to obtain A>=1, degree positivity and the sum bound to obtain r1>0, and the logarithmic threshold to derive the hypothesis for four_lt_rpow. Invoke three_small_factors at alpha0 to control (1+A)^(m*r1). Rewrite B^(1+3delta)=B*(B^delta)^3 using Real.rpow_add_of_nonneg and Real.rpow_mul_natCast, prove the floor bound B positive, and invoke the rpow-budget helper. Unfold gam and lam to match its index cutoff. The sole auxiliary-polynomial caller adds evaluation control and weakens the floor coefficient bound to the real power bound.

Completed `Roth.exists_auxiliary_polynomial_of_log_bound_aux`: Obtain P and its index from the log-budget helper after dropping the nonnegative alpha logarithm term. Use three_small_factors for powers of2 and 1+abs(alpha), deduce positivity of B from a nonzero coefficient of P, and identify B*(B^delta)^3 with B^(1+3delta). Use Nat.floor_le to enlarge RSet and abs_eval_iterated_hasseDeriv_lt_aux for the uniform evaluation estimate, then linear_combination closes the power identity. The sole index-gap caller additionally bounds Theta by eta; it is not part of this helper.

Completed `Roth.theta_lt_eta_of_sq_log_bound_aux`: Write the nonzero dimension m as n+1. The positive square-log bound and delta>=0 imply delta>0; multiply through delta squared to derive the weaker logarithmic hypothesis needed by Theta_lt from delta*m<=1. Translate the last degree and adjacent ratio premises with Nat.cast_le and div_le_iff, invoke Theta_lt, and unfold eta. The sole index-gap caller first drops the nonnegative A/alpha logarithm terms. This is the numerical Theta-to-selected-eta specialization, distinct from constructing the auxiliary polynomial.

Completed `Roth.exists_auxiliary_polynomial_with_index_gap_aux`: Expose m=n+1 and infer delta>0 from the square-log threshold. The delta<=1/m and adjacent ratio bounds make the degree vector antitone using Fin.antitone_iff_succ_le; this bounds the degree sum by m*r0 and propagates positivity from the last degree. Invoke exists_auxiliary_polynomial_of_log_bound_aux and theta_lt_eta_of_sq_log_bound_aux, then linarith combines gamma<=index with Theta<eta. The sole main_lemma caller uses this strict gap to choose an intermediate cutoff before applying exists_hasseDeriv_index_eval_bound_aux. This helper does not yet guarantee rational-point nonvanishing of the final derivative.

Completed `Roth.main_lemma`: Existing Siegel small-kernel vector, finite pigeonhole, monic remainder reconstruction and root evaluation are genuine pinned building blocks. None establishes the joint quantitative polynomial/index/nonvanishing statement; isolated19 candidate probes and exact semantic representation bridge archived.

Completed `Roth.approxSet`: Pinned DiophantineApproximation.Basic supplies reduced rational exponent2 results; LiouvilleWith is an existential-C frequent-witness endpoint with exact-equality exclusion. New image/fiber and arbitrary-error/filter bridges verify the relationships; neither is an exact replacement for fixed1 unreduced pair membership.

Completed `Roth.exists_nat_mul_isIntegral`: NO-mathlib-has-it: IsAlgebraic.exists_nsmul_eq in Algebraic/Integral207–214 plus verified integralClosure property bridge; canonical natDenominator/isIntegral_natDenominator_smul/natDenominator_ne_zero in Algebraic/Denominator supply normalized witness.

Completed `Roth.approxSet_den_le_finite`: Existing finite intervals, finite unions/products and finite-fiber criterion verified. Rat.finite_rat_abs_sub_lt_one_div_den_sq concerns reduced rational targets, rational center and exponent2, not these supplied pairs. Neither that result nor of_finite_fibers directly replaces this arithmetic bridge.

Completed `Roth.eventually_div_rpow_lt`: Existing Filter/Tendsto/rpow ingredients; LiouvilleWith has related internal absorption but no demonstrated exported exact comparison replacement.

Completed `Roth.reduction`: Existing LiouvilleWith.nat_mul/mul_rat and frequently_lt_rpow_neg cover constant-allowing frequent approximation and exponent slack. They do not directly state fixed-constant pair infinitude. Existing sdiff/image/mono supply structural transport, with a new pointwise estimate still required.

Completed `Roth.exists_monic_aeval_eq_zero`: building blocks: Polynomial.Monic.mul, Polynomial.monic_X_pow, map_mul, Polynomial.aeval_def, zero_mul, Polynomial.natDegree_mul_X_pow, Polynomial.Monic.ne_zero; exact existing full result located: False

Completed `Roth.approxSet_num_den_mem_aux`: Rat.den_dvd gives the reduced positive denominator at most the original q. Rat.cast_def rewrites the value without changing it, and nonnegative-exponent monotonicity makes the reciprocal error tolerance no smaller at the reduced denominator. The sole exists_reduced_approx caller uses the result to force bounded reduced representatives under its contradiction hypothesis; finite fibers then handle arbitrary unreduced pairs.

Completed `Roth.exists_reduced_approx`: forms: current: finder: Partial match: Dirichlet2, LiouvilleWith, bounded denominator separation.; search: Partial match: rational Dirichlet2; no same arbitrary supplied κ theorem.; loogle: No results for Irrational _, IsCoprime _ _.; rg: No matching source lines in exact query; not absence.; local: Project target returned, index=error; no absence inference.; standard: finder: Dirichlet rational infinitude at exponent2.; search: Dirichlet and Legendre rational-set APIs.; loogle: Dirichlet2 and iff irrational matched.; rg: Pinned Dirichlet2/finite rational approximants/LiouvilleWith signatures.; local: Two Dirichlet names returned, index=error; verify pinned source/native.; abstract: finder: Finite image and finite fibers: Set.Finite.of_finite_fibers.; search: Exact finite-fiber building block; not approximation arithmetic.; loogle: Exact Set.Finite.of_finite_fibers signature.; rg: Pinned finite-fiber lemma and finite image API.; local: Finite-fiber name returned, index=error; not absence.; cells: {'form': 'current', 'method': 'finder', 'receipt': 'formal-current-finder.json', 'status': 'PASS', 'finding': 'Partial match: Dirichlet2, LiouvilleWith, bounded denominator separation.'}, {'form': 'current', 'method': 'search', 'receipt': 'formal-current-search.json', 'status': 'PASS', 'finding': 'Partial match: rational Dirichlet2; no same arbitrary supplied κ theorem.'}, {'form': 'current', 'method': 'loogle', 'receipt': 'formal-current-loogle.json', 'status': 'PASS', 'finding': 'No results for Irrational _, IsCoprime _ _.'}, {'form': 'current', 'method': 'rg', 'receipt': 'formal-current-rg.json', 'status': 'PASS', 'finding': 'No matching source lines in exact query; not absence.'}, {'form': 'current', 'method': 'local', 'receipt': 'formal-current-local.json', 'status': 'attempted; pinned/native fallback used', 'finding': 'Project target returned, index=error; no absence inference.'}, {'form': 'standard', 'method': 'finder', 'receipt': 'formal-standard-finder.json', 'status': 'PASS', 'finding': 'Dirichlet rational infinitude at exponent2.'}, {'form': 'standard', 'method': 'search', 'receipt': 'formal-standard-search.json', 'status': 'PASS', 'finding': 'Dirichlet and Legendre rational-set APIs.'}, {'form': 'standard', 'method': 'loogle', 'receipt': 'formal-standard-loogle.json', 'status': 'PASS', 'finding': 'Dirichlet2 and iff irrational matched.'}, {'form': 'standard', 'method': 'rg', 'receipt': 'formal-standard-rg.json', 'status': 'PASS', 'finding': 'Pinned Dirichlet2/finite rational approximants/LiouvilleWith signatures.'}, {'form': 'standard', 'method': 'local', 'receipt': 'formal-standard-local.json', 'status': 'attempted; pinned/native fallback used', 'finding': 'Two Dirichlet names returned, index=error; verify pinned source/native.'}, {'form': 'abstract', 'method': 'finder', 'receipt': 'formal-abstract-finder.json', 'status': 'PASS', 'finding': 'Finite image and finite fibers: Set.Finite.of_finite_fibers.'}, {'form': 'abstract', 'method': 'search', 'receipt': 'formal-abstract-search.json', 'status': 'PASS', 'finding': 'Exact finite-fiber building block; not approximation arithmetic.'}, {'form': 'abstract', 'method': 'loogle', 'receipt': 'formal-abstract-loogle.json', 'status': 'PASS', 'finding': 'Exact Set.Finite.of_finite_fibers signature.'}, {'form': 'abstract', 'method': 'rg', 'receipt': 'formal-abstract-rg.json', 'status': 'PASS', 'finding': 'Pinned finite-fiber lemma and finite image API.'}, {'form': 'abstract', 'method': 'local', 'receipt': 'formal-abstract-local.json', 'status': 'attempted; pinned/native fallback used', 'finding': 'Finite-fiber name returned, index=error; not absence.'}; conclusion: Partial existing building blocks; no verified same arbitrary fixed-quality theorem. Existing Dirichlet2 is a complete replacement only in subcritical range after nontrivial reduction/transport. Exact? closure probe is bounded evidence, not universal absence.; pinned signature receipt: isolated2-receipt.json; native generic route probe: composition-receipt.json

Completed `Roth.exists_m`: Existing Archimedean exists_nat_gt/Nat.le_ceil, Real.sqrt_sq and order/division lemmas are useful building blocks; no exact or≤3-call full simultaneous replacement verified.

Completed `Roth.exists_delta`: ContinuousAt.eventually_lt, Filter.Eventually.and/exists_gt, ContinuousAt.div and Real.continuousAt_rpow_const supply primitives. Generic cap/two-envelope selection compiles isolated; exact full arithmetic recovery is a new bridge, not ≤3 verified existing calls.

Completed `Roth.exists_approximants`: Set.seq_of_forall_finite_exists, Nat.exists_strictMono_subsequence, Filter.extraction_forall_of_frequently and log monotonicity are primitives, not a verified ≤3-call exact chain replacement. Dirichlet supplies subcritical reduced rational infinitude. LiouvilleWith has existential constantC and excludes exact equality, so is not the same fixed1 predicate.

Completed `Roth.exists_degrees`: Existing Nat.ceil_lt_mul is scalar rounding; tendsto_nat_ceil_mul_div_atTop is asymptotic. Neither is a verified existing full finite package; generic helper is newly proved scratch mathematics.

Completed `Roth.one_le_prod_pow_mul_abs_eval`: Existing one_le_pow_mul_abs_eval_div and DenomsClearable are univariate; MvPolynomial.isLocalization localizes coefficient rings but does not supply coordinatewise denominator degree clearing or its separation estimate.

Completed `Roth.abs_prod_pow_le_rpow_of_le_weight`: Use Finset.abs_prod and abs_pow for pointwise absolute-value estimates. Rewrite reciprocal powers as negative real powers; Real.rpow_le_rpow_of_nonpos and the denominator growth comparison replace all bases by powers of q0. Collapse the product with Real.rpow_sum_of_pos and the weight formula. Finally use q0>=1 and the nonpositive exponent multiplier to replace weight by its lower bound c. Zero coordinate degrees are allowed because real division is total; no positive r premise is silently added.

Completed `Roth.abs_eval_lt_of_le_index`: existing: Finset.abs_sum_le_sum_abs, Finset.sum_lt_sum_of_nonempty, Real.rpow_mul, Real.rpow_sum_of_pos, Real.rpow_le_rpow_of_nonpos, Polynomial.taylor_coeff, MvPowerSeries.weightedOrder_le; search: 15 cells actual plus corrected current Loogle and local retries; local indices error/warming, no absence claim; new helpers: Generic finite-expansion/cost theorem and recovery are newly proved, not preexisting mathlib.

Completed `Roth.exists_roth_parameters_aux`: Use exists_monic_aeval_eq_zero for f of degree at least2. Choose A=1 plus the sum of absolute coefficients, so A>=1 and every coefficient is bounded via Finsupp.single_eval_le_sum. Invoke exists_m and exists_delta for m/delta; the degree lower bound gives m>=2. The supplied integral alpha need not be irrational for this internal parameter package.

Completed `Roth.exists_roth_approximants_aux`: Apply exists_approximants at the required logarithmic threshold divided by delta squared and exists_degrees for the rounding construction. Show Antitone r from the adjacent degree ratio and delta<=1 using Fin.antitone_iff_succ_le. Bound every degree by r0, convert the first logarithm inequality by div_lt_iff, and infer the last degree at least3 from its stronger 10/delta lower bound.

Completed `Roth.one_lt_roth_eval_bound_aux`: Invoke main_lemma to get Q, coordinate degree bounds, strict index bound, rational-point nonvanishing and derivative bounds. Transfer coordinate degrees across the injective integer coefficient map via support_map_of_injective. Derive the real-power denominator comparison from the balanced-log hypothesis using Real.rpow_le_iff_le_log and positive degrees. Multiply abs_eval_lt_of_le_index by the positive denominator product and combine one_le_prod_pow_mul_abs_eval.

Completed `Roth.roth_product_bound_aux`: Extract the square-log threshold at least3 from m>=1 and nonnegative logarithm contributions. Apply four_lt_rpow and sqrt_lt_floor to get positivity of B and B<=q0^(delta*r0). Bound each degree factor by 2^r0 via Nat.lt_two_pow_self and rj<=r0, then use Finset.prod_le_pow_card and the first three_small_factors bound.

Completed `Roth.roth_log_bound_aux`: Use the strict balance inequality at index0 to infer r0>0 and delta>=0. Expand the logarithm of the positive product with Real.log_mul, Real.log_rpow and Real.log_prod. Sum the strict balanced logarithmic bounds over the nonempty finite variable set, replace log of the degree product and log B using the supplied estimates, then divide by positive r0*log(q0). The final linear bound uses delta<=1 and m>=2. G is arbitrary real; its later specialization is gamma-minus-eta.

Completed `Roth.roth_of_isIntegral`: Pinned LiouvilleWith is the useful existing predicate; current mathlib Liouville bound depends on polynomial degree and Dirichlet proves exponent2 existence, neither proves Roth exponent≤2. All15 actual search cells executed; local index:error honestly limited.

Completed `Roth.roth`: All15 search cells executed; local current/standard errors and abstract warming are limitations. Liouville degree-dependent bound and Dirichlet exponent2 existence do not supply Roth’s sharp upper bound. Pinned LiouvilleWith doc explicitly names the missing p>2 transcendence implication.

Completed `Roth.roth_rat`: Pinned Rat rational-center finiteness and Real exponent2 Infinite iff Irrational support dropping the irrationality binder; they do not prove the algebraic Roth exponent bound. Filter.eventually_cofinite gives the finite-exception interface.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`: closest: LiouvilleWith; exact replacement: False; warning: Must retain irrationality conjunct; rational cutoff family holds while IsDiophantine fails.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`: Define the scaled error f(p,q)=abs(x-p/q)*q^kappa. Add the sentinel pair(0,1) to the finite exceptional set and choose a minimum by Set.exists_min_image. Irrationality and positive denominator make that minimum positive. Choose C=min(1/2,f(a)/2). Inside the exceptional set use its finite positive minimum; outside it the failure of approxSet membership gives scaled error at least1, hence strictly greater than C. Lift a positive integer denominator to a natural one before clearing the positive real-power denominator. The sole isDiophantine_iff caller uses this for exponent2+epsilon after ruling out an infinite exceptional set. This is the finite-exception-to-uniform-constant step, not Roth theorem itself.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`: LiouvilleWith and its frequently_lt_rpow_neg/affine API are relevant building blocks; no direct uniform-bound/cutoff equivalence hit was verified. The generic bridge is authored proof, not an existing mathlib call.

## Part 4: Moral duplications

All293 declarations have completed assessments. The support-product coefficient has no second independent implementation; its all-coordinate product bridge is not a better replacement for arbitrary variable types. The complete pair evidence below distinguishes shared ingredients, equivalent endpoint interfaces and substantive independent statements across the whole project.

Completed `MvPolynomial.hasseDeriv_monomial`: Proof is generic linear-extension evaluation; no independent rederivation of exact monomial law found in written production code.

Completed `MvPolynomial.hasseDeriv_apply`: Generic finite-support linear-extension evaluation instantiated with defining component maps; no independent exact inline rederivation found in canonical production sources.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: Combines existing generic/scalar/order API; no exact named existing theorem claimed.

Completed `MvPolynomial.coeff_hasseDeriv`: Natural multivariate extension of Polynomial.hasseDeriv_coeff; generic lowering characterization and weighted-pullback implementation are new alternatives rather than existing API duplicates.

Completed `MvPolynomial.hasseCoeff_eq_prod`: A specialization of generic identity-padding of a finitely supported product. Multinomial factorial ratios are a false friend, not the same coefficient.

Completed `MvPolynomial.hasseDeriv_zero_apply`: Mirrors univariate pointwise/map zero laws. Generic coefficient preservation implies identity via extensionality, but normalization for the concrete Hasse family remains content; new local abstraction is not an existing replacement.

Completed `MvPolynomial.hasseDeriv_zero`: Mirrors Polynomial.hasseDeriv_zero and neighboring pointwise normalization. Generic LinearMap.ext only packages a premise and is not unconditional concrete operator normalization.

Completed `MvPolynomial.hasseDeriv_C`: Mirrors Polynomial.hasseDeriv_C; generic C/monomial/lsum normalization exists but does not supply concrete nonzero-order binomial vanishing premise.

Completed `MvPolynomial.hasseDeriv_map`: No verified replacement; analogous univariate and first-order naturality patterns.

Completed `MvPolynomial.hasseDeriv_rename`: No verified direct replacement; standard all-order extension of first-order injective renaming law.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Shared coordinatewise binomial cocycle used twice, no duplicated downstream scalar proof identified in source search.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: Divided-derivative iteration extends univariate composition; not automatic for arbitrary HS families.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: Support-separated corollary of new general composition; not a ≤3call composition from existing pinned mathlib.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Isolates one-coordinate normalization for the sole partial/Hasse compatibility proof; no duplicated independent successor proof found in source audit.

Completed `MvPolynomial.pderiv_hasseDeriv`: Coordinate case of additive iterativity, extending univariate Hasse composition.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: Same degree-lowering idea as univariate Hasse bound; generic support-shift helper overlaps degreeOf support-sup infrastructure. Not a literal duplicate.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: Same support-vanishing idea as univariate theorem; not a literal duplicate.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Monomial induction helper for public arbitrary-factor separation, no same-interface duplicate found by source audit.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Constant-factor special case of future full multivariate Leibniz API, not a duplicate of the pinned univariate or ordinary derivative API.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: A short basis-ext and definition-simp proof exists; Phase6b review case.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: Equivalent to coordinate aeval compatibility in the unique-variable case, but that bridge is project API. Generic linear conjugacy needs normalization.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Hasse-named packaging of a finite-product natural combinatorial bound; not an exact named replacement claim.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Shared generic additive recurrence induction, compiled for Polynomial and MvPolynomial; no exact pinned replacement.

Completed `Roth.box`: Principal lower interval of Finsupp pointwise order, MainLemma282-323 already uses Iic(ofSupportFinite r) under finite-support bounds

Completed `Roth.weight`: Finsupp.weight, Finsupp.linearCombination

Completed `Roth.mem_box`: Box API duplicates existing product/interval membership.

Completed `Roth.card_box`: Generic finite Cartesian-product counting.

Completed `Roth.card_le_card_box`: Finite Cartesian-product cardinality and monotonicity under inclusion, Finsupp interval cardinality bound after membership and endpoint normalization

Completed `Roth.weight_nonneg`: Elementary sum positivity after definitional reduction; not a duplicated named Finsupp theorem

Completed `Roth.weight_zero`: Zero preservation already structural for bundled Finsupp.weight; bridge from ratio formula is not defeq.

Completed `Roth.weight_add`: Weighted monomial degree is an additive homomorphism; current ratio representation requires normalization.

Completed `Roth.weight_eq_zero_iff`: Positive sum zero principle already exists; reciprocal/cast/finsupp packaging is project API.

Completed `Roth.weight_single`: Finsupp.weight_single, Finsupp.sum_single_index

Completed `Roth.weight_le_card`: Instance of generic finite-sum upper bound. Parent Finsupp.weight bridge verified; no matching dedicated upper-cardinality law established.

Completed `Roth.weight_mul_left`: Finsupp.bilinearCombination.map_smul, Finsupp.linearCombination generator linearity

Completed `Roth.weight_le_degree_div`: Finset.sum_le_sum + div_le_div_of_nonneg_left proof pattern, Finsupp.sum_le_sum aggregation, Related real-ratio proof in Roth.weight_le_delta_aux

Completed `Roth.weight_mapDomain`: Naturality of free-module evaluation under generator relabelling, Finsupp.linearCombination_comp_lmapDomain bundled companion

Completed `Roth.wronskianMatrix`: Direct construction is a verified two-block composition; meaningful semantic API exemption., Multivariate genWronskian constructs related selected-operator matrix, not identical target.

Completed `Roth.wronskian`: Binary Wronskian specializes at l2, not arbitrary arity, Generic determinant infrastructure already handles raw data construction

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: Multivariate easy direction repeats relation/kernel argument; generic operator-family route can unify.

Completed `Roth.det_choose_eq`: Generic monic evaluation content is already in mathlib; specific binomial normalization resembles an existing private integer bridge. Do not add another generic evaluation theorem.

Completed `Roth.coeff_prod_of_natDegree_le'`: Related public common-bound API, not the same statement; no project duplicate found.

Completed `Roth.sum_range_le_sum_of_injective`: Existing sharper lower-bounded finite integer-set sum theorem already contains the Nat/Fin c=0 case.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Classical leading-monomial/Vandermonde calculation; existing common-bound product coefficient theorem does not directly give varying bounds. No exact pinned replacement found.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: Generic coefficient nonzero and Vandermonde nonzero steps already abstract. Hasse coefficient and binomial conversion bridges remain new mathematical helpers; downstream criterion cannot be used circularly.

Completed `Roth.wronskian_update_sub_smul`: Elementary determinant transvection, but not a defeq or strict <=3-existing-call replacement for the family statement.

Completed `Roth.linearIndependent_update_sub_smul`: linearIndependent_add_smul_iff, Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:751

Completed `Roth.sum_natDegree_update_lt`: Standard leading-term cancellation plus generic finite-sum comparison; normalized cancelLeads bridge is compiled, not definitional.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: The existing general elementary-shear independence law replaces one helper, not the Wronskian criterion. Downstream iff and generalized Wronskian theorem are circular replacements.

Completed `Roth.wronskian_eq_zero_iff`: Propositional assembly duplicates no substantive mathlib theorem: both constituent criterion lemmas are project-local. Generic matrix determinant dependence helps only the easy direction with scalar/jet bridges.

Completed `MvPolynomial.taylor`: MvPolynomial.aeval (fun j ↦ X j + C (α j)), MvPolynomial.bind₁ with the same substitution, Polynomial.taylorAlgHom: univariate analogy only

Completed `MvPolynomial.taylor_apply`: Own defining equation applied to P, Polynomial.taylor_apply: genuine univariate API analogy only

Completed `MvPolynomial.taylor_X`: MvPolynomial.aeval_X specialized definitionally to the translation assignment

Completed `MvPolynomial.taylor_C`: Specialization of generic AlgHom coefficient preservation; univariate Polynomial.taylor_C is analogous but not identical.

Completed `MvPolynomial.taylor_monomial`: Existing aeval_monomial specialized to g j=X j+C(α j), A=MvPolynomial σ R.

Completed `MvPolynomial.coeff_aeval_X_mul`: One implementation and one direct caller; isolates the support-independent coefficient extraction, not the full Hasse/Taylor theorem.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Special coordinate factorization, distinct from general cocycle or successor identities in HasseDeriv; one shared implementation for the monomial induction.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Exponent splitting differs from scalar binomial-coordinate helper; no second exact implementation in module.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Coordinate induction step is distinct from universal aeval_monomial and full coefficient theorem; scalar helpers separate different calculations.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Monomial special case is proof scaffold for linear extension, distinct from aeval_monomial image formula and full coefficient theorem.

Completed `MvPolynomial.coeff_taylor`: Univariate Polynomial.taylor_coeff is analogous, not a replacement for arbitrary σ., Direct aeval statement is definitionally equivalent, not a distinct theorem.

Completed `MvPolynomial.eval_taylor`: Abstract substitution-evaluation law already exists; Polynomial.taylor_eval is a univariate analogue only.

Completed `MvPolynomial.taylor_taylor`: Polynomial.taylor_taylor is only a univariate analogue; generic comp_aeval_apply needs nondefinitional generator normalization.

Completed `MvPolynomial.taylor_zero`: Elementary identity-assignment law after zero normalization; not a direct definitional specialization.

Completed `MvPolynomial.taylor_map`: Naturality of substitution specialized to translations; no distinct new mathematical argument.

Completed `MvPolynomial.taylor_rename`: Generic substitution naturality specialized to shifted generators; close analogue rename_expand, not same substitution.

Completed `MvPolynomial.degreeOf_taylor_le`: Univariate Taylor degree invariance is analogous but not direct replacement. Direct aeval spelling is definitionally equivalent.

Completed `MvPolynomial.taylor_neg_taylor`: Specializes additive composition to mutually cancelling shifts, and is a left-inverse interface for injectivity. Neither is a duplicate of composition or injectivity.

Completed `MvPolynomial.taylor_injective`: A generic left-inverse corollary, analogous to univariate Taylor injectivity. Not an independently available multivariate all-mathlib one-call term.

Completed `MvPolynomial.taylor_eq_zero_iff`: Univariate zero-reflection analogue and generic ring injectivity corollary; stronger arbitrary-variable semiring theorem provides genuine additional triangular coefficient content.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Distinct coefficient, polynomial reconstruction and evaluation layers; same inverse-shift motif as univariate sum_taylor_eq but no direct specialization to multivariate Hasse box expansion.

Completed `MvPolynomial.eval_eq_sum_box`: Polynomial reconstruction, coefficient identification and evaluated scalar identity are distinct layers; Main consumer adds strict analytic estimates. No independent full evaluated expansion rederivation found.

Completed `Roth.normOne`: No second full coefficient-L1 definition found. Diagonal/evaluation absolute-sum estimates concern different quantities. Bound laws need independent assessments rather than automatic inheritance of construction verdict.

Completed `Roth.diag`: No second arbitrary-variable diagonal implementation found; HasseDeriv unique-variable transport is different. Not generating-series coefficient diagonal extraction. Bounds need independent assessments.

Completed `Roth.normOne_nonneg`: Generic finite-sum nonnegativity; individual abs_nonneg uses elsewhere are not duplicate full theorem.

Completed `Roth.normOne_eq_sum_of_support_subset`: Support-padding law already in Finsupp API. Univariate Polynomial.sum_eq_of_subset is analogous, not direct multivariate replacement. Hamming norm and module length semantic hits measure different objects.

Completed `Roth.normOne_monomial`: Exact singleton sum law already in MvPolynomial and Finsupp. Univariate Polynomial.sum_monomial_index analogous. supNorm_monomial/gaussNorm_monomial are distinct size functions, not whole normOne replacements.

Completed `Roth.normOne_zero`: Exact empty finite-support aggregate law already in mathlib; Polynomial.sum_zero_index analogous; support_zero+sum_empty alternative. Generic norm_zero requires a correct norm structure. Nearby normOne_neg/cardinality proofs are not inline duplicate zero laws.

Completed `Roth.abs_coeff_le_normOne`: A direct specialization of an existing general finite-support nonnegative coordinate bound. Mathlib NumberTheory/Height/MvPolynomial.lean:277 uses same generic law for absolute values.

Completed `Roth.normOne_add_le`: Mathematically an l1 triangle inequality, but existing sup-norm and integral norm theorems concern different objects; no inherited has-it result from parent.

Completed `Roth.normOne_neg`: Standard norm sign invariance; existing Finsupp coordinate reindexing is sufficient. Height/integralL1/fieldnorm are different objects.

Completed `Roth.normOne_sum_le`: Abstract subadditive finite-sum bound and norm_sum_le; direct existing theorem specializes once the project zero/triangle witnesses are supplied.

Completed `Roth.normOne_mul_le`: Discrete Young L1 convolution inequality; standard normed-ring law is analogous but no verified representation bridge.

Completed `Roth.normOne_prod_le`: Finite iteration of discrete Young coefficient L1 convolution bound; generic finite submultiplicative map bound already in mathlib.

Completed `Roth.normOne_le_card_mul`: Same scalar finite-family inequality independently used by abs_coeff_diag_le; exact target already duplicates existing generic Finset theorem.

Completed `Roth.normOne_det_le`: Analog of Matrix.det_le for merely submultiplicative real seminorms; degree/index/Wronskian determinant expansions prove different laws.

Completed `Roth.abs_coeff_hasseDeriv_le`: Same finite binomial factor appears in normOne_hasseDeriv_le; that is an L1 estimate and cannot retain the coefficient B without an unwanted support-cardinality factor.

Completed `Roth.normOne_hasseDeriv_le`: Univariate Hasse coefficient formula is an analogue; Gauss sup norm, Mahler measure, and coefficient sup bound are distinct estimates.

Completed `Roth.diag_eq_sum`: Elementary specialization and normalization of existing evaluation expansion; genuine product-power/monomial bridge prevents claiming definitional exact duplicate.

Completed `Roth.abs_coeff_diag_le`: A finite-fiber pushforward triangle bound; abstract Finset inequalities exist but the polynomial substitution-to-fiber bridge is real normalization, not definitional equality.

Completed `Roth.natDegree_diag_le`: Overlaps existing aeval substitution law; local coordinate sum hypothesis bridge is distinct and not definitional.

Completed `Roth.eval_diag`: Generic polynomial substitution associativity/naturality already in mathlib and re-used inline.

Completed `Roth.diag_sub`: Wrapper of map_sub; no independent algebraic content.

Completed `Roth.geom_sum_le_one_add_pow`: No project duplicate or inspected exact existing replacement; binomial expansion is mathematical source, not a direct replacement.

Completed `Roth.sum_box_prod_pow_le_aux`: Finite-box product estimate is an internal factorization stage, distinct from scalar geometric sum and polynomial support/evaluation bound. No duplicate full argument found in this source review.

Completed `Roth.abs_eval_le`: No duplicate: abs_coeff_diag_le handles coefficient collisions; normOne_le_card_mul is unweighted; Main.abs_eval_lt_of_le_index is a Taylor/index estimate. A future weighted-support majorant can share proof stages with the homogeneous bound.

Completed `Roth.degreeOf_det_hasseDeriv_le`: Generic polynomial determinant degree bound underlies this Hasse specialization; no current mathlib exact replacement verified.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: A Hasse-specific assembly of support-cardinality, derivative-length and determinant seminorm estimates. Prior accepted project assessments do not make these existing mathlib lemmas.

Completed `Roth.genWronskian`: One-line determinant wrapper, with established semantic API exemption. Raw entry-dependent derivative matrices in CoeffNorm/Separation/Theta are related but not copies of its row-order/family-column form.

Completed `Roth.kronecker`: Literal one-call specialization of existing universal evaluation, with legitimate local semantic naming exemption.

Completed `Roth.kroneckerExp`: Specialization of existing generic weighted exponent map. Shared generic API pattern with independently accepted Roth.weight, which instead targets Real with reciprocal weights; these project maps are not equal.

Completed `Roth.kronHasse`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.kronSpan`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: Roth.wronskian_eq_zero_of_not_linearIndependent has analogous coefficient-witness proof

Completed `Roth.kronecker_monomial`: Redundant specialization of existing generic monomial evaluation under parent re-aim. Old spelling requires genuine finite-product normalization; not definitional and not a one-call old-form proof.

Completed `Roth.kroneckerExp_injOn`: Private NoetherNormalization.sum_r_mul_ne90–98 independently performs essentially same positional conversion. Its expanded statement replays using generalized weight helper; not a public exact replacement or actual source caller.

Completed `Roth.coeff_kronecker`: Coefficient separation is existing support-local mapDomain transport; exact aeval coefficient API not identified.

Completed `Roth.kronecker_eq_zero_iff`: Abstract support-local injection is already in Finsupp.mapDomain_injOn; no duplicate Finsupp theorem needed.

Completed `Roth.linearIndependent_kronecker`: Final linear relation transport duplicates generic map_injOn; degree-bound/weighted-support sufficient condition is additional specialized proof.

Completed `Roth.derivative_aeval`: Standard multivariable analogue of the existing univariate chain rule; no verified existing ≤3-call replacement.

Completed `Roth.derivative_kronHasse_aux`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.derivative_mem_kronSpan`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.hasseDeriv_kronecker_mem`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Final extraction is generic span linear algebra, but the private uniform higher chain-rule premise is new project content. No verified existing <=3-call replacement for the full law.

Completed `Roth.det_sum_rows`: Standard multilinearity, already represented by two generic mathlib laws; convenience wrapper inclusion is a Phase6b taste decision.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: The determinant transport is distinct from the standalone row-multilinearity expansion and from the final nonvanishing implication; no duplicate full construction.

Completed `Roth.exists_genWronskian_ne_zero`: Classical Bostan–Dumas Theorem3 polynomial specialization, with Hasse normalization; not duplicated by existing two-polynomial Wronskian API.

Completed `Roth.sqrt_one_sub_inv_lt`: A specialized Bernoulli/AM-GM consequence, not an identical theorem.

Completed `Roth.inv_add_inv_le`: Complementary-pair and whole-grid reciprocal estimates are distinct steps of the lattice proof, not duplicate full constructions.

Completed `Roth.sum_inv_le`: Complementary-pair and whole-grid reciprocal estimates are distinct steps of the lattice proof, not duplicate full constructions.

Completed `Roth.sum_inv_lt`: Reciprocal convexity already follows from convexOn_zpow(-1); sum reindexing exists. Grid rational upper bound and sqrt comparison still need proof.

Completed `Roth.extend_apply_castSucc`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.extend_apply_last`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_box_fiber_aux`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_box_last`: Abstract counting is Finset.card_eq_sum_card_fiberwise; geometric Finsupp identification is real project proof.

Completed `Roth.filter_weight_le_eq_empty`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_fiber_eq`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_weight_le_succ_aux`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_weight_le`: Not Roth arithmetic-progression/Behrend results. Generic fibre count handles decomposition, probability theory supplies a potential stronger route requiring new uniform-box moment/count bridges.

Completed `Roth.index`: Generic support minimum is already infDegree., Natural weightedOrder is a positive-integral-parameter alternate interface; its project bridge is actual proof, not an existing library call.

Completed `Roth.mem_support_taylor_iff`: The helper has a distinct role in the index proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.index_le_weight`: Finite infimum is bounded by each member, independently of the degree map; already Finset.inf_le.

Completed `Roth.exists_weight_eq_index`: Attainment of a finite nonempty support infimum in a linear order is already Finset.exists_mem_eq_inf., MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder provides the standard natural-weight analogue.

Completed `Roth.le_index_iff`: Finite meet lower-bound universal property, not a new theorem about derivatives.

Completed `Roth.index_nonneg`: Finite infimum preserves a common lower bound. Polynomial and point data select the finite support but add no order-theoretic content.

Completed `Roth.index_eq_zero_iff`: Finite support minimum equals bottom iff a supported degree is bottom, Taylor constant coefficient is evaluation at center

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Classical Roth/Milojevic derivative-index estimate. Generic infDegree sums/products are adjacent, not duplicates. New supportShift proof is not a preexisting mathlib call.

Completed `Roth.le_index_sum`: Classical minimum-order sum inequality, exactly generic finite-support degree inequality under OrderDual. MvPowerSeries.min_weightedOrder_le_add is adjacent natural-weight binary API.

Completed `Roth.weight_eq_finsuppWeight_div`: Generic map/linearity law already exists; no claim that denominator arithmetic is definitional or ≤3 calls.

Completed `Roth.index_eq_weightedOrder_div`: Original proof manually identifies two minima; this is missing generic bridge API, not duplicated existing comparison.

Completed `Roth.index_mul`: The natural-weight algebraic core is exactly the existing series multiplication theorem. The old real-index spelling requires genuine normalization and finite projection; new comparison proofs from133/143 are not preexisting mathlib calls.

Completed `Roth.index_prod`: Natural-series finite-product additivity is already mathlib. Old real default-zero form needs genuine normalization, finite projection and casting. Parent local binary law and earlier new bridge proofs are not existing mathlib calls.

Completed `Roth.index_neg`: Degree support-negation law; weightedOrder_neg/order_neg are related alternative APIs.

Completed `Roth.index_C_mul`: Scalar support invariance; related weightedOrder inequality/multiplication and negation API.

Completed `Roth.index_mul_left_weights`: Homogeneous scaling of a finite support minimum is existing finite-inf hom transport. Original representation bridge is genuine normalization, not definitional or a preexisting theorem.

Completed `Roth.index_rename`: Underlying finite-support transport duplicates generic lattice image functoriality; weightedTotalDegree rename is a related maximum law, not the exact minimum.

Completed `Roth.index_le_card`: Canonical support-witness estimate is existing infDegree/Finset.inf_le; coordinate weight bound overlaps weight_le_card. Neither alone is exact full theorem.

Completed `Roth.index_unique`: Existing rootMultiplicity_eq_natTrailingDegree is the analogous univariate law of the parent infDegree abstraction., Existing natTrailingDegree coefficient/support laws express the least nonzero coefficient.

Completed `Roth.coeffNone`: New plain-function name for existing equivalence followed by coordinate projection; local semantic-name exemption acknowledged.

Completed `Roth.eq_mapDomain_some_add_single`: Finsupp.optionElim_some expresses reconstruction at Zero generality; expanded additive form requires bridge

Completed `Roth.coeff_X_none_pow_mul_rename`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.coeff_coeffNone`: The existing canonical coefficient correspondence is the same mathematical law under normalized exponent coordinates.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: Polynomial coefficient reconstruction under the existing iterated polynomial-ring algebra equivalence.

Completed `Roth.degreeOf_coeffNone_le`: Arbitrary Option analogue of existing finite degreeOf_coeff_finSuccEquiv., Support insertion preserves remaining coordinate bounds; abstract finite supremum proof verified as a component, not existing full replacement.

Completed `Roth.coeff_rename_mul_aeval`: Canonical double coefficient law is exactly three existing calls; first-coefficient-only law is insufficient for the full theorem., No exact original Option/aeval law was verified as a single existing theorem.

Completed `Roth.aeval_X_eq_rename`: Pointwise specialization of existing equality of the same R-algebra homomorphisms; no new mathematical law.

Completed `Roth.hasseDeriv_rename_mul_aeval`: Univariate constant outer-factor Hasse law is proved in mathlib-only scratch; it covers only the none-coordinate part., Previous159 aeval bridge is already in mathlib, and its wrapper is eliminated in the target replay.

Completed `Roth.coeff_uniqueAlgEquiv_symm`: The Roth law is the singleton-exponent specialization of the existing arbitrary-finsupp law, not a namespace-aware prefilter hit.

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: The selected-variable/natDegree content exists canonically, but a genuine newly proved presentation bridge is needed to apply it to uniqueAlgEquiv. No automatic inherited NO from coefficient theorem161.

Completed `Roth.degreeOf_rename_mul_aeval`: Product-degree additivity plus injective renaming are existing mathlib facts., Analogous none-variable theorem is distinct because its RHS is V.natDegree.

Completed `Roth.degreeOf_none_rename_mul_aeval`: Canonical constant-multiplication degree law exists, but old separated form needs an actual new AlgHom normalization proof.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_coeffNone_basis_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_separated_representation`: Two-factor tensor/matrix rank factorization is abstract mathematical context; generic pure-tensor expansion loses simultaneous independence and bounds.

Completed `Roth.det_hasseDeriv_separated`: Outer matrix formula is existing det_mul+transpose. Full derivative matrix normalization uses project multivariate Hasse/product API and is not an existing ≤3-call mathlib replacement.

Completed `Roth.exists_sum_mul_eq_gcd`: Integer specialization and reordered equality of existing finite Bezout theorem.

Completed `Roth.exists_nat_smul_eq_map`: Same denominator mechanism as existing localization laws; concrete positive-natural output packaging is not an exact short existing-call theorem.

Completed `Roth.exists_primitive_smul_eq`: Classical content/primitive-part normalization underlying Gauss lemma, not the whole product-primitivity law., Finite-function gcd extraction is already mathlib; the multivariate/fraction-field bridge is additional.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: finite Bezout identity, membership detected by generators of unit ideal

Completed `Roth.rescale_separated_factor_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_int_factors`: Gauss-type descent; univariate Gauss integrality is a partial match requiring actual multivariate and support/primitivity bridges.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_det_eq_mul`: det_mul and map_det cover transport but not bounded derivative-row selection, nonvanishing and original-ring separated descent. Binary Polynomial.wronskian is not the finite-family construction.

Completed `Roth.RSet`: Degree component is the existing restrictSupport carrier., Finite coefficient-array boxes compose with Finset.finsupp under extra finite exponent-box data., Polynomial.supNorm is univariate; projective Height and ℓ¹ norm are not the same bound.

Completed `Roth.indexSet`: Exact generic outer binary-image construction already exists., Parent index normalization re-aims to infDegree/Finsupp.weight/aeval, with explicit default0 projection.

Completed `Roth.Θ`: Outer supremum operation is exact existing SupSet.sSup specialization., Parent family is exact Set.image2; full index expansion uses existing infDegree with new finite-support normalization glue.

Completed `Roth.lem6M`: Chosen majorant of determinant coefficient estimate; not Matrix.det_le, whose hypotheses and object differ.

Completed `Roth.lem6Φ`: Existing addition of two supremal values; no standalone universal Roth Phi concept established. Real totalization prohibits silently replacing it by extended-real or product-set suprema.

Completed `Roth.one_mem_RSet`: Elementary unit-degree and coefficient-delta facts exist; exact all-three-condition family membership law not independently verified upstream. No absence claim from unavailable local index.

Completed `Roth.indexSet_nonempty`: Binary-image nonemptiness after accepted180 parent re-aim. Arithmetic complete-family witness is separately project mathematics, not a mathlib building block.

Completed `Roth.indexSet_bddAbove`: Θ_le_card repeats the same mapped-degree/index bound inside a stronger numeric supremum estimate; full target is useful local side-condition API.

Completed `Roth.index_le_Θ`: Dependent law of parent Θ, already exact SupSet.sSup; re-aim gate applies after independent native law/bridge checks.

Completed `Roth.Θ_nonneg`: Existing nonnegative real supremum law specialized to the project family; parent re-aim independently checked.

Completed `Roth.Θ_le_card`: indexSet_bddAbove repeats the same arithmetic pointwise proof but asserts existence of an upper bound; Θ_le_card retains the known bound. Neither is identical to the other, and BddAbove alone cannot supply this cardinality bound.

Completed `Roth.Θ_le_of_forall_index_le`: Structural supremum law shared with Real.sSup_le in Θ_le_card; unlike the preceding substantive bound, the full pointwise arithmetic premise is supplied here.

Completed `Roth.Θ_mono`: The analogous monotonicity law for sSup already exists in csSup_le_csSup; apply the parent re-aim rule rather than proposing a Roth-specific upstream law.

Completed `Roth.indexSet_comp_subset`: The inclusion transport is used in both directions by Θ_equiv; it is distinct from the final equality of suprema and from height monotonicity. Retain this private transport boundary.

Completed `Roth.Θ_equiv`: No independent duplicate Theta invariance found; generic supremum congruence is already available but has an unprovided admissible-family equivalence/equality premise.

Completed `Roth.isPrimitive_linear`: The helper has a distinct role in the polynomial-index transport and bounding proofs as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.isPrimitive_pow`: The helper has a distinct role in the polynomial-index transport and bounding proofs as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_eq_pow_mul_of_rootMultiplicity`: Classical Gauss lemma plus root multiplicity divisibility; the missing bridge handles primitive qX-h and the full mapped root multiplicity. Existing rational-root numerator/denominator bounds are first-order partial analogues.

Completed `Roth.pow_rootMultiplicity_le`: Rational root theorem with multiplicity; determinant coefficient proofs reuse integer discreteness but do not rederive this bound.

Completed `Roth.index_unique_le_log_div`: The helper has a distinct role in the polynomial-index transport and bounding proofs as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.Θ_unique_le`: {'other': 'Roth.Θ_le_of_forall_index_le', 'same_statement': False, 'same_proof': False, 'assessment': 'Only the outer supremum step agrees; current theorem must prove its arithmetic pointwise premise.'}, {'other': 'Roth.index_unique_le_log_div', 'same_statement': False, 'same_proof': 'pointwise arithmetic reused', 'assessment': 'One-polynomial logarithmic bound versus extremal-family bound; keep helper factoring.'}, {'other': 'csSup_le', 'same_statement': False, 'same_proof': 'outer order step only', 'assessment': 'Not a full arithmetic replacement.'}

Completed `Roth.one_le_lem6M`: {'other': 'List.one_le_prod', 'same_statement': False, 'same_proof': 'abstract product induction subsumes multiplication stage', 'assessment': 'Actual four factor inequalities must still be established; list normalization is explicit.'}, {'other': 'one_le_mul_of_one_le_of_one_le', 'same_statement': False, 'same_proof': 'three assembly calls', 'assessment': 'Does not include power and factorial premises.'}, {'other': 'Roth.lem6M', 'same_statement': False, 'same_proof': False, 'assessment': 'Parent defines envelope; theorem supplies its lower bound.'}

Completed `Roth.floor_sq_div_two_le_sum`: Gauss summation already in Finset.sum_range_id_mul_two/sum_range_id. Nearby mul_div_two_le_sum_max_aux and mul_sq_div_three_le_sum_max_of_pos_aux repeat cast/sum normalization, with different full conclusions.

Completed `Roth.sq_div_three_lt_floor_sq_div_two`: Private mul_sq_div_three_le_sum_max_of_pos_aux directly proves a²/3≤sum using Gauss identity and nonnegative remainders; it bypasses but does not rederive strict floor-square comparison. MainLemma sqrt comparison is related, with a different conclusion.

Completed `Roth.mul_div_two_le_sum_max_aux`: The helper has a distinct role in the polynomial-index transport and bounding proofs as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`: The helper has a distinct role in the polynomial-index transport and bounding proofs as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.mul_sq_div_three_le_sum_max_aux`: The helper has a distinct role in the polynomial-index transport and bounding proofs as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.min_le_sum_max`: Three private helpers are complementary branches, not independent unconditional minimum duplicates. index_numeric_bound_aux consumes a bound. Paper floor FACTs are bypassed by stronger direct remainder proof.

Completed `Roth.sum_max_sub_le_index_det`: Abstract determinant-order argument parallels valuation/tropical determinant lower bound; Matrix.det_le is an absolute-value upper bound and is not a replacement. Project index helpers do not count as existing mathlib.

Completed `Roth.index_separated_mul_le_aux`: The helper has a distinct role in the polynomial-index transport and bounding proofs as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.index_det_le`: Index support-minimum and multiplication have generic mathlib counterparts; the determinant envelope and separated integer factor-height membership proof remain project/new content.

Completed `Roth.weight_le_delta_aux`: This ratio-to-weight estimate supplies derivative-row admissibility in index_le_lem6; mapped_det_ne_zero_aux instead proves determinant nonvanishing, and index_numeric_bound_aux closes a scalar real inequality. These are distinct proof obligations.

Completed `Roth.mapped_det_ne_zero_aux`: This is the nonvanishing bridge for the determinant lower estimate; weight_le_delta_aux proves the independent derivative-weight bound and index_numeric_bound_aux closes the scalar inequality.

Completed `Roth.index_numeric_bound_aux`: This scalar real inequality closes index_le_lem6 once min_le_sum_max and the two determinant bounds have been combined. It neither establishes determinant nonvanishing nor proves derivative-weight admissibility, the separate roles of the two preceding helpers.

Completed `Roth.index_le_lem6`: Generic index/order ingredients can use infDegree or weightedOrder after explicit bridges; this endpoint additionally chooses a nonzero separated Hasse determinant, controls integer factors and applies a substantive numerical estimate. The individual witness and following supremum theorem are distinct.

Completed `Roth.Θ_option_le`: The outer supremum/finite-maximum step is existing order theory, while index_le_lem6 is a distinct arithmetic existential endpoint. Reaiming Θ at SupSet.sSup and index at infDegree does not supply that whole recursive height/rank law.

Completed `Roth.factorial_coefficient_le_two_pow_aux`: This natural factorial/power envelope controls the non-height factors in lem6M_lt; two_pow_lt_rpow_aux instead proves the strict logarithmic comparison with a real power of q. They are successive, different inequalities.

Completed `Roth.two_pow_lt_rpow_aux`: The preceding factorial_coefficient_le_two_pow_aux is a weak natural combinatorial bound. This helper makes the strict comparison with a q-power via logarithms, and lem6M_lt composes the two stages with the height factor.

Completed `Roth.lem6M_lt`: A source-specific application of factorial majorization and exponential absorption. Generic positive multiplication/rpow transport is already available, but supplying its numerical premises needs new/project proofs.

Completed `Roth.lem7_Φ_bound`: The real-power ingredients and generic ordered weighted transport are existing API. The concrete constants and simultaneous absorption still require numerical reasoning; new generic envelope is a proved helper, not an existing mathlib replacement.

Completed `Roth.lem7_numeric`: Classical square-root upper bounds and dyadic power normalization are ingredients, not an identified duplicate of the combined absorption.

Completed `Roth.theta_scaled_unique_le_aux`: The singleton scaled logarithmic bound is distinct from the prefix induction and the subsequent two-term/root absorption; it reuses Θ_mono and Θ_unique_le rather than duplicating their proofs.

Completed `Roth.theta_delta_succ_lt_aux`: A reciprocal numerical margin for enlarging delta, distinct from coefficient-envelope bounds, singleton logarithmic control and prefix-index transport. It supplies only the induction-parameter threshold.

Completed `Roth.theta_prefix_lt_aux`: The prefix bound uses the supplied lower-dimensional induction hypothesis after monotonicity and scaling. The singleton helper instead uses Θ_unique_le and positive logarithms; their shared Θ_mono step does not duplicate the two distinct conclusions.

Completed `Roth.theta_lt_base_aux`: This small-delta one-variable base case derives Θ≤δ from Θ_unique_le and then a strict square-root target. The large-delta helper instead uses the dimension bound; the singleton scaled helper also uses logarithms but has a different balanced-denominator conclusion.

Completed `Roth.theta_denominators_one_lt_aux`: Uses the same positive-product/logarithm primitives as other denominator preparations, but supplies a uniform denominator conclusion shared by three callers rather than an extremal-index inequality. Retain the private preparation boundary.

Completed `Roth.theta_phi_lt_aux`: Combines the distinct singleton logarithmic and prefix-induction estimates with two numerical absorption stages for each determinant rank. It is not the finite-maximum successor theorem or a reproof of its ingredients.

Completed `Roth.theta_lt_succ_aux`: Converts the recursive Option-coordinate supremum bound into the next-dimensional target by uniformly bounding every rank. The per-rank theta_phi_lt_aux proves the numerical input; this helper supplies variable transport and finite-maximum aggregation, while the large-delta branch uses a different dimension bound.

Completed `Roth.theta_lt_of_large_delta_aux`: This large-delta branch uses only the dimension upper bound and scalar power comparisons. The small-delta base uses a logarithmic singleton estimate, and the successor uses determinant/finite-maximum induction; their conclusions agree on different premise regimes.

Completed `Roth.Θ_lt`: Θ is a sSup and index has weighted-support representations; generic upper/strict supremum laws organize bounds already supplied. Schwartz–Zippel counts roots over finite products, and additive Roth bounds/Chevalley complexity are different mathematics. No identified exact existing-law replacement of the full quantitative endpoint.

Completed `Roth.lam`: The literal cutoff reappears as 4*c*f.natDegree*sqrt m in the more general project auxiliary-polynomial helper; the new scaled a formula unifies the arithmetic after reassociation, not the substantive theorem. gam is an affine cutoff derived from lam, eta a different error term, and Lattice lam a free real variable; these are not duplicate declarations.

Completed `Roth.gam`: Expanded cutoff occurs in private rpow-bound/counting helpers with c replacing 1+3δ. This is a specialization link, not a duplicate declaration to delete.

Completed `Roth.eta`: The same dyadic profile occurs in Roth.lem7_Φ_bound with factor3; the exact eta expression occurs in Roth.lem7_numeric and Θ_lt endpoints/helpers. A future shared name must precede Theta to avoid MainLemma→Theta import cycle. lam is a square-root dimension loss; gam is the large-index threshold; neither equals this nonlinear small-index error.

Completed `Roth.mainCoeffBound`: Same floor-of-power pattern appears as Cn in exists_mem_RSet_le_index_of_rpow_bound_aux and in pigeonhole_count, with different bases/exponents. Existing sqrt_lt_floor already isolates the generic square-root floor argument; the named B1 is its application, not new rounding machinery.

Completed `Roth.boxFamily`: RSet differs by nonzero and symmetric absolute bounds; restrictSupport omits coefficient bounds. No exact duplicate established.

Completed `Roth.exists_delta_bound`: Shares neighborhood shrinking with Roth.exists_delta; its strict square-root gap is independent content. No other source inlining of this exact bound found.

Completed `Roth.eta_lt_gam_iff`: The exact eta formula has no role in the equivalence. Morally a translated strict inequality; exists_delta_bound supplies a substantive numerical bound rather than this equivalence.

Completed `Roth.sqrt_lt_nat_floor_aux`: The helper proves the strict lower bound used by sqrt_lt_floor, while Nat.floor_le supplies its non-strict upper bound; the two halves are distinct mathematical facts.

Completed `Roth.sqrt_lt_floor`: Lower content equals the private helper; upper projection equals Nat.floor_le. Natural-input floor-sqrt identity needs a new bridge for arbitrary real X.

Completed `Roth.four_lt_rpow`: Private two_lt_rpow_aux shares the square-comparison method with target2. Generic arbitrary-target powerTransfer and ordered-semiring squareTransfer are new verified proofs, not existing mathlib replacement lemmas.

Completed `Roth.mul_log_div_two_lt_log_mainCoeffBound`: A log corollary of sqrt_lt_floor rather than the same statement; realPower and logFloor remove project coefficient representation. No independently rederived inline counterpart found.

Completed `Roth.two_lt_rpow_aux`: Shares the square-comparison method with public four_lt_rpow, but strictlog2 premise/target2 differs from sufficient3 premise/target4. Keep the distinct local interface; no inherited upstream verdict.

Completed `Roth.three_small_factors`: The local key repeats one power/log transport for three bases. sqrt_lt_floor and mul_log_div_two_lt_log_mainCoeffBound are prerequisite floor and logarithm estimates, not the same proposition; no independent inline rederivation found.

Completed `Roth.exists_norm_coeff_reduction_aux`: One leading-term elimination and coefficient-budget step, distinct from the iterated public remainder estimate. The latter uses strong induction and a saturated natural exponent. No inherited contribution verdict.

Completed `Roth.norm_coeff_modByMonic_le`: The private reduction is one step of this theorem; diagonal Hasse remainder estimate is a genuine downstream specialization, not a duplicate. Factor/root bounds are different statements.

Completed `Roth.boxFamily_eq_image_finsupp_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.boxFamily_finite`: Shares the coefficient-array representation with Roth.ncard_boxFamily; finiteness and counting are different statements. It is not a duplicate of finite degree-index sets or nonzero bounded families.

Completed `Roth.ncard_boxFamily`: Shares enumeration with boxFamily_finite and exponent count with card_box; neither counts polynomial coefficient assignments. Enumerated count is a short closing simp composition; semantic bridge and finprod transport remain distinct.

Completed `Roth.floor_rpow_count_lt_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.pigeonhole_count`: {'other': 'Roth.floor_rpow_count_lt_aux', 'same_statement': False, 'same_proof': False, 'action': 'Keep scalar floor bound distinct from exponent-budget lifting.'}, {'other': 'Roth.exists_ne_modByMonic_eq', 'same_statement': False, 'same_proof': False, 'action': 'Keep arithmetic size comparison distinct from finite pigeonhole existence.'}

Completed `Roth.exists_ne_modByMonic_eq`: Generic collision duplicates Fintype pigeonhole only after a substantive polynomial encoding and project box cardinality bridge; pigeonhole_count supplies the budget and ncard_boxFamily supplies source size, neither is the same theorem.

Completed `Roth.sub_mem_RSet`: Only scalar/degree/nonzero leaves coincide with existing mathlib theorems. The complete membership tuple is not identical to any one of them; a new scratch generic interval helper is a specialization route, not existing API.

Completed `Roth.eval_hasseDeriv_sub_eq_zero`: Equal-remainder evaluation is a short chain of existing polynomial evaluation laws, but the full mapped-Hasse-diagonal conclusion requires coefficient/evaluation normalization. Parent diag is one-call aeval; diag_sub is map_sub; Hasse and its transport were accepted YES separately. No verdict inherited.

Completed `Roth.le_index_of_forall_eval_eq_zero`: le_index_iff supplies unrestricted nonzero-derivative bounds, not bounded checking., eq_sum_box_hasseDeriv and degreeOf_taylor_le share out-of-box annihilation but conclude reconstruction/support confinement., exists_hasseDeriv_eval_ne_zero is the complementary strict upper-cutoff witness theorem.

Completed `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`: Related theta_lt_eta_of_sq_log_bound_aux repeats square clearing with weak hypotheses/conclusion; not an exact duplicate or actual caller.

Completed `Roth.exists_hasseDeriv_eval_ne_zero`: Strict-cutoff consequence of Roth.exists_weight_eq_index, Contraposition of Roth.le_index_iff, Existing Finset.inf_lt_iff re-aim law

Completed `Roth.abs_eval_iterated_hasseDeriv_lt_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_hasseDeriv_index_eval_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_mem_RSet_le_index_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.mul_card_filter_weight_le_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_mem_RSet_le_index_of_log_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_auxiliary_polynomial_of_log_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.theta_lt_eta_of_sq_log_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_auxiliary_polynomial_with_index_gap_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.main_lemma`: Private construction/selector lemmas factor the proof; they are not duplicates of the complete named lemma or existing mathlib. New numerical_envelope exposes semantic budgets and recovers old statement exactly.

Completed `Roth.approxSet`: Related to reduced rational-height conditions in roth_rat and uniform lower-bound IsDiophantine, with different representation/quantification. No exact bypassing duplicate was found.

Completed `Roth.exists_nat_mul_isIntegral`: Separation.exists_nat_smul_eq_map clears rational polynomial coefficients and is not the same theorem: integral scaled root additionally requires monic normalization.

Completed `Roth.approxSet_den_le_finite`: Comparable finite-fiber reasoning inside exists_reduced_approx additionally needs irrationality and positive-exponent decay to bound unreduced representations of a fixed rational. These are distinct facts.

Completed `Roth.eventually_div_rpow_lt`: Internal calculation in LiouvilleWith.frequently_lt_rpow_neg uses same exponent-gap absorption; not identical exported theorem.

Completed `Roth.reduction`: Powergap and integral scalar prerequisites are existing project abstractions, not duplicate reductions. exists_reduced_approx uses rational reduction/fiber finiteness; this theorem uses injective numerator scaling and finite subtraction, a different map.

Completed `Roth.exists_monic_aeval_eq_zero`: IsIntegral is the standard monic-annihilator existential without degree padding; irrational-root degree bound needs an extra irrationality premise and cannot replace this theorem. No second project padding theorem found.

Completed `Roth.approxSet_num_den_mem_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_reduced_approx`: Rat.num_div_den/Rat.reduced cover representation only. Dirichlet2 covers the subcritical existence regime; LiouvilleWith changes existential constant/equality exclusions; IsDiophantine is uniform lower bounds for every epsilon, not this pointwise lemma.

Completed `Roth.exists_m`: Shares small-parameter selection theme with exists_delta/exists_delta_bound, but chooses natural dimension at infinity rather than a realδ near0; no duplicate conclusion.

Completed `Roth.exists_delta`: Shares neighborhood shrinking with exists_delta_bound, but adds independent quotient continuity and slack. No separate actual inline reconstruction found.

Completed `Roth.exists_approximants`: Reduced selector supplies arithmetic existence; target adds recursive finite selection and strict log growth. exists_degrees consumes that output and has a different rounding/balancing argument. No separate source inline rederivation found.

Completed `Roth.exists_degrees`: {'a': 'Roth.exists_degrees', 'b': 'Roth.exists_approximants', 'same_statement': False, 'same_proof': False, 'verdict': 'Complementary denominator selection versus degree rounding; do not unify.'}, {'a': 'Roth.exists_degrees', 'b': 'Nat.ceil_lt_mul', 'same_statement': False, 'same_proof': 'Partial ceiling estimate only', 'verdict': 'Reuse scalar candidate in future cleanup; finite synchronization/separation is new proof.'}, {'a': 'Roth.exists_degrees', 'b': 'tendsto_nat_ceil_mul_div_atTop', 'same_statement': False, 'same_proof': 'Asymptotic version of one-coordinate rounding', 'verdict': 'A finite quantitative theorem still needs scale selection and arithmetic assembly.'}

Completed `Roth.one_le_prod_pow_mul_abs_eval`: Shares discrete integer separation with Theta coefficient estimates and univariate Liouville bound; not the same statement. Taylor upper bound is complementary, not duplicate.

Completed `Roth.abs_prod_pow_le_rpow_of_le_weight`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.abs_eval_lt_of_le_index`: Finite triangle/strict sum/rpow components only. Univariate Taylor and natural-weight ENat power-series order do not supply the quantitative finite multivariate upper estimate. Distinct from simple abs_eval_le and denominator lower bound.

Completed `Roth.exists_roth_parameters_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.exists_roth_approximants_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.one_lt_roth_eval_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.roth_product_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.roth_log_bound_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `Roth.roth_of_isIntegral`: Roth.roth is reduction-based algebraic extension; Roth.roth_rat and LeanEval endpoint are equivalent public formulations with genuine representation bridges, not independent copies of the proof.

Completed `Roth.roth`: Integral Roth is the proof core, general algebraic endpoint adds substantive scaling/exponent-loss transport; rational-value and uniform lower-bound endpoints are equivalent formulations for irrational α through genuine bridges.

Completed `Roth.roth_rat`: Same Roth theorem endpoint as Roth.roth with distinct representation semantics; pair irrationality remains necessary. LeanEval uniform strict constant bound is distinct.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`: Related to Roth.approxSet infinitude cutoff through a substantive bridge, not defeq.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`: The structural review distinguishes this helper from adjacent construction and numerical-estimate stages; no duplicate full construction is introduced.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`: Shares exponent-gap and finite-denominator tools with Main.reduction; these serve different statements. Private positive-minimum helper supplies one direction; no duplicate full equivalence found.

### Complete semantic comparison evidence

The [module-pair table index](.mathlib-quality/overview/evidence/final/pairwise/README.md) links every full comparison table and its adjacent source/report-hash evidence. All42778 comparisons retain their full mathematical relationship and action. These are reviewed mathematical judgments, not machine proofs of inequivalence.

## Part 5: Generalization opportunities

The completed assessment compiled an optional extension accepting an arbitrary upper-index
function instead of a Finsupp. It is not needed for the standard monomial API and does not
create independent upstream content. No production change is recommended during this review.

The derivative already uses arbitrary variable types and commutative-semiring coefficients.
The rejected `Semiring` experiment fails at `MvPolynomial` itself; no weakening is proposed.

Completed `MvPolynomial.hasseDeriv_monomial`: No verified hypothesis weakening; CommSemiring floor confirmed. Natural-index/Laurent widening changes domains. Q8 points to already-existing abstract evaluation theorem.

Completed `MvPolynomial.hasseDeriv_apply`: No verified hypothesis weakening; Semiring floor cannot form current operator. Q8 identifies existing arbitrary-family lsum_apply abstraction; unrelated higher derivations are not this fixed coordinate operator.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: No coefficient assumptions, arbitraryσ. Verified expanded theorem permits upper k:σ→ℕ; lower d supplies finite product support. Existing hasseCoeff signature fixes upperFinsupp, so realize widening by broader product statement or parent API change. Arbitrary-ring cast iff rejected.

Completed `MvPolynomial.coeff_hasseDeriv`: Maximal for pinned MvPolynomial CommSemiring domain. A Semiring-only domain is compile-rejected. Generic weighted L helper verified but optional; bundled lcoeff/function forms verified and less convenient at current rewrite callers.

Completed `MvPolynomial.hasseCoeff_eq_prod`: Verified expanded version accepts arbitrary upper k:σ→ℕ with the same proof. Generic factor/CommMonoid and finite ambient-set forms already exist in mathlib. The literal full ∏j expression needs Fintype; upper-function widening needs no new product construction.

Completed `MvPolynomial.hasseDeriv_zero_apply`: Current interface already arbitrary σ and CommSemiring. Unnormalized arbitrary linear maps, general zero-order differential operators, or general-codomain HS zero homomorphisms need not be identity; counterexample compiled.

Completed `MvPolynomial.hasseDeriv_zero`: Current operator interface already arbitrary-variable CommSemiring. Module-valued/general higher-derivation families require new definitions; no verified one-edit weakening. False arbitrary-linear-map identity formally refuted.

Completed `MvPolynomial.hasseDeriv_C`: Already arbitrary-variable commutative-semiring interface. Abstract HS-system packaging would require parent redevelopment. No verified mechanical weakening; d=0,C1 formal counterexample.

Completed `MvPolynomial.hasseDeriv_map`: Optional additive coefficient-map companion verified with AddMonoidAlgebra.map. Fixed RingHom map interface remains canonical and literature-compatible.

Completed `MvPolynomial.hasseDeriv_rename`: Actual collision counterexample proves global injectivity cannot simply be dropped; support-local injectivity plausible but no verified weakening. Embedding/square variants equivalent; literal Semiring interfaces fail.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Arbitrary variable type and natural multi-indices; no R/CommSemiring argument in actual replay type; no unverified wider cocycle claim.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: MAXIMALLY GENERAL for pinned canonical interface: CommSemiring, arbitrary variable types, indices and polynomial; literal Semiring parent fails.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: MAXIMALLY GENERAL for geometric support-separation corollary; scalar-cast-one criterion verified strictly weaker in characteristic2 and already subsumed by unrestricted parent law.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Arbitrary variable type, distinguished variable and natural multi-indices; no ring assumptions in actual replay type.

Completed `MvPolynomial.pderiv_hasseDeriv`: MAXIMALLY GENERAL for canonical pinned polynomial/pderiv interface; arbitrary variables, semiring, order and input. Literal Semiring parent fails.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: All arguments already broad within parent CommSemiring interface; conclusion not maximally strong. Same-argument degree-minus-order bound verified and strictly improves X³ witness.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: MAXIMALLY GENERAL fixed CommSemiring parent interface; strictness essential. Stronger support/coefficient zero criteria are companions; existential j wrapper syntactically equivalent.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Arbitrary variables and commutative semiring; arbitrary c,g; exponent separation on support d sufficient, no necessity or unverified weakening claimed.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Current fixed-parent signature maximally general. Vars-disjoint equivalent and symmetric-side companion tested; abstract sum extension tested with actual compatibility premise.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: No verified weakening under canonical parent; bundled square is equivalent.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: No strict weakening verified; Subsingleton plus a chosen variable repackages Unique. Inverse/bundled forms equivalent.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Verified same conclusion with hk only on d.support; stronger support-sum form needs no Fintype. Raw finite-set form uses ordinary functions.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: MAXIMALLY GENERAL for fixed CommSemiring MvPolynomial/pderiv interface; no verified literal weakening. Q8 fires; meaningful shared induction extraction compiled with two consumers, but not mandatory replacement of canonical coordinate compatibility theorem. Concrete recurrence obligations remain.

Completed `Roth.box`: Verified classical DecidableEq-free and Finite-only versions; finite-support bounds allow infinite ambient variables; unrestricted constant1 infinite box refuted natively.

Completed `Roth.weight`: Native arbitrary-index finite-support and AddCommMonoid M forms, Finite-only old syntax and arbitrary real denominators verified.

Completed `Roth.mem_box`: Existing generic interval; finite-only and arbitrary finite-support bounds verified after parent reaim.

Completed `Roth.card_box`: Mapped arbitrary dependent finite coordinate sets; support-indexed lower intervals. Already existing APIs. Scoped Classical hides decision instance rather than proving independence.

Completed `Roth.card_le_card_box`: Dependent finite coordinate FUNCTION-family form already composable; arbitrary ambient Finsupp finite-support upper-bound form verified. Support-local hs is equivalent, not strictly weaker.

Completed `Roth.weight_nonneg`: No unused original binder; larger formula and Finsupp representations compiled with ordinary families, finite subsets, nonnegative real denominators, ordered fields, arbitrary ambient variable types and ordered additive monoids. Signed-denominator false generalization rejected.

Completed `Roth.weight_zero`: Existing arbitrary ambient Finsupp.weight in AddCommMonoid and DivisionSemiring finite formula verified; no fixed-parent binder removal.

Completed `Roth.weight_add`: Current parent-interface constraints fixed; verified finite functions in DivisionSemiring and arbitrary semiring-coefficient module-valued Finsupp weights, including infinite ambient types.

Completed `Roth.weight_eq_zero_iff`: Verified support-local positivity; verified generic ordered-additive Finsupp.weight and ordered-field denominator representations.

Completed `Roth.weight_single`: Native finite_kernel permits arbitrary zero-preserving kernels; finite_division permits DivisionSemiring values and arbitrary denominators. Bundled Finsupp.weight drops ambient finiteness and has existing API. These replace the parent representation, not a mechanical weakening of Roth.weight.

Completed `Roth.weight_le_card`: Strictly weaken bounds to nonzero-denominator coordinates; support localization equivalent; support.card stronger conclusion; Finsupp representation drops ambient finiteness; ordered-field finite-function representation compiled.

Completed `Roth.weight_mul_left`: Native arbitrary semiring/module generator scaling without Fintype; arbitrary Field finite-set denominator identity; unchanged Roth interface is maximally general in hypotheses.

Completed `Roth.weight_le_degree_div`: Verified support-local and conditional nonzero-denominator hypotheses; arbitrary ambient index set; ordered Semifield reciprocal-weight comparison. hm cannot be dropped: Unit m0,r1,d1.

Completed `Roth.weight_mapDomain`: Drop hf in unchanged statement; on existing parent Finsupp.weight drop both Fintype instances, permit semiring coefficients and arbitrary module values.

Completed `Roth.wronskianMatrix`: Verified Field→Semiring for standalone same-body definition., Verified arbitrary rectangular row-order matrix specializes by rfl., Verified bundled R-linear operator specializes by rfl and provides map_add.

Completed `Roth.wronskian`: Expanded standalone body CommRing verified; unchanged Field-only matrix parent prevents literal binder-only drop. Arbitrary finite selected orders verified separately.

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: Expanded determinant theorem verifies CommRing+NoZeroDivisors including zero ring; fixed public parents still require Field. Generic scalar-linear-family version verifies CommSemiring base, domain CommRing target, AddCommMonoid source, faithful algebra action.

Completed `Roth.det_choose_eq`: Verified exact quotient under local nonzero factorials; stronger arbitrary CommRing identity factorial-product * det(choose) = Vandermonde product, including zero ring. Char2 size2 positive specialization and size3 failure guard compile.

Completed `Roth.coeff_prod_of_natDegree_le'`: Verified same-body Field→CommSemiring, no domain/nontriviality/characteristic/finite-ambient restriction.

Completed `Roth.sum_range_le_sum_of_injective`: Arbitrary finite index type and integer-valued injective family with common lower bound c verified natively; existing finset theorem already covers it. Injectivity is necessary, verified Fin 2 constant-zero counterexample.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Native verified expanded CommRing identity for arbitrary finite ι and arbitrary r : ι → ℕ; original Field form and sole caller recovered. Does not claim literal Field deletion through project parent interface.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: Verified same-parent Field weakening removes global CharZero in favor of cast-degree injectivity. Separately verified expanded CommRing+IsDomain form. No factorial-nonzero premise needed. ZMod2 positive and negative guards; ZxZ zero-divisor guard.

Completed `Roth.wronskian_update_sub_smul`: Raw [CommRing R], arbitrary finite index and selected Hasse orders verified; existing parent interface remains Field-bound.

Completed `Roth.linearIndependent_update_sub_smul`: Ring R; arbitrary AddCommGroup M with Module R M; arbitrary index; arbitrary coefficient function vanishing at source; iff. Already available.

Completed `Roth.sum_natDegree_update_lt`: Compiled Field→DivisionRing, arbitrary Fintype index, replace global LI and distinctness by local nonzero difference or positive common degree.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: Expanded CommRing+IsDomain+CharZero determinant theorem completely verified by fraction-field descent using explicit Field proof replay. Current Roth.wronskian is Field-bound, so this is a new theorem/interface decision rather than mechanical hypothesis weakening. CharZero drop refuted by compiled independent [1,X²] over ZMod2 with zero determinant.

Completed `Roth.wronskian_eq_zero_iff`: Complete expanded CommRing+IsDomain+CharZero iff compiled using fraction-field hard proof plus generic easy direction, and recovers original Field iff. Changing fixed Field parent interfaces is Class5, not a one-edit weakening. Compiled ZMod2 and CharZero product-ring counterexamples reject dropping CharZero and IsDomain.

Completed `MvPolynomial.taylor`: Already maximally general in this MvPolynomial/AlgHom representation; generic substitutions already aeval. Ring-only AlgEquiv is complementary infrastructure, not weakening.

Completed `MvPolynomial.taylor_apply`: Maximally general relative to the existing CommSemiring/AlgHom parent interface; arbitrary substitution already aeval; no verified strict weakening claimed.

Completed `MvPolynomial.taylor_X`: Maximally general relative to fixed parent interface. Expanded arbitrary-target/assignment representation already exists as aeval_X and is verified; no assumption weakening claimed.

Completed `MvPolynomial.taylor_C`: No same-interface assumption-drop opportunities; already-existing broader representation verified. No unverified weakenings.

Completed `MvPolynomial.taylor_monomial`: Already general over CommSemiring at fixed taylor interface; arbitrary assignment and target commutative algebra form already exists.

Completed `MvPolynomial.coeff_aeval_X_mul`: Already arbitrary variables/commutative semiring, f,B,d; no successful weakening proposed. hB is the coordinate-independence premise used to discard other summands.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Only variable type and natural exponent data occur in actual native type; zero R/Fintype/DecidableEq assumptions. No unverified weakening of residual-coordinate hypothesis.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Native verified CommSemiring R to CommMonoid M with unchanged proof body; original source remains unchanged in read-only overview.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Native type needs no Fintype/DecidableEq/field/charzero/nonzero or npositive hypotheses; no additional weakening or circular use of later coeff_taylor claimed.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Native type already arbitrary variables/commutative semiring; no leftover k_i=0 or IH in final statement; no circular weakening using later theorem.

Completed `MvPolynomial.coeff_taylor`: Already commutative semiring/arbitrary variable generality; bundled and base-change forms verified derived companions.

Completed `MvPolynomial.eval_taylor`: No removable assumptions in fixed interface; arbitrary R-algebra target checked natively as expanded representation.

Completed `MvPolynomial.taylor_taylor`: Already arbitrary-variable CommSemiring interface; no removable assumptions. Bundled AlgHom composition verified; additive action or ring AlgEquiv is prospective structure, not an existing replacement.

Completed `MvPolynomial.taylor_zero`: Already general within parent CommSemiring interface. Arbitrary-algebra zero-perturbation of any assignment verified separately; no unverified class weakening.

Completed `MvPolynomial.taylor_map`: Maximal within fixed parent CommSemiring interface; arbitrary substitution/variable target is already existing mathlib. Bundled RingHom square verified without adding assumptions; no verified parent weakening.

Completed `MvPolynomial.taylor_rename`: Maximal within parent CommSemiring interface; bundled AlgHom square and arbitrary target-algebra evaluation verified. No mechanical weakening established.

Completed `MvPolynomial.degreeOf_taylor_le`: Maximal within CommSemiring parent interface; CommRing equality via inverse is a separately verified stronger specialization, not assumption weakening.

Completed `MvPolynomial.taylor_neg_taylor`: CommRing is the fixed negation/cancellation interface floor. Conditional mutually cancelling shifts over CommSemiring are an expanded statement, not dropping ring assumptions from unchanged negative-shift law.

Completed `MvPolynomial.taylor_injective`: No verified unchanged-signature mechanical weakening. Conditional semiring inverse-pair injectivity verified. Bare CommSemiring weakening refuted by WithTop Nat shift top colliding X+C1 and X+C2. Cancellative semiring alternatives not tested; no absolute minimality claim.

Completed `MvPolynomial.taylor_eq_zero_iff`: Verified CommRing→CommSemiring same statement and parent with replacement 28-line maximal-support/Hasse argument, not unchanged-body mechanical deletion. All measured consumers checked. Semiring injectivity remains false and is not claimed.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Verified no explicit DecidableEq binder using open Classical in statement plus proof-local classical. Old arbitrary instance recovered by Subsingleton.elim and cases; propositional, not definitional transport. Fintype retained for full product and box. Raw arbitrary-variable support expansion is a different representation, not this same statement.

Completed `MvPolynomial.eval_eq_sum_box`: Strongest verified: coefficient CommSemiring A, arbitrary independent-universe CommRing A-algebra B, BOTH α/x : σ→B, aeval α derivative values. No explicit DecidableEq via scoped Classical; original CommRing A=A/arbitrary instance recovered propositionally by Subsingleton.elim/cases. Degree bound after coefficient map proved by support_map_subset; uses hasseDeriv_map and eval₂_eq_eval_map. Fintype, natural exponents and degree bound retained. Earlier center-in-A algebra law is intermediate.

Completed `Roth.normOne`: Verified CommSemiring R + Norm R coefficient sum and integer recovery; arbitrary Zero coefficient / AddCommMonoid value / arbitrary index Finsupp aggregation with exact rfl recovery. Arbitrary Norm data does not imply norm axioms. Universe/lifted-index and existing metric synthesis tested.

Completed `Roth.diag`: Verified CommSemiring R, independent arbitrary variable universe, exact ℤ specialization, empty/lifted variables and arbitrary commutative R-algebra evaluation. Bool/ℤ noninjectivity proved; no degree equality or equivalence claimed.

Completed `Roth.normOne_nonneg`: Fixed parent interface has no removable assumptions. Verified expanded formula to arbitrary Zero coefficients and ordered additive monoid sizes, requiring nonnegativity only on support; norm-coefficient specialization also verified.

Completed `Roth.normOne_eq_sum_of_support_subset`: No removable assumptions at fixed normOne interface. Expanded indexed zero-preserving coefficient size over Zero R/AddCommMonoid S verified; zero premise can be restricted further to added positions; norm-coefficient version verified.

Completed `Roth.normOne_monomial`: Fixed normOne interface has no removable assumptions. Expanded indexed zero-preserving size theorem and arbitrary Finsupp form verified; norm coefficient version verified. Local premise only size e0=0 needed; removing it false for coefficient0.

Completed `Roth.normOne_zero`: Fixed parent interface no assumptions to weaken. Expanded generic Finsupp/polynomial laws verified; sizeZeroUnnecessary guards removal of unnecessary size-zero premise.

Completed `Roth.abs_coeff_le_normOne`: Existing law permits arbitrary index α, Zero M, AddCommMonoid N, PartialOrder N, IsOrderedAddMonoid N, zero-preserving nonnegative g. Fresh lattice-ordered additive-group abs form compiled. New exploratory helper further weakens target order to Preorder/AddLeftMono and nonnegativity to actual support values, verified in isolated native general set; this new proof is not an existing replacement and does not alter original exact-hit verdict.

Completed `Roth.normOne_add_le`: Fresh generic AddZeroClass coefficient/ordered additive Preorder output indexed-size theorem; broader nonnegative-at-zero form also verified, including constant1 support cardinality. No claim of class-minimality.

Completed `Roth.normOne_neg`: Fixed parent interface has no droppable premises. Verified general indexed-size form over SubtractionMonoid coefficients and AddCommMonoid output with hzero and hneg; assumptions sufficient, not claimed minimal.

Completed `Roth.normOne_sum_le`: Fixed normOne interface maximal; expanded generic Finsupp-weight finite bound verified over arbitrary additive commutative coefficient monoid and ordered additive target.

Completed `Roth.normOne_mul_le`: Verified expanded CommSemiring coefficient size with zero/subadditivity/submultiplicativity; parent fixed interface has no droppable hypotheses.

Completed `Roth.normOne_prod_le`: Expanded genericProd verified over CommSemiring with nonnegative coefficient size, size1≤1 and zero/subadditive/submultiplicative laws; abstractProd verified arbitrary CommMonoid.

Completed `Roth.normOne_le_card_mul`: Support-only hB and arbitrary AddCommMonoid/Preorder/AddLeftMono codomain compile; existing mathlib law covers both.

Completed `Roth.normOne_det_le`: Verified arbitrary CommRing R, existing RingSeminorm p with p1≤1, arbitrary Fintype n; exact normOne specialization packaged and compiled.

Completed `Roth.abs_coeff_hasseDeriv_le`: Verified arbitrary CommRing R with AddGroupSeminorm R, followed by exact integer absolute-value specialization.

Completed `Roth.normOne_hasseDeriv_le`: Native-verified arbitrary CommRing R and AddGroupSeminorm R coefficient sum; exact int recovery. MODERN-IDIOM.

Completed `Roth.diag_eq_sum`: Verified CommSemiring R coefficient expansion with aeval; no need finite σ. Current diag remains fixed at ℤ.

Completed `Roth.abs_coeff_diag_le`: Verified CommSemiring coefficients, arbitrary subadditive size map and ordered additive monoid codomain; CommRing AddGroupSeminorm specialization. Stronger support-fiber sum/cardinality and fiber-local hypothesis recover original.

Completed `Roth.natDegree_diag_le`: Expanded statement verified for arbitrary CommSemiring R; totalDegree bound removes Fintype; integer parent interface unchanged.

Completed `Roth.eval_diag`: Compiled arbitrary CommSemiring R,S with f:R→+*S and Algebra aeval forms. Parent diag remains ℤ-specific.

Completed `Roth.diag_sub`: Expanded arbitrary CommRing diagonal and arbitrary algebra substitution compile; generic AddGroupHom law also compiles.

Completed `Roth.geom_sum_le_one_add_pow`: Verified noncommutative ordered semiring; no CharZero, no linear order; ht essential (t=-1,r=2).

Completed `Roth.sum_box_prod_pow_le_aux`: Finite variable enumeration, natural coordinate bounds, nonnegative real B and arbitrary real coordinates are explicit. No assumption weakening or broader public contribution is claimed under private triage.

Completed `Roth.abs_eval_le`: Verified strongest primary form: arbitrary CommSemiring R coefficients, CommSemiring S evaluation, ordered CommSemiring T output with PartialOrder and IsOrderedRing, FunLike F S T and existing Zero/Nonneg/Subadditive/Submultiplicative hom classes. Original ℤ/ℝ map input and full private caller specialize cleanly. No unit-size bound, injectivity, domain, total order, strict order or negation premise.

Completed `Roth.degreeOf_det_hasseDeriv_le`: CommRing coefficients, arbitrary finite matrix index, fixed-coordinate scalar bound verified. Factor generic entry/column determinant bounds.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Verified RingSeminorm over arbitrary CommRing, normalized at1, arbitrary finite matrix index; omit hB0.

Completed `Roth.genWronskian`: Native verified CommRing R and arbitrary finite square index; original specialization rfl. Variables already arbitrary. Semiring-N signed determinant guard rejects further weakening.

Completed `Roth.kronecker`: CommSemiring coefficients and arbitrary explicit ranks/weights verified; existing aeval is already more general. Hidden enumeration is noncanonical and changes the substitution.

Completed `Roth.kroneckerExp`: Existing arbitrary-index weight removes Fintype only when explicit weights replace chosen equivFin; generic semiring coefficients/module target compiled. Original chosen positional interface retains Fintype; coefficient Field is already absent.

Completed `Roth.kronHasse`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.kronSpan`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: Verified arbitrary finite index, CommRing+NoZeroDivisors polynomial coefficients; semiring base/module source abstract operator family with domain target/faithful scalar action. Plain ring false via ℤ×ℤ singleton.

Completed `Roth.kronecker_monomial`: Compiled arbitrary-σ CommSemiring weighted theorem and arbitrary commutative target algebra evaluation; fixed geometric enumeration remains a project representation choice.

Completed `Roth.kroneckerExp_injOn`: Checked explicit e:σ≃Fin n with proof-local Fintype and arbitrary k (no hk). Fixed original-interface no-hk bridge checked. Infinite-position injective maps and mixed radix considered but not claimed compiled.

Completed `Roth.coeff_kronecker`: Verified arbitrary sigma, CommSemiring, arbitrary weights with support-local InjOn; explicit finite enumeration and no hk positional specialization also checked.

Completed `Roth.kronecker_eq_zero_iff`: Verified CommSemiring, arbitrary σ and weights with support separation; positional explicit e and no hk; literal parents retain Field/Fintype constraints.

Completed `Roth.linearIndependent_kronecker`: Verified CommSemiring, arbitrary family index, arbitrary weighted variable set; explicit finite enumeration and no k>1 for positional theorem.

Completed `Roth.derivative_aeval`: Verified Field→CommSemiring; arbitrary algebra/module-valued derivation; arbitrary-variable finite-support sum over P.vars.

Completed `Roth.derivative_kronHasse_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.derivative_mem_kronSpan`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.hasseDeriv_kronecker_mem`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Verified arbitrary γ : σ → Polynomial R, CommSemiring R + Algebra ℚ R, Finite σ. Original specialization and actual sole caller compile. Characteristic-independent primary literature formula not claimed compiled.

Completed `Roth.det_sum_rows`: Verified arbitrary finite square J and dependent I:J→Type*, original Fin l recovery. Abstract CommSemiring module-valued weighted expansion verified separately; determinant itself still requires CommRing.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_genWronskian_ne_zero`: Verified deletion of Finite σ, using finite union of vars, LI.of_comp, derivative rename, degree_mapDomain and determinant rename. Direct one-edit replay fails at Fintype.ofFinite. Domain/fraction-field and formal-series extensions remain distinct unverified proposals.

Completed `Roth.sqrt_one_sub_inv_lt`: Verified candidate: real m≥1, nonstrict 2√m≤lam, still strict conclusion. Does not claim optimal hypotheses.

Completed `Roth.inv_add_inv_le`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.sum_inv_le`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.sum_inv_lt`: Verified real m>1 and weak2√m≤lam preserve strict conclusion; both private pair/grid proofs work for1<lam. Independent raw proof and sole caller replay clean.

Completed `Roth.extend_apply_castSucc`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.extend_apply_last`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_box_fiber_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_box_last`: Native generic finite α/β fibre map, arbitrary filtered product, dependent finite tuple sections and scoped classical predicate-decision removal. Independent tuple theorem does not claim complete recovery of original spelling.

Completed `Roth.filter_weight_le_eq_empty`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_fiber_eq`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_weight_le_succ_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_weight_le`: Arbitrary universe-polymorphic Fintype index transport actually compiled; expanded piFinset ordinary-sum form with DecidableEq and original Fin/Finsupp recovery compiled. These are new project-dependent proofs; no droppable original premise found.

Completed `Roth.index`: Verified arbitrary variable types, CommSemiring coefficient type, arbitrary real weights via finite support; Fintype dependence belongs only to the current weight interface.

Completed `Roth.mem_support_taylor_iff`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.index_le_weight`: Compiled abstract Semiring/any support-degree map/any SemilatticeInf OrderTop target, and translated CommSemiring arbitrary-variable arbitrary-real-degree version without Fintype.

Completed `Roth.exists_weight_eq_index`: Verified Semiring coefficients, arbitrary ambient support type with no Fintype, arbitrary degree map into any LinearOrder/OrderTop target with independent universes; separately verified real default-zero projection.

Completed `Roth.le_index_iff`: Verified arbitrary Semiring coefficients, arbitrary degree map and ambient support index type, arbitrary SemilatticeInf+OrderTop codomain; no nonzero hypothesis in unprojected law.

Completed `Roth.index_nonneg`: Verified Semiring coefficient carrier with arbitrary support index type, arbitrary degree map to SemilatticeInf+OrderTop and arbitrary lower bound c. Projected real nonnegative law verified for all P with support-local nonnegative D.

Completed `Roth.index_eq_zero_iff`: Expanded arbitrary Semiring coefficients/support carrier/distinguished exponent/bounded linear target; degree bottom iff distinguished exponent. Real degrees need nonnegativity and zero-fiber control; no unchanged-parent mechanical drop.

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Verified standalone projectedInfDegreeShift and expandedProjectedShift over arbitrary sigma, CommRing R, real degree D with D(i+k)=D(i)+D(k). supportShift separately CommSemiring. Parent fixed-interface restrictions are not claimed mechanically deleted. Infinity-preserving and general ordered-target variants remain optional unverified extensions.

Completed `Roth.le_index_sum`: Verified Semiring R, arbitrary support A, degree D:A→T and SemilatticeInf/OrderTop target, no finiteness on A or sum-nonzero premise in top-valued law. Point aeval projected form verified over CommRing and arbitrary sigma. Fixed parent restrictions are not silently deleted. Zero-default real projection retains sum nonzero; X+(-X) guard confirms cancellation necessity.

Completed `Roth.weight_eq_finsuppWeight_div`: Arbitrary Semifield K; nonzero cast common denominator and divisibility only on d.support; no ambient Fintype or CharZero needed in strongest accepted form. Generic parent law has arbitrary semiring coefficients and module targets.

Completed `Roth.index_eq_weightedOrder_div`: named weakening: delete hP, independently compiled zero case; expanded representation: CommSemiring/arbitraryσ/allP/assigned naturalw weightedOrder_coe, verified mathlib-only; projection scaling: scaledInfDegree real D≥0 including0/allP, verified; rejected: uniform hr removal false; arbitrary real w not same natural weightedOrder; negative real scaling not min-preserving

Completed `Roth.index_mul`: Verified exact-interface deletion of hr. Expanded natural-series law removes Fintype, ℝ, Taylor center, positivity and factor nonvanishing via infinity at zero; compiled. Broader arbitrary-real polynomial infDegree multiplication is a design proposal, not a compiled weakening.

Completed `Roth.index_prod`: Verified deletion of hr while preserving the exact conclusion. Natural-series and polynomial formulations remove finite-variable and real-coefficient restrictions, using infinity at zero. Arbitrary-real ordered polynomial extension is a proposal only.

Completed `Roth.index_neg`: Verified expanded representation arbitrary Ring coefficients, exponent type and degree map into semilatticeinf/top. No claim Fintype can drop from unchanged parent signature.

Completed `Roth.index_C_mul`: Verified arbitrary exponent/degree semilatticeinf/top and coefficient semiring acted on by scalar domain with torsion-free module. This library interface is not logical minimum; zero-preserving injective coefficient maps have existing support_mapRange_of_injective; unit/regular scalar extension not claimed compiled.

Completed `Roth.index_mul_left_weights`: No mechanically droppable hypotheses in fixed Roth interface. Verified expanded law for arbitrary semiring coefficients/A/degree targets and zero-preserving monotone maps; scalar specialization arbitrary ordered semiring and c≥0. Fintype/ℝ changes require parent restatement.

Completed `Roth.index_rename`: Verified expanded law has arbitrary variable types without Fintype, CommSemiring coefficients, additive direct weights into SemilatticeInf AddCommMonoid, WithTop and untopD0. Fixed original parent cannot simply drop its Fintype binders. hf remains essential, verified collision guard.

Completed `Roth.index_le_card`: Verified noNonzero drops hP; oneWitness weakens entire degree box to one nonzero Taylor coefficient in box; weightedWitness accepts arbitrary coefficient weight bound. Mathlib-only realSupport handles arbitrary finite exponent set; infDegreeWitness arbitrary semiring coefficients and grading/order target. Fixed parent interface remains real/Fintype.

Completed `Roth.index_unique`: verified drop: P ≠ 0; finite data: Unique.fintype supplies the Fintype interface; choice independence checked; expanded: Univariate Taylor coefficient minimum over arbitrary CommRing R, real numerical codomain and natural denominators; independently compiled; rejected: Signed scaling without nonnegativity, Unprojected infinite zero order identified with real zero, Arbitrary many-to-one variable collapse

Completed `Roth.coeffNone`: fixed interface: Already arbitrary CommSemiring and variable universes; no finite/equality classes. MvPolynomial carrier requires CommSemiring.; expanded representation: STRICTLY NARROWER representation level: existing Finsupp.comapDomain slices coefficients over Zero; actual native direct_coeff bridge proved. Fixed MvPolynomial carrier requires CommSemiring. Initial sum-filter remains exploratory.

Completed `Roth.eq_mapDomain_some_add_single`: status: STRICTLY NARROWER THAN STANDARD; fixed surface: AddCommMonoid M (mapDomain interface); embedding surface: AddZeroClass M; canonical surface: Zero M; native verified: True

Completed `Roth.coeff_X_none_pow_mul_rename`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.coeff_coeffNone`: status: MAXIMALLY GENERAL for fixed parent interface; canonical surface: CommSemiring R; arbitrary variable type and independent universes; expanded representation: Zero A suffices for underlying coefficient slicing by Finsupp.comapDomain; prior152 actual slice_apply and direct_coeff bridge reused with freshly matching17source/pin hashes. This is a wider representation, not a mechanical weakening of the fixed coeffNone interface.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: status: MAXIMALLY GENERAL for fixed parent interface; canonical surface: Existing finite Polynomial expansion over Semiring A with natDegree p < m.; expanded representation: Generic Semiring A reconstruction actually compiled. Setting A=MvPolynomial τ R gives canonical Option expansion; does not weaken CommSemiring required by fixed parent.

Completed `Roth.degreeOf_coeffNone_le`: status: MAXIMALLY GENERAL for fixed interface; canonical surface: degreeOf j ((optionEquivLeft R τ P).coeff ν) ≤ degreeOf (some j) P; abstract component: Finset support transport with pointwise weight bound implies supremum bound; independently compiled without DecidableEq or coefficient algebra. This is an expanded representation, not weakening CommSemiring in the original.

Completed `Roth.coeff_rename_mul_aeval`: status: MAXIMALLY GENERAL for fixed polynomial representation; verified: Underlying coefficient-times-singleton law holds for arbitrary Semiring S and AddZeroClass M, not just natural multidegrees.; boundary: CommSemiring R is required by existing MvPolynomial interface; abstract AddMonoidAlgebra restatement changes representation. Variable-disjointness cannot be removed, as collision_guard proves.

Completed `Roth.aeval_X_eq_rename`: fixed interface: MAXIMALLY GENERAL; verified weakenings: None; representation extension: Arbitrary Unique index verified by a new hom-ext proof; not counted as existing-call API.; modern idiom: Existing bundled equality already supplies canonical abstract form.; false generalization: Arbitrary replacement of X_i while keeping the chosen-coordinate rename is false; concrete coefficient guard verified.

Completed `Roth.hasseDeriv_rename_mul_aeval`: status: STRICTLY NARROWER representation interface; verified: HasseSeparation160.freshCoordinate; statement: Replace some : τ → Option τ and none by an arbitrary injective f : τ → σ and fresh i : σ satisfying ∀ j, f j ≠ i; no surjectivity/exhaustiveness required.; fixed interface: Original already uses weakest parent interface CommSemiring and arbitrary τ; no typeclass drop claimed.; original specialization: HasseSeparation160.originalFormAgain

Completed `Roth.coeff_uniqueAlgEquiv_symm`: status: More general exponent form already in mathlib; fixed parent interface maximally general; verified: arbitrary finitely supported exponent d, arbitrary coordinate j in Unique σ, representation d=single default (d default); rejected: Semiring alone cannot instantiate the fixed uniqueAlgEquiv algebra interface, Bool variable set lacks Unique; coordinate forgetting does not preserve coefficients

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: Already maximal for fixed CommSemiring/Unique interface; arbitrary coordinate is checked equivalent restatement. Arbitrary selected-variable general law is already in mathlib; Semiring interface drop and Bool uniqueness drop rejected.

Completed `Roth.degreeOf_rename_mul_aeval`: CommSemiring R + NoZeroDivisors R complete proof compiled; arbitrary-degree-zero-factor principle compiled separately; hV and nonannihilation guards compiled. NoZeroDivisors is a sufficient global condition; weakest point-local nonannihilation alternatives are not claimed.

Completed `Roth.degreeOf_none_rename_mul_aeval`: CommSemiring+NoZeroDivisors verified; arbitrary CommSemiring point-local V=0 or U*(V.map C).leadingCoeff≠0 verified. U-nonzero and zero-divisor counterexamples compiled.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_coeffNone_basis_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_separated_representation`: status: verified sufficient scalar weakening; from: Field K; to: CommRing K + IsDomain K + IsPrincipalIdealRing K; preserved: arbitrary τ, hP nonzero, chosen n and hn, 1 ≤ l ≤ n+1, LinearIndependent K φ, LinearIndependent K ψ, all φ natDegree bounds, all ψ coordinate degree bounds, separated reconstruction; not claimed: PID is not claimed the weakest possible scalar condition; given-basis variant is conditional.; primary evidence: separated-repr-isolated-pid-executed.lean.txt / separated-repr-isolated-pid-receipt.json

Completed `Roth.det_hasseDeriv_separated`: Clean native full expanded CommRing law; arbitrary finite square indexι and arbitrary univariate ordersE; injected f:τ→σ plus fresh coordinatei outside its range. Original named full conclusion and sole full caller compile via both ring bridge and strongest fresh-coordinate bridge. Original named Field parents cannot mechanically lower unchanged.

Completed `Roth.exists_sum_mul_eq_gcd`: status: STRICTLY NARROWER THAN STANDARD; verified: CommRing R + IsBezout R + NormalizedGCDMonoid R; independently compiled; abstract ideal form: Ideal.mem_span_range_iff_exists_fun under Semiring R and Fintype ι is also existing; not claimed identical gcd theorem without Bezout.

Completed `Roth.exists_nat_smul_eq_map`: status: Verified broader existing interfaces; polynomial: CommRing R/S + Algebra R S + IsLocalization M S; clear denominator in M.map C.; finite family: CommSemiring A/B + localization; finite coefficient family common denominator.; fixed interface: Exact positive-natural rational/integer specialization retained.

Completed `Roth.exists_primitive_smul_eq`: current: Fixed ℤ/ℚ interface; all variable-type and nonzero assumptions essential or already unrestricted.; expanded: CommRing R + IsDomain R + NormalizedGCDMonoid R, Field K + Algebra R K + IsFractionRing R K, preserving g ≠ 0, map(algebraMap R K) U = g • G, gcd1.; scope: Full normalized-GCD-domain/fraction-field theorem native-checked, preserves every conclusion, no parent-definition migration. Concrete one-call specialization checked separately.; false generalization guard: gcd1 does not imply unit-ideal/unimodular coordinates over arbitrary GCD domains. No arbitrary field unrelated to R, no zero input, no infinite series.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: reason: MODERN-IDIOM; primary: Submodule.gcd_smul_mem; signature: {R M ι : Type*} [CommRing R] [IsBezout R] [NormalizedGCDMonoid R] [AddCommMonoid M] [Module R M] (N : Submodule R M) (s : Finset ι) (u : ι → R) (v : M) (hv : ∀ i ∈ s, u i • v ∈ N) : s.gcd u • v ∈ N; secondary: IsUnit (s.gcd u) implies unscaled membership via existing smul_mem_iff_of_isUnit; original bridge: N = LinearMap.range (Algebra.linearMap ℤ ℚ); convert product witnesses; rewrite gcd=1; return integer witness with equality symmetry; guard: Arbitrary GCD rings need not be Bezout; no claim that gcd1 implies unit ideal without Bezout.

Completed `Roth.rescale_separated_factor_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_int_factors`: status: Verified full GCD-domain/fraction-field proof, exact concrete specialization and entire sole caller.; signature: variable {τ R K : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    [Field K] [Algebra R K] [IsFractionRing R K]
theorem exists_separated_factors {U' : MvPolynomial τ K} {V' : Polynomial K} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) R} (hF : map (algebraMap R K) F =
      rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) K) V') :
    ∃ (U : MvPolynomial τ R) (V : Polynomial R), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree; no IsBezout: True; no UFD: True; all conclusions preserved: True

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_det_eq_mul`: verified: True; coefficient ring: [CommRing R] [IsDomain R] [NormalizedGCDMonoid R] [CharZero R]; variables: arbitrary τ; remove Finite τ by finite-support bridge; fraction field: FractionRing R internal; arbitrary external K variant also proved; preserved: 1 ≤ l, l ≤ r none + 1, ∀ μ, (D μ).degree ≤ μ, U ≠ 0, V ≠ 0, ∀ j, degreeOf j U ≤ l * r (some j), V.natDegree ≤ l * r none, exact determinant factorization; parent interface: Field-only genWronskian remains over fraction field; base-ring Hasse API already valid.

Completed `Roth.RSet`: status: already broad variable/bound parameters; no mechanically droppable instance; verified: Generic degree/support bridge over arbitrary σ and CommSemiring; not a generic arithmetic development.; rejected: Do not replace by total degree, projective height, submodule including zero, or finite box without extra assumptions.

Completed `Roth.indexSet`: status: No mechanically removable class while keeping parent index signature. Existing image2 abstracts independent source/target types and universes. Expanded index representation supports arbitraryσ; finite specialization checked.; rejected: Do not omit nonzero/degree/coefficient/coprimality restrictions, impose positive q in all-input comparison, change default0 to infinity, or replace by submodule/total degree.

Completed `Roth.Θ`: status: No mechanically removable parameter within fixed indexSet interface. Generic outer SupSet already maximally abstract; expanded arbitrary-variable expression without Fintype and its finite specialization actually compile.; rejected: Do not alter full RSet/nonzero/degree/coefficient constraints, coprimality, total q/r zeros, or empty/unbounded real default0; do not apply CompleteLattice-only image2 supremum laws to ℝ.

Completed `Roth.lem6M`: Semiring expression compiles; representation expansion only, not literature-standard replacement or suggested new upstream definition.

Completed `Roth.lem6Φ`: Generic SupSet+Add formula compiled; arbitrary-variable expanded representation compiled. Fintype belongs to fixed Θ parent interface; no new generalization ticket needed for existing outer operations.

Completed `Roth.one_mem_RSet`: Already arbitrary σ and r under fixed RSet. Expanded normalized normed-ring form compiles and specializes back to ℤ via Int.norm_eq_abs; changing fixed RSet is a separate API project.

Completed `Roth.indexSet_nonempty`: Abstract law accepts arbitrary types/sets/total binary maps without Fintype, arithmetic, order or topology. Original hB is sharp: actual indexSet.Nonempty↔1≤B checked via nonzero integer coefficient.

Completed `Roth.indexSet_bddAbove`: No mechanical deletion of target assumptions verified or claimed. Generic structural law works at LE and arbitrary domains; it retains the substantive uniform-bound premise. Parent infDegree/Finsupp.weight representation does not settle full Taylor-degree/cardinality bound.

Completed `Roth.index_le_Θ`: Fixed polynomial interface needs Fintype; expanded generic conditionally complete lattice member law is already le_csSup, verified without Roth imports. Verified expanded allow_zero removes the hidden R≠0 conjunct, handling zero via index0=0 and independent Θ_nonneg; this separate real-default extension does not alter original member-law duplication.

Completed `Roth.Θ_nonneg`: unchanged parent: No extra premise to drop; Fintype fixed by current index interface.; expanded: Arbitrary Set ℝ or arbitrary real two-argument family with pointwise nonnegativity; already existing law.; guard: Negative singleton rules out deleting the nonnegative-value premise; preserve real default0.

Completed `Roth.Θ_le_card`: Verified expanded_family handles arbitrary sets of real multivariate polynomials (including zero) and arbitrary real evaluation points, with only coordinate degree bounds. This changes the parent family/interface; it is not deletion of a hypothesis from the existing Θ statement. Generic supremum law already exists.

Completed `Roth.Θ_le_of_forall_index_le`: Abstract csSup_le handles arbitrary conditionally complete lattices and arbitrary nonempty sets. Fixed Θ/index interface retains Fintype. Replacing hB by 0≤c is verified using Real.sSup_le, and under hc, Θ≤c iff0≤c; no unconditional premise deletion claimed. Actual compiled Roth counterexample at B=0,c=-1 supplies hc vacuously but Θ=0 fails≤-1, so unconditional hB deletion is false; family-only emptiness legitimately omits Fintype.

Completed `Roth.Θ_mono`: verified hypothesis deletion: hB can be dropped for this actual family: Real.sSup_le plus le_csSup, height inclusion, and Θ_nonneg. Native all_bounds/monotone_all verified.; abstract form: csSup_le_csSup over any ConditionallyCompleteLattice, already in mathlib.; interface constraint: Fintype remains needed by Θ/index fixed signatures; removing it from the abstract set theorem is a change of interface.; false generalization guard: Subset alone is false for real sSup: ∅ ⊆ {-1}, with sSup∅=0 > -1. No CompleteLattice/OrderBot instance for ℝ assumed.

Completed `Roth.indexSet_comp_subset`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.Θ_equiv`: No mechanical weakening established under fixed Theta/index signatures. Candidate reusable core is renameEquiv transport of nonzero polynomials with separate coordinate degree caps and arbitrary coefficient predicates.

Completed `Roth.isPrimitive_linear`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.isPrimitive_pow`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_eq_pow_mul_of_rootMultiplicity`: Verified no-positive-denominator theorem, arbitrary commutative GCD domain A with any fraction field K, IsRelPrime h q rather than Bézout IsCoprime, IsGCDMonoid with locally chosen normalized gcd. Original exact quotient interface and full caller checked.

Completed `Roth.pow_rootMultiplicity_le`: Verified signed integer denominator, no positivity, Ring L ordered target, direct abs lc bound; separate GCD-domain/fraction-field denominator-power divisibility for q≠0. IsRelPrime strictly generalizes Bézout condition only in generic coefficient domains; numerical law retains ℤ coefficients.

Completed `Roth.index_unique_le_log_div`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.Θ_unique_le`: Native fullUniqueOnly drops redundant explicit Fintype binder under Unique; original already has no DecidableEq binder. Broader height/GCD-domain arithmetic belongs to independent196/197 proposals, not an automatic existing-mathlib replacement.

Completed `Roth.one_le_lem6M`: Expanded formula compiles over Semiring K, PartialOrder K, IsOrderedRing K (genericWeak); initial stronger genericScalar also verified. Actual lem6M remains fixed ℝ interface; altering it is a parent API redesign. Verified exponent-local premise1≤B^l is weaker than1≤B; l0 needs no bound. Uniform omission of hB is false (p=r₁=0,l1,B0).

Completed `Roth.floor_sq_div_two_le_sum`: Verified Field/LinearOrder/IsStrictOrderedRing/FloorSemiring statement; arbitrary n≤a removes floor; stronger division-free n²+n≤2sum works for CommRing/PartialOrder/IsOrderedRing. ha cannot simply be dropped.

Completed `Roth.sq_div_three_lt_floor_sq_div_two`: Verified Field/LinearOrder/IsStrictOrderedRing/FloorSemiring with5≤a; floor-free2*a²<3*n² for ordered CommRing from0≤a,5≤n,a<n+1. Certified99/20 and0counterexamples, plus negative abstract-input guard. No optimal cutoff/minimal hierarchy claim.

Completed `Roth.mul_div_two_le_sum_max_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.mul_sq_div_three_le_sum_max_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.min_le_sum_max`: Verified arbitrary scalar scale over ordered Field. FloorSemiring eliminated via bounded Nat.findGreatest. Quadratic /2 estimate verified; it strengthens original natural-scale /3 endpoint, whose bridge uses Nat.cast_nonneg. No uniform coefficient comparison for negative scale, minimal hierarchy or optimal constant claim.

Completed `Roth.sum_max_sub_le_index_det`: Compiled new generic row/column schema for any commutative domain with supplied finite-sum, product and integer-unit invariance laws, with values in an ordered additive commutative group. Compiled project weakening replaces hD plus globalhδ by only ∀μ weight(Dμ)≤δ; original follows and actual caller compiles. No bundled valuation or arbitrary-coefficient Hasse replacement is claimed.

Completed `Roth.index_separated_mul_le_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.index_det_le`: Compiled arbitrary derivative matrix E, direct input degree/coeff bounds, no RSet nonzero, no hl including l=0, and zero-factor endpoint cases under real index(0)=0. Separately derived both factor degree bounds under the original coupled nonzero interface. No full arbitrary-coefficient or maximality claim.

Completed `Roth.weight_le_delta_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.mapped_det_ne_zero_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.index_numeric_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.index_le_lem6`: Compiled removal of _hq and weakening r_none≥3 to≥1 using newly re-proved /2 finite-sum and numerical bounds; whole actual caller statements preserved. Independently compiled arbitrary nonnegative Φ(l) numerical witness core. No claim zero distinguished weight is impossible or full arbitrary-coefficient endpoint is verified.

Completed `Roth.Θ_option_le`: Jointly compiled no q>0, arbitrary real B, and r_none≥1. Real.sSup_le uses nonnegative RHS to cover empty families; independently compiled B<1⇒indexSet=∅ and Θ=0. The≥1 branch carries213’s new /2 finite-sum and numeric proofs, not existing mathlib API. Abstract outer transport verified for arbitrary conditionally complete linear orders with nonempty input family.

Completed `Roth.factorial_coefficient_le_two_pow_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.two_pow_lt_rpow_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.lem6M_lt`: Successfully compiled real q>=0 with threshold deriving q>1, l<=2^r and explicit r>0, with original theorem as checked wrapper and downstream statements unchanged. No optimality or maximality claim; endpoint formula guards and negative-log symmetry constrain unsupported widenings.

Completed `Roth.lem7_Φ_bound`: Verified delta<=2 with original wrapper and unchanged downstream statements; independently proved x*c+A*(x*c)^e<2*c*A*x^e for 0<x<=1,1<=c,1<A,e<=1. This removes the coupling of dyadic exponent, reciprocal dimension and base10. Dimension0 works only as a totalized arithmetic formula and is not a useful index-induction generalization.

Completed `Roth.lem7_numeric`: Compiled coefficient4 cap with δ≤1 and arbitrary negative Φ; generic real scalar envelope with free a,c,b,d,L,x,s also compiled. No δ-range or optimality claim.

Completed `Roth.theta_scaled_unique_le_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_delta_succ_lt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_prefix_lt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_lt_base_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_denominators_one_lt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_phi_lt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_lt_succ_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_lt_of_large_delta_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.Θ_lt`: Verified full theorem last degree≥1, and natural-positive form; complete sole caller adapts. Stronger finite-sum /2 and Lemma6 numeric proofs are carried explicitly, not existing mathlib. One-variable case only needsq>1 andr>0;δ=0 counterexample meets other public premises. No joint numeric extension, zero-weight necessity, general-field theorem or maximality claim.

Completed `Roth.lam`: No hypotheses/typeclasses to weaken. A real n/m extension and arbitrary semiring expression with supplied square-root-like function compile, but are representation extensions, not verified standard semantic weakenings. The meaningful abstraction is an admissible cutoff or a=(1+3δ)n in the count bound; scaleCount verifies its normalization. Do not claim YES-generalise-first merely by replacing casts or sqrt with an arbitrary function.

Completed `Roth.gam`: Compiled real-parameter formula and polymorphic Field halfGap/algebraic representations. These expand arithmetic representation; natural n,m remain degree/dimension in Roth. A reusable arbitrary admissible cutoff is an API proposal, not an existing mathlib definition.

Completed `Roth.eta`: Compiled new profile (C b δ : ℝ) (m : ℕ) ↦ C^m*δ^(b^m), its dimension0/zero/positive laws, nonnegative root interpretation and NNReal bridge. These are expanded representations, not a verified literature-standard weakening of a hypothesis. Real.rpow negative-base cosine convention prevents blanket replacement by iterated principal roots or NNReal.

Completed `Roth.mainCoeffBound`: Compiled floorPower (q e : ℝ) := ⌊q^e⌋₊ and an arbitrary FloorSemiring order characterization using existing Nat.le_floor_iff. These are expanded representations/existing infrastructure rather than a new literature-standard hypothesis weakening. Replacing the natural output with raw real power or globally claiming continuity changes the interface.

Completed `Roth.boxFamily`: Verified CommSemiring coefficient-family with monomial-specific allowed sets; arbitrary sigma and function-valued r retained for Set semantics; finite enumeration uses finitely supported r. Tested zero-membership premise is sufficient, not minimal.

Completed `Roth.exists_delta_bound`: No removable original premise: native sharp iff. Verified new arbitrary-real C,D,b,r,a and positive-exponent p perturbation theorem; specialization still needs the square-root gap and a normalization proof. This is a proposed generic API, not a previously existing mathlib result.

Completed `Roth.eta_lt_gam_iff`: Verified arbitrary e:ℝ in place of eta and arbitrary a,b,c in a Field K with LinearOrder K and IsStrictOrderedRing K: a + 2*b < c/2 ↔ a < (c-4*b)/2. This is a new generic proof, not an existing mathlib declaration; the underlying additive law already holds for AddGroup G, LT G, AddRightStrictMono G.

Completed `Roth.sqrt_lt_nat_floor_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.sqrt_lt_floor`: 2 ≤ X is exact; meaningful ordered-semiring floorSquare and rootBound with y²≤X compile as new proofs, including a rational witness and full original specialization. Not preexisting mathlib API. Final power route proves the generic quadratic kernel from three existing blocks; full original requires additional sqrt and upper-bound APIs.

Completed `Roth.four_lt_rpow`: Verified real q≥2, real r≥1; strict4log2<δ²logq sufficient, uniform sharp threshold at q2,δ2,r1. Arbitrary target/threshold square-gap transfer and ordered CommSemiring algebraic kernel compiled. Real q>1 alone, real r>0 alone, and dropping δ sign are refuted; no individual maximality claim.

Completed `Roth.mul_log_div_two_lt_log_mainCoeffBound`: Compiled mathlib-only logFloor: ∀ {X : ℝ}, 2 ≤ X → Real.log X / 2 < Real.log (⌊X⌋₊ : ℝ); realPower allows nonnegative real q and arbitrary real z. Positive-floor-domain sharp iff holds under 1 ≤ X. New helper proofs are not existing library declarations.

Completed `Roth.two_lt_rpow_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.three_small_factors`: Compiled replacement of hA by 0≤Real.log(1+A) preserves all3 strict conclusions; A=-2 is an explicit admitted instance. m0 permits arbitrary A. Compiled generic floorPower: 2≤X,0<δ, (s:ℝ)*log t≤δ*log X/2 imply t^s<(floor X)^δ. These are verified candidates, not a claim of maximal domain or existing API.

Completed `Roth.exists_norm_coeff_reduction_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.norm_coeff_modByMonic_le`: Verified mathlib-only Ring R and arbitrary v:R→ℝ with v0=0, nonnegativity, sub triangle and submultiplicativity, preserving s+1-f.natDegree. This is a newly proved size_remainder, not existing mathlib. Bundled RingSeminorm alternative is source-inspected, not claimed compile-verified; no extra import authorization received.

Completed `Roth.boxFamily_eq_image_finsupp_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.boxFamily_finite`: Compiled: arbitrary CommSemiring R, arbitrary finite monomial support, and finite coefficient sets (only on selected monomials). Original recovered with no signature change. Also B=0 permits removal of the support condition; unqualified support removal fails for ℕ variables, r=1, B=1.

Completed `Roth.ncard_boxFamily`: Verified new generic semantic family over arbitrary CommSemiring R and r : sigma →₀ Nat, with coordinate-dependent Finset choices t d and 0∈t d only off Finset.Iic r. Original function-r/finite-support/finprod type recovered and caller retained. This changes parent representation, not a mechanical weakening of an Int typeclass.

Completed `Roth.floor_rpow_count_lt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.pigeonhole_count`: verified: theorem powerBudget {a b t : ℝ} {k N : ℕ} (ha : 0 ≤ a) (hb : 1 < b)
    (hbase : a < b ^ t) (hN : 0 < N) (hbudget : t * k ≤ N) : a ^ k < b ^ N; semantic: Arbitrary a,b,t separate count generation from exponent lifting; permits other coefficient-count bounds. Flattening nD to k alone is only representation normalization.; hypothesis localization: N positivity can be localized to k=0 in verified localizedBudget; exact target cannot drop it because nD=0 is allowed.; sharpness: B0,c0,N0/no-budget and positive c=1/2 counterexamples compile. No claim that c>=1 is sharp or that current hypotheses are globally maximal.

Completed `Roth.exists_ne_modByMonic_eq`: STRICTLY NARROWER THAN STANDARD: deleting [Finite (Function.support r)] alone is verified by two clean independent proofs. Preferred constants route: finite branch original proof; infinite support gives finprod(r+1)=1 and the all-zero degree subfamily suffices. Independent Xi route uses infinitely many admissible variables and existing Finite.exists_ne_map_eq_of_infinite. Abstract finite/infinite polynomial observations are both compiled; full generalized Lean type is in generalized-type.json.

Completed `Roth.sub_mem_RSet`: Verified ordered commutative ring interval endpoints yield diameter ub-lb, with original integer/RSet specialization preserving B. A size/set diameter helper supports semantic coefficient ranges. Parent-family representation changes are a separate API decision.

Completed `Roth.eval_hasseDeriv_sub_eq_zero`: Verified arbitrary CommRing coefficient R and algebra target S with the same Hasse/diagonal semantics. A separately proved generic AddGroup observation D into Polynomial R and RingHom e killing f works over arbitrary rings, with exact original recovery checked. Root and remainder equality are both necessary.

Completed `Roth.le_index_of_forall_eval_eq_zero`: Verified cutoff-local outside-box degree condition, or outside-box evaluated annihilation, weakens the global degree premise. New finite-support observation proofs work over arbitrary Zero coefficients and conditionally complete linear ordered weights; arbitrary-variable/CommRing polynomial indexAny recovers the exact original via finite-support weights. Fintype cannot simply be deleted from the unchanged parent signatures.

Completed `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`: Verified Budget253.generic replaces 2m+1 by arbitrary positive a under the same class assumptions; exact original recovery compiled. Weak δm≤1 and strict-budget partners compiled.

Completed `Roth.exists_hasseDeriv_eval_ne_zero`: Verified arbitrary I, semiring coefficients A and any linear order L with top for infDegree; arbitrary σ and CommRing A with real exponent-cost D for translated Hasse form. Existing index signature itself retains Fintype.

Completed `Roth.abs_eval_iterated_hasseDeriv_lt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_hasseDeriv_index_eval_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_mem_RSet_le_index_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.mul_card_filter_weight_le_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_mem_RSet_le_index_of_log_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_auxiliary_polynomial_of_log_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.theta_lt_eta_of_sq_log_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_auxiliary_polynomial_with_index_gap_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.main_lemma`: Retain full named quantitative statement. Scratch numerical_envelope independently varies B,beta,c,X,E under mathematical admissibility conditions and recovers all original hypotheses/conclusions; it is complementary internal API, not a replacement for deriving Theta<eta from numerical hypotheses. Arbitrary finite ordered variables require explicit reindexing; complex/absolute-valued-field versions require index/analytic API transport, not an unchecked hypothesis drop.

Completed `Roth.approxSet`: Verified arbitrary error-function approxWith and coefficient approxC family with exact C1 recovery, nonpositive-C emptiness, C monotonicity and actual C1/C2 distinction. Arbitrary ψ bounded-slice/filter proofs compile mathlib-only. Rational image equality needs κ≥0; finite fibers and pair/rational infinitude equivalence need irrationality and κ>0.

Completed `Roth.exists_nat_mul_isIntegral`: Verified {A : Type*} [Ring A] {x : A} (h : IsAlgebraic ℤ x) : ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : A) * x). Also arbitrary domain R/fraction field K/commutative K-algebra A yields ∃ r:R,r≠0 ∧ IsIntegral R (r•x), already existing infrastructure; no GCD needed. PositiveNat does not generalize to arbitrary base R.

Completed `Roth.approxSet_den_le_finite`: Freshly compiled arbitrary real radius ψ:ℕ→ℝ bounded-denominator theorem, credited267newproof template, exact current statement specialization. New finite-radius integer tubes over arbitrary finite index sets work over [Ring K] [LinearOrder K] [IsStrictOrderedRing K] [FloorRing K]; closed endpoints and signed radii allowed. No unverified relaxation claimed.

Completed `Roth.eventually_div_rpow_lt`: proposed type: ∀ {α : Type*} {l : Filter α} {f : α → ℝ}, Filter.Tendsto f l Filter.atTop → ∀ {M C κ κ' : ℝ}, κ' < κ → 0 < C → ∀ᶠ x in l, M / f x ^ κ < C / f x ^ κ'; verified: True; source: isolated3-executed.lean.txt; recovery: Decay270Generic.threshold hκ zero_lt_one; axes: arbitrary positive RHS amplitude C, arbitrary cofinal real input along any filter

Completed `Roth.reduction`: verified: True; proposed type: ∀ {α : ℝ}, Irrational α → IsAlgebraic ℚ α → ∀ {t κ : ℝ}, t < κ → (approxSet α κ).Infinite → ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ t < κ' ∧ κ' < κ ∧ (approxSet α' κ').Infinite; scaling type: ∀ {α κ κprime : ℝ} (M : ℕ), 0 < M → κprime < κ → (approxSet α κ).Infinite → (approxSet (M * α) κprime).Infinite; evidence: isolated-executed.lean.txt; isolated-receipt.json; meaning: 2 is a reusable semantic lower threshold, not essential here; M>0 scopes the injective map and irrational output, not a claimed necessary condition for the weaker standalone Infinite conclusion.

Completed `Roth.exists_monic_aeval_eq_zero`: verified: True; proposed type: ∀ {R A : Type*} [CommRing R] [Nontrivial R] [Ring A] [Algebra R A] {a : A}, IsIntegral R a → ∀ N : ℕ, ∃ g : Polynomial R, g.Monic ∧ Polynomial.aeval a g = 0 ∧ N ≤ g.natDegree; source: isolated3-executed.lean.txt; receipt: isolated3-receipt.json; semiring: Witness-level version uses CommSemiring R, Nontrivial R, Semiring A, Algebra R A; no Nontrivial A required.

Completed `Roth.approxSet_num_den_mem_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_reduced_approx`: status: STRICTLY NARROWER THAN STANDARD; verified: True; proposed type: ∀ {α : ℝ}, Irrational α → ∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite →
  ∀ Q₀ : ℕ, ∃ hq ∈ Roth.approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ); subcritical type: ∀ {α : ℝ}, Irrational α → ∀ {κ : ℝ}, κ ≤ 2 →
  ∀ Q₀ : ℕ, ∃ hq ∈ Roth.approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ); proof source: isolated2-executed.lean.txt; semantic generic source: generic-executed.lean.txt; rows: {'parameter': 'α : ℝ', 'assessment': 'Real absolute value and real powers are actual arithmetic; no unsupported ordered-field or p-adic claim.'}, {'parameter': 'Irrational α', 'assessment': 'Uniform removal false: α=0 κ=3 has infinitely many exact pairs but no reduced denominator>1. Native counterexample.'}, {'parameter': 'κ : ℝ and 0<κ', 'assessment': 'Drop positivity entirely via original positive branch and irrational Dirichlet2 for κ≤0; actual stronger κ≤2 branch omits hinf.'}, {'parameter': 'hinf', 'assessment': 'Needed conditionally in unrestricted theorem above2; subcritical theorem verified without it. No proof of unconditional supra2 statement claimed.'}, {'parameter': 'Q₀ : ℕ', 'assessment': 'Arbitrary inclusive threshold including0 retained, strict output Q₀<q retained.'}, {'parameter': 'ℤ×ℕ and coprimality', 'assessment': 'Positive natural denominator and integer numerator canonicalize to rational num/den; reduction is substantive, not Rat.num_div_den alone.'}, {'parameter': 'fixed coefficient1 / tolerance', 'assessment': 'Coefficient1 is a genuine supplied-quality predicate, not the existential C of LiouvilleWith. Arbitrary semantic s/f/r/height/good schema independently proved with all necessary finiteness/normalization premises and exact current recovery; no blanket analytic arbitrary-tolerance theorem claimed.'}; generic vs existing: unbounded_canonical and arithmetic recovery are own new proofs. Set.Finite.of_finite_fibers and Dirichlet2 are existing mathlib building blocks.

Completed `Roth.exists_m`: verified: True; status: Verified semantic parameter widening; no claim that literature standardizes this exact generic API; proposed type: ∀ {a b κ : ℝ}, b < κ → ∃ m : ℕ, a ^ 2 < (m : ℝ) ∧ a * √(m : ℝ) < m ∧ b * m / (m - a * √(m : ℝ)) < κ; current type: ∀ {n : ℕ} {κ : ℝ},
  2 < κ → ∃ (m : ℕ), 16 * n ^ 2 < m ∧ 4 * ↑n * √↑m < ↑m ∧ 2 * ↑m / (↑m - 4 * ↑n * √↑m) < κ; old recovery: a=4*n,b=2, natural first bound recovered by nlinarith + exact_mod_cast; original full type retained; nonnegative real size: generic-executed verifies a≥0; signed-executed removes this assumption with |a| bound; arbitrary coefficient: signed coefficient theorem takes arbitrary real c,t,b,κ; positive c and nonnegative t are included; hypothesis drop: κ>2 cannot weaken to κ≥2 uniformly: n=0,κ=2 no witness certified; threshold caution: b<κ is sufficient; not claimed necessary for every fixed signed a,b; representation: ℝ fixed by Real.sqrt; abstract Archimedean simultaneous-bound lemma checked separately, not a fake ordered-semiring sqrt theorem; limit: Limit-to-b is a conceptual alternative; no full limit-to-b replacement claimed or used. Existing tendsto_sqrt_atTop and bounded-div-atTop cover pieces, not simultaneous quantitative conclusion.

Completed `Roth.exists_delta`: verified: True; proposed type: ∀ {f p q : ℝ → ℝ} {U B K : ℝ}, 0<U → ContinuousAt f 0 → ContinuousAt p 0 → ContinuousAt q 0 → q 0≠0 → f 0<B → p 0/q 0<K → ∃ δ : ℝ, 0<δ ∧ δ<U ∧ f δ<B ∧ p δ/q δ<K; recovery: Exact original type recovered with f=eta+square-root expression, p=m(1+4δ), q=gam-eta; supplies square-root gap, positive cap, exponent continuity and value-at0.; quantitative envelope type: ∀ {A e M s U K : ℝ}, 0<e → 4*s<M → 0<U → 2*M/(M-4*s)<K → ∃ δ : ℝ, 0<δ ∧ δ<U ∧ A*δ^e+2*(1+3*δ)*s<M/2 ∧ M*(1+4*δ)/((M-4*(1+3*δ)*s)/2-A*δ^e)<K; quantitative recovery: Verified mathlib-only19: A=10^m, e=(1/2)^m, M=m, s=n*sqrt m, U=1/m; reconstructs both old quantitative envelopes from genuine mathlib operations. Native ambient bridge uses only [eta,gam,lam] and exact original type equality.

Completed `Roth.exists_approximants`: verified: True; proposed type: ∀ {A : Type*} (s : Set A) (height : A → ℝ), (∀ B : ℝ, ∃ a ∈ s, B < height a) → ∀ (F : ℕ → ℝ → ℝ) (L : ℝ), ∃ f : ℕ → A, (∀ k, f k ∈ s) ∧ (∀ k, 0 < height (f k)) ∧ L < height (f 0) ∧ ∀ k, F k (height (f k)) < height (f (k+1)); kappa: Remove0<κ: newly proved unrestricted selector yields full chain; κ≤2 also drops supplied infinitude.; recovery: Exact original full signature recovered from generic cofinal-height finite selection, with native type equality. Explicit δ0,-1 and full old positiveκ type through unrestricted theorem verified.

Completed `Roth.exists_degrees`: verified: True; proposed type: variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [FloorRing K]
theorem exists_separated_nat_multiples {ι : Type*} [Finite ι] (b : ι) {ℓ : ι → K} (hℓ : ∀ j, 0 < ℓ j)
    {ε B δ c : K} (hε : 0 < ε) (hB : 0 < B) (hc : 1 < c)
    (R : ι → ι → Prop) (hg : ∀ i j, R i j → c / δ * ℓ i ≤ ℓ j) :
    ∃ r : ι → ℕ, (∀ j, 0 < r j) ∧ (∀ j, B < r j) ∧
      (∀ i j, R i j → (r j : K) / δ < r i) ∧
      (∀ j, (r b : K) * ℓ b ≤ r j * ℓ j) ∧
      ∀ j, (r j : K) * ℓ j < (1 + ε) * (r b * ℓ b) ; remove: δ≤1 from original target; retain: δ>0 for positive ε=δ/10 and B=10/δ in original quantitative recovery, q>1/log positivity, strict adjacent ratio and strict upper balanced product; weak lower product; scope: Generic ordered field with FloorRing; arbitrary Finite ι, base b, positive ℓ, ε,B, c>1, arbitrary relation R, unrestricted generic δ. Original full type recovered exactly.

Completed `Roth.one_le_prod_pow_mul_abs_eval`: verified: True; reason: LITERATURE-WEAKENING, MODERN-IDIOM; proposed type: theorem signed {ι K : Type*} [Fintype ι] [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (Q : MvPolynomial (ι) ℤ) {r : ι → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h : ι → ℤ) {q : ι → ℤ} (hq : ∀ j, q j ≠ 0)
    (hne : eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) ≠ 0) :
    1 ≤ |∏ j, (q j : K) ^ r j| * |eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q)|; natural wrapper type: theorem generic {ι K : Type*} [Fintype ι] [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (Q : MvPolynomial (ι) ℤ) {r : ι → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h : ι → ℤ) {q : ι → ℕ} (hq : ∀ j, 0 < q j)
    (hne : eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : K) ^ r j) * |eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q)|; mechanical: Fin m -> arbitrary Fintype; ℝ -> ordered field; original body otherwise unchanged; extended: Signed integer denominators with absolute product; CharZero field algebraic clearing; norm target requires explicit integer separation bound; recovery: recovery01 exact original written signature, Fin0 edges01; algebraic helper type: theorem clearing_semiring {ι R S : Type*} [Fintype ι] [CommSemiring R] [CommSemiring S]
    (f : R →+* S) (Q : MvPolynomial ι R) {r : ι → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (a b : ι → R) (bi : ι → S)
    (hbi : ∀ j, bi j * f (b j) = 1) :
    ∃ N : R, f N = (∏ j, f (b j) ^ r j) * eval₂ f (fun j ↦ f (a j) * bi j) Q; algebraic generality: Verified arbitrary commutative semirings and ring hom with coordinate denominator inverses, no CharZero/injective map/field/order. Numeric bound requires integer separation separately.

Completed `Roth.abs_prod_pow_le_rpow_of_le_weight`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.abs_eval_lt_of_le_index`: verified: True; proposed type: lemma expansion_bound {σ : Type*} [Fintype σ] {s : Finset (σ →₀ ℕ)} (hs : s.Nonempty)
    {a x μ : σ → ℝ} {A : (σ →₀ ℕ) → ℝ} {b c C : ℝ} (hb : 1 ≤ b)
    (hC : ∀ d ∈ s, |A d| < C) (hx : ∀ j, |x j - a j| ≤ b ^ (-μ j))
    (hvanish : ∀ d ∈ s, A d ≠ 0 → c ≤ ∑ j, μ j * d j) :
    |eval x (∑ d ∈ s, MvPolynomial.C (A d) * ∏ j, (X j - MvPolynomial.C (a j)) ^ d j)|
      < (s.card : ℝ) * C * b ^ (-c) ; project type: lemma cost_bound {σ : Type*} [Fintype σ] [DecidableEq σ]
    {Q : MvPolynomial σ ℝ} {r : σ → ℕ} (hd : ∀ j, degreeOf j Q ≤ r j)
    {a x μ : σ → ℝ} {b c C : ℝ} (hb : 1 ≤ b)
    (hC : ∀ d ∈ box r, |eval a (hasseDeriv d Q)| < C)
    (hx : ∀ j, |x j - a j| ≤ b ^ (-μ j))
    (hvanish : ∀ d ∈ box r, eval a (hasseDeriv d Q) ≠ 0 → c ≤ ∑ j, μ j * d j) :
    |eval x Q| < (∏ j, ((r j : ℝ) + 1)) * C * b ^ (-c) ; normed ring type: lemma expansion_bound {σ K : Type*} [Fintype σ] [NormedCommRing K] [NormOneClass K]
    {s : Finset (σ →₀ ℕ)} (hs : s.Nonempty)
    {a x : σ → K} {μ : σ → ℝ} {A : (σ →₀ ℕ) → K} {b c C : ℝ} (hb : 1 ≤ b)
    (hC : ∀ d ∈ s, ‖A d‖ < C) (hx : ∀ j, ‖x j - a j‖ ≤ b ^ (-μ j))
    (hvanish : ∀ d ∈ s, A d ≠ 0 → c ≤ ∑ j, μ j * d j) :
    ‖eval x (∑ d ∈ s, MvPolynomial.C (A d) * ∏ j, (X j - MvPolynomial.C (a j)) ^ d j)‖
      < (s.card : ℝ) * C * b ^ (-c) ; original recovery: Exact original statement recovered after restricting hC to box; arbitrary zero/mixed-zero r preserved.; semantic parameters: arbitrary real μ and b≥1, arbitrary center/evaluation, finite variable type; positive radii b^(-μ) are semantic data, not renamed integer denominators.; limit: Project Hasse/index not ported to arbitrary coefficient ring; normed expansion theorem is independently mathlib-only.

Completed `Roth.exists_roth_parameters_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_roth_approximants_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.one_lt_roth_eval_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.roth_product_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.roth_log_bound_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.roth_of_isIntegral`: verified: True; reason: MODERN-IDIOM; proposed type: ∀ {α p : ℝ}, IsIntegral ℤ α → LiouvilleWith p α → p ≤ 2; exact equivalence: For irrational α, classical all-exponent pair bound iff ∀ {p}, LiouvilleWith p α → p≤2; modern integral theorem derives irrationality only in p>2 branch.; native scope: Mathlib-only new conditional bridge plus original exact proof/type agreement; no independent mathlib Roth proof claimed.

Completed `Roth.roth`: verified: True; reason: MODERN-IDIOM; proposed type: ∀ {α p : ℝ}, IsAlgebraic ℚ α → LiouvilleWith p α → p ≤ 2; exact equivalence: For irrational α, the all-exponent pair-bound property iff ∀ {p}, LiouvilleWith p α → p≤2; modern algebraic endpoint derives irrationality only in p>2 case.; native scope: Fresh conditional bridge adapted from287, compiled independently with algebraicity premises; original proof replay validates the mathematical premise. No independent mathlib Roth proof claimed.

Completed `Roth.roth_rat`: proposed type: ∀ {α : ℝ}, IsAlgebraic ℚ α → ∀ {κ : ℝ}, {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite → κ ≤ 2; drop: Irrational α; verified: True; evidence: general02-receipt.json; scope: Compiled implication from the exact original endpoint schema hR; original hR separately re-elaborated and type-agreed. No extra axiom introduced.; modern: Equivalent finite rational bad-set or cofinite non-strict lower-bound form verified in modern01; not a uniform strict positive-C bound.; constant: Verified C≤1 extension in edges01. C>1/existential coefficient variant assessed but not claimed compiled.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`: proposed type: (t x : ℝ) → Prop; proposed body: ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧ ∀ p q : ℤ, 0 < q → C / (q : ℝ) ^ (t + ε) < |x - (p : ℝ) / q|; modern type: UniformBound t x ↔ Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t; verified: True; consequences: cutoff_mono, add_rat_iff, mul_rat_iff; recovery: UniformBound 2 is definitionally the complete original formula

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`: verified: True; drop: hx; all real type: ∀ {x : ℝ}, IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2; generic type: ∀ {t x : ℝ}, UniformBound t x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t; modern type: ∀ {t x : ℝ}, UniformBound t x ↔ Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t; conditions: No positivity condition on t; Liouville bridge retains irrationality; fixed2 recovered without assumption

## Part 6: API improvements

The Hasse coefficient and derivative belong with a coherent multivariate differential API; all supporting identities now have completed assessments. The per-declaration findings below identify existing evaluation/support primitives, substantive missing operator laws and optional upstream interface choices. A scalar construction alias alone does not replace this package. The Roth endpoints likewise form one theorem contribution with derived interfaces, rather than separate novel proofs.

Completed `MvPolynomial.hasseDeriv_monomial`: No new generic evaluation API needed: existing Finsupp.lsum_single directly proves the law after definitional transport. Exact coordinate operator name absent in mathlib-only environment is not a mathematical absence proof.

Completed `MvPolynomial.hasseDeriv_apply`: No new generic evaluation API needed. Mathlib-only exact qualified name check does not establish absence of all equivalent mathematics.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: None proven; upstream packaging of natural multi-binomial/order criterion is a policy question.

Completed `MvPolynomial.coeff_hasseDeriv`: Arbitrary-variable characteristic-free Hasse derivative coefficient interface, next to MvPolynomial.PDeriv and the multivariate Hasse operator.

Completed `MvPolynomial.hasseCoeff_eq_prod`: None for the support/full-product bridge: Finsupp.prod_fintype and prod_of_support_subset already cover it.

Completed `MvPolynomial.hasseDeriv_zero_apply`: No separate generic helper gap established. Whether this pointwise normalization deserves its own exported corollary in the new multivariate Hasse API is an upstream design question.

Completed `MvPolynomial.hasseDeriv_zero`: Concrete multivariate Hasse definition and coefficient interface form the upstream context; no distinct missing generic extensionality helper. Exporting one or both zero-law forms is an API design question.

Completed `MvPolynomial.hasseDeriv_C`: Multivariate Hasse parent and coefficient/monomial interface are needed upstream context. Named scalar constant normalization/simp policy remains a design choice; no missing generic lsum-single helper.

Completed `MvPolynomial.hasseDeriv_map`: Multivariate all-order divided derivative coefficient-change law beside the parent Hasse operator.

Completed `MvPolynomial.hasseDeriv_rename`: Injective-renaming naturality for all multivariate divided derivative orders.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: No missing generic finite-product API needed here; public Hasse composition assessed separately.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: Canonical multivariate polynomial Hasse iterativity, analogous to Polynomial.hasseDeriv_comp but for finitely supported multi-orders.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: Canonical multivariate Hasse composition for disjoint differential supports, grouped with parent iterativity.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Existing finite-product and choose simplification suffice; public partial/Hasse derivative compatibility assessed separately.

Completed `MvPolynomial.pderiv_hasseDeriv`: Canonical multivariate Hasse compatibility with ordinary pderiv in arbitrary characteristic.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: Coordinate-degree/degree-box preservation for canonical multivariate Hasse derivative, with sharp primary companion matching univariate degree-minus-order convention.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: Coordinate-degree annihilation for canonical multivariate Hasse derivative; support and exact weighted-coefficient criteria useful companions.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Generic monomial/support infrastructure sufficient; public factor-separation operator API assessed next.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Canonical multivariate Hasse factor-independence/relative-linearity rule; eventual full multi-index product formula.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: Public coordinate compatibility API for new multivariate Hasse derivatives, subject to packing decision.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: Public API choice for unique-variable Hasse transport beside proposed multivariate Hasse operator.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Design choice whether general Finset/Nat binomial-product estimate merits named upstream API.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Characteristic-free multivariate Hasse to iterated partial compatibility.

Completed `Roth.box`: None for constructing box; interval sum/product bridge a separate optional API question.

Completed `Roth.weight`: No missing API for definition; assess re-aimed dependent order/index lemmas separately.

Completed `Roth.mem_box`: None established.

Completed `Roth.card_box`: None

Completed `Roth.card_le_card_box`: No categorical missing-API claim. Design question: whether useful Finsupp natural-endpoint/support interval convenience bounds deserve upstream names.

Completed `Roth.weight_nonneg`: No necessary gap: generic sum/scalar positivity composes. A standalone Finsupp.weight_nonneg convenience name not found; no absence claim.

Completed `Roth.weight_zero`: No required missing upstream zero-preservation fact.

Completed `Roth.weight_add`: No new missing mathlib theorem identified; existing Finsupp.weight/map_add cover abstract content.

Completed `Roth.weight_eq_zero_iff`: Candidate positive-weight zero-fiber theorem without canonical-order assumption; design unresolved, absence not proven.

Completed `Roth.weight_single`: No demonstrated missing singleton-evaluation mathematics; design issue is whether to expose finite cast/division convenience API or migrate parent weight to bundled support sums.

Completed `Roth.weight_le_card`: Potential ordered Finsupp.weight upper bound by support.card • b; API design question, not established absence.

Completed `Roth.weight_mul_left`: No mathematical API gap established; dedicated weight_smul spelling would wrap bundled linearity.

Completed `Roth.weight_le_degree_div`: Potential support-local weight monotonicity or constant/degree upper bound; design choice, not an existing verified law.

Completed `Roth.weight_mapDomain`: None

Completed `Roth.wronskianMatrix`: Coherent named n-ary normalized Wronskian API; existing pinned TODO. No absolute absence theorem claimed.

Completed `Roth.wronskian`: Coherent normalized n-ary Wronskian name/compatibility/scaling API subject to upstream design.

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: Design-dependent packaging of finite Hasse alternating map or generic operator-family determinant law; abstract vanishing law already exists.

Completed `Roth.det_choose_eq`: Public characteristic-aware binomial evaluation determinant API; Pochhammer monicity/degree can be transferred from ℤ to remove pinned NoZeroDivisors assumptions.

Completed `Roth.coeff_prod_of_natDegree_le'`: Potential varying-bound public coefficient generalization; full public contribution verdict n/a under private prefilter.

Completed `Roth.sum_range_le_sum_of_injective`: None

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Coefficient of determinant of arbitrary finite Hasse derivative matrix at sum degrees minus sum orders; varying-bound coefficient-product helper supports its proof.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: N-ary Hasse Wronskian top-coefficient/nonvanishing API, supported by cancellation-free binomial determinant identity.

Completed `Roth.wronskian_update_sub_smul`: Conditional on parent acceptance: finite-family Hasse-Wronskian alternating-map interface or family-to-matrix update compatibility. No missing generic determinant column law.

Completed `Roth.linearIndependent_update_sub_smul`: No mathematical gap; generic update spelling is optional convenience.

Completed `Roth.sum_natDegree_update_lt`: Potential normalized quotient cancellation corollary and relation to cancelLeads; generic finite-update wrapper is optional design question.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: N-ary polynomial Hasse Wronskian criterion, coherent binary/n-ary naming bridge, potentially reusable polynomial echelon basis.

Completed `Roth.wronskian_eq_zero_iff`: N-ary Hasse Wronskian foundation and criterion, coherent binary/n-ary naming and finite column reindexing.

Completed `MvPolynomial.taylor`: Design question: stable named multivariate translation with Hasse coefficient, composition and inverse APIs.

Completed `MvPolynomial.taylor_apply`: No mathematical normalization API needed for this constitutive equation. Optional stable unfold theorem may accompany a future upstream translation bundle.

Completed `MvPolynomial.taylor_X`: No mathematical gap for this law. A future translation bundle may independently choose its own stable generator simp interface.

Completed `MvPolynomial.taylor_C`: None

Completed `MvPolynomial.taylor_monomial`: None

Completed `MvPolynomial.coeff_aeval_X_mul`: No missing primitive blocks existing proof; public extraction API suitability is unassessed under private prefilter.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Existing product/erase/support primitives suffice; full public upstream assessment n/a under private rule.

Completed `MvPolynomial.prod_pow_single_add_tsub`: No missing primitive blocks proof. Potential generic monomial-evaluation formulation is a future public assessment, not claimed completed.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: No missing primitive blocks current decomposition; prospective public multivariate Hasse/Taylor API assessed separately.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: No missing primitive blocks exponent induction; prospective public Hasse/Taylor API separately assessed at next declaration.

Completed `MvPolynomial.coeff_taylor`: Coefficient normalization of multivariate substitution X+Cα against binomial Hasse derivative.

Completed `MvPolynomial.eval_taylor`: Translation-specific convenience API is an upstream design question; no missing generic engine established.

Completed `MvPolynomial.taylor_taylor`: Design question: package translation composition as named law or structural action API; no missing generic composition engine.

Completed `MvPolynomial.taylor_zero`: No mathematical API gap; parent translation naming/simp design independently assessed.

Completed `MvPolynomial.taylor_map`: Design choice whether a named multivariate translation API merits coefficient-map convenience law; no generic substitution gap.

Completed `MvPolynomial.taylor_rename`: No generic substitution gap; decision whether named multivariate translation API merits explicit rename convenience law.

Completed `MvPolynomial.degreeOf_taylor_le`: Coordinate-degree control under multivariate constant-shift substitution, with arbitrary variable type and commutative-semiring coefficients.

Completed `MvPolynomial.taylor_neg_taylor`: Potential bundled multivariate translation algebra equivalence; its inverse fields are new obligations, not a missing generic equivalence theorem.

Completed `MvPolynomial.taylor_injective`: Potential multivariate translation AlgEquiv; no missing generic left-inverse theorem.

Completed `MvPolynomial.taylor_eq_zero_iff`: Multivariate semiring translation zero-reflection and reusable maximal-support Hasse constant lemma.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Multivariate Hasse/Taylor coefficient-to-finite-box reconstruction; optional support-indexed intermediate using generic evaluation sums.

Completed `MvPolynomial.eval_eq_sum_box`: Multivariate Hasse finite Taylor evaluated expansion and foundational coefficient/polynomial reconstruction; existing generic homomorphism transport should be reused.

Completed `Roth.normOne`: No missing scalar construction established; general coefficient L1/convolution normed structure and substantive bounds are separate potential contributions. Pinned Polynomial.Norm explicitly lists other Lp norms as TODO.

Completed `Roth.diag`: No missing scalar construction, hom bundle or evaluation-composition API established. Specialized coefficient/degree bounds remain separate assessment candidates.

Completed `Roth.normOne_nonneg`: None established for nonnegativity; full bundled coefficient/convolution norm structure is separate from this law.

Completed `Roth.normOne_eq_sum_of_support_subset`: None needed for support padding. No global coefficient norm instance proposed.

Completed `Roth.normOne_monomial`: None needed. No new coefficient norm instance recommended.

Completed `Roth.normOne_zero`: None. No proposed new global polynomial norm instance.

Completed `Roth.abs_coeff_le_normOne`: No missing API for this declaration. Optional separate generalization of existing single_eval_le_sum to Preorder/AddLeftMono/support-local nonnegativity now has a proof witness; no absence/novelty claim or new upstream verdict for that separate API.

Completed `Roth.normOne_add_le`: Design candidate: generic Finsupp support-sum subadditivity versus compatible L1 normed-group or translation-distance API. Searches establish candidates, not formal absence.

Completed `Roth.normOne_neg`: None required for the verified replacement; new assessment generic helper is not counted as existing mathlib.

Completed `Roth.normOne_sum_le`: Potential generic Finsupp sum subadditivity/coefficient-size bridge; existing finite induction itself has no gap.

Completed `Roth.normOne_mul_le`: Candidate shared coefficient-size convolution/RingSeminorm API; broad AddMonoidAlgebra endpoint is a future design question.

Completed `Roth.normOne_prod_le`: Substantive coefficient-size binary convolution/representation bridge, not finite-product induction.

Completed `Roth.normOne_le_card_mul`: No missing API required for this bound; broader coefficient norm representation issues do not obstruct this theorem.

Completed `Roth.normOne_det_le`: RingSeminorm determinant factorial bound beyond multiplicative AbsoluteValue.map_prod.

Completed `Roth.abs_coeff_hasseDeriv_le`: Quantitative coefficient bounds for multivariate Hasse derivatives, atop the proposed multivariate Hasse algebraic API.

Completed `Roth.normOne_hasseDeriv_le`: Multivariate Hasse derivative foundation and coefficient seminorm finite-support sum bound. State explicit coefficient sums, avoiding a new coefficient norm foundation.

Completed `Roth.diag_eq_sum`: Optional named constant-X evaluation expansion, contingent on upstream API design; no mathematical proof infrastructure gap.

Completed `Roth.abs_coeff_diag_le`: Optional coefficient formula for constant-X substitution, followed by a design choice about exposing a generic estimate. No missing finite-sum inequality infrastructure.

Completed `Roth.natDegree_diag_le`: Potential named coordinate-to-totalDegree inequality / bounded variant, pending upstream API choice; search failure not an absence proof.

Completed `Roth.eval_diag`: None established; no new normalization helper needed.

Completed `Roth.diag_sub`: None needed for subtraction preservation.

Completed `Roth.geom_sum_le_one_add_pow`: Finite geometric/binomial unweighted comparison without t<1 restriction.

Completed `Roth.sum_box_prod_pow_le_aux`: Existing finite-product, finite-sum and order primitives support the decomposition; prospective public geometric bound is independently assessed at96.

Completed `Roth.abs_eval_le`: Nonhomogeneous rectangular coordinate-degree polynomial evaluation majorant; generic geometric-sum bound from declaration96 is a separate new prerequisite.

Completed `Roth.degreeOf_det_hasseDeriv_le`: MvPolynomial coordinate degree bound on arbitrary polynomial matrix determinants; Hasse corollary after upstream multivariate Hasse API.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Coefficient l1 size API for multivariate polynomials, its Hasse estimate, and normalized RingSeminorm determinant estimate. Pinned Polynomial/Norm TODO documents missing lp norm API.

Completed `Roth.genWronskian`: Named finite-family multivariate Hasse Wronskian; upstream multivariate Hasse prerequisite. Existing pairwise Polynomial Wronskian file has n-tuple TODO.

Completed `Roth.kronecker`: No missing API for the definition itself; bounded encoding/injectivity and derivative results assessed separately.

Completed `Roth.kroneckerExp`: None for this definition. Radix injectivity and substitution coefficient/derivative laws require their own assessment; arbitrary weights do not inherit injectivity.

Completed `Roth.kronHasse`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.kronSpan`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: Design choice: shared scalar-linear determinant family lemma versus alternating generalized-Wronskian representation.

Completed `Roth.kronecker_monomial`: No missing evaluation infrastructure established; new weighted helper probe is not counted as an existing mathlib theorem.

Completed `Roth.kroneckerExp_injOn`: Public Finsupp geometric-weight injectivity on bounded digits; concrete recurring list conversion in Roth and pinned NoetherNormalization private helper.

Completed `Roth.coeff_kronecker`: Candidate normalization between aeval monomial powers and mapDomainAlgHom(weight); decide whether to expose extraction corollary.

Completed `Roth.kronecker_eq_zero_iff`: Weighted monomial-evaluation coefficient/mapDomain bridge; packaging of restricted aeval injection versus zero corollary remains API choice.

Completed `Roth.linearIndependent_kronecker`: aeval(X^w) coefficient mapDomain bridge and support-restricted injection; packaging inherited questions from109–110, independently evaluated for111. No missing generic linear-independence transport.

Completed `Roth.derivative_aeval`: Module-valued MvPolynomial evaluation chain rule expressed with pderiv, complementing Derivation.map_aeval.

Completed `Roth.derivative_kronHasse_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.derivative_mem_kronSpan`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.hasseDeriv_kronecker_mem`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Higher polynomial-substitution law for multivariate Hasse derivatives, with choice of filtered-span, finitely supported coefficients or explicit Taylor formula.

Completed `Roth.det_sum_rows`: Possible named weighted multilinear finite-sum convenience law or determinant-specific row-expansion corollary, not a claimed missing mathematical theorem.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_genWronskian_ne_zero`: Bounded generalized Hasse-Wronskian nonvanishing criterion for independent finite polynomial families; finite-family univariate criterion and multivariate Hasse interface are prerequisite API.

Completed `Roth.sqrt_one_sub_inv_lt`: No missing generic tangent API; whether to add the extra threshold convenience API is an upstream design question.

Completed `Roth.inv_add_inv_le`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.sum_inv_le`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.sum_inv_lt`: Candidate generic convex symmetric-average endpoint theorem or positive reciprocal-grid rational bound; exact sqrt corollary may remain downstream.

Completed `Roth.extend_apply_castSucc`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.extend_apply_last`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_box_fiber_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_box_last`: Design question: named arbitrary dependent tuple sections/cardinality law and binary filtered-product wrapper; no categorical structure required.

Completed `Roth.filter_weight_le_eq_empty`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_fiber_eq`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_weight_le_succ_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_weight_le`: Design choice: named finite-product normalized lower-tail count versus primary stronger product-measure concentration with local count corollary; retain redundant project box/weight aliases outside mathlib.

Completed `Roth.index`: No new generic minimum-support definition needed. A named point-index wrapper and normalization bridge can remain local; infinity-preserving API is distinct at zero.

Completed `Roth.mem_support_taylor_iff`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.index_le_weight`: No missing generic upper-bound law. Parent finite-sInf/infDegree projection bridge is normalization glue; coeff_taylor is separate project API.

Completed `Roth.exists_weight_eq_index`: No missing generic attained-minimum law. Parent finite-sInf/infDegree bridge and Taylor coefficient conversion are real normalization and separately justified project API.

Completed `Roth.le_index_iff`: No missing lower-bound law on infDegree. Parent coefficient/translation and real-default bridge are normalization API separately assessed.

Completed `Roth.index_nonneg`: No missing nonnegative-support lower-bound law on infDegree; project normalization bridge is actual new proof, not an existing mathlib call.

Completed `Roth.index_eq_zero_iff`: No missing generic finite-infimum bottom criterion; real/NNReal/Taylor bridges are new normalization proofs.

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Compatible coefficient-support shifts imply infDegree lower bounds, with Hasse derivative specialization and explicit finite minimum projection bridge.

Completed `Roth.le_index_sum`: No missing analogous sum law. Parent real-projection/Taylor normalization is a separately proved bridge, not existing-call replacement.

Completed `Roth.weight_eq_finsuppWeight_div`: No missing generic naturality law identified; supportClear is new normalization glue, not an existing mathlib replacement.

Completed `Roth.index_eq_weightedOrder_div`: MvPowerSeries.weightedOrder_coe against AddMonoidAlgebra.infDegree; proposed new theorem, not preexisting replacement

Completed `Roth.index_mul`: Potential extremal weighted-homogeneous component multiplication and arbitrary-real polynomial infDegree multiplication law. Existing component, support, graded decomposition APIs support arbitrary additive commutative weight monoids. Scope/normal-form design remains open; no absence theorem claimed.

Completed `Roth.index_prod`: Potential polynomial infDegree finite-product equality for real additive weights, likely grouped with binary equality and extremal weighted homogeneous component multiplication. No proof of absence claimed.

Completed `Roth.index_neg`: No essential gap; infDegree_neg name absent in loaded pin but exact law exists on OrderDual.

Completed `Roth.index_C_mul`: No essential mathematical gap. Named degree_smul convenience not identified; explicit congruence composition sufficient.

Completed `Roth.index_mul_left_weights`: No missing generic law: map_finset_inf. Project zero-default and reciprocal-weight adapters verified as new normalization proofs; not counted as existing mathlib primitives.

Completed `Roth.index_rename`: No essential mathematical gap. A discoverability-only infDegree rename wrapper is a separate API design choice; composition already uses two existing calls.

Completed `Roth.index_le_card`: Choice of named Taylor coordinate-degree envelope and its cardinality corollary versus generic support-witness use. Mathematical proofs are complete; upstream API questions remain.

Completed `Roth.index_unique`: Potential generic normalization API between finite real support minimum, projected infDegree and polynomial trailingDegree; exact new bridge evidence supplied, no unsupported absence claim.

Completed `Roth.coeffNone`: None required for the definition. Bundled coefficient map is existing composition; no claim of a preexisting name for whole composite.

Completed `Roth.eq_mapDomain_some_add_single`: No missing reconstruction law; optional naming question for additive Option normal form is not a blocking gap.

Completed `Roth.coeff_X_none_pow_mul_rename`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.coeff_coeffNone`: No missing coefficient law. An optional named Option-index bridge is a separate normal-form API question.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: No missing reconstruction theorem. A named inverse-C/rename bridge is optional convenience API; scratch bridge is new proof, not a counted mathlib call.

Completed `Roth.degreeOf_coeffNone_le`: Candidate Option-variable coordinate-degree coefficient law beside existing Fin analogue; whether to expose it directly or via a more general support-degree transport API is an upstream design question.

Completed `Roth.coeff_rename_mul_aeval`: Potential MvPolynomial coefficient adapter for separated Option-variable product, or reusable optionEquivLeft rename/aeval transport law; upstream API design question, not an absence theorem.

Completed `Roth.aeval_X_eq_rename`: None needed for exact target or five complete callers.

Completed `Roth.hasseDeriv_rename_mul_aeval`: Upstream multivariate Hasse derivative parent and compatibility API, Fresh-coordinate separated-product law over arbitrary injective embeddings; newly verified proof, not existing mathlib call

Completed `Roth.coeff_uniqueAlgEquiv_symm`: None

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: Potential named uniqueAlgEquiv degree rewrite or normalization bridge; upstream design choice rather than established mathematical gap.

Completed `Roth.degreeOf_rename_mul_aeval`: Design choice between degree preservation under multiplication by a nonzero zero-degree factor and degree zero outside the range of a renaming. No global absence claim.

Completed `Roth.degreeOf_none_rename_mul_aeval`: Design choice: general optionEquivLeft/rename-some AlgHom normalization bridge versus further separated degree wrapper.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_coeffNone_basis_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_separated_representation`: Bounded independent separated decomposition, using generic finite-free coefficient-span machinery.

Completed `Roth.det_hasseDeriv_separated`: Multivariate Hasse derivative and fresh-coordinate factorwise law, settled finite-family Hasse-Wronskian API (binary polynomial Wronskian file has n-tuple TODO), and possible public separated derivative matrix/determinant factorization.

Completed `Roth.exists_sum_mul_eq_gcd`: None

Completed `Roth.exists_nat_smul_eq_map`: Design question: positive-natural rational-polynomial specialization versus generic map/scalar numerator bridge; no generic denominator-law gap.

Completed `Roth.exists_primitive_smul_eq`: MvPolynomial primitive representatives over a normalized GCD domain and its fraction field, with mapped scalar identity and coefficient gcd one. Finset.extract_gcd and localization are existing ingredients, not the full result.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: finite-gcd scalar membership in an arbitrary submodule over a Bezout ring

Completed `Roth.rescale_separated_factor_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_int_factors`: Generic multivariate primitive representative (accepted172 proposal)., Finite primitive coefficient scalar descent over GCD domains (new reduced-fraction proof)., Separated polynomial factor descent with all degree conclusions.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_det_eq_mul`: Finite-family Hasse Wronskian nonvanishing with bounded row orders, Separated original-ring factor descent over normalized GCD domains, Generic CommRing degree bound for Hasse derivative determinants, Synthesis theorem preserving separated nonzero factors and all individual bounds

Completed `Roth.RSet`: Potential generic multivariate naive coefficient-height interface and support/degree bridges; not an established upstream design.

Completed `Roth.indexSet`: No missing generic image API established; possible arithmetic-height/support laws require separate assessments.

Completed `Roth.Θ`: No missing generic supremum constructor/bound API established. Broader arithmetic-height/index development is a separate assessment.

Completed `Roth.lem6M`: Upstream packaging of auxiliary polynomial height/index infrastructure is a design question; later declarations assessed independently.

Completed `Roth.lem6Φ`: No missing API for outer constructor; index-infDegree bridge is new representation evidence assessed separately, not a claimed existing replacement.

Completed `Roth.one_mem_RSet`: Possible generic nonzero degree/height family unit-membership API, to be designed with BORDERLINE parent RSet; no missing primitive lemma needed for current proof.

Completed `Roth.indexSet_nonempty`: No missing binary-image nonempty law. Accepted184 bounded-family API judgment remains separate.

Completed `Roth.indexSet_bddAbove`: Upstream design choice for reusable weighted Taylor degree-envelope law; generic binary-image packaging needs no new theorem.

Completed `Roth.index_le_Θ`: No missing generic supremum law. Substantive arithmetic boundedness remains project API, accepted186 BORDERLINE; it is not a mathlib building block.

Completed `Roth.Θ_nonneg`: None

Completed `Roth.Θ_le_card`: Whether a Taylor coordinate-degree/cardinality envelope merits named upstream API after the index/Taylor parent representation is settled. Generic supremum transport is present; no claim that search failure proves absence.

Completed `Roth.Θ_le_of_forall_index_le`: No missing supremum-upper-bound API. image2 transport exists as Set.forall_mem_image2; arithmetic polynomial bounds remain separate.

Completed `Roth.Θ_mono`: No missing generic supremum monotonicity law. A local indexSet-height inclusion helper may improve organization; it is not an existing mathlib replacement. This does not resolve the substantive boundedness API assessment.

Completed `Roth.indexSet_comp_subset`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.Θ_equiv`: Potential bounded-polynomial/height family transport interface; upstream design question, not an established missing generic supremum law.

Completed `Roth.isPrimitive_linear`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.isPrimitive_pow`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_eq_pow_mul_of_rootMultiplicity`: Polynomial.pow_linear_dvd_of_rootMultiplicity: primitive reduced linear-factor power divides over a GCD domain to the full fraction-field root multiplicity. Generic primitive-linear and primitive-power helpers are additional new-proof candidates, not existing mathlib replacements.

Completed `Roth.pow_rootMultiplicity_le`: Generic multiplicity integral-linear-factor descent and denominator-power leading-coefficient divisor; numeric discrete-order corollary.

Completed `Roth.index_unique_le_log_div`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.Θ_unique_le`: Upstream decision on coefficient/degree-bounded arithmetic extremal families; independently useful multiplicity-sensitive denominator and leading-coefficient APIs already assessed196/197.

Completed `Roth.one_le_lem6M`: No missing elementary order arithmetic API identified. Open upstream choice is whether a named proof-specific coefficient envelope and its lower-bound certificate belong in Roth auxiliary-polynomial infrastructure.

Completed `Roth.floor_sq_div_two_le_sum`: Potential exact affine arithmetic-series normalization or arbitrary natural-cutoff lower-bound API; these are newly proved candidates, not existing hits.

Completed `Roth.sq_div_three_lt_floor_sq_div_two`: Potential numeric floor-square comparison or arbitrary approximation polynomial-comparison API; demand and statement grain remain design questions. All proposed helpers are new proofs.

Completed `Roth.mul_div_two_le_sum_max_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.mul_sq_div_three_le_sum_max_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.min_le_sum_max`: Potential finite positive-part arithmetic-progression estimate at ordered-field level, with quadratic denominator2; audience and public endpoint versus branch API remain design questions. All candidate helpers are newly proved.

Completed `Roth.sum_max_sub_le_index_det`: Upstream design choice: generic determinant lower bound against valuation/infDegree with top, and separation of entry Hasse bound from matrix transport. Current real index maps zero to0, requiring nonvanishing guards.

Completed `Roth.index_separated_mul_le_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.index_det_le`: Potential reusable separated coefficient-height transfer with size≥1 witnesses; audience and primary extremal-index endpoint remain future upstream scope questions.

Completed `Roth.weight_le_delta_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.mapped_det_ne_zero_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.index_numeric_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.index_le_lem6`: Potential reusable numerical witness and stronger finite-sum interfaces, plus generic determinant-order and separated integer factor-height prerequisites; whole upstream audience/module remains a design choice.

Completed `Roth.Θ_option_le`: No missing order-transport primitive. Possible upstream material lies in reusable determinant, factor-height, numerical witness and finite-sum ingredients; the specialized recursive Θ endpoint needs a separate audience/interface decision.

Completed `Roth.factorial_coefficient_le_two_pow_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.two_pow_lt_rpow_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.lem6M_lt`: Potential public package: determinant coefficient-height envelope with factorial overhead and explicit large-denominator absorption. Whether this particular envelope should be public remains an audience/design question, not a proven universal missing API.

Completed `Roth.lem7_Φ_bound`: Potential generic weighted real-power absorption interface; no universal absence claim. Public usefulness and choice between primitive product/exponent bounds and a packaged envelope remain upstream API-design questions.

Completed `Roth.lem7_numeric`: Potential public weighted square-root absorption API, subject to demonstrated audience; scratch envelope is new proof, not existing mathlib.

Completed `Roth.theta_scaled_unique_le_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_delta_succ_lt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_prefix_lt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_lt_base_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_denominators_one_lt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_phi_lt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_lt_succ_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_lt_of_large_delta_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.Θ_lt`: Potential reusable generalized-Wronskian separation, determinant coefficient-height estimates and rational-point weighted-index API. No missing generic supremum transport. Upstream inclusion/grain of the specialized10^m endpoint remains an explicit bounded design question.

Completed `Roth.lam`: No missing basic sqrt/arithmetic/continuity API shown. Potential reusable cutoff/count theorem boundary must be designed together with the auxiliary-polynomial and lattice estimates; scratch scaleCount is a new generic proof, not an existing mathlib lemma.

Completed `Roth.gam`: No arithmetic infrastructure gap. A gamma continuity lemma can shorten exists_delta locally; proof compiled by fun_prop after unfolding. The substantive reusable index/counting API should be assessed separately.

Completed `Roth.eta`: No arithmetic infrastructure gap. A local eta continuity/zero API could shorten exists_delta_bound and exists_delta; project-context proofs compile with existing Real.continuous_rpow_const/zero_rpow. Upstream reusable index-estimate semantics remain an API design question.

Completed `Roth.mainCoeffBound`: No missing arithmetic API needed for this definition. The isolated sqrtLower proof is new assessment evidence of the earlier project generic floor estimate, not an existing mathlib replacement or an automatic verdict for that theorem.

Completed `Roth.boxFamily`: Potential general degree-box/coefficient-family image bridge; whether a named family belongs upstream is an API choice.

Completed `Roth.exists_delta_bound`: Possible convenience helper for positive-power perturbations on a closed right interval; generic topology transport already exists. Whether to add that helper is an upstream API choice.

Completed `Roth.eta_lt_gam_iff`: No established mathematical gap; upstream naming of the normalized scalar identity or a future Roth parameter API remains a design question.

Completed `Roth.sqrt_lt_nat_floor_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.sqrt_lt_floor`: Candidate standalone strict/iff sqrt-floor or broader root-witness API; arbitrary-real floor/sqrt bridge also proved. Generic floorSquare is verified three-block composition, not a missing primitive.

Completed `Roth.four_lt_rpow`: Upstream design candidate: numerical square-gap-to-power comparison versus use of existing square/multiplication monotonicity plus normalization. Exact general API choice remains a future taste question.

Completed `Roth.mul_log_div_two_lt_log_mainCoeffBound`: Potential generic logarithm-of-natural-floor lower-bound API; primary square-root-floor interface versus logarithmic corollary packaging remains a future upstream design choice.

Completed `Roth.two_lt_rpow_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.three_small_factors`: Possible generic strict floor-power absorption from a non-strict half-log budget; its API boundary relative to floor/log primitives and exact Roth triple remains a future upstream design choice.

Completed `Roth.exists_norm_coeff_reduction_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.norm_coeff_modByMonic_le`: Quantitative coefficient growth under iterated monic reduction; choice of direct norm, bundled seminorm or supNorm public interface remains upstream design.

Completed `Roth.boxFamily_eq_image_finsupp_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.boxFamily_finite`: A semantic finite-coefficient/finite-support bridge for MvPolynomial is the candidate API boundary; current Finset.finsupp image machinery already supplies the enumerated form.

Completed `Roth.ncard_boxFamily`: Potential semantic coefficient-family representation/counting interface; existing enumerator cardinality APIs already suffice after the new bridge. Exact upstream API packaging remains a future question.

Completed `Roth.floor_rpow_count_lt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.pigeonhole_count`: Possible arbitrary strict-base/exponent-budget lifting law with explicit zero-exponent behavior; public value undecided., Possible scalar floor-count estimate; supplied project helper is not existing mathlib.

Completed `Roth.exists_ne_modByMonic_eq`: Potential finite-alphabet polynomial-observation collision bridge, with finite/infinite source handling. Both outer pigeonhole principles and low-degree monic reconstruction already exist; finite support is not a missing mathematical prerequisite.

Completed `Roth.sub_mem_RSet`: Possible combined coefficient-family subtraction inclusion with degree bounds; three concrete future upstream design questions in report.

Completed `Roth.eval_hasseDeriv_sub_eq_zero`: Upstream design decision between a generic equal-remainder evaluation companion, a reusable diagonal-evaluation bridge, and retaining the full Hasse corollary locally; three concrete future questions in report.

Completed `Roth.le_index_of_forall_eval_eq_zero`: Potential discoverability for bounded Hasse/Taylor support checking, not a missing finite-infimum order law. Upstream choice between a public boxed convenience theorem and local use of shared support bridges remains a taste/API question.

Completed `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`: Potential positive-scale budget-transfer family; scratch proof is new, not existing mathlib API. No missing instance or simp API justified.

Completed `Roth.exists_hasseDeriv_eval_ne_zero`: No new strict finite-infimum witness law needed. Project translation/Hasse coefficient bridge and zero-default real projection are separate normalization API, not existing mathlib calls.

Completed `Roth.abs_eval_iterated_hasseDeriv_lt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_hasseDeriv_index_eval_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_mem_RSet_le_index_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.mul_card_filter_weight_le_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_mem_RSet_le_index_of_log_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_auxiliary_polynomial_of_log_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.theta_lt_eta_of_sq_log_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_auxiliary_polynomial_with_index_gap_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.main_lemma`: Quantitative bounded-coefficient high-index auxiliary polynomial plus derivative selection at a prescribed rational tuple; reusable Hasse/index, remainder-height and evaluation-height support can precede the Roth feature.

Completed `Roth.approxSet`: Choose a primary named approximation family and expose finite slices, reduced rational image/fiber conversions and frequent-witness/LiouvilleWith bridges together.

Completed `Roth.exists_nat_mul_isIntegral`: No mathematical gap for the real result: stronger existing nonzeroNat integral-closure existence and normalized denominator API verified. Do not propose the scratch RingA sign lemma as already existing; it is a newly verified generic proof.

Completed `Roth.approxSet_den_le_finite`: Potential upstream choice between arbitrary-ψ approximation slices and a general finite integer-cast tube lemma. Finite image/fibers already exists; arithmetic interval transport remains real proof.

Completed `Roth.eventually_div_rpow_lt`: Exported eventual inequality comparing arbitrary amplitudes across real exponent gaps at infinity.

Completed `Roth.reduction`: Potential fixed-unit pair scaling/threshold API or explicit bridge to LiouvilleWith. Whether to introduce a second approximation representation upstream is unresolved design, not unfinished proof verification.

Completed `Roth.exists_monic_aeval_eq_zero`: Possible arbitrary-cutoff monic-annihilator existence API; packaging choice remains a future upstream question.

Completed `Roth.approxSet_num_den_mem_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_reduced_approx`: Finite fixed-rational-value fibers for decay approximation sets, canonicalization-to-unbounded-reduced-denominator transfer, and public unrestricted/subcritical existence interfaces.

Completed `Roth.exists_m`: Possible reusable generic scalar dimension selector, own signed-a,b proof verified; upstream home/publicness remains design question.

Completed `Roth.exists_delta`: Potential simultaneous quantitative perturbation convenience lemma; generic point selection itself already exists. Public API scope remains a future question.

Completed `Roth.exists_approximants`: Possible cofinal real-height recursive-growth selection theorem, with finite-chain corollary. Generic scratch theorem is new proof; upstream API granularity remains a future design question.

Completed `Roth.exists_degrees`: Finite simultaneous positive-weight natural rounding with an arbitrary relative error, lower degree bound and strict separation margin.

Completed `Roth.one_le_prod_pow_mul_abs_eval`: Coordinatewise multivariate polynomial denominator-clearing equality at arbitrary rational points with individual degree bounds, and nonzero integer lower-bound corollary.

Completed `Roth.abs_prod_pow_le_rpow_of_le_weight`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.abs_eval_lt_of_le_index`: Reusable weighted finite expansion decay plus an eventual multivariate Taylor/order interface; no current verified exact mathlib replacement.

Completed `Roth.exists_roth_parameters_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_roth_approximants_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.one_lt_roth_eval_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.roth_product_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.roth_log_bound_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.roth_of_isIntegral`: New exponent-family LiouvilleWith bridge and bounded-denominator/frequently transport, Actual Roth exponent2 exclusion for algebraic integers; pinned LiouvilleWith doc names this missing theorem, Staged Hasse/Taylor/index and main-lemma dependencies

Completed `Roth.roth`: Sharp exponent2 exclusion for algebraic real LiouvilleWith values, New bounded-denominator/frequently transport and exponent-family equivalence, Staged auxiliary polynomial/Hasse/Taylor/index/Roth-main-lemma prerequisites

Completed `Roth.roth_rat`: Algebraic real exponent-two Roth theorem is the substantive missing API; add the all-algebraic rational endpoint as a corollary of the coherent theorem package, using existing rational-center finiteness.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`: Uniform-bound iff irrationality-conjoined LiouvilleWith exponent cutoff; scratch proof new, not existing mathlib.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`: Generic finite-exception/uniform-bound and exponent-cutoff bridges; decide normal form before exporting new definitions.

## Part 7: Junk / removable

hasseCoeff is live API, not dead code. Keep it locally during this read-only overview.
The detailed report provides an optional all-callers inlining plan for a later authorized
refactor; it has not been executed or falsely reported as validated.

The derivative is live API across Taylor expansions, multiplicities and generalized
Wronskians; retain it. No production removal or refactor was performed.

Completed `MvPolynomial.hasseDeriv_monomial`: Not junk: seven explicit uses across four caller declarations, including Taylor interface.

Completed `MvPolynomial.hasseDeriv_apply`: Not junk: one explicit caller uses the support expansion to bound normOne.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: Useful semantic interface at3callers; not dead or vacuous.

Completed `MvPolynomial.coeff_hasseDeriv`: None: substantial coefficient interface, not glue, unused code or a three-call wrapper.

Completed `MvPolynomial.hasseCoeff_eq_prod`: Useful local semantic rewrite with one caller, but a redundant standalone upstream wrapper; not narrow rfl/unfold glue.

Completed `MvPolynomial.hasseDeriv_zero_apply`: Used at three explicit sites and semantically standard; not dead code or rfl/unfold glue. It may be API-redundant if only bundled normalization is exported.

Completed `MvPolynomial.hasseDeriv_zero`: No explicit callers, but a registered simp rule with actual implicit-consumer demonstrations; not established dead code, and not rfl/unfold glue.

Completed `MvPolynomial.hasseDeriv_C`: Not junk: one real Taylor induction caller, standard positive-order law, no inherited glue classification.

Completed `MvPolynomial.hasseDeriv_map`: False

Completed `MvPolynomial.hasseDeriv_rename`: False

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Retain shared private helper, two real uses; no deletion/export recommended.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: No: canonical normalization used by disjoint law and index inequality.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: No: reusable geometric API supporting separated-variable determinant proof.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Retain private descriptive two-line specialization, no source change recommended.

Completed `MvPolynomial.pderiv_hasseDeriv`: No: factorial iteration and generalized Wronskian recurrence use it.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: No: five direct invocations in two files, canonical common API.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: No: reused in translation degree, finite Taylor expansion and index box restriction.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Retain focused private induction helper; one real use, no deletion/export recommended.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: No: two explicit calls in one theorem are essential steps toward separated determinant factorization.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: Not dead: one explicit consumer; no inline duplicate located.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: False

Completed `MvPolynomial.hasseCoeff_le_two_pow`: False

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Unused explicitly in project; retain as standard canonical operator compatibility API, not evidence of hidden callers.

Completed `Roth.box`: Useful local semantic API; not dead code.

Completed `Roth.weight`: No sorry/unsafe/raised limits; upstream duplicate, locally semantically useful.

Completed `Roth.mem_box`: Not dead:7 caller declarations. Thin wrapper candidate.

Completed `Roth.card_box`: Useful local API with 3 consumers, redundant as upstream addition.

Completed `Roth.card_le_card_box`: False

Completed `Roth.weight_nonneg`: Useful three-caller project API, not dead code.

Completed `Roth.weight_zero`: Not dead-code conclusion: simp API can be used without explicit name.

Completed `Roth.weight_add`: Useful local rewrite API (three callers), not dead code; no independent upstream addition recommended.

Completed `Roth.weight_eq_zero_iff`: False

Completed `Roth.weight_single`: Not dead: two explicit caller files; no simp attribute.

Completed `Roth.weight_le_card`: One real caller; not dead code.

Completed `Roth.weight_mul_left`: No sorry/unsafe/raised limits; active one-consumer local convenience theorem.

Completed `Roth.weight_le_degree_div`: No sorry/unsafe/raised limits. Zero explicit callers is only source-level evidence, not proof of dead public API.

Completed `Roth.weight_mapDomain`: Useful local API with three callers; redundant upstream analogue, not unused/dead code.

Completed `Roth.wronskianMatrix`: False

Completed `Roth.wronskian`: False

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: False

Completed `Roth.det_choose_eq`: No; explicitly used once in Wronskian nonvanishing. No external-to-file reference claim or simp-closure inference.

Completed `Roth.coeff_prod_of_natDegree_le'`: Retain focused private induction helper for sole actual caller; prime distinguishes common-bound theorem.

Completed `Roth.sum_range_le_sum_of_injective`: Unused public convenience wrapper; zero explicit callers, zero inline re-derivations found.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: No: sole local caller supplies nonvanishing induction base. Historical name can be improved.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: False

Completed `Roth.wronskian_update_sub_smul`: Useful sole induction caller; not dead code.

Completed `Roth.linearIndependent_update_sub_smul`: Used twice; not dead code, but public polynomial-specific theorem duplicates existing generic law.

Completed `Roth.sum_natDegree_update_lt`: Live induction-measure helper, not junk.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: No: same-module iff plus two independent external consumers.

Completed `Roth.wronskian_eq_zero_iff`: No deletion: zero named source callers, but explicitly documented main public criterion; related downstream results use its primary implication. No simp attribute currently.

Completed `MvPolynomial.taylor`: One-line definition with concrete semantic/API-stability exemption; no automatic deletion merely from line count.

Completed `MvPolynomial.taylor_apply`: Zero named callers; standalone bridge is dispensable. Semantic translation definition is independently BORDERLINE, not inherited here.

Completed `MvPolynomial.taylor_X`: Used by one named private caller and exported as simp; not dead code. Redundant standalone mathematical result.

Completed `MvPolynomial.taylor_C`: Not dead code: one explicit named caller plus simp API; redundancy is independent of usage.

Completed `MvPolynomial.taylor_monomial`: Redundant local specialization with one explicit caller; no dead-code inference.

Completed `MvPolynomial.coeff_aeval_X_mul`: Retain private helper; useful boundary in monomial-induction proof. No sorry, resource raise, TODO or excessive proof size.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Keep private helper; short coordinate calculation separates scalar combinatorics from polynomial coefficient proof.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Retain private helper; clear algebraic boundary in monomial coefficient induction; no sorry, resource raises or unused local assumptions.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Retain private induction-step helper to keep Finsupp induction case concise; no sorry, limitraise or long proof.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Retain private monomial boundary; full public theorem then reduces to additivity and this case.

Completed `MvPolynomial.coeff_taylor`: False

Completed `MvPolynomial.eval_taylor`: No named callers; not a simp theorem. Unused public compatibility API, not automatically dead code.

Completed `MvPolynomial.taylor_taylor`: Live: sole direct caller supplies negative-translation inverse, then injectivity/nonzero and Taylor expansion. No automatic junk verdict.

Completed `MvPolynomial.taylor_zero`: Not dead: simp attribute has verified implicit inverse-translation caller despite zero explicit references.

Completed `MvPolynomial.taylor_map`: Unused by explicit project source references, but standard base-change convenience law; zero references alone does not establish dead code.

Completed `MvPolynomial.taylor_rename`: Used in index invariance, not dead code. One source use and generic derivation do not by themselves force deletion.

Completed `MvPolynomial.degreeOf_taylor_le`: Used by index/cardinality bound; not dead code. Short proof relies on genuine new Hasse/Taylor content.

Completed `MvPolynomial.taylor_neg_taylor`: Two live mathematical callers, so not dead code; optional inlining depends on retaining or replacing the named translation API.

Completed `MvPolynomial.taylor_injective`: Live zero-reflection caller; named convenience corollary status depends on future translation API.

Completed `MvPolynomial.taylor_eq_zero_iff`: Live simplifier API with4 production consumers; not unused despite0explicit tokens.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Keep standard substantive reconstruction theorem; actual evaluated consumer feeds main Diophantine estimate.

Completed `MvPolynomial.eval_eq_sum_box`: Keep standard exact identity with actual use in Roth upper estimate; short corollary of a missing substantive project theorem is not existing-mathlib duplication.

Completed `Roth.normOne`: Useful semantic one-line local API with fourteen consumers; keep in Roth/CoeffNorm.lean under production freeze. No assertion the norm laws or determinant estimates are junk.

Completed `Roth.diag`: Useful one-line semantic local API with eleven consumers; retain in CoeffNorm under production freeze. No claim downstream estimates are junk.

Completed `Roth.normOne_nonneg`: Useful local convenience with two consumers, not dead code. No production deletion in read-only survey.

Completed `Roth.normOne_eq_sum_of_support_subset`: Useful local convenience with two consumers/four rewrites; not dead code. No source changes in assessment.

Completed `Roth.normOne_monomial`: Useful project convenience with three consumers, not dead code; no source changes in read-only assessment.

Completed `Roth.normOne_zero`: Useful local public simp convenience with one explicit caller; not dead code. Direct proof audit closes293 values but does not justify deleting future/public simp API without refactor/rebuild.

Completed `Roth.abs_coeff_le_normOne`: Useful local convenience, not dead mathematics; no simp attribute, one explicit caller. Redundant as upstream theorem.

Completed `Roth.normOne_add_le`: Useful local subadditivity witness; one actual caller precludes dead-code classification.

Completed `Roth.normOne_neg`: Useful local sign simplification used in determinant, not dead code; redundant as an upstream contribution.

Completed `Roth.normOne_sum_le`: Not dead:4 occurrences in3 consumers. One-call local convenience whose upstream role follows coefficient-size API design.

Completed `Roth.normOne_mul_le`: Live main-result helper; not dead or junk.

Completed `Roth.normOne_prod_le`: Live helper for determinant norm estimate; no dead-code conclusion.

Completed `Roth.normOne_le_card_mul`: Thin wrapper with one caller; useful estimate, redundant public declaration.

Completed `Roth.normOne_det_le`: Not junk: module Main result and direct Lemma3 consumer.

Completed `Roth.abs_coeff_hasseDeriv_le`: Not junk: three explicit uses support main Lemma9, including iterated derivatives and diagonal remainder bounds.

Completed `Roth.normOne_hasseDeriv_le`: Keep estimate; integer-specific spelling becomes local specialization. Test-only size helper is not recommended public upstream API.

Completed `Roth.diag_eq_sum`: Not dead: two direct callers use the common expansion.

Completed `Roth.abs_coeff_diag_le`: Used by sole remainder coefficient estimate in Roth main lemma; not dead. No rewrite attribute or instance side effects.

Completed `Roth.natDegree_diag_le`: Not dead: one explicit and one canonical direct proof consumer, same private MainLemma theorem.

Completed `Roth.eval_diag`: Unused named wrapper; no simp attribute. Zero references alone not proof of mathematical uselessness.

Completed `Roth.diag_sub`: Not dead: one genuine consumer, mechanically replaceable using typed hdiag.

Completed `Roth.geom_sum_le_one_add_pow`: Used by private helper; not dead code.

Completed `Roth.sum_box_prod_pow_le_aux`: Retain this four-line private proof boundary with its single public caller. No sorry, new axiom, TODO or raised resource limit.

Completed `Roth.abs_eval_le`: Not junk: live main-lemma dependency and nontrivial finite weighted-support reasoning.

Completed `Roth.degreeOf_det_hasseDeriv_le`: Used twice; sound nonvacuous inequality; no junk classification.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Sound, used main-result lemma with nonempty and empty determinant cases; no junk finding.

Completed `Roth.genWronskian`: No dead-code claim; standard named invariant with5 explicit consumers and stable nonvanishing interface.

Completed `Roth.kronecker`: Useful local semantic API, not dead code. No new typeclass/coercion instance.

Completed `Roth.kroneckerExp`: Useful local semantic one-line API with3 callers; not dead code. No new instance/coercion structure.

Completed `Roth.kronHasse`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.kronSpan`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: No present named callers; mathematically standard paper lemma, not automatically junk.

Completed `Roth.kronecker_monomial`: Useful single-caller local coefficient calculation; no simp attribute, not dead code or an independent upstream contribution.

Completed `Roth.kroneckerExp_injOn`: Useful non-simp arithmetic helper, not dead; project alias should be replaced by general upstream law.

Completed `Roth.coeff_kronecker`: Not junk: actual zero-detection consumer supports generalized Wronskian theorem.

Completed `Roth.kronecker_eq_zero_iff`: Not dead: sole explicit caller and canonical direct dependency agree; no inline duplicate found.

Completed `Roth.linearIndependent_kronecker`: No; actual sole source consumer verified by replay.

Completed `Roth.derivative_aeval`: Live single-consumer helper feeding higher-order Kronecker/Hasse recurrence, not dead code.

Completed `Roth.derivative_kronHasse_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.derivative_mem_kronSpan`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.hasseDeriv_kronecker_mem`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Live Wronskian helper; single explicit consumer does not make it dead or automatically composable.

Completed `Roth.det_sum_rows`: Live single-use helper; private local lemma or inlining is concrete alternative.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_genWronskian_ne_zero`: Live module main theorem, substantive classical result; not junk despite a single direct consumer.

Completed `Roth.sqrt_one_sub_inv_lt`: Live single-use scalar helper; retain locally while upstream scope is undecided.

Completed `Roth.inv_add_inv_le`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.sum_inv_le`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.sum_inv_lt`: Not dead: one private induction caller supports public lattice-count estimate. No duplicate full inline derivation found.

Completed `Roth.extend_apply_castSucc`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.extend_apply_last`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_box_fiber_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_box_last`: No: sole live induction consumer. Public visibility could become private if current source API suffices.

Completed `Roth.filter_weight_le_eq_empty`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_fiber_eq`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_weight_le_succ_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_weight_le`: No: live sole count estimate on the auxiliary-polynomial/main-lemma path.

Completed `Roth.index`: False

Completed `Roth.mem_support_taylor_iff`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.index_le_weight`: False

Completed `Roth.exists_weight_eq_index`: False

Completed `Roth.le_index_iff`: Not dead: four consumers/five uses; not simp. Specialized wrapper need not be upstream.

Completed `Roth.index_nonneg`: Not dead; three consumers, not a simp theorem. Useful manuscript-facing local convenience, no upstream theorem gap.

Completed `Roth.index_eq_zero_iff`: Used local manuscript convenience API, not dead code; redundant upstream after parent re-aim.

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Used twice; no dead-code or duplicate-wrapper deletion justified.

Completed `Roth.le_index_sum`: Used once in determinant proof; not dead code. Local manuscript wrapper may remain while upstream contribution would duplicate existing degree API.

Completed `Roth.weight_eq_finsuppWeight_div`: Active local implementation bridge; not dead code.

Completed `Roth.index_eq_weightedOrder_div`: Active local API, three applications in sole caller; not dead code.

Completed `Roth.index_mul`: Not junk: two callers, one in another module, and a module main result. No independent production inline duplicate found.

Completed `Roth.index_prod`: Not junk: module main result and one determinant caller in another module. No independent inline duplicate found in production.

Completed `Roth.index_neg`: Currently unused theorem without simp attribute; harmless local compatibility helper, not evidence of external deadness.

Completed `Roth.index_C_mul`: Used compatibility adapter; not dead code. No proof holes or infrastructure changes.

Completed `Roth.index_mul_left_weights`: Not junk: two proof applications in sole private caller. Not a simp theorem; no external use inferred.

Completed `Roth.index_rename`: Useful transport API, not dead code: equivalence and separate-variable embeddings are genuine consumers.

Completed `Roth.index_le_card`: No. Two actual callers use the bound. hP is redundant only under current projected real convention.

Completed `Roth.index_unique`: False

Completed `Roth.coeffNone`: Useful local helper with seven consumers; not dead code.

Completed `Roth.eq_mapDomain_some_add_single`: Not dead: one explicit and direct-kernel caller.

Completed `Roth.coeff_X_none_pow_mul_rename`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.coeff_coeffNone`: Useful: two explicit callers and two direct kernel-value consumers.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: Useful: one source caller and one direct kernel-value consumer.

Completed `Roth.degreeOf_coeffNone_le`: Zero explicit/kernel callers; one mathematically relevant inline derivation. Not automatically dead or automatically public API.

Completed `Roth.coeff_rename_mul_aeval`: Useful local adapter: three uses in two callers; not junk.

Completed `Roth.aeval_X_eq_rename`: Useful in five callers, hence not dead code; public wrapper duplicates existing bundled Mathlib API.

Completed `Roth.hasseDeriv_rename_mul_aeval`: False

Completed `Roth.coeff_uniqueAlgEquiv_symm`: No explicit callers and no direct canonical kernel consumers; exact redundant law established independently, so zero-use count is supporting evidence rather than a dead-API inference.

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: Not dead: two actual source uses and two exact native direct kernel-value consumers.

Completed `Roth.degreeOf_rename_mul_aeval`: Not junk: one explicit project use and one direct kernel-value consumer.

Completed `Roth.degreeOf_none_rename_mul_aeval`: Not dead: one explicit and direct kernel consumer, Roth.exists_det_eq_mul.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_coeffNone_basis_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_separated_representation`: Not junk: substantive finite-rank decomposition, both independent factor families and degree control are used to construct nonzero Wronskians in the sole caller.

Completed `Roth.det_hasseDeriv_separated`: Not junk: sole full private caller uses this identity to obtain rational separated factors, feeding integer separation; no duplicate inline derivation found.

Completed `Roth.exists_sum_mul_eq_gcd`: Useful current caller, so not dead code; redundant local wrapper.

Completed `Roth.exists_nat_smul_eq_map`: Live integrality helper with one source caller and one canonical direct consumer.

Completed `Roth.exists_primitive_smul_eq`: Not dead code: one explicit consumer uses every conclusion. Not safely deletable as a three-call wrapper.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: dead code: False; reason: one source caller and one direct kernel consumer in integral polynomial descent

Completed `Roth.rescale_separated_factor_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_int_factors`: status: False; reason: Main module result used by determinant factorization.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_det_eq_mul`: False

Completed `Roth.RSet`: Retain: live local arithmetic API; no dead-code/deletion recommendation. For B<0 the set is empty; zero is always excluded. Zero degree limits and empty/infinite variable types are valid inputs. All coefficients, including absent ones, are tested.

Completed `Roth.indexSet`: Live local semantic alias with4 textual caller declarations/5 occurrences and10 direct kernel value consumers; retain in Theta.

Completed `Roth.Θ`: Live semantic local alias,19 explicit callers/28 occurrences,13 direct kernel-value and17 type consumers. Retain locally; no deletion recommended.

Completed `Roth.lem6M`: Retain locally: live semantic API used on19 source lines by six declarations; not dead code.

Completed `Roth.lem6Φ`: Retain locally: useful semantic name used by five declarations; not dead code.

Completed `Roth.one_mem_RSet`: Retain locally in Roth/Theta.lean: live unit witness for index-family nonemptiness.

Completed `Roth.indexSet_nonempty`: Useful locally to2 supremum callers; delete wrapper with parent re-aim and use existing image2 law; local paper-navigation compatibility is the only retention rationale.

Completed `Roth.indexSet_bddAbove`: Not dead: two explicit uses. Docstring wrongly suggests positive r despite no premise.

Completed `Roth.index_le_Θ`: Useful local helper; not dead. Upstream duplicate of generic supremum API.

Completed `Roth.Θ_nonneg`: Not dead code: two explicit calls in one declaration; not tagged simp.

Completed `Roth.Θ_le_card`: Not dead: used once to close the large-delta branch of Lemma7. Retain local API during read-only assessment.

Completed `Roth.Θ_le_of_forall_index_le`: Not dead: two explicit applications and two direct canonical value consumers; no simp attribute. Local convenience spelling may be retained only as a deliberate downstream choice.

Completed `Roth.Θ_mono`: Used twice in private Lemma7 helpers; not dead code. No explicit type consumers or external-to-file callers. Not a simp theorem.

Completed `Roth.indexSet_comp_subset`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.Θ_equiv`: Live theorem; sole caller changes Fin coordinates to Option coordinates before Lemma6.

Completed `Roth.isPrimitive_linear`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.isPrimitive_pow`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_eq_pow_mul_of_rootMultiplicity`: No dead-code finding. Docstring mentions nonzero R while actual theorem permits zero; adjust prose during cleanup.

Completed `Roth.pow_rootMultiplicity_le`: False

Completed `Roth.index_unique_le_log_div`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.Θ_unique_le`: Not dead code: two actual private consumers. Short source proof is not a composition of existing mathlib arithmetic.

Completed `Roth.one_le_lem6M`: Not dead: one actual private consumer theta_phi_lt_aux, used to supply1≤M to Θ estimates. No full inline duplicate found.

Completed `Roth.floor_sq_div_two_le_sum`: Unused within this tracked project; no claim of external deadness. Source faithfully records a local fact from the paper.

Completed `Roth.sq_div_three_lt_floor_sq_div_two`: Unused by current source and canonical direct consumers; no external-deadness claim. Paper-facing second FACT is bypassed by the stronger direct-sum argument.

Completed `Roth.mul_div_two_le_sum_max_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.mul_sq_div_three_le_sum_max_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.min_le_sum_max`: Not dead: sole explicit determinant-index consumer is substantive; no simp attribute or external deadness claim.

Completed `Roth.sum_max_sub_le_index_det`: Live, not simp-tagged; one explicit caller and one canonical value consumer. Its source formula is specialized proof plumbing, while its matrix layer is reusable.

Completed `Roth.index_separated_mul_le_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.index_det_le`: The theorem has the live sole caller Roth.index_le_lem6 and supplies its determinant upper estimate; the caller and inline experiments establish useful proof structure, not a claim that the theorem can be removed.

Completed `Roth.weight_le_delta_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.mapped_det_ne_zero_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.index_numeric_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.index_le_lem6`: The live sole caller Θ_option_le uses the existential rank before taking a finite maximum and supremum. Complete inlining compiles but expands the mathematical argument and is not a recommendation to delete this proof-stage theorem.

Completed `Roth.Θ_option_le`: The live sole caller theta_lt_succ_aux uses this recursion before bounding each finite-maximum term. Complete inlining compiles but preserves the same mathematical argument; it is not evidence of dead code or a recommendation to delete the named Lemma6 stage.

Completed `Roth.factorial_coefficient_le_two_pow_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.two_pow_lt_rpow_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.lem6M_lt`: Not dead code: one explicit source caller and one direct canonical kernel-value consumer; its abstraction can organize the induction despite a single consumer.

Completed `Roth.lem7_Φ_bound`: Not dead code: sole explicit caller theta_phi_lt_aux uses the strict estimate in the induction. Its single use permits local inlining but does not prove a <=3-existing-call composition.

Completed `Roth.lem7_numeric`: Used once by theta_phi_lt_aux; verified actual caller and downstreamΘ_lt replay. Not dead code.

Completed `Roth.theta_scaled_unique_le_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_delta_succ_lt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_prefix_lt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_lt_base_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_denominators_one_lt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_phi_lt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_lt_succ_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_lt_of_large_delta_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.Θ_lt`: Live sole direct caller supplies the strictΘ<eta estimate used in the auxiliary-polynomial index gap and main lemma. Complete inlining compiles but retains the same project arithmetic proof; neither dead code nor≤3 existing-call redundancy.

Completed `Roth.lam`: Not dead code: four executable consumers and a local semantic/API-name exemption. Fully inlinable with all four original signatures and both full modules verified; public upstream status remains an API-grain question.

Completed `Roth.gam`: Used semantic parameter; not dead code. One-line public versus local status remains an upstream API decision after complete inlining verification.

Completed `Roth.eta`: Used semantic parameter, not dead code. Full inlining is mechanically possible, but one-line construction alone does not settle public versus local status.

Completed `Roth.mainCoeffBound`: Used local numerical notation, not dead code. Redundant as a standalone mathlib contribution because the exact construction uses3 existing operations; local semantic convenience remains valid.

Completed `Roth.boxFamily`: Not dead: seven actual consumers and semantic-name exemption. Literal inlining works, but does not establish an existing mathlib replacement.

Completed `Roth.exists_delta_bound`: Used, nontrivial 16-line proof; not established redundant. Inlining is possible and verified at the sole caller but adds the entire arithmetic/continuity argument.

Completed `Roth.eta_lt_gam_iff`: Not dead: two critical proof consumers. Full caller inlining works, but removing the stable named bridge is a local API decision.

Completed `Roth.sqrt_lt_nat_floor_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.sqrt_lt_floor`: Not dead (three callers); conjunction is useful local coefficient-bound packaging, not proven existing-only composable.

Completed `Roth.four_lt_rpow`: Used in two substantial callers. No verified existing-only ≤3-call replacement; full caller inlining duplicates substantive arithmetic. Retain locally pending API design.

Completed `Roth.mul_log_div_two_lt_log_mainCoeffBound`: Used and mathematically valid; not dead code. No demonstrated ≤3-existing-call replacement for original statement. Coefficient-specific public name should remain project-local pending generic API choice.

Completed `Roth.two_lt_rpow_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.three_small_factors`: Used by3 distinct private callers with all factors consumed. Keep locally; no demonstrated≤3-existing-call replacement. If inlining is chosen later, verified full caller experiments provide a mechanical recipe.

Completed `Roth.exists_norm_coeff_reduction_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.norm_coeff_modByMonic_le`: Not removable as a ≤3-existing-mathlib-call wrapper; the only local caller can use the new generic theorem but that is a new proof. Local direct inlining hit default limits and is not a deletion recommendation.

Completed `Roth.boxFamily_eq_image_finsupp_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.boxFamily_finite`: Used once and successfully inlined in its actual caller with unchanged type, but the inline still uses the project private representation bridge. Do not call it a pure existing-mathlib wrapper or dead code.

Completed `Roth.ncard_boxFamily`: Used mathematical count, not dead code. No unconditional removal from the local API is justified. Pure existing <=3-call replacement not established.

Completed `Roth.floor_rpow_count_lt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.pigeonhole_count`: Not dead: one private actual caller and transitive use in main_lemma. An actual inline proof compiles, but no <=3 existing-mathlib-call proof was established; deletion as trivial wrapper is unsupported.

Completed `Roth.exists_ne_modByMonic_eq`: Used once in the central auxiliary-polynomial construction. Inlining verified but expands the caller by the complete encoding proof; no dead-code or <=3-call wrapper finding.

Completed `Roth.sub_mem_RSet`: Used by one actual caller and transitively main_lemma; not dead code. Optional local inlining compiled, but the full tuple is not a ≤3 existing-call wrapper.

Completed `Roth.eval_hasseDeriv_sub_eq_zero`: Not dead code: one direct caller and the main-lemma continuation. Full inlining compiles but does not establish a ≤3 existing-call replacement for the entire theorem.

Completed `Roth.le_index_of_forall_eval_eq_zero`: Not dead code: the sole caller converts pigeonhole remainder equalities into the key index bound. Full inlining works but duplicates the degree-box proof; one use alone does not establish ≤3-mathlib-call composability.

Completed `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`: Unused within audited source/direct-kernel scope; candidate for local removal if no stable public API intended. No external/simp/transitive deadness claim.

Completed `Roth.exists_hasseDeriv_eval_ne_zero`: Used, mathematically valid local convenience. Redundant upstream after infDegree re-aim; candidate for local inlining, not dead code.

Completed `Roth.abs_eval_iterated_hasseDeriv_lt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_hasseDeriv_index_eval_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_mem_RSet_le_index_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.mul_card_filter_weight_le_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_mem_RSet_le_index_of_log_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_auxiliary_polynomial_of_log_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.theta_lt_eta_of_sq_log_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_auxiliary_polynomial_with_index_gap_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.main_lemma`: Keep named main theorem. One caller and short orchestration proof do not make its mathematical construction junk; actual inlining still invokes substantial project-only lemmas.

Completed `Roth.approxSet`: Not junk: stable semantic family shared by ten explicit callers. Literal inlining works but does not eliminate the mathematical need to preserve supplied denominator information.

Completed `Roth.exists_nat_mul_isIntegral`: Used in the Roth reduction, mathematically meaningful; redundant upstream wrapper, not dead code.

Completed `Roth.approxSet_den_le_finite`: Used by the reduction and reduced-approximant extraction and LeanEval equivalence; meaningful local API, not dead code or an established<=3call wrapper.

Completed `Roth.eventually_div_rpow_lt`: Used analytic helper, no deletion justified as ≤3-existing-call wrapper.

Completed `Roth.reduction`: Used once in the main theorem; meaningful source-level reduction, not dead code and not a verified <=3-mathlib-call wrapper.

Completed `Roth.exists_monic_aeval_eq_zero`: Used by one private helper and transitively by Roth/LeanEval. Not dead code; local visibility or inlining is viable.

Completed `Roth.approxSet_num_den_mem_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_reduced_approx`: Not junk: one actual recursive sequence caller, nontrivial finite-fiber arithmetic. Mere single use does not make a1–3call wrapper.

Completed `Roth.exists_m`: Used once directly and by5canonical transitive consumers; substantive proof, no dead-code/wrapper conclusion.

Completed `Roth.exists_delta`: Used theorem; sole caller can inline it but requires full proof, so not established junk or redundant.

Completed `Roth.exists_approximants`: Used theorem, complete proof can inline into sole caller but no ≤3-call mathlib replacement established. Keep project-local while assessing generic upstream selection API.

Completed `Roth.exists_degrees`: Not dead: one complete actual private caller and terminal dependency chain. No ≤3-existing-call replacement verified; retain local wrapper until upstream generic API exists.

Completed `Roth.one_le_prod_pow_mul_abs_eval`: KEEP: substantive clearing argument, used in the Roth contradiction. No dead-code or trivial existing-mathlib composition justification for deletion.

Completed `Roth.abs_prod_pow_le_rpow_of_le_weight`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.abs_eval_lt_of_le_index`: Not junk: sole direct proof caller participates in final Roth contradiction; namespace/export decision remains separate.

Completed `Roth.exists_roth_parameters_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_roth_approximants_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.one_lt_roth_eval_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.roth_product_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.roth_log_bound_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.roth_of_isIntegral`: Keep the mathematical result; one direct caller and short orchestration do not erase a named main theorem. No deletion based on generic order closure.

Completed `Roth.roth`: Keep the named BIG endpoint; four-line assembly and two callers do not reduce the theorem to existing mathlib content.

Completed `Roth.roth_rat`: No removal: zero internal consumers does not make the explicitly documented public rational endpoint dead. Avoid separate upstream PR for the five-line conversion alone.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`: Keep stable LeanEval compatibility predicate; two actual consumers.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`: Not dead: actual final caller. One caller alone does not turn its nontrivial proof into a mathlib composition.

## Part 8: Mathlibable assessment

Each non-prefiltered public declaration received the full applicable literature, generality, modern-idiom, infrastructure, five-method/form search, statement-shape, caller, composition and native verification workflow. The detailed report governs its exact evidence and caveats. BORDERLINE questions concern optional upstream API design, not incomplete verification.

| # | Declaration | Verdict | Detailed report |
|---:|---|---|---|
| 1 | `MvPolynomial.hasseCoeff` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff.md) |
| 2 | `MvPolynomial.hasseDeriv` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv.md) |
| 3 | `MvPolynomial.hasseDeriv_monomial` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial.md) |
| 4 | `MvPolynomial.hasseDeriv_apply` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_apply.md) |
| 5 | `MvPolynomial.hasseCoeff_eq_zero_iff` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_zero_iff.md) |
| 6 | `MvPolynomial.coeff_hasseDeriv` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_hasseDeriv.md) |
| 7 | `MvPolynomial.hasseCoeff_eq_prod` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_prod.md) |
| 8 | `MvPolynomial.hasseDeriv_zero_apply` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero_apply.md) |
| 9 | `MvPolynomial.hasseDeriv_zero` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero.md) |
| 10 | `MvPolynomial.hasseDeriv_C` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_C.md) |
| 11 | `MvPolynomial.hasseDeriv_map` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_map.md) |
| 12 | `MvPolynomial.hasseDeriv_rename` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_rename.md) |
| 13 | `MvPolynomial.hasseCoeff_mul_hasseCoeff` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_hasseCoeff.md) |
| 14 | `MvPolynomial.hasseDeriv_hasseDeriv` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv.md) |
| 15 | `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint.md) |
| 16 | `MvPolynomial.hasseCoeff_mul_succ` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_succ.md) |
| 17 | `MvPolynomial.pderiv_hasseDeriv` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.pderiv_hasseDeriv.md) |
| 18 | `MvPolynomial.degreeOf_hasseDeriv_le` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_hasseDeriv_le.md) |
| 19 | `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt.md) |
| 20 | `MvPolynomial.hasseDeriv_monomial_mul` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial_mul.md) |
| 21 | `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero.md) |
| 22 | `MvPolynomial.hasseDeriv_single_aeval_X` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_single_aeval_X.md) |
| 23 | `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.uniqueAlgEquiv_hasseDeriv.md) |
| 24 | `MvPolynomial.hasseCoeff_le_two_pow` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_le_two_pow.md) |
| 25 | `MvPolynomial.factorial_smul_hasseDeriv_single` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.factorial_smul_hasseDeriv_single.md) |
| 26 | `Roth.box` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.box.md) |
| 27 | `Roth.weight` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.weight.md) |
| 28 | `Roth.mem_box` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.mem_box.md) |
| 29 | `Roth.card_box` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.card_box.md) |
| 30 | `Roth.card_le_card_box` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.card_le_card_box.md) |
| 31 | `Roth.weight_nonneg` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.weight_nonneg.md) |
| 32 | `Roth.weight_zero` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.weight_zero.md) |
| 33 | `Roth.weight_add` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.weight_add.md) |
| 34 | `Roth.weight_eq_zero_iff` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_zero_iff.md) |
| 35 | `Roth.weight_single` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.weight_single.md) |
| 36 | `Roth.weight_le_card` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.weight_le_card.md) |
| 37 | `Roth.weight_mul_left` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.weight_mul_left.md) |
| 38 | `Roth.weight_le_degree_div` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.weight_le_degree_div.md) |
| 39 | `Roth.weight_mapDomain` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.weight_mapDomain.md) |
| 40 | `Roth.wronskianMatrix` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.wronskianMatrix.md) |
| 41 | `Roth.wronskian` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.wronskian.md) |
| 42 | `Roth.wronskian_eq_zero_of_not_linearIndependent` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_of_not_linearIndependent.md) |
| 43 | `Roth.det_choose_eq` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.det_choose_eq.md) |
| 44 | `Roth.coeff_prod_of_natDegree_le'` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.coeff_prod_of_natDegree_le'.md) |
| 45 | `Roth.sum_range_le_sum_of_injective` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.sum_range_le_sum_of_injective.md) |
| 46 | `Roth.coeff_wronskian_of_natDegree_injective` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.coeff_wronskian_of_natDegree_injective.md) |
| 47 | `Roth.wronskian_ne_zero_of_natDegree_injective` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_natDegree_injective.md) |
| 48 | `Roth.wronskian_update_sub_smul` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.wronskian_update_sub_smul.md) |
| 49 | `Roth.linearIndependent_update_sub_smul` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_update_sub_smul.md) |
| 50 | `Roth.sum_natDegree_update_lt` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.sum_natDegree_update_lt.md) |
| 51 | `Roth.wronskian_ne_zero_of_linearIndependent` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_linearIndependent.md) |
| 52 | `Roth.wronskian_eq_zero_iff` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_iff.md) |
| 53 | `MvPolynomial.taylor` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md) |
| 54 | `MvPolynomial.taylor_apply` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_apply.md) |
| 55 | `MvPolynomial.taylor_X` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_X.md) |
| 56 | `MvPolynomial.taylor_C` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_C.md) |
| 57 | `MvPolynomial.taylor_monomial` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_monomial.md) |
| 58 | `MvPolynomial.coeff_aeval_X_mul` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_aeval_X_mul.md) |
| 59 | `MvPolynomial.hasseCoeff_single_add_eq` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_single_add_eq.md) |
| 60 | `MvPolynomial.prod_pow_single_add_tsub` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.prod_pow_single_add_tsub.md) |
| 61 | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_single_add_aux.md) |
| 62 | `MvPolynomial.coeff_taylor_monomial_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_aux.md) |
| 63 | `MvPolynomial.coeff_taylor` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor.md) |
| 64 | `MvPolynomial.eval_taylor` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_taylor.md) |
| 65 | `MvPolynomial.taylor_taylor` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_taylor.md) |
| 66 | `MvPolynomial.taylor_zero` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_zero.md) |
| 67 | `MvPolynomial.taylor_map` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_map.md) |
| 68 | `MvPolynomial.taylor_rename` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_rename.md) |
| 69 | `MvPolynomial.degreeOf_taylor_le` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_taylor_le.md) |
| 70 | `MvPolynomial.taylor_neg_taylor` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_neg_taylor.md) |
| 71 | `MvPolynomial.taylor_injective` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_injective.md) |
| 72 | `MvPolynomial.taylor_eq_zero_iff` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_eq_zero_iff.md) |
| 73 | `MvPolynomial.eq_sum_box_hasseDeriv` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.eq_sum_box_hasseDeriv.md) |
| 74 | `MvPolynomial.eval_eq_sum_box` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_eq_sum_box.md) |
| 75 | `Roth.normOne` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.normOne.md) |
| 76 | `Roth.diag` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.diag.md) |
| 77 | `Roth.normOne_nonneg` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_nonneg.md) |
| 78 | `Roth.normOne_eq_sum_of_support_subset` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_eq_sum_of_support_subset.md) |
| 79 | `Roth.normOne_monomial` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_monomial.md) |
| 80 | `Roth.normOne_zero` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_zero.md) |
| 81 | `Roth.abs_coeff_le_normOne` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_le_normOne.md) |
| 82 | `Roth.normOne_add_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_add_le.md) |
| 83 | `Roth.normOne_neg` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_neg.md) |
| 84 | `Roth.normOne_sum_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_sum_le.md) |
| 85 | `Roth.normOne_mul_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_mul_le.md) |
| 86 | `Roth.normOne_prod_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_prod_le.md) |
| 87 | `Roth.normOne_le_card_mul` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_le_card_mul.md) |
| 88 | `Roth.normOne_det_le` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_det_le.md) |
| 89 | `Roth.abs_coeff_hasseDeriv_le` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_hasseDeriv_le.md) |
| 90 | `Roth.normOne_hasseDeriv_le` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.normOne_hasseDeriv_le.md) |
| 91 | `Roth.diag_eq_sum` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.diag_eq_sum.md) |
| 92 | `Roth.abs_coeff_diag_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_le.md) |
| 93 | `Roth.natDegree_diag_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.natDegree_diag_le.md) |
| 94 | `Roth.eval_diag` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.eval_diag.md) |
| 95 | `Roth.diag_sub` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.diag_sub.md) |
| 96 | `Roth.geom_sum_le_one_add_pow` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.geom_sum_le_one_add_pow.md) |
| 97 | `Roth.sum_box_prod_pow_le_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.sum_box_prod_pow_le_aux.md) |
| 98 | `Roth.abs_eval_le` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_le.md) |
| 99 | `Roth.degreeOf_det_hasseDeriv_le` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_det_hasseDeriv_le.md) |
| 100 | `Roth.abs_coeff_det_hasseDeriv_le` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_det_hasseDeriv_le.md) |
| 101 | `Roth.genWronskian` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.genWronskian.md) |
| 102 | `Roth.kronecker` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.kronecker.md) |
| 103 | `Roth.kroneckerExp` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp.md) |
| 104 | `Roth.kronHasse` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.kronHasse.md) |
| 105 | `Roth.kronSpan` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.kronSpan.md) |
| 106 | `Roth.genWronskian_eq_zero_of_not_linearIndependent` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.genWronskian_eq_zero_of_not_linearIndependent.md) |
| 107 | `Roth.kronecker_monomial` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.kronecker_monomial.md) |
| 108 | `Roth.kroneckerExp_injOn` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp_injOn.md) |
| 109 | `Roth.coeff_kronecker` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.coeff_kronecker.md) |
| 110 | `Roth.kronecker_eq_zero_iff` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.kronecker_eq_zero_iff.md) |
| 111 | `Roth.linearIndependent_kronecker` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_kronecker.md) |
| 112 | `Roth.derivative_aeval` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.derivative_aeval.md) |
| 113 | `Roth.derivative_kronHasse_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.derivative_kronHasse_aux.md) |
| 114 | `Roth.derivative_mem_kronSpan` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.derivative_mem_kronSpan.md) |
| 115 | `Roth.hasseDeriv_kronecker_mem` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_kronecker_mem.md) |
| 116 | `Roth.exists_hasseDeriv_kronecker_eq_sum` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_kronecker_eq_sum.md) |
| 117 | `Roth.det_sum_rows` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.det_sum_rows.md) |
| 118 | `Roth.wronskian_kronecker_eq_sum_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.wronskian_kronecker_eq_sum_aux.md) |
| 119 | `Roth.exists_genWronskian_ne_zero` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_genWronskian_ne_zero.md) |
| 120 | `Roth.sqrt_one_sub_inv_lt` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.sqrt_one_sub_inv_lt.md) |
| 121 | `Roth.inv_add_inv_le` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.inv_add_inv_le.md) |
| 122 | `Roth.sum_inv_le` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_le.md) |
| 123 | `Roth.sum_inv_lt` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_lt.md) |
| 124 | `Roth.extend_apply_castSucc` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_castSucc.md) |
| 125 | `Roth.extend_apply_last` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_last.md) |
| 126 | `Roth.card_filter_box_fiber_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_fiber_aux.md) |
| 127 | `Roth.card_filter_box_last` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_last.md) |
| 128 | `Roth.filter_weight_le_eq_empty` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.filter_weight_le_eq_empty.md) |
| 129 | `Roth.card_filter_fiber_eq` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.card_filter_fiber_eq.md) |
| 130 | `Roth.card_filter_weight_le_of_le_sqrt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_of_le_sqrt_aux.md) |
| 131 | `Roth.card_filter_weight_le_succ_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_succ_aux.md) |
| 132 | `Roth.card_filter_weight_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le.md) |
| 133 | `Roth.index` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index.md) |
| 134 | `Roth.mem_support_taylor_iff` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.mem_support_taylor_iff.md) |
| 135 | `Roth.index_le_weight` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index_le_weight.md) |
| 136 | `Roth.exists_weight_eq_index` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.exists_weight_eq_index.md) |
| 137 | `Roth.le_index_iff` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.le_index_iff.md) |
| 138 | `Roth.index_nonneg` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index_nonneg.md) |
| 139 | `Roth.index_eq_zero_iff` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index_eq_zero_iff.md) |
| 140 | `Roth.index_sub_weight_le_index_hasseDeriv` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.index_sub_weight_le_index_hasseDeriv.md) |
| 141 | `Roth.le_index_sum` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.le_index_sum.md) |
| 142 | `Roth.weight_eq_finsuppWeight_div` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_finsuppWeight_div.md) |
| 143 | `Roth.index_eq_weightedOrder_div` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.index_eq_weightedOrder_div.md) |
| 144 | `Roth.index_mul` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.index_mul.md) |
| 145 | `Roth.index_prod` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.index_prod.md) |
| 146 | `Roth.index_neg` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index_neg.md) |
| 147 | `Roth.index_C_mul` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.index_C_mul.md) |
| 148 | `Roth.index_mul_left_weights` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index_mul_left_weights.md) |
| 149 | `Roth.index_rename` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.index_rename.md) |
| 150 | `Roth.index_le_card` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.index_le_card.md) |
| 151 | `Roth.index_unique` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index_unique.md) |
| 152 | `Roth.coeffNone` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.coeffNone.md) |
| 153 | `Roth.eq_mapDomain_some_add_single` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.eq_mapDomain_some_add_single.md) |
| 154 | `Roth.coeff_X_none_pow_mul_rename` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.coeff_X_none_pow_mul_rename.md) |
| 155 | `Roth.coeff_coeffNone` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.coeff_coeffNone.md) |
| 156 | `Roth.eq_sum_X_none_pow_mul_coeffNone` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_X_none_pow_mul_coeffNone.md) |
| 157 | `Roth.degreeOf_coeffNone_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_coeffNone_le.md) |
| 158 | `Roth.coeff_rename_mul_aeval` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.coeff_rename_mul_aeval.md) |
| 159 | `Roth.aeval_X_eq_rename` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.aeval_X_eq_rename.md) |
| 160 | `Roth.hasseDeriv_rename_mul_aeval` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_rename_mul_aeval.md) |
| 161 | `Roth.coeff_uniqueAlgEquiv_symm` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.coeff_uniqueAlgEquiv_symm.md) |
| 162 | `Roth.degreeOf_uniqueAlgEquiv_symm` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_uniqueAlgEquiv_symm.md) |
| 163 | `Roth.degreeOf_rename_mul_aeval` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_rename_mul_aeval.md) |
| 164 | `Roth.degreeOf_none_rename_mul_aeval` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_none_rename_mul_aeval.md) |
| 165 | `Roth.linearIndependent_coordinate_polynomials_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_coordinate_polynomials_aux.md) |
| 166 | `Roth.eq_sum_aeval_basis_coeffNone_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_aeval_basis_coeffNone_aux.md) |
| 167 | `Roth.exists_coeffNone_basis_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_coeffNone_basis_aux.md) |
| 168 | `Roth.exists_separated_representation` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_separated_representation.md) |
| 169 | `Roth.det_hasseDeriv_separated` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.det_hasseDeriv_separated.md) |
| 170 | `Roth.exists_sum_mul_eq_gcd` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.exists_sum_mul_eq_gcd.md) |
| 171 | `Roth.exists_nat_smul_eq_map` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_nat_smul_eq_map.md) |
| 172 | `Roth.exists_primitive_smul_eq` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_primitive_smul_eq.md) |
| 173 | `Roth.exists_int_eq_of_gcd_eq_one` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_int_eq_of_gcd_eq_one.md) |
| 174 | `Roth.rescale_separated_factor_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.rescale_separated_factor_aux.md) |
| 175 | `Roth.exists_int_polynomial_of_primitive_factor_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_int_polynomial_of_primitive_factor_aux.md) |
| 176 | `Roth.exists_int_factors` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_int_factors.md) |
| 177 | `Roth.exists_rat_factors_det_hasseDeriv_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_rat_factors_det_hasseDeriv_aux.md) |
| 178 | `Roth.exists_det_eq_mul` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_det_eq_mul.md) |
| 179 | `Roth.RSet` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.RSet.md) |
| 180 | `Roth.indexSet` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.indexSet.md) |
| 181 | `Roth.Θ` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.Θ.md) |
| 182 | `Roth.lem6M` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.lem6M.md) |
| 183 | `Roth.lem6Φ` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.lem6Φ.md) |
| 184 | `Roth.one_mem_RSet` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.one_mem_RSet.md) |
| 185 | `Roth.indexSet_nonempty` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.indexSet_nonempty.md) |
| 186 | `Roth.indexSet_bddAbove` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.indexSet_bddAbove.md) |
| 187 | `Roth.index_le_Θ` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.index_le_Θ.md) |
| 188 | `Roth.Θ_nonneg` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_nonneg.md) |
| 189 | `Roth.Θ_le_card` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_card.md) |
| 190 | `Roth.Θ_le_of_forall_index_le` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_of_forall_index_le.md) |
| 191 | `Roth.Θ_mono` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_mono.md) |
| 192 | `Roth.indexSet_comp_subset` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.indexSet_comp_subset.md) |
| 193 | `Roth.Θ_equiv` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_equiv.md) |
| 194 | `Roth.isPrimitive_linear` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.isPrimitive_linear.md) |
| 195 | `Roth.isPrimitive_pow` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.isPrimitive_pow.md) |
| 196 | `Roth.exists_eq_pow_mul_of_rootMultiplicity` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_eq_pow_mul_of_rootMultiplicity.md) |
| 197 | `Roth.pow_rootMultiplicity_le` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.pow_rootMultiplicity_le.md) |
| 198 | `Roth.index_unique_le_log_div` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.index_unique_le_log_div.md) |
| 199 | `Roth.Θ_unique_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_unique_le.md) |
| 200 | `Roth.one_le_lem6M` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.one_le_lem6M.md) |
| 201 | `Roth.floor_sq_div_two_le_sum` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.floor_sq_div_two_le_sum.md) |
| 202 | `Roth.sq_div_three_lt_floor_sq_div_two` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.sq_div_three_lt_floor_sq_div_two.md) |
| 203 | `Roth.mul_div_two_le_sum_max_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.mul_div_two_le_sum_max_aux.md) |
| 204 | `Roth.mul_sq_div_three_le_sum_max_of_pos_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.mul_sq_div_three_le_sum_max_of_pos_aux.md) |
| 205 | `Roth.mul_sq_div_three_le_sum_max_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.mul_sq_div_three_le_sum_max_aux.md) |
| 206 | `Roth.min_le_sum_max` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.min_le_sum_max.md) |
| 207 | `Roth.sum_max_sub_le_index_det` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.sum_max_sub_le_index_det.md) |
| 208 | `Roth.index_separated_mul_le_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.index_separated_mul_le_aux.md) |
| 209 | `Roth.index_det_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.index_det_le.md) |
| 210 | `Roth.weight_le_delta_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.weight_le_delta_aux.md) |
| 211 | `Roth.mapped_det_ne_zero_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.mapped_det_ne_zero_aux.md) |
| 212 | `Roth.index_numeric_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.index_numeric_bound_aux.md) |
| 213 | `Roth.index_le_lem6` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.index_le_lem6.md) |
| 214 | `Roth.Θ_option_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_option_le.md) |
| 215 | `Roth.factorial_coefficient_le_two_pow_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.factorial_coefficient_le_two_pow_aux.md) |
| 216 | `Roth.two_pow_lt_rpow_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.two_pow_lt_rpow_aux.md) |
| 217 | `Roth.lem6M_lt` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.lem6M_lt.md) |
| 218 | `Roth.lem7_Φ_bound` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.lem7_Φ_bound.md) |
| 219 | `Roth.lem7_numeric` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.lem7_numeric.md) |
| 220 | `Roth.theta_scaled_unique_le_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_scaled_unique_le_aux.md) |
| 221 | `Roth.theta_delta_succ_lt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_delta_succ_lt_aux.md) |
| 222 | `Roth.theta_prefix_lt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_prefix_lt_aux.md) |
| 223 | `Roth.theta_lt_base_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_base_aux.md) |
| 224 | `Roth.theta_denominators_one_lt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_denominators_one_lt_aux.md) |
| 225 | `Roth.theta_phi_lt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_phi_lt_aux.md) |
| 226 | `Roth.theta_lt_succ_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_succ_aux.md) |
| 227 | `Roth.theta_lt_of_large_delta_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_of_large_delta_aux.md) |
| 228 | `Roth.Θ_lt` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.Θ_lt.md) |
| 229 | `Roth.lam` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.lam.md) |
| 230 | `Roth.gam` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.gam.md) |
| 231 | `Roth.eta` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.eta.md) |
| 232 | `Roth.mainCoeffBound` | NO-composable-from-mathlib | [report](.mathlib-quality/overview/mathlibable/Roth.mainCoeffBound.md) |
| 233 | `Roth.boxFamily` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.boxFamily.md) |
| 234 | `Roth.exists_delta_bound` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_delta_bound.md) |
| 235 | `Roth.eta_lt_gam_iff` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.eta_lt_gam_iff.md) |
| 236 | `Roth.sqrt_lt_nat_floor_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.sqrt_lt_nat_floor_aux.md) |
| 237 | `Roth.sqrt_lt_floor` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.sqrt_lt_floor.md) |
| 238 | `Roth.four_lt_rpow` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.four_lt_rpow.md) |
| 239 | `Roth.mul_log_div_two_lt_log_mainCoeffBound` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.mul_log_div_two_lt_log_mainCoeffBound.md) |
| 240 | `Roth.two_lt_rpow_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.two_lt_rpow_aux.md) |
| 241 | `Roth.three_small_factors` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.three_small_factors.md) |
| 242 | `Roth.exists_norm_coeff_reduction_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_norm_coeff_reduction_aux.md) |
| 243 | `Roth.norm_coeff_modByMonic_le` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.norm_coeff_modByMonic_le.md) |
| 244 | `Roth.boxFamily_eq_image_finsupp_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.boxFamily_eq_image_finsupp_aux.md) |
| 245 | `Roth.boxFamily_finite` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.boxFamily_finite.md) |
| 246 | `Roth.ncard_boxFamily` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.ncard_boxFamily.md) |
| 247 | `Roth.floor_rpow_count_lt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.floor_rpow_count_lt_aux.md) |
| 248 | `Roth.pigeonhole_count` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.pigeonhole_count.md) |
| 249 | `Roth.exists_ne_modByMonic_eq` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_ne_modByMonic_eq.md) |
| 250 | `Roth.sub_mem_RSet` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.sub_mem_RSet.md) |
| 251 | `Roth.eval_hasseDeriv_sub_eq_zero` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.eval_hasseDeriv_sub_eq_zero.md) |
| 252 | `Roth.le_index_of_forall_eval_eq_zero` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.le_index_of_forall_eval_eq_zero.md) |
| 253 | `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul.md) |
| 254 | `Roth.exists_hasseDeriv_eval_ne_zero` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_eval_ne_zero.md) |
| 255 | `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_iterated_hasseDeriv_lt_aux.md) |
| 256 | `Roth.exists_hasseDeriv_index_eval_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_index_eval_bound_aux.md) |
| 257 | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux.md) |
| 258 | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux.md) |
| 259 | `Roth.exists_mem_RSet_le_index_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_mem_RSet_le_index_aux.md) |
| 260 | `Roth.mul_card_filter_weight_le_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.mul_card_filter_weight_le_aux.md) |
| 261 | `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_mem_RSet_le_index_of_rpow_bound_aux.md) |
| 262 | `Roth.exists_mem_RSet_le_index_of_log_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_mem_RSet_le_index_of_log_bound_aux.md) |
| 263 | `Roth.exists_auxiliary_polynomial_of_log_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_auxiliary_polynomial_of_log_bound_aux.md) |
| 264 | `Roth.theta_lt_eta_of_sq_log_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.theta_lt_eta_of_sq_log_bound_aux.md) |
| 265 | `Roth.exists_auxiliary_polynomial_with_index_gap_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_auxiliary_polynomial_with_index_gap_aux.md) |
| 266 | `Roth.main_lemma` | YES-add-as-is | [report](.mathlib-quality/overview/mathlibable/Roth.main_lemma.md) |
| 267 | `Roth.approxSet` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.approxSet.md) |
| 268 | `Roth.exists_nat_mul_isIntegral` | NO-mathlib-has-it | [report](.mathlib-quality/overview/mathlibable/Roth.exists_nat_mul_isIntegral.md) |
| 269 | `Roth.approxSet_den_le_finite` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.approxSet_den_le_finite.md) |
| 270 | `Roth.eventually_div_rpow_lt` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.eventually_div_rpow_lt.md) |
| 271 | `Roth.reduction` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.reduction.md) |
| 272 | `Roth.exists_monic_aeval_eq_zero` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_monic_aeval_eq_zero.md) |
| 273 | `Roth.approxSet_num_den_mem_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.approxSet_num_den_mem_aux.md) |
| 274 | `Roth.exists_reduced_approx` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_reduced_approx.md) |
| 275 | `Roth.exists_m` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_m.md) |
| 276 | `Roth.exists_delta` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_delta.md) |
| 277 | `Roth.exists_approximants` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.exists_approximants.md) |
| 278 | `Roth.exists_degrees` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.exists_degrees.md) |
| 279 | `Roth.one_le_prod_pow_mul_abs_eval` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.one_le_prod_pow_mul_abs_eval.md) |
| 280 | `Roth.abs_prod_pow_le_rpow_of_le_weight` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.abs_prod_pow_le_rpow_of_le_weight.md) |
| 281 | `Roth.abs_eval_lt_of_le_index` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_lt_of_le_index.md) |
| 282 | `Roth.exists_roth_parameters_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_roth_parameters_aux.md) |
| 283 | `Roth.exists_roth_approximants_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.exists_roth_approximants_aux.md) |
| 284 | `Roth.one_lt_roth_eval_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.one_lt_roth_eval_bound_aux.md) |
| 285 | `Roth.roth_product_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.roth_product_bound_aux.md) |
| 286 | `Roth.roth_log_bound_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/Roth.roth_log_bound_aux.md) |
| 287 | `Roth.roth_of_isIntegral` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.roth_of_isIntegral.md) |
| 288 | `Roth.roth` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.roth.md) |
| 289 | `Roth.roth_rat` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/Roth.roth_rat.md) |
| 290 | `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine.md) |
| 291 | `LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux` | SKIP | [report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux.md) |
| 292 | `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` | BORDERLINE-needs-human | [report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff.md) |
| 293 | `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` | YES-but-generalise-first | [report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth.md) |

### Coherent contribution groups

- **Multivariate Hasse operator and core laws**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.factorial_smul_hasseDeriv_single`.
- **Translation and finite Hasse Taylor expansion**: `MvPolynomial.coeff_taylor`, `MvPolynomial.degreeOf_taylor_le`, `MvPolynomial.taylor_eq_zero_iff`, `MvPolynomial.eq_sum_box_hasseDeriv`, `MvPolynomial.eval_eq_sum_box`.
- **Binomial determinant and Hasse Wronskians**: `Roth.det_choose_eq`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.genWronskian`, `Roth.exists_genWronskian_ne_zero`.
- **Coefficient-size and evaluation bounds**: `Roth.normOne_det_le`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.normOne_hasseDeriv_le`, `Roth.geom_sum_le_one_add_pow`, `Roth.abs_eval_le`, `Roth.degreeOf_det_hasseDeriv_le`, `Roth.abs_coeff_det_hasseDeriv_le`.
- **Bounded Kronecker exponent encoding**: `Roth.kroneckerExp_injOn`.
- **Polynomial substitution chain rule**: `Roth.derivative_aeval`.
- **Weighted vanishing order comparison**: `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.index_eq_weightedOrder_div`.
- **Disjoint-variable separation and determinant factorization**: `Roth.hasseDeriv_rename_mul_aeval`, `Roth.exists_separated_representation`, `Roth.exists_det_eq_mul`.
- **Primitive representatives and integral factor descent**: `Roth.exists_primitive_smul_eq`, `Roth.exists_int_eq_of_gcd_eq_one`, `Roth.exists_int_factors`.
- **Rational-root factor and denominator multiplicity bound**: `Roth.exists_eq_pow_mul_of_rootMultiplicity`, `Roth.pow_rootMultiplicity_le`.
- **Quantitative Roth auxiliary-polynomial construction**: `Roth.main_lemma`.
- **Power asymptotics and reduced rational approximation**: `Roth.eventually_div_rpow_lt`, `Roth.exists_reduced_approx`.
- **Finite positive-weight natural rounding and strict separation**: `Roth.exists_degrees`.
- **Multivariate coordinate-denominator clearing and integer evaluation separation**: `Roth.one_le_prod_pow_mul_abs_eval`.
- **Roth exponent exclusion and Diophantine approximation endpoints**: `Roth.roth_of_isIntegral`, `Roth.roth`, `Roth.roth_rat`, `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`.

## Recommended action plan

1. Preserve current production behavior. For existing-API migrations, follow the report-specific caller and normalization plans rather than delete an entire NO bucket. Revalidate every downstream use before implementation.
2. Extract coherent Hasse/Taylor/coefficient/determinant/descent contributions in dependency order. Use each YES report’s exact target home, statement, grouping and reviewer evidence; do not infer approval for neighboring BORDERLINE wrappers.
3. Apply verified generalizations in a later implementation task with the exact original-specialization proofs retained. In particular, the selected-remainder collision theorem does not need finite support of the degree bounds; two proofs verify this. Its nonFinite finprod is a sufficient budget, not the cardinality of the infinite family. Monicity remains necessary for low-coefficient remainder reconstruction.
4. Retain the sharp B bound for subtraction of [0,B] coefficient families. Decide scalar/observation versus Hasse-specific API grain before upstreaming the local difference and root-vanishing helpers. Their broader scratch theorems are newly proved, not already existing mathlib APIs.
5. Preserve local proof boundaries and meaningful endpoint theorems even when direct internal consumer counts are zero. Private B1 status and absent direct consumers are not public novelty or external deadness judgments.

## Verification scope

The source/pin snapshot, exact293 native direct dependency graph, binder-type repairs, detailed accepted reports, all pairwise JSON/Markdown evidence and portable validation scripts are required supporting artifacts. Final completion additionally requires actual successful literal `lake build` and `lake build Roth.LeanEval` receipts; the default root does not import LeanEval. This renderer does not itself assert that those commands have run. The final readiness record and tracked final build evidence govern that gate.

### Completed: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`

Latest completed assessment:293; [detailed report](.mathlib-quality/overview/mathlibable/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth.md). All required per-declaration verification is independently accepted before publication.

Final literal build validation: **PASS** for `lake build` and **PASS** for `lake build Roth.LeanEval`. Exact command/exit/log hashes are retained in [final build verification](.mathlib-quality/overview/evidence/final/final-build-verification.json).
