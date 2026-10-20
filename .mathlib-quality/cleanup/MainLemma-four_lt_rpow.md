# Cleanup: `Roth.four_lt_rpow`

Status: COMPLETE original8 per-change audit; UNPUBLISHED. Counts remain223/264,
MainLemma7/27 until owner publication. Wholefile performance certification and
the existing foreign slow-proof queue remain the file owner's separate work.

Entry source: `85af4993b70decb29489013593420d99644a93e2ac6891cecfa7cad5fb2b55f8`.
Evidence directory: `/private/tmp/roth-mainlemma-four-rpow/`.
Exclusive source/compiler/native/profile/report leases held during this audit;
explicit final freeze/drain/release is recorded at the end.

Caller repairs are limited to the three actual hX applications. In
three_small_factors, hδm is now mathematically unused. The exact original caller
contract, including this written binder, is intentionally retained for its later
fresh audit (original10). This is not a completed foreign generalisation audit.
An attempted `clear hδm` warning fix first failed on an unassigned base metavariable
(affected-build8-v2). Explicitly supplying the base made it elaborate in v3, but
did not remove the warning. Both redundant additions were therefore removed.
Final caller repairs use only `linarith only [...]` for the constant-bound proof.
The new unused hδm warning is reported honestly, without suppression or fake use.

## Reference reads

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Installed mathlib-quality
and lean4 SKILL.md read in full. Cleanup/cleanup-all/buzz commands consulted;
the complete 854-line authoritative worker prompt was recovered without truncation
in explicit ranges 1–300, 301–600, 601–854 after the initial wrapper-truncated read.
Relevant style-rules sections, naming-conventions, profiling, review-stages normal
forms/syntactic generality/documentation depth, prospective notes, and prospective
scoped-profile instructions read. Task/user overrides govern generalisation,
structural bounds, no subagents, central progress, and publication ownership.

## Audit (all 24 items)

1. LINT: no target warning in fresh complete unfiltered ML/Main diagnostics.
   Existing log_B₁_gt unused hδ0/hr₁ and file copyright metadata warnings are
   outside target scope; the new foreign unused hδm warning is disclosed above.
2. HAVE SCAN: entry L113 hm' has `by`, used twice (hδ1 and hkey arithmetic), KEEP;
   L114 hδ1 no `by`, used once implicitly by nlinarith, INLINE candidate;
   L115 hL has `by`, used in positivity and q positivity, KEEP;
   L120 hq has `by`, used once by rpow conversion, KEEP mathematical content;
   L125 hr has `by`, used once by h2, KEEP;
   L126 hlog4 has `by`, used once in hkey arithmetic, KEEP;
   L127 anonymous log bound no `by`, used once by linarith, INLINE;
   L129 hkey has `by`, used once in exp monotonicity, KEEP or eliminate via mathlib;
   L130 h1 has `by`, used once by final nlinarith, KEEP or use monotonicity API;
   L131 h2 no `by`, used once in final nlinarith, INLINE candidate.
3. SET_OPTION: none in declaration; no limits may be raised.
4. SIMP SQUEEZE: `simp [h] at hL` is terminal contradiction; retain unsqueezed
   if that branch remains. No nonterminal bare simp in entry target.
5. NAMING: four_lt_rpow describes the strict lower bound, is snake_case, and has
   no forbidden abbreviation or numeric scheme. No rename needed; queue preserved.
6. LINE PACKING: both entry and final two-line signatures measured below;
   the next complete binder cannot fit on either applicable first line.
7. BY PLACEMENT: all existing by tokens attach to preceding declaration/have line.
8. FORMAT: replace semicolon `rw [...]; exact hm'` by one tactic per line or a term.
   Preserve 2-space proof indentation and no internal blank lines.
9. COMMENTS: no inline proof comments present. Preserve source quotation in docstring.
10. DOCSTRING: updated to the constant-3 sufficient bound, retaining the historical quotation.
11. VISIBILITY: public justified by actual use in Roth/Main.lean:roth_of_isIntegral,
    in addition to three_small_factors and main_lemma in this file.
12. STRUCTURE: ordinary theorem, 23 declaration lines / 21 proof lines at entry,
    no conjunction conclusion, largest branch 5 lines, within ≤30 / ≤10 bounds.
13. MATHLIB: actual five-method searches recorded below. Loogle found
    Real.lt_rpow_of_log_lt, eliminating manual rpow/exp rewriting.
14. JUNK DEF: n/a, this is a theorem.
15. EXISTS LEMMA: n/a, no existential conclusion/witness wrapper.
16. SHOW vs CHANGE: no tactic-mode goal reshaping; the final term-mode show pins
    the real-valued numeric equality used by rw and is load-bearing in actual tests.
17. PUSH_NEG: none; existing push Not may combine with by_contra!.
18. GENERALISE: actual mechanical drop/strict-to-weak tests for every effective
    outer/inner binder recorded below; the dominating constant-3 variant is implemented.
19. INEQUALITY: zero reversed Lean inequalities; occurrence table below.
20. NORMAL-FORM: strict real-power lower bound is the natural consumer form;
    log comparison is internal via Real.lt_rpow_of_log_lt, no new equivalence API.
21. SYNTAX-GEN: removing the dimension and reciprocal hypotheses makes
    applications simpler; preserve conclusion, order and written binder names of
    retained parameters. Exact old contract must remain recoverable.
