# Θ_lt — original declaration 35 audit

Public audit handoff; checkpoint NOT accepted yet. Φ helper performance is OPEN: its required
repeat measured1013.946ms. The owner will audit Φ FIRST, then every other introduced helper
(including the deleted prototype), and refresh all final gates before count216/publication.
No helper/original audit credit or whole-file performance PASS is claimed here.

Scope: `Roth.Θ_lt`, substantive private estimates needed to decompose it, and the direct
`Roth.main_lemma` proof application. Public MainLemma statements and Main remain protected.
The scoped implementation and semantic gates are complete; final performance evidence is recorded below.
Publication and independent helper audits remain with the parent.

Baseline source: Theta `a98740b5b006547f5deafca6cbb12c6b4972dbfc130eae64645e67bdd9b8d800`;
MainLemma `a3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8`;
Main `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`.
The published34 doctor/fullbuild/native evidence is inherited exactly as dispatched.

The entire immutable original2b MainLemma module, including its main theorem's unchanged
proof body, was independently re-elaborated successfully in
`/private/tmp/Theta35OriginalMainLemmaCallerProbe.lean` (exit 0,
`/private/tmp/theta35-originalcaller-first.log`). Its verifier checks full effective
telescopes (ordinary names, BinderInfo, order, implicit instances and conclusion),
opaque values using `value! true`, standard axes, old-Theta dependency and absence of
Root.main_lemma self-use across all 48 copied declarations. This is whole-proof evidence.

## Initial substantive audit

| # | Item | Finding and action |
|---|---|---|
| 1 | Lint | Inherited full native diagnostics: 0 errors, 8 warnings. Final native: 0 errors, same 8 warnings; full result retained. |
| 2 | Have scan | Original proof has extensive one-use arithmetic facts; factor independent numerical, scaling, log and induction contributions, inline pure forwarding terms. Full inventory below. |
| 3 | Options | No per-declaration limits; retain default limits. |
| 4 | Simp | Preserve nonterminal squeeze; remove terminal squeeze where harmless. |
| 5 | Naming | Θ_lt describes the bound and is named in Main results; retained public name. New estimates use mathematical snake_case and `_aux`. |
| 6 | Packing | All final signature lines measured below; every changed Lean line≤100. |
| 7 | By placement | Existing `:= by` correctly ends declaration line. |
| 8 | Format | Replace lambda arrows, semicolon chains and deeply nested branches in owned proof. |
| 9 | Comments | Preserve/re-anchor all five original narrative signposts. |
| 10 | Documentation | Preserve source attribution; describe any compiled wider input range accurately. |
| 11 | Visibility | MainLemma consumes Θ_lt; keep public. New local estimates private. |
| 12 | Structure | Original headline exceeds 200 lines; extract mathematical contributions to ≤30, every branch≤10, headline≤15. |
| 13 | Mathlib | Five searches actually executed; details below. No replacement identified by these searches; no absolute absence claim. |
| 14 | Junk definitions | Not a definition; introduce no extra definition. |
| 15 | Existentials | No trivial existential wrapper needed. |
| 16 | Show/change | No new redundant show; keep cross-type casts explicit where required. |
| 17 | Negation | Existing `push Not` is canonical; avoid contradiction proof if positivity follows directly. |
| 18 | Generalise | Compile endpoint δ≤1/(n+1), lastweight≥3, multiplicative weak ratios, weak log bound; test derived hr0/hq0 and every retained effective binder before recommendation. |
| 19 | Inequalities | Original owned statement uses ≤/<; preserve orientation and emit occurrence inventory. |
| 20 | Normal form | Multiplicative growth avoids division and composes with scaled induction. |
| 21 | Syntax generality | Preserve natural weights/denominators, Fin dimension and real analytic conclusion; no arbitrary-domain change. |
| 22 | Fanout | No new imports. Sole external code caller is MainLemma.lean:670; Theta.lean:33 is documentation. Main.lean contains no direct use. |
| 23 | Casts | Natural-to-real casts are required throughout; normalize once in each independent estimate. |
| 24 | Instance names | Existing singleton instance anonymous; no named/global instance introduced. |

## Mathlib and literature search (construction stage)

All five methods were executed through native tools or exact source search:

- Lean-Finder: “Roth polynomial index theta growth bound induction lemma seven”, 3 results,
  returned additive-combinatorial Roth-number lemmas, not this polynomial-index estimate.
- Loogle: `Antitone, Fin`, 6 results; `Fin.antitone_iff_succ_le` is directly applicable.
- LeanSearch: “antitone finite sequence from adjacent inequalities”, 5 results; same finite
  adjacent-antitone API, to be used directly.
- Source search: finite antitone, real log/rpow and sup inequalities in Mathlib;
  construction uses existing public analytic/order lemmas directly.
- Local search `antitone_iff_succ`, limit 5: found exact Fin lemma, index unavailable;
  positive source hit is useful, empty results would not certify absence.

Web queries for the named polynomial-index Lemma 7 and Roth's original rational-approximation
formulation were executed. The immutable local `clean.tex`:935–1036 states the original
strict assumptions and gives the complete induction. Its paragraph before the base case
explicitly derives all q_j>1 from the balanced logarithms. Public search found the original
Roth abstract/formulation and Princeton's chapter on polynomial index:
[Roth’s original paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf)
and [the Princeton notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf). These establish context,
not Lean endpoint claims; wider endpoints must be supported by compiled proofs.

A further explicit search, “Roth polynomial index Lemma 7 weak growth delta logarithm bound
generalization”, returned the classical formulation, several different Roth lemmas and subspace
theorem generalisations. It did not supply a primary source for these exact endpoint changes;
the compiled stronger theorem is the evidence for them, with no literature priority claim.

Inversion diagnostic: the proof continues to use Θ through the one-variable estimate,
monotonicity, finite reindexing and lower-dimensional induction; the named object does not
disappear after one unfolding. Extract the independent scalar/scaling estimates, rather
than replace the public polynomial theorem with an abstract unrelated statement.

