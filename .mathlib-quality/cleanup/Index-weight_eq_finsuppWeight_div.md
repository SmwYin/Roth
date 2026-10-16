# Roth.weight_eq_finsuppWeight_div — fresh single-declaration audit

Completed 2026-10-16 on `ramin-cleanup`, starting checkpoint `71dd84b`.
Sole source scope: `Roth/Index.lean`, original L129–138, final L130–137.
Canonical independent original snapshot: `/private/tmp/roth-index-original.lean` at `e557886`.

Result: approved removal of the unused σ-DecidableEq instance, before the byte-preserved
docstring; ordinary lambdas normalized to `↦`; direct finite-weight API and explicit
cancellation replace manual support expansion and `field_simp`. No other public mathematical
hypothesis, name, argument order, definition, import, documentation or declaration changed.
The actual public type **does change** by the approved instance omission. The remaining
`hr : ∀ j, 0 < r j` is preserved.

The theorem block decreases 10→8 lines (proof 8→6); the added scoped omission makes the whole
file 270→269 lines. No helper or rename was introduced. Owner confirms the only source users
are the two internal uses in `index_eq_weightedOrder_div`; there are no external callers.

## Scope and references

Read the complete fresh-worker contract, both skills, all of `cleanup.md` and `cleanup-all.md`,
and the complete golfing, proof-pattern, search, generalisation, cleanup-gates, naming,
review-stages, profiling and buzz references. Read the style sections relevant to theorem
signatures, inequalities, mathematical API, comments, casts, instances, hypotheses, imports,
performance and syntax. The skills' source-preservation defaults and this session's stricter
approval contract take priority over generic docstring/visibility suggestions. No subagents.

I have read `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, and `cleanup-gates.md` in full.

The mathematics: let D be the finite product of the positive natural denominators. Each
r_j divides D, so casting its natural quotient gives the real quotient D/r_j. Expand the
natural weighted sum, distribute division by D, compare summands, and cancel the nonzero D.
This is an arithmetic bridge between two existing weight APIs, not a new definition.

## All 24 audit items

| # | Item | Concrete finding and resolution |
|---|---|---|
| 1 | LINT | Baseline complete native diagnostics identify unusedSectionVars and unusedDecidableInType for this target. Approved omission removes both. Final full native result has no target warning/error. |
| 2 | HAVE SCAN | Original `hD` has an embedded `by exact_mod_cast hr i` proof, used by denominator discharge; retained as an explicit positivity fact, now referenced once as `hD.ne'`. Original `hrj` has a `by exact_mod_cast` proof and one explicit use in cast_div; removed because cast_div_charZero eliminates that obligation. No proof-free single-use alias remains. |
| 3 | SET_OPTION | None in target; no limits, linter suppressions or debug options added. |
| 4 | SIMP SQUEEZE | Original `(by simp)` closes the zero-smul side goal supplied to sum_fintype, so genuine terminal simp, no squeezing needed. Replaced the entire manual expansion with weight_eq_sum. Final target has no simp invocation. |
| 5 | NAMING | `weight_eq_finsuppWeight_div` states its two sides and operation; embedded `finsuppWeight` reflects the named API subject. No forbidden abbreviation, numbered scheme, `_ge_`/`_gt_`, single-letter name or numbered auxiliary. No rename needed or applied. |
| 6 | LINE PACKING | All signature lines measured below; actual built #check at format.width100 included. No hypothesis or complete conclusion clause fits across the existing break. |
| 7 | BY PLACEMENT | The declaration and both inline proof constructions place `by` at the preceding expression's end; none alone. |
| 8 | FORMAT | Two-space proof indentation; four-space signature continuation; no internal blank line, trailing whitespace or haveI/letI. Three ordinary lambda arrows normalized. Final cancellation merged into preceding rw. |
| 9 | COMMENTS | Zero inline proof comments before and after. All three existing docstring lines preserved byte-for-byte; surrounding module metadata untouched. |
| 10 | DOCSTRING | Existing public docstring explains D and source implementation context, not merely the raw equality. Preserved under explicit contract; no new docstring or source note. |
| 11 | VISIBILITY | Public arithmetic bridge supporting the weighted-order API; exported status protected. No private helper needed. Classic file, not module dialect. |
| 12 | STRUCTURE | Six proof lines; no conjunction, case split or >10-line branch; comfortably below all thresholds. No decomposition flag. |
| 13 | MATHLIB | Five actual methods below. Positive partial matches Finsupp.weight_eq_sum and Nat.cast_div_charZero used directly. Remote DNS failure disclosed; no unjustified absence claim. |
| 14 | JUNK DEF | n/a: target is a theorem, creates no data wrapper. |
| 15 | EXISTS LEMMA | n/a: not private or existential. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every binder, drop test, finite-parent attempt, strict→weak and support-local form checked below. Only already approved DecidableEq omission applied. |
| 19 | INEQUALITY | All inequalities use `<` with zero on the left; occurrence table below. No reversed notation or name. |
| 20 | NORMAL-FORM | Equality converts Roth rational weight to natural Finsupp.weight/D, exactly the form consumed by the weighted-order bridge. No equivalence clique or simp attribute introduced. |
| 21 | SYNTAX-GEN | Existing explicit hr and d support rewriting in either direction at the two bridge sites. No easier equivalent call shape justified changing the protected API. |
| 22 | IMPORT-FANOUT | n/a: no imports added or removed. Scratch tactic imports do not affect source. |
| 23 | CASTS | No cast removed merely cosmetically. Kept cross-type natural→real cast of Finsupp.weight and natural denominator; `(0 : ℝ)` and `(r i : ℝ)` fix the real positivity/product target. No redundant same-type cast introduced. |
| 24 | INSTANCE-NAME | n/a: target declares no instance. Approved omission removes an inherited decidability binder; creates no classical/global instance. |

