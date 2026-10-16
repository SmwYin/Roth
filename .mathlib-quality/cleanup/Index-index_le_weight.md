# Phase 4 — Roth.index_le_weight

Scope: single declaration in `Roth/Index.lean`, entry lines 62–65, final lines
63–66; branch `ramin-cleanup`, entry HEAD `a51a6b1`. Only the target and this
report were edited. The user explicitly approved removing this theorem's unused
`[DecidableEq σ]`. The sole source edit is `omit [DecidableEq σ] in` immediately
before its existing docstring. Mathematical arguments, name, universes,
conclusion, docstring and proof body are unchanged. No helpers or imports added.

Source editing released after every Lean request completed, at SHA256
`2bf2b502f4e95caf1b28cdc247ccd4a26cc9f1c60c747d8e7c388cf9035234cb`.
All subsequent work by this worker is report writing only. The owner may now
continue the sequential declaration pass. File length at release: 268 lines.

## Step 1 — References and mathematics

Read both lean4 and mathlib-quality SKILL.md files; the complete 1,847-line
cleanup.md command including the Phase-4 worker contract; full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns and cleanup-gates;
relevant style-rules sections on formatting, declarations, comments/docs,
inequalities, API, hypotheses and generality; naming-conventions. Also read
buzz.md and profiling.md. No subagents dispatched by this worker.

Mathematical argument: nonvanishing of a Hasse derivative means its exponent
belongs to the Taylor polynomial's support. Its weight therefore belongs to
the finite image defining the index. The infimum of that bounded-below finite
image is at most this member. Neither decidable equality nor positivity of
the weights is needed; finiteness of the variable type is required by the
existing definition of `weight` and `index`.

## Step 2 — Full audit, 24 items

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Entry complete native LSP reported unused-section-variable and unused-decidability warnings for this target. Applied approved omission. Final complete LSP: success=true, partial=false, timed_out=false, failed_dependencies=[]; zero target warnings. 26 remaining warnings concern the header/other declarations. |
| 2 | HAVE SCAN | n/a: zero have/let expressions in this two-line term proof. |
| 3 | SET_OPTION | n/a: no target override, debug option or limit raise. |
| 4 | SIMP SQUEEZE | n/a: no simp in retained proof. Standalone simp test fails without progress. |
| 5 | NAMING | PASS: index_le_weight states the inequality's operands in order, uses snake_case, and contains no forbidden abbreviation, numbering scheme or single-letter public name. No rename required or queued. |
| 6 | LINE PACKING | PASS: both signature lines measured in codepoints; table below. |
| 7 | BY PLACEMENT | n/a: retained proof is a term, no by token. |
| 8 | FORMAT | PASS: flush-left declaration, four-space signature continuation, two-space proof indentation; no empty internal line, tactic chain, haveI or letI. |
| 9 | COMMENTS | All three existing docstring lines preserved byte-for-byte; zero inline proof comments existed. |
| 10 | DOCSTRING | Public theorem has its mathematical meaning and source citation. Preserved under Rule A and explicit scope constraints. |
| 11 | VISIBILITY | Keep public: meaningful index API, used internally five times and externally by Roth/Main.lean:493 at entry. |
| 12 | STRUCTURE | Two-line term body; no conjunction, case split or long branch; no extraction or decomposition flag needed. |
| 13 | MATHLIB | Five actual methods ran; partial generic/order and weighted-power-series matches found. Retain project-specific index API on those primitives. Details below. |
| 14 | JUNK DEF | n/a: theorem, not a data definition. |
| 15 | EXISTS LEMMA | n/a: public inequality, not a private single-use existential witness. |
| 16 | SHOW vs CHANGE | n/a: retained proof has neither. |
| 17 | PUSH_NEG | n/a: none. |
| 18 | GENERALISE | Every binder drop-tested in native isolated snippets; DecidableEq omission independently proved, approved and applied. No other API change; table below. |
| 19 | INEQUALITY | PASS: only ≤ in signature, no ≥ or >; scan below. |
| 20 | NORMAL-FORM | Already index ≤ weight, with support membership translated through the existing Taylor API. weightedOrder has natural weights and ℕ∞ codomain; replacing this interface requires rescaling and nonzero/positive-weight hypotheses. |
| 21 | SYNTAX-GEN | The derivative nonvanishing hypothesis matches existing callers. Coefficient/support variants are intermediate existing APIs, not an easier replacement for those callers. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | Diff: 0 dropped / 0 kept cross-type / 0 kept load-bearing. Sole added line contains no cast. |
| 24 | INSTANCE-NAME | n/a: theorem introduces no instance declaration or instance name. |

