# Cleanup: `Roth.eq_mapDomain_some_add_single`

Dedicated original-d02 worker, owner-supplied starting HEAD `8b0dcd7`. Only this theorem's proof is edited; no Git operations. Original source `/private/tmp/roth-separation-original.lean`; starting proof already incorporates original-d01's direct library replacement. Both public instance parameters and all existing documentation are preserved. Their removal is a separate pending user decision in `Separation-instance-proposal.md`.

Read both skills, full installed cleanup instructions, golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md and relevant style/naming/profiling references. No subdelegation. Parent supplied green baseline full/separate LeanEval builds and complete LSP 0 errors/32 warnings.

## All 24 audit items

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | Three target warnings: unused section instances, unused DecidableEq in type, unused Fintype in type. Both omissions independently compile but remain pending user approval; no suppressions. |
| 2 | HAVE SCAN | No have in original or final proof. |
| 3 | SET_OPTION | No scoped option or raised limit. |
| 4 | SIMP SQUEEZE | Both original simp calls close their branch; final shared simp closes both branches. Unsqueezed terminal simp retained. |
| 5 | NAMING | eq_mapDomain_some_add_single describes equality, domain map, injection and single summand; embedded camelCase references actual mapDomain API. No forbidden abbreviation, numbered scheme or ge/gt name. No rename. |
| 6 | LINE PACKING | Two signature lines, measured below; next conclusion does not fit with first line. |
| 7 | BY PLACEMENT | by stays at end of conclusion line. |
| 8 | FORMAT | Two-space tactics, wrapped simp continuation; no empty proof line, trailing spaces, haveI or letI. |
| 9 | COMMENTS | No proof comments existed; docstring preserved byte-for-byte. |
| 10 | DOCSTRING | Public theorem has a concise interpretation of multi-index splitting; preserved. |
| 11 | VISIBILITY | Public API is frozen; retain visibility. General Finsupp decomposition is reusable beyond its two current local uses. |
| 12 | STRUCTURE | Six original proof lines become three; no conjunction or long branch. No helper extraction necessary. |
| 13 | MATHLIB | Five actual searches below locate restriction/Option equivalence and pointwise mapDomain API. No exact additive mapDomain decomposition found; retain pointwise extensional proof built directly from library lemmas. |
| 14 | JUNK DEF | n/a: theorem, no definition. |
| 15 | EXISTS LEMMA | n/a: public equality, no existential witness. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every effective binder audited below. Generic coefficient monoid and omission candidates compiled independently; no public contract change applied. |
| 19 | INEQUALITY | No inequality in signature or hypotheses; scan below. |
| 20 | NORMAL-FORM | Equality splitting a Finsupp at distinguished none; pointwise equality canonical for extensional verification. Existing optionEquiv uses update/embDomain, a related representation rather than this additive expression. |
| 21 | SYNTAX-GEN | Current RHS explicitly exposes additive multi-index needed by subtraction and coefficient callers. Switching to optionElim would require caller rewrites, with no immediate application advantage. |
| 22 | IMPORT-FANOUT | n/a: no imports added. |
| 23 | CASTS | No casts or type ascriptions introduced by diff. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues fixed: duplicate Option branch simplification merged; three proof lines saved. Refactoring needed: pending public instance-removal decision remains with parent. No new declaration, rename or decomposition flag.

## Line packing

Width-100 `#check @D02.original` is captured in verification log; explicit original effective type is reconstructed independently, with both original instance arguments.

| Signature line | Codepoints | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| L50 | 58 | complete conclusion `d = ... := by`, 72 chars excluding indentation | 58 + 1 + 72 = 131 > 100 | ok |
| L51 | 76 | none: proof body follows | n/a | ok |

The equality is a single syntactic conclusion unit; appending just `d` to the first line would split an expression without packing a binder or conclusion. Proof lines L52–54 measure 7,54,87 codepoints. Signature byte-identical before/after.

## Inequality scan

| Location | Original | Rewrite | Rename |
|---|---|---|---|
| Whole signature and all hypotheses | n/a: no ≥ or > occurrence | none | none |

## Generalisation status: every effective binder