## Original have inventory
| Source line | Have | Pure reference count in declaration |
|---|---|---|
| 747 | `have hL : 0 < Real.log (q 0) := lt_trans (by positivity) hq1` | 3 |
| 748 | `have hq : 1 < q 0 := by` | 11 |
| 750 | `have hB : (1 : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) :=` | 6 |
| 752 | `have h := Θ_unique_le (q := q) (r := r) hB (by convert hq; exact Subsingleton.elim _ _) (hr0 _)` | 6 |
| 753 | `have hr : (0 : ℝ) < r 0 := by exact_mod_cast hr0 0` | 14 |
| 754 | `have key : ∀ x y : Fin (0 + 1), Θ ((q 0 : ℝ) ^ (δ * r 0)) q r ≤` | 1 |
| 758 | `have hδeq : δ * r 0 * Real.log (q 0) / (r 0 * Real.log (q 0)) = δ := by` | 1 |
| 762 | `have hδ1 : δ < 1 := by simpa using hδ` | 7 |
| 763 | `have h1 : δ ≤ δ ^ ((1 / 2 : ℝ) ^ (0 + 1)) := by` | 7 |
| 766 | `have h2 : 0 < δ ^ ((1 / 2 : ℝ) ^ (0 + 1)) := Real.rpow_pos_of_pos hδ0 _` | 5 |
| 767 | `have h3 : (10 : ℝ) ^ (0 + 1) = 10 := by norm_num` | 3 |
| 771 | `have hL : 0 < Real.log (q 0) := lt_trans (by positivity) hq1` | 1 |
| 772 | `have hq0' : 1 < q 0 := by` | 2 |
| 775 | `have hB : 1 ≤ B := Real.one_le_rpow (by exact_mod_cast hq0'.le) (by positivity)` | 4 |
| 776 | `have hn2 : (0 : ℝ) < (n : ℝ) + 1 + 1 := by positivity` | 0 |
| 778 | `have hu0 : 0 < u := by positivity` | 0 |
| 779 | `have huP : u * ((n : ℝ) + 1 + 1) = 1 := by rw [hu]; field_simp` | 0 |
| 780 | `have hδu : δ < u := by` | 1 |
| 784 | `have hδ1 : δ < 1 := by nlinarith` | 5 |
| 786 | `have hanti : Antitone r := Fin.antitone_iff_succ_le.2 fun i => by` | 3 |
| 787 | `have h1 := hratio i` | 6 |
| 788 | `have h2 : (r i.succ : ℝ) ≤ r i.succ / δ := le_div_self (Nat.cast_nonneg _) hδ0 hδ1.le` | 4 |
| 790 | `have hr₁ : ∀ j, r j ≤ r 0 := fun j => hanti (Fin.zero_le j)` | 1 |
| 791 | `have hratio' : ∀ j : Fin (n + 1), (r (Fin.last (n + 1)) : ℝ) < δ * r (Fin.castSucc j) :=` | 2 |
| 793 | `have h1 := hratio (Fin.last n)` | 4 |
| 795 | `have h2 : (r (Fin.castSucc (Fin.last n)) : ℝ) ≤ r (Fin.castSucc j) := by` | 2 |
| 798 | `have hlast_lt0 : r (Fin.last (n + 1)) < r 0 := by` | 0 |
| 799 | `have h := hratio' 0` | 3 |
| 800 | `have hr0' : (0 : ℝ) < r 0 := by exact_mod_cast hr0 0` | 0 |
| 810 | `have hq'n : q' none = q (Fin.last (n + 1)) := by simp [hq', he]` | 1 |
| 811 | `have hr'n : r' none = r (Fin.last (n + 1)) := by simp [hr', he]` | 4 |
| 812 | `have hq's : ∀ j, q' (some j) = q (Fin.castSucc j) := fun j => by` | 1 |
| 814 | `have hr's : ∀ j, r' (some j) = r (Fin.castSucc j) := fun j => by` | 2 |
| 816 | `have hr'0 : ∀ j, 0 < r' j := fun j => hr0 _` | 0 |
| 817 | `have hr'1 : ∀ j, r' j ≤ r 0 := fun j => hr₁ _` | 1 |
| 818 | `have hq'0 : ∀ j, 0 < q' j := fun j => hq0 _` | 1 |
| 820 | `have hle := Θ_option_le (τ := Fin (n + 1)) hδ0.le hδ1.le (r := r')` | 1 |
| 837 | `have hl'' : l ≤ r 0 := by omega` | 1 |
| 841 | `have hδδ₁ : δ ≤ δ₁ := le_mul_of_one_le_right hδ0.le (le_add_of_nonneg_right (by positivity))` | 3 |
| 842 | `have hδ₁0 : 0 < δ₁ := by positivity` | 1 |
| 843 | `have hMlt : M < (q 0 : ℝ) ^ (δ₁ * (l * r 0)) :=` | 2 |
| 848 | `have hM1 : 1 ≤ M := one_le_lem6M _ _ hB l` | 2 |
| 850 | `have hC1 : 1 ≤ C := Real.one_le_rpow (by exact_mod_cast hq0'.le) (by positivity)` | 1 |
| 851 | `have hlR : (0 : ℝ) < l := by exact_mod_cast hl1` | 1 |
| 853 | `have hΘ1 : Θ M (fun _ : Unit => q' none) (fun _ => l * r' none) ≤ δ₁ := by` | 0 |
| 855 | `have hqr' := hqr (Fin.last (n + 1))` | 1 |
| 856 | `have hrl : (0 : ℝ) < r (Fin.last (n + 1)) := by exact_mod_cast hr0 _` | 0 |
| 857 | `have hr0R : (0 : ℝ) < r 0 := by exact_mod_cast hr0 0` | 0 |
| 858 | `have hLl : 0 < Real.log (q (Fin.last (n + 1))) := by` | 1 |
| 862 | `have hql : 1 < q (Fin.last (n + 1)) := by` | 1 |
| 876 | `have hΘ2 : Θ M (q' ∘ some) (fun j => l * r' (some j)) <` | 0 |
| 878 | `have hfq : q' ∘ some = fun j => q (Fin.castSucc j) := funext hq's` | 1 |
| 879 | `have hfr : (fun j => l * r' (some j)) = fun j => l * r (Fin.castSucc j) :=` | 1 |
| 883 | `have hCeq : C = ((q (Fin.castSucc 0) : ℕ) : ℝ) ^` | 1 |
| 888 | `have hA : δ₁ < 1 / ((n : ℝ) + 1) := by` | 1 |
| 889 | `have hδ₁u : δ₁ = δ * (1 + u) := by rw [hδ₁, hu]; push_cast; ring` | 1 |
| 891 | `have h1 : u * ((n : ℝ) + 1) = 1 - u := by linarith` | 2 |
| 892 | `have h2 : u * (1 + u) * ((n : ℝ) + 1) = 1 - u ^ 2 := by` | 1 |
| 895 | `have h3 := mul_lt_mul_of_pos_right hδu (by positivity : (0 : ℝ) < (1 + u) * (n + 1))` | 1 |
| 897 | `have hB' : 10 / δ₁ < ((l * r (Fin.castSucc (Fin.last n)) : ℕ) : ℝ) := by` | 1 |
| 898 | `have h1 : 10 / δ₁ ≤ 10 / δ := div_le_div_of_nonneg_left (by norm_num) hδ0 hδδ₁` | 0 |
| 899 | `have h2 : (r (Fin.last (n + 1)) : ℝ) ≤ r (Fin.castSucc (Fin.last n)) := by` | 0 |
| 901 | `have h3 : (r (Fin.castSucc (Fin.last n)) : ℝ) ≤ l * r (Fin.castSucc (Fin.last n)) :=` | 0 |
| 905 | `have hC' : ∀ i : Fin n, ((l * r (Fin.castSucc i.succ) : ℕ) : ℝ) / δ₁ <` | 1 |
| 908 | `have h : (r (Fin.castSucc i.succ) : ℝ) / δ < r (Fin.castSucc (Fin.castSucc i)) :=` | 1 |
| 915 | `have hD' : ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ₁ <` | 1 |
| 925 | `have hE' : ∀ j : Fin (n + 1), ((l * r (Fin.castSucc 0) : ℕ) : ℝ) *` | 1 |
| 936 | `have hb := lem7_Φ_bound (p := n + 1 + 1) (by omega) hδ0 hδ1.le` | 1 |
| 938 | `have hΦlt : lem6Φ q' r' M l <` | 1 |
| 943 | `have hfin := lem7_numeric (p := n + 1 + 1) (by omega) hδ0 hδ1.le hΦlt.le` | 0 |


