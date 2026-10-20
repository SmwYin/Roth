# Roth.log_B₁_gt — original9 cleanup

Completed worker scope; owner review, whole-project build, separate LeanEval/root native gates,
publication, and the eventual whole-file ALL-row profile remain owner work. No Git or central
progress mutation was performed. No new production helper was introduced.

Entry HEAD: `b43bdb90fa5e7c162f03c534fd96ffddc0c26c4e` (ramin-cleanup).
Entry MainLemma SHA: `2b8a5cab541e92ba56eb71142867bb3f562461682ccada4c07e7ea4fcfcd87a4`.
Selected **v7** source SHA: `2bfa8a61e85ead5ff702d57ff6a28ddda85c39a0d1faf960d27cb3cdede319cd`.
Evidence: `/private/tmp/roth-mainlemma-log-b1/`; manifest `evidence-manifest9.json`.
Lean remains `leanprover/lean4:v4.34.0`; mathlib HEAD remains
`5ed2965256430c3649e86755f9576b54eca72435`. All 17 source/config pins are frozen in
`final-v7-build-freeze.json`; exact production binaries/setup/companions are frozen there too.

## Result

Removed all three sign premises (`hδ0`, `hq₁`, `hr₁`) and weakened `4 < q₁^(δ*r₁)` to
`2 ≤ q₁^(δ*r₁)`, retaining the **identical strict logarithmic conclusion** and data arguments.
The sole direct call in `three_small_factors` now supplies its derived power bound. Its full
written contract and the contracts of `main_lemma` and Main's `roth_of_isIntegral` remain exact.
Main.lean is byte-identical to entry. No next-original audit credit is claimed.

Before: 9 declaration lines / 6 proof lines. After: 6 declaration lines /
4 proof lines. Saved: 3 declaration lines. Full file: 696 →
696 lines (application documentation accounts for the offset).
Comments: zero original inline proof comments; the exact historical source quotation is preserved.

```lean
theorem log_B₁_gt {δ : ℝ} {q₁ r₁ : ℕ} (hX : 2 ≤ (q₁ : ℝ) ^ (δ * r₁)) :
    δ * r₁ * Real.log q₁ / 2 < Real.log (B₁ δ q₁ r₁) := by
  simpa [B₁, Real.log_sqrt (by positivity), Real.log_rpow
    (((Real.one_lt_rpow_iff (Nat.cast_nonneg q₁)).1
      (lt_of_lt_of_le (by norm_num) hX)).elim (fun h ↦ zero_lt_one.trans h.1) And.left)] using
    Real.log_lt_log (Real.sqrt_pos.2 (lt_of_lt_of_le (by norm_num) hX)) (sqrt_lt_floor hX).1
```

## Reading and initial audit

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. The full 854-line worker prompt was
recovered in explicit ranges 1–300,301–600,601–854. Both installed SKILL.md files, complete
cleanup/cleanup-all/buzz commands, full required references (including style/naming/profiling/
review stages/principles), all future-profiler corrections and dispatch context were read.
Initial large combined skill output was truncated; every line was subsequently recovered in
bounded reads. `work-state.json` records the complete range inventory.

The full initial 24-item audit was recorded **before production edits** in `initial-audit.md`.
The resolutions below supersede its prospective choices (including the earlier v6 zero-base
case proof). Source §6 was checked directly at clean.tex1350–1388.

## Final full audit — all 24 items

1. **LINT:** target has no warnings. Final fresh complete native ML diagnostics have only the
   preserved header warning and foreign `three_small_factors.hδm` / newly unused `.hq₁` warnings.
   The latter are explicitly carried to original10 without suppression or fake uses.
2. **HAVE SCAN:** original `hq` (L139, by, used once) and `hX0` (L140, by, once) are eliminated;
   `h` (L141, no by, once), `hs` (L142, no by, once), anonymous log bound (L143, no by, once)
   are inlined. Final v7 has **zero have/let declarations**. Base positivity is obtained directly
   by eliminating `Real.one_lt_rpow_iff`, using `zero_lt_one.trans h.1` / `And.left`.
