# Fresh independent audit: `exists_coeffNone_basis_aux`

Initial audit written before any source edit, 2026-10-18. Owned scope: this private helper only; no source edits proposed yet. Exact original helper: `/private/tmp/roth-s21-exists_coeffNone_basis_aux.lean.txt`. Whole source freeze: `/private/tmp/roth-separation-s21-source-freeze.lean`, SHA256 `dc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e`.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, plus the Lean and mathlib-quality skill instructions and Phase 4 worker contract. Source is a private 26-line declaration (5 signature lines and 21 body lines), at lines 285–310 initially.

The proof takes the span of the finitely many coefficient polynomials. The polynomial expansion and nonzero polynomial force a nonzero coefficient, hence positive dimension. A finite basis has at most the number of generators. The canonical `restrictSupport` submodule transfers coordinatewise degree bounds from generators to basis vectors.

## Initial 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | Obtain complete native module diagnostics; no suppression. |
| 2 | HAVE SCAN | Anonymous finite-dimensional instance needed by `finBasis` and `finrank`; `hl1` contains substantive nonzero coefficient argument; `hdegree` contains span/support argument. Keep each, consider direct Mathlib alternatives. |
| 3 | SET_OPTION | None in helper. |
| 4 | SIMP SQUEEZE | `simp [h]` closes contradiction; `simpa using` closes support degree goal. Both terminal. |
| 5 | NAMING | Name describes coefficient basis existence; `_aux` private suffix; no forbidden abbreviation or numeric scheme. No rename needed. |
| 6 | LINE PACKING | Five signature lines; measure all with complete next syntactic units. |
| 7 | BY PLACEMENT | Both `by` tokens end preceding lines. |
| 8 | FORMAT | Two-space body indentation, no blank internal lines or inline-instance syntax. |
| 9 | COMMENTS | No helper comments to remove; preserve surrounding narratives. |
| 10 | DOCSTRING | Private helper has none, appropriate. |
| 11 | VISIBILITY | Private single-file helper with `_aux`. |
| 12 | STRUCTURE | 21-line substantive helper below 60, nonzero branch 7 lines; caller remains 14 body lines. Conjunction packages one basis with its required properties; splitting would introduce another helper contrary to owned scope, so retain shared witness package. |
| 13 | MATHLIB | Five actual searches plus generic exact/apply probes required; investigate basis/span/finrank/restrictSupport building blocks. |
| 14 | JUNK DEF | n/a: theorem, not definition. |
| 15 | EXISTS LEMMA | Nontrivial: finite dimension, positive rank, cardinality, and degree construction; not reflexive witness junk. |
| 16 | SHOW/CHANGE | Existing `change` makes local abbreviation visible in expansion; no redundant `show`. |
| 17 | PUSH_NEG | `by_contra!` already used; no deprecated `push_neg`. |
| 18 | GENERALISE | Audit effective τ,K,Field,P,hP,n,hP′; Fintype/DecidableEq τ explicitly omitted. |
| 19 | INEQUALITY | Only ≤ in statement and support bound; no reversed inequalities. Detailed table below. |
| 20 | NORMAL-FORM | `Module.Basis`, `Submodule.span`, `Module.finrank`, and `restrictSupport` are canonical Mathlib forms. |
| 21 | SYNTAX-GEN | Expansion certificate intentionally shared with caller; replacing it by degree bound duplicates expansion work. |
| 22 | IMPORT-FANOUT | n/a: no new imports planned. |
| 23 | CASTS | Fin→Nat exponent and subtype→polynomial are genuine coercions; typed ν fixes finite index. No diff casts yet. |
| 24 | INSTANCE-NAME | Anonymous local finite-dimensional instance appropriate; no global instance declaration. |

Initial issues to investigate: native diagnostics, existing Mathlib equivalent, every binder, whole-proof automation, width and structure certificates. Public contracts and declined wrapper/domain/Nat alternatives preserved. Literature search explicitly exempt: private declaration, no public API generalisation proposed.

## Five actual Mathlib searches

Raw native responses: `/private/tmp/roth-s21-helper-native-initial.json`.