## Compiled generalisation results and application

The full original-growth relaxation is clean in `candidate-fourth.log`/`.json` (exit0).
The full factored candidate with hr0/hq0 removed is clean in `helpers-fifth.log`/`.json`.
`helpers-large-third.log`/`.json` proves the additional removal of the δ upper bound:
for δ≥1/p, δ^(2^-p)≥1/p and p²<10^p, while Θ≤p. The final public proof handles
both ranges directly in its induction; no same-statement private theorem hides the induction.

`positive-final-candidate.log`/`.json` is exit0 (52.007s): ENTIRE independently elaborated
candidate MainLemma proof, full original/candidate MainLemma telescope comparison, 48 copied
proof values/standard axes/no imported main_lemma self-use, candidate Θ proof dependency,
all candidate private values/axes/no imported old Θ self-use, exact original full Θ adapter
(telescope, ordinary names, BinderInfo, types, order, conclusion), and opaque values pass.
A positive δ=0 counterexample shows that weakening strict positivity to nonnegativity is false;
all other growth conditions hold there. Its only axioms are the standard three.

The source and minimal caller proof patch were applied under standing user authority after
these complete candidate/adapter/caller gates. MainLemma's public contract is unchanged.
The preceding Theta source prefix through original34 is byte-identical to published34.

| Effective original binder | Compiled probe / result | Final action |
|---|---|---|
| n : ℕ | Positive Meta telescope probe finds n in actual conclusion | Retain dimension and Fin domain |
| δ : ℝ | Positive Meta probe finds δ in conclusion | Retain real parameter; real log/rpow are load bearing |
| hδ0 : 0<δ | Full positive proof; nonnegative δ=0 counterexample clean | Retain strict positivity |
| hδ upper bound | Closed endpoint candidate; then complete large-δ extension clean | Remove upper bound |
| r | Positive Meta probe finds array in conclusion | Retain Nat weights |
| q | Positive Meta probe finds array in conclusion | Retain Nat denominators |
| hr0 | Full factored candidate derives all weights using antitonicity and last≥3 | Remove derived hypothesis |
| hrlast | Full candidate weakens 10/δ<last to 3≤last | Apply weaker condition |
| hratio | Full candidate replaces strict division with weak multiplication | Apply weak multiplicative condition |
| hq0 | Full candidate derives q_j>1 from positive weighted log and balance | Remove derived hypothesis |
| hq1 | Full candidate uses weak log lower bound | Apply endpoint |
| hqr | Full candidate retains balance for all j | Retain |

`BinderNegative.lean`/`binder-negative-first.log` is a separate expected-failure batch,
exit1 (34.052s), anonymous exact? probes before the audited theorem: dropping hδ0, weakening it
to nonnegative, dropping/weakening lastweight to nonnegative, dropping ratios, dropping log bound,
and dropping balance all failed to close the goal. These are bounded proof-search failures,
not necessity or absence proofs. The positive δ=0 counterexample is separate evidence for
hδ0. Structural binder probes are positive compiled dependency checks, not invalid undeclared
identifier tests. No universe or section-instance generalisation is available in this concrete
Fin/Nat/Real signature; the full effective telescope is checked, not inferred from header text.

`Automation.lean`/`automation-first.log`, exit1 (31.414s), uses the EXACT production prefix
before original Θ_lt, so no imported/self Θ_lt can pollute suggestions. Anonymous probes tried
rfl, simp, ring, linarith, nlinarith, lia, exact?, apply?, grind, aesop, simp_all at scratch-only
5000 heartbeats. None closed the whole theorem; apply? produced incomplete structural options
and reached the conservative budget. Named negative trials were not available to searches.
Known native multi_attempt stalls were not repeated; ordinary isolated compiler fallbacks were
bounded and fully drained. No production limit or pin changed.

## All 42 golfing rules

