# Declaration 8: `Roth.eq_sum_X_none_pow_mul_coeffNone`

Scope: only this public theorem and this report. Public Fintype/DecidableEq omission remains pending and will not be applied. No helpers planned. Parent owns Git, cumulative compatibility, full and LeanEval builds, publication.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md and the applicable Lean, style, naming and profiling guidance.

## Initial audit (before source edits)

Baseline HEAD f86b28b, source 601 lines. Fresh native unfiltered LSP `/private/tmp/roth-separation-d08-initial-0.json`: complete success, 0 errors/31 warnings. Target warnings: unused Fintype and DecidableEq in type; both pending approval. Actual baseline profiler supplied by parent `/private/tmp/roth-separation-d07-final-profile.log`: command 33.548 + async proof 104.047 = 137.595 ms.

| # | Audit | Finding and action |
|---|---|---|
| 1 | Lint | Two index-instance warnings, preserve pending public contract. |
| 2 | Have scan | One anonymous `have := monomial_le_degreeOf ...`, consumed implicitly by omega. Try direct degree-bound contradiction to remove it. |
| 3 | set_option | None. |
| 4 | Simp | `simp_rw` coefficient rewrite and nonterminal `simp only [Finset.mem_range] at he` already explicit. |
| 5 | Naming | Descriptive expansion equality, references X and coeffNone API; no banned pattern or abbreviation. |
| 6 | Packing | Measure all three signature lines below; retain full conclusion on own line if next expression overflows. |
| 7 | By | At end of signature. |
| 8 | Format | Two-space tactics, no blank lines or instance lets. |
| 9 | Comments | Zero proof comments; preserve existing docstring verbatim. |
| 10 | Docs | Existing expansion explanation and source citation sufficient. |
| 11 | Visibility | Public expansion API used by exists_separated_representation; retain. |
| 12 | Structure | 12 tactic lines, longest branch 5, no conjunction; no helper needed. |
| 13 | Mathlib | Five actual searches find polynomial range expansion and optionEquivLeft; test strategy via equivalence. |
| 14 | Junk def | n/a: theorem. |
| 15 | Exists | n/a: public equality, no existential helper. |
| 16 | Show | None. |
| 17 | push_neg | None. |
| 18 | Generalise | Probe every effective binder; public index omission pending, other algebra prerequisites checked. |
| 19 | Inequality | hn already uses ≤; no ≥ or > in Lean signature. |
| 20 | Normal form | Explicit finite reconstruction is canonical; equivalence transport may shorten proof. |
| 21 | Syntax | Existing bound and explicit expansion useful for rewrite/application, no restatement proposed. |
| 22 | Imports | No additional import planned. |
| 23 | Casts | No explicit coercions or ascriptions in original target proof. |
| 24 | Instance names | n/a: not an instance. |

Initial action: test direct equivalence transport of `Polynomial.as_sum_range_C_mul_X_pow'`; otherwise simplify contradiction and replace omega with tested lia. Public wrapper removal would alter API; only report such a proposal if justified, never apply it here.

## Search and literature evidence