3. **SET_OPTION:** none on target or added to production. No limits raised.
4. **SIMP SQUEEZE:** one final terminal `simpa [B₁, ...]`; it is unsqueezed. No nonterminal simp.
5. **NAMING:** queued `Roth.log_B₁_gt → Roth.mul_log_div_two_lt_log_mainCoeffBound` (public).
   This names the smaller left side and aligns with the already queued B₁→mainCoeffBound rename.
   No in-place rename. Both existing queue entries are byte-preserved.
6. **LINE PACKING:** measured full initial/final signature tables below; no remaining repack.
7. **BY PLACEMENT:** `by` is at the signature line end.
8. **FORMAT:** four proof lines, two-space tactic indentation, packed continuation, no empty
   proof lines, semicolon chains, haveI/letI, trailing spaces, or legacy lambdas.
9. **COMMENTS:** zero inline proof comments existed; exact source quotation retained once.
10. **DOCSTRING:** corrected the hypothesis description and added the application tip that the
    power bound supplies positivity when converting coefficient bounds into exponential bounds;
    the historical quotation still states the original paper's >4 context verbatim.
11. **VISIBILITY:** retained established public coefficient-bound API and original public
    contract recovery; no new private/public wrapper or helper was added.
12. **STRUCTURE:** four-line body, one tactic with a composed term; no conjunction conclusion,
    proof branch >10 lines, or headline-theorem issue. No decomposition flag needed.
13. **MATHLIB:** actual five-method search below; selected proof uses the existing power iff
    and logarithm APIs together with the already audited floor bound. No duplicate API added.
14. **JUNK DEF:** n/a — theorem, not a definition.
15. **EXISTS LEMMA:** n/a — no existential helper.
16. **SHOW vs CHANGE:** none in the selected target; no redundant show introduced.
17. **PUSH_NEG:** none.
18. **GENERALISE:** complete effective-binder audit, mechanical drop/threshold tests, literature
    search, independent original recovery and sharp counterexamples below.
19. **INEQUALITY:** zero reversed Lean operators; exact scan below and smaller-left name queued.
20. **NORMAL-FORM:** strict smaller-left order and original product/log/division conclusion
    retained; no alternative normal form, simp attribute or equivalence network introduced.
21. **SYNTAX-GEN:** a single power bound replaces three redundant sign arguments; old callers
    retain their full written contracts. No public data-domain restatement is recommended.
22. **IMPORT-FANOUT:** n/a — no production import change.
23. **CASTS:** zero redundant casts retained. The explicit natural→real base ascription is
    required: actual removal failed HPow ℕ ℝ and the closed-TYPE guard rejected it. Natural q₁,
    r₁ and B₁ coercions are genuine cross-type bridges. No new load-bearing cast introduced.
24. **INSTANCE-NAME:** n/a — no instance declaration or named local instance.

## Mathlib search status — five actual methods

[A] **Lean-Finder:** query “logarithm of the natural floor of a real number is greater than half
its logarithm if x is at least 2”, top3 Real.log2_le_logb / Nat.log_le_clog / Behrend.le_sqrt_log.
The available remote index defaults to v4.28; it is not asserted to be the pinned v4.34 index.
These are not replacements for the target. Actual tool response is in the conversation.
[B] **Loogle:** `Real.log, Nat.floor, _ < _`; Chebyshev.pi_le_log4_mul_div,
Chebyshev.eventually_primeCounting_le, Chebyshev.pi_ge' are unrelated partial keyword matches.
Raw response: `search-loogle.json`.
[C] **LeanSearch:** “For x at least 2, half the natural logarithm of x is less than the natural
logarithm of its floor”; returned Nat.log_lt_self, Real.natLog_le_logb and harmonic-floor bounds,
not the estimate sought. Raw response: `search-leansearch.json`.
[D] **Pinned source grep:** full untruncated `sqrt.*floor|floor.*sqrt|log.*floor|floor.*log`
(33 rows), full proposed-name grep (zero hits), and 104 auxiliary-variant rows are saved.
Real.log_sqrt, Real.log_rpow, Real.log_lt_log and Real.one_lt_rpow_iff are the useful APIs.
[E] **Name pattern / lean_local_search:** `log_sqrt`, `log_lt_log` returned the expected source
hits; index states warming/error are disclosed, not absence evidence. Pinned source search and
actual compiled name/type use provide the fallback. Raw responses are saved.

