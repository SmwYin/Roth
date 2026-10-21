# Helper4 cleanup: `Roth.boxFamily_eq_image_finsupp_aux`

Completed scoped Mode B introduced-helper audit. This is **not** completion of original18,
original19, MainLemma's full-file cleanup, or any of the264 original-declaration count.
The file owner retains publication, Git, shared progress, global simplify/usage pruning and
ALL-row performance gates. No Git, shared-progress, rename-queue, or child-agent writes occurred.

The family is represented by the **image of whole bounded finitely supported coefficient arrays**
on `Iic (ofSupportFinite r ...)`. Forward membership uses degree bounds to constrain every supported
monomial; reverse membership reconstructs degrees and treats coefficients outside the down-set as
zero. This is substantive integration of the project's family DATA with Mathlib's `Finset.finsupp`
API, not a one-to-three-call wrapper. It is transitional production code: no production consumer
exists yet; the intended broad counting prototype has separately compiled using this actual helper.

Changes: signature packing; one terminal simp replaces the final zero-coefficient rewrite and
positivity pair; the first-draft-only Interval import is removed after an actual exact-source
no-import compile established transitive availability. The full helper contract is unchanged.
No docstring was added to this private helper. No DATA, public declaration, earlier helper, caller,
Main source, mathematical assumption, limit, or conclusion changed.

| Frozen object | SHA256 |
|---|---|
| First compiling helper, including Classical wrapper and final newline | `f15a583699c9ccafd69aa6b7faa8d99b9e6aab534d603f7192d015eb92984a59` |
| Selected helper, including wrapper and final newline | `8e541df58adf5f5cdbaebda0098baff81e8e0286fa24e69b936e727ca4932d9f` |
| First-draft full context | `246b195aa03f89c10f5ba4f09c875ec38b92bd7cb05c8473470be42dfca69535` |
| Selected live full context | `354ae06443a541463530d38c3a4fc7f48a548cbb6331ebc88839655fc93121c3` |
| Published17 entry recovered byte-exact | `ff29cc40cece7f7432c7a2ddc64fd9cc73ceafd995b37b6927b7f3d2897bbac7` |

Helper20→19 declaration lines;15→14 proof lines; longest branch6 lines; maximum width98 codepoints.
Whole source730→728 lines (one helper proof line and one redundant import removed).

## Phase0 doctor and Phase1 preparation

The installed lean4 and mathlib-quality skills, full cleanup/cleanup-all/buzz commands,
854-line verbatim worker prompt (all three ranges),112-line future-profiler instructions,
and mandatory actual reference files were read. Truncated combined reads were recovered in bounded
ranges; immutable copies and byte hashes are in `read-inputs.json` / `read-inputs/`.
The target file was read, including recovered middle ranges. Dialect: classic imports, not `module`.
The helper is the sole declaration owned by this leaf. Whole-file edits remain with the file owner.

| Baseline check | Actual invocation / result |
|---|---|
| Cache fetch | skipped: existing pinned compiled cache available; no fetch needed |
| Affected build | `lake build Roth.MainLemma Roth.Main`, exit0,6.396065s; `beforeH4-affected.json` |
| Full build | `lake build`, exit0,40.214097s; `beforeH4-full.json` |
| Native ML | full unfiltered nonpartial/nontimeout success,0 errors, old header warning |
| Native Main | initial partial result rejected as completion; full success obtained after drain and again before serialized profile; `beforeH4-main-complete.json` |
| Linter | actual build/native diagnostics; no separate configured runLinter executable |

Phase2 punch-list: pack the finite-support instance (68+1+29=98); simplify final support-zero
case if a closed proof passes; test statement ascriptions and all mechanical weakenings; establish
actual import redundancy. No helper lint warning or docstring issue. File-level header warnings
and unrelated proofs are protected and are not silently described as fixed.
Phase3 file-level action is limited to removal of the helper-added Interval import.

## Full24-item initial audit

# Helper4 initial audit (before any edit)
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.
Scope: only introduced private `Roth.boxFamily_eq_image_finsupp_aux`; source lines330–349 including local Classical wrapper. This is not original18 completion.