Actual native search outputs are `/private/tmp/roth-separation-d08-initial-{1,2,3,4}.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | multivariate polynomial expand in powers of one variable coefficient optionEquivLeft | `optionEquivLeft`, `_symm_apply`, `_monomial` and variable equations. |
| B Loogle | Polynomial.sum_monomial_eq | Found generic sum reconstruction over Semiring. |
| C LeanSearch | polynomial equal sum X powers times coefficients up to degree bound | Found `as_sum_range'`, `as_sum_range_C_mul_X_pow'` and unbounded variants. |
| D Source rg | optionEquivLeft.*degree, degree.*optionEquivLeft, as_sum_range_C_mul_X_pow | Equiv.lean L569–582 and Degree/Support.lean L86–99 inspected, including `natDegree_optionEquivLeft`. |
| E Name pattern | sum_X_pow | Source hits include `Polynomial.as_sum_support_C_mul_X_pow`; index warming, so no absence claim. |

Auxiliary variants actually inspected in source: `_symm_apply`, `_X_none`, `_X_some`, `_C`, `_symm_C_X`, `_symm_C_C`, `degree_optionEquivLeft`, `natDegree_optionEquivLeft`, range expansion with/without prime and support expansion. Common-equivalents table: none of its topology, finiteness, or bornology buckets applies.

Conclusion: mathlib supplies the general reconstruction and equivalence transport; an independently compiled transport proof is retained as verification evidence. The public theorem packages the project-specific `coeffNone` API and degree bound. Deleting this existing public theorem is outside this worker's authorization. No absence claim or new API/helper is needed.

Actual WebSearch query: “polynomial ring R[x y] isomorphic R[x][y] collecting coefficients semiring generalization”. Top three returned hits: UCSD Polynomial rings (math.ucsd.edu), Chavan Polynomial Rings in Several Variables, UCSD duplicate host (mathweb.ucsd.edu). Primary sources relied on: [McKernan, Polynomial rings](https://www.math.ucsd.edu/~jmckerna/Teaching/15-16/Spring/103B/l_15.pdf) and [Chavan, Polynomial rings in several variables](https://home.iitk.ac.in/~chavan/alg3.pdf). Both describe the iterated coefficient-ring identification over commutative rings; local mathlib already provides the semiring generality. Local source `.mathlib-quality/references/clean.tex` L369–374 explicitly collects terms by powers of the distinguished variable. No math ChatGPT MCP was available (actual tool inventory searched). Literature suggests arbitrary index types; the compiled public index-instance omission remains pending. No stronger algebra or finite-dimensional assumption is mathematically needed.

## Signature packing and inequality occurrence tables

Initial and final signature lines are byte-identical. Codepoint counts measured using Python `len`, excluding newline:

| Line | Width | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 89 | 79 | `(hn : degreeOf none P ≤ n)` (26) | 79 + 1 + 26 = 106 > 100 | ok |
| 90 | 32 | Full next conclusion/signature line, stripped (78) | 32 + 1 + 78 = 111 > 100 | ok |
| 91 | 82 | no next signature line | n/a | ok |

The expression concluding the theorem is a syntactic unit; its first whitespace-delimited `P` alone is not the next complete signature component. The width-100 compiler `#check` is in the independent log.

| Occurrence | Location | Original | Rewrite / rename |
|---|---|---|---|
| 1 | hypothesis hn | `degreeOf none P ≤ n` | Already smaller side left. |
| none | Entire signature and inherited binders | No `≥` or `>` | n/a |

## Golf pass: all 42 rules

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl proof. |
| 1.3 | n/a: no rewrite followed by exact; closing branch uses one direct term. |
| 1.4 | n/a: no simp followed by exact; independent equivalence strategy tested simpa explicitly. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor pair. |
| 1.7 | n/a: no apply/exact pair in retained proof. |
| 1.8 | Removed contradiction branch entirely; no push_neg existed. |
| 1.9 | n/a: final lambda consumes support evidence nontrivially, not eta-reducible. |
| 1.10 | Removed anonymous single-use degree-bound have by direct composition at its use site. |
| 1.11 | n/a: no apply/intro chain. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected conjunction have. |
| 1.14 | n/a: rewrites are separated by simp_rw and split_ifs; no consecutive rw. |
| 1.15 | Removed the old nonterminal simp only with entire branch; no terminal simp only remains. |
| 1.16 | Remaining simp_rw is explicit; no bare nonterminal simp. |
| 1.17 | Applied `(monomial_le_degreeOf none h).trans hn`; explicit bound composition. |
| 1.18 | Parentheses in final arithmetic/membership term delimit nested arguments; no reducible trailing tactic/lambda argument. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Native live whole-proof grind failed with negated expansion goal. |
| 2.2 | n/a: no grind retained; branch-only grind also failed. |
| 2.3 | Explicit independent equivalence proof succeeds with simpa only; requires local algebra-hom transport facts and does not shorten the final coefficient strategy. Initial broad simp attempt hit recursion depth; no limits raised. |
| 2.4 | n/a: no continuity, differentiability, or measurability goal. |
| 2.5 | n/a: goal is coefficient equality; no structural positivity/nonzero goal. |
| 2.6 | n/a: no monotonicity goal; arithmetic bound uses direct transitivity. |
| 2.7 | Compiler probe of original branch with lia recorded below; retained proof removes arithmetic automation entirely. |
| 2.8 | Native whole-proof aesop failed, no progress. |
| 2.9 | n/a: no concrete numeric computation or cast normalization. |
| 2.10 | n/a: arbitrary semiring coefficient equality, no finite decidable computation. |
| 2.11 | n/a: no denominator or field structure. |
| 2.12 | n/a: no ring-ending proof or linear polynomial identity. |
| 2.13 | n/a: membership and nonmembership branches are not symmetric. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: branches require different coefficient reconstruction/support arguments. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy function-property tactics. |
| 3.3 | Removed omega entirely; lia probe in 2.7. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | Preserve public attributes: expansion rewrite is not globally simplifying, no new automation registration justified. |
| 3.6 | Native branch simp_all tested; leaves coefficient zero goal, no retained simp_all only. |
| 3.7 | n/a: no heartbeat limit existed or was added. |

