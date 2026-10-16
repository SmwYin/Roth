# Cleanup: `Roth.index_hasseDeriv_ge`

Single-declaration audit on branch `ramin-cleanup`, owner-supplied HEAD `9d5365e`. Sole source target `Roth/Index.lean`; canonical report is this file. Source authority released and revoked at SHA256 `e5f65f41f0054212ead03ba47fb84d660a1fbe451c7918ee83df9fb9325d4174`, after every worker Lean request/compiler/MCP-helper process finished. Subsequent activity is report writing only. No Git, full-project build, LeanEval, shared-log edit, or other-declaration edit was performed by this worker.

## Result

Applied the explicitly approved `omit [DecidableEq σ] in` before the byte-identical docstring. Replaced a single-use `have`, its rewrite, and `linarith` with direct transport of the same inequality:

```lean
omit [DecidableEq σ] in
/-- Applying `Δ_k` lowers the index by at most the weight of `k`.
Source: §4, Lemma `lem:index-of-derivative` ("`ind(Δ_k P) ≥ ind(P) - ∑ k_j / r_j`"). -/
theorem index_hasseDeriv_ge {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ} (hk : hasseDeriv k P ≠ 0)
    (α : σ → ℝ) (r : σ → ℕ) : index P α r - weight r k ≤ index (hasseDeriv k P) α r := by
  obtain ⟨i, hi, hiw⟩ := exists_weight_eq_index hk α r
  rw [hasseDeriv_hasseDeriv, smul_eq_C_mul, map_mul, eval_C, mul_ne_zero_iff] at hi
  exact sub_le_iff_le_add.2 (by simpa [weight_add, hiw] using index_le_weight (r := r) hi.2)
```

Mathematics: choose an exponent attaining the derivative's index. Hasse composition makes its nonzero evaluation a scalar times the evaluation at exponent `i + k`; the latter therefore is nonzero. The original index is bounded above by `weight r (i + k)`. Additivity of weight and the minimizing equality give the claimed lower bound on the derivative's index.

Declaration 7 → 5 lines, proof body 5 → 3 lines; adding the scoped omission gives file 270 → 269 lines. Original public name, mathematical proposition, data arguments, argument order, universes, visibility, docs, and all definitions remain unchanged. The omission changes the elaborated public type, as authorized; exact original-type recovery was separately compiled. No helper, import, attribute, axiom, limit raise, or profiling scaffolding added.

Refactoring needed: project-end rename `Roth.index_hasseDeriv_ge` → `Roth.index_sub_weight_le_index_hasseDeriv`, to name the existing smaller-left inequality. Owner accepted the concrete old/new/reason and confirmed the actual sidecar entry was appended to `.mathlib-quality/renames.jsonl`: public scope, Roth/Index.lean, decl_line108, worker index_hasseDeriv_ge. No source rename was applied. External callers identified by owner: `Roth/MainLemma.lean:684` and `Roth/Theta.lean:385`. Owner verifies those callers and publishes the checkpoint.

## References and workflow

Applied lean4 and mathlib-quality; skill use was announced to the file owner before editing. Read the fresh-worker contract `/private/tmp/roth-index-leaf-contract.txt`, both skills, cleanup.md including all Phase-4 worker requirements and remaining phases, cleanup-all's ownership/delegation/reporting contract, golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, naming-conventions.md, profiling.md and commands/buzz.md. Consulted style-rules on declaration layout, docs/comments, inequality, variables, imports, casts, normal forms, performance, instances, and syntax; mathlib-review-stages normal-form, syntactic-generality and documentation sections. Initial large grouped reads were output-truncated; bounded reads supplied the operative sections. Read the complete source file and original target snapshot. No subagent was spawned.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.

Baseline: owner supplied clean published checkpoint and full-build responsibility. Initial complete native Index diagnostics returned success=true, partial=false, timed_out=false; target had unusedSectionVars and unusedDecidableInType warnings for DecidableEq. Optional cache/linter/full-build are owner-level gates, not fabricated worker runs. Classic import dialect; no file-level header/import/metadata edits authorized or made.