1. LINT: no helper warnings; native whole ML has existing header warning.
2. HAVE SCAN: none.
3. SET_OPTION: none. Classical statement scope is deliberate and not a limit override.
4. SIMP SQUEEZE: none initially; final outside-support branch may simplify terminally.
5. NAMING: mixed object name `boxFamily` retained as the named DATA, equality/image/finsupp snake-case predicates and `_aux` private suffix are descriptive; no forbidden patterns or abbreviations. No rename required.
6. LINE PACKING: exact codepoint table below; wrapper excluded from signature and retained with command.
7. BY PLACEMENT: at end of signature.
8. FORMAT: two-space proof indent, four-space continuation, no internal blanks, no haveI/letI, no consecutive rewrites.
9. COMMENTS: none in helper; all surrounding comments protected.
10. DOCSTRING: none, as required for private helper.
11. VISIBILITY: private, intended to support finite-support public count.
12. STRUCTURE: 20 declaration lines including wrapper,15 proof lines; forward branch6, reverse branch7; no statement conjunction (coefficient bounds occur inside DATA definition).
13. MATHLIB: Finder found support-restricted polynomial equivalence, degreesLE/restrictDegree; Loogle found Finsupp.card_Iic; LeanSearch found generic support definitions. Source/name searches locate Finset.mem_finsupp_iff, Finsupp.ofSupportFinite, degreeOf_le_iff. These are partial building blocks; no replacement for this project-specific family equality was established. Generic automation probes pending before absence conclusion.
14. JUNK DEF: n/a theorem has no new DATA.
15. EXISTS LEMMA: n/a set equality, not trivial existential.
16. SHOW vs CHANGE: single term-mode `show c d = 0 from ...` fixes rewrite equality; test replacement by direct expression and terminal simp.
17. PUSH_NEG: none.
18. GENERALISE: table below; full function bound with finite support already handles infinite variable types.
19. INEQUALITY: no ≥/> in signature; all internal natural exponent inequalities use ≤.
20. NORMAL-FORM: image of a canonical finite finsupp product on Iic; RHS suits ncard_image and card_finsupp directly.
21. SYNTAX-GEN: retain unbundled r because intended public caller receives r : σ → ℕ; a Finsupp-only alternative would require bundling in every intended call, without strengthening mathematical scope. Test specialization/adapter separately.
22. IMPORT-FANOUT: helper uses new Mathlib.Data.Finsupp.Interval for LocallyFiniteOrder of exponent Finsupp. Existing Mathlib.Data.Finset.Finsupp is direct. MainLemma imports are used by Main, LeanEval, umbrella Roth; baseline full build passes. No extra import proposed.
23. CASTS: statement (0:ℤ), outer ↑Finset and Set ascription; (0:ℤ) fixes coefficient ring. Probe each; do not accept changed array type. B coercion Nat→Int is genuine.
24. INSTANCE-NAME: n/a no instance declaration.

| Signature line | Chars | Next complete unit | Arithmetic | Action |
|---|---:|---|---|---|
|331|68|[Finite (Function.support r)] (29)|68+1+29=98|repack|
|332|87|outer set expression (66+ chars)|87+1+66>100|ok|
|333|74|fun _ ↦ Finset.Icc (0 : ℤ) B) (29)|74+1+29=104|ok|
|334|66|none|n/a|ok|

| Inequality occurrence | Status |
|---|---|
|signature|n/a no ≥ or >; no _ge_/_gt_ name|

| Effective binder | Class/use | Mechanical candidates / reason |
|---|---|---|
|σ : Type*|type variable, monomial indices|already universe polymorphic; Sort alternative must support Finsupp/MvPolynomial Type input; probe|
|r : σ → ℕ|DATA, degree bounds and Iic endpoint|drop cannot preserve conclusion: r occurs essentially; test actual autoImplicit=false failure; Finsupp representation specialization can be recovered by coercion|
|[Finite (Function.support r)]|finiteness, ofSupportFinite endpoint|drop-test actual synthesis probe; no weaker parent class of Finite; point-localization cannot supply full array support needed by every exponent|
|B : ℕ|DATA, all coefficient intervals|drop cannot preserve conclusion: B essential; test actual autoImplicit=false failure|
|implicit degree index j and coefficient index d inside family DATA|effective inner binders|universally quantified bounds, needed at every monomial; no strict premise to weaken; independently frozen family DATA TYPE/VALUE must match|
|anonymous coefficient-array index in RHS lambda|inner type binder, ignored value|constant interval by design; no proposition to weaken, drop lambda changes Finset.finsupp argument type|

