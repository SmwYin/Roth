# Dedicated boundary revisit — `Roth.index_le_lem6` (original 29)

This is a fresh revisit of original29, not another original audit. Counts remain 210/264,
Theta29. Sole worker/compiler/native-LSP window; no Git operations or shared report edits.
User-selected GPT-6.1 Sol, medium. Scope: public29 plus minimal proof forwarding in public30.

## Baseline and authorization

Inherited exact source SHA256 `47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`.
Owner dispatch identifies clean published HEAD `5880d589ca2dd465598907a7d9b489ec95e43ad5`.
Baseline module build exit0, 41.228s; actual compatibility exit0, 57.774s, recorded in
`/private/tmp/roth-mapped-helper/final-gate-status.json`. Complete unfiltered native LSP
`/private/tmp/roth-mapped-helper/final-lsp.json`: success, partial=false, timed_out=false,
0 errors/10 warnings. These are explicitly inherited, not fresh checks.

Inherited accepted real same-SHA exact-entire-prefix timings, first/repeat, milliseconds:
public29 895.050/854.163; numeric 939.576/873.525; weight 408.013/361.605;
mapped 707.126/651.477. No new baseline trace duplicates that measurement.
Optional cache/linter executable: not needed; native diagnostics include actual linters.
Owner retains full-project build followed by separate `Roth.LeanEval` gate after handoff.

Standing user authority: “From now on implement all changes that you recommend. Only ask me
if you can't decide.” Concrete K was dispatched as recommended: weak delta boundaries and
`3 ≤ (r none : ℝ)`. Further hr0/hB drops were only preliminary notes; this revisit first
compiled the exact candidate with entire independent original29 and original30 proofs,
complete adapters and new caller proof/value/dependency/standard-axiom checks, then applied.
`hq` is explicitly protected and RETAINED. Earlier protected hypotheses in Θ_nonneg,
Θ_le_card and Θ_mono are untouched. Public30 keeps its entire public telescope here.

## Mathematical change

The conclusion, shared witness `l`, both bounds on `l`, and the complete index inequality
remain unchanged. Replace `0 < δ`, `δ < 1`, `10 / δ < r none` by `0 ≤ δ`, `δ ≤ 1`,
`3 ≤ (r none : ℝ)`. Existing weak ratio hypothesis remains.

Remove `hr0`: the distinguished weight is positive because it is at least3; each other
weight is positive because its product with nonnegative δ is at least that positive
weight. Remove `hB`: some integer coefficient of nonzero R is nonzero, hence has absolute
value at least1, and hR bounds that coefficient by B. Both derivations are local typed
proofs; no new helper. They also explain why these drops preserve the theorem's content.

