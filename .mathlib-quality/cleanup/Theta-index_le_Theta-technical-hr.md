# Dedicated original9 revisit — remove technical `index_le_Θ.hr`

Applied only the selected public hypothesis removal and three routine call-argument deletions.
`Roth.index_le_Θ` now accepts arbitrary natural weights, including zero weights; its original
one-line `le_csSup` proof is byte-identical. Public definitions, domains, conclusion, name and
visibility remain. The two internal calls are in `index_separated_mul_le_aux` (Theta438/440);
the external call is in `main_lemma` (MainLemma676). No other direct calls exist in repository
Lean sources. `Θ_unique_le.hr` remains for its separate checkpoint. All protected Θ premises,
hq/header/wrapper/domain choices remain. No new helper, rename or original-count inflation:
original216/264, Theta35/35,9/14 files remain owner counts.

Artifacts below live in `/private/tmp/theta-index-technical-hr/`. Owner retains Git/shared-log
ownership and final full-build→separate-LeanEval/publication gates. This report does not certify
those owner gates before the owner runs them.

## Preparation and baseline

Read the authorized dispatch, leaf instructions, Lean4/mathlib-quality skills, installed cleanup,
cleanup-all/buzz workflow and required golfing-rules/proof-patterns/mathlib-search/
generalisation-patterns/cleanup-gates/profiling references; relevant formatting, naming,
documentation, hypotheses, inequality and visibility guidance. Read current target/context,
all direct callers, original2b source and original9 reports, reviewer candidates/inventory, and
the migration requirements. Reviewer full-copy candidates contain both technical removals and
were not copied into production. This checkpoint removes only index_le_Θ.hr.

Baseline HEAD `af23763141cda3be5157d5662ba440c5e1e99448`, source
`1b62c7dd177609e4cf6544e8c06b9ead761506122391e2345fd5db35fa46b4cc`, MainLemma
`ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4` were verified.
Baseline doctor uses the dispatch's completed sequential owner full build75.708s then separate
LeanEval52.572s and identical-source complete native diagnostics (8 Theta warnings,0errors).
Cache fetch and separate runLinter unnecessary; native supplies actual diagnostics. Fresh
`baseline-source-pin-hashes.json` records all17 sources/pins at this window, rather than claiming
an inherited pre-publication map certifies current bytes. `protected-report-hashes.json` records
all current Theta reports, including the untracked final-simplify report SHA
`484a772138314b48bf1793e71aa2b4013b49aa37c3b377ca8a3189746b329576`, protected unchanged.

`Candidate.lean` independently elaborated the exact pre-target source prefix with only hr
removed, exit0. Only after that concrete evidence was the narrowly matched production edit
applied. Final target signature is packed to95 codepoints on its first line.

## Full fresh24audit