2.6c: no evidenced beneficial API restatement. 2.6d: n/a private decl, literature search not required. 2.6e: no weakening accepted yet. Point-local/strict-to-weak assessed at outer and effective inner binders; no strict hypotheses.

Phase3 file-level actions: none; source outside helper/import is protected by lease.
Phase5a/b prospective: no requested rename or non-rename refactor; global rename queue is owned by file owner and untouched.


## Search and generality conclusions (Phases2.5–2.6)

| Method | Actual query / outcome |
|---|---|
| A Lean-Finder | multivariate polynomials with bounded degree/coefficients as images of coefficient arrays; support-restricted polynomial equivalence and degreesLE/restrictDegree partial matches |
| B Loogle | `Finsupp, Finset.Iic`; `Finsupp.card_Iic` and related interval cardinalities |
| C LeanSearch | finite support functions/coefficient arrays/polynomial bounded degrees/image; support and onFinset definitions |
| D pinned source | full untruncated grep for helper/family plus `ofCoeff_injective`, `ofSupportFinite_coe`, `degreeOf_le_iff`, `mem_finsupp_iff`; raw output `search-source-full.log` |
| E local name | `Finsupp`,12 source hits; index explicitly unavailable, **not** evidence of absence |

All five methods were actually attempted. Raw results are `search0.json`–`search3.json` and source
logs. Variants include `mem_finsupp_iff_of_support_subset`, `ofCoeff_inj`, `ofSupportFinite_coe`,
interval/support variants. The finiteness common-equivalents bucket supplies images and finite
products, not this project's family equality. Conclusion: partial matches reused directly;
no replacement established. A whole-proof `exact?` actually failed; `apply?` supplied partial
refinements only and is rejected under the pinned synthetic-admission caveat. No generic absence
or impossibility claim is inferred from search or failed synthesis alone.

Outer and effective inner binders were assessed separately in the initial table. The finite-support
class has no weaker parent, and the full down-set needs the complete support, not one selected
point. There is no strict premise to weaken. `Type*` is already universe-polymorphic; the actual
Sort probe fails because Finsupp requires a Type. Dropping r/B under `autoImplicit=false` gives
unknown identifiers; dropping Finite fails `Set.toFinite`; removing statement Classical scope fails
the locally finite order instance. These are concrete elaboration results, not universal
counterexamples to differently restated theorems. Nat degree bounds and integer coefficients are
fixed by the protected polynomial-family DATA; changing their domains would change the object.
A Finsupp-bound specialization is exercised by the infinite-single-support property boundary;
retaining function r plus finite support suits the actual intended caller without bundling work.
No API change or old-contract adapter is needed. Literature: **n/a private decl, not required**.
No weakening, parent-class change, point-localization, or strict-to-weak restatement was accepted.

Ascriptions: `(0 : ℤ)` is load-bearing (removal constructs natural, not integer, coefficient
arrays and fails). Nat→Int B coercion is genuine. Removing the outer Set ascription compiles and
is actually defeq, but changes raw TYPE AST; it is not selected and no necessity-to-elaborate claim
is made for that annotation. Keeping the explicit array type protects the exact first-draft
contract. The explicit zero-equality `show` is removed by terminal simp. No new external Mathlib
identifier is introduced by the golf: all calls are already in the first draft and are verified
in pinned sources and actual whole compiler runs; `simp` is an existing Lean/Mathlib tactic.

## Final packing and inequality hard gates

The `#check`/TYPE reference is the complete actual TYPE AST logged by independent checks at the
frozen contract, including written names, order, binder information and universe parameters.
Widths below are codepoints, not UTF8 bytes. A next unit is a complete binder/function argument.