Issues found: one unused instance producing two diagnostics; fixed by one scoped
omission. No cross-declaration edits. Existing warnings on other declarations
are owned by their later workers, not treated as clean here.

## Step 2.5 — Five-method mathlib search

All queries were real native tool calls with bounded results. None failed.

| Method | Actual query | Observed results |
|---|---|---|
| A Lean-Finder | `index of multivariate polynomial at a point at most weight of a nonzero Hasse derivative`, 3 results | MvPowerSeries.weightedOrder_le; MvPolynomial.le_weightedTotalDegree; ChevalleyThm.MvPolynomialC.degBound. |
| B Loogle | `sInf ?s ≤ ?a`, 5 results | sInf_le, sInf_le_sInf, sInf_le_of_le, sInf_le_iff, sInf_le_iff_forall_lt. Complete-lattice results require adaptation for real conditional completeness. |
| C LeanSearch | `infimum of finite set is less than or equal to every member`, 3 results | Finset.inf_le_of_le, Finite.ciInf_le, Finset.inf'_le. |
| D source rg | Full-name index_le_weight across mathlib; csInf_le variants in ConditionallyCompleteLattice/Basic; weightedOrder_le in MvPowerSeries/Order; Taylor coefficient source | No full-name index_le_weight text hit; positive source hits for csInf_le (generated by to_dual), csInf_le_of_le, csInf_le', weightedOrder_le. Project coeff_taylor is Roth/Taylor.lean:128. An initial guessed Mathlib Taylor path did not exist; corrected search located the actual project API. |
| E local name search | `csInf_le`, limit 10 | Positive hits csInf_le', DirectedOn.csInf_le_csSup, csInf_le_csSup, csInf_le_csInf', csInf_le_csSup_of_nonempty_inter. Index status unavailable: positive source hits remain useful; empty output would not establish absence. |

Auxiliary variants examined: `_of_le`, `_of_nonempty_inter`, `_le`, `_left`,
`_right`, `_eq_top_iff` by candidate/source inspection. Common-equivalents
lookup: no discrete, separation, bornology or finiteness-wrapper replacement
for the domain-specific index statement. The finite-set lower-boundedness
primitive is already used directly.

Conclusion: **partial matches**, chiefly `csInf_le` and
`MvPowerSeries.weightedOrder_le`. The retained theorem ties the project's index
and weight to nonvanishing derivatives. Its public interface is protected;
there is no verified equivalent with that exact project-specific statement.
No declaration is added, and no claim of exhaustive absence is made. The
untruncated full-name rg was performed; generic-route exact?/apply? tests below
did not provide a non-self complete replacement. The source proof already uses
mathlib csInf_le and finite-image boundedness directly, without a new wrapper.

## Step 2.6 — Generalisation status and actual probes

Tests used self-contained native lean_run_code snippets with `import Roth.Index`
and `set_option autoImplicit false`, avoiding transient edits to public source.
The independent proof below works without DecidableEq, and does not call the
target, le_index_iff, or its private support helper. Every failed drop test had
success=false, timed_out=false; the no-DecidableEq proof had success=true,
timed_out=false.

| # | Binder | Class/use | Mechanical candidates actually tested | Result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable, exponent/variable index | Drop with autoImplicit=false | Fails at snippet L4: unknown σ. Already universe polymorphic; no universe widening left. |
| 2 | `[Fintype σ]` | class, weight's sum and index signature | Drop; replace by `[Finite σ]` | Both fail at snippet L4–5: cannot synthesize Fintype σ. No weaker computational parent supplies the required instance. |
| 3 | `[DecidableEq σ]` | decidability, unused in mathematics | Drop in independent proof; live omission | Independent proof compiles; approved live omission compiles. Kept. |
| 4 | `{P : MvPolynomial σ ℝ}` | data, Taylor polynomial | Drop | Fails at snippet L4–5: unknown P. No property/class parent to weaken. Coefficient abstraction would change protected definitions. |
| 5 | `{α : σ → ℝ}` | data, evaluation/translation point | Drop | Fails at snippet L4–5: unknown α. No global continuity/differentiability hypothesis to localize. |
| 6 | `{r : σ → ℕ}` | data, weight denominators | Drop | Fails at snippet L4–5: unknown r. No positivity assumption is present to weaken. |
| 7 | `{d : σ →₀ ℕ}` | data, chosen supported exponent | Drop | Fails at snippet L4 and L6: unknown d. No propositional weakening applies. |
| 8 | `(h : eval α (hasseDeriv d P) ≠ 0)` | proposition, obtains support membership | Drop | Fails at snippet L6: assumption cannot prove derivative nonvanishing. No strict-order or bundled hypothesis occurs. Replacing nonzero by nonnegative would not supply membership; not a generalisation preserving this proof. |

