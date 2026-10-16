# Phase 4: `derivative_mem_kronSpan`

Fresh d15 audit of this declaration only. Start snapshot `/private/tmp/roth-d15-start.lean`;
original mathematical statement `/private/tmp/roth-genwronskian-baseline.lean`.
Final source SHA256 `ca4b042b39f51080139eda0a986c5be683cb78f101f22c14934351295817c39b`.
Source ownership was revoked after module/LSP success; subsequent work was report and scratch only.

## References and scope

Read both installed skills, the full worker contract, initial GenWronskian audit, and
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, relevant `style-rules.md`,
`naming-conventions.md`, and `mathlib-review-stages.md`.
Private literature exemption: n/a: private decl, literature search not required.
No Git actions, shared-log edits, full builds, LeanEval, imports, public declarations,
definition values, existing comments, or docstrings were changed by this worker.

## Full 24-item audit

1. **LINT:** no target-range warning. Complete final file diagnostics have exactly the five
   known outside warnings, reproduced below; no new warnings/errors.
2. **HAVE SCAN:** original generator `heq` (has `by`, used once) became the named derivative
   identity helper. Original scalar `heq` (has `by`, used once) was removed: direct `convert`
   against the sum-membership term proves precisely its needed equality. No final `have`.
3. **SET_OPTION:** none; no limits raised.
4. **SIMP SQUEEZE:** degree reduction is nonterminal `simp only [Set.mem_ofPred_eq, map_add,
   Finsupp.degree_single] at hd ⊢`; preserved exact explicit list. Zero, addition and scalar
   function equalities close with terminal unsqueezed `simp`. Generator identity's existing
   nonterminal explicit simp list moved verbatim to the helper.
5. **NAMING:** describes derivative membership in the named `kronSpan`; snake case with
   existing object identifier; none of the forbidden numeric patterns or abbreviations.
   New meaningful helper `derivative_kronHasse_aux`, private, no docstring, no numbered suffix.
6. **LINE PACKING:** all signature lines measured below; no repack row remains.
7. **BY PLACEMENT:** `by` remains at the end of the conclusion line.
8. **FORMAT:** two-space proof indentation, four-space signature continuation, no empty
   proof lines/trailing spaces, ordinary lambdas changed to `↦`; case arrows remain `=>`.
   No `haveI`/`letI`. No sequential rewrites to merge.
9. **COMMENTS:** none in the target; surrounding protected docs remain byte-identical.
10. **DOCSTRING:** private helper theorem needs none; none added. Existing private-definition
    docs outside the target preserved per session instructions.
11. **VISIBILITY:** target stays private. New identity helper private and before its user.
12. **STRUCTURE:** start 36 declaration lines / long generator case; final 27 declaration
    lines, 25 lines counting the `:= by` line, no conjunction, longest case under 10 lines.
    Extracted the chain-rule identity into 9-line `derivative_kronHasse_aux` (L145–153).
    All four span-induction cases retain their mathematical roles; no decompose deferral.
13. **MATHLIB:** actual five-method search and compiled generic-route probes below. Span
    induction and span monotonicity are used directly; no local monotonicity wrapper added.
14. **JUNK DEF:** n/a: theorem, not definition.
15. **EXISTS LEMMA:** n/a: conclusion is membership, not an existential witness wrapper.
16. **SHOW vs CHANGE:** no `show` in the target.
17. **PUSH_NEG:** none.
18. **GENERALISE:** every generated parameter audited below; no statement weakening applied.
19. **INEQUALITY:** table below; zero reversed inequalities in signature/hypotheses.
20. **NORMAL-FORM:** canonical submodule membership in the existing span; generator-set and
    span containment APIs used directly, no redundant equivalence formulation.
21. **SYNTAX-GEN:** OK: hF is already a direct membership hypothesis, and the bound is in the
    exact form consumed by the iterated-Hasse caller. A bundled derivation would change the
    representation and add API without simplifying this generator-specific fact.