## Full audit: all 24 items

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | Two target DecidableEq warnings initially; approved omission resolves both. Final complete unfiltered native Index diagnostics: zero target items, 21 unrelated warnings. |
| 2 | HAVE SCAN | Original L111 `have := index_le_weight (r := r) hi.2`, no by; its anonymous fact is rewritten once and consumed once by linarith. Inline its mathematical bound through sub_le_iff_le_add and simpa. No have remains. |
| 3 | SET_OPTION | No per-declaration option, heartbeat/recursion override, or debug setting. |
| 4 | SIMP SQUEEZE | No original simp. Trial final `simpa only [weight_add, hiw]` compiled; unsqueezed terminal `simpa [weight_add, hiw]` also compiled and was retained. No nonterminal bare simp introduced. |
| 5 | NAMING | Existing mixed identifier refers to existing hasseDeriv operation; `_ge` is the orientation defect. Owner accepted explicit project-end rename to index_sub_weight_le_index_hasseDeriv. No numeric scheme, forbidden abbreviation, or single-letter public name. |
| 6 | LINE PACKING | Every signature line measured at 89 codepoints; first next binder is 11, so 89+1+11=101. Both lines remain justified; table and actual width-100 check below. |
| 7 | BY PLACEMENT | by ends second signature line. Nested final by stays on exact line. |
| 8 | FORMAT | Two-space body indentation, four-space signature continuation; no empty body lines, trailing whitespace, semicolon chain, haveI/letI, or redundant rw pair. |
| 9 | COMMENTS | No inline proof comments to preserve; every block comment in the full file byte-identical by regex comparison. |
| 10 | DOCSTRING | Existing public statement/source docstring preserved byte-for-byte, including permitted prose ≥. No doc rewrite authorized. |
| 11 | VISIBILITY | Main public API used in MainLemma and Theta; remains public. |
| 12 | STRUCTURE | Main-result body 3 lines ≤15; no conjunction in statement or long case branch. No helper/decomposition warranted. |
| 13 | MATHLIB | All five actual methods attempted, remote failures disclosed below; existing group-order transport supplies final step. Local Hasse composition is project API. No unsupported absence conclusion. |
| 14 | JUNK DEF | n/a: theorem, no definition edit. |
| 15 | EXISTS LEMMA | n/a: public inequality theorem; existing minimizing lemma is substantive reusable API, not a trivial private witness wrapper. |
| 16 | SHOW/CHANGE | Neither in target original/final body; scratch independent proof uses change to expose actual membership/index definitions. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All eight binders mechanically tested below; only approved DecidableEq omission applied. hk unchanged. |
| 19 | INEQUALITY | Conclusion already uses ≤; no ≥/> in code. `_ge` name handled by explicit owner queue action. Full table below. |
| 20 | NORMAL-FORM | Smaller-left subtraction bound is directly useful to callers. Equivalent additive form is an internal proof step, not an extra public equivalence API. |
| 21 | SYNTAX-GEN | hk is nonvanishing of the derivative whose finite index is used; no bundled condition or equivalent caller formulation improves use enough to justify API change. |
| 22 | IMPORT-FANOUT | n/a: no new import. |
| 23 | CASTS | 0 dropped / 0 kept as cross-type / 0 kept as load-bearing in diff. No cast added. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues fixed: unused DecidableEq inclusion; unnecessary intermediate arithmetic block. Deferred refactoring: one owner-managed project-end rename. No other proposed API change.

## Line packing: every signature line

Original L107 and final L108 are identical 89-codepoint first lines. Original L108 and final L109 are identical 89-codepoint second lines. Measurements use Python len on Unicode strings, not bytes.

| Sig line | Chars | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| Original107 / final108 | 89 | `(α : σ → ℝ)` =11 | 89 + 1 + 11 =101 >100 | ok |
| Original108 / final109 | 89 | none; body follows := by | n/a, signature ends | ok |

No repack required. Both point/weight binders and complete conclusion share the second line. No ≥95-character escape invoked. Actual built module check (`set_option format.width 100 in #check @Roth.index_hasseDeriv_ge`) compiled:

```lean
@index_hasseDeriv_ge : ∀ {σ : Type u_2} [inst : Fintype σ] {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ},
  (hasseDeriv k) P ≠ 0 → ∀ (α : σ → ℝ) (r : σ → ℕ), index P α r - weight r k ≤ index ((hasseDeriv k) P) α r
```

