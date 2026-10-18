# exists_separated_representation — final approved-instance revisit, initial audit

Before source edits: HEAD 742eecd, clean worktree, source target lines 290–325, 30 proof-body lines. Actual supplied baseline `/private/tmp/roth-separation-r08-profile-final.log{,.json}`: 30.910 + 784.046 = 814.956 ms; reconstruction helper 699.921 ms. User approved removing both ambient Fintype τ and DecidableEq τ; this revisit owns only that scoped omission and this report. Both wrapper removals and Domain coefficient weakening were declined. Nat codomain and all other public contracts stay fixed. Two retained helpers were freshly independently audited; the degree helper was removed after its audit. No helper edits or new helpers permitted.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, both skills and the worker contract. Relevant style, naming and profiling references read. The argument chooses a basis of the finite span of the n+1 coefficient polynomials, proves that span nonzero, bounds its dimension, and reconstructs P using basis coordinates. Independence and reconstruction use the two audited helpers; support restriction gives every remaining-variable degree bound. The finite family is Fin (n+1), so τ itself need not be finite.

1. LINT: live pre-edit goal confirms both ambient instances. Complete diagnostics to follow; supplied previous complete LSP is the baseline.
2. HAVE SCAN: anonymous finite-dimensional evidence is an instance used repeatedly; hP' is used in positivity and reconstruction; hl1 has a nonzero witness proof; hdegree is a deliberately typed span inclusion whose inlining was previously profiled slower. Keep all four.
3. SET_OPTION: none in target.
4. SIMP: terminal simp only in contradiction has an existing measured performance exemption; terminal simpa for support bound stays; no nonterminal bare simp.
5. NAMING: exists_separated_representation describes the existential independent separation, has no forbidden abbreviation, scheme number or _ge_/_gt_; no rename needed.
6. LINE PACKING: exact mathematical signature remains unchanged; complete codepoint table below after final check.
7. BY PLACEMENT: attached to statement.
8. FORMAT: two spaces, no blank lines in declaration, ordinary lambdas use ↦; no haveI/letI.
9. COMMENTS: no original proof comments; preserve original docstring verbatim and attach omit before it.
10. DOCSTRING: existing statement/source attribution is protected.
11. VISIBILITY: main public theorem, retain public API.
12. STRUCTURE: prior 64-line proof already decomposed to 30 lines plus two independently audited helpers; no >10-line branch. Refactoring needed: /decompose-proof flag retained for the >15-line headline and conjunctions, with no further helper extraction authorized in this focused revisit.
13. MATHLIB: fresh native Finder/Loogle/LeanSearch searches succeeded; local name search found finrank_range_le_card with warming index. Source and generic-route probes below. Partial matches supply basis/span machinery, not the complete separation result.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: substantial public representation theorem, not a trivial witness wrapper.
16. SHOW: none.
17. PUSH_NEG: none; existing by_contra! retained.
18. GENERALISE: apply exact approved pair omission; independently compile arbitrary-τ proof, all effective binder probes and original full binder-order adapter. No coefficient/Field weakening applied.
19. INEQUALITY: hn and all four degree/dimension bounds use ≤; no ≥/> in code signature. Table below.
20. NORMAL-FORM: separated factors with both families independent and degree bounds are the intended coefficient-rank form.
21. SYNTAX-GEN: Fin l matches determinant consumers; no restatement needed.
22. IMPORT-FANOUT: n/a, no import changes.
23. CASTS: Fin→Nat and basis subtype→MvPolynomial coercions are real; expected types pin X and support inclusion. Omission adds no casts.
24. INSTANCE-NAME: n/a, no declared instance; local anonymous finite-dimensional evidence stays anonymous.

Initial action: insert `omit [Fintype τ] [DecidableEq τ] in` immediately before original docstring. Existing classical should discharge decidability; no other edits planned.

## Five actual search methods and literature

