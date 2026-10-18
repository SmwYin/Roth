# Dedicated cleanup: private `index_unique_le_log_div`

This is the fresh, separate audit of the ONE helper introduced while auditing original20,
`Θ_unique_le`. It does not increment original-declaration counts. Initial working Theta SHA256:
`56a5db29f3c368733fc4adb065ceb265586d0b2ecb80b6d7116bde24c771ce58`.
Evidence directory: `/private/tmp/roth-theta-log-helper/` (all paths below relative to it).
Initial exact source is `initial.lean`; exact helper text is `initial-helper.txt`; their hashes
are recorded in `manifest.json`. Snapshot preceded all production edits. The owner's concurrent
docs-only commit b68de204130d4ad9c7120ffc4f5b25fc9bcc6e5c changed no Lean source.

## Result

The private individual-index estimate now accepts arbitrary natural weights, including zero,
and assumes only a bound on the leading coefficient of the equivalent univariate polynomial.
Division by a nonnegative natural cast preserves the multiplicity inequality; strict weight
positivity was unnecessary. Two single-use no-`by` intermediates are inlined. Helper proof26→23
lines, public caller proof2→3, total Theta981→979. No additional production helpers introduced.

The public `Θ_unique_le` retains **every** original parameter, domain, conclusion, name and
BinderInfo except the previously approved DecidableEq removal. In particular hB, hr and Fintype
stay exactly as dispatched. Its proof supplies the leading coefficient's bound from the uniform
coefficient bound. Public hr becomes intentionally unused; its warning stays visible, unsuppressed.
The owner scoped this helper audit to private assumptions and retained the public parameters,
consistent with the user's earlier positive-weight API preferences. No public hr removal is proposed.

## Preparation and baseline doctor

Read the complete lean4 and mathlib-quality skills, complete cleanup command, complete golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates and profiling references,
complete naming reference and relevant style rules. I have read golfing-rules.md, proof-patterns.md,
mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.

Inherited matching baseline evidence from the preceding dedicated original20 report is explicit,
not represented as fresh: `/private/tmp/roth-theta-unique/module-final.log` records successful
`lake build Roth.Theta`; `final-lsp.json` is complete/unfiltered, success=true, partial=false,
timed_out=false, failed_dependencies=[], 0errors/16warnings on the exact initial SHA above.
The helper/public declarations themselves initially have no warnings. The owner supplied the
accepted uncontended exact-prefix baseline helper454.013ms/public43.093ms, combined497.106ms,
raw `final-profile.log`, anchors and `timings.json` under that same preceding evidence directory.
No repeated identical baseline doctor or profile was needed. Owner whole-project and separate
LeanEval gates are reserved for after this audit; they are not claimed here.