Auxiliary variants checked: log_lt_log_iff, one_lt_rpow_iff / _iff_of_pos, log_rpow,
zero_rpow_le_one, floor_eq_iff, lt_floor_add_one, floor_real_sqrt_eq_nat_sqrt,
nat_floor_real_sqrt_eq_nat_sqrt. Common-equivalents catalogue: no disguised topology/finiteness/
bornology/custom-class hypothesis applies. All selected names are compiler-verified in the
pinned environment; the actual v7 metadata uses standard axioms only.

**Concluded:** partial matches supply the building blocks; keep this project-specific B₁
estimate and build directly on those APIs. The final proof uses four distinct mathlib analytic
APIs plus the established floor estimate, not a new 1–3-call convenience wrapper. No new API
extraction signal remains. This is not an unsupported formal claim of global library absence.
Whole-proof exact?/apply? controls were attempted; partial/search admissions are rejected.

## Generalisation status — all OUTER and INNER effective binders

| # | Original binder | Class / use | Catalogue/drop/weakening candidates | Verified result |
|---|---|---|---|---|
|1|`{δ : ℝ}`|data; exponent/product and B₁|drop; real→abstract field; product-exponent restatement|retain value/domain: occurs in fixed B₁ signature and exact conclusion; abstract log/rpow/domain change would restate B₁, not mechanical deletion|
|2|`hδ0 : 0 < δ`|proposition; unused original proof|drop first; `0 ≤ δ` dominated by successful drop|native clear test, selected joint-drop full live diagnostics, exact new full-type/value checks pass; removed|
|3|`{q₁ : ℕ}`|data; B₁ base and logarithm|drop; abstract/real base; explicit cast drop|retain fixed B₁ data domain; actual base-ascription drop fails HPow ℕ ℝ and closed TYPE; no data-definition change recommended|
|4|`{r₁ : ℕ}`|data; exponent and B₁|drop; real exponent/domain|retain fixed B₁ natural degree domain; replacing it changes the named construction/conclusion rather than dropping a hypothesis|
|5|`hq₁ : 1 < q₁`|proposition; supplied positivity in old proof|drop first; `1 ≤ q₁`, `0 < q₁` dominated|removed in verified stronger joint-drop API; derived from hX in guarded boundary theorem|
|6|`hr₁ : 0 < r₁`|proposition; unused original proof|drop first; `0 ≤ r₁` dominated|native clear and verified selected joint-drop API pass; removed|
|7|`hX : 4 < q₁^(δ*r₁)`|proposition; floor/log positivity|drop; 4≤; 2<; **2≤**; 1<; 1≤;0≤; any lower uniform threshold|keep2≤; endpoint included; every c<2 has an actual positive-δ/q=2/r=1 counterexample; dropping also fails|

Joint removal is a **stronger** compiled check than retaining unused copies of the other sign
premises: the final exact expected type contains only δ,q₁,r₁,hX. Earlier native clear tests
individually checked hδ0/hr₁. Successful complete live diagnostics and the full opaque-value/type
check validate the joint substitution. Successful weakest drop dominates merely weakening its
strict premise; no stronger premise is kept for convenience.