22. **IMPORT-FANOUT:** n/a: no import change.
23. **CASTS:** 0 dropped / 2 kept genuine Nat→K and Fin→Nat coercions / 1 kept load-bearing
    Nat ascription in the extracted identity. `(K := K)` and `(σ := σ)` are named arguments,
    not casts. Target itself has no numeric coercion.
24. **INSTANCE-NAME:** n/a: no instance declaration introduced or changed.

Issues fixed: long generator case; repeated local function equality in scalar case;
ordinary lambda arrows; arithmetic automation where a direct monotonicity theorem suffices.
Refactoring needed: owner must give **new helper `derivative_kronHasse_aux` a fresh dedicated
Phase-4 audit before the next original declaration**. No original-declaration audit credit
is claimed for the helper here. No renames queued.

## Mathlib search-status

Native schemas were discovered through ALL_TOOLS. The native batch remained unresponsive
and was bounded/cancelled; direct MCP helper calls then actually executed all methods.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `derivation of submodule span Leibniz rule membership` | executed; DNS resolution error, not an absence result |
| B Loogle | `Polynomial.derivative (_ * _)` | executed; DNS resolution error |
| C LeanSearch | `derivation maps span into submodule if generators map into submodule` | executed; DNS resolution error |
| D source rg | `span_induction`, `degree_single`, `pderiv_hasseDeriv`, `derivative.*span`, `span.*derivative`; full exact target/helper names | span induction/degree API; Chebyshev-specific derivative-span lemmas; no full-name match |
| E local name search | `span_induction` | found `Submodule.span_induction`, Span/Defs; index unavailable, so no negative index claim |

Artifacts `/private/tmp/roth-d15-{finder,loogle,search,local}.json`.
Auxiliary variants considered: span monotonicity, scalar/add/sum membership, derivative
product rule, map-membership in span images. `Submodule.apply_mem_span_image_of_mem_span`
in Chebyshev uses a linear map; differentiation is not linear over the polynomial scalars
here, so scalar differentiation still needs the product rule.
Common-equivalents table: no match (none of the topology/finiteness/bornology buckets).

Conclusion: partial matches provide induction/membership/degree operations, already used
directly. No claim that external services proved global absence. The specialized theorem
is not a 1–3-call wrapper: its generator chain rule and Leibniz closure are essential.
All six strict rules considered: no new wrapper; full-name and generic probes performed;
auxiliary variants checked; no custom predicate replaces a typeclass; no equivalent found
requiring deletion; no module-doc mutation under existing-doc preservation authorization.

Compiled nonself probes use cloned private `kronHasse`/`kronSpan`, importing the built
module for public dependencies, **without access to this private target**:
`/private/tmp/roth-d15-{grind,simp,aesop,exactsearch,applysearch}.lean` and logs.
`grind` fails; `simp` makes no progress; `aesop` makes no progress; `exact?` cannot close;
`apply?` produces only partial suggestions and a diagnostic scratch sorry, not a proof.
That scratch is not an accepted proof artifact and was never copied into project source.
Native/direct multi-attempt calls also timed out at their bounded deadlines, so the
completed standalone probes provide the actual automation results.

## Generalisation status (every parameter)