## Full substantive 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | No initial helper warning. Public hr becomes unused by the authorized private generalisation; retained per explicit API choice. All other baseline warnings outside this scope. |
| 2 | Have scan | hlogq:no-by,1use→inline Real.log_pos. hrpos:by,1use→delete with private hr. hR10:no-by,1use→inline injectivity. hcoef:by,1use→replace its uniform hypothesis by its actual leading-coefficient input. hmapeq:by,1use→keep genuine extensionality proof. hmult:by,1use→keep genuine field-map proof. hlog:no-by,used by rw and final inequality→keep. |
| 3 | Options | No production options, limit changes or trace scaffolding. Automation scratch alone lowers heartbeats to20000. |
| 4 | Simp | hmult terminal simp unchanged; final simpa remains terminal. Removed helper hcoef's terminal simpa only; its caller conversion uses focused simpa only because tested unsqueezed simpa hits default maxRecDepth. No limit raised. |
| 5 | Naming | Descriptive snake_case mathematical index/log/divisor estimate; no forbidden pattern or abbreviation. Name was explicitly selected by owner. No rename needed. |
| 6 | Packing | Full five-line before/after measured table below; every retained signature break justified. |
| 7 | By | All by tokens end their preceding declaration/have lines. |
| 8 | Format | Two-space proof indentation, four-space signature continuations, no blank proof lines/semicolon chains/haveI/letI, lambdas ↦. |
| 9 | Comments | Initial helper has no comments; public original source-aware documentation preserved byte-for-byte. No narrative removed. |
| 10 | Docstring | Private helper has none as required; public docstring retained. |
| 11 | Visibility | Mathematical implementation bound remains private; public wrapper preserved. Classic file dialect. |
| 12 | Structure | Helper23≤30; public3≤15. No ∧ conclusion or >10-line branch. hmapeq5lines/hmult7lines (including headers) do not trigger extraction. No further helper warranted. |
| 13 | Mathlib | Five actual fresh methods + auxiliary searches and clean compiled generic-route probes below; partial ingredients used directly. No complete replacement found. |
| 14 | Junk def | n/a: theorem, no definition introduced. |
| 15 | Exists | n/a: no existential conclusion/trivial witness lemma. |
| 16 | Show/change | Neither occurs. |
| 17 | Push-neg | None. |
| 18 | Generalise | Every effective initial binder probed below. Remove private hr; localize hRB. Retain Fintype object's presentation and bundled Unique; no public changes. |
| 19 | Inequalities | Complete occurrence table below; no reversed code inequalities. |
| 20 | Normal form | Existing index and canonical polynomial rootMultiplicity/log forms retained; no new equivalence or simp normal form. |
| 21 | Syntax generality | hRB directly matches pow_rootMultiplicity_le's leading-coefficient API; public application recovers it in one small coefficient conversion. |
| 22 | Imports | No imports added, removed or reordered. |
| 23 | Casts | New Nat.cast_nonneg supplies genuine ℕ→ℝ order bridge. Remaining ℤ→ℝ/ℚ and ℕ→ℝ/ℚ/ℤ casts are cross-domain; Polynomial ℤ and `(0 : ℝ)` are load-bearing. No redundant new coercion. |
| 24 | Instances | No instance declarations, explicit generated names, priorities or global attributes. |

## Five fresh actual mathlib methods and compiled generic-route trials

| Method | Actual query/artifact | Result |
|---|---|---|
| A Lean-Finder | one variable MvPolynomial index logarithm height/root-denominator multiplicity; `search-finder.json` | one_le_pow_mul_abs_eval_div and Chevalley degree-bound material; not this index estimate. |
| B Loogle | Polynomial.rootMultiplicity, Real.log; `search-loogle.json` | Successful empty response; not an exhaustive absence certificate. |
| C LeanSearch | root multiplicity rational root denominator power bounded by leading coefficient integer polynomial; `search-leansearch.json` | den_dvd_of_is_root, pow_rootMultiplicity_dvd, roots_pow and multiplicity factor lemmas; useful pieces but no full bound. |
| D source rg | untruncated index_unique_le_log_div/rootMultiplicity-log/uniqueAlgEquiv-map patterns; `search-source.log` | No exact pattern hits. Independently read uniqueAlgEquiv/coeff_uniqueAlgEquiv in Algebra/MvPolynomial/Equiv and eq_rootMultiplicity_map in Algebra/Polynomial/Roots. |
| E native name search | rootMultiplicity and Nat.cast_nonneg; `search-local.json`, `search-cast.json` | Actual declarations found; local index unavailable, honestly not indexed absence evidence. Nat.cast_nonneg additionally compiler-verified. |

Auxiliary variants: denominator-clearing/root-factor powers, multiplicity under injective maps,
unique polynomial coefficient equivalence, polynomial leading coefficient and log-power division.
No common-equivalents bucket applies. Existing project index_unique and pow_rootMultiplicity_le,
plus mathlib's field/map/log lemmas, capture the mathematics. The helper is a substantial bound,
not a one-to-three-mathlib-call wrapper. The short coefficient extensionality equality is ordinary
representation transport; it does not warrant another production helper/API in this scoped audit.

`automation.lean/.log` uses four separate anonymous examples against the exact INITIAL source
prefix ending BEFORE the audited helper. No matching target or failed named trial is imported.
grind fails, aesop fails exhaustively, exact? cannot close, apply? returns unrelated partial order
routes before the conservative20000-heartbeat bound. No complete replacement suggestion ignored.
Expected-failure exit1 is exploration only, never axiom evidence. Known repeated native full-Theta
multi_attempt stalls are not retried; bounded ordinary compiler exploration is the authorized
fallback. Five methods are presence searches; no blanket proof of mathlib absence is claimed.

## Effective-binder generalisation, inversion and private-literature exemption