Step back: whole-proof native grind/simp/aesop fail; exact?/apply? reach the default 200000 heartbeat limit. The bounded attempts are recorded in the tool transcript. A distinct proof transports the standard univariate range expansion across optionEquivLeft; its first broad simp attempt hit recursion depth, while explicit transport with an algebra-hom equality succeeds without raising limits. The source keeps the coefficient proof because the transport requires local hom boilerplate and offers no line reduction beyond the direct-support replacement. This also avoids introducing another repository helper. Native branch testing showed the direct term closes the branch; continuation syntax errors came from old multiline body remnants in the single-line replacement mechanism, so the actual module build and complete diagnostics establish the replacement rather than interpreting those syntax errors as term failures.

Correction to initial count: exact before body L92–102 has 11 physical proof lines, not 12; final L92–100 has 9. Both branch lengths are below the structural gate. The theorem including signature is 14 → 12 lines; file 601 → 599. Four deleted proof lines and two added lines, no other source declaration changed. No inline narrative comments existed; docstring preserved byte-for-byte. Casts: 0 dropped, 0 cross-type, 0 load-bearing introduced.

## Independent original type and actual axioms

`/private/tmp/roth-separation-d08-independent.lean` restates the original `coeffNone` definition and exact original expansion statement in `OriginalD08`. Its proof is independent of the target theorem and uses mathlib's `Polynomial.as_sum_range_C_mul_X_pow'`, `natDegree_optionEquivLeft`, and algebra-equivalence transport. An equality-of-proofs check `example : @independent = @Roth.eq_sum_X_none_pow_mul_coeffNone := rfl` verifies the exact original quantified type, relying only on proof irrelevance after definitional equality of the original coefficient definition. Initial check failed solely because the scratch binder order placed R before the inherited index instances; this was corrected to the exact original order and the final compiler run exits 0.

The same final run proves a concrete counterexample to dropping hn: `X none` over `MvPolynomial (Option Empty) ℕ`, bound `n = 0`, cannot equal its constant expansion. It also #checks all newly introduced identifiers. Complete log `/private/tmp/roth-separation-d08-independent.log`; actual built target and independent theorem both report exactly `[propext, Classical.choice, Quot.sound]`. No private declaration was changed or added.

Width-100 compiler reference:

```lean
@Roth.eq_sum_X_none_pow_mul_coeffNone : ∀ {τ : Type u_3} [Fintype τ] [DecidableEq τ] {R : Type u_4}
  [inst : CommSemiring R] (P : MvPolynomial (Option τ) R) {n : ℕ},
  degreeOf none P ≤ n → P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * (rename some) (Roth.coeffNone P ν)