Issues fixed: both target instance warnings; three lambda arrows; manual finite-sum expansion;
redundant individual-denominator proof; costly final field_simp. Refactoring needed: none.

## Five actual mathlib search methods

| Method | Actual query/action | Result and verification |
|---|---|---|
| A Lean-Finder | `natural number weights common denominator finite sum rational weight`, num_results3, bounded direct MCP helper | DNS `nodename nor servname provided, or not known`; unavailable, not evidence of absence. `/private/tmp/roth-weight-div-finder.json`. |
| B Loogle | `Nat.cast (_ / _) = _ / _`, num_results3, bounded direct MCP helper | Same DNS failure, `/private/tmp/roth-weight-div-loogle.json`. |
| C LeanSearch | `cast natural number division when denominator divides numerator`, num_results3, bounded direct MCP helper | Same DNS failure, `/private/tmp/roth-weight-div-search.json`. |
| D Local source | Untruncated rg of target's full name; cast_div in Data/Nat/Cast/Field; weight_apply/weight_eq_sum/sum_fintype in Data/Finsupp/Weight; cancellation variants in Algebra/GroupWithZero and Algebra/Group/Basic | No full-name target match in mathlib; actual partial matches weight_eq_sum at Weight.lean100, cast_div_charZero at Field.lean41. Existing direct theorem bodies inspected; new API references compiled against built imports. |
| E Name pattern | Native lean_local_search `Nat.cast_div` and `weight_eq`, limit20 for latter | `weight_eq` returns Finsupp.weight_eq_sum and weight_eq_zero_iff_eq_zero, among unrelated results. Index warming reported, so empty results would not establish absence. Generated scratch-target hits excluded from evidence. |

Auxiliary variants: weight_apply/weight_eq_sum/weight_single; cast_div/cast_div_charZero;
mul_div_assoc/mul_div_right_comm/div_right_comm/div_div_cancel/mul_div_cancel_right₀.
Common-equivalents table: no discrete/finiteness/topology bucket applies.

Compiled generic-route probe: native `exact?` on original goal fails to close; `apply?`
returns generic Real extensionality and division rearrangement obligations, not this bridge.
Whole grind, simp and aesop do not solve the original goal. Some multi_attempt results
include errors from the original remainder because that tool replaces a tactic rather than
the entire body; only the explicit tactic-failure/remaining goal is used as evidence.
No global absence claim is made with the three remote indexes unavailable. Conclusion:
keep this project arithmetic bridge, build directly on the two identified mathlib lemmas.
No missing wrapper API needs extraction: the now six-line proof expresses the actual cast,
finite sum and cancellation argument once, without repeated wrapper round trips.