| Method | Actual query / result | Action |
|---|---|---|
| A Lean-Finder | “A basis of the span of finitely many coefficient polynomials has positive dimension and degree bounded by the original polynomial”; returned univariate `Polynomial.exists_degree_le_of_mem_span_of_finite`, `span_le_degreeLE_of_finite`, and related degree bounds. | Partial, univariate bounds do not construct this multivariate coefficient basis. |
| B Loogle | `Module.finBasis`; returned exact existing finite-basis constructor, with Free/Finite/StrongRankCondition requirements. | Already used directly. |
| C LeanSearch | “finite basis of span finite family finrank bounded by cardinality positive if nonzero”; returned `finrank_le_of_span_eq_top`, `basisOfTopLeSpanOfCardEqFinrank`, `FiniteDimensional.span_finset`, `Submodule.spanFinrank_span_le_ncard_of_finite`. | Partial: basis existence/cardinality building blocks, no coefficient-support construction. |
| D Source | Untruncated searches for `finrank_range_le_card`, `finrank_pos_iff_exists_ne_zero`, `span_of_finite`, `degreeOf_le_iff`, `mem_support_coeff_optionEquivLeft`, `restrictSupport`, full target name; additional degreeOf/span/basis variants across Mathlib. | `/private/tmp/roth-s21-helper-source-search.log`, `/private/tmp/roth-s21-helper-variants-search.log`. Existing construction already uses direct Mathlib APIs. |
| E Native local names | `finrank_range_le_card`, `restrictSupport`; positive hits for dimension bound and canonical support submodule, including `restrictSupport_mono`, `_eq_span`, `_univ`, `_zero`, `_add`. Index reports `warming`, so empty/omitted hits are not absence evidence. | Positive results verified by source and compiler. |

All three remote methods responded; no remote outage or literature-based claim of absence. Auxiliary variants searched: `exists.*Basis`, `Basis.*exists`, `span.*restrictSupport`, `degreeOf.*span`, `span.*degreeOf`, `_le_card`, `_le_of_span_eq_top`, `_of_finite`, `_pos_iff_exists_ne_zero`. Common-equivalents table: finite-dimensional span is already canonical, no disguised custom predicate. Conclusion: partial matches, retain substantive construction using those APIs. This is not a 1–3-call wrapper: the proof derives coefficient nonvanishing from the expansion, constructs nonzero span data, transfers multivariate support bounds, and packages rank constraints on the same basis. No generic theorem discovered that eliminates it while preserving the ≤15-line main outline.

Generic-route probes: native whole-proof `exact?` failed, `apply?` produced only generic existential transformations with remaining obligations (not a completed proof). `grind` failed; `aesop` hit default recursion depth. Raw results `/private/tmp/roth-s21-helper-native-automation.json`. No limits raised. These failures are scoped evidence about attempted routes, not a universal absence theorem.

## All 42 golfing rules