| Rule | Actual status |
|---|---|
| 1.1 by-exact | Pure forwarding estimates use terms; public successor is exact application. |
| 1.2 by-rfl | n/a: no standalone by-rfl proof introduced. |
| 1.3 rw+exact | Finite reindexing uses direct Θ_equiv/Θ_option_le; logarithmic cancellation uses direct rw/field_simp. |
| 1.4 simp+exact | Applied to scalar/card/finite reindex conversions with simpa using. |
| 1.5 simp+rfl | n/a: no redundant trailing rfl after simp. |
| 1.6 constructors | n/a: conclusion is one strict bound, no conjunction constructor. |
| 1.7 apply+exact | Successor application uses exact; base apply retains genuine arithmetic conversion. |
| 1.8 contradiction | Removed the old q_last-log contradiction; positive-product reflection gives log positivity directly. |
| 1.9 eta | Derived denominator bound is partially applied once; no needless forwarding lambda. |
| 1.10 have scan | Pure single-use final assembly forwarded; retain reused M/ε/bounds and typed arithmetic proof blocks. |
| 1.11 apply+intro | sup'_lt_iff concludes with an exact pointwise lambda. |
| 1.12 show | n/a: no redundant show in final proof. |
| 1.13 obtain | Icc membership destructed with obtain ⟨hl1,hl2⟩. |
| 1.14 merged rw | Log/div rewrites combined; no successive rw chain remains in owned proof. |
| 1.15 terminal simp | Terminal conversions use simpa; no squeezed terminal simp introduced. |
| 1.16 nonterminal simp | hb normalisation uses explicit simp only [Nat.add_sub_cancel,Nat.cast_add,Nat.cast_one]. |
| 1.17 dot notation | Bounds use .trans/.trans_lt/.trans_eq and .le. |
| 1.18 parentheses | Keep necessary tactic-proof/positivity arguments and explicit typed bounds; no marginal syntax churn. |
| 1.19 push_neg | n/a: old push Not contradiction removed, no deprecated syntax. |
| 1.20 trivial ∃ | n/a: no existential helper or extra definition introduced. |
| 2.1 grind whole | Actually failed against exact pre-target source at 5000 scratch heartbeats. |
| 2.2 pre-grind deletion | n/a: no selected grind sequence. |
| 2.3 simpa consolidation | Applied in finite-option transport, cast bridge, cardinality, and singleton bound. |
| 2.4 fun_prop | n/a: no continuity/measurability/differentiability goals. |
| 2.5 positivity | Used for all local nonnegative bases/exponents/divisors and numerical multipliers. |
| 2.6 gcongr | Actual selected proof closes power-base monotonicity 4^p≤10^p; exact product lemmas pin scaled inequalities. |
| 2.7 lia | Initial integer l≤r0/dimension searches were replaced by direct Nat facts after measured hotspots; whole-goal trial failed. |
| 2.8 aesop | Whole-goal anonymous trial failed; no broad search retained. |
| 2.9 norm_num/cast | Used for endpoints/singleton and cross-type Nat→Real estimates. |
| 2.10 decide | n/a: analytic inequality is not finite computation; no native_decide. |
| 2.11 field_simp/ring | Singleton logarithmic cancellation uses field_simp; reciprocal cancellation now one_div_mul_cancel; ring for scalar commutations. |
| 2.12 linear_combination | LocalPositive.lean tests u/scaled-product/inverse identities; final reciprocal h1 uses linear_combination, avoiding linear search. |
| 2.13 wlog | n/a: induction dimensions and parameter ranges are not symmetric cases. |
| 2.14 calc terms | Two-step analytic monotonicity is .trans; retain the substantive cardinality chain. |
| 2.15 <;> | Tried singleton convert/norm_num. Fresh module build flagged unnecessarySeqFocus; replaced by three direct lines before final source gates. |
| 3.1 erw | n/a: none. |
| 3.2 legacy function tactics | n/a: no continuity/measurability tactic. |
| 3.3 omega | New integer goals use lia; no omega introduced. |
| 3.4 rcases rfl | n/a: no such substitution pattern. |
| 3.5 attributes | n/a: private proof-stage estimates need no global automation attribute. |
| 3.6 simp_all | Whole original goal actually failed; no simp_all only remains. |
| 3.7 options | No production limits/profiler/scaffolding introduced. |

`local-positive.log`/`.json`, exit0 (26.595s), verifies the linear_combination alternatives
and the direct mul_self_lt_mul_self route for the strict square bound. It also resolves every
new external identifier by getConstInfo: pos_of_mul_pos_right, Real.log_pos,
Fin.castSucc_zero, pow_le_one₀, Real.rpow_le_rpow, div_le_one, Nat.lt_two_pow_self,
mul_lt_of_lt_one_left, mul_le_of_le_one_left, mul_self_lt_mul_self. Other referenced names
already occur in the protected preceding source or original proof and are checked by the
actual module builds. No unresolved guessed identifier remains.

## Structure, packing, comments and scope

`final-source-inventory-sixth.json` contains actual source lines, all proof/branch counts and widths.
Θ_lt has 13 nonblank/noncomment proof lines; its largest induction branch has 6.
Private estimates have 15,16,8,30,15,8,7,30,26,30 proof lines, in source order;
the longest explicit branch is the 10-line scaled-ratio argument. Every changed Lean line≤100.
No conjunction packaging or same-statement private wrapper hides the headline proof.

The five original narrative comments are all re-anchored: antitone weights, Option transport,
one-variable term, lower-dimensional induction, and combination. The original source attribution
is retained; the docstring accurately states the wider weak bounds and no δ upper restriction.
No other public statement/definition/import/header or earlier proof changed. The MainLemma change
is a single proof application hunk (six lines replacing two); Main.lean is byte-identical to original2b.
The Theta file grows from948 to1031 lines. The final independent reviewer will assess its
thematic structure; it remains below the1500-line split threshold, so no file split is prescribed.
This scoped leaf does not move declarations or imports.

Actual new Root Θ_lt has exactly 9 effective binders, including no hidden σ/section instance or
extra universe parameter; `actual-semantics-final.log`/`.json` verifies every ordinary name,
BinderInfo, type, order, universe arity and result against the reviewed candidate telescope.
The exact old full telescope adapter and source fragment for the owner's all29 generator is
`/private/tmp/theta35-audit/owner-bridge.lean.txt`.

| Signature line | Codepoints | Next complete atomic signature item | Arithmetic | Action |
|---|---:|---|---|---|
| 1010 | 66 | hrlast binder (35) | 66+1+35=102>100 | ok |
| 1011 | 97 | hq1 binder (68) | 97+1+68=166>100 | ok |
| 1012 | 72 | hqr binder (62) | 72+1+62=135>100 | ok |
| 1013 | 68 | conclusion through := by (80) | 68+1+80=149>100 | ok |
| 1014 | 84 | no next signature line | n/a | ok |

The actual width100 #check is in `actual-semantics-final.log` (a compiled telescope, not header text).