| Binder | Class | Use / catalogue candidates | Verified result |
|---|---|---|---|
| `{τ : Type*}` | type variable | Domain of Option/Finsupp; already universe polymorphic. Drop would leave unbound τ; Sort cannot be Finsupp domain. | Retain; universe-separated generic test succeeds. |
| `[Fintype τ]` | typeclass | No finite ambient domain used. Drop is weaker than Finite replacement. | Independent generic proof omits it entirely; pending user approval, original retained. |
| `[DecidableEq τ]` | decidability | No computational instance needed in statement. Drop with local classical. | Independent generic proof omits it; pending user approval, original retained. |
| `(d : Option τ →₀ ℕ)` | structure value | Subject of equality, cannot drop d while retaining statement. Concrete coefficient ℕ → arbitrary `[AddCommMonoid M]`; no order, arithmetic, multiplication used. | Generic proof independently compiles with arbitrary M and no finite/decidable assumptions. Public coefficient restatement is a separate larger API proposal, not applied. |
| `{R}`, `[CommSemiring R]` | inactive section variables | Neither appears in effective target type; no extra hypothesis to remove. | Original effective type confirms absence. |

Point localisation, strict→weak, algebraic parent-class weakening of an existing coefficient class and conjunction unbundling are n/a: there are no such hypotheses. Binder deletion necessity is syntactic for τ and d; not claimed as a failed compilation test. Inversion check: concrete ℕ is unnecessary; arbitrary coefficient monoid retains the same coordinate argument. No concrete named witness is unfolded.

## Literature search (public theorem)