| Method | Fresh query | Actual result |
|---|---|---|
| A LeanFinder | polynomial separated representation coefficient span basis linearly independent families | Polynomial.Sequence.linearIndependent/basis, Bernstein independence, charpoly basis independence. These are partial conceptual matches only. Raw `/private/tmp/roth-separation-r09-finder.json`. |
| B Loogle | LinearIndependent _ (fun _ => ∑ _, _) | LinearIndependent.sum_smul_of_nondegenerate, requiring a nondegenerate matrix; not this degree-controlled representation. Raw `roth-separation-r09-loogle.json`. |
| C LeanSearch | multivariate polynomial separated sum independent coefficient span basis | Polynomial.Sequence.basis, MvPolynomial.coeffsIn_eq_span_monomial and instFree; no full representation returned. Raw `roth-separation-r09-search.json`. |
| D source | full exists_separated_representation; span_of_finite; finrank_range_le_card; sum_smul_of_nondegenerate | Full-name mathlib source search returned no hit. Read actual Dimension/Constructions:451, FiniteDimensional/Defs:199–200 and Matrix/Nondegenerate:199; direct finite-span, dimension-bound and independence building blocks. |
| E local name | finrank_range_le_card | Actual matching declaration in Dimension/Constructions, index warming; this is a positive hit, not an absence claim. |

Auxiliary variants: Module.finBasis, finrank_pos_iff_exists_ne_zero, span_le, range_subset_iff, restrictSupport, degreeOf_le_iff. Common-equivalent topology/bornology buckets do not match this algebraic coefficient-rank statement. Live native exact? fails on the actual arbitrary-τ theorem goal, grind fails, aesop fails and its temporary downstream continuation hits default heartbeats. Raw `/private/tmp/roth-separation-r09-attempts.json`; no limits raised or temporary tactics saved. The final unfiltered native diagnostic recheck after attempts is complete and clean of errors. Conclusion: partial mathlib matches retained directly; no claim of exhaustive mathematical absence and no replacement/new helper needed.