No DecidableEq remains in the actual public signature. Lean's #check rendering does not always strictly wrap every output line at the setting; actual source arithmetic above is the line-packing gate.

## Inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | Conclusion | index P α r - weight r k ≤ index (hasseDeriv k P) α r | none: smaller-left already | index_hasseDeriv_ge → index_sub_weight_le_index_hasseDeriv queued by owner |
| 2 | Entire signature and hypotheses | n/a: zero ≥/> tokens in Lean code | none | same owner queue action |

The docstring's ≥ is mathematical prose, explicitly outside the code gate. hk is ≠, not an incorrectly oriented inequality.

## Five actual search methods

Tools discovered through ALL_TOOLS metadata; direct bounded MCP helper attempts and native calls were real requests, all finished before release.

| Method | Actual query/search | Outcome |
|---|---|---|
| A Lean-Finder | Hasse derivative lowers weighted index of polynomial by at most weight of derivative; num_results5 | DNS failure `nodename nor servname provided, or not known`; unavailable, not absence. `/private/tmp/hasse-lean_leanfinder.json`. |
| B Loogle | MvPolynomial.hasseDeriv, _ ≤ _; num_results5 | DNS failure; unavailable, not absence. `/private/tmp/hasse-lean_loogle.json`. |
| C LeanSearch | index order vanishing multivariate polynomial Hasse derivative lower bound; num_results5 | DNS failure; unavailable, not absence. `/private/tmp/hasse-lean_leansearch.json`. |
| D Mathlib source | Untruncated full-name rg for index_hasseDeriv_ge and proposed new name; Hasse/index/weightedOrder combinations; inspected MvPowerSeries/Order.lean and project HasseDeriv169–179, Box79 | No exact-name source hit; weightedOrder_le and generic order API are partial ingredients. One guessed MvPolynomial/Taylor path did not exist and was corrected by inspecting actual project Hasse/Taylor imports. Search failures never counted as proof of absence. |
| E Name pattern | lean_local_search hasseDeriv_hasseDeriv; then sub_le_iff_le_add | First verified project composition and of_disjoint variant. Second returned namespaced partial hits, index error; generic lemma independently verified by actual compiled #check. |

Auxiliary variants: hasseDeriv_hasseDeriv_of_disjoint, weightedOrder_le, le_index_iff, sub_le_iff_le_add', subtraction/addition transport. Common-equivalents table has no polynomial-index match. No new predicates or wrapper helpers introduced. Whole-goal native exact? failed before the target was available; apply? offered partial le_index_iff and subtraction transport, not a closing theorem. The latter informed the direct final step. These establish usable ingredients, not a certified assertion that no equivalent exists in mathlib. Retain the owner's public theorem and use the generic ingredient directly; no deletion/public redefinition authorized.

## Generalisation: every binder

Fresh isolated compiler probes imported the built module with autoImplicit=false, without an enclosing variable context that could silently reintroduce dropped data. Logs `/private/tmp/hasse-drop-N.lean.log` for N0–7 and `/private/tmp/hasse-finite.lean.log`.

| # | Binder | Class | Use | Actual mechanical tests | Result |
|---|---|---|---|---|---|
| 0 | {σ : Type*} | type-variable/universe | Polynomial/exponent/point/weights type | Drop with autoImplicit=false | Unknown σ in dependent binder types; retain. Already universe polymorphic. |
| 1 | [Fintype σ] | typeclass | Protected index/weight signatures | Drop; weaken to [Finite σ] in fresh context | Both fail synthesizing Fintype σ in statement/application; retain. No other applicable algebraic/analytic parent. |
| 2 | [DecidableEq σ] | decidability | Unused inherited section inclusion | Drop and apply actual theorem with no local instance | Exit0; applied approved omission. |
| 3 | {P : MvPolynomial σ ℝ} | structure value | Polynomial in hk and both indices | Drop with autoImplicit=false | Unknown P in hk/conclusion; retain. Invalid proof recovery also ran into default heartbeat limit, not used as mathematical evidence. |
| 4 | {k : σ →₀ ℕ} | structure value | Derivative multi-index and weight subtraction | Drop with autoImplicit=false | Unknown k in hk/conclusion; retain. |
| 5 | hk : hasseDeriv k P ≠ 0 | proposition | Nonempty support attaining derivative index | Drop, try direct theorem application with missing premise discharged by assumption | Fails exactly on hasseDeriv k P ≠0. Retain; no weakening applied or claimed. |
| 6 | α : σ → ℝ | structure value | Evaluation point in both indices | Drop with autoImplicit=false | Unknown α; retain. |
| 7 | r : σ → ℕ | structure value | Weights in both indices and weight term | Drop with autoImplicit=false | Unknown r; retain. |

