# Phase 4: `Roth.kroneckerExp_injOn`

Fresh dedicated d07 audit; scope is this declaration and this report only. Start snapshot:
`/private/tmp/roth-d07-start.lean`; original public baseline:
`/private/tmp/roth-genwronskian-baseline.lean`. No Git operations, shared-log edits, full builds,
LeanEval runs, or other-declaration changes. Final source SHA256:
`71987145fa101e7d90eb961eb3f939babce38d9ae9c33d33864ced02969c4f1d`.
Source ownership returned to the file owner after module build and complete LSP verification.

## Step 1: references and scope

Read both installed `mathlib-quality/SKILL.md` and `lean4/SKILL.md`, the full 853-line worker
contract, initial `GenWronskian.md`, and the mandatory golfing-rules, proof-patterns,
mathlib-search, generalisation-patterns, cleanup-gates references. Read relevant style-rules
sections, naming-conventions, and mathlib-review-stages. Existing public types, definitions,
docstrings, and comments are protected. The parent supplies the frozen full-project baseline.

## Step 2: full audit

Start L64–77: 14 declaration lines. Final L64–74: 11 declaration lines, nine body lines.

1. **LINT:** no warning in the target. Complete initial and final diagnostics each show the
   same five outside warnings, listed below.
2. **HAVE SCAN:** initial L68 `hsum` has a tactic proof and is instantiated twice at L71;
   retain its useful content but combine it with the digit expansion. Initial L72 anonymous
   function equality has a tactic proof, used once by `congrFun` at L77; replace that equality
   plus pointwise extensionality with existing injectivity APIs. Final L68 `hsum` has a tactic
   proof and simplifies both sides at L74; retained. There are no single-use term-only haves.
3. **SET_OPTION:** none in the declaration or file; none added.
4. **SIMP SQUEEZE:** initial L70 `simp [e]` and L75/L77 `simpa` are terminal. The length and
   digit-bound argument proofs are also terminal. Final L69–70 `simp` closes `hsum`; every
   `by simp`/`by simpa` and final L74 `simpa` closes its own goal. No nonterminal bare simp.
5. **NAMING:** `kroneckerExp` names the subject definition; `_injOn` names `Set.InjOn`.
   No forbidden pattern, number scheme, abbreviation, or single-letter public name. No rename.
6. **LINE PACKING:** both signature lines measured in codepoints; table below. Final local
   `hsum` signature is 99 characters. All changed proof lines are at most 99 characters.
7. **BY PLACEMENT:** theorem and local lemma have `by` at the preceding line end.
8. **FORMAT:** two-space proof indentation, no blank lines inside, no tactic semicolons,
   no `haveI`/`letI`. The ordinary `fun d => by` becomes a direct binder on `hsum`.
9. **COMMENTS:** no inline proof comments present. All four original docstring lines preserved
   byte-for-byte, including the source quotation.
10. **DOCSTRING:** present, explains the restricted domain and cites the source. Existing
    documentation is protected; no speculative rewrite.
11. **VISIBILITY:** public API preserved. It is used twice in `coeff_kronecker`; changing
    visibility is outside the authorization. No new helper declarations.
12. **STRUCTURE:** final nine-line proof, no conjunction or case branch; no extraction needed.
13. **MATHLIB:** five actual methods below. Retain the public domain-specific theorem while
    using digit and function injectivity APIs directly. No duplicate helper introduced.
14. **JUNK DEF:** n/a: this is a theorem, not a definition.
15. **EXISTS LEMMA:** n/a: no existential result or witness wrapper.
16. **SHOW vs CHANGE:** no `show` or `change` present.
17. **PUSH_NEG:** none present.
18. **GENERALISE:** all actual parameters audited below; `hk` can be removed mathematically,
    compiled independently, but public API retained as instructed. No pending proposal.
19. **INEQUALITY:** only `<`; no reversed inequality or name to change. Table below.
20. **NORMAL-FORM:** `Set.InjOn` on the bounded set is the canonical restricted-injectivity
    statement. The internal canonical encoding is `Nat.ofDigits`; final proof uses it directly.
21. **SYNTAX-GEN:** current statement applies directly to two bounded exponent vectors and
    their exponent equality, as both callers demonstrate. No more convenient equivalent API
    required. A digit-list statement already exists in Mathlib.
