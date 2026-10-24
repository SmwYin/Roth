# Independent helper audit: `exists_pos_div_rpow_lt_aux`

Status: PASS, helper-local only. This helper contributes no original-declaration count and
must be accepted and published jointly with its parent `isDiophantine_iff`. The parent and
remaining file declarations were not audited here. No Git, central progress, Main, root,
pin, definition, docstring, or other declaration edits were made.

## Scope, preparation, and genuine baseline

Read both skills and both cleanup commands in full, and all nine required references:
golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates,
style-rules, naming-conventions, profiling, and pr-feedback-examples. In particular:
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.

Before any helper Lean/golf action, independently saved the author's genuine first
ungolfed source and the live entry file under `/private/tmp/roth-eval-finite-helper/`:

| Snapshot | Bytes | SHA256 |
|---|---:|---|
| `first-ungolfed.lean` | 1338 | `6a0fa884b07d2f4b65ae25833e4824a9c6f86b87d034ea094632f4e2b5a715bf` |
| `entry.lean` | 3399 | `4d6a3d7eda1ea16c17a161c4e41c7dcb36d3e22077129c2753fb820f41d961ba` |

Actual helper declaration payloads in those two snapshots compare byte-for-byte equal.
Baseline unfiltered LSP: success, partial=false, no diagnostics. The unchanged-source
readiness native check and previously accepted broad baseline supplied by the owner are
reused; there was no cache fetch or redundant baseline broad run. No helper-local linter
warning was present. Existing upstream copyright/linter warnings are outside this scope.

The helper proves a single coherent positive-bound existence fact. On the finite exceptional
set, the positive error times the positive denominator power has a positive minimum after
inserting `(0,1)` to ensure nonemptiness. Half this minimum and `1/2` provide one uniform
constant. Outside the exceptional set the scaled error is at least one. This reasoning
works for arbitrary real `κ`; it does not require positivity of `κ`.

## Full 24-item audit

| Item | Concrete finding and action |
|---|---|
| 1 LINT | Initial and final complete unfiltered live diagnostics contain zero items. |
| 2 HAVE | `haq`: explicit use zero, implicit use in the rpow positivity proof, keep substantive `by` proof. `hfa`: one explicit use in `half_lt_self` plus implicit use in witness `positivity`, keep. `hq'`: two explicit uses, in `div_lt_iff₀` and `lt_div_iff₀`, keep. No single-use trivial have remains. |
| 3 SET_OPTION | None in the declaration; no resource limit was changed. |
| 4 SIMP | One terminal `simpa using hx.ne_rational`; retain unsqueezed. No nonterminal bare simp or terminal simp-only. |
| 5 NAMING | Descriptive snake case, mathematical `exists_pos_div_rpow_lt`, private `_aux`, no numbered/forbidden name pattern; no rename needed. |
| 6 LINE PACKING | All three signature lines measured below. No underpacked semantic unit fits. |
| 7 BY | `:= by` at end of signature; inner `by` attached to preceding expression. |
| 8 FORMAT | Two-space proof indentation, no blank body lines, no haveI/letI, no sequential rewrites to merge. |
| 9 COMMENTS | No comments existed inside the helper; zero removed or relocated. |
| 10 DOCSTRING | Private helper correctly has no docstring. Other docs untouched. |
| 11 VISIBILITY | Private, sole production caller is the parent equivalence in this file. |
| 12 STRUCTURE | 20 declaration lines; 18 proof-boundary/body lines including the `:= by` line, 17 tactic/body lines; each membership branch is two lines. The positivity conjunction belongs to the same existential witness, so no artificial splitting. |
| 13 MATHLIB | Five-method search and compiled exact?/apply? probe below; retain substantive number-theoretic finite-exception argument using `Set.exists_min_image`. |
| 14 JUNK DEF | n/a: theorem, no new definition. Local f avoids repeated large expressions. |
| 15 EXISTS LEMMA | Not a trivial witness/rfl wrapper: finite minimum, irrationality, lifting and exceptional-set case split are substantive. |
| 16 SHOW/CHANGE | n/a: neither appears. |
| 17 PUSH_NEG | n/a: none. |
| 18 GENERALISE | All four bound variables/hypotheses audited below; retain accepted arbitrary-real exponent formulation. |
| 19 INEQUALITY | Three signature inequalities, all `<`; no reversed symbol or target-name ge/gt pattern. |
| 20 NORMAL-FORM | Standard `Set.Finite`, `Irrational`, absolute rational error, and real rpow. Division form matches the parent's exact predicate. |
| 21 SYNTAX-GEN | Existential C bundles its positivity and uniform bound for direct application. No easier required call form identified. |
| 22 IMPORT-FANOUT | n/a: no imports added or changed. |
| 23 CASTS | Zero dropped; five cross-type casts retained: signature p/q to real, body a.1/a.2 to real, and q to real in hq'. Numeric `(1 : ℝ)` retained to fix the scalar comparison. No cast introduced by the sole edit. |
| 24 INSTANCE-NAME | n/a: no instance declaration. |