| Parameter | Class | Drop/weakening candidates | Evidence/result |
|---|---|---|---|
| `{K : Type*}` | universe/type | drop, universe-polymorphism | Already independent universe; K occurs in both polynomial types and scalar ring. Removing its binder leaves K unbound; fixing K specializes rather than generalizes. |
| `[Field K]` | typeclass | drop; DivisionRing; CommRing; CommSemiring; CommRing+IsField | Generated `#check @kronSpan` and `#check @kronecker` explicitly require Field. The statement's existing named objects require that class before any proof starts. DivisionRing also lacks the commutative scalar structure required by MvPolynomial/algebra evaluation. CommRing/CommSemiring may support a redesigned ancestor chain, but cannot elaborate these unchanged existing objects; no assertion of mathematical field-necessity is made. CommRing+IsField is an API restatement with the same field content, not a useful inline weakening. |
| `{σ : Type*}` | universe/type | drop; universe-polymorphism | Already independent universe; occurs as the variables of the input polynomial/function and in the multiindex. Removing it leaves the dependent type unbound. |
| `[Fintype σ]` | finite/enumeration data | drop, Finite, point-localization | `#check @kronSpan` explicitly requires Fintype through the chosen Kronecker enumeration; `Fintype.equivFin σ` and the finite generator sum use its data. A Finite assumption does not preserve the existing chosen enumeration/definition value. No proof-failure-as-necessity argument. |
| `k : ℕ` | structure/index value | drop, implicitness, abstract ordered index | Occurs in hF and conclusion via the fixed substitution exponents k^j; dropping it leaves the statement unbound. Making it implicit is API reshuffling; abstract order discards the arithmetic defining these objects. |
| `μ : ℕ` | order/index value | drop, abstract ordered index, strict→weak | Controls Finsupp.degree bound in premise and its successor in conclusion. Drop leaves both unbound. Natural addition/degree are the mathematical content, not merely well-founded induction. No strict inequality hypothesis exists to weaken. |
| `{F : MvPolynomial σ K → Polynomial K}` | structure value | drop, point-localization, abstract codomain | Already arbitrary function; occurs in hypothesis and derivative. A pointwise result changes the membership conclusion, which concerns the whole operator. Drop leaves F unbound. |
| `(hF : F ∈ kronSpan k μ)` | proposition | drop, point-localization, strict→weak, unbundle | Compiled counterexample below proves dropping hF makes the assertion false. Membership is one unbundled proposition; no global analytic or strict hypothesis to localize/weaken. |

The ambient `l` section variable is absent from the elaborated signature; no unused
parameter was introduced. No decidability parameter; local `classical` suffices.

Actual independent drop-test counterexample:
`/private/tmp/roth-d15-generalisation.lean` compiles (exit 0). Over K=ℚ, σ=Unit,
k=2, μ=0, choose F to be the constant operator P↦X. Its derivative is the constant
operator P↦1. Every operator in kronSpan 2 1 vanishes on P=0 (proved independently by
span induction); the constant-one operator does not. Thus the no-hF form is false.

Inversion check: the proof uses the particular kronHasse generators, substitution chain
rule, degree increment, and inclusion of their bounds. It is not an object-free argument
after one unfolding. A general derivation/span theorem would need new Leibniz and generator
hypotheses; no inline equivalent abstraction removes that content. Broader coefficient-ring
support belongs to coordinated ancestor generalisation; no unverified public change made.
Private literature search: n/a by explicit private-declaration exemption.

## Line packing

Reference: `set_option format.width 100 in #check @derivative_mem_kronSpan_reproof`
in the compiled independent clone (`/private/tmp/roth-d15-reproof.log`):

```lean
@derivative_mem_kronSpan_reproof : ∀ {K : Type u_3} [inst : Field K] {σ : Type u_4}
  [inst_1 : Fintype σ] (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K},
  F ∈ kronSpan k μ → (fun P => Polynomial.derivative (F P)) ∈ kronSpan k (μ + 1)
```

Every target signature line, measured in codepoints. Natural next signature unit is the
complete hypothesis or conclusion, not a sliced lexical symbol.

| Sig line | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 155 | 85 | `(hF : F ∈ kronSpan k μ) :` (25) | 85+1+25=111 >100 | ok |
| 156 | 29 | full conclusion through `:= by` (82) | 29+1+82=112 >100 | ok |
| 157 | 86 | none; proof follows | n/a | ok |

No signature reflow needed. The ordinary lambda arrow changes notation only; exact original
type is independently asserted against the renamed nonself reproof in the scratch file.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| – | all signature lines/hypotheses | no `≥` or `>` | n/a | no `_ge_`/`_gt_` |

The generator's local `hd : d.degree ≤ μ` and output bound are already left-oriented.
Case `=>` arrows are syntax, not inequalities.