No strict positivity hypothesis to weaken, no global continuity/differentiability/monotonicity hypothesis to point-localize, no bijection/conjunction to unbundle. hk is already the point-independent nonvanishing premise used to get the finite minimum; replacing it with a sign assumption on a polynomial is not a catalogue-compatible weakening. No assumption on r positivity is present, so no such assumption was added. Parent weakening for Fintype via Finite was actually tested; the protected functions still require Fintype. Universes already Type*. Concrete-field/weight abstraction would require changing protected index/weight definitions and the theorem family, not an approved local mechanical omission.

Initial parallel probe batch overlapped the module rebuild: P/k/hk probes got transient missing Index.olean errors. Those results were discarded and each rerun after successful build; genuine binder/premise results above are from completed reruns. Data-drop failures are negative syntax/typing probes, never accepted as successful theorem verification. All final-source proof/type gates use independent exit0 compilations.

Inversion check: no fixed special polynomial/point occurs; P, α, r, k are arbitrary. Generic arithmetic after the coefficient argument is precisely the existing sub_le_iff_le_add API. Abstracting the coefficient field is definition-level restatement; no extra helper/public generalisation proposed.

## Public literature search

WebSearch actual queries: `Roth theorem polynomial index Hasse derivative weighted index generalization`; `site.mathlib.org Hasse derivative index polynomial`; `Takloo Bighash Yin Formalizing Roth theorem index derivative`. Search results included primary mathematical sources, mathlib documentation, and unrelated weighted-projective/arithmetic-progression papers; unrelated results were not treated as evidence. ChatGPT math MCP: n/a, no matching callable tool found in metadata; no external message sent.

Report-only literature correction: the original grouped search output did not preserve per-query first-three rankings in this artifact. Each exact query was repeated as a separate actual bounded WebSearch on 2026-10-16 after source release; the following records the first three **displayed leads in those repeated results**, not a reconstructed original ranking. Rankings/results changed between the earlier grouped request and these individual repeats. These leads are discovery records, not all sources relied on for mathematical claims.