|#|Item|Concrete result|
|---|---|---|
|1|LINT|Remove unused hr; retain every other protected unused premise without underscore suppression. Fresh native results below.|
|2|HAVE SCAN|No `have` in target; no intermediary to inline. Necessary caller expression arguments alone change.|
|3|SET_OPTION|No target option or limit raise; exploration lowers heartbeat allowance to2000 only in scratch.|
|4|SIMP SQUEEZE|Selected proof has no simp; fresh anonymous simp trial leaves index≤supremum.|
|5|NAMING|index_le_Θ names mathematical operands and ≤ in order; no forbidden abbreviation, numeric scheme or single-letter declaration.|
|6|LINE PACKING|Every signature line measured below,95/43/78 including the final :=; no complete following argument/conclusion fits.|
|7|BY PLACEMENT|Direct term, no by wrapper.|
|8|FORMAT|4-space signature continuation,2-space body, no internal blank line or new haveI/letI; ordinary lambda ↦.|
|9|COMMENTS|Entire target docstring and all proof comments unchanged. Internal membership rfl preserved.|
|10|DOCSTRING|Existing public application-facing mathematical assertion and §5 attribution remain accurate for all weights.|
|11|VISIBILITY|Public domain API retained as explicitly chosen; external MainLemma caller remains.|
|12|STRUCTURE|Body1line≤ordinary30; target not among module's seven Main results. No conjunction conclusion or branch>10; no helper warranted.|
|13|MATHLIB|Five actual searches find le_csSup already used directly. No missing generic API; explicit public-wrapper preference preserved.|
|14|JUNK DEF|n/a theorem; no definition edit.|
|15|EXISTS LEMMA|n/a public inequality, not private one-use existential lemma. Correlated set witnesses remain together.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective binder audited with fresh drop/weakening probes; only selected hr removed. Full original adapter and current actual metadata below.|
|19|INEQUALITY|Only index≤Θ after removal; no ≥/> Lean comparison.|
|20|NORMAL FORM|Canonical element≤supremum; generic le_csSup already matches.|
|21|SYNTAX-GEN|Membership/coprimality arguments remain directly applicable; zero-weight calls no longer need an impossible positivity proof.|
|22|IMPORT-FANOUT|n/a no import added/removed.|
|23|CASTS|No cast diff. Int/nat→real in numerator/denominator and Int.castRingHom ℝ are genuine bridges/codomain choice.|
|24|INSTANCE-NAME|No instance declaration. Anonymous instance generated names exempt, actual domain/order/BinderInfo retained.|

## Signature packing and inequalities

Actual `#check @Roth.index_le_Θ` is captured in final semantic logs at format.width100.
`packing.json` contains the measured table, codepoints rather than UTF8 bytes.

|Signature line|Chars|Next complete argument or conclusion|Arithmetic|Action|
|---|---:|---|---|---|
|93|95|`(hh : ∀ j, IsCoprime (h j) (q j : ℤ))`37|95+1+37=133>100|ok|
|94|43|entire dependent index≤Θ conclusion with :=,74|43+1+74=118>100|ok|
|95|78|proof next|n/a|ok|

The conclusion is one mathematical expression; it cannot fit on the preceding hypothesis line.
The existing return-expression wrapping stays intact. Inequality inventory:

|#|Location|Expression|Decision|
|---|---|---|---|
|1|conclusion|`index … ≤ Θ B q r`|canonical|
|2|all signature hypotheses|zero ≥/> comparisons|no rewrite/rename|

## Five actual mathlib searches and abstraction check

Raw `native-search-{finder,loogle,search,local}.json` and untruncated `mathlib-source.log`.

|Method|Fresh query|Inspected result|
|---|---|---|
|A Lean-Finder|Every member of a bounded above set is at most its supremum|le_csSup, ConditionallyCompleteLattice.le_csSup, le_csSup_of_le, le_sSup, le_ciSup|
|B Loogle|`BddAbove ?s → ?a ∈ ?s → ?a ≤ sSup ?s`|le_csSup, DirectedOn.le_csSup|
|C LeanSearch|An element of a bounded above set is less than or equal to its supremum|le_csSup, le_csSup_of_le, le_sSup, le_csSup_iff', le_sSup_iff|
|D source rg|full le_csSup/le_csSup_of_le/le_csSup_iff declarations, Mathlib/Order/ConditionallyCompleteLattice|Basic.lean197/205/213 and variants, source read in context|
|E local name|le_csSup,limit15|8 source hits including DirectedOn/Monotone/iff/of_le; index=unavailable so no empty-index absence claim|

Auxiliary routes inspected: le_csSup_of_le, le_csSup_iff/iff', le_sSup, le_ciSup,
DirectedOn.le_csSup and csSup_le. Common-equivalents bucket: order/supremum, not a disguised
new predicate. Inversion fires: the index is simply a member of a bounded set and the remaining
argument is abstract order theory. A `ConditionallyCompleteLattice` example using le_csSup
compiles in Positive/Generality. No new abstract helper is needed. The protected domain-facing
wrapper remains; this is not an unsupported claim of mathematical absence.

