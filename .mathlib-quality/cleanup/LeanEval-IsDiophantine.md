# Single-declaration cleanup: `IsDiophantine`

Scope: `Roth/LeanEval.lean`, original lines 11–13, declaration 1/3. Fresh single-declaration worker; no Git, central progress, rename queue, or other declaration changes. Full installed mathlib-quality/Lean4 skills, cleanup/cleanup-all commands, full Phase 4 worker instructions, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style-rules, naming-conventions and profiling references read. The unavailable built-in `simplify` was not invoked; this independent audit and the later fresh file-final review are the authorized substitute.

## Baselines and change

Before any Lean/golf, genuine initial file from git `d2eb5e9a1806e12e66db25d15d8954ade4be9874` and current entry were saved separately in `/private/tmp/roth-eval-is-diophantine/{original,entry}.lean`. SHA256 respectively `e95c44ae19345ef1514a59ca5e8b182247e9a32aaf4b7d39f0ce57ae5ed27f56` and `610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca`. They are different files; their target definition source is byte-identical. No equality of other original/current declarations is asserted.

Added a precise two-line docstring explaining the uniform lower bound on the error scaled by `q ^ (2 + ε)`. Inverting exactly that insertion recovers the complete entry file byte-for-byte. Definition/signature/body tokens, both public theorem users, imports, metadata and pins are unchanged. Final Eval SHA256 `7e528eb63d7b06616dcb0cd72c3383cc8e433c44d60aa91104a94da4944f2eb0`. Source declaration remains 3 lines; documentation adds 2 file lines (60 → 62).

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Complete unfiltered fresh Eval LSP after initial doc insertion: success, nonpartial, no timeout, no failed dependencies, no diagnostics. Final precision revision is qualified by exact comment insertion inverse; final prefix compile also clean. |
| 2 | HAVE SCAN | n/a: no `have` in this Prop-valued definition. |
| 3 | SET_OPTION | None; defaults retained. |
| 4 | SIMP SQUEEZE | n/a: no simp/tactic calls. |
| 5 | NAMING | `IsDiophantine` names the external Prop predicate; UpperCamelCase predicate name, no forbidden abbreviation/pattern. No rename warranted. Existing project queue of 5 remains owner's later global task. |
| 6 | LINE PACKING | Single signature line, 35 codepoints; table below. No unjustified signature break. |
| 7 | BY PLACEMENT | n/a: term definition, no `by`. |
| 8 | FORMAT | Two-space definition continuation; no blank lines inside, trailing whitespace or tactic chains. |
| 9 | COMMENTS | No original declaration comments; none removed. |
| 10 | DOCSTRING | Missing on public def; added scaled-error interpretation, one sentence over two lines. |
| 11 | VISIBILITY | Public external LeanEval predicate is used by equivalence and headline theorem, an API contract; keep public. |
| 12 | STRUCTURE | Two-line Prop body, no proof branches. Its existential conjunction defines one mathematical predicate; theorem-conjunction splitting does not apply and would change the external contract. No helper warranted. |
| 13 | MATHLIB | Five-method findings below; preserve exact external predicate. Related upper-approximation predicates do not replace its definition. |
| 14 | JUNK DEF | Not junk: named external mathematical predicate, two public theorem users and characterization API. |
| 15 | EXISTS LEMMA | n/a: not private existential witness theorem. |
| 16 | SHOW/CHANGE | n/a: neither present. |
| 17 | PUSH_NEG | n/a: none. |
| 18 | GENERALISE | Per-binder table below; no theorem hypotheses to mechanically weaken, no safe public contract change. |
| 19 | INEQUALITY | All four body inequalities use `<`; signature has no reversed inequality; table below. |
| 20 | NORMAL-FORM | Canonical external lower-bound condition preserved. `isDiophantine_iff` already relates it to the exponent bound, avoiding a network of redundant equivalences. |
| 21 | SYNTAX-GEN | OK: callers obtain ε-dependent C and bound directly; no easier equivalent public restatement required. |
| 22 | IMPORT-FANOUT | n/a: no imports added. |
| 23 | CASTS | Diff: 0 dropped / 0 kept cross-type / 0 kept load-bearing (documentation only). Existing p/q ℤ→ℝ casts are genuine cross-type; `2 : ℝ` fixes the real exponent; untouched. |
| 24 | INSTANCE-NAME | n/a: not an instance and no instances introduced. |