`binders.lean` runs named trials isolated inside distinct namespaces, with autoImplicit=false;
`binders-isolated.log` is the definitive expected-failure batch. Each deletion/weakening is really
compiled. The first exploratory batch used trial names matching removed hypothesis identifiers;
name resolution could then point at a previous failed declaration. It was discarded and corrected
with `Drop_<binder>.trial` namespaces before accepting any result. No automation search uses it.
Negative results establish dependence of this statement/proof, not mathematical impossibility.
Positive selected proof/adapter checks run separately with exit0.

| Effective binder | Compiled drop/weakening | Finding and decision |
|---|---|---|
| {σ : Type*} | remove with autoImplicit=false | Unknown σ; retains arbitrary universe-polymorphic index type. |
| [Fintype σ] | standalone deletion; actual section omit | Standalone deletion uses Unique-derived canonical Fintype; section omit is rejected because existing index signature references ambient Fintype. Retain initial arbitrary enumeration presentation and exact public type. Canonical-instance restatement is not a simple drop of the initial object. |
| [Unique σ] | drop; Inhabited only; Subsingleton+Inhabited with local Unique reconstruction | Drop loses default/uniqueAlgEquiv; Inhabited loses uniqueAlgEquiv; reconstructed bundle compiles but is an equivalent unbundling, not weaker mathematics. Retain Unique. |
| {B : ℝ} | drop | Unknown B; Real.log fixes real codomain, abstract ordered-field replacement unavailable. |
| {q : σ→ℕ} | drop | Unknown q in hq/coprimality/point/log; retains arbitrary natural function. |
| {r : σ→ℕ} | drop | Unknown r in index/denominator; retain arbitrary natural function. |
| hq : 1<q default | drop; 1≤q default | Missing positivity/argument mismatch for log_pos and pow bound. Retain; q=1 gives log q=0 and cannot control arbitrary root multiplicity by this quotient. |
| hr : 0<r default | remove; weaken to0≤r default | Both compile with Nat.cast_nonneg; remove PRIVATE binder. No replacement assumption needed. Public hr intentionally retained. |
| {R : MvPolynomial σ ℤ} | drop | Unknown R; integer nonzero leading-coefficient arithmetic is essential to source bound. |
| hR : R≠0 | drop | Unknown hR for map nonvanishing and rational multiplicity-power bound; retain. |
| hRB : all coefficients bounded | drop; localize to equivalent univariate leading coefficient | Drop loses hRB; localized candidate compiles and initial uniform statement recovered by adapter. Apply localized private form. |
| {h : σ→ℤ} | drop | Unknown h in coprimality and point; retain arbitrary integer numerators. |
| hh : IsCoprime… | drop | Unknown hh at pow_rootMultiplicity_le; retain reduced rational-point input. |
| DecidableEq | already omitted in initial helper | Independent initial and selected declarations compile without any such binder; no new removal decision required. |

Literature: n/a, private declaration; inline literature search is explicitly exempt by cleanup
Step2.6d. Public caller's literature and contract audit belongs to original20 and is not replaced.
Math second-opinion MCP unavailable; no consultation claimed.

Inversion check: the individual index is rewritten once into rootMultiplicity/r. The remaining
argument is the already existing project pow_rootMultiplicity_le plus generic log monotonicity and
nonnegative division. No concrete distinguished polynomial/witness appears: R,q,r,h are arbitrary.
The abstraction from the public supremum already happened in original20. The actual extra
generality exposed here is precisely hRB localization and the zero-weight case, now implemented.

## Measured signature packing and inequality table

Widths are Unicode codepoints including indentation; `packing.txt` contains exact text/widths.
`#check @expectedNew` in definitive actual-helper log supplies format.width100 reference.
First next tokens are complete binders or mathematical expression units, not byte counts.

| Signature line | Initial width | Final width | Next unit and arithmetic | Action |
|---|---:|---:|---|---|
| private lemma through hq |91|91| `{R : MvPolynomial σ ℤ}`:22;91+1+22=114>100 |ok|
| R,hR,hRB (initial hr,R,hR,hRB) |95|95| `{h : σ → ℤ}`:11;95+1+11=107>100 |ok|
| h,hh,colon |62|62| full index LHS through≤:63;62+1+63=126>100 |ok|
| index LHS≤ |67|67| full RHS log/divisor:47;67+1+47=115>100 |ok|
| log/divisor, :=by |59|59| no next signature line |ok|