## Every-binder mechanical generalisation

Probes use `set_option autoImplicit false`. Artifact
`/private/tmp/roth-weight-div-binders.lean` with final diagnostics in
`/private/tmp/roth-weight-div-binders2.log` records every negative substitution. These are
expected failed candidate checks, not accepted proofs. The first run omitted FieldSimp's
scratch import and had extraneous unknown-tactic errors; it is excluded. The rerun adds
that import and preserves the actual meaningful failures below.

| Binder | Classification/use | Candidates mechanically checked | Result |
|---|---|---|---|
| Universe behind `Type*` | universe-polymorphic | Inspect actual built #check; no fixed universe to weaken | Actual theorem is Type u_1; already fully universe-polymorphic. |
| `{σ : Type*}` | type variable, domain of r and d | Drop with autoImplicit=false | Unknown σ in Fintype and signature. Domain needed; no further algebraic/topological structure assumed. |
| `[Fintype σ]` | enumeration data for weight and product | Drop; replace by `[Finite σ]` | Both fail to synthesize Fintype in the statement's sums/products. A Finite-to-Fintype construction would restate the enumeration context, not a direct binder drop. No other parent class applies. |
| `[DecidableEq σ]` | decidability, no mathematical role | Drop in independent standalone candidate and actual target via approved omit | Candidate alt4 exit0; actual full native diagnostics and module build pass. Actual built #check confirms absent, original type recovered separately. Applied. |
| `{r : σ → ℕ}` | data, denominators and natural weights | Drop with autoImplicit=false | Unknown r in hr and conclusion. Function is used throughout, no property class to weaken. |
| `(hr : ∀ j, 0 < r j)` | proposition ensuring D≠0 | Drop; weak ∀j,0≤rj; local ∀j∈d.support,0<rj (reordered in scratch solely so well-scoped) | Drop leaves unknown hr in positivity proof; weak form fails exact_mod_cast positivity; local form supplies a membership→positivity function, not the positivity needed for all product factors. A separately compiled counterexample below proves these two proposed mathematical weakenings false. Preserved. |
| `(d : σ →₀ ℕ)` | structure value, exponent vector | Drop with autoImplicit=false | Unknown d in both sides, cannot disappear. No positivity/continuity/localization property attached to this data binder. |

The stricter hypothesis is mathematically essential to this particular D: on Fin2 take
r=![0,1] and d=Finsupp.single1 1. Compiled examples show the left side is1, the right
side is0, and all support-local denominators are positive. Thus merely nonnegative weights,
no hr, and positivity restricted to d.support cannot give the stated identity.
`/private/tmp/roth-weight-div-counterexample.lean`, log `...-counterexample2.log`, exit0.
The first counterexample run lacked Fin vector/big-operator imports; only the corrected
run is accepted. The counterexample does not alter source or the theorem statement.

Inversion check: after expanding Roth.weight, the proof is an abstract finite-sum
arithmetic computation, but generalizing its real codomain would require changing the
separate protected weight definition. No such API proposal is applied. Replacing D by
a common multiple is a different API restatement, not a drop of a current binder.
No further compiled public generalisation is proposed for approval.

## Public literature and first-three displayed leads

Actual searches used the web search tool. Initial two-query batch produced mixed rankings;
for auditable per-query rankings both queries were repeated separately (R1/R2 below).
These repeated rankings are recorded as repeats, not reconstructed as initial results.