Actual WebSearch query: `finitely supported function Option direct sum decomposition arbitrary additive monoid`. Top three results: [IsarMathLib finite support](https://isarmathlib.org/FinSupp_ZF.html), a mirror of Mathlib.Algebra.DirectSum.Finsupp, and [official mathlib Finsupp/direct sum documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/DirectSum/Finsupp.html). Primary formal-library sources support the inference that finite support concerns support rather than finiteness of the ambient index type, and additive monoids support such decompositions. The local primary implementation `Mathlib/Data/Finsupp/Option.lean` gives `optionEquiv` already with only Zero M, and its additive operations require AddZeroClass. This suggests the tested AddCommMonoid coefficient version; mapDomain itself requires commutative addition. No claim of a separately named paper theorem.

ChatGPT mathematical MCP: unavailable in ALL_TOOLS; similarly named ChatGPT Space editing tools do not provide mathematical consultation. No external message sent. Literature-driven candidates: generic coefficient monoid (public conclusion restatement, not applied); removal of finite/decidable instances already covered by parent's pending menu.

## Five actual mathlib search methods

Raw native results `/private/tmp/roth-separation-d02-{finder,loogle,leansearch,names}.json` and full source search `/private/tmp/roth-separation-d02-source-search.log`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | finitely supported function Option decomposition mapDomain some single none | Finsupp.some, optionElim, optionEquiv; related representations. |
| B Loogle | Finsupp.some, Finsupp.mapDomain | Empty items; no matching indexed theorem returned. |
| C LeanSearch | finitely supported function option equals restriction to some plus single none | some_single_some, optionEquiv, optionEquiv_apply. |
| D Source | eq_mapDomain_some_add_single; mapDomain.*some.*single; single.*none.*some; optionElim_some; optionElim_add | No exact name; Option reconstruction and additive API found; full untruncated output saved. Basic.lean embDomain_eq_mapDomain checked separately. |
| E Name pattern | some (limit20), then Finsupp.optionElim (limit30) | Verified related Option API. Index warming, so empty results would not establish absence. |

Auxiliary variants considered: optionElim_some, some_optionElim, some_embDomain_some, embDomain_some_none, embDomain_some_some, optionElim_add, optionEquiv_apply, embDomain_eq_mapDomain. Common-equivalents lookup: none of topology/finiteness/bornology buckets apply. Conclusion: related reconstruction exists as optionElim_some, but no direct additive mapDomain equality identified. Retain the target, composing pointwise mapDomain lemmas; no new wrapper/API extraction. No claim of exhaustive mathematical absence. `exact?` failed and `apply?` suggested extensionality in the live proof; these do not certify absence from mathlib, since live context includes the project.

## All 42 golfing rules

Initial multi_attempt at conclusion L51 was mispositioned and returned parser errors; these are invalid probes, not automation failures. Corrected L52 probes genuinely tested rfl/simp/grind/aesop/exact?; all failed to close. apply? produced extensionality suggestions. A multiline replacement also left stale original branch syntax because multi_attempt replaces a tactic span, not the complete proof. These discarded parse artifacts are explicitly excluded. A standalone complete candidate then compiled via native run_code with success=true, timed_out=false and no diagnostics before contextual edit.

| Rule | Concrete status |
|---|---|
| 1.1 by exact | n/a: no by-exact wrapper. |
| 1.2 by rfl | n/a: original uses ext/cases/simp. |
| 1.3 rw + exact | n/a: no rw or exact. |
| 1.4 simp + exact | n/a: simp closes both branches. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 constructor pairs | n/a: equality, no constructor pair. |
| 1.7 apply + exact | n/a: no such chain. |
| 1.8 contradiction + push_neg | n/a: no contradiction. |
| 1.9 eta reduction | n/a: no lambda. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply + intro | n/a: no such chain. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have + projections | n/a: no have. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: original terminal simp already unsqueezed. |
| 1.16 nonterminal simp | n/a: all simp calls terminal in branches. |
| 1.17 dot notation | n/a: explicit injection theorem argument is clear; no receiver application shortened. |
| 1.18 trailing parentheses | n/a: parentheses group injection proof inside simp theorem application. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential | n/a: no existential. |
| 2.1 whole grind | Correct live probe failed; keep ext/cases/simp. |
| 2.2 delete pre-grind | n/a: retained proof has no grind. |
| 2.3 simpa | n/a: no closing external fact after simp. |
| 2.4 fun_prop | n/a: no function regularity property. |
| 2.5 positivity | n/a: no order or positivity goal. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: coordinate identification, no arithmetic proposition requiring solver. |
| 2.8 aesop | Correct live probe failed to close. |
| 2.9 norm_num/cast | n/a: no numeric calculation or coercion. |
| 2.10 decide/kernel | n/a: equality of arbitrary Finsupp data, not finite computation. |
| 2.11 field_simp/ring | n/a: no division/ring expression. |
| 2.12 linear_combination | n/a: no ring endpoint or hypotheses. |
| 2.13 wlog | n/a: none and some cases are structurally different, not symmetric. |
| 2.14 term calc | n/a: no calc. |
| 2.15 shared <;> close | Applied: cases o <;> simp shares the two terminal branch computations. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 fun_prop migration | n/a: no legacy continuity/measurability. |
| 3.3 omega→lia | n/a: no arithmetic solver in target. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 attributes | No simp attribute: rewriting every arbitrary Finsupp into two terms would expand rather than normalize. No grind attribute requested. |
| 3.6 simp_all | n/a: no simp_all only or hypotheses to normalize. |
| 3.7 options | n/a: no limit option. |

## Step back / simplify review

rfl, bare simp, grind and aesop do not close; exact? found no complete proof. Option extensionality is the natural argument: at none the mapped restriction vanishes, and at some j injection recovers the original coordinate. The branch-specific simp lists can be combined into one shared list without changing reasoning. Existing Option equivalence uses a different reconstruction, and converting via it adds update/embedding plumbing. Three proof lines need no helper. Built-in simplify tool is unavailable; in-thread holistic review found no further reuse/quality/performance issue. Outcome PASS-THROUGH after the shared-branch edit; no extra source modifications.

## Verification and gates

- Native complete unfiltered LSP: `/private/tmp/roth-separation-d02-lsp.json`, success=true, partial=false, timed_out=false, 0 errors,32 unchanged warnings. Three target warnings are the explicit pending instance-removal proposal; other declarations remain outside scope. Header warning preserved per owner/user decision. No sorry diagnostic.
- Actual module command `lake build Roth.Separation`, session63738 exit0; `/private/tmp/roth-separation-d02-build.log` ends `Build completed successfully (1876 jobs)`.
- Independent original statement and six-line coordinate proof in namespace D02, plus actual `@original = @Roth.eq_mapDomain_some_add_single := rfl`, compiled in `/private/tmp/roth-separation-d02-verify.lean`, final session28197 exit0. This checks original effective type and proof-irrelevance identity while independently proving the statement. Original proof does not call target. First draft accidentally used unknown pp.width; corrected to format.width before successful gate. Failed draft is excluded.
- Actual built target `#print axioms` returns exactly propext, Classical.choice, Quot.sound. Generic arbitrary-coefficient candidate also has only these axioms. Raw verification log `/private/tmp/roth-separation-d02-verify.log`.
- No new identifiers: moved library names all already occur in original theorem. No changed definitions, public statement, imports or docstrings. Automated exact original-signature and docstring comparison passes.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual lake build Roth.Separation session63738 exit0 |
| definition_protected | pass | no def/abbrev edits |
| theorem_statement_protected | pass | exact original signature comparison and independent original-contract example |
| structure_gate | pass | three-line body, no conjunction or long branch |
| naming_gate | pass | descriptive name, no forbidden pattern; no rename queue entry needed |
| line_packing_gate | pass | full two-line table above, both rows ok |
| inequality_orientation_gate | pass | complete zero-occurrence table above |
| trust/limits | pass | standard actual axioms; no sorry, axiom, limit, haveI or letI added |

Full-project, separate LeanEval, cumulative callers, Git commit and push remain parent-owned sequential final gates before dispatching next original declaration; this worker does not assert those have already run for its edit.

## Buzz: budget1000ms

Native lean_profile_proof failed standalone extraction (`unexpected end of input`) and is not used as timing evidence. Plain profiler aggregate categories are saved in `/private/tmp/roth-separation-d02-profile.log`, session23252 exit0, but are not attributed to a theorem.

Actual anchored trace command:

```text
lake env lean -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-separation-d02-profile.lean
```

Session87396 exit0. Raw `/private/tmp/roth-separation-d02-anchored-profile.log` explicitly anchors final source-extracted independent target `D02Profile.eq_mapDomain_some_add_single`: outer Elab.command10.682ms plus proof Elab.async67.831ms = conservative78.513ms, with kernel replay1.912ms additionally if counted separately. Nested Elab.definition.value66.227ms is not added again. All well below750ms; no borderline repeat needed. Imported original theorem is not used in the profile proof. FAST-BOARD; no performance fix, over-budget deferral, raised limit or repository profiling scaffolding.

## Result / all eleven Phase-4 steps

Original effective signature and documentation preserved. Proof six→three lines; declaration eight→five lines, saving3. File616→613lines. Rule2.15 applied. No proof comments existed. No renames queued. Pending public-instance decision reported, no unauthorized omission.

- [x] Step1 references read.
- [x] Step2 all24 audit items recorded.
- [x] Step2.5 five actual search routes and auxiliary variants recorded.
- [x] Step2.6 every effective binder and public literature search recorded.
- [x] Step2.7 every signature line measured.
- [x] Step2.8 inequality occurrence table recorded.
- [x] Step3 all42 rules recorded.
- [x] Step4 holistic reflection and complete candidate verified.
- [x] Step5a complete unfiltered native LSP, no errors/sorries.
- [x] Step5b actual module and trust/contract/diff gates pass.
- [x] Step6a no rename, no sidecar mutation necessary.

All Lean requests and compiler sessions drained. ALL SOURCE OWNERSHIP REVOKED; report-only from this point. Frozen Roth/Separation.lean SHA256 `92ffb3a092b9a23fdedc0da16bdd954f57d4c979ddf469b1d4f36cefc8c20278`.

## Owner cumulative gates and actual module profiling

Owner14103exit0 freshly re-proves the entire ORIGINAL30 declarations in another namespace,recovers all20 original public type/value equalities and checks ALL29 actual retained standardaxiom sets. `/private/tmp/roth-separation-d02-compatibility.{lean,log,json}`. Owner22880 sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,122.05s/30.04s; source SHA before/after unchanged. Logs `...-full.log`, `...-leaneval.log`, `...-builds.json`.

Owner2444exit0 runs the actual repository module with `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`. Exact actual target anchors command14.840ms,asyncproof83.286ms,total98.126ms,below750ms; `/private/tmp/roth-separation-d02-actual-profile.log{,.json}`. This supplies actual-module evidence in addition to the worker's standalone source-extracted78.513ms. Hash remains frozen. Exact diff/docs/whitespace checked; exact-path commit and successful cleanup-branch push precede next declaration.