## Line packing and inequalities

Actual TYPE was inspected with `format.width=100`, and live hover confirms the same
signature. The width query also checked `expandLemma : Macro`. Its standalone query line
had an unrelated long-line warning; production diagnostics are clean.

```
∀ {x κ : ℝ}, Irrational x → (Roth.approxSet x κ).Finite →
  ∃ C, 0 < C ∧ ∀ (p q : ℤ), 0 < q → C / ↑q ^ κ < |x - ↑p / ↑q|
```

| Signature line | Codepoints | Next complete semantic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 17 | 70 | `(hs : (Roth.approxSet x κ).Finite)` (34) | 70+1+34=105 | ok |
| 18 | 40 | Complete existential conclusion through `:= by` (79 without indentation) | 40+1+79=120 | ok |
| 19 | 83 | No next signature line | n/a | ok |

The initial suggestion that the first break could be repacked was withdrawn immediately
after actual measurement; no speculative signature edit was made.

| Occurrence | Location | Actual form | Action |
|---|---|---|---|
| 1 | C property, line 19 | `0 < C` | retain |
| 2 | denominator hypothesis, line 19 | `0 < q` | retain |
| 3 | approximation bound, line 19 | `C / ... < abs ...` | retain |
| reversed ≥/> | whole signature | none | no rewrite/rename |

Body inequalities also use smaller-left orientation. The tactic separator `<;>` is syntax,
not an inequality. No imported lemma was renamed.

## Five-method mathlib search

| Method | Actual query/result |
|---|---|
| A Lean-Finder | `finite set of positive real numbers has a positive uniform lower bound`; returned finite-set einfsep facts, not this weighted approximation statement. |
| B Loogle | `Set.Finite, ∃ ε, 0 < ε ∧ _`; zero hits. |
| C LeanSearch | `finite set positive function has positive lower bound`; returned `Set.Finite.bddBelow`, `Finset.le_inf`, `Finite.bddBelow_range`, all partial order-theoretic ingredients. |
| D source search | Finite-set/order bounds, exists/positive/lt/le, and the full helper name; no same weighted approximation declaration. Standard finite/Finset minimum files inspected. |
| E name pattern | `exists_min_image`; found and verified `Set.exists_min_image`, with Finset/Multiset/Northcott variants. Index was warming, so no absence claim relies on this index alone. |

Auxiliary variants: minimum-image, finite bddBelow/image, Finset inf/min forms. Common
equivalents: finite-set minimum is the partial match already used; no custom compactness,
bornology, isolation, or typeclass predicate is introduced. All six strict replacement
rules were considered: no 1–3-call wrapper, exhaustive presence search plus actual compiled
probe, auxiliary variants, standard predicates, no duplicate to delete, and no module
docstring churn for a private helper. There is no API-extraction plumbing signal requiring
a new public helper.

At the actual initial live goal, bounded `grind`, `simp`, `aesop`, and `exact?` failed.
`apply?` returned only incomplete existential/logic wrappers. Its empty goals array was
explicitly rejected as completion evidence because its diagnostics described remaining
subgoals. The accepted proof is separately compiled and its opaque VALUE is checked below.

## Generalisation and inversion

| Binder | Classification/use | Drop/weakening evidence | Resolution |
|---|---|---|---|
| `{x : ℝ}` | Concrete value; irrationality and error expression | Removing x cannot preserve the same well-scoped statement. Field abstraction changes the fixed real-rpow/approxSet API. | Retain; no mechanical candidate. |
| `{κ : ℝ}` | Arbitrary exponent used in approxSet and rpow | Removing κ cannot preserve the statement; already arbitrary real, no ε positivity restriction. | Retain accepted generality. |
| `hx : Irrational x` | Proposition, `hx.ne_rational` establishes nonzero error | Actual minimal-hypotheses drop probe fails at line26: unknown hx.ne_rational; caller mismatch also observed. No class parent/strict-to-weak candidate applies. | Retain. |
| `hs : ...Finite` | Proposition, finite minimum selection via hs.insert | Actual drop probe fails at line21: unknown hs.insert, then lost ha.1 type and caller mismatch. Boundedness alone is not a mechanical replacement for finite minimum selection. | Retain. |