22. **IMPORT-FANOUT:** no new import. Behrend alternative considered and rejected because its
    module publicly imports complex analysis, inner products, and additive combinatorics.
23. **CASTS:** final diff adds no explicit coercion or type ascription beyond binder types.
    Removed both explicit `(i : ℕ)` annotations with the eliminated sum; `List.mapIdx` supplies
    the natural index. Cast status: two index ascriptions removed with their expressions,
    zero added cross-type casts, zero added load-bearing casts. Public `(σ := σ)` preserved.
24. **INSTANCE-NAME:** n/a: no instance declaration in target or diff.

Issues found: (1) ordinary lambda arrow; (2) separate sum reindexing and digit conversion;
(3) anonymous function-equality/extensionality detour. All three fixed.
Refactoring needed: none. No rename or helper audit needed.

## Step 2.5: Mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `injectivity positional base expansion sum digits times powers fixed length`; then `Nat.ofDigits_inj_of_len_eq` | Both native calls returned read-operation timeout (about ten seconds each); unavailable evidence, not absence. |
| B Loogle | `Nat.ofDigits, _ = _ → _` | Found `Nat.ofDigits_inj_of_len_eq` with the exact fixed-length digit uniqueness statement. |
| C LeanSearch | `A finite sequence of digits less than the base is determined by the sum of digit times base to the index` | Found `Nat.ofDigits_eq_sum_mapIdx`, `Nat.getD_digits`, and `Behrend.map_eq_iff`; successful native search. |
| D source search | untruncated `rg -n 'ofDigits_inj_of_len_eq|ofDigits_eq_sum_mapIdx|ofFn_inj|map_injOn'` in the relevant four Mathlib files | Verified `Nat.ofDigits_inj_of_len_eq` (Defs L312), expansion (Lemmas L37), `List.ofFn_injective`/`ofFn_inj` (OfFn L184–190), `Behrend.map_injOn` (Behrend L162). |
| E local names | `ofDigits`, `Nat.ofDigits_inj_of_len_eq`, `injective_comp`, `Behrend.map_injOn`, `DFunLike.coe_injective` | Positive source-backed results; index unavailable initially, warming subsequently. No empty result used as an absence claim. |

Verified the digit theorem signature by live hover at original L73. Auxiliary variants:
`List.ofFn_inj'`, `List.ofFn_injective`, `Function.Surjective.injective_comp_right`,
`Equiv.injective_comp`, `Behrend.map_eq_iff`, and `map_injOn`. Common-equivalents table:
no discrete/compact/bornology bucket applies; the match is positional digit encoding.

Conclusion: partial match in `Nat.ofDigits_inj_of_len_eq`; retain the domain-specific result
and use it directly with list and function injectivity. `Behrend.map_injOn` gives the exact
finite-function mathematical fact but requires a much larger module and reindexing adapter;
it supplies neither an existing theorem on `kroneckerExp` nor a simpler imported route.
The six replacement rules were checked: no new 1–3-call wrapper; no claim of absence from
search alone; auxiliary variants searched; no custom typeclass predicate; no exact local
duplicate to delete under preserved API; existing module documentation preserved per scope.

Independent generic-route probe used the source prefix before the target, so the target was
unavailable: `/private/tmp/roth-d07-exact.lean` reports `exact? could not close the goal`.
Separate `/private/tmp/roth-d07-apply.lean` offers only partial generic injectivity/monotonicity
routes, not a closed proof; its generated partial/sorry result is rejected. No scratch partial
proof enters the source. The standalone reproof below is complete and independent.

## Step 2.6: generalisation status

`#check @Roth.kroneckerExp_injOn`, width 100:

```lean
@Roth.kroneckerExp_injOn : ∀ {σ : Type u_1} [inst : Fintype σ] {k : ℕ},
  1 < k → Set.InjOn (Roth.kroneckerExp k) {d | ∀ (j : σ), d j < k}
```