| Signature line | Chars | Next unit width | Arithmetic | Action |
|---|---:|---:|---|---|
|330|98|B binder7|98+1+7=106|ok|
|331|57|outer down-set/finsupp argument68|57+1+68=126|ok|
|332|74|constant-interval lambda29|74+1+29=104|ok|
|333|66|none|n/a|ok|

| Inequality scan | Result |
|---|---|
| All statement and hypothesis occurrences | n/a: no ≥ or >; no `_ge_`/`_gt_` name |

Name describes the DATA object and image-of-finsupp equality, with a private `_aux` suffix;
no forbidden numeric pattern/abbreviation. No rename queued. Body14≤30, branches≤6≤10, no
conjunction in the statement; no decomposition flag required. `by` remains at signature end,
no internal blank line, no haveI/letI, no deleted comment (none existed in the helper).

## All42 rules and step-back

# All42 golfing rules and step-back

1.1 n/a: no by-exact wrapper.
1.2 n/a: no by-rfl wrapper.
1.3 n/a: closing rewrite not followed by exact of an existing term; replaced outside-support block by simp instead.
1.4 n/a: no simp/exact pair.
1.5 n/a: no trailing rfl after simp.
1.6 n/a: constructor branches contain substantive support and degree reasoning, not two exact terms.
1.7 n/a: no apply/exact pair.
1.8 n/a: no contradiction-negation sequence.
1.9 n/a: lambdas use multiple projections/arguments or discard the index deliberately; none eta-reducible.
1.10 n/a: no haves.
1.11 n/a: no apply/intro.
1.12 applied: removed final term-mode show through terminal simp; bare equality rewrite without show also compiled but superseded.
1.13 n/a: existing obtain already destructures support/coefficient conjunction.
1.14 n/a: no consecutive rw calls.
1.15 n/a: initially no simp; selected terminal simp remains unsqueezed.
1.16 n/a: no nonterminal simp.
1.17 already uses .trans/.1/.2; no useful further dot notation.
1.18 n/a: no trailing-parenthesis function applications improved by <|; lambdas already parsed without them.
1.19 n/a: no push_neg.
1.20 n/a: substantive set-equality helper, no trivial existential lemma.
2.1 actual whole grind probe failed; retained direct proof.
2.2 n/a: no grind retained.
2.3 applied: support-zero rewrite plus positivity becomes terminal simp.
2.4 n/a: no analytic function-property goal.
2.5 initial positivity for nonnegative natural cast becomes terminal simp; no remaining positivity block.
2.6 n/a: no calc/monotonicity arithmetic block; degree transitivity is a direct proof term.
2.7 whole omega tried and failed, no usable constraints; no arithmetic subgoal survives simp, so lia is not needed in selected proof.
2.8 whole aesop tried and failed.
2.9 dropInt-ascription actual probe changed coefficient array from integers to naturals and failed; no concrete numeric computation/norm_cast problem remains.
2.10 whole decide actual probe rejected free variables; arbitrary polynomial set equality is not finite decidable computation.
2.11 n/a: no denominators/ring identities.
2.12 n/a: no ring-ending block.
2.13 n/a: forward/reverse image membership branches are not symmetric proof duplicates.
2.14 n/a: no calc chain.
2.15 n/a: refine subgoals have distinct witnesses/degree/support obligations, not common closing tactic.
3.1 n/a: no erw.
3.2 n/a: no continuity/measurability.
3.3 n/a: omega was only a failed scratch whole-proof attempt, none in selected source; no arithmetic goal remains for lia.
3.4 already uses rintro ⟨c,hc,rfl⟩ without subsequent substitution simplification.
3.5 n/a: private representation helper used explicitly by intended count; global simp/grind attribute would change automation without evidence.
3.6 n/a: no simp_all only.
3.7 n/a: no limits present or raised; no heartbeat wrapper used.

Step-back: actual rfl/simp/grind/aesop/exact?/decide/omega whole-proof probes all failed. apply? returned only partial library-search refinements (including preimage characterization) and a synthetic zero-goal artifact; it is rejected, never treated as a proof. An inverse/preimage strategy still requires the same two support/degree implications plus coefficient reconstruction, so no shorter verified path was established. The theorem equates the actual coefficient arrays, with one common array for all monomials; its two implications are mathematically different and no duplicated skeleton is available to factor. Final14-line proof and ≤6-line branches fit ordinary-helper thresholds; further helper extraction would obscure this local representation argument. No unsupported global mathlib-absence claim is made.


