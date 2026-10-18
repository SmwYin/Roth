# Dedicated cleanup: `Roth.Θ_equiv` (original 15)

Scope: this public declaration only, `Roth/Theta.lean`, branch `ramin-cleanup`.
Immutable original: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`.
Checkpoint14 start SHA256: `f7c692b5eac9b0fb46be5031ae57440a49e27f3f34dfeb6bf2fb38962e388c9a`.
Evidence directory: `/private/tmp/roth-theta-equiv`.

## Result and authorization

The proof now applies `congrArg sSup` directly to equality of the two index sets,
replacing `rw [Θ, Θ]` followed by `congr 1`. The private transport lemma supplies both
inclusions; the inverse equivalence gives the reverse inclusion after simplification.
Proof body: 4 → 3 lines. No new helper, import, definition, or caller edit.

During this audit the coordinator relayed NEW EXPLICIT USER APPROVAL for A: remove
BOTH public `DecidableEq σ` and `DecidableEq τ` from this active target. Applied exactly
that approval: `omit [DecidableEq σ] in` precedes the preserved docstring and the explicit
τ-instance was removed. Every other binder, type/domain, order, visibility, name and
conclusion is retained. No D/E/F broader change was authorized or applied; other targets
and header metadata are untouched. The declaration remains public.

The retained anonymous τ-Fintype binder is synthesized as `inst_1` rather than old
`inst_2`. Per owner clarification, anonymous instance numbering is exempt from the name
comparison; exact instance types/order/BinderInfo and all user-written argument names
are checked. A temporary explicit synthetic instance name was reverted. The initial
overstrict certifier failure is retained in `independent-original-actual.log`; only the
corrected final exit-zero certifier is definitive evidence.

## Baseline / doctor

Both skills, full cleanup command, full golfing-rules, proof-patterns, mathlib-search,
generalisation-patterns and cleanup-gates were read, plus relevant style/naming and full
profiling reference. The task-specific Lean4.34 profiler command overrides the stale
`-Dprofiler=true` example in the profiling reference.

Read-only preparation respected the checkpoint14 fence. Compiler/source window started
only on explicit RELEASE after pushed commit `e777d0a740a8c39ee7acdd618eaad67e98ae613d`.
The owner supplied clean full build 60.885s then separate `Roth.LeanEval` 22.704s, both
exit 0 at identical start hash. No duplicate owner build was launched here.

Reused identical-hash complete baseline LSP
`/private/tmp/roth-theta-index-comp/final-lsp-omit.json`: success=true, partial=false,
timed_out=false, failed_dependencies=[], 0 errors, 32 warnings. Target findings were
unused section `DecidableEq σ` and a diagnostic listing both unused decidable instances.
Cache fetching and file-wide housekeeping are n/a for this single-declaration leaf.

## Full substantive audit (24 items)

| # | Item | Finding / action |
|---|---|---|
| 1 | Lint | Baseline reports the two redundant decidability instances; approved removal addresses both. Final complete LSP recorded below. |
| 2 | Have scan | No `have` in this proof; nothing to inline or duplicate. |
| 3 | Options | No local limits, trace settings, or linter suppressions. None introduced. |
| 4 | Simp squeeze | One terminal `simpa [Function.comp_def] using …`; retained unsqueezed. |
| 5 | Naming | `Θ_equiv` describes the defined invariant and equivalence behavior. No forbidden abbreviation/numeric pattern, no rename needed. |
| 6 | Packing | Both signature lines measured below; conclusion cannot fit the preceding line. |
| 7 | By placement | `:= by` remains at the end of the conclusion line. |
| 8 | Format | Two-space proof indentation; no empty body lines, semicolon chain or haveI/letI. |
| 9 | Comments | No inline proof comments; original two-line docstring preserved byte-for-byte. |
| 10 | Docstring | Existing public statement/source documentation remains anchored to the declaration. |
| 11 | Visibility | Public invariance API named in module main results; retained public. |
| 12 | Structure | Headline proof is 3 lines, ≤15; no conjunction or branch >10 lines; no extraction justified. |
| 13 | Mathlib | Five actual methods and compiled clean-prefix automation below; use generic congruence directly. |
| 14 | Junk def | N/a: theorem, no definition introduced. |
| 15 | Exists lemma | N/a: public equality theorem, no existential output. |
| 16 | Show/change | Neither tactic occurs. |
| 17 | Push-neg | No negation normalization occurs. |
| 18 | Generalise | All ten original effective binders individually drop-tested; both DecEq drops approved/applied, remaining eight retained. |
| 19 | Inequalities | No inequality in signature; scan table below. |
| 20 | Normal form | Equality of Θ values under pulled-back q/r is the canonical renaming form; generic part is set equality plus congruence. |
| 21 | Syntactic generality | Bundled equivalence supplies both forward/inverse transport directly; no unbundled restatement improves this call site. |
| 22 | Import fanout | No import added; fanout unchanged. |
| 23 | Casts | Diff introduces no ascription/coercion. Casts: 0 dropped / 0 cross-type / 0 load-bearing. |
| 24 | Instance names | No instance declaration introduced; retained Fintype argument stays anonymous. |

Issues fixed: two redundant public instances under explicit approval; redundant unfold/congruence
proof step. No production helper, rename queue entry, shared report or Git mutation.

## Mathlib search status (five actual methods)

Raw remote/name requests: `searches.json`; source sweep: `source-search.log`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `supremum invariant under equivalence renaming variables multivariate polynomial index` | Related `MvPolynomial.rename_psum`, `totalDegree_renameEquiv`, `rename_esymm`; none states this custom admissible-index supremum equality. |
| B Loogle | `sSup ?s = sSup ?t` | Generic supremum results including `csSup_of_not_bddAbove`; no Θ/indexSet transport result. |
| C LeanSearch | `multivariate polynomial index invariant under equivalence of variables` | Symmetric-polynomial renaming and `MvPolynomial.IsSymmetric`; different invariant. |
| D source rg | Full `Θ_equiv`, `indexSet_comp_subset`, csSup equality and renameEquiv variants across project/order/polynomial sources | Custom Θ only in this project; generic order equality and polynomial renaming API are building blocks. |
| E local name | `sSup_congr`, followed by `congrArg` | First empty with index=unavailable (NOT absence evidence). `congrArg` found in Lean Prelude, with unavailable index reported honestly. |

Auxiliary variants checked: `csSup_eq_csSup_of_forall_exists_le`, `renameEquiv_refl`,
`renameEquiv_symm`, `renameEquiv_trans`, set subset antisymmetry and congruence.
No common-equivalents bucket (discrete, finiteness, separation, bornology) matches Θ.
Conclusion: no direct replacement was found in this bounded search; retain the custom
mathematical transport theorem and call generic `congrArg` directly. This is not a proof
that no indexed/remote equivalent exists. No private wrapper was added.

`automation.lean` is the exact source prefix ending BEFORE the target, followed by anonymous
examples. `rfl`, `simp [Θ]`, `grind`, `aesop`, `exact?` all fail to close the goal;
`apply?` offers only partial real-extensionality/real-power goals and generates an incomplete
scratch declaration warning. The expected-failure batch exits 1 and certifies no axioms.
No query can cite the target (it is absent from the prefix); no failed named declaration
is available for selfproof contamination. The supplied known native multi_attempt stall
was not repeated; ordinary bounded isolated compiler exploration was used.

## Generalisation: every effective original binder

`positive-binders.lean` separately compiles removing each DecEq and removing both (exit 0).
`negative-binders.lean` uses autoImplicit=false and explicitly writes the whole original
telescope outside the section: eight other individual drops fail (exit 1 as expected).
`weakening.lean` separately tests Fintype→Finite on each side and equivalence→function,
injective function, and surjective function. These probes fail to elaborate the retained
statement or transport proof; they do not prove those mathematical alternatives impossible.

| # | Effective parameter | Class/use | Compiled drop / weakening result | Decision |
|---|---|---|---|---|
| 0 | `{σ : Type*}` | Type variable for pulled-back weights and polynomial variable type | Drop: unknown σ with autoImplicit=false. Already universe-polymorphic. | Retain |
| 1 | `[Fintype σ]` | Finite index/weight infrastructure on source | Drop: synthesis failure; `[Finite σ]` replacement: Fintype synthesis failure in retained Θ expression. | Retain |
| 2 | `[DecidableEq σ]` | Unused section decidability | Drop compiles, including simultaneous drop. | Approved A, removed |
| 3 | `{τ : Type*}` | Target variable type, e/q/r domains | Drop: unknown τ. Already independently universe-polymorphic. | Retain |
| 4 | `[Fintype τ]` | Finite target index/weight infrastructure | Drop: synthesis failure; `[Finite τ]` replacement: Fintype synthesis failure. | Retain |
| 5 | `[DecidableEq τ]` | Unused explicit decidability | Drop compiles, including simultaneous drop. | Approved A, removed |
| 6 | `(e : σ ≃ τ)` | Forward and inverse admissible-index transport | Drop: unknown e. Function/injective/surjective substitutions fail current helper type and `.symm`. | Retain bundled equivalence |
| 7 | `(B : ℝ)` | Common coefficient bound in both sets | Drop: unknown B. Abstract coefficient/order change would change the underlying definitions, beyond this theorem. | Retain |
| 8 | `(q : τ → ℕ)` | Denominators pulled back by e | Drop: unknown q. Point-localisation n/a: every coordinate participates. | Retain |
| 9 | `(r : τ → ℕ)` | Degree/weight tuple pulled back by e | Drop: unknown r. Strict→weak n/a: this is data, with no positivity hypothesis here. | Retain |

No proposition hypothesis exists here to weaken strictness or localise. No domain, codomain,
argument order, result or other class change was applied. Finite-only formulations would
require choosing finite enumerations before the Θ expressions; any such wider restatement
is outside the approved scope. Correlated existential outputs n/a: result is equality.

## Public literature and inversion check

Actual web queries: `Roth theorem polynomial index invariant renaming variables`,
`Roth lemma 5 index polynomials Theta supremum variable permutation`,
`site.ncatlab.org supremum isomorphism invariant`,
`site.stacks.math.columbia.edu Roth theorem polynomial index`.
Top topical results included the [AMS chapter preview](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf),
[Milojevic's elementary exposition](https://aleksa-milojevic.github.io/expository/roth.pdf),
and [Roth's ICM account](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf).
The Milojevic PDF was opened successfully; the ICM open returned an internal error (no
claim of having read it). The nLab query returned [join](https://ncatlab.org/nlab/show/join),
[isomorphism](https://ncatlab.org/nlab/show/isomorphism) and property-sup; Stacks gave no
specific Θ renaming theorem. These are contextual results, not a literature absence proof.
No ChatGPT math MCP tool is available (tool inventory checked).

Local primary source `.mathlib-quality/references/clean.tex` lines 625–633 requests variable
renaming invariance; lines 646–665 define the finite-variable coefficient/degree-bounded
supremum. Our inference from those definitions: simultaneous relabeling preserves the
admissible family. The theorem already imposes no B/q/r positivity beyond what its
definitions require; literature supplies no reason to add such hypotheses.

Mandatory inversion diagnostic: Θ occurs only at the initial unfolding in the old proof;
the remaining proof uses equality of index sets. This fires the abstract-congruence case:
the generic result is already `congrArg sSup`, now used directly. The substantive renaming
of admissible polynomials remains in existing private `indexSet_comp_subset`. Introducing
another generic supremum helper would duplicate Lean/mathlib, so no helper/restatement.

## Signature packing and inequality tables

Final #check at format.width=100 is in `independent-original-actual-final2.log`.

| Signature line | Codepoints | Next complete signature component | Arithmetic | Action |
|---|---:|---|---|---|
| 146 | 75 | `Θ B (q ∘ e) (r ∘ e) = Θ B q r := by` (35) | 75 + 1 + 35 = 111 > 100 | ok |
| 147 | 39 | No next signature line | n/a | ok |

Original corresponding widths were 91 and 39 (91 + 1 + 35 = 127 > 100).
`omit` is a command outside the signature, placed before the docstring as required.

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | Entire signature and all hypotheses | No ≥ or > inequalities (function arrows are not inequalities) | n/a | n/a |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by-exact | n/a: no wrapper. |
| 1.2 by-rfl | n/a: no reflexive proof. |
| 1.3 rw+exact | Assessed; direct congrArg removes explicit unfolding, rather than rwa. |
| 1.4 simp+exact | Existing final simpa already consolidated. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 constructors | n/a: equality handled via subset antisymmetry, no constructor/exact pair. |
| 1.7 apply+exact | Direct congrArg application has a nontrivial subsequent subset proof; no immediate exact to merge. |
| 1.8 contradiction | n/a: no contradiction. |
| 1.9 eta | n/a: no lambda. |
| 1.10 single-use have | n/a: none. |
| 1.11 apply+intro | n/a: no intro chain. |
| 1.12 show | n/a: none. |
| 1.13 have projections | n/a: none. |
| 1.14 merge rw | Replaced complete rw/congr pair with direct congrArg. |
| 1.15 terminal simp-only | n/a: final simpa is unsqueezed already. |
| 1.16 nonterminal simp | n/a: no such simp. |
| 1.17 dot notation | Existing e.symm retained; congrArg is a function theorem, no useful dot conversion. |
| 1.18 trailing parentheses | No removable callback parentheses; helper arguments need grouping in subset_antisymm. |
| 1.19 push-neg | n/a: absent. |
| 1.20 trivial exists | n/a: no existential lemma. |
| 2.1 grind | Actual anonymous whole-proof trial fails. |
| 2.2 pre-grind removal | n/a: no grind retained. |
| 2.3 simpa | Whole `simp [Θ]` trial leaves indexSet equality; existing final simpa kept. |
| 2.4 fun_prop | n/a: not a continuity/measurability/differentiability goal. |
| 2.5 positivity | n/a: equality of two arbitrary suprema, not a sign goal. |
| 2.6 gcongr | Assessed congruence: direct congrArg removes redundant unfold/congr; no inequality monotonicity. |
| 2.7 lia/omega | n/a: no linear integer arithmetic goal. |
| 2.8 aesop | Actual anonymous whole-proof trial fails. |
| 2.9 norm-num/cast | n/a: no numeric computation/cast normalization. |
| 2.10 decide | n/a: arbitrary real equality over polynomial families, no finite executable decision goal. |
| 2.11 field-simp/ring | n/a: no algebraic identity in field expressions. |
| 2.12 linear-combination | n/a: no ring-ending arithmetic proof. |
| 2.13 wlog | Reverse direction already reuses identical transport through e.symm; no duplicate case branch. |
| 2.14 calc | n/a: no calc chain. |
| 2.15 all-goals closure | Only one residual inclusion, closed by simpa; no repeated parallel goal closures. |
| 3.1 erw | n/a: absent. |
| 3.2 legacy continuity | n/a: absent. |
| 3.3 omega→lia | n/a: neither occurs. |
| 3.4 rcases-rfl | n/a: no local case split. |
| 3.5 attributes | No new simp/grind registration: invariant renaming rule needs explicit e and could create rewriting churn. |
| 3.6 simp-all | n/a: no simp_all-only and no useful local hypothesis family. |
| 3.7 limits | No raised limits existed or were added. |

Step-back reflection: one-tactic rfl/simp/grind/aesop failed, exact? found no closure and
apply? only partial reductions. The selected proof expresses the mathematical structure:
equality of sets from two transports, then congruence of sSup. A nested term-mode expression
would obscure the reverse-inclusion simplification without removing mathematical work.

## Verification / final gates

Definitive positive gates (ordinary compilation remains separate from expected-failure trials):

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | PASS | `/Users/ramin/.elan/bin/lake build Roth.Theta`, `module-build-frozen.log`, exit 0, 57.911s. |
| complete final LSP | PASS | Fresh native `lean_diagnostic_messages` for entire live Θ file with no filters, `final-lsp.json`: isError=false, success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors, 30 warnings. No diagnostic on target lines142–151. |
| independent original type/value | PASS | `lake env lean independent-original-actual-final2.lean`, exit 0, 28.711s. Immutable original private transport and Θ_equiv proofs included literally, independently re-elaborated; no invocation of current Θ_equiv to prove the original. |
| full old telescope recovery | PASS | Explicit `oldAdapter` retains both old DecEq instances; kernel `rfl` equality to the independent original proof; exact old type, universes and BinderInfo checked. |
| actual final contract | PASS | Actual built constant has eight binders in retained order, user argument names and BinderInfo preserved; both DecEq absent from type AST/telescope. Separate `caller-original-type.lean` directly checks expected new-eight type/universes against actual type. |
| actual axioms | PASS | Actual final Θ_equiv, oldAdapter and independent original proof each only `[propext, Classical.choice, Quot.sound]`, verified programmatically and via `#print axioms`. |
| original caller contract | PASS | `lake env lean caller-original-type.lean`, exit 0, 34.059s. Immutable original Θ_lt statement recovered, kernel equality and exact type/universes/user names/BinderInfo verified; actual caller standard axioms printed. |
| definition_protected | PASS | No def/abbrev/data body changed. |
| theorem_statement_protected | PASS under explicit A | Only approved removal of both DecEq instances; every other parameter and conclusion retained. |
| structure_gate | PASS | 3 body lines, headline≤15, no long branch/conjunction. |
| naming_gate | PASS | No forbidden pattern/abbreviation; no rename. |
| line_packing_gate | PASS | Full measured two-row table, 111>100 split justified. |
| inequality_orientation_gate | PASS | Complete zero-occurrence table. |
| new identifiers | PASS | `congrArg` found by local search in Lean Prelude and compiled in selected proof; no unverified new identifier. |
| performance | PASS / FAST-BOARD | `accepted-final-profile.log`, exact final source prefix, exit 0, 41.812s process time; target aggregate37.638ms after complete LSP drain. |

