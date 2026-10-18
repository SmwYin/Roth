# Cleanup: `Roth.sum_max_sub_le_index_det`

Dedicated original declaration 27/35. Source: `Roth/Theta.lean`, original lines 370–403,
final lines 371–402. This leaf owns only this theorem and its necessary routine caller
proof adjustment in `index_le_lem6`; no Git, shared log, or rename queue mutations.

## Result and authorization

Applied the user's explicitly approved removal of `[DecidableEq τ]` and named `hR : R ≠ 0`.
All other original arguments, their names, types, order, BinderInfo, universes, domain,
visibility, theorem name and conclusion are retained. The sole caller no longer passes
`hmapR`, and its now-unused two-line proof is removed. The caller's entire original type,
including `hq` and `[DecidableEq τ]`, is protected by an independent-original verifier.

The entry bound now obtains the zero branch of `max_le` directly from `add_nonneg`,
`index_nonneg`, `weight_nonneg`, and the weight bound; its remaining arithmetic uses
`linarith only [h1, h2]`. Rewriting `hdet` directly removes its temporary copy. Nonvanishing
of each permutation product comes directly from `mul_ne_zero_iff`. Lambda arrows use `↦`.
No helpers, attributes, imports, limits, or axioms were introduced.

Proof body: **25 → 24 lines**. Declaration: **34 → 32 lines**. Entire source:
**983 → 980 lines** (the added `omit` line offsets part of the declaration savings).
No proof comments were present in the target; the original docstring and caller comments
are preserved verbatim. No further changes are recommended by this leaf.

## Baseline and evidence scope

- Starting source SHA256:
  `e6360c9acdc9d7be22356ba3a26006e24cc1b0b667b5992395759228e1087530`.
- Inherited exact-source complete unfiltered native LSP:
  `/private/tmp/roth-theta-positive-audit/final-lsp.json`, success true, partial false,
  timed_out false, failed_dependencies [], 0 errors, 17 warnings.
- Inherited owner baseline full build 92.510s, followed separately by LeanEval 33.553s;
  both pass on the identical starting source. These are inherited, not leaf executions.
- Fresh profile uses the exact source prefix through this declaration, including all its
  original imports and preceding context, then closes `Lemma6` and `Roth`. It does not
  claim a whole-file instrumented pass: the later original `index_le_lem6` instrumented
  heartbeat issue belongs to its reserved audit.
- All scratch sources, UTF-8 logs and machine-readable results are in
  `/private/tmp/roth-theta-sum-index/`.

## Full 24-item audit