Clean anonymous probes in `Automation.lean` preserve the exact pre-target imports/source, close
the old section context, then reopen Roth with only the current Fintype section instance.
They use the literal new header, no imported Roth.Theta, no failed named candidates and no
target/later theorem to contaminate exact?/apply?. `PrefixAbsence.lean` independently succeeds,
asserting both qualified/public and private-suffix absence for index_le_Θ/Θ_unique_le/
index_separated_mul_le_aux/main_lemma, with positive indexSet_bddAbove/Θ/le_csSup controls.
grind[Θ,indexSet], aesop, simp[Θ,indexSet], rfl and gcongr fail; exact?/apply? are bounded at2000
heartbeats and inconclusive. The preliminary automation run retained the inherited DecEq context;
it is retained as historical exploration. The first reopened-context correction omitted `open MvPolynomial` and produced unknown-map header errors; that failed scratch artifact is preserved. `automation-clean-final.log` restores the open declaration; `automation-literal-final.log` additionally matches final signature line packing verbatim and is the definitive current-goal run.
Known full-Theta multi_attempt stalls were not repeated. Expected-failure exit1 exploration
never certifies a proof, absence or axioms.

## Every effective parameter, drop and weakening

`Binders.lean` uses autoImplicit=false in a separate context; `binder-ranges.json` gives named
trial source ranges. The negative file is expected exit1. `Positive.lean` and `Generality.lean`
are separate successful independent direct le_csSup proofs. Failures demonstrate these candidate
proofs/types fail, not that no deeper mathematical generalization can exist.

|Parameter|Role and actual fresh probe|Decision|
|---|---|---|
|σ:Type*|Drop produces unknownσ; all positive/actual checks remain universe-polymorphic.|retain type domain/universe|
|Fintypeσ|Drop fails instance synthesis. Finiteσ plus explicit local Fintype.ofFinite in conclusion/proof compiles.|retain selected finite-enumeration API; no unrelated class change|
|B:ℝ|Drop unknownB. Independent proof works for arbitrary B.|retain project real bound; abstract order form already le_csSup|
|q:σ→ℕ|Drop unknownq. Positive proof accepts arbitrary q, no positivity demanded.|retain denominator data/domain|
|r:σ→ℕ|Drop unknownr. No-hr/weak-hr/zero-weight cases compile.|retain weights, remove only positivity premise|
|hr:∀j,0<rj|Drop compiles; weak ∀j,0≤rj compiles; strongest version needs no premise.|remove as selected|
|R:MvPolynomialσℤ|Drop unknownR; arbitrary membership-satisfying polynomial accepted.|retain dependent datum|
|hR:R∈RSetBr|Drop unknownhR; weakening to R≠0∧degree bound fails missing coefficient-bound membership construction.|retain complete RSet membership|
|h:σ→ℤ|Drop unknownh (some secondary bounded elaboration errors).|retain evaluation datum|
|hh:∀j,IsCoprime…|Drop unknownhh; existential-coordinate replacement fails expected universal type.|retain pointwise coprimality|

Historical DecEq removal remains valid; it is absent from the actual new telescope, not silently
reintroduced. No algebraic-parent, point-localization or strict→weak candidate applies beyond
these rows: project definitions fix integers, naturals and reals. No undecidable preference gap.

## Public literature

Read clean.tex644–669: the original exposition assumes positive r/q and B≥1 and defines Θ as
the supremum of exactly the bounded-polynomial/copime-coordinate indices. The current index
convention and already generalized boundedness proof support zero weights; this conclusion
comes from kernel checks, not an inference from a search snippet.