**2.6b:** complete nonpartial live diagnostics and kernel checks accepted the substitutions.
All selected data binders, their names/order/BinderInfo, universes and exact conclusion are
checked independently. Failed numeric/cast candidates are retained, not accepted on a prefix PASS.
**Inner binders:** none in the original or final statement/hypotheses. There are no section
instances, explicit typeclass/decidability parameters, universe binders, global function
hypotheses, or point/global continuity/monotonicity assumptions to weaken/localise. Both public
types have empty universe parameter lists. The proof's local Or-elimination lambda is not a new
API hypothesis.
**2.6c:** no remaining recommended big-change candidate. A generic X/log/floor reformulation is
already the logarithmic use of the existing sqrt_lt_floor API; extracting another thin wrapper
would add no needed API. Concrete-via-abstract inversion therefore selects existing APIs, not a
new helper or restated B₁ definition.
**2.6d:** actual public literature searches with top3 per query below; optional ChatGPT math MCP
is unavailable in ALL_TOOLS and is skipped honestly. No literature-based abstract-domain change
is recommended. The sharp threshold is established by compiled Lean witnesses, not inferred from
an unrelated search hit.
**2.6e:** all verified improvements are applied under the standing user authorization to
implement recommendations. No undecidable choice or approval is pending.

### Actual edge/counterexample gates

`boundary9-v7-final` exits0 with closed full TYPE, actual opaque VALUE, inferred type and
standard-axiom checks for every named test:

- `below_two_fails`: δ=1/2,q=2,r=1 gives X=√2∈(1,2), B₁=1, so the strict log conclusion fails
  despite all three old sign premises.
- `endpoint_included`: δ=1,q=2,r=1 gives X=2 and the strict conclusion holds.
- `every_lower_threshold_fails`: for **every c<2**, choose X=(max(1,c)+2)/2∈(1,2), then
  δ=log X/log2>0, q=2,r=1; X≥c but B₁=1 and the conclusion is false.
- `old_sign_premises_follow`: hX implies 0<δ,1<q₁,0<r₁ (their removal is mathematical, not just
  an unused-argument linter deletion).
- `no_bound_fails`, `zero_degree_fails`, `zero_base_fails`, `unit_base_fails`: actual degenerate
  counterexamples, so the power condition cannot simply disappear.

## Literature search status — public declaration

[A] WebSearch ran three actual queries. Raw results: literature-query1/2/3.json and
literature-top3.json. The first query includes the explicit “generalization” search; the third
requests nLab/Stacks. Top3 results are listed in the appended table. DLMF gives standard log
inequalities; nLab gives the floor's canonical order formulation. Neither is claimed to state
this exact B₁ bound or the sharp2 threshold. Source clean.tex provides the original X>4 estimate;
the verified strengthening is our compiled mathematical finding.
[B] ChatGPT math MCP: n/a — unavailable, optional skip authorized. Literature-driven remaining
big-change candidates: none.

Query: `floor logarithm square root floor x inequality generalization x 2`