| Occurrence | Initial | Final/action |
|---|---|---|
| hq |1<q default|retain|
| hr |0<r default|private binder deleted; public stays|
| hRB |∀d,abs(coeff d)≤B|abs(leadingCoeff)≤B|
| conclusion |index…≤log B/(r log q)|retain exact conclusion|
| proof positivity |hlogq/hrpos and positive q-power|strict log positivity remains inline; weight replaced by Nat.cast_nonneg|
| reversed ≥/> in Lean signature/code |0|0; no rename|

## All 42 golfing rules

| Rule | Finding/action |
|---|---|
|1.1 by exact|No wrapper in helper; caller remains term proof.|
|1.2 by rfl|n/a: nontrivial inequality.|
|1.3 rw+exact|No adjacent pair to merge.|
|1.4 simp+exact|Caller conversion uses terminal simpa only directly.|
|1.5 trailing rfl|None.|
|1.6 constructor|n/a: no conjunction conclusion.|
|1.7 apply+exact|No unnecessary apply chain.|
|1.8 contradiction|None.|
|1.9 eta|No lambda eta-redex; point lambda performs division.|
|1.10 single-use have|Inline hlogq/hR10; delete hrpos/hcoef through private generalisation; hlog retained for rw+final use.|
|1.11 apply+intro|No such pair.|
|1.12 show|None.|
|1.13 projections|Caller hR.1/hR.2.2 used briefly once each; no repeated projection family.|
|1.14 merge rw|Conversion rewrites already single lists.|
|1.15 terminal simp only|Helper's squeezed hcoef deleted. Tested unsqueezed coefficient adapter maxRecDepth failure; focused simpa only retained, no limit raise.|
|1.16 nonterminal simp|None bare. dsimp only unfolds one local abbreviation.|
|1.17 dot|Standard .2 iff adapters and .injective retained.|
|1.18 trailing parens|No useful simplification; grouped positive-power proof and typed casts carry meaning.|
|1.19 push Not|None.|
|1.20 trivial exists|n/a: no existential helper.|
|2.1 grind|Actual clean anonymous whole-proof trial fails.|
|2.2 delete before grind|n/a: no selected grind.|
|2.3 simpa|Final divisor rearrangement already one terminal simpa; caller is focused conversion.|
|2.4 fun_prop|n/a: no function-property goal.|
|2.5 positivity|Retain positive natural q-power proof; replace weight strict positivity with direct Nat.cast_nonneg.|
|2.6 gcongr|No monotonic calc chain; direct div_le_div_of_nonneg_right provides exact endpoint.|
|2.7 lia/omega|n/a: no arithmetic case proof; Nat.zero_lt_of_lt is direct.|
|2.8 aesop|Actual clean anonymous whole-proof trial fails exhaustively.|
|2.9 norm_num/cast|exact_mod_cast needed only at genuine q/log domain bridge; no numeric computation.|
|2.10 decide|n/a: arbitrary polynomial/log statement, no closed finite computation.|
|2.11 field_simp/ring|Final algebraic rearrangement already simpa [div_div,mul_comm]; no remaining identity needing normalization.|
|2.12 linear_combination|n/a: no ring/ring_nf endpoint.|
|2.13 wlog|n/a: no symmetric cases.|
|2.14 calc collapse|No calc; inequalities composed directly.|
|2.15 repeated goals|No repeated independent goals.|
|3.1 erw|None.|
|3.2 continuity|None.|
|3.3 omega→lia|No omega retained/introduced.|
|3.4 rcases rfl|None.|
|3.5 attributes|Explicit nonvanishing/height/coprimality hypotheses unsuitable for global simp/grind rule.|
|3.6 simp_all|None.|
|3.7 limits|No production limits/scaffolding.|

## Step back, simplify and scope

The proof is the mathematical chain: identify the one-variable index; transport real root
multiplicity to rationals; apply the integer leading-coefficient power bound; take logarithms;
divide by log q and the nonnegative natural weight. Generic automation does not discover these
transport steps. The new assumptions state exactly what that chain uses, including r=0.
The public theorem is still the supremum corollary under its preserved original hypotheses.