| # | Item | Concrete assessment/action |
|---|---|---|
| 1 | LINT | Baseline target has unused section DecidableEq and unused hR warnings. Both approved removals address them; unrelated file warnings belong to their dedicated declarations. Final native counts are recorded below. |
| 2 | HAVE SCAN | Every original `have` is inventoried in the next table; remove h3/h4/hdet' while preserving proof content and useful shared bounds. |
| 3 | SET_OPTION | No local options or heartbeat/recursion raises exist; none added. |
| 4 | SIMP SQUEEZE | `simp [h, index_neg]` in the sign cases and `by simp` for the constant sum both close their goals and remain unsqueezed. No nonterminal bare simp. |
| 5 | NAMING | `sum_max_sub_le_index_det` describes a lower sum bound on determinant index; snake case, no forbidden abbreviations, scheme numbers, or single-letter public name. No rename needed. |
| 6 | LINE PACKING | Repacked D onto the first line and α after the determinant hypothesis. Every signature line is measured below; maximum 100 codepoints. |
| 7 | BY PLACEMENT | Every `by` remains at the end of its preceding line. |
| 8 | FORMAT | Two-space proof indentation, four-space signature continuation, no blank proof lines, no haveI/letI, one tactic per line except the existing intentional `<;>` shared sign-case closer. |
| 9 | COMMENTS | No inline target comments to remove; original three-line source docstring and all caller narrative comments preserved. |
| 10 | DOCSTRING | Existing public theorem documentation describes the lower bound and cites §5 Lemma 6; protected unchanged. |
| 11 | VISIBILITY | Retain the existing public source-facing theorem under the user's prior wrapper/API choices. A single internal caller does not authorize reopening that choice. |
| 12 | STRUCTURE | 24 body lines ≤ 30; hterm has 7 lines after its header, sign cases each use the same one-line closer; no branch exceeds 10 lines. No conjunction conclusion or extraction required. |
| 13 | MATHLIB | Five actual searches and clean pre-target anonymous exact?/apply? probes below. Partial building blocks exist; no replacement was established. This is not a claim of exhaustive mathematical absence. |
| 14 | JUNK DEF | n/a: theorem, no new definition or notation. |
| 15 | EXISTS LEMMA | n/a: this is not a private existential wrapper. |
| 16 | SHOW vs CHANGE | No `show` or `change` occurrences. |
| 17 | PUSH_NEG | No push_neg occurrences in this declaration. |
| 18 | GENERALISE | Every effective original binder receives a compiled drop/weakening probe below; exactly the two approved removals are applied. Finite-family and strict-degree alternatives compile but are not recommended here. |
| 19 | INEQUALITY | All five signature inequalities use ≤/<. Per-occurrence scan below; no reversed inequality tokens. |
| 20 | NORMAL-FORM | Existing finite sum of max-minus-δ is the source's lower-bound normal form; index on the right, degree/weight bounds in canonical ≤ orientation. No new equivalence API. |
| 21 | SYNTAX-GEN | Removing the irrelevant R nonvanishing argument directly simplifies the sole caller. Retain the established degree-bounded interface rather than introducing another public wrapper. |
| 22 | IMPORT-FANOUT | n/a: no imports added or changed. |
| 23 | CASTS | Zero casts dropped. Retained ν:ℕ conversions of Fin indices, sign→ℤ→polynomial coercions, and l:ℝ in hlδ are cross-type or load-bearing. No redundant cast introduced in the diff. |
| 24 | INSTANCE-NAME | No instance declarations introduced; the section's anonymous synthetic binder is omitted only for this theorem. Anonymous-instance renumbering is permitted by verifier; ordinary named arguments remain exact. |

### Every original `have`

| Have | Original use / proof status | Action |
|---|---|---|
| hterm | Proof-bearing local bound, used in final summand comparison | Retain; 7-line proof fits the branch limit. |
| h1 | Derivative index bound; rewritten before use | Retain the explicit rewritten bound; used by the restricted linarith. |
| h2 | Weight bound specialized using hD and μ.isLt | Retain; final proof uses it both in transitivity and linarith. |
| h3 | index_nonneg, one implicit arithmetic use | Inline into explicit add_nonneg. |
| h4 | weight_nonneg, one implicit arithmetic use | Inline into the transitive proof of 0≤δ. |
| hdet' | Alias of hdet, one proof continuation | Delete alias; rewrite hdet directly. |
| hprod | Nonzero permutation product, used twice | Retain; derive with `(mul_ne_zero_iff.mp hs).2`. |
| hidx | Proof-bearing invariance under multiplication by sign | Retain the short sign-case proof. |
| hlδ | Proof-bearing constant-sum identity | Retain `by simp`, followed by the sum subtraction rewrite. |

## Five-method mathlib search

Actual raw responses: `search-results.json`; untruncated local source search: `grep-search.log`.

| Method | Actual query | Result and interpretation |
|---|---|---|
| A Lean-Finder | lower bound weighted order index of determinant of a matrix of multivariate polynomial derivatives | Successful response: det_mvPolynomialX_ne_zero, det_matrixOfPolynomials, polynomial determinant degree bounds; none states this index lower bound. |
| B Loogle | `Matrix.det, _ ≤ _` | Successful response: Matrix.det_le / det_sum_le (absolute values), PosSemidef.det_nonneg and polynomial degree bounds. These are upper absolute-value bounds or positivity, not this result. |
| C LeanSearch | valuation of determinant lower bound sum of lower bounds on columns | Successful response includes AddValuation.map_le_sum and determinant absolute-value bounds. AddValuation is a conceptual partial match, not directly usable for index with index 0=0. |
| D Source grep | `sum_max_sub_le_index_det|index_det|det.*(weightedOrder|valuation)|weightedOrder.*det` over all mathlib source | Untruncated search returns only unrelated textual matches. No declaration-equivalent found by this search. |
| E lean_local_search | `det`, limit 20 | Actual response returns Matrix.det_le and project determinant lemmas among others; `index: unavailable`. The source fallback contributed results; this does not certify symbol-index absence. |