| Parameter | Class | Actual use | Mechanical candidates and verification | Resolution |
|---|---|---|---|---|
| `{σ : Type*}` | type/universe | exponent vector index, enumeration | Drop with `autoImplicit false`: unknown `σ`; already universe-polymorphic. Arbitrary finite indexing already supported, no concrete-to-abstract restriction. | retain |
| `[Fintype σ]` | typeclass | public `kroneckerExp` type and `equivFin` | Drop: failed to synthesize `Fintype σ`. Replace by parent `[Finite σ]`: same error in the protected statement. Choosing a new Fintype changes the expression's instance-dependent definition and is not a mechanical weakening of this API. | retain |
| `{k : ℕ}` | structure value | base and bounded digit domain | Drop with `autoImplicit false`: unknown `k`. Abstract ordered structure cannot support this fixed natural-number exponent encoding without restating `kroneckerExp`. | retain |
| `(hk : 1 < k)` | proposition | required by Mathlib digit theorem | Drop and strict→weak: a complete no-`hk` theorem compiled in `/private/tmp/roth-d07-generalise.lean`, case-splitting at `1 < k`; small-base case uses digit bounds and `lia`. Thus even no base hypothesis is sufficient. | preserved public API; optional change closed, no speculative pending task |

The full no-`hk` reproof exits 0, standard axioms only. It strictly contains the `0 ≤ k` and
`1 ≤ k` weakening candidates. No pointwise/global or bundled-hypothesis catalogue entries
apply: `hk` is a scalar arithmetic fact and the remaining parameters are data/typeclasses.
`K`, `[Field K]`, and `l` do not occur in the elaborated theorem type, so they are not hidden
parameters requiring weakening. The returned digit bounds `hd`, `hd'` and equality `h` are
the three arguments of `InjOn`; dropping a bound would allow carry collisions, and dropping
the equality would assert all bounded vectors are equal. They are used directly, globally
over their complete vector domains, with no point-local weakening possible.

Inversion check: after unfolding `kroneckerExp`, the abstract content is positional digit
uniqueness, already supplied by `Nat.ofDigits_inj_of_len_eq` and `Behrend.map_injOn`.
Do not extract another copy. No new generalized helper or public restatement needed.
Big-change candidates requiring action: none. The optional public `hk` removal was tested
and deliberately closed under the explicit signature-preservation instruction.

### Public literature search

Primary query: `"Kronecker substitution" "injective" "exponents"`. Top three returned hits:

1. [Derandomizing Multivariate Polynomial Factoring for Low Degree Factors, §2.6](https://drops.dagstuhl.de/storage/00lipics/lipics-vol317-approx-random2024/LIPIcs.APPROX-RANDOM.2024.75/LIPIcs.APPROX-RANDOM.2024.75.pdf): standard substitution encodes bounded exponent vectors by powers of a base; supports the present statement.
2. [ECCC Report 197/2024](https://eccc.weizmann.ac.il/report/2024/197/download): the same explicit bounded-monomial encoding; not independent evidence from the first hit.
3. [An Algebraic Rigidity Framework…, Lemma 5.4.2](https://www.researchgate.net/publication/400854586_An_Algebraic_Rigidity_Framework_for_Order-Oblivious_Deterministic_Black-Box_PIT_of_ROABPs): surfaced uniqueness terminology; no implementation or generalization decision relies on this secondary-hosted hit.

Canonical-form query: `"numeral system" "uniqueness" "mixed radix" generalization`.
Top three returned hits:

1. [Numeral system](https://en.wikipedia.org/wiki/Numeral_system).
2. [Non-standard positional numeral systems](https://en.wikipedia.org/wiki/Non-standard_positional_numeral_systems).
3. [Mirror of the latter](https://wiki.chogus.org/content/wikipedia_en_all_maxi_2025-08/Non-standard_positional_numeral_systems).

These catalogue mixed-radix terminology; no mathematical proof claim depends on them.
The primary source above already establishes the relevant uniform-base formulation.
Mixed radices would replace the definition of `kroneckerExp` and do not supply a needed
weakening of this theorem. Exploratory query `Kronecker substitution injective bounded
exponents base representation generalization` also surfaced
[Beecken–Mittmann–Saxena, §3.1](https://www.cse.iitk.ac.in/users/nitin/papers/alg-indep.pdf)
and its [CiteSeer copy](https://citeseerx.ist.psu.edu/document?doi=3df4dbe3eb8ced3d6b5035eff42ded4df5da1e24&repid=rep1&type=pdf);
this is broader polynomial faithfulness, not a missing condition for digit uniqueness.
Math ChatGPT MCP: n/a, no such tool in the discovered session catalogue.
Literature-driven pending changes: none.

## Step 2.7: signature line packing

| Signature line | Chars | Next complete signature component | Arithmetic | Action |
|---|---:|---|---|---|
| 64 | 49 | `Set.InjOn (kroneckerExp (σ := σ) k) {d \| ∀ j, d j < k} := by` (60) | 49 + 1 + 60 = 110 > 100 | ok |
| 65 | 64 | no next signature line | n/a | ok |

Signature unchanged from original baseline, not merely start snapshot. Local `hsum` binder
and conclusion are packed onto one 99-codepoint line; maximum final target width is 99.

## Step 2.8: inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | entire signature and hypotheses | no `≥` or `>` occurrence | n/a; `1 < k` and `d j < k` already correctly oriented | none |

## Step 3: all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by-exact wrapper | n/a: no such wrapper. |
| 1.2 by-rfl | n/a: no reflexivity wrapper. |
| 1.3 rw + exact | n/a: no such consecutive pair; old hsum rewrites eliminated. |
| 1.4 simp + exact | applied: final `simpa [Function.comp_def, hsum] using h` combines conversion and equality. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 constructor pair | n/a: no conjunctive constructor. |
| 1.7 apply + exact | applied in spirit: composed existing injectivity proofs directly, rather than named intermediate equality. |
| 1.8 by_contra! | n/a: no contradiction argument. |
| 1.9 eta lambdas | applied binder form to `hsum`; remaining lambdas compose evaluation with `e.symm`, so not eta-redexes. |
| 1.10 inline single-use have | applied: removed anonymous function equality and its pointwise use; the surviving hsum has proof content and two instantiations. |
| 1.11 apply + intro | n/a: no such pair. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have/projections | n/a: no tuple projections. |
| 1.14 merge rw | n/a: no consecutive rewrites; no rw remains. |
| 1.15 unsqueeze terminal simp only | checked: final simpa was tested without `only` and compiles; final source has no simp only. |
| 1.16 squeeze nonterminal simp | n/a: all simp/simpa calls close their own goal. |
| 1.17 dot notation | applied `e.symm.surjective.injective_comp_right`. |
| 1.18 less parentheses | applied `<|` for the composed injectivity proof. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential helper | n/a: none. |
| 2.1 grind whole proof | tried: isolated whole-goal `grind` failed; native hsum-position `grind [kroneckerExp]` also failed, not timed out. |
| 2.2 delete pre-grind tactics | n/a: retained proof contains no grind. |
| 2.3 simpa consolidation | applied: hsum directly converts digit encoding to exponent; final simpa replaces rewriting both sides and finishing. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability property. |
| 2.5 positivity | n/a: target and subgoals are equalities or given strict digit bounds, not structural positivity obligations. |
| 2.6 gcongr | n/a: no monotonicity inequality to prove. |
| 2.7 lia/omega | tried whole-goal lia: failed; `lia` succeeds for the independently tested small-base generalization branch. No omega introduced. |
| 2.8 aesop | tried whole-goal and native local hsum: both fail; no useful digit-reindexing automation. |
| 2.9 norm_num/norm_cast | n/a: no concrete numerical computation or cross-type cast equality; Fin-to-Nat index conversion is removed with the sum. |
| 2.10 decide | n/a: polymorphic unbounded digit vectors and arbitrary base, no finite closed computation. |
| 2.11 field_simp/ring | n/a: no division or ring identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint or linear polynomial identity. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 collapse calc | n/a: no calc block. |
| 2.15 common closing tactic | n/a: three Nat.ofDigits premises are length/bound/bound, not repeated identical goals; existing individual simp proofs are direct. |
| 3.1 erw to rw | n/a: no erw. |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactic. |
| 3.3 omega to lia | satisfied in 2.7; no omega in final source. |
| 3.4 rcases rfl | n/a: no rcases/substitution. |
| 3.5 automation registration | n/a: restricted injectivity does not define a useful global simp normal form; no new declaration requiring registration. |
| 3.6 simp_all | n/a: no simp_all only; whole-goal simp/aesop fail and final direct simpa closes. |
| 3.7 remove raised options | n/a: no heartbeat/recursion option to remove. |

The initial native whole-proof multi-attempt batch was cancelled after no bounded response.
Direct standalone probes then supplied actual whole-goal results; a subsequent native local
multi-attempt completed with explicit failed grind/aesop/simp results and timed_out=false.
Negative probes are outside the repository. No raised limit, axiom, sorry, or native_decide
was introduced into source.

## Step 4: step back

The mathematics is unique fixed-length base expansion transported through the enumeration.
The final proof expresses exactly that: establish encoding equality once, cancel evaluation
and precomposition by an equivalence, then invoke list/digit injectivity. `exact?` did not
find a closed imported proof and `apply?` offered only generic partial routes. Whole-goal
automation and local hsum automation did not remove the encoding argument. A term-only
version would duplicate a four-line encoding expression or bury it in a lambda. No new
single-use helper is justified. An earlier overly inferred pointwise candidate failed;
the final generic function-injectivity route avoids that elaboration ambiguity entirely.

## Step 5: verification and gates

Actual module command: `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session 96637,
exit 0; `/private/tmp/roth-d07-module.log` ends `Build completed successfully (1838 jobs).`
Complete final native `lean_diagnostic_messages` on the full source:
`success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`, zero errors.
The five warnings are:

1. L1 missing authoritative header metadata, explicitly protected.
2. L36 unused section `[Fintype σ]` in `genWronskian_eq_zero_of_not_linearIndependent`.
3. L32 unused `[Fintype σ]` in that theorem's type.
4. L233 unused `[DecidableEq ι]` in `det_sum_rows`.
5. L251 unused `[Fintype σ]` in `exists_genWronskian_ne_zero`.

No target warning. Full-project and separate LeanEval checks belong to the owner and were
not rerun here.

Independent nonself proof: `/private/tmp/roth-d07-independent.lean`, session 78416 exit 0.
This copies only the source prefix before the target, proves `Roth.d07_candidate` directly
using the final proof, and never imports or calls `Roth.kroneckerExp_injOn`. Axiom output:
`[propext, Classical.choice, Quot.sound]`.

Exact original public type gate: `/private/tmp/roth-d07-type.lean`, session 22743 exit 0,
explicitly assigns `@Roth.kroneckerExp_injOn` to the original fully quantified type with
`1 < k` retained; width-100 #check shown above. Its #print axioms gives the same three standard
axioms. Python comparison also confirms the original baseline signature is byte-identical,
not merely definitionally equal. Nonself reproof and public theorem both satisfy trust gate.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module command/session exit 0 above |
| definition_protected | pass | diff contains no definition/abbreviation changes |
| theorem_statement_protected | pass | exact original signature, explicit original-type assignment exit 0 |
| structure_gate | pass | nine proof lines; no conjunction or case branch |
| naming_gate | pass | descriptive subject plus InjOn; no forbidden pattern or abbreviation |
| line_packing_gate | pass | both signature rows measured; longest target line 99 |
| inequality_orientation_gate | pass | scan table; no reversed inequality in signature |
| comment/doc protection | pass | original docstring intact; no inline comment removed |
| declaration scope | pass | byte comparison: only target changed from worker snapshot |
| standard axioms/nonself | pass | two independent compiled artifacts above |

Overall: pass. Focused source diff stored at `/private/tmp/roth-d07.diff`.

## Step 6: result and required checklist

Before 14 lines; after 11; saved 3. Compared with the original baseline's 11-line public
declaration, the target has returned to 11 lines while eliminating the five-line private
digit wrapper previously removed by d06. Do not credit d06's wrapper deletion to this worker.
Audit issues found: 3; fixed: 3; refactoring deferred: 0. Renames queued: none.
Rules chiefly applied: 1.4, 1.7, 1.9, 1.10, 1.17, 1.18, 2.3. Comments preserved: four of
four docstring lines; none inside proof. Refactoring needed: none.

- [x] Step 1 — reference docs read.
- [x] Step 2 — all 24 audit items given concrete outcomes.
- [x] Step 2.5 — five-method search block; timeout/warming limitations explicit.
- [x] Step 2.6 — every actual parameter audited; public literature and compiled hk-drop test.
- [x] Step 2.7 — per-signature-line codepoint table, width-100 #check.
- [x] Step 2.8 — inequality occurrence scan.
- [x] Step 3 — all 42 golfing rules have statuses.
- [x] Step 4 — whole-proof/API/term-mode reflection.
- [x] Step 5a — complete clean LSP, all five outside warnings recorded.
- [x] Step 5b — module and diff gates; exact original type and independent nonself proof.
- [x] Step 6a — no rename required, no sidecar mutation.