| Rule | Concrete status |
|---|---|
| 1.1 by exact | n/a: no wrapper. |
| 1.2 by rfl | n/a: no reflexivity-only body. |
| 1.3 rw/exact→rwa | n/a: expansion rewrite is followed by `simp [h]`, not exact. |
| 1.4 simp/exact→simpa | Already `simpa using monomial_le_degreeOf ...` at support step. |
| 1.5 trailing rfl | n/a: neither simp call has trailing rfl. |
| 1.6 anonymous constructors | Already final nested witness tuple and nonzero subtype tuple. |
| 1.7 apply/exact | n/a: `apply hP` changes target, followed by expansion rewrite and simp. |
| 1.8 by_contra! | Already present in nonzero coefficient argument. |
| 1.9 eta reduction | `fun ν ↦ coeffNone P ν` contains a Fin→Nat coercion; other lambdas transform arguments, no direct eta reduction. |
| 1.10 single-use have | Anonymous finite-dimensional fact is instance used repeatedly by finBasis/finrank; `hl1` has proof content; `hdegree` has support proof content in nested by-lambda and names the span invariant, not a trivial alias. |
| 1.11 refine+fun | n/a: no apply/intro chain. |
| 1.12 redundant show | n/a: no show; local change reveals abbreviation in expansion certificate. |
| 1.13 obtain | Already destructures nonzero coefficient with `obtain ⟨ν,hν⟩`; no redundant conjunction projection chain. |
| 1.14 merge rw | n/a: only one rewrite. |
| 1.15 terminal simp | Terminal `simp [h]` and terminal simpa unsqueezed. |
| 1.16 nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | Already `.2`, `.trans_eq`; `Submodule.span_le` and `Module.finrank_pos_iff_exists_ne_zero` have no meaningful receiver to shorten. |
| 1.18 trailing parentheses | Parentheses are projection/application grouping, not gratuitous final lambda delimiters. |
| 1.19 push_neg | n/a: no deprecated tactic. |
| 1.20 trivial exists | Rejected: basis witness requires substantive 21-line construction. Inlining restores 30-line headline proof, violating explicit ≤15 requirement. |
| 2.1 grind | Native whole-proof attempt failed to construct basis and support invariant. |
| 2.2 delete before grind | n/a: retained proof contains no grind. |
| 2.3 simpa consolidation | Already uses simpa at support bound. |
| 2.4 fun_prop | n/a: algebraic basis/degree result, no analytic property. |
| 2.5 positivity | Native coefficient existence attempt reports “not a positivity goal”; positivity cannot construct a nonzero coefficient/basis. |
| 2.6 gcongr | n/a: bounds use dimension cardinality and support characterization, not monotone arithmetic expressions. |
| 2.7 lia/omega | Native `lia` attempt fails to infer nonzero coefficient from polynomial expansion; no arithmetic chain to replace. |
| 2.8 aesop | Native whole/helper coefficient attempts reach default recursion depth; retained explicit argument. |
| 2.9 norm_num/cast | n/a: symbolic rank and degree, no numeric calculation or redundant cast equality. |
| 2.10 decide | n/a: existential vector-space basis over arbitrary field is not finite decidable computation. |
| 2.11 field_simp/ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf terminal proof or ring equality with linear hypotheses. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc composition | Already `(finrank_range_le_card ...).trans_eq ...`; no calc. |
| 2.15 multiple-goal combinator | n/a: construction has different mathematical obligations rather than duplicate branches. |
| 3.1 erw | n/a: no erw. |
| 3.2 continuity | n/a: no legacy analytic tactic. |
| 3.3 omega→lia | n/a: no omega retained; lia tested in 2.7. |
| 3.4 rcases rfl | n/a: no equality case substitution. |
| 3.5 attributes | n/a: private dependent existential construction is not a simplification/extensionality rule. |
| 3.6 simp_all | Native coefficient attempt reaches recursion depth; no simp_all only in retained proof. |
| 3.7 options | No heartbeat, recursion, trace, linter-suppression or profiler scaffolding in source. |

Additional native chunk results: `/private/tmp/roth-s21-helper-native-rank-automation.json`. Every automation failure was bounded by defaults, with no proof source edited.

## Step-back review and correlated witness certificate

The entire proof cannot be replaced by tested `grind`, `aesop`, or `exact?`; `apply?` supplies no domain-specific completed replacement. Term mode would still require the positive-rank contradiction and support submodule proof. All three `have`s carry instance/invariant/proof work. `v`, `V`, and `b` prevent repeated long dependent expressions. The actual construction keeps every basis element in one canonical support submodule and derives the degree bound directly, so no repeated span induction or custom predicate remains.

The conjunction splitter is mathematically inapplicable to independent existential results: `∃ l,b, A(l,b) ∧ B(l,b)` cannot be reconstructed from separate `∃ l,b,A(l,b)` and `∃ l,b,B(l,b)` witnesses. The chosen index cardinality and chosen basis must agree. Splitting would require passing the common chosen witness through extra lemmas or duplicating choice and subsequently proving compatibility, not simplifying independent facts. The helper is already the substantive decomposition of finite dimension, positive rank, cardinality and degree; helper body 21, headline body 14, largest nonzero-coefficient branch 7. Retain the correlated certificate; no unfinished decomposition obligation and no new helper proposed. This applicability finding follows the mathematics and the explicit preserved shared-certificate requirement.

## Width and inequality certificates