The drop tool skips the grouped implicit binder; x and κ were separately inspected as
above. Point-localisation, decidability and universe weakening are n/a: no abstract
structure/typeclass/universe parameter or function regularity hypothesis occurs.

Mathematically, finite approxSet also forces irrationality because exact rational
multiples would give infinitely many approximations. Deriving that implication would
add a substantial optional argument/API; the owner explicitly directed retaining hx
under the user's minimal-sufficient-evidence/no-optional-expansion instruction. This is
not unfinished required work. No binder or conclusion was weakened.

Inversion check: `Roth.approxSet` occurs in minimum setup through hs, membership splitting,
and the outside-set contradiction. Irrationality and weighted denominator structure are
used throughout the bound construction. This is not a concrete object unfolded once and
then forgotten. A generic finite positive-function theorem is an ingredient, not grounds
to proliferate helpers here. Literature search: n/a, private helper.

## All 42 golfing rules

| Rule | Status/evidence |
|---|---|
| 1.1 by-exact wrapper | n/a: no declaration wrapper. |
| 1.2 by-rfl | n/a: none. |
| 1.3 rw+exact | n/a: rw is followed by a genuine case split. |
| 1.4 simp+exact | Already terminal simpa at irrationality step; no redundant pair. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor fields | Witness and conjunction already use anonymous constructor. |
| 1.7 apply+exact | Outside-set branch considered; composing the long typed scalar comparison and contradiction adds nesting/wrapping with no line or speed benefit. Retain the two explicit lines under the minimum-value filter. |
| 1.8 by_contra+push | n/a: neither. |
| 1.9 eta | f's lambda uses both projections; bound lambda constructs the proof, not eta. |
| 1.10 have inline | All three haves retained for substantive proof or multiple explicit/implicit uses, as counted. |
| 1.11 apply+intro | Already bound witness uses `fun p q hq ↦`; no such pair. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | Minimum witness already destructured by obtain. |
| 1.14 consecutive rw | n/a: one rw with both rewrites. |
| 1.15 terminal simp-only | n/a: none. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | hs.insert, hx.ne_rational and transitive estimates already use it. |
| 1.18 trailing parentheses | Considered; nested inequalities need grouped term arguments, no cosmetic churn. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial exists helper | n/a: substantive finite-set argument, not witness/rfl. |
| 2.1 whole grind | Actual live attempt fails with remaining contradiction goal. |
| 2.2 pre-grind deletion | n/a: no retained grind. |
| 2.3 simpa consolidation | Existing irrationality conversion already consolidated. |
| 2.4 fun_prop | n/a: no regularity goal. |
| 2.5 positivity | Already used for positive denominator/min witness; retains haq and hfa implicit dependencies. |
| 2.6 gcongr | n/a: no missing congruence step; the hard inequality is the finite minimum bound. |
| 2.7 lia/omega | n/a: no linear Nat/Int arithmetic chain; q positivity crosses types via exact_mod_cast. |
| 2.8 aesop | Actual whole-goal attempt fails, makes no progress. |
| 2.9 norm_num/norm_cast | Existing norm_num handles dummy denominator and scalar half; exact_mod_cast handles genuine integer/natural/real bridges. |
| 2.10 decide | n/a: not a closed finite-computation proposition. No native_decide. |
| 2.11 field_simp/ring | n/a: no rational-function identity; division conversion already uses div_lt_iff₀. |
| 2.12 linear_combination | n/a: no ring/ring_nf close with contextual identities. |
| 2.13 wlog | n/a: membership and nonmembership branches are mathematically asymmetric. |
| 2.14 two-step calc | Already trans_lt/trans_le terms; no calc. |
| 2.15 parallel goals | Existing rcases/first/<;> closes the dummy and exceptional denominator cases. |
| 3.1 erw | n/a: none. |
| 3.2 legacy regularity | n/a: none. |
| 3.3 omega→lia | n/a: neither. |
| 3.4 rcases rfl | Dummy membership branch already substitutes rfl without extra rewrite. |
| 3.5 automation attributes | n/a: private existential helper, no canonical rewrite/regularity registration. |
| 3.6 simp_all-only | n/a: none. |
| 3.7 maxHeartbeats | None present or added. |

Step-back review found the genuine performance defect: `hmin _` lets expected-type
propagation unfold the weighted absolute-error function before learning its pair argument.
Supplying `(p,q)` removes this unification search. Term mode, automation, and a different
finite-induction strategy do not replace this concise minimum proof with a better API.
No helper proliferation or one-line cosmetic churn was performed.