Built-in /simplify and Skill invocation are unavailable in this host; performed scoped holistic
review directly. Outcome ISSUES-FOUND-AND-FIXED: private weight assumption deleted, coefficient
bound localized, aliases inlined. No additional extracted helpers, unused imports or wrapper
lemmas. Phase3 file-level fixes n/a to this single helper. Phase5a contains these private changes
only; Phase5b no renames needed, shared queue untouched. No Git/shared log mutations by worker.

## Definitive sequential gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file |pass| `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0,2423jobs; `module-final.log`. |
| Fresh complete live LSP |pass| Native lean_diagnostic_messages over entire live Theta, unfiltered; `final-lsp.json`, isError=false, success=true, partial=false, timed_out=false, failed_dependencies=[],0errors/17warnings. |
| Warning delta |intentional| Baseline16→final17: sole new warning is public hr at252, retained by this audit’s explicit public-API scope. No helper warning. Other warnings are outside this helper's scope. |
| Initial helper independent proof |pass| `initial-and-adapter.lean`→`initial-and-adapter-final.log`, exit0, independently compiles exact initial source proof before target introduction, plus selected stronger proof and full old-helper adapter. |
| Actual built helper exact selected type |pass| `actual-helper.lean`→`actual-helper-final.log`, exit0, discovers actual private suffix programmatically, checks exact selected type AST and all named metadata, universe names normalized/anonymous instance names exempt only. |
| Initial helper contract recovered from actual |pass| Same definitive actual-helper probe has complete initially typed hr/uniform-coefficient adapter and proof-irrelevance equality to the independently recompiled initial proof. Its source value is checked not to invoke the actual helper. |
| Actual helper standard axioms |pass| Actual private constant, independently recompiled initial proof, actual-helper initial adapter and expected selected theorem each use only propext,Classical.choice,Quot.sound. |
| Public20 complete immutable-original proof/contract |pass| `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-theta-log-helper/final20-original.lean`, exit0; `final20-original.log`. Reuses original20's complete independent original Index+Theta proof namespace and full-old DecEq adapter, rerun AFTER actual module build. |
| Public20 actual exact selected type/metadata/axioms |pass| Same final20 verifier checks actual selected type AST, all retained original parameter names/order/BinderInfo, old10-binder telescope minus ONLY DecidableEq, old-adapter defeq/equality, nonself original proof and standard axioms of actual public20/helper/original proof/adapter. |
| Immutable proof source |pass| `immutable-check.json`: independently checks old Θ_unique_le and pow_rootMultiplicity_le blocks byte-identical to immutable2b64544; new helper initial proof byte-identical to initial-helper snapshot. |
| Scope and public header protection |pass| `source-protection.json`: byte-identical source outside helper/public20 region, public20 header byte-identical to INITIAL selected header; public docstring/omit protected. `change.diff` is exact audit-owned diff. |
| Definitions/imports/attributes |pass| No changed definitions, imports, options, attributes or instances. |
| Structure/naming/packing/orientation |pass| Helper23/public3, no long branch/conjunction, mathematical name, full width/inequality tables above, no reversed code inequalities. |
| Caller coverage |pass| Repository Lean rg finds only the public20 call in Theta; that caller is covered by module and complete final LSP. |
| Scaffolding/trust |pass| No sorry/axiom/native_decide/limit raise/trace/haveI/letI/TODO/FIXME in scoped changes; definitive successful axiom probes contain no sorryAx. |
| Full project then separate LeanEval |pending OWNER| Intentionally not run by helper worker. These gates follow terminal audit handoff. |

Accepted definitive actual-helper probe is `actual-helper-final.log`, not `actual-helper.log`.
The first scratch verifier returned the full constant from a term elaborator where a proof of
the binder-instantiated goal was expected. Supplying its explicit hq/hR/hRB/hh arguments fixed
that SCRATCH expectedNew proof; production was untouched. Its failed run, which correctly rejected
scratch sorryAx, certifies nothing. Likewise, the first unsqueezed coefficient adapter hit default
maxRecDepth; focused simpa only fixed it. No recursion/heartbeat limit was raised.

New identifier verification: Nat.cast_nonneg found by native local search (`search-cast.json`)
and elaborated in the successful selected proof, module build and actual-helper probe. Every other
lemma identifier already occurs in the initial source or its public caller context. No unresolved
guessed identifier.

## Required 11-step phase checklist