| Inequality occurrence scan | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| n/a | all signature hypotheses and conclusion | zero ≥/> in Lean code | none | no _ge_/_gt_ name |

## Fresh original35 ownership boundaries

Ten retained private estimates and one introduced-then-deleted prototype have immutable FIRST CLEAN
compiled contexts, before later golf:
`first-clean-helpers-batch1.lean/.json` (first three), `batch2` (next seven), `batch3` (large-δ bound),
with exact whole-context hashes and their successful raw logs. All final private contracts/value/axes
are additional artifacts; these construction checks are NOT separate fresh helper audits and do NOT
increment the project's cleanup count. Parent must dispatch one later fresh dedicated audit per
introduced helper (including a deletion/replacement audit for the prototype) and refresh
public35/caller gates after any helper edit.

The mandatory known index29/numeric timing repair queue (1068.193/1115.157ms repeats) is still
explicitly pending with the file owner. No whole-Theta/all-project performance PASS is claimed
from this target cleanup. Full lake build THEN separate Roth.LeanEval, independent file-wide
simplification, cumulative all29 and all private audits, staging/commit/push are parent-only gates.


## Final semantic, native and diff gates

Final Theta SHA256: `0cb111c95cb755ec1e80a5a39ac4c1a35ad0460dfd3c75988be0fd89e4ed7118`.
Final MainLemma SHA256: `ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4`.
Main remains original2b SHA `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`.
All paths below are relative to `/private/tmp/theta35-audit/` unless absolute.

| Final frozen-source gate | Evidence | Result |
|---|---|---|
| Theta module build | final-theta-build-eighth.log/json | exit0, 35.333s |
| Then MainLemma module build | final-mainlemma-build-fourth.log/json | exit0, 45.327s |
| Independent entire original caller and actual updated Root checks | ActualSemanticsFinal.lean; actual-semantics-final.log/json | exit0, 151.396s |
| Literal new effective public contract | ActualNewContract.lean appended verbatim after import to ActualSemanticsFinal.lean; actual-semantics-final.log/json | same combined exit0, all9 binders |
| Complete unfiltered Theta native | final-native-theta-final.json | success=true, partial=false, timed_out=false; 0errors,8 existing warnings |
| Complete unfiltered MainLemma native | final-native-mainlemma-final.json | success=true, partial=false, timed_out=false; 0errors,3 existing warnings |

The MainLemma warnings are the existing header and unused `hδ0`/`hr₁` at149. Theta has its
existing header and earlier retained unused arguments; the hr warnings at93/252 reflect prior
owner scope choices, not explicit user vetoes. The precise user hq/globalΘ hB/hr choices remain
recorded in the shared contract ledger. No new warning was hidden or suppressed.
The final semantic log prints all ten actual private contracts, binder metadata, opaque proof
values and standard axes, compares the full original/current main_lemma effective telescope,
and positively finds current main_lemma's new Θ_lt dependency. It also finds no actual deleted
prototype and verifies the successor's direct Θ_option_le and Θ_equiv dependencies. The original
prepared scaffold's historical UNCOMPILED preparation record is preserved; its later successful
compilation is recorded separately in `original-caller-success-appendix.json`.

Final step-back/simplify review found the seven-line finite-option transport prototype was
convenience packaging. A positive complete candidate compiled (`inline-candidate.log/json`,
exit0,35.192s), then its proof was inlined into the substantive successor estimate. The FIRST
clean prototype remains immutable in batch1 and needs a later fresh deletion/replacement audit.
The final retained helper count is TEN. No callable Skill/simplify/buzz capability was exposed
in the tool inventory; this was a manual full scoped workflow review, not a claim that such a
built-in command was invoked. Parent's independent whole-file simplify remains pending.

| Diff gate | Status |
|---|---|
| definition_protected | pass: no public definition changed |
| theorem_statement_protected | pass under standing authorization: supported stronger Θ_lt, same conclusion; exact old adapter and entire old/new caller proofs compiled |
| effective_type/value/standard_axes | pass: independent original and actual updated declarations checked |
| naming/visibility | pass: public name retained; substantive estimates private with `_aux` |
| structure | pass: headline13; ten private bodies≤30; all branches≤10 |
| line_packing/inequality_orientation | pass: measured tables above; changed source lines≤100 |
| comments/imports/header/limits/pins | pass: five comments reanchored; no imports/header/limits/pins changed |
| earlier independent Index/Theta proofs | pass: immutable block hashes72cf/355a retained in final successful semantic source |
| source scope | pass: preceding published34 Theta bytes unchanged; one minimal caller proof hunk; Main unchanged |
| owner publication/fullbuild/LeanEval/helper audits | delegated pending, no leaf completion claim |

Phase checklist:

- [✓] Step1: required skills/workflow/reference docs read.
- [✓] Step2: all24 substantive audit items recorded.
- [✓] Step2.5: five actual mathlib search methods recorded.
- [✓] Step2.6: every effective binder considered; clean positive and separate expected-failure probes.
- [✓] Step2.7: measured final line-packing table.
- [✓] Step2.8: final inequality occurrence scan.
- [✓] Step3: all42 golfing-rule statuses recorded.
- [✓] Step4: reflection and scoped simplification completed, unnecessary wrapper deleted.
- [✓] Step5a: both complete unfiltered final native diagnostics clean of errors.
- [✓] Step5b executed: diff/semantic/module gates recorded; Φ performance OPEN, transferred to owner’s first fresh helper audit.
- [✓] Step6a: no rename, no rename sidecar write required; parent owns shared logs/Git.


### First complete timing sweep and measured repair

The first frozen source `e162d02d...` completed the exact whole-module real profiler command
in286.779s (`final-theta-profile.log/json`), preserving253116912 raw bytes, strict UTF8.
`final-theta-profile-table.json` matches all52/52 source declarations with one actual proof
anchor per owned target and exact source hash. Public Θ_lt259.113ms; retained helpers in order:
546.680,721.040,305.352,550.476,678.096,309.958,227.644,1400.627,768.089,859.248ms.
The Φ helper failed1000ms; successor and large-δ estimates require a same-final-source repeat.
This sweep is historical diagnostic evidence, not the final performance pass.