Issues found: one missing docstring; fixed. Refactoring needed: none. No optional API expansion.

### Line packing

Reference: n/a — definition. Signature ends at `:=`, before the Prop expression.

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| `def IsDiophantine (x : ℝ) : Prop :=` (final L13) | 35 | none; term body next | n/a: only signature line | ok |

### Inequality scan

| Location | Original/rewrite | Result |
|---|---|---|
| Signature | n/a — no `≥`/`>` | pass |
| Body ε hypothesis | `0 < ε` unchanged | smaller side left |
| Body C condition | `0 < C` unchanged | smaller side left |
| Body q hypothesis | `0 < q` unchanged | smaller side left |
| Approximation inequality | `C / ... < abs ...` unchanged | smaller side left |

### Mathlib search-status

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | real Diophantine approximation, every positive epsilon, positive C, lower bound C/q^(2+ε) | `LiouvilleWith`, `Liouville`, `LiouvilleWith.exists_pos`: frequent upper approximations, different polarity/quantifiers. |
| B Loogle | `"Diophantine"` | Empty successful response. |
| C LeanSearch | Diophantine real irrationality measure at most two lower rational approximation bound | `Irrational.eventually_forall_le_dist_cast_rat_of_den_le`, denominator-bounded variants: finite-denominator separation, not uniform exponent predicate. |
| D Source | `IsDiophantine`, `Diophantine`, `irrationality` in NumberTheory/DiophantineApproximation and Transcendental/Liouville | Read `LiouvilleWith` definition; no identical predicate found in these files. |
| E Name pattern | `Diophantine`, `IsDiophantine` | First index unavailable; subsequent warming index returned local predicate and equivalence plus unrelated diffeomorphism names. Not certified exhaustive absence. |

Auxiliary variants: `LiouvilleWith.exists_pos`, irrational `eventually_forall_le_dist_cast_div_of_denom_le`, `..._of_den_le`. Common-equivalents table: no matching discrete/finite/bounded-wrapper bucket. Six replacement rules checked: no wrapper lemma, no substitute typeclass found, no deletion/replacement warranted, auxiliary variants inspected, no new mathlib dependency to document. This is preservation of an externally required definition, **not a claim of exhaustive mathlib absence**. Compiled `exact?`/`apply?` absence probes are n/a: a definition constructs a proposition, rather than asserting it, and no new theorem/definition is being written or absence claimed. Tactics proving arbitrary `Prop` would not test equality to this predicate.

### Generalisation status and literature

| Binder | Class/use | Catalogue candidates | Verification/result |
|---|---|---|---|
| `(x : ℝ)` | structure value, target of rational approximation | Drop would leave x unbound or change predicate arity; abstract field changes real exponent/absolute value contract | No safe candidate; retain. |
| `ε : ℝ`, `0 < ε` | internal universal binder and hypothesis defining exponent range | Dropping binder or allowing ε=0 changes predicate; not a theorem hypothesis weakening | n/a: mathematical definition content; retain. |
| `C : ℝ`, `0 < C` | internal existential witness and positivity | Removing positivity permits degenerate bound and changes meaning | n/a: not a removable assumption; retain. |
| `(p q : ℤ)`, `0 < q` | internal quantifiers and positive denominator | Abstract/natural denominators or dropping q positivity restates external predicate | No small safe change; retain. |

No typeclass, decidability, universe, global continuity/pointwise, or bundled theorem hypotheses. Inversion check: n/a, definition specifies the object; no proof outruns a concrete statement. No literature-driven API change recommended.