22. IMPORT-FANOUT: no new imports proposed; existing imports contain required API.
23. CASTS: nine individual actual tests recorded below; only the redundant
    signature numeral ascription was removed. Real bridges/load-bearing annotations remain.
24. INSTANCE-NAME: n/a, declaration introduces no instance.

Entry issues addressed: redundant strict/dimension/reciprocal premises, manual
exp/log conversion, trivial anonymous log scaffold, broad arithmetic context and
semicolon chain. No helper was introduced; no helper audit is pending.

## Initial line packing

| Signature line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 111 | 93 | `(hr₁ : 0 < r₁)` (13) | 93+1+13=107>100 | ok |
| 112 | 96 | none (proof follows) | n/a | ok |

Selected final signature, remeasured from actual source (the old table is entry evidence):

| Signature line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 112 | 69 | `(hq₁ : 3 ≤ δ ^ 2 * Real.log q₁)` (31) | 69+1+31=101>100 | ok |
| 113 | 67 | none (proof follows) | n/a | ok |

Final declaration 20 lines / proof body 18 lines, versus entry 23/21: 3 lines
saved. Largest inner proof block is hkey's 8 body lines, within ordinary ≤30 and
branch ≤10. No helpers added. Final target maximum line width is 96 codepoints.
Final HAVE SCAN: hL has no by but is used repeatedly; hq/hlog2/hr/hkey each carry
substantive by proofs and are KEEP. No single-use trivial term have remains.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | complete signature and all inner have types | no ≥ or > | none | none |

Post-edit re-scan of the entire actual target declaration also finds zero ≥/> in
Lean code, including inner have types. Docstring inequalities and the preserved
historical quotation are excluded by the gate's definition.

### Actual final cast/ascription audit (item 23)

`strong3-cast-probes-v2` mechanically removes each annotation separately and checks
closed type, exact expected complete type AST, actual opaque body typing and
standard axioms. The slab exits1 because the eight negative probes reject;
only signature_three succeeds. No failing probe is promoted by an exit0 fragment.

| Annotation tested | Actual result | Final action |
|---|---|---|
| signature `(3 : ℝ)` | closed standard proof, exact full type AST equal=true | remove redundant ascription |
| output `(q₁ : ℝ)` | HPow ℕ ℝ synthesis failure; recovered type rejected | keep real-power base cast |
| inner hr `(1 : ℝ)` | becomes natural inequality, wrong type for multiplication lemma | keep |
| quadratic-bound `(0 : ℝ)` | numeral division defaults to ℕ, wrong lemma argument | keep |
| rewrite `(4 : ℝ)` | natural equality cannot rewrite Real.log4 | keep |
| log-monotonicity `(0 : ℝ)` | wrong natural-valued positivity argument | keep |
| q inequality `(2 : ℝ)` | natural inequality cannot fill real-order argument | keep |
| log positivity `(1 : ℝ)` | wrong natural-valued positivity argument | keep |
| gap proposition ascription | linarith cannot infer the intended positive factor | keep |

The v1 slab had a misleading output_base success marker after a declaration-type
elaboration error: a body-only guard was insufficient. It was rejected immediately
because the actual compiler error and unequal full type AST were visible. V2 adds
explicit no-mvar/free/loose-variable/sorryAx type guards and exact AST equality;
the recovered output_base type now explicitly rejects. All later independent and
automation gates use the stronger closed-type guard. Both raw slabs are retained.

## Actual mathlib search status

A. Lean-Finder: queried delta≤1/m, logarithmic lower bound, real power >4;
   returned unrelated Behrend/Szemeredi bounds, no exact specialized match.
B. Loogle: `Real.log, _ < _ ^ (_ : ℝ)` returned Real.lt_rpow_of_log_lt,
   Real.lt_rpow_iff_log_lt and historical rpow_lt_of_lt_log.
C. LeanSearch: real power lower bound from logarithm and positive exponent;
   returned pow/le_zpow/lt_pow/log_le_rpow_div/rpow_le_of_le_log building blocks.
D. rg source: untruncated exact full-name + variants in Pow/Real and Log/Basic;
   exact `four_lt_rpow` search across Mathlib has no match (exit1).
E. lean_local_search: `log_lt_rpow` returned empty with index unavailable; this
   is explicitly not absence evidence. Follow-up `new-name-search.json` and fresh
   constant-3 local search return positive Real.lt_rpow_of_log_lt source hits;
   warming-index empty responses are never treated as absence evidence.

Partial match found: build on Real.lt_rpow_of_log_lt; keep the specialized
multi-premise numerical implication. Common-equivalents buckets do not apply.
No custom predicate, finite wrapper or 1–3-call wrapper introduced.

Fresh constant-3 searches are retained as `strong3-search-0..3.json` and
`strong3-source-search.log`: actual Lean-Finder, Loogle, LeanSearch, local search,
and source grep. No exact specialized replacement was found. Existing
Real.quadratic_le_exp_of_nonneg supplies the numeric logarithm bound without a
new import. The local index was warming for some results; empty warming/error
responses are not absence evidence. Positive source hits were compiled.

## Generalisation 2.6a–e

All outer binders below are effective binders, not just names explicitly referenced
in tactic text. The final imported metadata gate checks the complete old/current
types, written names, order, BinderInfo and universes.