- [✓] Step1: all required complete references and relevant style/naming/profiling read.
- [✓] Step2: full substantive24-item audit, with every have/simp occurrence.
- [✓] Step2.5: five actual fresh search methods and clean compiled exact?/apply? generic probes.
- [✓] Step2.6: every effective initial binder compiled drop/appropriate weakening, private literature exemption and inversion.
- [✓] Step2.7: every signature line measured in codepoints and fully packed.
- [✓] Step2.8: complete inequality occurrence table, zero reversed inequalities.
- [✓] Step3: all42 golfing rules considered individually.
- [✓] Step4: strategy reflection and scoped holistic simplify review.
- [✓] Step5a: fresh complete unfiltered final native LSP, no errors.
- [✓] Step5b: actual module build, initial/selected exact types and independent proofs, actual standard axioms, public20 immutable-original/retained-metadata gates, protection/content gates.
- [✓] Step6a: no rename required; queue/shared sidecars/Git untouched by worker.

## Freeze before final performance request

All normal compiler/native requests completed before the last profile began. Source edits revoked
at SHA256 `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`;
`source-protection.json` records this freeze. No source edits after it. Final performance results
and fully drained terminal handoff are recorded below.

## Buzz: accepted final real exact-prefix profile

Outcome FAST-BOARD; no over-budget deferrals, no raised limits. The last fresh uncontended
request measured BOTH declarations in the same exact shared final source prefix through public20:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-log-helper/final-prefix.lean`

Actual exit0; raw UTF8 `final-profile.log`, parser `parse_profile.py`, totals `timings.json`.
The prefix preserves every exact preceding import/source/context and adds only section/namespace
closing commands. This is explicitly prefix-only performance evidence, not a whole-Theta sweep.
Owner must eventually sweep the actual whole module after later slow-proof cleanup, as dispatched.

The parser sums the OUTERMOST omit command, associated async proof, async kernel-addDecl root and
async linter root, excluding nested duplicate command/tactic timings. No proposition compiler root
is emitted. The source anchors below are one-based raw-log lines. All normal compiler/native
requests were drained beforehand; owner held all compilers, and no other request overlapped.

| Declaration/run | Outer ms | Proof ms | Kernel async ms | Linter ms | Total ms | Raw anchors |
|---|---:|---:|---:|---:|---:|---|
| inherited initial helper |66.297|353.251|17.236|17.229|454.013| preceding original20 final-profile.log308686/308766/417074/417076 |
| inherited initial public20 |18.867|17.906|0.878|5.442|43.093| preceding original20 final-profile.log418624/418637/419430/419432 |
| fresh final helper |68.339|381.264|16.470|15.448|481.521| final-profile.log308839/308929/413157/413159 |
| fresh final public20 |17.023|48.673|1.360|6.068|73.124| final-profile.log414696/414711/415972/415980 |

Combined initial497.106ms→final554.645ms. This small increase includes the caller coefficient
conversion and ordinary timing variance; no performance improvement is claimed. Both declarations
and their combined measurement are below750ms, so no repeat threshold triggers. Each is below the
1000ms declaration budget. No temporary profiler commands/options in production.

## Terminal handoff

All worker compiler/native/profile requests completed and drained; no outstanding sessions.
Source edits remain revoked; final repeated SHA256 is
`b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`.
Helper declaration218–245, omit217, body23; public20 declaration251–255, body3. Total981→979lines.
Only helper, necessary public caller proof, this dedicated report and scratch evidence were written.
No new production helper, no Git/shared-log/shared-sidecar mutation, no count increment.
Owner may now perform frozen full `lake build`, then separate `lake build Roth.LeanEval`, final
cumulative checks and publication of original20. Those pending OWNER actions are not claimed done.


## Owner final frozen batch gates

After every leaf request drained and source authority was revoked, owner ran full `lake build`
then separate `lake build Roth.LeanEval`: exit0 in39.883s and15.025s. All17project/pin/source
hashes were identical before and after both commands; Theta SHA256 `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`.
Raw `/private/tmp/roth-theta-d20-full.log`, `roth-theta-d20-leaneval.log`, machine record
`/private/tmp/roth-theta-d20-builds.json`. These gates complete the leaf’s pending owner entries.
This helper is separately audited and retained; it is NOT an additional original. Original20
publication brings Theta20/35,overall201/264,9/14files only after successful push.