Public literature search: query `Roth theorem diophantine approximation epsilon constant lower bound generalization`. Top three hits recorded: [Columbia Diophantine Approximation notes](https://www.math.columbia.edu/~ums/Diophantine-Approximation.pdf), [Evertse's Notes on Diophantine Approximation](https://www.math.leidenuniv.nl/~evertsejh/Roth.pdf), [BIRS Diophantine Approximation and Algebraic Curves report](https://archive.birs.ca/files/2017/17w5045/report17w5045.pdf). Evertse's search excerpt states the positive-constant bound for exponents κ>2; this supports the present real positive-ε formulation. More general number-field/place settings change the problem's objects and are outside this exact external real-number contract. Search snippets only were consulted, not claimed as full-paper review. ChatGPT math MCP unavailable.

## All 42 golfing rule statuses

Each n/a is specific to the actual term definition, not a failed proof experiment.

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no tactic wrapper. |
| 1.2 by rfl | n/a: no rfl proof. |
| 1.3 rw + exact | n/a: no rewrites/proof. |
| 1.4 simp + exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: no simp/rfl. |
| 1.6 constructor chain | n/a: conjunction specifies predicate, not a constructor proof. |
| 1.7 apply + exact | n/a: no proof calls. |
| 1.8 by_contra + push_neg | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: no lambda application wrapper. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply + intro | n/a: no tactic block. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have projections | n/a: no have/projections. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: no simp. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | n/a: no theorem applications. |
| 1.18 less parentheses | n/a: parentheses fix types/group real exponent; no nested application wrapper. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 inline existential lemma | n/a: not an existential theorem. |
| 2.1 grind whole proof | n/a: defines Prop rather than proving it. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa consolidation | n/a: no simp/closing tactics. |
| 2.4 fun_prop | n/a: no analytic property proof. |
| 2.5 positivity | n/a: positivity conditions define predicate, not proof goals. |
| 2.6 gcongr | n/a: inequality is definition content, not a goal. |
| 2.7 lia/omega | n/a: no arithmetic proof. |
| 2.8 aesop | n/a: no asserted proposition to prove. |
| 2.9 norm_num/norm_cast | n/a: no numerical/cast proof. |
| 2.10 decide | n/a: arbitrary real quantified predicate, not finite computation. |
| 2.11 field_simp/ring | n/a: no identity proof. |
| 2.12 linear_combination | n/a: no ring proof/hypotheses. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 close goals with <;> | n/a: no subgoals. |
| 3.1 erw → rw | n/a: neither. |
| 3.2 fun_prop replacement | n/a: no legacy analytic tactics. |
| 3.3 omega → lia | n/a: neither. |
| 3.4 rcases with rfl | n/a: no case split. |
| 3.5 automation attributes | n/a: predicate is exact external contract, no new theorem to register. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 remove resource option | n/a: none; defaults confirmed. |

Step-back review: this term is already the direct mathematical proposition. There is no shorter proof to search for, no redundant intermediate fact, and no helper to extract. Keep exact external definition; document its intended interpretation.

## Correctness gates and evidence qualifications

Actual Eval environment families were enumerated before guards: `IsDiophantine[]`, `IsDiophantine._proof_1[]`, `isDiophantine_iff[]`, `isDiophantine_iff._simp_1_1[u_1]`, `thueSiegelRoth[]`. Target family exactly two constants. Fresh prefix guard enumerates actual family before any guard and checks both constants (one run_cmd per costly check). Strict recursive Expr comparison covers names, binder information, levels, metadata and syntax; raw TYPE and universe strings also checked against saved actual entry metadata, not Expr BEq. Original source target bytes equal entry, so that baseline applies to the genuine original target too. Default resources 200000/20000/512, actual opaque `value! true`, inferred VALUE type, closure, standard axioms, exact VALUE hash/length and direct upstream origins checked. Hash/length evidence is not claimed to be full raw VALUE equality.

| Constant | TYPE bytes | VALUE bytes | VALUE hash | Axioms |
|---|---:|---:|---|---|
| IsDiophantine | 108 | 5901 | 15408651368986333937 | propext, Classical.choice, Quot.sound |
| IsDiophantine._proof_1 | 950 | 644 | 1908684697056394220 | propext |

Actual direct dependency graph: predicate → its generated `_proof_1`; generated proof → upstream Mathlib/Lean only. Neither has self-dependencies, no backward edge, so family is acyclic. No sorry, new axiom, conclusion weakening, resource raises, or scaffolding in source.

| Gate | Result/evidence |
|---|---|
| lake_build | Qualified reuse of actual `lake build` exit0, 33.967s, `/private/tmp/roth-main-final/closing-full-build-{launch,terminal}.json`. |
| lake_build_file | Qualified reuse of subsequent separate `lake build Roth.LeanEval` exit0, 35.280s, `closing-Eval-build-{launch,terminal}.json`. Correct full→separate order retained. Not a new invocation. |
| native current source | Qualified reuse of closing Eval31.275s/root28.916s and Main30.691s checks, same executable source/import/tool hashes; plus new current-prefix semantic/profile compile. |
| diagnostics | Complete unfiltered fresh first-doc Eval LSP clean; closing Main/Eval/root LSP evidence reused for identical executable source. Final-doc comment-only inverse bound; no final-doc LSP invocation invented. |
| definition_protected | pass: all definition source bytes unchanged, including signature. |
| theorem_statement_protected | pass: both theorem sources untouched. |
| structure_gate | pass: short predicate definition; splitting defining conjunction is inapplicable. |
| naming_gate | pass: mathematical predicate name, no forbidden pattern/abbreviation. |
| line_packing_gate | pass: complete single-line signature table. |
| inequality_orientation_gate | pass: zero reversed inequalities. |
| cumulative external breakage | Qualified pass: exact inverse insertion, unchanged executable source and all prior 40 timing inputs except this documented source delta; no new identifiers in code. |

The reuse is authorized pure-documentation reuse, not certification from an old build without binding. `source-binding.json` records exact inverse insertion; fresh profile compares all prior 40 frozen input hashes and finds only Eval documentation changed. Copyright/license metadata untouched. Later file-final worker independently profiles entire Eval; this worker does not claim file-final completion.

## Buzz/performance

Outcome FAST-BOARD, no fix/deferral. Exact final-source prefix derivative (`Prefix.lean`) preserves imports, namespace/options and both generated family members. Canonical command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-eval-is-diophantine/Prefix.lean`. Stdout/stderr separate; default resources verified by target guard; no options raised.

| Disjoint target root | ms |
|---|---:|
| Outer Elab.command | 25.092 |
| Generated proof kernel async parent | 0.653 |
| Definition kernel async parent | 0.145 |
| Compile async parent | 0.040 |
| Lint async parent | 16.656 |
| Conservative charge: 20 top-level Meta.whnf roots | 0.030 |
| Total | **42.616** |

Actual lazy DATA declaration roots: none observed. The 20 Meta.whnf roots are Meta roots conservatively charged here, not DATA declarations. No separate async proof elaboration root beyond the enumerated roots. Nested header/value/addDecl/Kernel/Compiler/overlappingInstances times not double-counted. The full canonical target command in raw stdout lines184–188 equals the final source command after whitespace normalization, and the derivative equals the exact source prefix plus namespace close (`timing.json`). Canonical cumulative stderr categories retained separately; not added to target roots. Import20.6s and cumulative interpretation832ms are not target declaration times. Actual total<750ms, so no repeat required. No unchanged third sample.

Owner explicit HOLDACK before preparation/capture, then actual compiler/driver PID+PGID absent, frozen source/inputs equal, raw UNPARSED drain message, then owner RELEASE before parsing. `profile-terminal.json`, `profile-drain.json`, `profile-launch.json`, `timing.json` retain actual evidence. Child `lake env` full bytes compared in memory before/after: equal; only hash/length and allowlisted PATH retained. This does not assert parent-process full-environment equality.

## Worker result and checklist

3 source lines → 3 source lines; 2 documentation lines added. Audit findings1/fixed1; no refactoring deferred, rename requests0; no original comments removed. Gates pass with explicitly qualified unchanged-executable-source reuse. Simplify unavailable; independent audit complete, later fresh file-level reviewer remains owner's workflow.

- [x] Step1 required references read.
- [x] Step2 all24 audit items.
- [x] Step2.5 five-method search-status, with honest unavailable/warming qualification.
- [x] Step2.6 per-binder generalisation and public literature search.
- [x] Step2.7 complete signature width table.
- [x] Step2.8 inequality scan table.
- [x] Step3 all42 rule statuses.
- [x] Step4 step-back reflection; exact?/apply?/automation inapplicability justified.
- [x] Step5a complete clean diagnostics evidence with doc-only qualification.
- [x] Step5b explicit gates, semantic and performance receipts.
- [x] Step6a no rename needed; shared queue untouched.

Final exact-doc semantic guard: actual exit0 in47.233s, empty stderr; source-ordered hash binding and exact family/DAG/drain in `semantic-receipt.json`. The first semantic compile before doc-precision revision was redundant in hindsight and is retained honestly; no further inference/profile replay follows.