The minimal public30 proof passes hδ0.le/hδ1.le and derives `3 ≤ r none` via
`3 ≤ 10 ≤ 10/δ ≤ r none`; it omits the now-derived hr0/hB arguments. Its own hypotheses,
including implicit section instances, hq and hB, are preserved. The published public30
API audit is a later task, not claimed by this revisit.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Baseline29 hq unused is protected. Complete fresh diagnostics required below. New public30 hr0 warning is expected from preserving its old telescope after localizing public29; no artificial proof use added. |
| 2 | HAVE SCAN | hr0: local proof with cases, used4 times; hB: local proof, used once but substantive proof; hM1: term, used twice; hlower: term, rewritten then used; hupper: term, rewritten then used. Keep all; no single-use term-have to inline. |
| 3 | SET_OPTION | No production local/global limit or debug option introduced; default heartbeat budget. |
| 4 | SIMP SQUEEZE | Two nonterminal simps on hupper/hlower remain explicit `simp only`; final simpa is terminal. Prior rejected mapped simp variant remains rejected and unchanged. |
| 5 | NAMING | index_le_lem6 is snake_case, describes index comparison and source Lemma6; matches none of the forbidden numeric patterns (`mN_`, triple-number, numeric_aux) or banned abbreviations. No rename recommended/queued. |
| 6 | LINE PACKING | All8 signature lines measured below; every next binder/expression would exceed100. |
| 7 | BY PLACEMENT | Main and local proof `by` follow their preceding lines. |
| 8 | FORMAT | Two-space tactics, no blank proof lines, no haveI/letI, no semicolon chain; owned theorem lambda uses ↦. |
| 9 | COMMENTS | Both prior signposts retained byte-identically: M/Φ nonnegativity and two determinant index bounds. |
| 10 | DOCSTRING | Existing source-cited documentation preserved, including original quotation; no authorized docstring rewrite needed. |
| 11 | VISIBILITY | Public wrapper/domain retained per user preference. Private helper APIs remain exactly as freshly audited. |
| 12 | STRUCTURE |29 proof lines including2 comments (before22), ordinary≤30. hr0 case branches≤3 lines. Correlated existential bounds use same witness; splitting them would destroy useful correlation. No new helper merely to meet a cap. |
| 13 | MATHLIB | Five actual methods plus clean anonymous exact?/apply? probes below. Partial coefficient/positivity lemmas used directly. No target equivalent found; bounded searches do not establish absolute absence. |
| 14 | JUNK DEF | n/a: theorem, not definition; no definition touched. |
| 15 | EXISTS LEMMA | Nontrivial public existential bound, not trivial private witness wrapper. |
| 16 | SHOW/CHANGE | Only retained `show 0 < l from hl` is term annotation fixing the cast input; no tactic show rewriting a goal. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every effective binder and original hr0/hB audited/probed below; actual independent full old adapters protect public interface compatibility. |
| 19 | INEQUALITY | Every signature inequality uses ≤ or <; full occurrence table below. |
| 20 | NORMAL-FORM | Bound expressed as index≤explicit real quantity, natural witness bounds; standard inequalities, sqrt notation, and RSet membership. No new equivalence web. |
| 21 | SYNTAX-GEN | Removing derivable hr0/hB reduces caller obligations. Do not bundle hδ0/hδ1 into Set.Icc: no demonstrated downstream benefit. |
| 22 | IMPORT-FANOUT | n/a: no import changed. |
| 23 | CASTS |0 redundant casts added; `(r none : ℝ)` and coefficient Int→ℝ cross genuine domains; `(0 : ℝ)`/`(1 : ℝ)` annotations fix exact_mod_cast targets. No cast-normalization churn. |
| 24 | INSTANCE-NAME | No instance declaration introduced; anonymous section instances retained with original binder order. |

## Five-method search and literature

Raw actual searches: `/private/tmp/roth-public29-K/search-results.json`,
`/private/tmp/roth-public29-search.log`, `new-identifiers.log`.

| Method | Actual query | Result/action |
|---|---|---|
| A Lean-Finder | Roth lemma6 index polynomial rational point bound square root delta | Unrelated additive Roth-number bounds; no target match. |
| B Loogle | `MvPolynomial.coeff, _ ≠ 0`, corrected to `"MvPolynomial.coeff", _ ≠ 0` | First query unknown identifier in remote index; corrected query returns coeff_mem_coeffs, coeff_rename_ne_zero etc. No theorem replacement. |
| C LeanSearch | nonzero integer polynomial has coefficient absolute value at least1 | MvPolynomial.ne_zero_iff; polynomial Mahler/coeff facts. Use ne_zero_iff with Int.one_le_abs directly. |
| D source grep | full index_le_lem6, lem6Φ, Int.one_le_abs, ne_zero_iff | Full untruncated saved output shows project-specific target and standard coefficient facts. No mathlib full target match. |
| E local name pattern | MvPolynomial.ne_zero_iff; pos_of_mul_pos_right | Positive exact source hits. Index unavailable; empty index results would not prove absence. |

Auxiliary variants: coeff_mem_coeffs, coeff_rename_ne_zero, leadingCoeff_ne_zero,
Int.one_le_abs, positive-product right factor, ne_zero_iff. Common-equivalents table:
none of discrete/finiteness/separation/poles applies. No wrapper extracted for the2-call
coefficient derivation. Anonymous `exact?`/`apply?` use exact source prefix before target,
so cannot self-prove or cite failed named candidates. No unbounded multi_attempt repeated:
known previous stalled requests are recorded session limitations; compiler probes are bounded.