Reference: the actual built private helper is located by exact suffix; `/private/tmp/roth-s21-helper-type-axioms.log` prints its full type with `format.width := 100` and verifies definitional equality against the exact original signature. Character counts below include source indentation; next-unit widths exclude indentation. Whole binders/conjunctions are meaningful units: moving a detached `∃ l,` or partial conjunction is token fragmentation, not meaningful packing. No width exceeds 100.

| Signature line | Chars | Next complete unit, width | Arithmetic | Action |
|---|---:|---|---|---|
| 285 | 93 | expansion-certificate binder including trailing colon, 79 | 93+1+79=173 | ok |
| 286 | 83 | dependent existential basis header `∃ l, ∃ b : Module.Basis (Fin l) K`, 33 (its dependent module argument follows) | 83+1+33=117 | ok |
| 287 | 37 | dependent span argument, 69 | 37+1+69=107 | ok |
| 288 | 75 | correlated constraints through conclusion, 90 including `:= by` | 75+1+90=166 | ok |
| 289 | 96 | no next signature unit | n/a | ok |

| Occurrence | Location | Inequality | Rewrite | Rename |
|---|---|---|---|---|
| 1 | conclusion | `1 ≤ l` | already canonical | none |
| 2 | conclusion | `l ≤ n + 1` | already canonical | none |
| 3 | conclusion | `degreeOf j (b ρ : MvPolynomial τ K) ≤ degreeOf (some j) P` | already canonical | none |
| 4 | body `hl1` | `1 ≤ Module.finrank K V` | already canonical | none |
| 5 | body `hdegree` | `V ≤ restrictSupport ...` | already canonical | none |
| 6 | support predicate | `d j ≤ degreeOf (some j) P` | already canonical | none |
| n/a | all signature/hypotheses | zero `≥` / `>` | none required | no `_ge_` / `_gt_` name |

Casts: zero dropped; genuine Fin→Nat exponent/coefficient coercions and subtype→polynomial coercions retained. Typed `ν : Fin (n+1)` in the support-lambda fixes the generator index; all other ascriptions identify local object types or theorem targets. No source diff introduced ascriptions.

## Effective binders and mechanical generalisation

All seven effective binders are shown by the actual built-type printer. Every drop test used `set_option autoImplicit false`; failed formation is distinguished from a semantic impossibility proof. Complete unfiltered compiler logs are `/private/tmp/roth-s21-helper-<variant>.log`, generated by `/private/tmp/roth-s21-helper-probes.py`; results index `/private/tmp/roth-s21-helper-probe-results.json`.

| Binder | Class | Mathematical use | Actual candidates / verification | Result |
|---|---|---|---|---|
| `{τ : Type*}` | type variable | variables of coefficients and coordinate degree bound | `drop_tau`, compiler exit 1, unknown τ; universe already polymorphic | Retain; changing variable type universe is not a weakening beyond Type*. |
| `{K : Type*}` | type variable | coefficient field and scalar ring | `drop_K`, compiler exit 1, unknown K | Retain; no concrete scalar choice to abstract. |
| `[Field K]` | typeclass | commutative polynomial coefficients plus free finite-dimensional span and positive rank | `drop_field`: missing CommSemiring; `divisionRing`: missing CommSemiring; `commRing`: missing DivisionRing/Module.Free/StrongRankCondition; `commSemiring`: corresponding missing division/free/rank structure, all exit 1. | No safe weakening survives this proof. IsField variant discussed below; domain/Nat alternatives explicitly declined, not reintroduced. |
| `{P : MvPolynomial (Option τ) K}` | structure value | expansion, nonzero argument, coefficient span, support bound | `drop_P`, compiler exit 1, unknown P throughout signature | Retain; formation dependency, not an independent removable hypothesis. |
| `(hP : P ≠ 0)` | proposition | forces nonzero coefficient, positive rank | `drop_hP`, compiler exit 1, unknown hP at contradiction. Zero P gives zero span and no positive-cardinality basis. No ordered nonnegativity weakening for arbitrary field. | Retain; necessary mathematical nonvanishing. |
| `{n : ℕ}` | index bound | finite family size, expansion, cardinality bound | `drop_n`, compiler exit 1, unknown n. Arbitrary index type restates construction, rather than mechanical weakening. | Retain; Fin cardinality and polynomial exponent use Nat intrinsically. |
| `(hP′ : expansion)` | proposition | converts vanishing finite coefficients into P=0 | `drop_hPprime`, compiler exit 1, unknown hP′ in expansion rewrite. Equality-to-two-inequalities is inapplicable to polynomial identity. Replacing it by degree bound would duplicate expansion work shared with caller. | Retain explicit expansion certificate. |