| Binder | Class/use | Weakest-first actual tests | Result |
|---|---|---|---|
| `{δ : ℝ}` | scalar in exponent/log estimate | drop with autoImplicit false | rejected: dependent δ occurrences unbound; retained ℝ because the actual log/rpow API is real |
| `hδ0 : 0 < δ` | sign of exponent/product | drop; `0 ≤ δ` | drop rejects; non-strict succeeds in original proof and joint v6 candidate; retain weaker premise |
| `{m : ℕ}` | original natural dimension and reciprocal | drop with autoImplicit false; replace dimension-dependent bound by constant 3 | original mechanical deletion rejects; constant-3 proof removes this binder entirely |
| `hm : 1 ≤ m` | lower bound on dimension | drop original proof; derive in v6; constant-3 restatement | removed; old hm is used only in the exact old-contract adapter to derive the constant bound |
| `hδm : δ < 1 / m` | original bound on δ | drop; `δ ≤ 1 / m`; constant-3 restatement | removed entirely by the stronger constant-3 proof |
| `{q₁ : ℕ}` | logarithm base | individual drop with autoImplicit false | rejected: dependent q₁ occurrences unbound; no typeclass/point-local/universe parent applies to a fixed natural value |
| `{r₁ : ℕ}` | positive degree | individual drop with autoImplicit false | rejected: dependent r₁ occurrences unbound; natural degree is the consumer's mathematical domain |
| `hr₁ : 0 < r₁` | provides 1≤(r₁:ℝ) | drop; `0 ≤ r₁` | both reject; r₁=0 boundary violates strict conclusion, formally checked below |
| `hq₁ : 2m+1 < δ² log q₁` | logarithmic lower bound | drop; `≤`; constant 3 | constant-3 closed lower bound succeeds; old bound implies it using hm≥1 |

Actual negative slabs: `mechanical-entry-probes.{lean,log,json}` and
`inner-and-individual-probes-v2.{lean,log,json}`. Negative elaborator recovery
contains sorryAx and is rejected, never accepted as theorem evidence. Positive
joint candidate: `candidate8-v6.{lean,log,json}` was validated but superseded.
Selected stronger candidate: `strong3-v4.{lean,log,json}`, exit0, no timeout,
strict UTF8, all17 pins immutable, actual PGID absent, standard axioms only.
It uses natural-base discreteness, log q₁≥log2, and the existing quadratic
exponential bound to show log2<3/4. Thus (δ log q₁)²≥3 log2>(log4)².
The failed strong3-first/v2/v3 probes are retained; norm_num on the counterassumption
removes a numeral cast before square monotonicity. No new import is needed.

### Inner premises and derived facts

| Entry inner scope/fact | Actual audit/test | Selected treatment |
|---|---|---|
| hδ1: δ<1 | weaken to ≤; old `.trans_le` result mismatch | eliminated; no upper bound on δ remains |
| hL: log q₁>0 | weaken to nonnegative; old q=0 contradiction no longer closes | derive positive logarithm directly with `pos_of_mul_pos_right`; remove negated-log binder |
| negated log binder h | local assumption supplied by by_contra/push Not | remove entire contradiction proof using existing order API |
| q=0 / q>0 branch binders | Nat.eq_zero_or_pos proof cases | remove both cases via Real.log_pos_iff and nonnegative natural cast |
| hq: q₁>0 | weaken to ≥0; rpow_def_of_pos then rejects | retain positive base as an inline derived fact, no public premise |
| hr: 1≤r₁ | cast bridge from natural strict positivity | retain; dropping public hr₁ or allowing r₁=0 is refuted by boundary |
| hlog4: log4<3 | ≤ version succeeds under old strict hq₁ | eliminated; derive log2<3/4 instead |
| anonymous bound inside hlog4 | no-by single-use have | eliminated with old log4 estimate |
| hkey: log4<logq*(δr) | ≤ version rejects strict conclusion | replace by strict log4<δ logq, then multiply by r≥1 |
| h1: δ²logq<δlogq | ≤ version succeeds under old strict hq₁ | eliminated; new argument compares squares |
| h2: δlogq≤δlogq*r | no-by single-use have | inline le_mul_of_one_le_right |
| discarded v6 m≤0/hm0 | mechanical premises tested in v6 | eliminated with m and reciprocal constraint |
| selected hL, hq, hlog2, hr, hkey | hL is a multiply-used term; other four facts have substantive by proofs | KEEP; each carries positivity, cast, numerical, or square-comparison content |
| selected counterassumption h: δ logq≤2log2 | by_contra! binder, already non-strict | retained locally; no global property to localise |

No hidden section variables, structure instances, type parameters or universe
parameters occur. Scalar inequalities have no global→pointwise catalogue variant.
Real.log/rpow remain central throughout the argument, so the concrete-object
inversion diagnostic does not reveal a merely unfolded wrapper. No unsupported
abstract-field restatement is claimed. All selected weakenings are authorized
by the standing user instruction, and require exact old-contract recovery.

2.6b: both candidates were compiled, not inferred from sketches; all rejected
probes and their actual errors/sorryAx are retained.
2.6c: implement the dominating constant-3 restatement; no rename or helper.
2.6d: public literature search recorded below.
2.6e: selected changes remove m/hm/hδm, weaken hδ0 and replace the log lower bound
by constant 3; strict conclusion retained. The old full contract is recovered below.