```

| New identifier in source diff | Verification | Result |
|---|---|---|
| `MvPolynomial.notMem_support_iff` | Local search index error, then exact unfiltered source rg at Basic.lean L516 and actual #check | pass |
| `Finset.mem_range` | Actual #check | pass |
| `Nat.lt_succ_of_le` | Actual #check | pass |
| `.trans` | Actual compiled application to the degree inequality | pass |

Existing `monomial_le_degreeOf` is independently #checked as well. No imports, attributes, definitions, theorem signatures, public instances, or documentation changed.

## Simplify and performance passes

Holistic simplify review performed directly: no built-in `/simplify` tool is available in this session. Outcome PASS-THROUGH after the applied branch cleanup. Reconstruction and out-of-range vanishing are already separated into their mathematical cases; factoring a two-line support argument into a new helper would obscure the direct inequality. No duplicated new proof skeleton, unused local, cast bridge, or cross-cutting issue remains in this diff.

Actual module profiling command:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Raw `/private/tmp/roth-separation-d08-final-profile.log`; parser `/private/tmp/roth-separation-profile-table.py`; anchored table `/private/tmp/roth-separation-d08-final-profile.log.json`. Target outer command 26.740 ms + outer async proof 116.512 ms = **143.252 ms**, exactly one anchor of each kind. Nested nodes are not added again. Baseline 137.595 ms → 143.252 ms (+5.657 ms, ~4.1%), within wall-clock noise; no speed improvement claimed. This is below 750 ms resweep threshold and 1000 ms budget. Buzz outcome FAST-BOARD for this target. No limit raises, scaffolding, or outstanding performance fix.

## Gate evidence

| Gate | Result | Concrete evidence |
|---|---|---|
| lake_build_file | pass | Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, 1876 jobs; `/private/tmp/roth-separation-d08-module.log`. |
| Complete unfiltered native LSP | pass | `/private/tmp/roth-separation-d08-final-lsp.json`: partial=false, timed_out=false, success=true, failed_dependencies=[]; 0 errors/31 warnings/0 infos. |
| Definition protection | pass | No def/abbrev/import/attribute changes. |
| Theorem statement protection | pass | Signature and docstring byte-identical; independent exact original-type recovery compiles. |
| Structure | pass | 9 final proof lines, no conjunction, branches 1 and 2 lines. |
| Naming | pass | Descriptive expansion API name with no forbidden patterns. |
| Packing | pass | Every signature line in required 79/32/82-codepoint table above; no next complete component fits. |
| Inequality orientation | pass | hn uses ≤, no reversed occurrence or name. |
| Standard axioms | pass | Actual built target and independent proof each exactly propext/Classical.choice/Quot.sound. |
| Actual target performance | pass | Complete actual-module profile, one outer command and one async proof anchor, conservative 143.252 ms. |
| Source diff hygiene | pass | `git diff --check -- Roth/Separation.lean` exit 0; exact raw diff `/private/tmp/roth-separation-d08.diff`, +2/-4 proof lines. |
| Cumulative/full/LeanEval/publication | parent-owned | Parent runs whole-original compatibility/all retained axioms and sequential full + separate LeanEval builds after this worker freezes; not duplicated here. |

No per-declaration limit, sorry, axiom, native_decide, haveI/letI, suppression, profiling scaffold, import, helper, rename, definition, public type change, or comment deletion was introduced. Phase 5a: no non-rename refactoring beyond the local proof composition. Phase 5b: no rename needed; shared queue untouched. No decomposition or simplify follow-up needed. Header and pending public instance warnings remain for explicitly recorded user decisions, not suppressed.

## Generalisation: every effective binder

Compiler-tested probes use `autoImplicit false`, independent universe parameters u/v, the independent non-self transport proof, and the unchanged original proposition. Full sources and unfiltered outputs: `/private/tmp/roth-separation-d08-probe-*.lean`, `/private/tmp/roth-separation-d08-probes.json`; runner `/private/tmp/roth-separation-d08-probes.py`.

| Binder | Kind / use | Candidate tested | Result |
|---|---|---|---|
| `{τ : Type*}` | Index type throughout polynomial/instances | Drop; explicit independent `Type u` | Drop fails unknown τ; independent universe compiles. Keep universe-polymorphic type. |
| `[Fintype τ]` | Inherited index instance | Drop individually; Finite; drop jointly with DecidableEq | Individual drop, Finite replacement, and joint drop all compile. Keep pending public approval. |
| `[DecidableEq τ]` | Inherited decidability | Drop individually and jointly | Individual and joint drop both compile. Keep pending public approval. |
| `{R : Type*}` | Coefficient type throughout algebra/polynomial | Drop; independent `Type v` | Drop fails unknown R; independent universe compiles. Keep arbitrary coefficient type. |
| `[CommSemiring R]` | Polynomial API and option equivalence | Drop; weaken to Semiring | Both fail to synthesize CommSemiring R in unchanged statement. Keep. |
| `(P : MvPolynomial (Option τ) R)` | Reconstructed polynomial | Drop | Fails unknown P; dependent statement requires it. Keep. |
| `{n : ℕ}` | Exponent range and degree bound | Drop | Fails unknown n. Exponents are natural numbers intrinsically; abstract index restatement changes the theorem. Keep. |
| `(hn : degreeOf none P ≤ n)` | Ensures vanishing above n | Drop | Independent proof fails unknown hn; separate compiled `X none`, n=0 counterexample confirms hypothesis cannot be dropped mathematically. Keep. |

No strict-to-weak candidate remains: hn already has a weak ≤ bound. No global analytic, pointwise, bundled conjunction, topology, completeness, or domain hypothesis exists. Other typeclass-parent catalogue candidates are inapplicable because the unchanged MvPolynomial/rename/coeffNone API needs CommSemiring. Inversion review: the abstract reconstruction is already mathlib's polynomial range expansion; optionEquivLeft packages coefficient collection. No new abstract lemma needed. Universes already independent.

Big-change candidate: omit `[Fintype τ]` and `[DecidableEq τ]`, as already pending in `.mathlib-quality/cleanup/Separation-instance-proposal.md`. No such omission, argument reordering, conclusion restatement, attribute change, or rename has been applied.


Final probe summary: all 11 compiler requests completed and were drained. Drop τ/R/CommSemiring/P/n/hn and Semiring weakening fail for the explicit reasons above; drop Fintype alone, drop DecidableEq alone, replacement Fintype → Finite, and joint omission all exit 0. Positive proposals remain unapplied. Original-branch lia scratch probe `/private/tmp/roth-separation-d08-lia.lean` also exits 0 with log `/private/tmp/roth-separation-d08-lia.log`; the retained proof removes the entire arithmetic-automation branch.

All eleven completion steps:

- [x] Step 1: required references read.
- [x] Step 2: complete 24-item initial audit written before source edits.
- [x] Step 2.5: all five actual searches, auxiliary variants and common-equivalents scan.
- [x] Step 2.6: every effective binder and public literature search.
- [x] Step 2.7: complete measured initial/final signature table and width-100 #check.
- [x] Step 2.8: per-occurrence inequality table.
- [x] Step 3: concrete status for all 42 golfing rules.
- [x] Step 4: step-back review and actual automation/exact?/apply? attempts.
- [x] Step 5a: complete unfiltered successful native LSP.
- [x] Step 5b: actual module, independent original type/proof, actual axioms, profile and diff gates.
- [x] Step 6a: no rename needed; dedicated report complete, shared rename queue untouched.

Final result: two proof lines saved, anonymous have and omega removed; 27 retained declarations, no helpers introduced, original public contract and all documentation preserved. Source 601 → 599 physical lines, worker diff +2/-4. Pending proposal remains public index-instance omission only.

Freeze: all native Lean/MCP and compiler/module/profile/probe requests have completed and been drained. Source SHA256 `24c37da51aee81b82da351937cb595a67679f2f566d475e8b72aecccad1a8a16`. I explicitly revoke **ALL source ownership**, including Roth/Separation.lean and all other source files. I am now **report-only** and will make no source edits. Parent may run its fresh whole-original/public/actual-axiom compatibility probe, then sequential full and separate LeanEval builds and publication.

## Owner cumulative publication gates

Source FROZEN SHA256 `24c37da51aee81b82da351937cb595a67679f2f566d475e8b72aecccad1a8a16`; leaf ownership revoked and requests drained before owner gates. Owner probe `19855` exit0,41.30s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d08-compatibility.{lean,log,json}`. Owner build session `64974` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,113.98s/26.46s; source hash stable. `/private/tmp/roth-separation-d08-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