Its strict raw nested rows identify the `lia` inside `have hlr` at691.625ms. Replace that
search with `hl2.trans (Nat.succ_le_of_lt (theta_last_lt_first_aux ...))`, a direct proof of
the same natural inequality. This removes one proof line and changes no statement or helper
set. First-clean helper contexts remain untouched. The new Theta SHA is `eebe533337182ad0e40f1ff026cf0a4559f2bc961f88eebb5fcd1ef522ec47d1`;
all final source gates are refreshed after this repair, with their current evidence below.


Fresh baseline profile limitations (before changing Θ_lt): exact whole-Theta trace bounded at
180.012s and original MainLemma trace at180.018s; neither reached a finite audited-target
measurement. No explicit Lean error was observed, so these timeouts do not establish a default
heartbeat failure. Raw logs `baseline-theta-profile.log` (168267849 bytes) and
`baseline-caller-profile.log` (138502239 bytes) remain byte-for-byte. The former ends with one
incomplete UTF8 byte CE at byte168267848; exact encoding record is
`baseline-theta-profile.log.utf8.json`, with labeled escaped tail view beside it. The caller raw
is strict UTF8. The first baseline runner lacked group management; subsequent process inspection
found no orphan of that request. All later compiler/profile runs use the bounded process-group
runner, terminate/kill as needed and drain. These limitations are distinct from the successful
final ordinary builds and complete independent caller proofs.


### Second sweep diagnosis and direct-lemma repairs

`final-theta-profile-second.log/json` completed the actual whole module in291.460s on
`eebe5333...`; all52 source declarations and all owned proof anchors matched, strict UTF8.
Public272.883ms; Φ1627.436ms and large-δ1072.364ms still failed. The raw Φ rows identify
the next large cost as hM's trivial dimension `lia` at753.322ms. No failed measurement is
excluded or relabeled as a pass. Replace all three trivial Φ dimension searches by direct
Nat positivity/order terms, and both large-δ square/division nonlinear searches by
`mul_self_lt_mul_self` and `pow_two` normalization. The shortened power identity is
`norm_num [sq, ← mul_pow]`. These are substantive measured repairs, no extra helper.
The first trial misapplied the2≤p argument to lem6M_lt, which needs0<p; the build caught it
(`final-theta-build-fifth.log`, exit1). The corrected next build passed. Failed logs certify
no positive gate.

`OwnedDiagnostic.lean` copies exactly the owned declarations into a fresh namespace after
importing the rebuilt Theta, for diagnostic timing only. Its clean trace105.595s matched
all11 declarations:677.343,884.648,377.999,484.981,734.765,213.539,162.623,872.042,
674.978,737.916,257.976ms in source order. This is not actual-module final timing acceptance.
To add margin, replace the reciprocal helper's field_simp/nonlinear conclusion by
one_div_mul_cancel, a polynomial identity and a direct order calc; replace Φ's last linear
search by the exact lt_div_iff₀' application of lem7_numeric. The set equation is unused after
this change and is removed. The transient seventh build straddled this last removal, so only
the subsequent exact-source eighth build is used as evidence (exit0,35.333s). First-clean
contexts remain immutable; no new helper or conclusion change occurred during performance repair.


Second diagnostic `OwnedDiagnosticSecond.lean` / `owned-diagnostic-profile-second.log/json`
compiled exit0 in97.916s. A strict decoder correctly rejected its full Φ slice: the raw fragment has CE, then an ASCII interpretation-timing message, then B3 at raw
offsets27881487 and27881565. The writer cause is unknown; the fragment is consistent with
interleaving within the encoding of γ.
The raw55015924-byte log remains unchanged, SHA29339ca34834710274d6581789e924e419d37607e67c1858d0f066d4449e6e7c.
Exact offsets/hex/context are in the `.log.utf8.json` sidecar; `.log.invalid-escaped.txt` is an
explicitly labeled escaped view. No replacement characters were inserted. The diagnostic-only
bytewise table matches ASCII timing headers and strictly decodes EACH retained timing row;
it flags Φ's full slice as non-UTF8 rather than falsely declaring that slice strict.
Its eleven values are660.753,577.599,361.171,461.312,716.031,229.240,171.431,736.664,
639.747,767.987,249.284ms. This supports the direct repairs, but remains diagnostic evidence;
final acceptance still requires the actual module after complete final source gates.

Current retained helper inventory (all first-clean contexts immutable):

| Helper | Body lines | FIRST CLEAN batch |
|---|---:|---:|
| `theta_scaled_unique_le_aux` | 15 | 1 |
| `theta_delta_succ_lt_aux` | 16 | 1 |
| `theta_prefix_log_le_aux` | 8 | 2 |
| `theta_prefix_lt_aux` | 30 | 2 |
| `theta_lt_base_aux` | 15 | 2 |
| `theta_denominators_one_lt_aux` | 8 | 2 |
| `theta_last_lt_first_aux` | 7 | 2 |
| `theta_phi_lt_aux` | 30 | 2 |
| `theta_lt_succ_aux` | 26 | 2 |
| `theta_lt_of_large_delta_aux` | 30 | 3 |

Introduced-then-deleted `theta_fin_option_le_aux`: batch1, seven-line first proof; final actual
absence and successor replacement checked. It receives no retained-helper/original count credit.

The final combined semantic run has67 PASS markers, no PANIC/error/sorryAx, and includes the
reviewed literal public contract verifier verbatim after its import. Its complete independent
original blocks preserve hashes72cf/355a; repair identifiers are explicitly resolved.


### Actual frozen-candidate sweeps — Φ repeat failed, acceptance OPEN

After the final semantic/native gates drained, the exact whole-module command on final
`0cb111c9...` completed exit0 in274.451s (`final-theta-profile-third.log/json`). The raw
242655141-byte log is strict UTF8 with zero invalid sequences/replacement sequences. The tested
LAST-command parser matches all52/52 source declarations against `final-Theta-source-sixth.lean`,
whose hash equals the current source, and finds exactly one actual proof anchor for each owned
target. Conservative totals include outer command plus disjoint async proof/addDecl/linters;
nested kernel rows are retained separately and not double counted. Every owned target is below
1000ms. Base/Φ/successor/large-δ are≥750ms, so an identical-source actual whole-module repeat is
mandatory; the completed repeat below FAILED Φ, so this candidate has no all-target
performance acceptance.