## Semantic verification and independent proof

Artifacts live in `/private/tmp/roth-eval-finite-helper/`. Actual enumeration before guards
found exactly one target-family constant, with universe parameters `[]`; no guessed suffix
count was used. Exact-source derivative name was `_private._stdin.0...exists_pos_div_rpow_lt_aux`.
The production imported name, separately enumerated and guarded after module refresh, is
`_private.Roth.LeanEval.0.LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux`.

`Guard.lean` uses a strict recursive comparator covering every Expr constructor, Name
component, BinderInfo, Level constructor/list, literal, and metadata/Syntax constructor.
The captured complete raw TYPE (4943 bytes) is also compared byte-for-byte. No hygiene
normalisation or equality exception was necessary. Universe list is checked as raw `[]`.

The genuinely independent `Independent.lean` proves the same statement by finite-set
induction: empty-set bound, insertion via min of the previous bound and half the new
positive scaled error, then separate exceptional/nonexceptional global estimates. It
does not invoke the target, its generated family, the parent, or any caller. Its native
compile exited0 in27.030s. Guarded TYPE is strictly/raw identical to the derivative
target TYPE. The independent and derivative target opaque VALUES were inferred together
in one run_cmd under the shared default 200000 heartbeat ceiling, not separately relaxed
ceilings; that stronger shared-budget check passed in48.406s.

After the sole repair, `LiveGuard.lean` imports the actual freshly built production module,
enumerates its singleton family, and independently infers the production opaque VALUE.
It passed in52.797s. Both guards verify actual `value! true`, inferred VALUE type, no
MVar/levelMVar/FVar/loose variables/sorry, defaults200000/20000/512, and only
`propext`, `Classical.choice`, `Quot.sound`. Direct dependencies are upstream imported
constants and exclude self, the entire target family, and both caller name families;
there is no same-LeanEval-module dependency. No circular alias or caller route is used.
Imported upstream acyclic/kernel-checked closure is reused rather than reproved broadly.

| Actual opaque object | VALUE bytes | VALUE hash | Direct dependencies |
|---|---:|---|---:|
| Original derivative target | 418526 | 1815957749928358977 | 233 |
| Independent induction proof | 598674 | 8190617364705215684 | 229 |
| Repaired production target | 418547 | 4772344139078824193 | 233 |

These are actual serialization hash/length receipts, not a claim of full raw VALUE identity
across module contexts. The independent VALUE inference is valid unchanged evidence and
was not replayed. The caller source and all other declaration payloads are byte-identical
to entry; the entire current module also passes compilation.

Two earlier scratch guard harnesses failed before semantic checking (missing reopened
Real scope; nonexistent Name.fromString constructor). They were corrected with explicit
recursive Name.str terms and actual family lookup. No production change or failed semantic
row was hidden. A live multi-attempt fragment also retained an old continuation line and
was rejected; actual source compilation and opaque VALUE checks establish the accepted fix.

## Performance, complete accounting, and capture lifecycle

Exact command for each captured source: `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 <source>`. Separate stdout/stderr retained. Genuine first
ungolfed source and final-prefix source have different preceding contexts, so no controlled
ratio between those contexts is claimed. Old final and its mandatory repeat use the exact
same unchanged Prefix source. Repaired Prefix is the exact live source through this helper.

Every capture had explicit owner HOLDACK before preparation, observation/environment/freeze
work; owner remained idle through actual compiler/driver-group drain. Only raw hashes and
lengths were observed until an explicit owner RELEASE allowed parsing. Full actual parent
and lake env bytes were compared in memory before/after each freeze; only hash/length and
safe PATH were persisted, no secret environment or unrelated process arguments. Each
43-input freeze stayed equal. Launch/terminal/drain JSON artifacts contain actual times,
PIDs/PGIDs and separate raw-stream bindings.

| Capture | Task PID/PGID | Driver PID/PGID | Exit / wall seconds | Drain |
|---|---:|---:|---|---|
| baseline | 44103 | 44081 | 0 / 101.576 | both groups absent |
| old final | 44137 | 44081 | 0 / 102.738 | both groups absent |
| mandatory unchanged repeat | 44267 | 44246 | 0 / 100.256 | both groups absent |
| repaired final | 44623 | 44602 | 0 / 29.061 | both groups absent |

Full actual command and disjoint target timing (milliseconds):