`[Fintype τ]` and `[DecidableEq τ]` are already explicitly omitted and absent from the actual effective type; the isolated positive proof compiles without either. There is no hidden CharZero/Nonempty/Nontrivial binder beyond what Field supplies. Local finite-dimensional instance is inferred from the finite span, not an external hypothesis.

`[CommRing K] [IsField K]` was also tried, but `IsField` is a proposition, not a class: this syntax fails at binder formation and is not evidence against the meaningful value-level alternative. A separate value-level test `(hK : IsField K)` uses plain `let : Field K := hK.toField`; its concrete compiler result is recorded below. Such an equivalent reconstruction is not a strict weakening and changes caller syntax, so no repository API change follows from it.

Inversion check: `coeffNone` is used both to define the spanning family and through the coefficient-support theorem, and the expansion has its specific distinguished-variable meaning. An abstract finite-family theorem would need nonzero-span and support hypotheses to replace precisely these arguments; it would not remove the domain-specific construction, and would add another abstraction/helper. No abstract/public restatement proposed. Literature status: n/a, private declaration; mechanical weakening remains fully audited above.

Value-level IsField result: `/private/tmp/roth-s21-helper-isField-value.lean` compiled with exit 0 and empty log. This reconstructs the same field with `(hK : IsField K)` and `let : Field K := hK.toField`; it is logically equivalent, introduces explicit caller plumbing and supplies no weaker mathematical hypothesis. Retain original Field binder; no pending generalisation proposal. The earlier invalid `[IsField K]` test is not used as negative evidence.

Scratch route accounting: positive and independent variants exit 0 with no diagnostics; every drop/structural weakening listed in the table exits 1. Scratch `generic_exact`, `generic_grind`, `generic_aesop` exit 1. `generic_apply` exits 0 **with `declaration uses sorry` generated by the incomplete search tactic** and many remaining obligations, so it is expressly rejected as a proof. No sorry token, synthetic proof, axiom, or raised limit was copied into repository source. Raw logs remain complete. Standalone failed generic probes have no certification role.

## Verification and gates