## Phases5a–5b and scoped simplify

No additional definition, wrapper, mathematical generalization, or API refactor was needed.
The shared rename queue is byte-exact and remains for the owner; this helper queues no rename.
The four earlier constructor/lookup/injectivity/range declarations and published17 finite proof
are preserved exactly, including all comments. Actual production TYPE/opaque-VALUE inventory is
empty both before and after; final LSP references contain only this declaration (total1).
This transitional state is not classified as junk. The separate intended count prototype invokes
the actual current private Name and passes all closed/std3 checks.

Phase6.5 scoped manual holistic review: PASS-THROUGH, no further helper issue found. The proof's
forward/reverse directions serve different obligations; no repeated skeleton within this helper
needs extraction. No built-in simplify callable exists in this environment, so no built-in
invocation or independent full-file simplify credit is claimed. The owner's fresh whole-file
simplify/reviewer/usage-pruning pass remains mandatory and outside this lease.

## Phase6 semantic, source, caller and native gates

The independent initial proof is a fresh replay of the actual **introduced first compiling
helper**, alongside an independently replayed exact family DATA definition. It is not a fictional
original-project helper and not a call to the current helper as the old proof. Both sides use
actual thmInfo/defnInfo metadata. Exact family TYPE and actual DATA VALUE equality and isDefEq are
checked. The helper compares full TYPE AST after only explicitly declared family DATA unfolding,
application-spine beta and both-side generated hygiene normalization; all written binder names,
order, BI and universe parameters are retained. The family DATA raw-value equality additionally
covers effective inner W/j/d binders hidden behind that DATA constant. Actual TYPE isDefEq and
actual opaque VALUE inferred type are checked separately. TYPE/VALUE have no expression or level
metavariables, fvars, loose bvars or sorryAx; collected axioms are restricted to propext,
Classical.choice and Quot.sound. The entire independent first-draft closure traverses5549 constants
and bans the actual current helper Name. There is no arity-based Name map or proof-irrelevance
substitute for DATA comparison.

Fresh initial guard: `beforeH4-independent-v2.json`, exit0,59.106997s.
Final guard: `finalH4-independent.json`, exit0,127.017074s. Six **property**, not DATA-application,
boundaries directly contain the actual current helper in their VALUE and pass closed TYPE/VALUE,
inferred TYPE and std3: Fin0, B0, ULift Bool, zero support on Nat, arbitrary single support on the
infinite Nat type, and common whole-array membership. The separate broad counting/old Fin formula
prototype also passes those guards and actually uses this helper; no original18 audit credit is
claimed. Effective limits were printed as200000/20000/512; no limits were raised, no heartbeat
wrapper used, no optional historical heartbeat claim made.

Source protection: all17 source/config pins other than the intended MainLemma bytes are exact;
Main and all earlier helper/public proofs/docs/comments are unchanged; stripping the selected
helper plus its separator recovers the published17 entry byte-for-byte. `source-protection-final.json`
and `helper-only.diff` retain exact evidence. This is stronger than a signature-line-only grep.

| Final check | Actual command / result |
|---|---|
| finalH4-affected | `lake build Roth.MainLemma Roth.Main`, exit0, 75.675672s; `finalH4-affected.json` |
| finalH4-full | `lake build`, exit0, 36.474753s; `finalH4-full.json` |
| finalH4-Eval-build | `lake build Roth.LeanEval`, exit0, 39.756759s; `finalH4-Eval-build.json` |
| finalH4-independent | `lake env lean -j1 finalH4-independent.lean`, exit0, 127.017074s; `finalH4-independent.json` |
| finalH4-inventory | `lake env lean -j1 final-inventoryH4.lean`, exit0, 60.064530s; `finalH4-inventory.json` |