Fresh web queries: `supremum least upper bound every member bounded above set` and
`Roth theorem index supremum Theta polynomials weights`. Generic top hits included ScienceDirect
least-upper-bound overview, [Gressman's Advanced Analysis](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html),
and [MathWorld Supremum](https://mathworld.wolfram.com/Supremum.html). A targeted third query, `Roth theorem "index" "supremum" polynomials Theta`, returned [Princeton Roth lecture](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), [Quantitative Roth–Ridout](https://citeseerx.ist.psu.edu/document?doi=97e1f64a69bd280d0abc586cb61277fbd390e499&repid=rep1&type=pdf), and [Diophantine Approximations](https://simonrs.com/eulercircle/irpw2022/leo-diopapprox-paper.pdf) as its top three specialized discovery hits; no further API claim follows from those snippets. The primary lecture source
defines a supremum as an upper bound, directly matching le_csSup. Specialized discovery included
[Roth's Theorem lecture notes](https://www.math.uh.edu/~minru/fields/roth.pdf); no claim of a
zero-weight literature theorem is based on that snippet. ChatGPT math MCP unavailable in exposed
tools. No literature-driven broader API change recommended in this selected checkpoint.

## All42golfing rules

|Rule|Concrete outcome|
|---|---|
|1.1 by exact|Already direct term.|
|1.2 by rfl|None.|
|1.3 rw/exact|No rw.|
|1.4 simp/exact|No simp chain.|
|1.5 trailing rfl|Membership rfl is required equality evidence, not redundant tactic.|
|1.6 constructors|Already anonymous correlated set witness.|
|1.7 apply/exact|Already direct le_csSup application.|
|1.8 contradiction|None.|
|1.9 eta|Cast/division lambda is not eta-reducible.|
|1.10 have|None in target.|
|1.11 apply/intro|None.|
|1.12 show|None.|
|1.13 projections|No have/projection chain.|
|1.14 rw merge|No rewrites.|
|1.15 terminal simp|None selected.|
|1.16 nonterminal simp|None selected.|
|1.17 dot notation|le_csSup's boundedness/member application already direct.|
|1.18 parentheses|Parentheses around boundedness application delimit its argument.|
|1.19 push_neg|None.|
|1.20 existential helper|No private witness helper to inline.|
|2.1 grind|Fresh clean anonymous trial fails.|
|2.2 grind predecessors|No retained grind/predecessors.|
|2.3 simpa|Fresh simp trial leaves goal; no chain to consolidate.|
|2.4 fun_prop|n/a no function-regularity conclusion.|
|2.5 positivity|n/a arbitrary index≤supremum, no positive arithmetic goal.|
|2.6 gcongr|Fresh trial makes no progress.|
|2.7 lia/omega|n/a no integer linear arithmetic goal.|
|2.8 aesop|Fresh clean anonymous trial fails.|
|2.9 norm_num/cast|n/a no concrete computation/cast equality.|
|2.10 decide|n/a arbitrary real-order membership property.|
|2.11 field_simp/ring|n/a no algebraic identity or denominator manipulation.|
|2.12 linear_combination|n/a no ring terminator/certificate combination.|
|2.13 wlog|n/a no symmetric branch cases.|
|2.14 calc|Already direct term, no calc.|
|2.15 <;>|No unresolved similar goals.|
|3.1 erw|None.|
|3.2 continuity|None.|
|3.3 omega/lia|None.|
|3.4 rcases/rfl|No destructuring, only necessary member equality rfl.|
|3.5 attributes|No new simp/grind attribute justified by this usage.|
|3.6 simp_all|No selected simp_all.|
|3.7 options|No production option/scaffolding.|

Step-back/manual holistic simplify: direct le_csSup with the actual membership witness is already
one line. Search automation adds work and no clarity. No missing proof skeleton, helper or
decomposition action; public wrapper preference is explicit. No callable built-in simplify skill
is exposed, so this is a documented manual holistic pass. MainLemma's existing long proof is
only an affected routine caller here, not another declaration cleanup or a performance claim.

## Static scope, preservation and exact callers

`static.py` asserts entire Theta equals the baseline with exactly the target signature and two
call-argument replacements; entire MainLemma equals baseline with exactly the one call argument
removed. `Theta-scoped.diff`/`MainLemma-scoped.diff` are concrete reviewable diffs. All50 Theta
declarations inventoried in `Theta-declaration-inventory.json`:48 unrelated source declaration
slices byte-identical, target body byte-identical, whole affected internal caller independently
copied. `MainLemma-declaration-inventory.json` proves every other source declaration identical;
the entire actual updated main_lemma and helpers are independently re-elaborated, not a snippet.
MainLemma hr0 still has real uses in four_lt_rpow,three_small_factors/card_filter_weight_le and
remains in its original public telescope. No docstring/comment/import/definition/limit edits.

## Eleven-step checklist

1. References and current/baseline context read.
2. Full24audit above, all items concrete.
3. Step2.5 all five actual searches and auxiliary variants.
4. Step2.6 every binder, weakening, inversion and public literature.
5. Step2.7 measured full signature packing.
6. Step2.8 full inequality inventory.
7. Step3 all42golf statuses above.
8. Step4 independent holistic reflection, no helper warranted.
9. Step5a fresh complete unfiltered native validation recorded below.
10. Step5b exact module/type/value/trust/migration/profile gates recorded below.
11. Step6a no rename required, owner sidecar untouched.


## Full original/current contracts, entire callers and trust

Fresh module gates ran in order: `lake build Roth.Theta` exit0,28.054s, then
`lake build Roth.MainLemma` exit0,35.028s. Complete unfiltered native diagnostics return
success=true,partial=false,timed_out=false,failed_dependencies=[] for both files: Theta0errors/
7warnings, MainLemma0errors/3warnings. Exact diagnostic delta removes only Theta93's unused hr
warning; all other messages/locations/categories/severities are unchanged. No warning suppression.
Raw JSON and source-hash binding are `native-{theta,mainlemma}-final.json` and
`native-final-source-binding.json`.

`Independent.lean` independently re-elaborates the immutable complete original Index and Theta
namespace (including original9's full old proof), all actual current Theta declarations and all
actual updated MainLemma source proofs/helpers in distinct namespaces. It compiles exit0 in
103.800s. New current index_le_Θ uses its own copied boundedness proof and direct le_csSup;
it neither aliases nor calls the actual Root target. Current full caller proofs are copied in
full, not a short call-site test. Current MainLemma proof and all its copied constants are
checked against Root MainLemma/private-helper self-use, with complete value/type/axiom checks.
Actual Root caller and independently elaborated callers have positive target dependencies.

`immutable-original9-source-binding.json` confirms the complete original2b index_le_Θ declaration and proof occur verbatim in the preserved canonical namespace.

Full original index_le_Θ telescope has11 binders (σ,Fintype,DecEq,B,q,r,hr,R,hR,h,hh).
Explicit `TechnicalHrAdapters.fullOriginal` preserves ALL argument names/order/BinderInfo,
universes and the whole conclusion, and calls the new actual Root theorem with the retained
arguments. The independently generated full old λ is also kernel-checked. Exactly the already
approved DecEq and newly selected hr are dropped relative to original2b. Actual new telescope
has9 binders, with exactly the retained names/order/BinderInfo/domains/conclusion and no hr/DecEq
AST binder. Actual full MainLemma contract has26 binders unchanged. Entire affected internal
consumer has16 binders unchanged. Synthetic anonymous instance names alone are exempt from
spelling equality; class type/order/BinderInfo stay exact. Private suffixes are resolved uniquely.

Positive `zeroWeights` calls the actual Root target with `r := fun _ ↦ 0`, not an old compatibility
wrapper. Standard axiom sets are exactly `[propext, Classical.choice, Quot.sound]` for each of:
independent original index_le_Θ, actual index_le_Θ, independent new index_le_Θ, full-old adapter,
zero-weight adapter, actual/independent whole index_separated_mul_le_aux, actual/independent whole
main_lemma, and the retained Θ_unique_le. Every opaque proof uses `value! true`; inferred proof
type is checked against the full constant type. Logs are clean of errors/PANIC/sorryAx.

## Inverse-recoverable cumulative migration

`ImmutableInput806.lean` preserves the complete preceding806-check input,692893 bytes,SHA
`80f9e72e4f94b13ede0a1c51660a8a6c9c574aae8eeaf15be42241cf58999a47`.
Four explicitly labelled HISTORICAL COMPATIBILITY contexts are inserted OUTSIDE immutable
blocks, before namespaces Theta35CallerOriginal,Theta35CallerUpdated,Index28RevisitIndependent,
SeparatedRevisitCurrent. The first resolves old calls through the independent original theorem;
the others accept the preceding hr contract and call the actual new Root theorem. The old
canonical proof bodies are never edited to fit a new API. Prior CurrentMainLemma and the
Index28/SeparatedCurrent old-call copies are historical compatibility evidence; fresh
TechnicalHrMain/TechnicalHrCurrent checks certify the NEW actual Root semantics separately.
No historical wrapper's type is mislabelled as the actual new Root target type.

`migration-operations.json` records precise insertion byte offsets and complete inserted bytes.
`inverse.py` reads the FINAL cumulative scaffold, removes its appended tail, then reverses all
four insertions. Its actual run reconstructs all692893 input bytes, byte-for-byte and hash-equal,
as `InverseRecovered806.lean`; this is stronger than selected-block preservation. The migrated
prefix is694651 bytes,SHA `5aa5cc5a2559aa734e53688e5978a2fdb1377a45ca89a3e908944415a5e95a35`.
This is a migrated prefix, not an unchanged806 byte prefix.

Four complete canonical blocks remain byte-identical at these accurate FINAL byte spans:

|Complete canonical block|Raw byte start|Raw byte end|SHA256|
|---|---:|---:|---|
|Original Index|1414|15125|`72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`|
|Original Theta|16628|68797|`355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`|
|Whole original2b MainLemma|70720|106186|`96f1abe996f5a0bc024939263ab8e92f355ba531dd87357d8de28871b715024a`|
|Whole preceding current MainLemma|118124|153674|`859af5c80ed9022535c15ba6a5d36e206ae63345d6d91133b1d2bf3a8130fe41`|


Fresh `ActualSemanticsAugmented.lean` compiles exit0 in352.304s. All806 preceding marker
categories and counts remain, with249 additional PASS markers,1055 total. The appended new
direct checks contribute131 markers in the cumulative environment, compared with133 in the
standalone environment; the only difference is compiler-generated `TechnicalHrMain.eta._proof_1`
and `TechnicalHrMain.lam._proof_1` constants absent from the cumulative namespace. All actual
source declarations, whole proofs and source value/type/axiom checks are present in both runs;
the inventory difference is explicit in `generated-mainlemma-inventory-difference.json`.
Compiler reuse of generated proof auxiliaries is the inferred explanation, not an omitted probe.
The first postprocessing assertion incorrectly demanded equal generated-auxiliary counts; it
was corrected to this exact two-name inventory check. Both compiler runs had already exited0;
no proof/source change or compiler rerun was needed for that accounting correction.

All29 original public full-contract adapters and five definition values are freshly kernel-checked
using the aligned owner verifier tail. Its only generator change is adding `(index_le_Θ,[hr])`
to namedDrops; owner scripts were not overwritten. The concrete copy is
`all29-owner-aligned-tail.lean`, with precise owner patch note `all29-generator.patch`.
All prior original/helper/FIRST/provenance evidence stays retained.23 combined FIRST/provenance
artifacts and81 current protected Theta reports match their hashes throughout this window.

Final cumulative scaffold SHA256
`903f10bdf10c4be5508886910804af3ebca2f978f5eafbc5116ddef2f5ee8da7`;
independent scaffold SHA256
`2a7da94b2c5e117d81346f04bd8a9b8bd0a511e93007193867979cfd540262fa`.
`semantic-marker-summary-final.json` is the complete normal/native/marker/delta result.

## Actual-file profile — scoped API checkpoint acceptance

All ordinary/native requests returned and13 recorded owned process groups were dead before
the real final command:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Theta.lean`.
It exited0 in215.897s with no Lean limit change or production scaffolding. This is the ACTUAL
whole source, not a prefix or renamed proof.50/50 retained declarations have source anchors;
every theorem/lemma has exactly one actual async proof anchor. All50 totals are below1000ms;
maximum855.603ms at lem7_Φ_bound. No new unrelated over-budget queue. Own target/direct local
consumer are both below750ms, so the scope's exact-repeat trigger does not fire; no repeat or
third unchanged-source sample was run.

|Declaration|Inherited before first/repeat|Fresh final actual total|
|---|---:|---:|
|index_le_Θ|51.095/39.828ms|38.121ms|
|index_separated_mul_le_aux|654.400/679.144ms|679.595ms|

Before values are explicitly inherited from accepted actual profiles on the exact initial1b62
source, with raw/status/table/source hashes verified in `inherited-baseline-profile-binding.json`.
No speedup is claimed from this small API change; the proof body is unchanged. Final accounting:

|Scope|Outer enclosing command|Async proof|Async addDecl|Async linter|Other disjoint async|Total|
|---|---:|---:|---:|---:|---:|---:|
|index_le_Θ|10.797|7.253|2.636|17.435|0|38.121ms|
|index_separated_mul_le_aux|48.464|545.989|14.268|70.872|0.002 realizeConst|679.595ms|

The enclosing omit command includes its nested theorem/lemma command; nested commands/kernel/
tactic times are not added again. All associated disjoint top-level async rows are included,
including both addDecl rows for the direct consumer. Full raw UTF8 stays unmodified; parser
uses strict decoding, zero invalid/replacement sequences, exact raw offsets, SHA256 and slices.
Target raw span[7882995,8007972),slice SHA
`15524213d289ca2fa5ad5ff7b169cb987c471424d91163724578c5339a0a21ba`;
consumer span[79437734,86488456),slice SHA
`a8a295476f9904b24d048b73c0afc3ebd2be8732126587a2bb77784f84e1c172`.
`actual-profile-final-first-table.json` retains all50 rows. Unrelated rows in[750,1000) are
index_det_le766.943,mapped_det_ne_zero_aux851.685,lem7_Φ_bound855.603,lem7_numeric766.818,
theta_delta_succ_lt_aux812.652,theta_prefix_lt_aux786.339,theta_phi_lt_aux750.017,
theta_lt_succ_aux811.921ms; none is hidden or relabelled by a lower repeat.

After that profile drained, one fresh actual MainLemma attempt used the same real flags with
an external60s bound, without any Lean limit increase. It was terminated/drained at60.024s,
exit-15,timeout=true, before main_lemma's source anchor (5/27 source declarations reached).
Finite actual `main_lemma` timing therefore remains UNAVAILABLE. Raw output is preserved and
strict UTF8-valid in `actual-mainlemma-profile-bounded.log`; machine result
`actual-mainlemma-profile-summary.json` explicitly distinguishes this incomplete performance
attempt from successful normal/native/independent whole-caller semantics. No normal/native,
renamed-proof or prefix timing substitutes for the unavailable actual caller timing. No whole-
project performance claim.

## Final gates

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Fresh Theta→MainLemma module builds,0errors|
|definition_protected|pass|No definition, import or domain diff; all29/five-value old recoveries|
|theorem_statement_protected|pass, authorized exception|Only selected hr removed; full original11/new9 metadata and adapters|
|caller_contracts|pass|Actual whole MainLemma26/internal consumer16 metadata, whole independent proof/value/axes/nonself/dependencies|
|structure/naming/packing/inequalities|pass|Body1line/no branch, descriptive name, complete measured tables|
|native diagnostics|pass|Complete unfiltered0errors,7/3warnings, exact one-warning removal|
|trust|pass|All scoped actual/original/adapter/current/caller sets exactly standard trio|
|cumulative migration|pass|1055 checks, all806 retained, all four canonical blocks, entire input inverse recovery|
|preservation|pass|48 unrelated Theta slices, all unrelated MainLemma slices,23 FIRST/provenance and81 reports preserved|
|actual Theta performance|scoped pass; final whole-file gates pending|50/50 under1000; scoped38.121/679.595ms; no repeat trigger or unrelated failure|
|actual MainLemma performance|unavailable|Bounded attempt drained before target; no proxy claim|
|owner full build→separate LeanEval→publication|pending owner|Not run or claimed by this worker|


## Terminal freeze and handoff

Final Theta SHA256 `0afac9d3af66eb80eab0bc2d8aa9c50dd2f61d693ff0868663b274a550509763`.
Final MainLemma SHA256 `a002b02724dc9f4bcef52280bc96c736eb2fd9acbc06b5352c6eff55b94dd689`.
All17 current source/pin hashes are in `source-hashes.json`; all actual final checks bind to
these source bytes. Existing final-simplify report remains SHA
`484a772138314b48bf1793e71aa2b4013b49aa37c3b377ca8a3189746b329576`.

`final-process-drain.json` records15 owned process groups dead, every native request complete,
normal_pending=[],native_pending=[],pending=[]. No systemwide ps scan is claimed. No Git/shared-
log/rename-queue mutation. Source, scratch, report, compiler and native authorities are REVOKED;
compiler/native window RELEASED at terminal handoff, with no further worker edits or requests.
`final-freeze.json` freezes the exact report/source/scaffold/canonical/FIRST/pin/artifact hashes.
Owner must verify this handoff, run frozen full `lake build` THEN separate `lake build Roth.LeanEval`,
and publish this checkpoint before any subsequent Θ_unique_le.hr source edit. Owner will publish
the protected untracked final-simplify report alongside this dedicated report.


## Owner independent review and scope clarification

Exact frozen report archived at /private/tmp/theta-index-technical-hr/leaf-final-report-owner-input.md, SHA256 `1317b679df05996397585a7fa7cf96eb2765d5a4d275bf16f26c64c62db29912`. Owner independently verifies17source hashes,3pins,23FIRST paths,213artifacts and fourcanonical blocks before ownerbuilds. owner-checked.json independently reconstructs all692893 prior bytes and checks exact publicbinder/threecaller edits,1055markers/all806prior counts, new actual contracts/native0errors7/3warnings and all50disjoint profiletotals/strictUTF8slices. owner-exploration-caller-check.json verifies7literal actual final anonymous headers/located errors; exact?/apply? boundedtimeouts remaininconclusive. new-declaration.lean is an earlier unpacked candidate; production and definitive Automation.lean headers match final95-character packing.

Two generated MainLemma auxiliaries absent cumulatively account for2fewer directmarkers;2added historical-wrapper proofchecks account for the opposite category delta. Standalone249/netnew249 therefore do not imply identical categories; exact differences are verified, no sourceproof/type/value/axiom check omitted. Historical compatibility wrappers are labelled and distinct from new actualRoot semantics.

The performance heading/table is narrowed from the frozen FAST BOARD wording: this is scopedacceptance. Own target/localdirectconsumer below750 require no scopedrepeat. Other declarations reach750 in this capture, so final owner whole-file performance requires the appropriate same-final-source repeat after final changes/review. MainLemma actualfinite timing remainsunavailable after60s cutoff beforetarget. No final whole-file/project performance pass is claimed.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 78.617 s and 56.394 s.
Theta SHA256 `0afac9d3af66eb80eab0bc2d8aa9c50dd2f61d693ff0868663b274a550509763` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p12-full.log` and `/private/tmp/roth-theta-p12-leaneval.log`; machine record
`/private/tmp/roth-theta-p12-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 9 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