Selected-statement mechanical probes `strong3-binder-probes-v1` test dropping
each of δ/hδ0/q₁/r₁/hr₁/hq₁, weakening hr₁ to nonnegative, and weakening the inner
hL/hq/hlog2/hkey facts. All eleven reject under actual opaque-body/axiom guards;
no rejected recovery containing sorryAx is accepted. Scalar and data binders have
no hidden instance/universe or global-to-pointwise hypothesis. A real base merely
greater than 1 cannot replace the natural base: log q can approach zero while
δ² logq=3, so δ logq need not exceed log4. Adding q≥2 would be a different API,
with an extra hypothesis; the current natural-base statement matches all callers.

The superseded v6 reciprocal counterexample applies only after dropping hm with
the dimension-dependent 2m+1 bound. It does not refute the selected constant-3 API.
The bounded-heartbeat test `strong3-hb-v1` compiles both complete original and
selected proofs under identical context with only Elab.async disabled, all limits
unchanged: 9,319,950→3,067,401 raw heartbeats (9319→3067 public units). Both actual
opaque bodies typecheck and depend only on propext/Classical.choice/Quot.sound.
This supplemental HB capture precedes the final redundant numeral-ascription
removal; actual final-source performance is measured separately below.

## Literature search (2.6d)

Query 1: `Roth theorem main lemma delta log q power bound generalization`.
Top three returned hits: [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Thue-Siegel-Roth_theorem),
[Maculan's Roth notes](https://webusers.imj-prg.fr/~marco.maculan/files/papers/roth_book),
[An Invitation to Modern Number Theory](https://dokumen.pub/an-invitation-to-modern-number-theory-9780691215976.html).
These search hits provide context, not a certified replacement for this numerical lemma.

Query 2: `exponential logarithm inequality log x less x minus one generalization`.
Top three returned hits: [NIST DLMF 4.5](https://dlmf.nist.gov/4.5),
[Math StackExchange question](https://math.stackexchange.com/questions/1222872/show-that-ln-x-leq-x-1),
[mirror of that question](https://wiki.hoelee.com/content/math.stackexchange.com_en_all_2023-08/questions/1222872/show-that-ln-x-leq-x-1).
Only the primary NIST formulation is relied on: it confirms the standard log(x)≤x−1
bound; mathlib supplies the strict x≠1 form and the general log-to-rpow implication.
The original numerical source quotation remains intact. All raw results are saved
as `literature.json`, `lit-roth.json`, `lit-log.json`; no exact specialized
replacement or additional literature-driven generalisation was verified.
ChatGPT math MCP: n/a, no callable mathematical second-opinion tool available.

## Golfing rule pass (all 42)

| Rule | Concrete status |
|---|---|
| 1.1 by exact wrapper | n/a: no target-level wrapper; final proof has substantive arithmetic |
| 1.2 by rfl | n/a: no reflexivity block |
| 1.3 rw+exact→rwa | removed manual rpow/exp conversion through the named mathlib implication |
| 1.4 simp+exact→simpa | no mergeable simp/exact sequence remains |
| 1.5 trailing rfl | n/a: none |
| 1.6 anonymous conjunction | n/a: no conjunction conclusion |
| 1.7 apply+exact | n/a: apply followed by a genuine nlinarith proof, not exact of a known term |
| 1.8 by_contra! | square comparison uses by_contra!; old negated-log contradiction removed |
| 1.9 eta reduction | n/a: no mathematical lambda |
| 1.10 inline single-use have | eliminate hδ1, h1, anonymous log bound; inline h2; retain substantive by proofs |
| 1.11 refine+fun | n/a: no apply/intro sequence |
| 1.12 redundant show | selected show is a required term type annotation in a lemma argument, not tactic-mode goal rewriting |
| 1.13 have projections→obtain | n/a: no projections of a paired hypothesis |
| 1.14 merge rw | remove the original rw/semicolon chain entirely |
| 1.15 terminal simp only | n/a: no squeezed terminal simp |
| 1.16 nonterminal simp squeeze | no bare nonterminal simp; norm_num normalizes the cast in h |
| 1.17 dot notation | hL.le and order-lemma projections used directly |
| 1.18 trailing parens | no gratuitous trailing proof parentheses; typed lemma arguments retain required grouping |
| 1.19 push_neg | none; old push Not removed with log contradiction |
| 1.20 trivial ∃ wrapper | n/a: no existential wrapper |
| 2.1 grind whole proof | actual independent whole-proof control rejects; no standard closed proof |
| 2.2 delete before grind | n/a: no grind in selected proof |
| 2.3 simpa consolidation | n/a: no simpa sequence remains |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability predicate |
| 2.5 positivity | whole-proof control rejects; local positivity discharges natural-cast side conditions |
| 2.6 gcongr | whole-proof control rejects; local monotonicity control also tested below; selected direct mul lemma is compact |
| 2.7 lia/omega | whole-proof controls reject transcendental goal; no Nat case arithmetic remains |
| 2.8 aesop | actual independent whole-proof control rejects |
| 2.9 norm_num/norm_cast | norm_num normalizes h and numeric side conditions; exact_mod_cast crosses Nat→Real for q₁ and r₁ |
| 2.10 decide | actual whole-proof control rejects free-variable target; no native_decide |
| 2.11 field_simp/ring | n/a: no field equality; nlinarith normalizes the square comparison |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint or equality certificate goal |
| 2.13 wlog | n/a: no symmetric case pair |
| 2.14 collapse calc | replace original two-line exp calc by Real.lt_rpow_of_log_lt |
| 2.15 close multiple goals | n/a: no parallel structural subgoals in selected proof |
| 3.1 erw→rw | n/a: no erw |
| 3.2 function-property automation | n/a: no continuity/measurability proof |
| 3.3 omega→lia | no omega in selected source; both actual whole-proof controls fail |
| 3.4 rcases rfl substitution | original Nat cases eliminated by log_pos_iff; no rcases remains |
| 3.5 automation registration | no attribute: specialized numerical bridge does not define a canonical simplifier/normal form |
| 3.6 simp_all | actual whole-proof control rejects; no simp_all in selected source |
| 3.7 limit removal | none present; no resource limit added or raised |

Whole-proof controls are actual separate theorem bodies, not merely first-tactic
replacements retaining the old suffix: `automation-guarded-v3.lean`. Every purported
success is checked using the actual opaque body and standard axioms. In particular,
apply? left zero visible goals but generated sorryAx and was explicitly rejected.
Native `lean_multi_attempt` output is separately retained; suffix diagnostics and
partial suggestions are not promoted to proof success.

## Step back and think

The decisive change uses discreteness: a natural base with positive logarithm is
at least 2. The constant-3 logarithmic bound then forces δ logq>log4 through square
comparison. No dimension or reciprocal bound is needed. Existing mathlib handles
the log-to-power conversion; manual exp rewriting and Nat base cases disappear.
Whole-proof automation and
generic exact?/apply? do not produce a closed standard proof. The final targeted
arithmetic keeps explicit small nlinarith inputs instead of broad proof search.
No new helper/API extraction, new imports, attributes, or global options are needed.

## Actual final correctness and native gates

`affected-build8-cast-final` passed actual `lake build Roth.MainLemma Roth.Main`:
exit0, 80.538s, strict UTF8 on separate stdout/stderr, 17 source/config pins
immutable, process group 50072 absent and drained. The earlier pre-cast final
build also passed; no pre-cast build substitutes for this final-source gate.

`independent-target8-v6` passed exit0/zero errors (35.822s). It compiles the full
unchanged project-original target proof independently (entry target equality was
checked against immutable project-original.lean), an exact old-contract adapter,
and the explicit expected new contract. Full raw type ASTs, all written names,
order, BinderInfo and empty universe lists match their expected contracts. The
old contract retains all nine binders; the new contract has six. The actual
opaque values (`value! true`) are closed, contain no mvars/free/loose variables
or sorryAx, infer to their genuinely closed full types, and use only propext,
Classical.choice and Quot.sound. The independent old-target closure visits 247
constants and excludes the actual current target and all three current callers.
The v2 harness failed only on boolean/list notation; v3 passed before the final
cast cleanup. Both rejected and prior passed harnesses remain preserved.

`independent-callers8-v6-full` passed exit0/zero errors (48.332s). It contains the
complete entry8 MainLemma/Main source copies in independent namespaces, with
explicit lam/gam/eta/B₁/approxSet namespace migrations. All three actual callers
match complete type ASTs and recursive binder names/order/BinderInfo/universes;
only generated names on both sides receive the parent-approved eraseMacroScopes
hygiene normalization, with raw names retained in the log. Written names are
never normalized. All migrations also pass isDefEq. Actual old/current opaque
values and their full types are closed and type-correct, with standard axioms
only. Old-proof transitive closures exclude the actual current target, all three
current callers and the uniquely resolved actual existing private helper
`_private.Roth.MainLemma.0.Roth.sqrt_lt_nat_floor_aux`: visited counts are
247/365/2536/2713 for target/three/main/roth respectively. This per-change recovery
does not complete the owner's pending cumulative project-original scaffold.

The same exit0 harness formally verifies the retained-hypothesis boundaries:
r=0 fails, negative δ fails, and missing logarithmic bound fails (q=1). It also
proves the new API at δ=3,q=2,r=1, beyond the original reciprocal restriction.
Every boundary has genuinely closed type/value and standard axioms only.

Fresh unfiltered actual native diagnostics: `native-final8-ml.json` and
`native-final8-main.json`, validated in `native-final8-validation.json`. BOTH have
success=true, partial=false, timed_out=false, failed_dependencies=[], isError=false,
zero errors. MainLemma has four warnings: pre-existing line1 copyright header,
log_B₁_gt hδ0/hr₁ at136, plus the newly mathematically unused foreign hδm at151.
Main has four pre-existing warnings: line1 header, hδ at333, hQ/hc at474/475.
No target warning, no sorry warning, no warning suppression or invented metadata.
Current module olean hashes and all17 source/config pins stayed stable through
both final independent gates and both native requests, recorded in
`after8-cast-final-imported-module-hashes.json` and `native-final-{before,after}-state.json`.
All native requests completed before after-profiling began.

## Profiling protocol and retained baseline

Actual CLI template for BOTH sides:
`/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
External process timeout900s; no Lean limits raised. Immutable before/after paths
differ explicitly. Each scaffold preserves the entire actual source prefix,
declaration bodies, types and order, with trace windows only around target and
actual direct consumers. ML scope is four_lt_rpow/three_small_factors/main_lemma;
Main scope is roth_of_isIntegral. Source/scaffold hashes and scopes are saved in
the corresponding `*-scope.json`. Actual final after snapshots are
`after8-final-{ml,main}.lean`, with matching `*-scoped.lean`; earlier after8 and
after8-v3 snapshots are preserved superseded candidates, not final captures.

Only canonical column0 Elab.command/Elab.async roots in the unique declaration
token span count. `parse8.py` invokes the owner's anchored_profile_span.py and
verify_profile_roots.py; it requires actual named proof plus kernel/lint roots,
excludes internal Meta/nested kernels/adjacent commands/foreign proof roots, and
retains each complete result and raw hash. Separators are exact declaration
tokens (name plus space), not substring first hits. No imported-self shortcut.

| Matched scoped BEFORE capture | Target four | three_small_factors | main_lemma | Main.roth_of_isIntegral |
|---|---:|---:|---:|---:|
| before8-ml-first | 774.351ms | 1803.356ms | 5403.445ms | n/a |
| before8-ml-repeat (same frozen source/scope) | 862.510ms | 1880.264ms | 5483.864ms | n/a |
| before8-main-first | n/a | n/a | n/a | 2997.107ms |
| before8-main-repeat-recovered-v2 (exact old binary; disclosed lookup wrapper) | n/a | n/a | n/a | 2993.523ms |

The target's ≥750ms first sample required the same-frozen repeat; both passed
the hard1000ms gate. Foreign consumers were already above1000ms. They receive
bounded matched regression checks, no independent cleanup/audit credit here.
Baseline raw hashes, actual argv, separate stdout/stderr, strict UTF8,
source/config pins, exit/timeout flags and actual PGID absence are saved in
each runner JSON. A rejected initial launcher interpreted --timeout as an
executable, started no child, and is explicitly preserved as no evidence.
The target baseline diagnosis attributes ~58% of its proof time to hkey and
broad nlinarith preprocessing; nested timings are diagnostic, never added to roots.

The parent's previous GLOBAL 818.063/754.120 target rows are not numerically
compared to these scoped captures. Final wholefile ALL90-row performance remains
the file owner's mandatory queue: the inherited actual wholefile failures for
δ/three/pigeonhole/main are not certified by these scoped checks or prefix passes.
The owner's older broad-δ parse/merged-UTF8 artifacts are not reused here.

Both required unchanged-source AFTER captures are retained for every direct
consumer ≥750ms. All canonical rows below have actual named proof, command,
kernel and lint roots, exit0, strict UTF8, immutable17pins and actual PGID absence.

| Matched scoped AFTER capture | Target four | three_small_factors | main_lemma | Main.roth_of_isIntegral |
|---|---:|---:|---:|---:|
| after8-final-ml-first (292.296s) | 367.057ms | 1814.087ms | 5315.959ms | n/a |
| after8-final-ml-repeat (297.227s) | 430.308ms | 2128.583ms | 7871.827ms | n/a |
| after8-final-main-first (146.811s) | n/a | n/a | n/a | 3118.857ms |
| after8-final-main-repeat (148.257s) | n/a | n/a | n/a | 3007.441ms |

The target passes1000ms in both retained after samples, with neither requiring
a target-triggered ≥750ms repeat. The second ML capture is required by its direct
consumers. No third unchanged sample was taken to select a faster result.
Foreign hard-budget failures remain failures in their existing audit queue;
they are not relabeled hard-budget passes or credited as independent cleanups.

### Bounded direct-consumer causal diagnosis

`consumer-top-level-step-diagnostics.json` preserves aligned top-level tactic
measurements for all retained captures; `consumer-causal-diagnosis-summary.json`
records the changed hX step and selected unchanged steps. These are diagnostic
subtrees and are NEVER added to canonical root sums. All aligned top-level step
counts agree: three36/main105/roth71.

| Changed hX step | BEFORE first/repeat | AFTER first/repeat |
|---|---:|---:|
| three_small_factors | 0.828 / 0.711ms | 27.439 / 34.885ms |
| main_lemma | 2.157 / 1.875ms | 15.079 / 26.803ms |
| roth_of_isIntegral | 0.872 / 0.895ms | 25.304 / 24.555ms |

The new constant-bound argument has a measured local cost of roughly13–34ms.
The large slow ML repeat extends across unchanged proof steps: hC762.196→1371.826,
hD197.863→532.866, hcount171.033→419.950ms. Even unchanged h32', BEFORE the edited
hX call, changes490.811→652.925ms. The first after main_lemma root is faster than
both before roots; the second is much slower on identical source. Main's second
after root3007.441ms is near its original2997.107ms baseline, whereas the first
is3118.857ms. These observations do not justify attributing the entire broad
variation to the API, nor claiming every consumer became faster. The measured
argument cost is explicitly retained as the local generalisation tradeoff; no
broader foreign proof cleanup is attempted. Overall ML capture elapsed times
before296.018/311.411s and after292.296/297.227s, with raw stdout bytes
206399896/206275528 before and192642177/192410520 after, are contextual evidence,
not a substitute for root accounting or wholefile certification.

### Recovery of the missing second BEFORE Main baseline

The initial beforeMain baseline had only one sample; this gap was disclosed.
The old imported ML API could not be replayed against the changed current cache.
With the owner's approval, exact frozen before8 ML source was rebuilt solely in
isolated output directories. `recovery-before-state.json` records current source
and cache hashes, original module/package/options/importArts from the copied Lake
setup JSON, and the expected old binary hash. The first reconstruction passed
exit0 (48.500s), but its olean hash differed because the isolated SOURCE filename
is serialized in the binary (offset2271856). This mismatch is preserved and is
not admitted as an exact old baseline.

Pinned Lean Shell.lean505–518 proves --stdin reads stdin bytes while retaining
the supplied filename. The bounded second reconstruction feeds exact frozen
before8 stdin SHA85af4993b70decb29489013593420d99644a93e2ac6891cecfa7cad5fb2b55f8,
with original logical filename/module/package/options and isolated outputs.
`recover-v7-stdin-provenance.json` distinguishes stdin from the physical current
source SHA2b8a5cab541e92ba56eb71142867bb3f562461682ccada4c07e7ea4fcfcd87a4;
the current file is not read as compiler input. The runner sees a Python exec
wrapper, so its automatic argv .lean-input map is empty; actual inner argv/stdin
and setup SHA are separately explicit. Exit0 (56.867s), strict UTF8, drained:
the recovered olean is EXACTLY the original recorded binary hash
`689f540cd0904909df40dfe68e2f051ca3a3eb24c4ba0d284b6278e78f867204`.
Reconstruction elapsed times are not performance samples. No additional semantic
equivalence approximation is needed when serialized identity matches exactly.

The first replay failed before target elaboration (9.362s, exit1): package-root
resolution sought Roth.Lattice under the isolated library. It is retained with
no timing credit. The concrete repair copies exactly the ten unchanged transitive
Roth artifacts enumerated by setup importArts into a FRESH closed isolated library,
alongside the three recovered ML outputs. Every one of13 artifacts is hashed;
no changed current Main or LeanEval artifact is copied. Legacy Roth modules emit
no split .olean.server/.private companions here; all actual generated outputs are
preserved. `recovered-before-main-contract-v2.json` records all copied artifacts.
An actual import probe passes exit0 and prints the old nine-binder public type.
An actual --deps probe explicitly resolves all11 Roth modules to the closed
isolated library, validated in `recovered-closed-resolution-validated.json`.

The second valid beforeMain replay uses the identical frozen scaffold SHA
fdcba95874ff8a4ba9ef42a7b3ed3548bcf719c71021b0ccae68713aab0338d3,
identical effective Lean flags and scope, with a DISCLOSED `lake env env
LEAN_PATH=... lean ...` wrapper to select the exact recovered old package.
Physical current17pins remain the frozen after source; logical frozen-before
17pins (old ML/Main source snapshots plus unchanged other15 pins) match the
initial actual before capture exactly. Both maps, exact argv and lookup paths
are preserved in the contract, rather than silently claiming byte-identical
wrapper argv or rolling back the current source/cache. The final repeated baseline
passes exit0 (142.072s), strict UTF8, immutable physical17pins, actual PGID60409
absence and canonical completeness:2993.523ms, ten disjoint command/proof/kernel/
lint roots. Raw stdout SHA
ccd44b7d2c7ae7b8fdc46e5f462d34cdbb4faf478a4c4e62680b59cab864719c.
`consumer-top-level-step-diagnostics-final.json` adds its71 aligned steps and
old hX0.895ms. The complete beforeMain pair is2997.107/2993.523ms. All required
before/after repeats are now complete; the failed pretarget launch is not a sample.

## Diff gates and phase checklist

`final-diff-protection.json` reconstructs the actual final files from immutable
entry8 copies using only the authorized target/doc replacement and three exact
hX-call repairs, and asserts byte equality. All definitions and other declaration
bytes are protected; declaration-name lists are unchanged. All other source/config
pins are stable. No imports, limits, axioms, sorry/admit, helpers or in-place
renames introduced. Existing Index and B₁ rename-queue bytes match entry d95ec18.
`git diff --check` passed. The owner may advance Git HEAD with metadata-only
takeover notes; this worker performs no Git mutation/publication or central writes.

| Gate | Status/evidence |
|---|---|
| definition_protected | PASS: all definition bytes unchanged |
| theorem_statement_protected | PASS under explicit standing authorization: stronger target inputs, exact unchanged conclusion/old adapter/current expected full AST; all foreign full contracts preserved |
| no_sorry/no_admit/no_new_axioms | PASS: source scan plus genuinely closed actual type/value and standard-axiom gates |
| no_limit_raise | PASS: no source option added; bounded HB only disabled Elab.async |
| structure_gate | PASS: ordinary declaration 20 / proof18 / largest inner body8, bounds30/10 |
| naming_gate | PASS: four_lt_rpow is descriptive, no forbidden pattern/abbreviation; no rename needed |
| line_packing_gate | PASS: both final signature lines remeasured, 69+1+31=101>100, no repack row |
| inequality_orientation_gate | PASS: required table plus post-edit full target scan zero ≥/> in Lean code |
| lake_build_file | PASS: actual final-cast ML/Main build exit0 |
| fresh_native | PASS: both complete/unfiltered actual files, zeroerrors; warnings accurately enumerated above |
| independent_original/current/callers | PASS: final v6 target and all3 caller gates exit0, closed type/value, exact contracts and allowed axioms |
| matched_after_performance | PASS for target1000ms gate and all required same-frozen repeats; bounded direct-consumer diagnosis complete, measured13–34ms argument cost disclosed; foreign budget failures retained, no wholefile certification claimed |

- [✓] Step 1 — all required reference docs and complete exact854-line prompt read.
- [✓] Step 2 — full24-item audit printed, including all effective outer/inner binders.
- [✓] Step 2.5 — all5 actual mathlib searches and status/partial matches recorded.
- [✓] Step 2.6 — a–e actual generalisation/drop/weakening/literature/implementation evidence recorded.
- [✓] Step 2.7 — final per-line measured line-packing table printed.
- [✓] Step 2.8 — inequality occurrence table and final zero-reversed scan printed.
- [✓] Step 3 — every one of42 golfing rules has a concrete status; original whole-proof controls are actual closed-proof probes, not suffix attempts.
- [✓] Step 4 — step-back reflection recorded.
- [✓] Step 5a — both actual full native diagnostic gates complete, target clean, zeroerrors; known foreign warnings reported.
- [✓] Step 5b — diff-gate status block above; target performance/repeat gates and bounded caller diagnosis complete.
- [✓] Step 6a — no rename needed, queue preserved byte-for-byte; no in-place rename.

Target issues addressed: strict sign premise; dimension binder; dimension lower-bound
premise; reciprocal premise; dimension-dependent strict log bound; manual exp/rpow
conversion; Nat base cases; anonymous log-bound scaffold; broad nlinarith context;
semicolon chain (10 addressed). A final redundant numeral type ascription was
additionally removed after actual individual tests. No target refactoring deferred.
No inline proof comments existed; the historical source quotation is preserved
verbatim (1 of1), with the docstring updated to the stronger sufficient bound.
Rules applied: 1.3,1.8,1.10,1.14,1.17,2.9,2.14,3.4 plus audit18/21/23.
No helper was introduced and no helper audit is pending. Prepared extra controls
for the selected stronger type were not compiled; they receive no evidence credit.
The required original-type whole-proof control slab and five fresh search methods
were actually executed and are retained above. No original9/10 audit credit claimed.

## Final result, freeze and lease release

Result: `Roth.four_lt_rpow`. Before23 declaration /21 proof lines; after20/18;
saved3 declaration/proof lines. Eleven target issues addressed (the ten listed
above plus the redundant numeral ascription). Helpers0; helper audits pending0;
renames queued0; target refactoring deferred0. All24 audit items,42 golfing rules,
five actual search methods, generalisation2.6a–e, measured packing/orientation
tables and all11 phase-checklist entries are present. Final per-change gates PASS,
including target367.057/430.308ms and all required direct-consumer repeat captures.
The measured13–34ms caller-argument cost and every slow foreign sample remain
explicit; no claim of a foreign1000ms budget pass or uniform caller speedup.

Final source SHA256 and sizes:

| File | SHA256 | Lines |
|---|---|---:|
| Roth/MainLemma.lean | 2b8a5cab541e92ba56eb71142867bb3f562461682ccada4c07e7ea4fcfcd87a4 | 696 |
| Roth/Main.lean | eb1a6650385707134c1be22b01707f2e5371340a1817188ad7b803cf2a7aa1cc | 685 |

`final-validation-board.json` checks all17 current source/config pins, current
cache immutability through isolated reconstruction/replay, closed old-library
artifact hashes, eight successful captures/sixteen canonically complete rows,
and24/42/5/11 coverage. `final-diff-protection.json` protects all unrelated source.
The usage-limit interruption left no orphan capture: resumed process inventory
and `resume-validated-state.json` verify old groups absent before relaunch.
`final-process-group-drain.json` freshly verifies all40 owned runner process
groups actually absent and no pending native request. `final-processes.txt`
retains the actual process inventory; shared persistent LSP infrastructure was
not terminated. Point CPU observations are not used to infer idleness from age.

Frozen source/report copies, all17 pins, current imported module hashes,
gate references and complete row board are sealed by `final-handoff-state.json`
and `evidence-manifest.json` in the evidence directory. The manifest covers all
prior artifacts, raw stdout/stderr (strict UTF8), scripts, snapshots and rejected
probes; it excludes itself and the final handoff to avoid circular hashes.
All failed casts/automation/recovery/import launches remain preserved; none
receive proof/performance credit. No successful unchanged third sample was used
to select a faster outcome.

The inherited GLOBAL wholefile failures δ11188.775ms, three1699.293ms,
pigeonhole1000.235ms and main4880.648ms remain the owner's final-file repair
queue. They are not numerically compared to the scoped rows and are not certified
by this audit. The owner's cumulative project-original full scaffold, final
wholefileALL90 rows, FULL build→separate Eval/root Eval native→review→exact stage/
metadata child/commit/push remain owner responsibilities. No publication or count
credit here:223/264 and MainLemma7/27 remain unchanged until publication.

FINAL FREEZE: no required original8 worker gate remains pending. All source,
compiler, native, profiler and report leases are explicitly RELEASED to the owner
with the sealed handoff. No further source/compiler/native/profile work will run
from this worker after that release.