Precise caller inventory: repository `rg` finds only Θ_lt at line834 as an actual theorem
call, plus the module documentation listing. No external Lean-file caller is present and no
caller edit is required. Θ_lt's implicit/section parameters were checked from its actual
constant, not inferred from visible header text alone.

Two scratch-certifier corrections are recorded honestly: initial exact synthetic-name
comparison failed as expected under removal; then unqualified `.instImplicit` in the
corrected script was ambiguous. `independent-original-actual-final2.lean` fully qualifies
`Lean.BinderInfo.instImplicit` and exits 0. Neither failed scratch run is certified as a
complete positive gate, and neither altered production proof trust.

Owner cumulative full `lake build`, then separate `lake build Roth.LeanEval`, and owner
whole-module profile sweep remain PENDING OWNER WORK on this new hash. Leaf completion
never claims those owner gates have already run.

## Simplify and buzz

The native `/simplify` and `Skill` dispatch tools are unavailable in this host. The
equivalent scoped holistic review was performed directly: no duplicated skeleton/new
helper/import/API layer, and the direct congruence proof is the reusable generic route.
Outcome: PASS-THROUGH after the selected proof change; no separate polish edit.

Baseline exact source-prefix profile command:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-equiv/baseline.lean`
exit 0. Target outer command 3.418ms + async proof 34.640ms + associated kernel/addDecl
1.268ms + associated top-level async linter 5.074ms = 44.400ms, avoiding nested double-counting.
Earlier same-source final profile (`final-profile.log`, exit 0, 38.646s process wall time)
measured outer omit command4.487ms + proof26.368ms + kernel0.911ms + linter4.778ms =
36.544ms. This pre-LSP sample is not the accepted final post-LSP sample.
Accepted final same-source sample after module + COMPLETE LSP + request drain:
`accepted-final-profile.log`, exit 0, 41.812s process time. Target outer omit command
5.770ms + async proof26.629ms + associated kernel/addDecl0.846ms + top-level async
linter4.393ms = **37.638ms**. The inner theorem/macro scope commands are already
included in the outer omit command and are not counted again. All column-zero target
async roots are included, with no nested double-counting. Baseline/final comparison on
the same basis: **44.400 → 37.638ms**, both comfortably below750ms, so no near-budget
repeat is required. Variation is expected; the conclusion is that both are safely fast.
Buzz outcome: **FAST-BOARD**; 0 limit raises, 0 outstanding performance deferrals.
Budget 1000ms; repeat threshold 750ms. Prefix evidence covers this target only, not the
whole Θ module. Known late whole-file profiling heartbeat issue and owner final sweep
remain explicitly owner work. No limit raise, native_decide, new axiom, sorry or profiling
scaffolding enters production.

## Required 11-step checklist

- [x] Step 1: required references read.
- [x] Step 2: full 24-item audit.
- [x] Step 2.5: five actual mathlib methods, limitations recorded.
- [x] Step 2.6: all effective binders, compiled probes, public literature/inversion.
- [x] Step 2.7: measured signature packing table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 golf rules assessed, applicable automation tried.
- [x] Step 4: alternative strategy and term mode considered.
- [x] Step 5a: fresh complete unfiltered final LSP, 0 errors / 30 warnings / none on target.
- [x] Step 5b: final module, exact contracts, axioms and post-LSP accepted profile gates.
- [x] Step 6a: no rename needed; no shared queue writes.

No Git mutation. No shared report/compatibility file changed. An adapted copy for all 29
original public contracts is prepared at `all-original-compatibility.lean` in the evidence
directory; its Θ_equiv row uses an explicit old-ten-binder adapter, not an invalid equality
between the new-eight and old-ten types. This prepared copy is not yet a compiled gate.


## Freeze / handoff

Final all-source SHA256 (`Roth/Theta.lean`):
`ee05dd2413443892400d9d05ca4be8d26afbb0c4f4c33b47339460451abfca4d`.
Source edits are frozen/revoked. Every launched compiler session and native request has
returned; no outstanding request/session is left. Final ordinary module, independent proof,
caller, complete LSP and accepted uncontended profile all use this source state. Reports
never claim owner cumulative builds have run on this hash.

Line delta: target proof4→3, theorem header/body6→5; the approved `omit` command adds one
line, so whole file remains974lines (net0). Two original docstring lines preserved exactly;
no proof comments were present. Overall leaf gates PASS. Remaining work: owner checkpoint
full build → separateLeanEval, cumulative compatibility/profile sweep and publication.


## Owner cumulative publication gates

After source freeze, revoked leaf authority and drained requests, owner ran `lake build` then
separate `lake build Roth.LeanEval`: both exited 0, in 45.642 s and 14.442 s. Theta SHA256
`ee05dd2413443892400d9d05ca4be8d26afbb0c4f4c33b47339460451abfca4d` remained identical
before and after both commands. Raw logs: `/private/tmp/roth-theta-d15-full.log` and
`/private/tmp/roth-theta-d15-leaneval.log`; machine `/private/tmp/roth-theta-d15-builds.json`.
These completed owner gates supersede the leaf's earlier pending cumulative entries. Exact-path
staging, commit and successful push publish original 15 before the next declaration edit.
Counts: Theta 15/35, overall 196/264, 9/14 files. This applies only Θ_equiv's two approved A
instance removals. Earlier approved targets now receive fresh sequential revisits; those revisits
will not increase original counts. Declined denominator and D/E/F extra widenings remain unapplied.