## Golfing-rule pass (all 42)

| Rule | Status and concrete reason |
|---|---|
| 1.1 | n/a: no by-exact wrapper |
| 1.2 | n/a: no by-rfl proof |
| 1.3 | n/a: generator rewrite precedes construction, not an immediately closing exact |
| 1.4 | tried zero/add simpa-only consolidation; explicit function-vs-Pi forms mismatch, retained convert/funext/simp |
| 1.5 | n/a: no trailing rfl after simp |
| 1.6 | n/a: no constructor/exact pair |
| 1.7 | n/a: no apply/exact pair |
| 1.8 | n/a: no contradiction/push-neg |
| 1.9 | inspected: derivative lambdas apply a map to F P and cannot eta-reduce to F; normalized arrows |
| 1.10 | no term-only have; scalar proof-bearing single-use heq eliminated with direct convert |
| 1.11 | n/a: no apply then intro |
| 1.12 | n/a: no show |
| 1.13 | n/a: no conjunction-valued have projections |
| 1.14 | n/a: no adjacent rewrites |
| 1.15 | terminal simp unsqueezed; remaining simp only calls are nonterminal |
| 1.16 | no nonterminal bare simp; explicit degree and helper lists preserved |
| 1.17 | applied zero_mem dot notation; other Submodule arguments need explicit target or inference |
| 1.18 | lambdas passed without parentheses; remaining parentheses group nested membership arguments |
| 1.19 | n/a: no push_neg |
| 1.20 | n/a: not a trivial existential helper |
| 2.1 | whole-proof grind actually tried in completed independent probe; failed |
| 2.2 | n/a: no final grind to simplify |
| 2.3 | zero/add direct simpa candidates tried and reverted after function/Pi mismatches |
| 2.4 | n/a: algebraic polynomial derivative, no analytic regularity predicate |
| 2.5 | n/a: no positivity/nonzero goal |
| 2.6 | degree monotonicity replaced by direct Nat.add_le_add_right; gcongr adds no value over exact API |
| 2.7 | direct Nat.add_le_add_right hd 1 eliminates arithmetic tactic entirely |
| 2.8 | whole-proof aesop actually tried; no progress |
| 2.9 | n/a: no concrete numeric/cast goal in target; generator scalar casting is structural |
| 2.10 | n/a: membership in a symbolic span over arbitrary fields is not closed decidable computation |
| 2.11 | n/a: no denominator identity |
| 2.12 | ring step moved unchanged into generator helper; its identity is unconditional algebra, no useful equality hypothesis to combine (outer hF only membership) |
| 2.13 | n/a: four span constructors are distinct, not symmetric branches |
| 2.14 | n/a: no calc |
| 2.15 | n/a: no duplicated parallel goals with a common closing tactic |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no continuity/measurability tactics |
| 3.3 | applied: omega removed in favor of direct bound API (stronger than replacing with lia) |
| 3.4 | preserved obtain ⟨d, hd, rfl⟩ substitution; no redundant equality simplification |
| 3.5 | no attributes: private specialization and one helper user, unsuitable global simplification rules |
| 3.6 | n/a: no simp_all only |
| 3.7 | n/a: no heartbeat/depth overrides |

## Step back

The membership statement is a Leibniz closure argument over Polynomial K, not a linear-map
image argument over that scalar ring. Compiled `grind`, `simp`, `aesop`, `exact?`, `apply?`
probes do not close it. The meaningful generator identity extraction removes the long branch;
rewriting the scalar function equality directly against the membership term removes its
single-use have. A separate linearity/derivation representation would add structure without
shortening the independent generator obligation. No further decomposition is required.

## Verification and gates

- `lake build Roth.GenWronskian`, final session31828, exit 0;
  `/private/tmp/roth-d15-module.log`, 1838 jobs.
- Full final LSP `/private/tmp/roth-d15-lsp.json`: success=true, partial=false,
  timed_out=false, failed_dependencies=[], zero errors, exactly five known outside warnings.