| Owned declaration | First actual final-source sweep ms |
|---|---:|
| theta_scaled_unique_le_aux | 719.946 |
| theta_delta_succ_lt_aux | 602.125 |
| theta_prefix_log_le_aux | 480.125 |
| theta_prefix_lt_aux | 732.389 |
| theta_lt_base_aux | 816.370 |
| theta_denominators_one_lt_aux | 362.355 |
| theta_last_lt_first_aux | 262.975 |
| theta_phi_lt_aux | 988.865 |
| theta_lt_succ_aux | 850.193 |
| theta_lt_of_large_delta_aux | 884.487 |
| Θ_lt | 320.673 |


The REQUIRED identical-source whole-module repeat completed exit0 in272.970s
(`final-theta-profile-fourth.log/json`, `final-theta-profile-fourth-table.json`), all52/52
source declarations, one actual proof anchor per owned target, strict UTF8 and zero literal
replacement sequences. Repeat totals in the same order are555.307,438.834,372.492,550.311,
713.441,272.562,197.554,1013.946,832.759,933.383,261.594ms. Φ FAILED1000ms; the first
988.865ms value is not cherry-picked as a pass. Public Θ_lt itself passed320.673/261.594ms.
The other retained estimates are below1000 in both sweeps, but these measurements are not
fresh independent helper audits and receive no audit credit.

Owner/coordinator changed the handoff scope: stop duplicate production optimization, freeze
the verified0cb candidate, carry Φ’s failed repeat into the FIRST mandatory fresh helper audit,
then audit ALL eleven introduced helpers and run final exact-SHA gates before count/publication.
A subsequent narrowing experiment was already in production when that instruction arrived;
its active build was drained (exit0,40.183s), exact source/diff/hash saved as
`post-0cb-narrowing-experiment.lean/.diff/.json`, then ONLY those own post0cb changes were
reverted with a narrow patch. Production is byte-identical to `final-Theta-source-sixth.lean`,
SHA0cb111c95cb755ec1e80a5a39ac4c1a35ad0460dfd3c75988be0fd89e4ed7118. The saved experiment
is not a final gate. Restored module/caller olean refresh and bounded caller trace follow.

Actionable first-fresh-Φ-audit leads, not implemented or claimed proved here:

- Narrow broad hM/hq cast simpa to `simpa only`; the preserved experiment compiles this with
  direct ε/base positivity terms, but has no accepted timing measurement.
- The Φ/successor IH still includes a small-δ upper-bound premise, while public Θ_lt now proves
  every positive δ. Using the unrestricted public IH might remove the need for theta_delta_succ_lt_aux, but
  this STRENGTHENS the private helper premise; it is not automatically a weakening or
  generalization of that private statement. Every affected helper requires exact FIRST-contract
  recovery, potentially extending the old bounded IH using the independent large-δ card
  estimate, with no current Root Θ self-use in the independent FIRST proof. This is an
  unimplemented inspection lead, not a compiled deletion candidate; retention remains reasonable
  if clean adapters/clarity evidence do not support deletion. If deleted, its FIRST-clean
  context/history still requires the separate fresh introduced-helper deletion/replacement audit.

Required owner queue remains: Φ performance first; ALL eleven fresh introduced-helper audits;
refresh public35/caller/allactualvalues/old adapters/natives/profiles on the resulting exact SHA;
known index29/numeric failed repeats; independent file-wide simplify; cumulative all29/allprivate
checks; full lake build THEN separate LeanEval; report/stage/commit/push. File/count/publication
are pending with the owner. This scoped handoff does not claim the whole project is complete.


Restored exact0cb Theta module rebuild passed38.013s (`restored-theta-build.log/json`), then
MainLemma build passed5.861s (`restored-mainlemma-build.log/json`). The earlier full67-check
semantic and complete native evidence is on this SAME exact source SHA. The later reverted
experiment cannot supply acceptance evidence for it. Source edits are now revoked; the final
bounded actual MainLemma profile runs on the restored modules/source before complete drain.


### Actual updated caller trace and final ownership release

The restored actual MainLemma source was profiled with the exact required command and the
same180s wall bound as the baseline. `final-caller-profile.log/json` timed out180.032s with
process group terminated/drained. Raw104304735 bytes are strict UTF8, zero replacement sequences,
SHA50a8cb7fb495b0675019b93afc9f5cd500d325196c18810efab5dfbbfcfe448a. Exact encoding/status
record and labeled escaped tail are `.log.utf8.json` / `.log.tail-escaped.txt`; raw unchanged.
`final-caller-profile-table.json` matches11/27 source declarations before the bounded stop;
last named anchor is abs_coeff_modByMonic_le. The actual main_lemma source/proof anchor is
absent, so NO finite main_lemma timing was measured and NO caller timing pass is claimed.
No explicit Lean error line or maximum-heartbeat message appears. The baseline likewise
had no finite main_lemma timing at180.018s. These are bounded profiling limitations in earlier
MainLemma elaboration, not proof/axiom failures or evidence of a default heartbeat error.
The entire actual updated caller proof/contract/value/standard-axis/native/module gates above
remain successful; owner will refresh all gates after the fresh helper audits.

Final scoped gate status: PUBLIC35 semantic/module/native PASS; public Θ_lt real timing
PASS320.673/261.594ms; Φ helper performance OPEN988.865/1013.946ms; caller timing UNMEASURED;
all eleven introduced-helper fresh dedicated audits, cumulative owner gates and publication
PENDING. No original/helper count increment was made. All owned source edits are revoked,
all ordinary/native/profile/parser requests drained, pending[]. Production sources remain
Theta0cb111c95cb755ec1e80a5a39ac4c1a35ad0460dfd3c75988be0fd89e4ed7118 and
MainLemmaca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4;
Main remains original2b. `helper-handoff.json` contains the ordered TEN retained helpers,
ONE introduced-then-deleted helper, FIRST-clean contexts/logs/hashes and actual contract/value/
axis evidence. `final-freeze.json` records exact final hashes and pending[] for the owner.


## Owner clarification: independent updated caller evidence