Actual module command `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, `Build completed successfully (1876 jobs)`. Complete log: `/private/tmp/roth-s21-helper-module-build.log`.

Exact original type plus independently elaborated non-self proof: `/private/tmp/roth-s21-helper-type-axioms.lean`, exit 0, log `/private/tmp/roth-s21-helper-type-axioms.log`. The proof reproduces the substantive original argument in a separate namespace; it never invokes the repository target. Meta `isDefEq` compares the elaborated original signature against the actual built private constant, found uniquely by exact suffix `.Roth.exists_coeffNone_basis_aux`. The log prints `EXACT ORIGINAL TYPE VERIFIED`. A scratch metaprogram local binding triggers one unused-variable warning; the independent theorem itself is clean. No repository source modification follows from scratch warnings.

Actual built declarations checked: `_private.Roth.Separation.0.Roth.exists_coeffNone_basis_aux`, `Roth.exists_separated_representation`, `Roth.exists_det_eq_mul`. Each, and the independent proof, has precisely `[propext, Classical.choice, Quot.sound]`; the metaprogram rejects other axioms. Names are discovered by suffix, not assumed private numeric components.

Complete unfiltered native final module LSP: `/private/tmp/roth-s21-helper-native-final.json`, `partial=false`, `timed_out=false`, `success=true`, failed dependencies empty; **0 errors, 9 warnings, 0 infos, 0 hints, 0 sorry diagnostics**. No helper diagnostic. Warnings are preserved header metadata and existing/public unused Fintype/DecidableEq binders outside owned scope. Initial raw diagnostics in `/private/tmp/roth-s21-helper-native-initial.json` have the same counts.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build exit 0, log above. |
| definition_protected | pass | Zero source edits by this worker. |
| theorem_statement_protected | pass | Exact original helper unchanged; exact type verified independently against built constant. |
| structure_gate | pass, correlated-output applicability | Helper 21 body lines, main 14, largest branch 7; dependent shared-basis constraints cannot be split into independent existential witnesses, as detailed above. |
| naming_gate | pass | Mathematical `exists_coeffNone_basis_aux`, no forbidden token or numeric scheme. |
| line_packing_gate | pass | All five source signature lines measured, whole-unit additions exceed 100. |
| inequality_orientation_gate | pass | All occurrences canonical; no reversed inequalities. |
| cumulative affected callers | pass at module scope | Built main/caller plus their actual axioms verified; parent owns full-project/cumulative compatibility checks. |

## Performance and simplify review

Retained helper is byte-identical to the supplied original and source SHA equals the supplied actual-module profile source freeze. Reuse of the valid actual baseline was explicitly allowed for unchanged targets. Actual anchored repository profile: `/private/tmp/roth-separation-s21-final-profile.log`, JSON `/private/tmp/roth-separation-s21-final-profile.log.json`, table `/private/tmp/roth-separation-s21-final-profile-table.log`.

| Actual declaration | Outer command | Outer async proof | Conservative total |
|---|---:|---:|---:|
| exists_coeffNone_basis_aux | 55.134 ms | 591.316 ms | 646.450 ms |
| exists_separated_representation | 58.943 ms | 292.125 ms | 351.068 ms |
| exists_det_eq_mul | 97.288 ms | 385.275 ms | 482.563 ms |

These values count outer command plus outer async proof without adding nested descendants. All are <750 ms repeat threshold and <1000 ms budget. No new profile was started or overlapped with probes; no claim of project-wide improvement. No source change means this actual baseline remains valid for this audit. Parent still reruns cumulative actual profiling after the entire batch drains.

Holistic simplify pass, independently performed after rule checklist: retaining a canonical support submodule is simpler and more reusable than bespoke span induction; basis/rank data is shared, no repetition to extract, no thin wrapper, no duplicate theorem found. Re-inlining would restore a 30-line main body and defeat the intended decomposition. No further edit justified by tested alternatives. Simplify and buzz skills are not separately available in this tool catalogue; their requested scoped reasoning and performance checks were performed explicitly rather than claiming an unavailable invocation.

## Eleven scoped completion stages

1. Doctor: supplied green actual baseline and fresh actual module build confirmed; parent owns original full-project baseline.
2. Prepare: contract, required full references, exact original helper and enclosing main read; mathematical proof explained before changes.
3. Audit: initial substantive 24-item table written before source edits.
4. File-level fixes: none in owned scope; surrounding metadata preserved.
5. Per-declaration deep cleanup: all 42 rules, actual five searches, generic routes, all effective binders, width and inequality tables completed.
6. Refactoring: none applied; correlated witness split concretely rejected; no new helper or public API change.
7. Rename pass: no forbidden name, no rename needed or queued.
8. Final scoped gates: actual module build, independent exact-type proof, actual built axioms and complete native module LSP pass. Parent owns cumulative/original/public compatibility and full project plus LeanEval gates.
9. Simplify: holistic alternative proof/abstraction review above; no further simplification survives requirements.
10. Buzz: unchanged actual source baseline reused with anchored per-declaration costs under both thresholds.
11. Report/freeze: dedicated report only, no source mutations, no shared log/Git mutations; all owned Lean/MCP/compiler requests drained.

## Final result and freeze

**Retain unchanged.** No Lean source edit, extra helper, import, definition, documentation change, public-contract change, or pending proposal. Source remains 597 lines. This helper remains 26 declaration lines = 5 signature + 21 body; main remains 14 body lines. Whole batch `git diff --numstat` is 32 added / 20 removed (net +12), inherited from the authorized structure batch; this worker's source diff is zero. Exact original helper comparison and whole-source comparison to provided freeze both pass.

Final source SHA256: `dc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e`.

All worker-owned requests are drained. **I revoke ALL source ownership and become report-only.** No further source edits will be made. Parent must finish cumulative profiles, compatibility/LSP/full-project/LeanEval checks and publish the authorized batch before moving to original declaration 22.