| Final unfiltered native file | Complete | Errors | Existing warnings |
|---|---|---:|---:|
|MainLemma|nonpartial/nontimeout success|0|1 header|
|Main|nonpartial/nontimeout success|0|4 header/unused variables|
|LeanEval|nonpartial/nontimeout success|0|0|

Raw native JSON is retained. No warning filter or partial result is used as acceptance.

| Gate | Result / evidence |
|---|---|
|lake_build_file / full / separate Eval|pass, actual commands above|
|definition_protected|pass, no DATA edit; exact initial/current family guard|
|theorem_statement_protected|pass, only whitespace packing; full contract AST/binders/isDefEq|
|structure_gate|pass,14 proof lines, max6 branch|
|naming_gate|pass, descriptive image equality, no forbidden pattern|
|line_packing_gate|pass, all four measured rows|
|inequality_orientation_gate|pass, explicit zero-occurrence table|
|comments/docstrings|pass, no helper docstring or deleted comment; surrounding bytes exact|
|no-limit-raise / no-scaffolding|pass, selected source has neither added limits nor profiling flags|
|cumulative caller safety|pass, actual production consumers empty; all existing source/caller bytes exact and Main/Eval builds/native complete|

## Phase6.6 buzz and provenance recovery

Actual required command on every matched variant is
`/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
Only temporary scaffolds add trace windows. True is before the complete original
`open scoped Classical in` wrapper, false after that complete command; removal of only inserted
option commands recovers each canonical source exactly. Source tokens include the exact helper
name and following separator. The actual fully qualified proof Name is
`_private._stdin.0.Roth.boxFamily_eq_image_finsupp_aux`.

The first overlapped profiler/native/independent attempt is rejected. A later historical serialized
pair produced160.884/164.167ms with correct arithmetic and whole exit0. Final provenance review
found that the inherited resolution script hashed the Elan Lake proxy and actual pinned Lean,
but missed the distinct actual pinned Lake executable. Those historical rows therefore do not
supply the accepted executable-provenance timing gate; **no late hash is called a before-golf hash**.
The owner authorized one fresh matched replay of the exact frozen first-draft and selected
scaffolds, with no production rollback/edit and no timing-selection repair. All old rows were
already fast; this is provenance recovery, not cherry-picking an unchanged third sample.

Fresh pre/post brackets hash actual pinned Lake/Lean, both Elan proxies, PATH resolution,
17pins/104companions, actual dynamic package/setup union and installed pinned-core compiled
SUPERSET. Both brackets are unchanged across both sequential replay runs. Exact CLI input SHA,
canonical-source SHA and scaffold recovery are verified. Current physical source/cache remains
selected during the first-draft replay; old/final variant input SHA is recorded separately.

| Accepted fresh replay | Complete disjoint total | Whole exit/time |
|---|---:|---|
|FIRSTDRAFT BEFORE|164.135ms|exit0, 54.928615s|
|SELECTED FINAL AFTER|164.965ms|exit0, 51.869225s|

FAST-BOARD. Both <750ms; no same-frozen repeat is triggered. No speedup is claimed.
No production direct consumer or meaningful production combined group exists yet; original18
must capture its later expanded count+consumer+audited-helper pair before editing public18.
The separate intended prototype is not substituted into this budget.

Root accounting uses the unique complete **outer** open-scoped command plus genuine disjoint
proof/compiler-kernel/lint async roots. Flat private-theorem/private-lemma macro-expansion command
roots are inclusive children and explicitly excluded. No Meta event, nested child, next command,
or end wrapper is double-counted. New drivers `parse-wrapperH4.py` and
`parse-recovery-wrapperH4.py` call unchanged frozen owner parsers. Each `*-source-wrapper-binding.json`
binds canonical/scaffold/raw SHA, exact outer payload, actual raw line boundaries, four disjoint
roots and both excluded expansion commands. Exact-name verifier succeeds on every accepted replay.
All streams are separate stdout/stderr, strict UTF8, with actual bytes/SHA in the manifest.

Fresh recovery binary hashes:
* actual pinned Lake51,824bytes: `c8c24f1398162ab4004e2a869952d8469f54293651151feaad4526f2b8474c6e`
* actual pinned Lean49,968bytes: `1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554`
* each Elan proxy5,880,832bytes: `d52c4516a6c6f0cc14cab0ecf36e5058a764f39b109d8609be7dd1279ca41e9f`

Package/setup union:12,201 artifacts /1,803,601,640bytes in both fresh brackets.
Pinned core compiled superset:12,592 artifacts /2,125,623,224bytes in both brackets.
The package union is the actual MainLemma/Main setup.importArts union plus existing split
companions, **not** the exact loaded closure and **not** all implicit Init/core inputs.
The core catalog is the entire installed pinned lib/lean compiled-artifact SUPERSET, also
**not** an exact loaded-module closure. Actual direct `--deps` rows include implicit Init and
are separately freshly verified against these catalogs. The before direct list has10 rows,
selected list9 because the redundant explicit Interval import is gone. ML/Main setup bytes,
importArts and options are exactly identical with/without it (`setup-comparison.json`).
Initial before-golf catalogs are additionally preserved: package12,201/1,803,599,656bytes,
core12,592/2,125,623,224bytes. The changed project artifact size is observed, not forced.
Fresh external-catalog reuse is hybrid: all actual referenced files were freshly hashed first;
new helper project artifacts were independently copied/hash-checked. No historical hash is invented.

## Rejected/negative evidence (preserved)

* `beforeH4-profile` and `beforeH4-independent`: overlapped native/compiler work; both explicitly
  REJECTED, no positive timing/gate credit. The independent run also failed ToMessageData logging.
* The first parser attempt ran before the raw profiler stream finished and found no marker;
  its error is retained in the conversation; no timing was extracted or credited from it.
* `mechanical-negative`: intentional whole exit1 for Finite/r/B/Sort/Classical/Int-ascription drops;
  no partial line in that run is positive proof evidence.
* `positive-alternatives`: whole exit1 (mt hs inference and raw AST guard), rejected entirely.
* `positive-alternatives-v2`: whole exit0; corrected support implication and closed/std3 alternatives.
  Its generic PASS label overstates the ascription-removal branch's AST status: an explicit preceding
  line says RAW AST EQUAL false and actual isDefEq true; that branch is not selected. Selected
  simp/drop-show alternatives pass exact AST and closed VALUE guards.
* Whole automation attempts fail; apply? only supplies partial/synthetic suggestions, not a proof.
  The first JSON-export attempt failed Unicode encoding; the exact stored tool response was then
  saved successfully via ASCII-escaped transport in `automation.json`.

## Artifacts, release and remaining owner work

Artifact root: `/private/tmp/roth-mainlemma-box-family-finsupp-helper`.
`artifact-manifest.json` schema `roth-helper4-artifact-manifest/v1` enumerates actual saved file
bytes, SHA256, strict-UTF8 result and explicit binary exceptions. It includes the report,
source/variant files, raw failures, instruction copies, every copied project companion and
catalog metadata. The package/core external files are referenced through their separately
freshly observed complete catalogs; they are not falsely described as copied or exact loaded
closures. `recovery-comparison.json` proves binary/catalog/source/cache equality across the pair.
`final-drain.json` freshly checks all20 owned compiler/profile PGIDs absent and all final native
requests complete; the persistent LSP server was not killed. No child agent or background job
was started. Source, helper, compiler, native, profile and report leases are all released at END.

All11 worker checks are satisfied in this scoped workflow: reference reads; full24 audit;
five-method status; outer+effective-inner generality; final packing; inequality scan;
all42-rule pass; step-back; complete native diagnostics; actual diff/build/semantic gates;
rename handling (none required, shared queue untouched). ModeB phases0–7 are represented above;
full-file global simplify/reviewer/cumulative/public+retained-axiom/import-doc-comment checks,
ALL-row performance, final Eval/publication/push remain the owner's later work.

Resume the **same original18 worker only after owner review and END**. Preserve helper/source SHA
above, capture expanded BEFORE on untouched old public count+direct consumer+audited helper before
public API edits, and include actual pinned Lake as well as Lean executable hashing in future
provenance (the inherited resolution18 proxy-only handling is insufficient). No original18/19 or
264-count credit is claimed by this helper report.