Inversion check: after index unfolds, the core order fact is abstract csInf_le,
which already exists. No missing abstract theorem needs extraction. The Taylor
coefficient fact is the project's existing coeff_taylor, not recreated here.

### Public literature search

Actual WebSearch queries:
`Roth theorem polynomial index minimum weighted derivative generalization` and
`Takloo Bighash Yin Formalizing Roth theorem index polynomial`.
Top three returned hits per query:

| Query | Top three hits | Relevant finding |
|---|---|---|
| weighted derivative/generalization | [Min Ru, Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf); [Miller–Takloo-Bighash book record](https://books.google.com/books/about/An_Invitation_to_Modern_Number_Theory.html?id=IxDzVsrIyqEC); [Roth ICM 1958](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) | Min Ru and Roth formulate index as a minimum of normalized nonvanishing derivatives. The upper bound by any such weight follows from the minimum property. No decidable-equality assumption is mathematical. |
| named formalization | [Miller–Takloo-Bighash book record](https://books.google.com/books/about/An_Invitation_to_Modern_Number_Theory.html?hl=en&id=IxDzVsrIyqEC&output=html_text); [Roth ICM mirror](https://paperzz.com/doc/7033317/h---rl-h.); [Roth introduction](https://paperzz.com/doc/8504985/roth-s-theorem--an-introduction-to-diophantine-approximation) | No exact named formalization was established from these search hits; rely on checked local source for the project's formulation. Mirror snippets are discovery leads, not support for new claims. |

The primary Roth/Min Ru formulations agree with the current meaning. Inference:
the minimum bound does not require positivity separately once the real-weight
finite-image definition has been fixed. No additional public restatement is
proposed. Coefficient-semiring abstraction is already an owner-level optional
proposal from the index worker; this worker does not apply it or claim it checked.
ChatGPT math MCP: n/a — no such callable tool is available in ALL_TOOLS.

Big-change candidates introduced by this worker: none. No new user approval
request is needed; the single instance omission was explicitly approved.

## Step 2.7 — Line packing, every signature line

Fresh compiled `#check @Roth.index_le_weight` at `format.width 100`:

```lean
@index_le_weight : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ},
  (eval α) ((hasseDeriv d) P) ≠ 0 → index P α r ≤ weight r d
```

The pretty-printer does not wrap the indivisible binder group exactly at 100;
the source arithmetic is the gate. Both signature lines are unchanged.

| Sig line | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 63 | 83 | `(h : eval α (hasseDeriv d P) ≠ 0)` = 33 | 83 + 1 + 33 = 117 > 100 | ok |
| 64 | 67 | none; `:=` already included, proof follows | n/a; no further signature token | ok |

Omission line has 23 codepoints and precedes the unchanged docstring. No
signature continuation remains underpacked by a movable complete binder.

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | conclusion, L64 | `index P α r ≤ weight r d` | already ≤ | none |
| 2 | signature/hypotheses | no ≥ or > occurrences | n/a | no _ge_ or _gt_ name |

## Step 3 — Golfing rules, all 42

Native live lean_goal at the term proof returned no_goal_at_position. The
initial live multi_attempt supplied tactic names at a term position and
therefore returned unknown-identifier errors; these are not evidence that the
tactics fail mathematically. Correct isolated `:= by` probes were then run:
grind failed; simp made no progress; aesop left the inequality; exact? could
not close; gcongr made no progress. apply? emitted partial suggestions and a
sorry diagnostic, so its nominal success=true is explicitly rejected as an
incomplete proof. No scratch automation result was copied into source.

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: already term mode. |
| 1.2 by rfl | n/a: no reflexivity wrapper. |
| 1.3 rw + exact | n/a: no rewrite tactics. |
| 1.4 simp + exact | n/a: no simplification chain. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 constructor | n/a: scalar inequality, no constructor chain. |
| 1.7 apply + exact | n/a: source already composed csInf_le term. |
| 1.8 contradiction | n/a: no contradiction or negation push. |
| 1.9 eta reduction | n/a: no source lambda. |
| 1.10 single-use have | n/a: no have. |
| 1.11 apply + intro | n/a: neither occurs. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain | n/a: no projections from a named have. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: no simp only. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | Already uses finite_toSet.image, .bddBelow and .2. |
| 1.18 <\| | Existing parentheses delimit csInf_le's second argument and nested applications; no lambda/by trailing-parenthesis pattern. No clarity gain from changing it. |
| 1.19 push_neg | n/a: absent. |
| 1.20 existential inlining | n/a: not an existential lemma. |
| 2.1 grind | Actually tested standalone; fails to prove inequality. |
| 2.2 delete before grind | n/a: retained proof has no grind. |
| 2.3 simpa consolidation | n/a: no simp-plus-closing chain. |
| 2.4 fun_prop | n/a: no function regularity goal. |
| 2.5 positivity | n/a: target is comparison of index and arbitrary weight, not a zero/positivity goal derivable from structure. |
| 2.6 gcongr | Actually tested; no progress. |
| 2.7 lia/omega | n/a: real infimum/support fact, not Nat/Int arithmetic. |
| 2.8 aesop | Actually tested; exhausted search, inequality remains. |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric or cast calculation. |
| 2.10 decide | n/a: arbitrary real infimum comparison, no finite decision computation. |
| 2.11 field_simp/ring | n/a: no algebraic identity or denominator normalization. |
| 2.12 linear_combination | n/a: no terminal ring/ring_nf or polynomial identity. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc collapse | n/a: no calc; already direct order lemma. |
| 2.15 <;> | n/a: no repeated goals. |
| 3.1 erw | n/a: absent. |
| 3.2 continuity/measurability | n/a: absent. |
| 3.3 omega to lia | n/a: no arithmetic tactic in retained proof. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attribute | No new attribute: support-witness upper bound is a directed API application, not a canonical simplification rule. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 heartbeat override | n/a: no override to remove; none added. |

## Step 4 — Step back

Retain the direct finite-image csInf_le proof. Tested automation does not replace
it with a complete shorter proof. The independent proof uses the same abstract
minimum argument with an explicit image witness and public coefficient API;
it is useful verification, but adds tactic scaffolding to an already compact
term. No helper extraction, global attribute or adjacent-declaration change is
warranted. Only the approved unused-instance omission remains in the diff.

## Step 5a — Compiler, LSP and exact compatibility

Actual command `lake build Roth.Index` ran in this worker session, session
92257, and exited **0**: Built Roth.Index (16s), Build completed successfully
(1501 jobs). This is a module build, not a full-project build. Its existing
warnings correspond to later workers/header work. No target warning remains.

Complete native LSP on the actual file after edit: success=true,
partial=false, timed_out=false, failed_dependencies=[], 26 warnings, none in
the target docstring/statement/body range. Repeated complete diagnostics also
returned. Native run_code after the build retained an obsolete imported
signature and reported imports out of date; that stale probe failed and is not
used as compatibility evidence.

Fresh-process command:

```text
lake env lean /private/tmp/roth-index-le-weight-verify.lean
```

Session 54440 exited **0**, confirming the actual built no-DecidableEq signature,
standard axioms, exact original-type adapter and independent proof. The first
version used a long lambda with synthesized instance notation and hit the
default isDefEq heartbeat limit; the replacement below uses explicit
introductions and passes at unchanged default limits. No limit raise occurred.

The verification file contains:

```lean
import Roth.Index
open MvPolynomial Roth
universe u
set_option format.width 100 in
#check @Roth.index_le_weight
#print axioms Roth.index_le_weight
example : ∀ {σ : Type u} [Fintype σ] [DecidableEq σ] {P : MvPolynomial σ ℝ}
    {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ},
    eval α (hasseDeriv d P) ≠ 0 → index P α r ≤ weight r d := by
  intro σ inst _ P α r d h
  exact @Roth.index_le_weight σ inst P α r d h
example {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ}
    {d : σ →₀ ℕ} (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d := by
  apply csInf_le ((taylor α P).support.finite_toSet.image (weight r)).bddBelow
  exact ⟨d, mem_support_iff.2 (by rwa [coeff_taylor]), rfl⟩
```

Actual axiom output:
`'Roth.index_le_weight' depends on axioms: [propext, Classical.choice, Quot.sound]`.
The adapter recovers every original universe, type argument, Fintype and
DecidableEq argument, implicit data argument and hypothesis in their original
order. The old type was checked before editing and against the original
snapshot `/private/tmp/roth-index-original.lean`. The stronger independent proof
does not refer to the target itself or to a theorem derived from it.

## Step 5b — Diff gates

Actual source diff is a single added `omit [DecidableEq σ] in` line.
`git diff --check` exited 0. No definition or existing declaration line changed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual lake build Roth.Index, session 92257, exit 0. |
| definition_protected | PASS | No def/abbrev change. |
| theorem_statement_protected | PASS under explicit approval | Only approved unused DecidableEq removed from elaborated API; textual statement, universe, arguments and conclusion preserved; exact old type recovered by compiled adapter. |
| structure_gate | PASS | Two body lines, no conjunction or branches. |
| naming_gate | PASS | Descriptive snake_case, no forbidden patterns; no in-place rename. |
| line_packing_gate | PASS | Both signature rows measured, 83+1+33=117; final row includes conclusion and :=. |
| inequality_orientation_gate | PASS | Zero ≥/> in signature; one canonical ≤. |
| no-trust-downgrade | PASS | Built target reports exactly standard three axioms; no source sorry/new axiom. |
| no-limit/no-scaffolding | PASS | Source adds only omission, no options/profiling wrappers. |

Overall worker gates: **pass**. Whole-project build, external Main caller
verification, final anchored profile trace and separate LeanEval remain the
owner's file/project gates under the dispatch contract.

## Step 6 — Result and phase checklist

Before: 4 declaration code lines; after: 4; saved: 0. Including its new omission
command: +1 source line. Two target linter messages resolved. Rules applied:
approved mechanical generalisation (audit 18); no proof golfing change.
Renames queued: none. Helpers added: none. Comments removed: none.
Refactoring needed from this declaration: none.

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 audit items answered.
- [✓] Step 2.5 — all five actual search methods recorded.
- [✓] Step 2.6 — every binder probed, literature search and approval recorded.
- [✓] Step 2.7 — every signature line measured with arithmetic and width reference.
- [✓] Step 2.8 — inequality scan emitted.
- [✓] Step 3 — all 42 rules have concrete status.
- [✓] Step 4 — whole-proof alternatives tested and assessed.
- [✓] Step 5a — complete target-clean LSP, module build, fresh compiler checks.
- [✓] Step 5b — all worker diff gates passed.
- [✓] Step 6a — no rename required; queue untouched.

### Buzz status

No performance change claimed. Dedicated buzz/Skill invocation is unavailable
in this host; owner explicitly owns the final anchored `--profile` trace and
aggregate interpretation after workers freeze. This worker has read buzz.md
and profiling.md, introduced no heavy tactic and left no profiling scaffolding.
Do not interpret the module's 16-second build or scratch compiler time as a
per-declaration elaboration measurement. The owner must supply the final
performance status; this report makes no invented FAST-BOARD assertion.

## Owner checkpoint evidence

Frozen source unchanged2bf2b502f4e95caf1b28cdc247ccd4a26cc9f1c60c747d8e7c388cf9035234cb.
Fresh whole ORIGINAL nonself reproof and all18 original public type/value recoveries,
including an explicit one-instance eta adapter, pass in55805, exit0.
All19 actual retained declarations have only standard axioms; actual target type
additionally scanned with Lean.Expr.find? to reject any DecidableEq constant.
`/private/tmp/roth-index-d05-compatibility.log` also prints the actual no-DecEq signature.

Sequential owner full then separate LeanEval89783 both exit0(144.71s/36.17s),
Index+Theta hashes stable, `/private/tmp/roth-index-d05-{full,leaneval}.log`.
After builds, native external Main caller diagnostics complete in owner cell118:
success=true,partial=false,timed_out=false, zero errors/four inherited warnings;
JSON `/private/tmp/roth-index-d05-main-lsp.json`. Original block docs identical,
all source widths≤100. Exact-path publication precedes the next declaration edit.