- [discrete mathematics - Solve $\lfloor \sqrt x \rfloor = \lfloor x/2 \rfloor$ for real $x$ - Mathematics Stack Exchange](https://math.stackexchange.com/questions/1038396/solve-lfloor-sqrt-x-rfloor-lfloor-x-2-rfloor-for-real-x)
- [Floor function and inequality - Mathematics Stack Exchange](https://math.stackexchange.com/questions/2088203/floor-function-and-inequality)
- [Useful Inequalities {x² ≥ 0} v0.27b · August 19, 2015](https://www.cs.mcgill.ca/~amehra13/handbook/handbook.pdf)

Query: `floor function inequalities logarithm integer part real powers`

- [DLMF: §4.5 Inequalities ‣ Logarithm, Exponential, Powers ‣ Chapter 4 Elementary Functions](https://dlmf.nist.gov/4.5)
- [Floor and ceiling functions](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)
- [Floor function of a real number - Mathematics Stack Exchange](https://math.stackexchange.com/questions/2830537/floor-function-of-a-real-number)

Query: `floor function logarithm inequality generalization nLab Stacks`

- [floor in nLab](https://ncatlab.org/nlab/show/floor)
- [DLMF: §4.5 Inequalities ‣ Logarithm, Exponential, Powers ‣ Chapter 4 Elementary Functions](https://dlmf.nist.gov/4.5)
- [elementary number theory - Inequality involving floor of logartithm - Mathematics Stack Exchange](https://math.stackexchange.com/questions/4955154/inequality-involving-floor-of-logartithm)

## Line-packing required artifacts

Initial #check width100 reference is superseded by the selected type printed by the final
independent metadata run (`set_option format.width 100 in #check @Roth.log_B₁_gt`).
The full raw output is preserved in independent9-v7-final.log.

| Initial signature line | Characters | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
|136|81|hX binder,30|81+1+30=112>100|ok|
|137|36|conclusion and :=by,54|36+1+54=91≤100|repack|
|138|58|none|n/a|ok|

| Final signature line | Characters | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
|139|70|conclusion and :=by,54|70+1+54=125>100|ok|
|140|58|none|n/a|ok|

All codepoints were measured, not UTF8 bytes; conclusion participates in packing. No wide-hyp
escape needed. Initial hX binder length includes its complete parentheses, not a first word.

## Inequality scan required artifact

|#|Location|Original|Rewrite|Rename|
|---|---|---|---|---|
|1|whole original/final signatures and hypotheses|n/a — zero ≥/> Lean operators|none needed|log_B₁_gt→mul_log_div_two_lt_log_mainCoeffBound queued|

All target proof-local inequalities also use smaller-left orientation. Reversed math prose in
the unchanged source quotation is deliberately preserved.

## Golfing rule pass — all 42

|Rule|Status / evidence|
|---|---|
|1.1 by exact wrapper|n/a — selected proof is one terminal simpa tactic, no wrapper|
|1.2 by rfl|n/a — none|
|1.3 rw+exact→rwa|original already used rwa; final entire chain replaced by terminal simpa|
|1.4 simp+exact→simpa|n/a adjacency; equivalent consolidation implemented under2.3|
|1.5 trailing rfl after simp|n/a — no rfl|
|1.6 constructor chain|n/a — no conjunction conclusion|
|1.7 apply+exact|final mathematical applications composed as direct terms|
|1.8 by_contra+push_neg|n/a — neither remains|
|1.9 eta-reduce lambdas|final lambda uses h.1, not eta-reducible; right branch already And.left|
|1.10 inline single-use have|all five original haves eliminated; no final have/let; base positivity directly composed from power iff|
|1.11 apply+intro→refine+fun|n/a — none|
|1.12 redundant show|n/a — none|
|1.13 have+.1/.2→obtain|n/a — only floor .1 used once and directly; destructuring would introduce unused .2|
|1.14 merge rw|n/a — no final rw chain|
|1.15 terminal simp only unsqueeze|applied; guarded v6/v7 use unsqueezed terminal simpa|
|1.16 squeeze nonterminal simp|n/a — no nonterminal simp|
|1.17 dot notation|power-iff .1 and .elim, zero_lt_one.trans, sqrt_pos.2 and floor .1|
|1.18 <| over redundant parens|remaining parentheses group projections/elimination and a simp lemma argument; removing them changes parsing|
|1.19 push_neg→push Not|n/a — none|
|1.20 trivial existential helper|n/a — none|
|2.1 whole grind|actual native original and entire-proof compiler controls fail; no zero-goal search acceptance|
|2.2 delete tactics before grind|n/a — no retained grind|
|2.3 simpa consolidation|applied; entire proof now one simpa using log_lt_log, with sqrt/log/rpow rewriting|
|2.4 fun_prop|n/a — no function-property goal|
|2.5 positivity|accepted for nonnegativity needed by log_sqrt; no sign premise retained|
|2.6 gcongr|entire-proof control did not make progress; use exact analytic APIs|
|2.7 lia/omega|selected proof has no Nat/Int linear-arithmetic goal; original omega positivity step eliminated by the power iff|
|2.8 aesop|actual native and whole-proof controls fail|
|2.9 norm_num/norm_cast|norm_num discharges only fixed numeric threshold checks; base-cast removal actually fails and is rejected|
|2.10 decide/+kernel|n/a — noncomputable variable real inequality, not finite decidable computation|
|2.11 field_simp;ring|n/a — target is analytic strict inequality, no algebraic-identity subgoal|
|2.12 linear_combination|n/a — no terminal ring/ring_nf or polynomial equality in target|
|2.13 wlog symmetric branches|n/a — no symmetric cases; final Or elimination is a short existing API term|
|2.14 collapse calc|n/a — no calc|
|2.15 <;> close similar goals|n/a — no repeated generated goals in final proof|
|3.1 erw→rw|n/a — neither|
|3.2 continuity/measurability→fun_prop|n/a — neither|
|3.3 omega→lia|original omega completely removed; no new omega/lia needed|
|3.4 rcases rfl auto-substitute|n/a — final proof has no cases/rfl; historical v6 discarded for shorter v7|
|3.5 automation attributes|none appropriate for this strict project-specific inequality; no new simp normal form|
|3.6 simp_all over simp_all only|n/a — none|
|3.7 remove maxHeartbeats|n/a — no override existed; none added|

### Step back and think

Whole-proof grind/simp/aesop/exact?/apply?/gcongr were actually attempted with failures preserved.
Pinned apply? can admit partial goals; all such apparent successes are rejected by actual opaque
VALUE/standard-axiom checks. The selected v7 is itself **one tactic**: terminal simpa around a
composed analytic term. The final step-back found Real.one_lt_rpow_iff and replaced the seven-line
case proof with four lines. There is no single-use have left to inline and no new helper is needed.
No prettier unsupported statement or weaker conclusion was substituted.

## Independent mathematical and contract gates

Actual FINAL build precedes the v7 imported metadata/native/profile gates:
`/Users/ramin/.elan/bin/lake build Roth.MainLemma Roth.Main` → exit0 (77.005s), in
`affected-build9-v7-final.json`. No source changed after that build.

`independent9-v7-final` runs actual pinned `lake env lean -j1 independent9-v2.lean` → exit0.
The immutable source snapshot is project-original.lean at d2eb5e9a…, SHA
`a3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8`.
The scaffold independently reimplements its **entire original target proof** with the original
old full paired sqrt_lt_floor proof/contract and own B₁ definition. It does not substitute the
entry9 prior-caller-repaired proof. Separately, full entry9 ML/Main copies recover the actual old
consumer proofs with explicit namespace/data migrations only.

Raw old/current complete type ASTs are preserved and compared: all written names/order,
BinderInfo (including inner binders), universe lists, and conclusion. Only generated macro names
on BOTH sides may eraseMacroScopes; written names are never normalized. Both TYPE and actual
opaque VALUE (`value! true`) are closed (no mvar/fvar/loose bvar/sorryAx), inferred full type
checked, axioms restricted to propext/Classical.choice/Quot.sound.

Accepted pairs: expected-new / actual v7 target; immutable project-original / old-type adapter;
independent entry9 target / adapter; old/current three_small_factors; old/current main_lemma;
old/current roth_of_isIntegral. The old-proof closures ban actual current target, every checked
actual current consumer, actual public sqrt_lt_floor and the uniquely resolved actual private
`_private.Roth.MainLemma.0.Roth.sqrt_lt_nat_floor_aux`. Five independent old closures pass.
This does not claim the owner's pending cumulative whole-project-original scaffold passed.

Fresh full UNFILTERED native ML/Main diagnostics (`native-v7-final-*.json`): success true,
partial false, timed_out false, isError false, failed_dependencies[], zero errors. ML warnings:
header + original10 hδm/hq₁; Main warnings: header + pre-existing hδ/hQ/hc. Nothing suppressed.

## Profiling — selected v7 only

Exact actual CLI on each immutable scaffold:
`lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
Scope is the complete actual target and sole direct consumer, preserving every declaration,
type/body/binder/order; the same scope-template reproduces the BEFORE and historical v6
scaffolds byte-for-byte. Different physical immutable paths are explicitly recorded in
scope9-v7-final.json. No global/scoped numerical comparison is made.

All ≥750ms direct-consumer BEFORE repeats finished **before API edits**. Imported binaries and
all setup/options/companion cache files were saved then (104 artifacts), so replay uses the real
old API. The deterministic before check's actual --deps resolves the copied original
Roth/MainLemma.olean. Its old call syntax also compiles against that old binary. No reconstruction
or source/cache rollback was needed.

Only column-zero disjoint Elab.command/Elab.async roots from the unique exact declaration-token
span are summed. Actual matching proof, kernel/compiler and lint roots are required. Nested Meta,
children, adjacent commands and end-command tails are not double-counted. Every accepted row
passes anchored_profile_span.py + verify_profile_roots.py and an exited/UTF8/17-pin-immutable
runner with owned process-group drain. Helpers introduced:0, so no hidden helper cost.

|Declaration|Before first/repeat (ms)|Final v7 first/repeat (ms)|Result|
|---|---:|---:|---|
|log_B₁_gt|103.207 / 113.451|83.057 / 81.675|target <1000ms|
|three_small_factors|1780.845 / 1832.483|1810.373 / 1847.068|foreign pre-existing >1s queue retained|

**Owner erratum (2026-10-20): optional heartbeat corroboration withdrawn.**
The historical target836→872 and consumer24607→24930 figures were measured using
Mathlib's builtin `#count_heartbeats in`. Pinned `Mathlib/Util/CountHeartbeats.lean:143`
elaborates its command under `set_option maxHeartbeats 0`; therefore the report's earlier
claim that this was a bounded cross-check without a limit raise was incorrect. These figures
are **not accepted corroboration** and are not needed for the required performance gate.
Associated historical v6 heartbeat figures are likewise excluded.

The accepted wall-clock table above uses the actual recorded bounded profiling CLI, with
no heartbeat-limit option changes. Its immutable complete roots, actual exits, source/type/
opaque-value/standard-axiom checks, native diagnostics and production builds remain valid.
No production source or profiling result was changed for this correction. The original
published report (SHA256`b6aeca806e84a6371dc05bd596520cda94417ce8e1133df2ca7d2f4037285ec7`)
is preserved at `/private/tmp/roth-mainlemma-owner/original9-published-report-before-heartbeat-erratum.md`
and in source/audit commit`d274aa6f0e361169811481b6a442f230fe719170`. The frozen leaf manifest's
report hash identifies that historical report; its other artifact hashes are unchanged.
Future heartbeat corroboration must use a verified bounded custom command that preserves
all limits. Historical optional heartbeat probes will not be rerun.

Selected v7 bounded diagnosis: the changed hlogB application costs4.762/6.190ms; the
unchanged final arithmetic refine costs1193.467/1216.540ms. Before application0.576/0.594ms
and final refine1187.376/1192.537ms. consumer-diagnosis9-v7.json preserves complete diagnostic
rows; these nested steps are not added to the root totals. The small direct-call cost increase
and heartbeat increase are explicit; no zero-regression claim is made.

Historical **v6**, not final-v7 certification: target95.410/107.128ms; foreign consumer
2230.199/1811.108ms. The slower2230.199ms sample is retained. Bounded diagnosis locates the changed
application at5.183/4.754ms vs0.576/0.594ms before; the large transient increase lies in unchanged
later arithmetic (final refine1478.839 then1199.464ms vs1187.376/1192.537ms). These are nested
DIAGNOSTIC timings, not added to root totals. consumer-diagnosis9.json preserves all rows. No
causal claim of zero regression or foreign hard-budget pass is made; original10 remains mandatory.
The v7 source change justified fresh v7 captures, not an unchanged third run chosen for speed.

Buzz outcome: target FAST-BOARD; no target performance deferral, no limit raises. Foreign
three_small_factors remains its own audit/performance item. Existing owner whole-file queues
(exists_delta_bound11188.775, pigeonhole1000.235, main_lemma4880.648 and prior slower samples) and
Main-own-file queue remain explicit. This worker does not certify whole-file performance.

## Failed and historical evidence — never laundered into a pass

- Candidate-v1 failed expected-term simplification (B₁ required explicit unfolding) and the
  scratch guard referenced the wrong instantiateMVars namespace; fixed in v2, not accepted v1.
- Native whole-proof grind/simp/aesop/exact? fail; apply? returns zero goals with partial
  suggestions and an error, never proof acceptance. Complete whole-proof compiler controls have
  no retained suffix; their sorryAx guards reject every failed/search-created value. Mixed-file
  exact?/apply? hits are not claimed as mathlib absence evidence or positive proofs.
- Direct zero-base branch v3 could not infer1<?m; v4 exposed the natural→real zero cast mismatch.
  V6 kept the cast normalization and passed; v7 superseded the whole branch via a mathlib iff.
- Actual explicit base-ascription removal fails HPow ℕ ℝ and closed TYPE. A prefix body marker
  cannot accept this run.
- Boundary-v1 failed floor cast/factor-orientation/direct-branch elaboration; repaired boundary-v5
  and final-v7 runs pass. Intermediate unexecuted repair drafts are not claimed as measurements.
- Independent-v1 passed some individual checks but overall exited1 for unknown pp.width; repaired
  format.width and final v7 complete exit0 are the accepted certificate.
- Initial premature profile parse ran before the first compile completed and found no command;
  it has no timing credit. The finished immutable capture was then parsed successfully.
- First broad skill/tool-description outputs were truncated; required complete reads/used tool
  descriptions were recovered before edits. A literature-summary parser error was repaired; raw
  search results are preserved. Initial sandbox ps denial was followed by authorized read-only
  inventory, not an inferred drain.
- V2/v6 builds, metadata checks, successful profiles and heartbeat checks remain historical;
  selected v7 has its own final build/imported proof/native/profile/heartbeat source hashes.

## Gates

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|actual affected-build9-v7-final invocation above exits0 for ML and Main|
|definition_protected|pass|exact source reconstruction; all definitions/imports/options/values unchanged|
|theorem_statement_protected|pass, authorized item18 change|strict conclusion/data preserved; three redundant sign premises removed and threshold weakened with sharp proofs; exact old full-type adapter|
|structure_gate|pass|four proof lines; no conjunction conclusion or long branch; zero new helpers|
|naming_gate|pass with queued action|one new JSONL rename, existing queue bytes preserved; no in-place rename|
|line_packing_gate|pass|all final signature lines measured70/58, no repack|
|inequality_orientation_gate|pass|no ≥/> Lean occurrences; required table and name queue present|
|cumulative_no_unintended_breakage|pass in affected scope|full actual ML/Main build + complete native checks + independent old/current full consumer contracts/values/axioms|
|production no-limit-raise / no-scaffolding|pass; optional HB excluded|no production options/imports/wrappers added; builtin scratch HB internally disables its limit and is withdrawn above|
|target performance|pass|both selected v7 complete root captures under1000ms; foreign slow queue disclosed|

Source reconstruction and queue-prefix proof: source-protection9-v7.json. All source outside the
exact target/doc and necessary single caller application is byte-protected. Source quotation
preserved once; Main.lean is entry-identical. No foreign signature edited or next original audited.

Refactoring needed: queued public rename above for Phase5b; original10 must audit newly unused
hq₁ as well as pending hδm and its pre-existing performance. No undecidable target action remains.
Owner final file/import/simplify/ALL-row/global performance and publication gates remain pending.

## Required phase checklist — all eleven

- [✓] Step1: complete prompt/reference reading and truncation recovery.
- [✓] Step2: initial/full final24-item audit.
- [✓] Step2.5: five actual mathlib search methods, failures/index limits disclosed.
- [✓] Step2.6: all effective binders, drops/weakenings, literature/top3, sharp boundaries.
- [✓] Step2.7: complete codepoint line-packing tables and final arithmetic.
- [✓] Step2.8: complete inequality scan and smaller-left rename queue.
- [✓] Step3: every one of42 golf rules has a concrete status.
- [✓] Step4: step-back selected existing power iff and one-tactic proof.
- [✓] Step5a: fresh full unfiltered final-v7 native ML/Main diagnostics, zero errors.
- [✓] Step5b: actual affected builds, exact type/value/source guards and final profiles pass.
- [✓] Step6a: JSONL rename appended; original Index/B₁ bytes preserved.

Overall: worker-owned target gates pass. Evidence manifest hashes every artifact and records
strict UTF8 or explicit binary-cache exceptions; final drain receipt records all owned PGIDs and
native_pending[]. All source/compiler/native/profile/report leases are explicitly released only
in the final handoff after evidence is frozen. No original-count inflation or publication claim.