The earlier scaffold verified the entire independent ORIGINAL MainLemma proof and the
actual updated Root.main_lemma body/type/standard axioms/dependency. Its wording above
about an independent updated caller overstated the evidence: it did not separately copy
the CURRENT caller proof. Those historical67/68-marker runs are retained without relabeling.
The fresh delta-helper audit supplies that missing supplement in
`/private/tmp/theta35-delta-fresh/ActualSemanticsAugmented.lean`: the entire prior scaffold
is a byte-identical prefix, followed by the ENTIRE current MainLemma module copy, its
opaque-value/standard-axiom checks, all26 effective binder names/order/BinderInfo/types
and conclusion, direct Root.Θ_lt dependence, and AST exclusion of imported Root.main_lemma
and private Root MainLemma helpers. Its actual fresh run passed92.739s/114 PASS markers
on Theta3ea263890113e18bef9a29203ef1db57d929c18e40fd5201e34c9e4f0e776fc2;
MainLemma remains ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4.
Owner verified all96 artifact/source hashes and raw clean output in
`/private/tmp/theta35-delta-fresh/owner-checked.json`. This augmented scaffold is required
in subsequent final-source helper/batch gates. The exact report before this clarification
is preserved in `/private/tmp/theta35-owner-report-corrections/`; source and prior measurements
are unchanged. Original35 publication and whole-file final gates remain pending.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (61.547 s),
then separate `lake build Roth.LeanEval` (31.863 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `cfa05489380deeae6eb1bc63202249c3754b791357912aabff24e29e1cae4788`.
Raw logs: `/private/tmp/roth-theta-d35-full.log`, `/private/tmp/roth-theta-d35-leaneval.log`; machine record
`/private/tmp/roth-theta-d35-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 35/35, overall 216/264 original
declarations, 9/14 completed files. All11 introduced obligations complete: retained scaled_unique,delta_succ,prefix_lt,base,denominators,phi,successor,large_delta; introduced/deleted fin_option,prefix_log,last_lt_first each have their own fresh generic original-contract/deletion-replacement audit. No helper or revisit count inflation.


## Final owner acceptance of complete original35 batch

All eleven introduced-helper obligations are complete, including eight retained helpers and three introduced-then-deleted helpers. The separate prefix performance revisit is also complete. This final acceptance supersedes earlier pending helper/owner entries in this report and its scoped child reports; no helper or revisit increases the original-declaration count.

| Fresh dedicated audit | Final disposition |
|---|---|
| [theta_phi_lt_aux](Theta-theta_phi_lt_aux.md) | retained |
| [theta_scaled_unique_le_aux](Theta-theta_scaled_unique_le_aux.md) | retained; exact FIRST recovery |
| [theta_delta_succ_lt_aux](Theta-theta_delta_succ_lt_aux.md) | retained |
| [theta_prefix_log_le_aux](Theta-theta_prefix_log_le_aux.md) | deleted; exact generic recovery/AST absence |
| [theta_prefix_lt_aux](Theta-theta_prefix_lt_aux.md) | retained; exact Antitone recovery |
| [theta_lt_base_aux](Theta-theta_lt_base_aux.md) | retained; exact FIRST recovery |
| [theta_denominators_one_lt_aux](Theta-theta_denominators_one_lt_aux.md) | retained; exact FIRST recovery |
| [theta_last_lt_first_aux](Theta-theta_last_lt_first_aux.md) | deleted; exact original recovery/AST absence |
| [theta_lt_succ_aux](Theta-theta_lt_succ_aux.md) | retained |
| [theta_lt_of_large_delta_aux](Theta-theta_lt_of_large_delta_aux.md) | retained |
| [theta_fin_option_le_aux](Theta-theta_fin_option_le_aux.md) | deleted; arbitrary FIRST12 recovery/opaque AST absence |

[Additional prefix performance repair](Theta-theta_prefix_lt_aux-performance.md) replaces only restricted `nlinarith` with `linarith`. Historical834.213/1098.066ms failure stays preserved. Final source SHA256 `cfa05489380deeae6eb1bc63202249c3754b791357912aabff24e29e1cae4788`; MainLemma SHA256 `ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4`. Main remains byte-identical to the original baseline. PublicTheta9 and entire MainLemma26 binders remain exactly checked.

Owner cumulative all29-public recovery compiles independently with29 explicit full old-type adapters,87 actual opaque-body/type checks and87 actual standard-axiom sets. All five public definition value equalities are kernel-checked by original-constant reflexivity against the full actual adapters. Raw probe `/private/tmp/ThetaApprovedOriginalFinalProbe-d35-values.lean`; log and machine counts `/private/tmp/roth-theta-d35-values-cumulative29.log`, `/private/tmp/roth-theta-d35-cumulative29-owner-counts.json`. Separate all50 actual retained declaration bodies/types and all50 axiom sets compile: `/private/tmp/ThetaAllActualValues-d35.lean`, `/private/tmp/roth-theta-d35-allactual.json`. No PANIC, error, sorryAx or nonstandard axioms. All17 project/source/pin hashes remain frozen. The entire359-check semantic scaffold preserves all four full original/current proof blocks byte-for-byte, including complete independent original2b and current MainLemma proofs.

Final complete native responses report Theta0errors/8warnings and MainLemma0errors/3warnings; no warnings suppressed. Owner independently verified artifact hashes, exact FIRST contexts, literal-prefix searches, actual opaque deletion scans, all50 dynamic source anchors, disjoint timing sums and strictUTF8 raw logs/slices. Final whole-source pair accepts every retained introduced35 helper and the headline:

| Actual declaration | First ms | Repeat ms |
|---|---:|---:|
| theta_scaled_unique_le_aux | 515.046 | 576.254 |
| theta_delta_succ_lt_aux | 726.873 | 673.393 |
| theta_prefix_lt_aux | 757.698 | 767.127 |
| theta_lt_base_aux | 487.755 | 425.002 |
| theta_denominators_one_lt_aux | 118.249 | 101.625 |
| theta_phi_lt_aux | 887.425 | 641.027 |
| theta_lt_succ_aux | 852.192 | 728.387 |
| theta_lt_of_large_delta_aux | 749.055 | 765.292 |
| Θ_lt | 413.535 | 330.244 |

All ≥750ms cases have the same-final-source repeat; no third unchanged-source sample clears a failure. Deleted helpers have timing N/A, never0. Final raw/table/slice evidence and owner checks: `/private/tmp/theta35-prefix-performance/`. Full `lake build`61.547s then separate `lake build Roth.LeanEval`31.863s pass with all17 source/pin hashes identical.

This is scoped original35 acceptance, not file-final or whole-file performance acceptance. Eight older unrelated performance revisits, fresh independent filewide simplification review and final cumulative gates remain. The actual MainLemma profile remains bounded/unmeasured before main_lemma; successful ordinary semantics/native/builds do not establish a finite caller timing. After successful push:216/264 originals,Theta35/35,9/14 completed files.