Fresh public literature web queries: `polynomial coefficient dimension separated representation basis coefficient space`, `Takloo Bighash Yin formalizing Roth theorem Lemma 2`, `"coefficient space" "basis" "ROABP"`, and `"Formalizing Roth" "Yin"`. The Roth-title searches did not return a reliable public source. The primary [PIT thesis](https://iitgoa.ac.in/~arpita/articles/PITAndLowerBoundsForSumABPs.pdf) explains the partial coefficient space and its basis; [sumROABP paper](https://image.informatik.htw-aalen.de/~thierauf/Papers/sumROABP.pdf) was opened, and the primary [constant-width ROABP paper](https://iitgoa.ac.in/~arpita/articles/GKS15constWidthROABP.pdf) uses coefficient-space bases. These support the coefficient-span viewpoint; the inference that our finite family needs no finite ambient variable type is established by the compiler, not asserted as a quotation from these papers. Local source `.mathlib-quality/references/clean.tex` and original21/helper audit reports provide the project formulation. No ChatGPT mathematics search MCP exposed. No unapproved public restatement is applied.

## All 42 golf rules — fresh focused review

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl declaration. |
| 1.3 | hP' rewrites finite indexing, then uses a distinct coefficient-expansion theorem; no matching closing rwa collapse. |
| 1.4 | Support bound already closes with simpa using the support equivalence. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | Existential/conjunction witness already one anonymous constructor. |
| 1.7 | n/a: apply hP is followed by rewriting and simplification, not immediate exact. |
| 1.8 | Nonzero coefficient proof already uses by_contra!. |
| 1.9 | Indexed lambdas build coefficient families and degree witnesses; no redundant eta lambda. |
| 1.10 | Keep anonymous finite-dimensional evidence, reused hP', substantive hl1, and measured typed hdegree boundary; no trivial single-use have. |
| 1.11 | Degree summands already supplied by fun ν _; no apply/intro pair. |
| 1.12 | n/a: no show. |
| 1.13 | Nonzero coefficient witness already obtained by obtain ⟨ν,hν⟩. |
| 1.14 | n/a: no consecutive rw calls. |
| 1.15 | Existing terminal simp only retained under original21/helper profiling exemption: broad simp made failed empty-univ discharge expensive. No simp changes in this revisit. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | .trans_eq/.2/.map'/.linearIndependent already use direct API projection and dot notation. |
| 1.18 | n/a: constructor boundaries and typed lambdas carry expected types; no useful parenthesis-only rewrite. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: substantive public construction, not a trivial private witness. |
| 2.1 | Actual live whole-goal grind failed; saved diagnostics. |
| 2.2 | n/a: no retained grind or redundant prefix before it. |
| 2.3 | Support equivalence already uses terminal simpa; no simp followed by another closing tactic. |
| 2.4 | n/a: no continuity/differentiability/measurability property. |
| 2.5 | Positive dimension requires a nonzero span member; direct finrank_pos_iff_exists_ne_zero constructs it, arithmetic positivity alone cannot choose it. |
| 2.6 | Degree estimate and finrank bound already direct monotonicity compositions; no calc or monotonicity tactic chain. |
| 2.7 | Nat.lt_succ_iff directly discharges the Fin bound; no arithmetic automation needed. |
| 2.8 | Actual live aesop fails; no saved tactic change. |
| 2.9 | n/a: no concrete numeric computation or cast normalization. |
| 2.10 | n/a: arbitrary-field existential basis construction is not finite decidable computation. |
| 2.11 | n/a: no divisions or denominator identity. |
| 2.12 | n/a: no ring/ring_nf endpoint in the owned target. Helpers separately audited and untouched. |
| 2.13 | n/a: no symmetric case branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: constructor obligations have distinct linear-algebra, degree and identity content. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases-with-rfl. |
| 3.5 | No automation attribute: existential basis choice is not a simplifier normal form. |
| 3.6 | n/a: no simp_all. |
| 3.7 | n/a: no limit options or scaffolding. |

## Step-back / simplify equivalent

The main theorem now uses a finite coefficient family rather than any enumeration of τ. Existing classical already supplies the only decidability needed. The proof retains its basis choice, nonzero-span argument, support restriction and degree/reconstruction witnesses; native whole-goal automation confirms none is replaced by an immediate generic theorem. A tensor-product or coefficient-matrix restatement would add transport, change consumer shape and exceed this approved instance-only scope. No new helper, no inlining of the previously measured hdegree boundary, and no proof edits improve this omission. Simplify equivalent: NO-ISSUES-FOUND in the focused diff; built-in simplify is unavailable. /decompose-proof flag remains explicit for the existing headline length, already addressed by the two audited helpers as far as this authorized revisit permits.

## Signature codepoint packing and inequalities

Actual `#check @Roth.exists_separated_representation` printed at `format.width 100` in `/private/tmp/roth-separation-r09-contract-final.log`. Complete source signature lines:

| Line | Width | Next complete displayed fragment width | Arithmetic | Action |
|---|---:|---:|---|---|
| 291 | 92 | hn binder + colon 28 | 92+1+28=121 | ok |
| 292 | 32 | existential data/dimension fragment 85 | 32+1+85=118 | ok |
| 293 | 89 | independence/φ degree fragment 76 | 89+1+76=166 | ok |
| 294 | 82 | ψ degree fragment 49 | 82+1+49=132 | ok |
| 295 | 55 | reconstruction identity with := by 94 | 55+1+94=150 | ok |
| 296 | 100 | proof body follows | n/a | ok |

Fragments are complete binders or displayed mathematical expression units, not raw whitespace tokens; original signature text is byte-identical. No owned signature line exceeds 100 codepoints.

| Occurrence | Location | Orientation | Action |
|---|---|---|---|
| hn | line292 | degreeOf none P ≤ n | canonical |
| dimension lower/upper | line293 | 1 ≤ l; l ≤ n+1 | canonical |
| φ degree | line294 | natDegree ≤ n | canonical |
| ψ degree | line295 | degreeOf j (ψ ν) ≤ degreeOf (some j) P | canonical |
| reversed scan | all hypotheses/signature | no ≥ or > | no rewrite/rename |

## Verification evidence already completed

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exits 0; raw `/private/tmp/roth-separation-r09-build.log`. Exact original independent 64-line proof retained in `/private/tmp/roth-separation-r09-original-independent.lean`, compiler exits 0 and prints standard axioms; corresponding `.log` preserved.

New arbitrary-τ proof is an isolated copy of the current proof with isolated copies of the two helper proofs in namespace R09; none refers to the target theorem. `/private/tmp/roth-separation-r09-contract.lean` also independently quantifies the FULL ORIGINAL binder order `{τ} [Fintype τ] [DecidableEq τ] {K} [Field K] {P} hP {n} hn` and applies `@Roth.exists_separated_representation τ K _ P hP n hn`. It prints actual new type at format.width100 and checks actual built target, both retained private helpers and actual same-file public caller `Roth.exists_det_eq_mul` by suffix lookup, rejecting all nonstandard axioms. Compiler exits 0; `/private/tmp/roth-separation-r09-contract-final.log`. All seven checks (independent main, copied helpers, actual main/helpers/caller) use only propext, Classical.choice, Quot.sound. No guessing private numeric components. No sorry/native/custom axiom.

Fresh untruncated caller search over repository `.lean` files excluding Separation has zero hits; raw `/private/tmp/roth-separation-r09-source-searches.json`. Direct caller is exists_det_eq_mul in this module, covered by actual build, full-file LSP and actual axiom check. No external caller source edit or extra external file verification required.

Final native MCP full-file diagnostics after all temporary tactic attempts are success=true, partial=false, timed_out=false, failed_dependencies=[], **0 errors / 9 warnings / 0 infos**; raw complete unfiltered `/private/tmp/roth-separation-r09-lsp-final.json`. Baseline previous final native LSP had 12 warnings; omission removes the target's three. Remaining header metadata warning and other declarations' instance warnings are preserved without suppressions. Native MCP, schema discovery and all five search methods were available; no fallback needed. Temporary aesop errors appear only in attempts raw, not the restored final file.

Scope diff has exactly one inserted omission line. A byte comparison verifies replacing that single insertion recovers HEAD source exactly; therefore all proof/helper/docstring/definition/header/import bytes are unchanged. Actual source 584→585 lines; target mathematical declaration 36→36 source lines and proof body 30→30. No new declaration, helper, rename or shared-log edit. Original audit counts do not increase on this revisit.

## Every effective binder and generalisation

Generator `/private/tmp/roth-separation-r09-generate.py`, sequential compiler driver `/private/tmp/roth-separation-r09-probes.py`, individual `/private/tmp/roth-separation-r09-NAME.{lean,log}`, complete result summary `roth-separation-r09-probe-results.json`. Each probe uses autoImplicit=false and independent copied proof/helper bodies, not the theorem itself.

| Effective binder | Role | Mechanical probe and result | Disposition |
|---|---|---|---|
| τ : Type* | arbitrary remaining-variable index | drop_tau: unknown τ; no ambient enumeration used; independent universe remains polymorphic | retain type, omit both instances |
| Fintype τ | inherited only | dropping it compiles, including arbitrary-τ independent proof | approved removal applied |
| DecidableEq τ | inherited only | classical supplies proof-local equality; arbitrary-τ independent proof compiles | approved removal applied |
| K : Type* | coefficients | drop_K: unknown K; already independent universe | retain |
| Field K | coefficient vector space and commutative polynomial algebra | drop_field fails CommSemiring; DivisionRing fails CommSemiring; CommRing fails DivisionRing, Module.Free and rank conditions | retain Field |
| P : MvPolynomial (Option τ) K | represented polynomial and source of all degrees | drop_P: unknown P | retain |
| hP : P ≠ 0 | positive dimension/nonzero coefficient witness | drop_hP: unknown hP at contradiction | retain; no meaningful ordered scalar weak form for arbitrary field polynomial |
| n : ℕ | bound, length Fin(n+1) | drop_n: unknown n | retain finite Nat degree/index contract |
| hn : degreeOf none P ≤ n | finite coefficient expansion | drop_hn: unknown hn | retain; already weak ≤ |

The catalogue's `[IsField K]` syntax does not typecheck here because IsField is a predicate. That failed scratch experiment is retained as `roth-separation-r09-isField.log`. A first corrected predicate experiment omitted section inclusion and failed to expose hK (`isField-valid.log`); neither is treated as a valid mathematical negative. Correct explicit `include hK in` with `(hK : IsField K)` and `let : Field K := hK.toField` compiles (`roth-separation-r09-isField-explicit.lean/.log`), exit0. It is equivalent field structure packaged differently, not a genuine assumption weakening; no public change proposed. The source stays on Field and introduces no local instance.

Point-localisation/unbundling: n/a, no continuity/global regularity or conjunctive input. Strict→weak: hn already ≤; hP nonzero is essential for 1≤l. Universe: both Type* are already independent and polymorphic. Concrete→abstract/inversion: n/a, all objects arbitrary from the outset; Nat is intrinsic to polynomial degree and Fin indexing. The independent arbitrary-τ theorem is stronger than any Finite τ intermediate, so no auxiliary Fintype.ofFinite restriction needed. All other public contract alternatives were declined or unchanged, no required input remains.

Final sequential probe batch completes with no timeouts: drop_tau/K/field/P/hP/n/hn, divisionRing and commRing all exit1 with the concrete compiler failures above; drop_fintype, drop_decidable, and drop_both each exit0. Correct explicit IsField experiment also exits0. Summary parser was corrected to recognize modern `error(lean.category)` labels; raw logs were never altered. These negative results mean the given independent proof depends on those binders, not a claim that no alternative theorem could exist.

## Diff gates and eleven completion steps

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | actual lake build Roth.Separation exits0, build.log |
| definition_protected | pass | one insertion; every definition byte identical |
| theorem_statement_protected | pass under explicit approval | exact approved removal of two inherited instances only, full original adapter compiles |
| naming_gate | pass | descriptive snake_case, no forbidden tokens or rename |
| line_packing_gate | pass | all six signature rows measured, maximum100 |
| inequality_orientation_gate | pass | complete canonical-orientation table, no reversed code inequality |
| structure_gate | pass with explicit existing /decompose-proof flag | headline remains30 lines with conjunctions; two prior independently audited helpers retained; no new helper authorized |
| cumulative callers | pass locally | no external direct caller; actual same-module caller built, LSP/axioms checked |
| diagnostics | pass | complete unfiltered native 0E/9W/0I |
| comments/docs/imports/limits | pass | exact byte comparison, no suppression/scaffolding/options |

1. Step1 references: both skills, contract and required reference catalogues read.
2. Step2 audit: all24 concrete items recorded before editing source.
3. Step2.5 searches: all five actual methods plus variants, live exact?/automation and public literature recorded.
4. Step2.6 generalisation: every effective binder probed, approvals honored, negative limitations explicit.
5. Step2.7 packing: complete six-row codepoint table and actual format.width100 output.
6. Step2.8 inequalities: full occurrence table, no reversed inequality.
7. Step3 golf: all42 rules with concrete outcomes; no proof churn.
8. Step4 step-back: coefficient-basis argument retained; simplify equivalent NO-ISSUES-FOUND for focused omission.
9. Step5a diagnostics: complete native post-attempt full-file response saved, zero errors.
10. Step5b gates: table above; actual independent original/new proofs, adapter and built axioms pass; final actual timing recorded below.
11. Step6a renames: none, no sidecar needed. Dedicated report only; parent owns cumulative project/separateLeanEval verification and Git publication.

## Actual repository profiling / buzz equivalent

All native MCP/search/tactic/diagnostic requests, module build, original/independent/adapter/axiom compilers and all binder compilers completed before profiling. Parent confirmed its compiler/MCP idle. No source changes during or between sweeps. Actual command:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

First sweep `/private/tmp/roth-separation-r09-profile.log` exits0; parser `/private/tmp/roth-separation-r08-profile-table.py` writes `.log.json`, 25 anchored declarations, none≥1000ms. It uses the largest outer command plus outer async proof timing, excluding nested timing double-counts. First target29.717+762.489=792.206ms (baseline814.956); coordinate independence49.801+221.004=270.805ms; basis reconstruction102.254+597.207=699.461ms; direct actual caller106.080+367.468=473.548ms. Required ≥750ms repeat runs sequentially after this completed sweep.

Second isolated actual sweep `/private/tmp/roth-separation-r09-profile-repeat.log` exits0; `.log.json` has25 anchored declarations and none≥1000ms. Both raw logs decode as UTF-8 without replacement characters. Required borderline repeat satisfied; no source profiling scaffolding, limits, suppressed diagnostics, helper edits or performance deferrals.

| Actual declaration | First ms | Repeat command + proof = total ms | Repeat raw command/proof line anchors |
|---|---:|---|---|
| exists_separated_representation | 792.206 | 30.633+738.006=768.639 | 413876 / 413965 |
| linearIndependent_coordinate_polynomials_aux | 270.805 | 49.282+225.151=274.433 | 264254 / 264396 |
| eq_sum_aeval_basis_coeffNone_aux | 699.461 | 105.510+581.204=686.714 | 322892 / 323129 |
| exists_det_eq_mul | 473.548 | 91.728+414.466=506.194 | 964702 / 986112 |

First raw anchors for the same rows: 414568/414657, 264673/264815, 323362/323599, 964873/986261. Repeated source-level omission wrappers produce two or three command anchors; parser takes only the largest enclosing command, then adds the single enclosing asynchronous proof, never nested duplicates. Final main is46.317ms below the supplied814.956ms baseline, within ordinary wall-clock variability; no whole-project performance improvement claimed. Buzz equivalent PASS, zero over-budget actual declarations.

## Final result and freeze

Applied exactly the approved removal of Fintype τ and DecidableEq τ using one scoped omit before the original docstring. Proof and both helpers byte-identical, all other public contracts/docs/definitions preserved. No new helper, rename, alternative public proposal or required user input. Existing original21 structure flag is documented, not a new request for helper work. All eleven completion steps above complete; parent retains full/separateLeanEval cumulative checks and Git publication before original22. This revisit leaves original audit count at21/30.

All owned Lean/MCP/compiler/profile requests are complete and drained, including both sequential actual sweeps. I revoke **ALL source ownership** and become **report-only**. Frozen `Roth/Separation.lean` SHA256:

`d30464cac2d8d49bcaeb4f7edc0d35469af4c36189acbe93edf4a7ea0f1b1b91`

No source edits after freeze. Dedicated report path `.mathlib-quality/cleanup/Separation-approved-instances-exists_separated_representation.md`.

## Owner cumulative publication gates

Source FROZEN SHA256 `d30464cac2d8d49bcaeb4f7edc0d35469af4c36189acbe93edf4a7ea0f1b1b91`; leaf ownership revoked and requests drained before owner gates. Owner probe `56755` exit0,39.91s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r09-compatibility.{lean,log,json}`. Owner build session `81056` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,119.01s/32.93s; source hash stable. `/private/tmp/roth-separation-r09-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