Auxiliary variants inspected: determinant sum expansion (`Matrix.det_apply'`), valuation
sum lower bounds, product nonvanishing, column bounds, weighted order, derivative index,
and polynomial determinant degree bounds. No common-equivalents discrete/finite/topology
bucket applies. Existing project index sum/product/derivative APIs and mathlib matrix/finite
sum APIs remain the building blocks. No new wrapper or duplicate was added.

The compiled generic-route exploration is `automation.lean`, an **exact source prefix
ending before the audited declaration**, with five separate anonymous `example`s. It does
not import Roth.Theta and cannot find the audited result or a named failed trial:

- whole-proof `grind`: fails with determinant index goal;
- whole-proof `aesop`: unsolved goal;
- `exact?`: no closer;
- `apply?`: partial `le_index_iff` route plus unrelated order embeddings, reaches default
  200000-heartbeat isDefEq limit; no limit raised;
- `simp_all`: unsolved normalized lower bound.

The batch exits 1, as expected for negative exploration; it is not axiom certification.
No native multi_attempt request was issued: the established repeated full-Theta stall
limitation was respected, with bounded ordinary-compiler fallback instead.

## Every-effective-binder generalisation pass

`binder-negative.lean` uses `set_option autoImplicit false`, disjoint namespaces and the
entire original target proof. Its expected-failure exit is 1; each range has actual errors
in `binder-negative-map.json`. `binder-positive.lean` separately exits 0 and contains
complete proofs of the two drops and two optional restatements. These are not selfproofs.

| Original effective binder | Classification/use | Compiled experiment and result | Decision |
|---|---|---|---|
| τ : Type* | Type variable used in polynomials, D, α, r | Drop fails unknown τ in dependent class/type declarations. Already universe polymorphic. | Retain. |
| [Fintype τ] | Finite-variable index product API | Drop fails synthesis of finite option-variable instances. Finite τ alone would require reinstantiating the same finite representation; no domain restatement recommended. | Retain. |
| [DecidableEq τ] | Decidability unused in statement/proof | Independent original proof with class removed and `classical` added compiles. | Approved removal applied via omit before docstring. |
| R | Polynomial value throughout statement and derivative proof | Drop fails unknown R in dependent hypotheses/conclusion. | Retain original domain ℝ. |
| hR : R≠0 | No use | Drop with entire original proof compiles. The l=0 case in particular need not have nonzero R. | Approved removal applied. |
| l | Size of matrix, range sum, and D domain | Drop fails unknown l in dependent types. Arbitrary finite-index restatement would change the column numbering and caller interface. | Retain. |
| D | Differentiation family | Drop fails unknown D in hD/determinant. | Retain. |
| hD | Degree bound used to specialize hδ | Drop fails at its original use. Combined replacement by direct finite-family weight bounds compiles (LocalWeights.finite_weights), removing hD. | No further change recommended; retain source-facing degree contract and current caller evidence. |
| hdet | Nonzero determinant needed by le_index_sum | Drop fails at hdet use and the sum lower-bound step. No weakening of this nonvanishing predicate preserves its role under index 0=0. | Retain. |
| α | Evaluation point used in every index | Drop fails unknown α throughout type/proof. | Retain full point function. |
| r | Weight denominators used in every index and hδ | Drop fails unknown r in dependent hypotheses/conclusion. | Retain natural weights. |
| hr | Positive weights needed by index_prod | Drop fails; strict→weak `∀j,0≤r j` fails at index_prod with argument type mismatch. | Retain. |
| δ | Common loss bound in both sides | Drop fails unknown δ in hδ and conclusion. | Retain ℝ. |
| hδ | Global bounded-degree weight bound | Drop fails at hδ use. Direct finite-family weights compile; degree≤l−1→degree<l also compiles after specializing with hD μ<l. | Both are assessed/unapplied options, not recommended changes. The sole caller naturally proves the current global degree bound. |

There are no algebraic typeclass-parent weakenings for ℝ in isolation: the project's
index is defined on real multivariate polynomials. General coefficient-field abstraction
requires redesigning that API, rather than changing one binder mechanically. No extra
hypotheses or weaker conclusion were introduced.

### Literature and inversion

Three actual web searches were performed:

1. “Roth theorem index determinant derivatives lower bound index weights generalization”;
2. “weighted valuation determinant lower bound sum columns derivative polynomial Roth lemma 6”;
3. “site.arxiv.org Formalizing Roth theorem Takloo Bighash Yin”.