Public literature queries: “Roth theorem index lemma6 polynomial1955 rational approximations
algebraic numbers delta” and “Roth index lemma6 polynomial determinant generalization weights”.
Top relevant primary hits: [original paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf),
[journal record](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F),
and [Roth's ICM account](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf).
Read original paper pp9–12, Lemma6 and proof; local `.mathlib-quality/references/clean.tex`
705–885. The paper imposes stricter boundaries; we infer from its last numerical comparison between rp+1 and4rp/3 that rp≥3 suffices
for this part of the argument. The supported weakening is established
by compiled proofs, not asserted as a newly found literature theorem. No connected math
ChatGPT tool exposed: unavailable, not searched-and-empty. No unsupported literature-driven
API restatement applied.

Inversion check: R, hR, degree data, mapped determinant and rational-point index persist
through the structural proof. The purely real numerical abstraction is already the
freshly audited index_numeric_bound_aux; weight and mapping abstractions already exist.
No concrete object vanishes after one unfolding leaving an unextracted abstract proof.
Replacing ℤ coefficients or ℝ target would change RSet/Θ/index's mathematical domains;
no same-content candidate supported here.

## Generalisation — every binder

Negative probes are mechanical drop tests, not mathematical necessity proofs. Data-binder
failures mean the signature/body requires the referenced data; no claim that Lean disproved
all conceivable reformulations. All probes use autoImplicit=false where removing data.

| Binder | Role/use | Compiled candidate/probe | Result |
|---|---|---|---|
| τ : Type* | Index type in R,r,q,D and Θ | drop_tau | Unknown renamed type; universe already polymorphic. Retain. |
| Fintype τ | Sums, cardτ and Θ | drop_Fintype | Cannot omit referenced section instance. Retain. Finite-only would need chosen Fintype data, restating Θ. |
| DecidableEq τ | Already absent actual29 | candidate omit; actual full type | Remains absent, no reinstatement. |
| δ : ℝ | Weight loss and sqrtδ | drop_δ | Data dependency fails; real sqrt/Θ fixes domain. |
| hδ0 | Nonnegative product and weight helper | strict→weak full candidate; drop_hδ0 | Weak boundary compiled; drop fails. Retain0≤δ. |
| hδ1 | Numeric helper δ≤sqrtδ comparison | strict→weak full candidate; drop_hδ1 | Weak boundary compiled; drop fails. Retainδ≤1. |
| r | Natural degree/index weights | drop_r | Data dependencies fail. |
| original hr0 | Positive index weights | Entire candidate reconstructs from hrp+hratio+hδ0 | Drop compiled with old29 adapter and whole new30 caller. Applied. |
| hrp | Numeric rp≥3 and distinguished positivity | Full old reciprocal→3 adapter; drop_hrp |3-bound compiled, drop fails. No claim3 is globally optimal. |
| hratio | Every non-distinguished weight; derivative loss | drop_hratio | Fails; existing weak≤retained. No useful restriction of quantifier since every coordinate enters weighted sums. |
| r₁ | Common upper degree bound | drop_r₁ | Data dependencies fail. |
| hr₁ | Coefficient determinant estimate | drop_hr₁ | Fails; positive form remains all-coordinate common bound. |
| q | Rational point denominators/Θ | drop_q | Data dependencies fail. |
| hq | Protected positive denominators | Clean protected_hq_drop, exit0 + standard axes | Redundant in current proof but explicitly RETAINED. No recommendation to override user preference. |
| B | Coefficient height/lem6M | drop_B | Data dependencies fail. |
| original hB |1≤B for M/Θ nonnegativity | Entire candidate derives via hR.1+coeffbound | Drop compiled with full adapters/caller. Applied. |
| R | Integral polynomial | drop_R | Data dependencies fail. |
| hR | Nonzero, coordinate degree, coefficient bound | drop_hR | Fails; all three fields used, no bundled/unbundled weakening. |
| h | Rational-point numerator | drop_h | Fails/dependent signature; diagnostic heartbeat failure is not a necessity claim. |
| hh | Coprimality for separated index bound | drop_hh | Fails; required by index_det_le, no weaker proof supported. |

Full candidate old-telescope adapters preserve universes, ordinary binder names/order,
BinderInfo, conclusion, and actual opaque proof values. Anonymous instance names may be
renumbered; exact class/type/position is checked. New29's hr0/hB drops and previous DecEq
drop are the ONLY permitted drop set for29. Old strict hratio is forwarded by le_of_lt.

Probe correction: first negative/positive scratch prefixes accidentally retained a target
docstring followed by another omit command; logs kept as `*-first-attempt.log`. Corrected
prefix ends before target omit/docstring. Only clean corrected exit0 positive and corrected
expected-exit1 negative logs count. No PANIC/sorryAx or failed-run axiom certificate accepted.

## Signature packing and inequality tables

All widths are codepoints, not UTF8 bytes. `#check @Roth.index_le_lem6` is in actual
compatibility log, with format.width100. For expression continuation, next token means
complete syntactic expression rather than splitting an application unnaturally.

| Sig line | Width | Next complete binder/expression width | Arithmetic | Action |
|---|---:|---:|---|---|
|545|76|24 (hrp)|76+1+24=101|ok|
|546|83|21 (hr₁)|83+1+21=105|ok|
|547|72|31 (R)|72+1+31=104|ok|
|548|74|37 (hh)|74+1+37=112|ok|
|549|73|63 index expression|73+1+63=137|ok|
|550|69|54 doubled expression prefix|69+1+54=124|ok|
|551|62|62 sqrt expression and boundary|62+1+62=125|ok|
|552|72|none|n/a final|ok|

| Occurrence | Signature inequality | Orientation/action |
|---|---|---|
|hδ0|0≤δ|correct|
|hδ1|δ≤1|correct|
|hrp|3≤(r none:ℝ)|correct|
|hratio|r none≤δ*r(some j)|correct|
|hr₁|rj≤r₁|correct|
|hq|0<qj|correct/protected|
|witness lower|1≤l|correct|
|witness upper|l≤r none+1|correct|
|conclusion|index≤2*(...)|correct|
|reversed glyph scan|no ≥ or > in signature|no rewrite/no rename|

## All42 golfing rules

| Rule | Status |
|---|---|
|1.1 by exact|n/a no wrapper|
|1.2 by rfl|n/a no reflexivity wrapper|
|1.3 rw+exact→rwa|n/a no consecutive pair|
|1.4 simp+exact→simpa|Final terminal simpa already consolidates conversion; retained|
|1.5 trailing rfl|n/a|
|1.6 anonymous constructors|Shared l witness already anonymous constructor|
|1.7 apply/exact|Numeric apply deliberately leaves one min-bound obligation; not a redundant pair|
|1.8 by_contra!|n/a no contradiction chain|
|1.9 eta|Weight and positivity lambdas carry transformations, not eta forms|
|1.10 single-use have|Every term-have reused; proof hB retained substantive content|
|1.11 refine fun|n/a no apply+intro pair|
|1.12 redundant show|Retained term show pins natural positivity cast; not tactic-only redundancy|
|1.13 obtain|Already uses obtain for nonzero coefficient and determinant witnesses|
|1.14 merge rw|n/a no adjacent rewrites|
|1.15 terminal simp unsqueeze|Final simpa terminal; two simp-only calls nonterminal on hypotheses|
|1.16 nonterminal squeeze|Existing exact simp-only lists retained|
|1.17 dot notation|Uses trans/trans_le; direct mathlib coefficient and product facts|
|1.18 <\||No unnecessary parenthesized tail lambda introduced; no $|
|1.19 push_neg|n/a absent|
|1.20 trivial existential helper|n/a substantive public bound, no trivial helper|
|2.1 grind|Clean anonymous whole-proof trial bounded to20000 heartbeats; see automation.log|
|2.2 delete before grind|n/a no production grind chain|
|2.3 simpa consolidation|Already terminal coefficient/index conversion kept|
|2.4 fun_prop|n/a no continuity/measurability goal|
|2.5 positivity|Local positivity closes rp≥3→rp>0 but fails product-factor positivity (local-automation.log, expected exit1); explicit product fact retained|
|2.6 gcongr|n/a no monotone calc chain; terminal bound is nonlinear index theorem|
|2.7 lia|Retained derivative degree natural arithmetic lia; no omega introduced|
|2.8 aesop|Clean anonymous bounded whole-proof trial; see automation.log|
|2.9 norm_num/cast|Explicit exact_mod_cast bridges positivity/coefficient bounds; norm_num retains elementary3≤10 in caller|
|2.10 decide|Whole-proof trial; cannot decide free-data theorem; no native_decide|
|2.11 field_simp/ring|n/a no field identity goal|
|2.12 linear_combination|n/a no ring/ring_nf terminal proof with hypotheses|
|2.13 wlog|n/a distinguished Option.none and some branches have different mathematical roles|
|2.14 calc term|No two-step calc in public proof; final trans is already composed|
|2.15 <;>|No multiple identical residual goals to close|
|3.1 erw|n/a no erw|
|3.2 fun_prop upgrade|n/a no continuity/measurability|
|3.3 omega→lia|Public29 already lia; public30 statement's existing omega is outside minimal proof change|
|3.4 rcases/rfl|n/a no substitution pattern|
|3.5 attributes|No global simp/grind registration for substantive existential theorem|
|3.6 simp_all|Clean anonymous whole-proof trial; no simp_all-only production chain|
|3.7 remove limits|No production limits added/retained in owned declaration|

Step-back reflection: the determinant factorization and independent upper/lower bounds are
real structural steps; whole-proof search is tested on a target-free exact prefix. Pure
arithmetic already lives in the audited numeric helper, and mapping/weights have separately
audited helpers. The2/6-line new local facts do not justify new API wrappers. The shared
existential cannot be split into independently witnessed outputs. No further supported
change recommended.

## Verification, simplify and buzz

All normal gates completed on the frozen source below. Performance acceptance requires the
completed repeated timing evidence at the end; owner project/publication gates stay separate.

### Fresh complete native diagnostics

Native `lean_diagnostic_messages` on `/Users/ramin/LEAN/Roth/Roth/Theta.lean`, with no
severity/range/declaration filter, timeout_s300: success=true, partial=false,
timed_out=false, failed_dependencies=[],0 errors/11 warnings. Full raw unfiltered object:
`/private/tmp/roth-public29-K/final-lsp.json`. No filtered-zero-error substitute.

| Line | Warning | Disposition |
|---:|---|---|
|1|copyright header short|User explicitly protects metadata; untouched.|
|93|hr unused|Earlier protected Θ_nonneg choice; untouched.|
|101|hB unused|Earlier protected Θ_le_card choice; untouched.|
|101|hr unused|Earlier source outside29 scope; untouched.|
|109|hB unused|Earlier protected Θ_mono choice; untouched.|
|129|hr unused|Earlier protected Θ_mono choice; untouched.|
|252|hr unused|Earlier original; untouched.|
|547|hq unused|Explicit user RETAIN in public29.|
|583|Θ_option_le DecidableEq not in type|Public30's own later audit; telescope retained here.|
|586|Θ_option_le unused section DecidableEq|Same public30 later audit.|
|586|Θ_option_le hr0 unused|Newly exposed by public29 drop; preserved original30 public telescope under dispatch.|

### New identifiers, scope, and immutable evidence

| Identifier introduced in29 diff | Verified |
|---|---|
|MvPolynomial.ne_zero_iff|Actual native local search source hit; actual candidate compile; local #check.|
|Int.one_le_abs|Exact full source grep; actual candidate compile; local #check.|
|pos_of_mul_pos_right|Actual native local search source hit and #check; full compiled candidate.|
|trans_le|Existing standard order API; full candidate and actual module compile.|

All other identifier names in added lines were already present in source or are local
binders. Local positivity trial proves rp≥3→rp>0, but cannot infer factor positivity from
hratio; `local-automation.log` expected exit1. The explicit standard product fact stays.
`grind` closes the tiny distinguished-positivity trial. Whole-goal exact? fails; apply?
only suggests partial existential/findGreatest/filter reductions with residual goals
(and its expected scratch `sorry` warning), not a complete target lemma. grind/aesop/
simp_all/decide fail. No negative scratch output certifies axiom safety.

Actual compatibility source/log:
`/private/tmp/roth-public29-K/actual-compatibility-final.lean` and `.log`.
The immutable entire independent Index and Theta original namespace blocks are byte-identical to
`/private/tmp/roth-mapped-helper/actual-compatibility-final.lean`. The leaf's
`immutable-proof-provenance.json` hashes the Index block only:
`72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`.
Owner separately compared BOTH exact namespace blocks and saved
`/private/tmp/roth-public29-K/owner-both-immutable-blocks.json`; the full Theta block SHA256 is
`355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`.
Both byte comparisons pass; this corrects the earlier combined-hash description without changing
Lean source or requiring another compiler run. Preserved tails also check actual
private proof values, standard axioms, absence of deleted coefficient helper, and full
numeric/mapped/weight first-contract adapters. No unchanged-type check was incorrectly
used for changed29: its complete old telescope explicitly forwards weakened δ/rp/ratio
and precisely drops prior DecEq plus new hr0/hB. Entire original30 independent proof is
preserved; its actual current whole old type is checked, and actual opaque new30 proof is
explicitly checked to contain the actual new29 constant.

`scope-verification.json`: every private helper and all source outside exactly public29
and minimal public30 proof byte-identical; public30 visible signature identical; independent
full actual type verifies implicit instances too. No definition/import/documentation edits.
File937→946 lines (+9); public29 proof22→29 (+7), caller forwarding+2. No new helper audit.

### Gate status — dedicated revisit

| Gate | Result | Actual evidence |
|---|---|---|
|lake_build_file|pass|`/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0,34.272s; final-module-build.log/normal-gate-status.json.|
|candidate_before_apply|pass|candidate-compatibility.lean/log exit0 with full original29/30 proof/adapters and new caller dependency.|
|actual_type_value_axioms|pass|`lake env lean actual-compatibility-final.lean`, exit0,50.088s; exact old adapters, independent proofs, actual values via value!true, allowed3 axioms only.|
|complete_native_diagnostics|pass with explicit warnings|Native unfiltered complete result0errors/11warnings above; user-protected/out-of-scope warnings listed, none suppressed.|
|definition_protected|pass|No def/abbrev/import edit; scope-verification.json.|
|theorem_statement_protected|pass, authorized generalisation|Only independently compiled K/hr0/hB recommendation applied under standing user authority; conclusion preserved. Public30 entire effective telescope retained.|
|structure_gate|pass|29 ordinary proof lines≤30; maximum new branch3; correlated shared-witness ∧ retained intentionally.|
|naming_gate|pass|No forbidden name pattern/abbreviation; no rename queue entry needed.|
|line_packing_gate|pass|All8 measured signature rows justified.|
|inequality_orientation_gate|pass|Complete occurrence scan, no reversed inequality glyph.|
|cumulative_no_unintended_breakage|scoped pass|Only project caller is public30 in same compiled module; full old public30 actual type and independent entire original proof checked. Parent still performs downstream full build.|
|whole_project_build_then_LeanEval|PENDING OWNER|Not run by worker; mandatory parent sequential final gates before publication.|

Simplify pass (dedicated scope): manual holistic pass completed; no built-in simplify tool
exposed in this worker. Found no further supported reuse/style simplification. No wrapper
for tiny coefficient/positivity facts and no extra helper solely for line cap. No edits
from this pass. This does not claim a nonexistent tool invocation.

Rename/refactoring pass: no rename proposed, no shared queue writes allowed or performed.
Applied supported signature weakening and minimal caller forwarding only; no definition
inlining, no additional helper, no scope expansion. Original public wrappers remain.

### Required11-step phase checklist

1. ✓ Required skill/reference files read; scope/doctor inherited exact published baseline.
2. ✓ Full24-item fresh audit recorded.
3. ✓ All5 actual mathlib searches plus auxiliary variants and clean anonymous generic probes.
4. ✓ Every effective binder mechanically probed; original hr0/hB positive reconstruction,
   weakδ/rp candidate and protected hq positive probe; public literature/inversion recorded.
5. ✓ All signature lines measured in codepoints with justified breaks.
6. ✓ Every signature inequality occurrence scanned and correctly oriented.
7. ✓ All42 golfing rules given individual status, with actual applicable trials.
8. ✓ Step-back structural/API/normal-form review completed.
9. ✓ Fresh complete unfiltered native diagnostics0errors,11explicit warnings.
10. ✓ Actual module build, full old type/value/adapter/standard-axiom and scope gates;
    performance result below must pass before handoff.
11. ✓ No renames needed; no queue mutation; all owner-only publication gates explicitly pending.

### Buzz pass — exact entire prefix through original29

Real Lean4.34 command, no limit changes or profiling mask:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true \
  -Dtrace.profiler.threshold=0 /private/tmp/roth-public29-K/final-prefix.lean
```

Every byte of the live prefix through original29 is preserved, with only `end Lemma6`
and `end Roth` appended to close actual open scopes. This is prefix-only timing evidence;
the separate normal `lake build Roth.Theta` did compile the entire actual module.
No whole-file timing claim. Final prefix SHA256
`f7e8adfc76f82ecd70807b1e41eb228f7a624c2620c53f9c83061648d3f8d95c`.

All ordinary/search/compiler/native-LSP requests drained before profiling. Source edits
revoked at `2026-10-18T22:48:28.796167+00:00`, SHA256
`59fc1479999b47953aff7aee6bf8be17a325e9523ca94375d8b48b273618e427`.
Sole compiler window confirmed to owner. First full prefix exit0,179.597s,
156761775 rawUTF8 bytes, `/private/tmp/roth-public29-K/final-profile.log`.
`final-profile-manifest.json` records command, full/prefix/live hashes and isolation;
`final-timings.json` records all declaration anchors and disjoint top-level nodes.
Count outer Elab.command plus associated async proof/kernel/linter nodes, without nesting
or double-counting. All4 targets first measured below1000ms; public29/numeric exceed750ms,
so same-source entire-prefix repeat is mandatory and recorded below when complete.

| Target | First total ms | First command anchor line | First async proof anchor line |
|---|---:|---:|---:|
|weight_le_delta_aux|455.974|1090834|1090864|
|mapped_det_ne_zero_aux|722.709|1138323|1138426|
|index_numeric_bound_aux|918.885|1240740|1240785|
|index_le_lem6|996.125|1347479|1347568|

maxHeartbeats raises removed:0; added:0. No production profiling scaffolding. Existing
numeric-helper optimization and unchanged mapped certificate remain; this revisit weakens
the public boundary and recovers derivable assumptions locally. No default-budget failure.


### Accepted repeat and final freeze

Required same-source repeat completed exit0,175.400s,156745339 rawUTF8 bytes;
`/private/tmp/roth-public29-K/repeat-profile.log`, `repeat-profile-manifest.json`,
`repeat-timings.json`. Same full/prefix/live hashes as first; sole uncontended compiler.

| Target | First ms | Repeat ms | Repeat command/proof anchors | Result |
|---|---:|---:|---|---|
|weight_le_delta_aux|455.974|355.065|1088635/1088665|both<1000ms|
|mapped_det_ne_zero_aux|722.709|634.434|1136091/1136194|both<1000ms|
|index_numeric_bound_aux|918.885|829.176|1238379/1238424|both<1000ms|
|index_le_lem6|996.125|936.382|1347414/1347503|both<1000ms|

Buzz outcome: FAST-BOARD on both accepted real entire-prefix traces. No deferred over-budget
target; no source change after first freeze. The public target is close to budget on the
first run, with a confirming936.382ms repeat. Both ordinary default-budget module build and
all compatibility/axiom checks passed on this exact final SHA. Profile scope stays prefix-only.
No production profiling scaffolding, limit raises, new axiom, sorry, or native_decide.

All owned work completed; pending requests=[]; all source editing authority remains revoked.
Final source SHA256 `59fc1479999b47953aff7aee6bf8be17a325e9523ca94375d8b48b273618e427`.
`final-freeze-manifest.json` records final drain, hashes and all4 repeated timing acceptance.
Compiler/native-LSP window returned to owner. No Git operations or shared-log mutations.
Owner still runs full `lake build`, then separate `lake build Roth.LeanEval`, then central
report/history updates and exact stage/commit/push. These owner gates are not claimed done.
Counts unchanged210/264,Theta29. Future compatibility generator must encode K's weakδ/rp3
forwarding and the additional named hr0/hB drops for29; do not claim cumulative final-state
validation until public30's own later DecEq/API audit is applied and independently verified.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 92.105 s and 29.557 s.
Theta SHA256 `59fc1479999b47953aff7aee6bf8be17a325e9523ca94375d8b48b273618e427` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-k29-full.log` and `/private/tmp/roth-theta-k29-leaneval.log`; machine record
`/private/tmp/roth-theta-k29-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisits original 29; original counts
remain Theta 29/35, overall 210/264, 9/14 files. No new original or helper is counted.