| Capture | Source lemma wrapper | Async proof | Kernel parent | Lint parent | Detached Meta.whnf roots | Conservative total | Result |
|---|---:|---:|---:|---:|---|---:|---|
| genuine baseline | 45.853 | 2015.240 | 175.523 | 27.589 | 877 / 1.007ms | 2265.212 | FAIL |
| old final | 10.622 | 2035.069 | 217.039 | 25.792 | 875 / 0.941ms | 2289.463 | FAIL |
| unchanged repeat | 13.242 | 2066.110 | 201.518 | 32.180 | 875 / 0.951ms | 2314.001 | FAIL |
| repaired final | 9.917 | 254.736 | 8.816 | 17.202 | 887 / 0.926ms | 291.597 | PASS |

The final target is below750ms, so no further unchanged repeat was run. Old failing rows
are preserved. The target has no compiler root; compilation of the preceding definition
is a separate declaration. Actual kernel child times are10.555/9.290/12.283/8.759ms,
reported separately and not added to their parents. No target lazy Kernel DATA declaration
exists: complete actual traces have zero DATA tokens and the target Kernel family is a
singleton. Detached roots were exhaustively classified as Meta.whnf, not mislabeled DATA.

The expanded private-theorem command is nested semantically within the private-lemma
wrapper despite earlier trace flushing. Its time is not added again. Complete expanded
and original command payloads were retained and compared under the sole lemma→theorem
token substitution. The actual implementation is root `expandLemma` in
`Mathlib/Tactic/Lemma.lean`, verified by source, local search and #check: it modifies that
atom and syntax kinds while preserving the full declaration structure. `timing.json`
binds complete expanded payloads and the macro implementation hash/length. All disjoint
outer/async/kernel/compiler/lint roots and conservative detached roots are accounted for;
no nested sums are used.

Root cause is the measured Meta.isDefEq explosion in `hmin _` (about1791ms in the old
final trace). Giving the already known pair explicitly is the only production edit.
No limits, native_decide, count_heartbeats, scaffolding, new axioms or weaker conclusions.

## Final gates and handoff

| Gate | Actual evidence |
|---|---|
| module refresh for production guard | `lake build Roth.LeanEval`, exit0,30.963s |
| final ordered full build | `lake build`, exit0,3.172s |
| final separate Eval build | `lake build Roth.LeanEval`, exit0,3.092s, after full build |
| final native source | `lake env lean Roth/LeanEval.lean`, exit0,27.584s, no output |
| final LSP | complete unfiltered success, partial=false, zero diagnostics |
| definition protected | no definition/doc/import/other declaration changes |
| theorem statement protected | helper signature exact bytes and strict/raw actual TYPE unchanged |
| structure | 18 proof-boundary/body lines, two-line branches, coherent same-witness conjunction |
| naming | private descriptive snake_case `_aux`, no queue entries |
| packing/orientation | full tables above; no reversed inequalities |
| no unintended caller breakage | exact single-edit whole-file comparison plus current module/native build |
| semantics | independent strategy and freshly imported production VALUE/TYPE guards pass |
| performance | repaired conservative complete total291.597ms |

Build logs replay existing warnings in upstream files, including copyright and unused
variables/Fintype hypotheses. There are no new target/LeanEval diagnostics; upstream files
were not reopened for fixes. File-wide phase0/1/2/3/5/6/6.5 responsibility remains with the
file owner; this report supplies this helper's complete Phase4 and performance pass.
No copyright/license identity was invented. No rename or non-rename refactoring is pending.

Built-in simplify is unavailable, so no invocation is claimed. This fresh substantive
independent audit reviewed reuse, structure, hypotheses and efficiency and repaired the
measured unification defect. Fresh independent file-final review remains the owner's
later required step, not an additional helper-local obligation.

Phase4 checklist: references ✓; 24-item audit ✓; five searches/probes ✓; binder and inversion
audit ✓; width table ✓; inequality table ✓; all42 rules ✓; step-back review ✓; diagnostics ✓;
diff/build/semantic/performance gates ✓; rename queue n/a (none) ✓. All required local work
complete. Declaration20→20 lines, proof18→18 lines; source+5 bytes, with substantial measured
speed improvement. No helper added; original count unchanged.

Final `Roth/LeanEval.lean`:3404 bytes,
SHA256 `b682d05b7faa24c0ac24d61d7fc36af71d79422c7ff9993c139a171a4e827c26`.
The full file equals entry with exactly `hmin _` replaced by `hmin (p, q)` at line34.
All helpers/guards/profiles are scratch artifacts outside production. See FINAL-END.json
in the scratch directory for actual final drain/release receipt.