- Independently cloned exact original private type, no use of the target theorem:
  `/private/tmp/roth-d15-reproof.lean`, exit 0, log of same stem. Its concluding `example`
  uses the exact baseline signature and the newly proved renamed clone.
- Both cloned proof and new helper depend only on propext, Classical.choice, Quot.sound.
- Actual built private target and helper axioms independently printed by environment-name
  lookup: `/private/tmp/roth-d15-axioms.lean`, exit0, corresponding `.log`; both use
  exactly propext, Classical.choice, Quot.sound.
- Worker diff is `/private/tmp/roth-d15.diff`, captured against start snapshot without Git.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module invocation, exit0 |
| definition_protected | pass | no def/abbrev values/signatures changed |
| theorem_statement_protected | pass | original type independently checked; only equivalent lambda notation changed |
| structure_gate | pass | target 27 declaration lines, longest case <10, no ∧; new 9-line identity helper |
| naming_gate | pass | descriptive target and helper; no forbidden patterns/abbreviations |
| line_packing_gate | pass | complete measured signature table above |
| inequality_orientation_gate | pass | complete scan, no reversed inequalities |

Overall: pass. New helper's **fresh audit remains an explicitly assigned owner action**;
this report is credit for the original target only.

## Result

Before 36 declaration lines; after 27; saved 9 in the target. New helper 9 declaration
lines; total declaration content remains 36 lines (plus the separating blank line).
Original generator branch is resolved rather than silently deferred. No renames.
Comments preserved: none present in target; all neighboring docs/comments untouched.
Refactoring needed: fresh dedicated helper audit of `derivative_kronHasse_aux`.

Phase checklist:
- [x] Step 1 — references read
- [x] Step 2 — full 24-item audit
- [x] Step 2.5 — actual five-method mathlib search and compiled generic probes
- [x] Step 2.6 — every parameter generalisation audit, independent drop counterexample
- [x] Step 2.7 — per-line measured signature width table
- [x] Step 2.8 — inequality occurrence table
- [x] Step 3 — all 42 golfing rules considered
- [x] Step 4 — step-back reflection and alternative strategy
- [x] Step 5a — complete successful LSP, all warnings retained
- [x] Step 5b — diff gates and module build
- [x] Step 6a — no rename needed, no sidecar mutation

## Complete final warning text

### L1:2 (diagnostic)

```text
* `-/`:
Copyright too short!


Note: This linter can be disabled with `set_option linter.style.header false`
```

### L36:1 (linter)

```text
automatically included section variable(s) unused in theorem `Roth.genWronskian_eq_zero_of_not_linearIndependent`:
  [Fintype σ]
consider restructuring your `variable` declarations so that the variables are not in scope or explicitly omit them:
  omit [Fintype σ] in theorem ...

Note: This linter can be disabled with `set_option linter.unusedSectionVars false`
```

### L32:1 (diagnostic)

```text
`genWronskian_eq_zero_of_not_linearIndependent` does not use the following hypothesis in its type:
  • [Fintype σ] (#4)

Consider replacing this hypothesis with the corresponding instance of `Finite` and using `Fintype.ofFinite` in the proof, or removing it entirely.

Note: This linter can be disabled with `set_option linter.unusedFintypeInType false`
```

### L222:1 (diagnostic)

```text
`det_sum_rows` does not use the following hypothesis in its type:
  • [DecidableEq ι] (#5)

Consider removing this hypothesis and using `classical` in the proof instead. For terms, consider using `open scoped Classical in` at the term level (not the command level).

Note: This linter can be disabled with `set_option linter.unusedDecidableInType false`
```

### L240:1 (diagnostic)

```text
`exists_genWronskian_ne_zero` does not use the following hypothesis in its type:
  • [Fintype σ] (#4)

Consider replacing this hypothesis with the corresponding instance of `Finite` and using `Fintype.ofFinite` in the proof, or removing it entirely.

Note: This linter can be disabled with `set_option linter.unusedFintypeInType false`
```