| Actual repeated query | First displayed lead | Second displayed lead | Third displayed lead | Assessment |
|---|---|---|---|---|
| `Roth theorem polynomial index Hasse derivative weighted index generalization` | [Roth’s Theorem, Min Ru/UH notes](https://www.math.uh.edu/~minru/fields/roth.pdf) | [mathlib3 Hasse derivative docs](https://leanprover-community.github.io/mathlib_docs/data/polynomial/hasse_deriv.html) | [Roth’s theorem on weighted projective lines](https://arxiv.org/abs/2610.17589) | First is a relevant index-theorem lead; second is univariate Hasse API documentation; third is a different weighted-projective topic, not used to justify this theorem or a generalisation. |
| `site.mathlib.org Hasse derivative index polynomial` | [mathlib3 Hasse derivative docs](https://leanprover-community.github.io/mathlib_docs/data/polynomial/hasse_deriv.html) | [mathlib3 derivative docs](https://leanprover-community.github.io/mathlib_docs/data/polynomial/derivative.html) | [Mathlib HasseDeriv, FLT documentation mirror](https://imperialcollegelondon.github.io/FLT/docs/Mathlib/Algebra/Polynomial/HasseDeriv.html) | The engine returned other mathlib documentation domains despite the literal site.mathlib.org query. These are API leads rather than an exact multivariate weighted-index theorem. Actual installed API was independently checked before release. |
| `Takloo Bighash Yin Formalizing Roth theorem index derivative` | [Miller–Takloo-Bighash, An Invitation to Modern Number Theory, Google Books](https://books.google.co.in/books?id=kLz4z8iwKiwC&lr=&num=20) | [Miller–Takloo-Bighash, algebraic/transcendental number notes](https://web.williams.edu/Mathematics/sjmiller/public_html/238/currentnotes/AlgTrans_Chap5.pdf) | [Formal derivative, Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Formal_derivative) | No exact Takloo-Bighash–Yin manuscript hit among these three; use the repository’s supplied primary manuscript for that attribution. No extra mathematical claim was based on the discovery snippets. |

The report-only requery made no Lean requests, source edits, builds, or mathematical changes. The already opened primary Hasse-composition source below remains the literature evidence used for the generality assessment.

Local primary source `.mathlib-quality/references/clean.tex:571–587`, Takloo-Bighash–Yin §4, states exactly this nonzero-derivative index bound and proves it by attaining the derivative minimum and Hasse composition. The protected zero-polynomial convention explains retaining hk.

[Tidor–Yu–Zhao, *Joints of Varieties*, GAFA32 (2022), §4.3](https://link.springer.com/article/10.1007/s00039-022-00597-5) was actually opened and searched. It defines multivariate Hasse derivatives over arbitrary fields, gives the binomial composition identity and Taylor coefficient interpretation. This supports the algebraic content of the proof and suggests coefficient-field abstraction mathematically; it does not supply a drop of hk under this protected real-valued zero-index convention. The broader-field conclusion here is an inference, not a compiled API proposal or an applied generalisation.

[K. F. Roth, ICM1958 proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) search excerpt defines index by minimal nonvanishing weighted derivative relative to positive parameters. Direct open failed because the PDF exceeds the web fetch size; no detailed theorem claim drawn from an unread PDF. No literature-driven local assumption removal beyond the compiled approved DecidableEq omission.

## All 42 golfing rules

Actual native lean_multi_attempt tested whole-goal grind, simp, aesop, exact?, apply? at the first proof line. Whole closers failed; simp/aesop exposed the additive inequality without proving it. apply? gave partial transformations and an enormous suggestion list; it did not prove the theorem. Multi-attempt retains following original tactics, so missing hi/no-goal messages in those trials are replacement-range artifacts, not final-source evidence. Both direct final snippets separately returned empty goals/no diagnostics at final line112, and fresh CLI/module compiles independently verified complete proofs.

| Rule | Concrete status |
|---|---|
| 1.1 by exact | n/a: no trivial by-exact wrapper; proof has substantive witness/composition argument. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw + exact → rwa | Original rw-at-this followed by linarith, not exact; direct transport removes both instead. |
| 1.4 simp + exact | n/a original; new simpa consolidates weight rewrite and attained equality in final transport. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor pairs | n/a: no constructor/conjunction conclusion. |
| 1.7 apply + exact | Applied compositional final proof through sub_le_iff_le_add.2. |
| 1.8 by_contra + push_neg | n/a: no contradiction tactics. |
| 1.9 eta reduction | n/a: no lambda in target. |
| 1.10 single-use have | Applied: removed anonymous index_le_weight intermediate. |
| 1.11 apply + intro | n/a: neither original pattern nor introduced lambda. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have projections | n/a: original obtain already destructures witness; hi.2 projects necessary nonzero factor. |
| 1.14 merge rw | n/a: original second rw was at a distinct fact; final only one rw. |
| 1.15 terminal simp only | Applied to new terminal simpa: unsqueezed spelling compiled, measured and retained. |
| 1.16 nonterminal bare simp | n/a: none. |
| 1.17 dot notation | Existing hi.2 and .2 on inequality equivalence are concise; no subject-based alternative to generic transport. |
| 1.18 avoid parens | Final parenthesized by argument is one local proof and fits within100; <| changes no structure/clarity benefit. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial existential helper | n/a: no new helper; minimizing index API is substantial and already reusable. |
| 2.1 grind | Actually tried whole proof: failed on opaque polynomial-index inequality. |
| 2.2 delete before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Applied to weight_add and hiw at direct final bound; both squeezed/unsqueezed versions compiled. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | n/a: target is a difference bound between opaque indices, not structural positivity/nonzero expression. |
| 2.6 gcongr | n/a: key step compares different Taylor-support minima, not a monotone congruence/calc; final arithmetic discharged by exact equivalence. |
| 2.7 lia / omega | n/a: arithmetic is ℝ, not Nat/Int; direct group-order API replaces linarith. |
| 2.8 aesop | Actually tried: exhaustive search did not establish additive bound. |
| 2.9 norm_num / norm_cast | n/a: no concrete numeric or cast computation. |
| 2.10 decide +kernel | n/a: arbitrary polynomial/real bound is not finite computational decision. |
| 2.11 field_simp; ring | n/a: no denominator identity in proof. |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint; avoid introducing automation for one order transport. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 close repeated goals | n/a: no parallel similar subgoals. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 continuity → fun_prop | n/a: no legacy analytic tactics. |
| 3.3 omega → lia | n/a: neither present; real inequality. |
| 3.4 rcases rfl | n/a: no rfl substitution pattern. |
| 3.5 automation attributes | Considered; no global attribute needed to use theorem, no new simp/grind rule applied. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 remove maxHeartbeats | n/a: none existed; no limits raised. |

Step-back reflection: opaque minima require the substantive witness/composition argument, so bare general automation cannot replace it. A different proof via le_index_iff would quantify over every nonzero derivative rather than choose one minimizer; current minimizing proof directly matches the source and is already three lines after transport. No term-only rewrite would improve clarity of witness extraction; no helper or new API needed. The generic group-order equivalence makes the final arithmetic explicit and removes the measured linarith hotspot.

## Verification and trust gates

Actual final `lake build Roth.Index` completed exit0, log `/private/tmp/hasse-final-build.log`, `Build completed successfully (1501 jobs)`. First candidate build also passed `/private/tmp/hasse-build.log`. Both logs contain inherited dependency/other-declaration warnings; target warnings resolved. No whole-project success claim.

Final complete native unfiltered Index diagnostics requested with only file_path/timeout, no declaration/range/severity filter. Native result success=true, partial=false, timed_out=false, failed_dependencies=[]; 21 warnings elsewhere, zero target warnings/errors. A second direct MCP session independently saved raw complete native output `/private/tmp/hasse-final-lsp.json`, same success flags and counts. Helper exited0; its shutdown emitted an asyncio closed-loop destructor warning after returning the complete result. The native complete diagnostic result remains valid; no pending process/request remained at release.

Independent original theorem `/private/tmp/hasse-independent.lean` imports only the original pre-Index imports (Roth.Box, Roth.Taylor and mathlib). It recreates the protected index definition, then proves the original public proposition with original Fintype/DecidableEq binders, directly via finite image minimum, coeff_taylor, Hasse composition, csInf_le and weight_add. It imports/reuses neither target nor Index private helper nor another Index theorem. Final compiler session99924 exit0; log `/private/tmp/hasse-independent.log` prints only standard `[propext, Classical.choice, Quot.sound]`. Earlier scratch versions had set-coercion, folded-index rewrite and final projection mistakes; all repaired and rerun. Their sorryAx diagnostics were rejected intermediate failures, never accepted evidence or committed source.

Exact original public signature extracted from `/private/tmp/roth-index-original.lean` (target at112), rebuilt as `hasse_original_type` by applying actual built index_hasseDeriv_ge. `/private/tmp/hasse-compat.lean.log` exit0 also contains actual width100 #check and #print axioms on actual target and original-type recovery; both standard `[propext, Classical.choice, Quot.sound]`. Only scratch original-signature unused-DecidableEq warning remains intentionally. This is separate from the independent proof and separate from actual target trust checks.

New-identifier gate:

| New source identifier | Verification | Result |
|---|---|---|
| sub_le_iff_le_add | Actual #check @sub_le_iff_le_add against built module, fresh candidate compile, final module build | exists; AddGroup/LE/AddRightMono equivalence |

Other added tokens (omit, exact, by, simpa, existing weight_add/hiw/index_le_weight) are syntax or preexisting identifiers. Whole-file regex comparison confirms all block comments equal; target had zero inline comments. Focused diff contains only the approved scoped omission and final proof replacement; no definition or other declaration edit.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | Actual lake build Roth.Index, exit0, final log above. |
| definition_protected | pass | No def/abbrev/body edit. |
| theorem_statement_protected | pass with authorized omission | Literal signature same; actual type drops only approved σ-DecEq; original type recovered compiled. |
| structure_gate | pass | Main-result body3≤15; no conjunction/long branch. |
| naming_gate | pass with explicit queued action | Owner accepted project-end old/new/reason; no source rename. |
| line_packing_gate | pass | Both signature lines tabled, 89+1+11=101 break; no repack rows. |
| inequality_orientation_gate | pass with queued name action | No ≥/> in code; required table and owner rename action. |
| no-limit-raise/no-scaffolding | pass | No added options, axiom, sorry, native_decide, profiler wrapper or trace. |
| full-project/caller/LeanEval | owner gate | Owner checks MainLemma/Theta and complete project after frozen source; not claimed by leaf. |

Overall scoped gates pass. Owner confirmed the agreed rename queue entry was appended before report completion. Header metadata warning explicitly user-preserved; no author invention or warning suppression.

## Simplify pass

Outcome PASS-THROUGH after the direct final bound. No callable builtin simplify Skill tool exists; performed its scoped reuse/quality/efficiency review manually and disclosed that limitation. No duplicate helper, import, alternative API, unused intermediate fact or extra casts remain. No further source edit. Owner retains file-final independent simplify responsibility.

## Buzz pass: budget1000ms

Actual anchored CLI profiles completed exit0 and parser asserted all19 current declarations anchored:

```text
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-hasse-before-profile-trace.log
python3 /private/tmp/roth-index-profile-parse.py hasse-before
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-hasse-after-profile-trace.log
python3 /private/tmp/roth-index-profile-parse.py hasse-after
```

| Target | Before command/proof/total | Final command/proof/total | Budget |
|---|---|---|---|
| index_hasseDeriv_ge, L107→108 | 18.52/251.61/289.94ms | 82.13/100.41/192.16ms | well below1000 and750 borderline |

Dominant original tactic was linarith174.437ms. Final dominant tracked tactic is composition rewrite43.836ms. Separate fresh prefix candidate profiles measured squeezed final-transport proof71.582ms and unsqueezed60.314ms (these are trial proof timings, not whole source totals). Both compiled before selection; unsqueezed final spelling also passed native final-line multi_attempt with empty goals/no diagnostics. Timing variance/cache/concurrent probes affect wall time; no stronger speedup claim inferred from a single trial. Final absolute192.16ms is the release budget evidence. Aggregate profiler categories were not substituted for declaration timing. No native per-theorem extraction claim; actual CLI source anchors were used throughout.

Outcome FAST-BOARD for this target. No slow-declaration deferral/propagation, no limit raises removed/added, no source scaffolding. Owner performs file-final profile sweep separately.

## Eleven checked steps

- [x] Step1 references read and scoped ownership established.
- [x] Step2 all24 concrete audit rows.
- [x] Step2.5 five actual search methods, failures honestly disclosed, usable ingredients checked.
- [x] Step2.6 every binder tested/classified; parent/strict/point/universe/inversion checks; public literature.
- [x] Step2.7 every signature line/codepoint arithmetic and actual built width100 check.
- [x] Step2.8 complete inequality scan and explicit project-end name action.
- [x] Step3 all42 golf rules, actual applicable alternatives and n/a reasons.
- [x] Step4 strategy reflection and shorter direct arithmetic finish evaluated.
- [x] Step5a complete unfiltered native diagnostics, zero target warnings/errors.
- [x] Step5b actual module build, independent original proof, exact original-type recovery, actual axioms and protection/content gates.
- [x] Step6a concrete rename old/new/reason sent to owner; owner confirmed actual sidecar append (public, line108, worker index_hasseDeriv_ge); no source rename.

Comments preserved: all block docs byte-identical; zero inline proof comments originally. Refactoring needed only agreed project-end rename. Source authority released before report-only work and owner checkpoint verification.


## Owner checkpoint d10

Frozen SHA256 `e5f65f41f0054212ead03ba47fb84d660a1fbe451c7918ee83df9fb9325d4174`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session71946 exit0, `/private/tmp/roth-index-d10-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval62194 both exit0(176.89s/40.45s),
Index+Theta hashes stable; `/private/tmp/roth-index-d10-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, 0target items/21other warnings. External MainLemma and Theta complete native LSP0errors/3and23inherited warnings, noinfos/no faileddependencies; Theta one45second partial followed complete retry. Both external callers accepted; raw /private/tmp/roth-index-d10-callers-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