| Query | Rank1 displayed | Rank2 displayed | Rank3 displayed |
|---|---|---|---|
| R1 repeat: `Takloo Bighash Yin Formalizing Roth theorem index weights common denominator generalization` | [An Invitation to Modern Number Theory, Google Books](https://books.google.com/books/about/An_Invitation_to_Modern_Number_Theory.html?id=IxDzVsrIyqEC) | [Miller–Takloo-Bighash chapter](https://web.williams.edu/Mathematics/sjmiller/public_html/238/currentnotes/AlgTrans_Chap5.pdf) | [An Invitation, JSTOR](https://www.jstor.org/stable/j.ctv131bw89) |
| R2 repeat: `weighted degree rational weights integer common denominator polynomial generalization` | [Rational Simplification Modulo a Polynomial Ideal, SFU](https://www.cecm.sfu.ca/CAG/papers/ratsimp.pdf) | [Weighted Ehrhart theory, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0001870824001427) | [Rational Simplification, second SFU address](https://www.cecm.sfu.ca/~mmonagan/papers/ratsimp.pdf) |
| `Roth polynomial index rational weights common denominator generalization` | [AMS Chapter4 Rational](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf) | [Irrationality measure, Wikipedia](https://en.wikipedia.org/wiki/Irrationality_measure) | [Wright notes, Berkeley](https://people.eecs.berkeley.edu/~fateman/282/F%20Wright%20notes/week1.pdf) |
| `Takloo-Bighash Yin "Formalizing Roth" index` | [Formalizing Informal Communication, Minerva](https://doi.org/10.1007/s11024-026-09639-w) | [Same unrelated article, arXiv2507.12812](https://arxiv.org/abs/2507.12812) | [Non-functional requirements, d-nb](https://d-nb.info/1221521462/34) |

The last query's top three are irrelevant and supply no mathematical evidence. The AMS
preview returned403 when opened, so its snippet is not treated as full-text verification.

Primary sources actually read: Roth's [1955 paper, §4 pp7–8](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/div-class-title-rational-approximations-to-algebraic-numbers-div.pdf)
defines the index relative to the r parameters and gives its derivative/product laws.
The [SFU authors' paper, p4](https://www.cecm.sfu.ca/CAG/papers/ratsimp.pdf) discusses
weighted degree orders graded by positive weight vectors. Neither source claims that
support-local positivity makes a global product denominator invertible. The project's
primary `.mathlib-quality/references/clean.tex` L546–555 explicitly describes D=∏r_j and
natural w_j=D/r_j for positive integral r, and distinguishes arbitrary positive real weights.
That source directly matches this bridge; no literature-supported missing hypothesis drop
was found. These findings concern formulation, not a claim to exhaustive mathematical novelty.
ChatGPT math MCP: unavailable in this tool inventory; no second-opinion result invented.

## Complete signature packing and inequality artifacts

The source signature has two lines. Codepoint widths count Unicode as one character.
The next complete signature clause is the conclusion expression, including `:= by`;
it cannot join the hypothesis line within100 characters.

| Signature line | Characters | Next signature clause | Arithmetic | Action |
|---|---:|---|---|---|
| 130 theorem/binders/colon | 82 | `weight r d = ... := by` (79 without indentation) | 82+1+79=162>100 | ok |
| 131 equality/`:= by` | 83 | no next signature line, proof starts | n/a | ok |

Actual built output from `/private/tmp/roth-weight-div-recovery.log`, compiled with
`set_option format.width 100` (not pp.width):

```lean
@weight_eq_finsuppWeight_div : ∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ},
  (∀ (j : σ), 0 < r j) → ∀ (d : σ →₀ ℕ), weight r d = ↑((Finsupp.weight fun j => (∏ i, r i) / r j) d) / ↑(∏ i, r i)
```

The printer itself retains a long equality clause; no claim that every pretty-printer
output line is capped at100. Source signature lines have widths82 and83.

| Occurrence | Location | Inequality | Rewrite | Name action |
|---|---|---|---|---|
| 1 | hr in signature L130 | `0 < r j` | already oriented | none |
| 2 | local positivity L132 | `(0 : ℝ) < ∏ i, (r i : ℝ)` | already oriented | none |
| reversed scan | complete signature and proof | zero `≥` and zero `>` inequality tokens | none | no `_ge_`/`_gt_` name |

## Every golfing rule (42/42)

| Rule | Status and actual evidence |
|---|---|
| 1.1 by-exact wrapper | n/a: declaration is a substantive tactic proof; nested exact_mod_cast is substantive cast reasoning. |
| 1.2 by-rfl | n/a: no by-rfl. |
| 1.3 rw/exact→rwa | n/a: no closing exact after rewrite. |
| 1.4 simp/exact→simpa | n/a: no such sequence; eliminated terminal side-goal simp with direct API. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor→tuple | n/a: equality, no constructors. |
| 1.7 apply/exact | n/a: no apply/exact sequence. |
| 1.8 by_contra! | n/a: no contradiction reasoning. |
| 1.9 eta lambdas | Lambdas compute quotient, perform cast proof, or expose a summand hole, so not eta wrappers; all ordinary arrows normalized to ↦. |
| 1.10 single-use have | hD retains embedded `by exact_mod_cast` proof content; hrj's entire obligation removed using cast_div_charZero. No proof-free alias left. |
| 1.11 apply/intro | n/a: sum_congr already uses refine/fun. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: no conjunction-valued have. |
| 1.14 merge rw | Applied: direct cancellation lemmas join the existing final cast rewrite. |
| 1.15 unsqueeze terminal simp | n/a: old side-goal terminal simp was already bare; no final simp only. |
| 1.16 squeeze nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | Existing hD.ne' retained; direct Finsupp/Nat API names carry subject and require no wrapper. |
| 1.18 application parentheses | Existing fun application already avoids parentheses; nested Finset divisibility argument is a required argument before further rewrite lemmas, not terminal `<|` opportunity. |
| 1.19 push_neg | n/a: absent. |
| 1.20 existential wrapper | n/a: no existential helper. |
| 2.1 whole grind | Tried native with weight and weight_apply hints; fails at nonzero-product/cast arithmetic. On the final scalar goal grind succeeds, but explicit three-lemma cancellation chosen for clarity and measured performance. |
| 2.2 delete pre-grind tactics | n/a: no grind retained; cast bridge cannot be inferred by tested whole grind. |
| 2.3 simpa consolidation | n/a: no closing simp/exact block; terminal scalar simp alternative did succeed, see alternatives below. |
| 2.4 fun_prop | n/a: algebraic finite-sum equality, no analytic function property. |
| 2.5 positivity | Actual standalone candidate `have hD ... := by positivity` fails strict positivity; reports only nonnegativity available. Kept explicit prod_pos using hr at each index. |
| 2.6 gcongr | n/a: no inequality goal in the main proof or monotonicity chain. |
| 2.7 lia/omega | n/a: no linear integer arithmetic goal; natural exact division is handled by cast_div_charZero and dvd_prod_of_mem. |
| 2.8 aesop | Tried on original goal; exhaustive search leaves the weight equality. |
| 2.9 norm_num/norm_cast | Native norm_num fails on scalar cancellation; exact_mod_cast is retained once per factor in positivity. Nat cast rewrite now uses characteristic-zero API. |
| 2.10 decide | n/a: arbitrary real equality over arbitrary finite index type, not a closed finite decidable computation. |
| 2.11 field_simp/ring | Original field_simp compiles, but profile identifies156.48ms hotspot. Replaced by measured direct rewrites; ring alone does not cancel the abstract inverse. |
| 2.12 linear_combination | n/a for final source: no ending ring/ring_nf and no polynomial hypotheses; denominator cancellation already direct. Independent verification uses ring only for commutative rearrangement. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc→term | n/a: no calc. |
| 2.15 multiple goals/<;> | n/a: sum_congr has one pointwise goal, not several similar branches. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 legacy analytic tactics | n/a: no continuity/measurability goals or tactics. |
| 3.3 omega→lia | n/a: neither occurs; no applicable linear arithmetic problem. |
| 3.4 rcases/rfl | n/a: no rcases. |
| 3.5 automation attributes | No attribute added: converting to natural weights introduces product and divisibility structure, unsuitable for default simp normalization. |
| 3.6 simp_all | n/a: no simp_all only retained; equality is proved directly. |
| 3.7 heartbeat options | None existed in scope; zero added. Scratch measurement wrapper is outside source. |

Step-back review: the proof now has one cast bridge and one scalar cancellation per
summand; direct weight_eq_sum removes manual finite-support plumbing. Whole-proof
search did not find a one-step replacement. A helper would wrap this single short
calculation and add API without a second consumer of its internal steps. The existing
hD explicitly records the mathematically necessary global positivity, which is clearer
than burying its factor proof into the last rewrite argument.

## Alternatives, simplify review and buzz

* Native final-scalar alternatives: explicit cancellation rw succeeds; terminal
  `simp [div_eq_mul_inv, mul_assoc, mul_left_comm, hD.ne']` succeeds; grind succeeds;
  ring and norm_num do not close. Explicit cancellation identifies exactly what is used.
* Initial direct cancellation attempt used mul_div_right_comm incorrectly; compiler
  exposed the changed expression, then corrected to reverse mul_div_assoc followed by
  div_right_comm and mul_div_cancel_right₀. Only corrected exit0 candidate is adopted.
* Actual standalone alt4 (weight_eq_sum, cast_div_charZero, no σ-DecidableEq) exits0.
  Its proof is applied to the actual file and measured there; no scratch-only success
  substituted for an actual module/profile gate.
* Scoped simplify review: PASS-THROUGH after these changes; direct reuse, no duplication,
  no redundant cast or private wrapper. Built-in simplify callable is not exposed here;
  file-final fresh simplify review belongs to owner under the leaf contract.

Buzz outcome: FAST-BOARD for this target, budget1000ms. Native lean_profile_proof was
actually attempted and failed standalone extraction (`cannot omit referenced section
variable`, then unexpected end); this is not a timing result. Fresh CLI traces are used.

| Measurement | Before | After |
|---|---:|---:|
| Anchored command+async total | 439.849ms | 212.334ms |
| Anchored proof | 404.052ms | 174.743ms |
| Dominant proof step | field_simp156.480ms | hD positivity73.841ms |
| Deterministic standalone heartbeats | 1501 | 583 |

Exact commands, each completed exit0:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean
python3 /private/tmp/roth-index-profile-parse.py weightdiv-before
python3 /private/tmp/roth-index-profile-parse.py weightdiv-after
```

Trace logs `/private/tmp/roth-index-weightdiv-{before,after}-profile-trace.log` and tables
`...-profile-table.json` anchor all19 current declarations; table maxima are not substituted
for the target. Initial premature before-parser invocation while the compiler still ran
failed its all-anchor assertion; rerun only after exit0 succeeded. No timing from the
incomplete log is used. The actual before trace target is439.849ms, not the approximate
354ms inherited checkpoint estimate. CountHeartbeats syntax initially lacked `#`, then
was corrected; only `/private/tmp/roth-weight-div-heartbeats2.log`, exit0, counts.
No over-budget deferral, no limit raise, no source profiling scaffolding.

## Verification and diff gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Index`, exit0, `/private/tmp/roth-weight-div-build.log`, final `Build completed successfully (1501 jobs)`. |
| Complete native diagnostics | pass for target | Unfiltered native lean_diagnostic_messages on actual Index: success=true, partial=false, timed_out=false, failed_dependencies=[]; all18 remaining items are warnings outside target. Raw complete result `/private/tmp/roth-weight-div-native-final.json`; zero target errors/warnings. |
| Independent ORIGINAL proof | pass | `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-weight-div-independent.lean`, exit0. Imports Box, Cast.Field, Finsupp.Weight and tactics, not Index; no same-file shortcuts/helper. Fresh proof multiplies by D first, distributes sum_mul, casts exact quotients, closes commutative rearrangement by ring. |
| Exact original public type recovery | pass | Original theorem signature copied mechanically from e557886 snapshot into recovered_original under original σ/Fintype/DecidableEq context, proved using actual built Roth.Index, exit0 `/private/tmp/roth-weight-div-recovery.log`. #check confirms original DecidableEq binder present in recovered type. |
| Actual built signature | pass | Same recovery file imports built Index; actual target #check shows Fintype only, no DecidableEq, and the same r/hr/d/equality. |
| Axioms | pass | Actual target, recovered_original, and independent original proof each print exactly [propext, Classical.choice, Quot.sound]. No sorry, new axiom or trust downgrade. |
| definition_protected | pass | No def/abbrev/import or any other declaration changed in start-snapshot diff. |
| theorem_statement_protected | pass, approved exception | σ-DecidableEq omission only public type change; equality syntax only lambda arrow normalization. hr and all data/math preserved. Original full type recovered separately. |
| structure_gate | pass | Six-line body, no conjunction or branches. |
| naming_gate | pass | Mathematical descriptive name; no forbidden pattern; no rename needed. |
| line_packing_gate | pass | Both signature rows measured above, all clauses fit only on existing lines. |
| inequality_orientation_gate | pass | Zero reversed inequality occurrences and no reversed name. |
| comments / identifiers | pass | Three-line docstring byte-identical, no proof comments lost. Every newly used theorem checked against actual imports below. |
| no-limit/no-scaffolding | pass | Source diff adds no options, count command, attributes, axioms or instances. |
| Whole project / LeanEval / external callers | owner gate | Not run by leaf. Owner takes source after release and performs independent compatibility/full build/separate LeanEval. No whole-project success claim here. |

Complete diagnostics warning inventory outside target: header L1; unusedSectionVars for
index_C_mul L204, index_le_card L232, index_rename L221, index_eq_weightedOrder_div L143,
index_neg L199, index_mul_left_weights L209, index_unique L242; unusedDecidableInType for
index_mul L165, index_neg L198, index_eq_weightedOrder_div L139, index_C_mul L203,
index_prod L181, index_rename L218 (both σ and τ), index_le_card L229,
index_mul_left_weights L208, index_unique L239; unused hr in index_le_card L232.
These pending owners' warnings were not hidden or suppressed. The exact raw messages
and positions are preserved in the complete native JSON artifact cited above.

New identifier hallucination check (actual compiled #check in recovery file, exit0):

| Identifier newly used in source | Verified type/source |
|---|---|
| Finsupp.weight_eq_sum | Weight.lean100; `[Semiring R] [AddCommMonoid M] [Module R M] [Fintype σ]`, gives weight w f=∑i,f i•w i. |
| Nat.cast_div_charZero | Cast/Field.lean41; `[DivisionSemiring K] [CharZero K]`, takes n∣m, gives cast(m/n)=cast m/cast n. |
| mul_div_assoc | Actual #check `[DivInvMonoid G]`, a*b/c=a*(b/c). Used reversed. |
| div_right_comm | Algebra/Group/Basic.lean549; actual #check `[DivisionCommMonoid α]`, a/b/c=a/c/b. |
| mul_div_cancel_right₀ | Actual #check `[MonoidWithZero M₀] [Div M₀] [MulDivCancelClass M₀]`, b≠0→a*b/b=a. |

## All 11 phase steps

- [x] Step1 references read.
- [x] Step2 all24 audit rows completed with concrete findings.
- [x] Step2.5 all five search methods actually attempted, unavailable remotes disclosed.
- [x] Step2.6 every binder and applicable weakening checked, literature included.
- [x] Step2.7 every signature line measured with codepoint arithmetic and actual width100 #check.
- [x] Step2.8 full inequality occurrence table and reversed-token scan.
- [x] Step3 all42 golfing rules given statuses, applicable alternatives tested.
- [x] Step4 strategy/clarity/helper/one-tactic reflection completed.
- [x] Step5a complete native diagnostics with target clean.
- [x] Step5b actual module build, independent original proof, original type recovery,
  actual signature/axioms, diff and anchored profile gates complete.
- [x] Step6a no target rename needed; unrelated existing rename queue left untouched.

## Source handoff

All native requests and all compiler processes completed before source release. Frozen
Index SHA256: `a57e50381e101099bf444b7e5feeb9af2e35d4f3908d8f21a7c93009e72b7374`.
Explicit SOURCE AUTHORITY RELEASED sent to owner; owner acknowledged and revoked source
permission. Thereafter this worker performed report writing only: no Lean request,
source edit or build. Git, shared owner state/logs, full-project verification and
publication remain with owner. No next declaration was touched.


## Owner checkpoint d12

Frozen SHA256 `a57e50381e101099bf444b7e5feeb9af2e35d4f3908d8f21a7c93009e72b7374`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session23587 exit0, `/private/tmp/roth-index-d12-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval33771 both exit0(152.33s/36.29s),
Index+Theta hashes stable; `/private/tmp/roth-index-d12-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index native LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/18other warnings; /private/tmp/roth-weight-div-native-final.json. Owner rg finds only2internal bridge uses; both accepted by module/full builds, no external caller to query.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