Relevant primary/expository source hits were [UCL's transcendental-number-theory notes](https://www.ucl.ac.uk/~ucahpet/TransNotes.pdf),
[Min Ru's Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf), and the
[1990 Annali article](https://www.numdam.org/item/ASNSP_1990_4_17_4_615_0.pdf).
The first derives the same max/sum determinant index bound from derivative-order losses;
the second states the index sum/product rules; the third uses determinant expansion to
compare lower and upper index bounds. These support the existing mathematical pattern,
not a mandatory new public interface. Search results are saved verbatim in search-results.json.
The third query did not identify the project's paper; no absence claim follows.

The authoritative local source is `.mathlib-quality/references/clean.tex:815–840`:
nonzero permutation terms, sign invariance, product additivity, derivative loss, and the
final displayed index bound match the Lean proof. ChatGPT math MCP is unavailable among
this session's callable tools; no external second-opinion response is claimed.

**Inversion diagnostic:** after establishing hterm, the determinant-expansion suffix is
indeed generic in a matrix E and column bounds c. This is a real abstraction opportunity,
not hidden or rejected as impossible. `inversion.lean` compiles a complete short proof of
`∑ν,c ν ≤ index E.det α r` for arbitrary finite square polynomial matrices, with nonzero
entry-conditional column bounds. However, introducing a new public theorem or one-use
private wrapper here would add an API and a fresh audit without removing the substantive
7-line derivative estimate. The current 24-line proof is clear, under all size/performance
limits, and its sole caller wants this concrete derivative determinant. I do not recommend
adding that companion in this cleanup. The generic probe is evidence of the assessment,
not an implemented or outstanding recommendation.

## Measured signature packing

Reference type is printed at `format.width 100` in the actual-built compatibility log.
Widths are Unicode codepoints, including indentation, not UTF-8 bytes. “Next token” below
means the next complete binder or application segment at a legal signature break, not a
single word torn from its dependent expression. The initial short first line admitted D;
the determinant-hypothesis continuation admitted α exactly up to 100; both were repacked.

| Sig line | Chars | Next complete token/group | Arithmetic | Action |
|---|---|---|---|---|
| 371 | 95 | `(hD : ∀ μ, (D μ).degree ≤ μ)` (28) | 95 + 1 + 28 = 124 > 100 | ok |
| 372 | 69 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0)` (75) | 69 + 1 + 75 = 145 > 100 | ok |
| 373 | 100 | `{r : Option τ → ℕ}` (18) | 100 + 1 + 18 = 119 > 100 | ok |
| 374 | 50 | `(hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ)` (63) | 50 + 1 + 63 = 114 > 100 | ok |
| 375 | 69 | `∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤` (64) | 69 + 1 + 64 = 134 > 100 | ok |
| 376 | 68 | `index (Matrix.of fun μ ν : Fin l ↦` (34) | 68 + 1 + 34 = 103 > 100 | ok |
| 377 | 40 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by` (80) | 40 + 1 + 80 = 121 > 100 | ok |
| 378 | 88 | `` (0) | final signature line | ok |

## Inequality scan

| Occurrence | Location | Final expression/orientation | Action |
|---|---|---|---|
| 1 | hD | `(D μ).degree ≤ μ` | already ≤ |
| 2 | hr | `0 < r j` | already < |
| 3 | hδ premise | `d.degree ≤ l - 1` | already ≤ |
| 4 | hδ result | `weight (r ∘ some) d ≤ δ` | already ≤ |
| 5 | conclusion | sum − lδ ≤ determinant index | already ≤ |
| reversed tokens | entire code signature | no ≥ or > | no rewrite or rename needed |

The name has `_le_`, not `_ge_`/`_gt_`. Mathematical prose in the protected docstring is
unchanged. The proof's typed hterm is also ≤ oriented.

## All 42 golfing rules

| Rule | Status and concrete reason/evidence |
|---|---|
| 1.1 by exact | n/a: no single exact proof wrapper. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw+exact→rwa | n/a: rewrites lead to sums or arithmetic rather than a closing exact on the same fact. |
| 1.4 simp+exact→simpa | n/a: both simp calls already close their goals; no simp-then-exact chain. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: no conjunction/structure construction. |
| 1.7 apply+exact | n/a: direct exact/refine already used. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | Nontrivial sum/product-entry lambdas retain varying membership arguments; no `fun x ↦ f x` wrapper. Lambda arrows standardized. |
| 1.10 inline have | h3/h4 inlined into explicit nonnegativity proof; hdet' removed. h2 is now used twice; hprod used twice; remaining have blocks have proof content. |
| 1.11 refine+fun | Existing le_index_sum proof already uses refine with its summand lambda. |
| 1.12 redundant show | n/a: none. |
| 1.13 destructure projections | hprod's repeated prod_ne_zero_iff use is a function on every entry, not a fixed conjunction to destructure; no spurious obtain introduced. |
| 1.14 merge rw | No consecutive rw calls with no intervening logical work; final hlδ and sum-subtraction rewrites already merged. |
| 1.15 terminal simp | Sign cases and hlδ unsqueezed already. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | Retain `(hD μ).trans`, use `.trans h2` and `(mul_ne_zero_iff.mp hs).2`; explicit arithmetic transitivity now visible. |
| 1.18 <| | No trailing parenthesized tactic proof is improved here; direct proof terms replace the old hprod tactic closure. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial ∃ helper | n/a: none. |
| 2.1 grind | Actual whole-proof anonymous pre-target probe fails. |
| 2.2 delete before grind | No production grind; whole-proof attempt already tests dropping all setup. |
| 2.3 simpa | No applicable terminal simp+closer; explicit max bound improves the entry proof. |
| 2.4 fun_prop | n/a: no continuity, measurability or differentiability predicate. Hasse derivative here is algebraic. |
| 2.5 positivity | Local 0≤a+δ probe with 0≤a, 0≤w≤δ tested in local-automation.lean; explicit transitivity is the selected proof. |
| 2.6 gcongr | Local finite-sum monotonicity alternative tested; direct Finset.sum_le_sum already states exactly the mathematical step without extra goal setup. |
| 2.7 lia/omega | Local `(D μ).degree≤l−1` arithmetic probe with hD μ and μ.isLt tested with lia; existing two-lemma term avoids adding arithmetic search. No omega added. |
| 2.8 aesop | Actual whole-proof anonymous pre-target probe leaves the determinant index bound. |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric computation or standalone cast equality goal; ν and l casts are genuine type bridges. |
| 2.10 decide | n/a: quantified arbitrary real/polynomial bound, not finite closed computation. |
| 2.11 field_simp;ring | n/a: no denominator identity goal; positivity of denominator is consumed by index_prod, not algebraic field normalization. |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint with hypotheses; restricted linarith supplies the linear inequality certificate. |
| 2.13 wlog | n/a: sign cases are ±1 simplifications, not symmetric copies of a substantive proof. |
| 2.14 term calc | n/a: no two-step calc; max zero branch converted directly to a composed term. |
| 2.15 shared <;> | Keep existing shared simp closer for the two sign cases. |
| 3.1 erw→rw | n/a: only rw used. |
| 3.2 fun_prop migration | n/a: no legacy continuity/measurability tactics. |
| 3.3 omega→lia | No omega in target; local finite arithmetic probe uses lia. |
| 3.4 rcases rfl | Sign-case equalities feed simp; substituting the unit sign variable itself is neither necessary nor clearer. |
| 3.5 attributes | One specialized determinant bound; adding simp/grind registration would broaden automation and is not recommended. |
| 3.6 simp_all | Whole-proof terminal simp_all probe fails; no production simp_all only to unsqueeze. |
| 3.7 heartbeat options | None present or added. |

## Step back, simplify, and performance

The proof has two mathematical stages: derive an entry bound from the Hasse derivative
weight, then expand the determinant and add column bounds. The generic inversion probe
shows that another abstraction is possible, while the existing arrangement keeps the
substantive estimate local without a new one-use helper. The selected explicit nonnegativity
term and restricted linarith are clearer and more controlled than broad automation.

A separate built-in `/simplify` callable skill is not exposed in this host. Its review
questions were executed directly: no duplicate new helper, redundant cast, avoidable
bridge, unchanged-comment loss, or unimplemented recommended change was found. Outcome:
ISSUES-FOUND-AND-FIXED by this leaf's explicit changes, then PASS-THROUGH on the final review.
The buzz workflow is performed directly using the real required Lean4.34 invocation below,
not the obsolete `-Dprofiler=true` command from older reference prose.

## Verification and frozen measurements

Frozen production SHA256:
`ac43e6d19ce869213d3d0f6a260ffc92ab8f419d9b2be320483539746e5434a9`.
No production source edits occurred after the freeze, module build, actual-built probe,
final native LSP, or final profile. All requests have completed; none are orphaned.

### Actual compiler and diagnostic gates

| Gate | Result | Concrete evidence |
|---|---|---|
| lake_build_file | PASS | `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit 0, “Build completed successfully (2423 jobs).” Raw `module-build.log`. |
| Final complete unfiltered native LSP | PASS | native `lean_diagnostic_messages` on absolute live Theta path with no range/declaration/severity/timeout filters; success true, partial false, timed_out false, failed_dependencies [], 0 errors, 14 warnings. Raw `final-lsp.json`. |
| Target diagnostics | PASS | No target warning or error. Baseline's 3 target warnings (unused hR plus two DecidableEq diagnostics) are removed by the 2 approved removals. |
| Entire caller contract | PASS | `actual-compatibility.lean` imports the just-built module, compiles the complete independent original Index+Theta namespace, and verifies the entire original `index_le_lem6` telescope with drop set []. Its hq and DecidableEq arguments remain. Exit 0. |
| Original target type/value | PASS | Same successful file checks the old target telescope via exactly [`DecidableEq`, `hR`] drops; all retained binder types/order/BinderInfo/names, universes and conclusion match. `value! true` checks the independent old complete proof value; proof-irrelevance recovery equality is kernel checked. |
| Actual-built axioms | PASS | Original target, actual target, original caller, actual caller and both recovery declarations each have exactly `[propext, Classical.choice, Quot.sound]`; no PANIC/error/sorryAx in the positive log. |
| Independent namespace immutability | PASS | Verification-tail-only copy from `/private/tmp/roth-theta-min-sum/actual-compatibility.lean`; immutable independent prefix is byte-identical, SHA256 `1fccac8a3ba419f384e5fb258dcd40dfc58abde7fb70cef78ea22c0d3e478837`. The target AND caller bodies are the complete old independent proofs, not header-only aliases or references to their current theorems. |
| definition_protected | PASS | No production def/abbrev changed. |
| theorem_statement_protected | PASS | Exactly the user's two approved target removals; no caller type change, no other argument/domain/conclusion change. Verified semantically against original types, including section instances. |
| structure_gate | PASS | 24 body lines ≤ 30, no >10-line branch, no conjunction conclusion, no new helper requiring a further audit. |
| naming_gate | PASS | Descriptive snake case; no rename needed. |
| line_packing_gate | PASS | All 8 signature lines measured above, max 100; no remaining repack row. |
| inequality_orientation_gate | PASS | All 5 signature inequalities have ≤/< orientation; no ≥/> code token. |
| cumulative_no_unintended_breakage | PASS for leaf scope | Sole source caller in Roth is adjusted routinely, compiled by the module build and independently checked for its entire original contract. Final owner project/LeanEval gates remain pending owner execution. |
| Source hygiene | PASS | No sorry/new axiom/native_decide/limit raise/profile scaffolding added; protected docstring and narrative comments unchanged. |

The 14 remaining full-file warnings are the protected header; retained hr/hB binders at
93,101,109,129,252; the separately reserved index_det_le warnings at 404,408,411,416;
the retained hq and separate DecidableEq audit at 523/517; and Θ_option_le DecidableEq at 619.
They are preserved in the complete raw JSON, not filtered or suppressed.

New identifier verification: `mul_ne_zero_iff` and `add_nonneg` are explicitly `#check`ed
in the positive built probe. Every other mathematical identifier in the changed proof was
already present in the original target; the local `classical` tactic is compiler checked.
Casts: 0 dropped; changed signature lines retain the 2 genuine Fin→Nat casts; no new cast
is introduced. Existing unchanged sign→integer→polynomial and l→real casts remain
cross-type or load-bearing.

`local-automation.lean` exits 1 **only** for the expected positivity failure; its separate
gcongr finite-sum and lia finite-degree examples elaborate without diagnostics. It is
exploration, not an axiom verifier. The selected actual proof is certified by the separate
exit 0 module and actual-built-original probe.

### Real uncontended profiles

Exact invocation, with SRC substituted by the stored exact prefix path:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 SRC
```

| Run / raw log | Exit | Outer command ms | Async proof ms | AddDecl ms (includes kernel) | Async lint ms | Accepted total ms |
|---|---|---:|---:|---:|---:|---:|
| initial `baseline-profile.log` | 1 | 101.948 | 586.828 | 35.167 | 27.957 | **discarded** |
| corrected `baseline-profile-corrected.log` | 0 | 113.922 | 607.584 | 31.263 | 26.773 | **779.542** |
| clean repeat `baseline-profile-repeat.log` | 0 | 121.261 | 649.137 | 33.000 | 28.564 | **831.962** |
| frozen final `final-profile.log` | 0 | 113.802 | 578.314 | 29.110 | 25.226 | **746.452** |

The first scratch prefix incorrectly closed Roth while Lemma6 was open. Its actual target
trace totaled 751.900ms but the file exited 1 at the closing command; it is not accepted as
a successful baseline gate. The closing scope was corrected without changing the exact
production prefix, and the corrected run passed. Since that clean 779.542ms baseline is
≥750ms, a second clean uncongested baseline was run and passed at 831.962ms. Both clean
baseline logs, not the discarded first run, establish the repeated baseline evidence.

The final `omit ... in` expands into several command rows. The counted 113.802ms is its
**outer wrapper**; the nested 108.802ms theorem/header and the section/omit/end machinery
are included there and are not added again. Likewise, the final kernel 16.735ms is nested
inside AddDecl 29.110ms and is not double-counted. There is no separate executable compiler
cost for this opaque theorem. All associated disjoint async proof, AddDecl and lint tasks
are included. An initial automatic extraction that found only the inner header was
corrected before reporting; authoritative `profile-target-timings.json` uses the wrapper
block containing the actual async proof. No 108.802ms-only timing is accepted.

The final aggregate 746.452ms is below both the 1000ms budget and 750ms repeat trigger;
no extra final repetition is required. Final prefix compile wall time 115.040s and clean
baseline repeat 119.276s are trace/import/output wall times for the whole stored prefix,
not timings of this theorem. Commands and exits are saved in `profile-runs.json`.
All ordinary compiler/LSP calls had drained before these final sequential profiles;
the owner explicitly kept the compiler window clear. No limits, masking options or
profiling scaffolding were added to production.

Buzz outcome: **FAST-BOARD** (baseline and final under 1000ms). No over-budget deferral;
maxHeartbeats raises removed 0 / added 0. Final measurements are prefix-only and make no
claim that the later whole-file instrumented heartbeat issue has been resolved.


## Eleven-step checklist

- [✓] Step 1: full golfing, proof patterns, mathlib search, generalisation and cleanup gate references read; relevant style/naming/profiling material consulted.
- [✓] Step 2: every one of the 24 audit items answered, with every original have inventoried.
- [✓] Step 2.5: all five actual search methods, auxiliary variants, and uncontaminated compiled generic-route probes recorded.
- [✓] Step 2.6: every effective original binder drop/weakening probe, literature and inversion assessments recorded.
- [✓] Step 2.7: every signature line measured and repacked; conclusion included.
- [✓] Step 2.8: all inequality occurrences scanned; no reversed code inequality remains.
- [✓] Step 3: all 42 golfing rules have a concrete status.
- [✓] Step 4: step-back and direct simplify review completed; no further recommended change left pending.
- [✓] Step 5a: final complete unfiltered native LSP recorded below.
- [✓] Step 5b: final diff gates, independent original proof/type/value/metadata and actual-built axioms recorded below.
- [✓] Step 6a: no rename required, therefore no sidecar writes.

No Git operations or shared-report/queue writes were performed. Owner full `lake build`,
separate `lake build Roth.LeanEval`, final cumulative sweep and publication remain owner
responsibilities; this leaf does not claim their final execution.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (110.300 s),
then separate `lake build Roth.LeanEval` (32.749 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `ac43e6d19ce869213d3d0f6a260ffc92ab8f419d9b2be320483539746e5434a9`.
Raw logs: `/private/tmp/roth-theta-d27-full.log`, `/private/tmp/roth-theta-d27-leaneval.log`; machine record
`/private/tmp/roth-theta-d27-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 27/35, overall 208/264 original
declarations, 9/14 completed files. No new production helper; all prior helpers remain separately audited.
