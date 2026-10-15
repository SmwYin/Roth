# Phase 4 — `MvPolynomial.factorial_smul_hasseDeriv_single`

Scope: only `Roth/HasseDeriv.lean:283–291` (before), now 283–289. Baseline `11f3d3c`, first 25 declarations complete. This worker changes only the target proof and this report. No Git operation, shared log, other declaration, definition, signature, import, version, or public documentation was changed.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full, together with the installed Lean 4 and mathlib-quality skills, Phase 4 procedure, relevant style rules, and naming conventions. The task's explicit statement and documentation preservation requirements govern this pass.

## Full audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No target warning. Final full-file diagnostics and module build show only the inherited copyright-header warning at line 1. |
| 2 | HAVE SCAN | No `have` declarations. The induction hypothesis is used once in the successor rewrite. |
| 3 | SET_OPTION | No local options or resource-limit overrides. |
| 4 | SIMP SQUEEZE | The zero branch has terminal bare `simp`, retained. No nonterminal simp. A terminal simp successor alternative compiled but was not clearer than the explicit rewrite. |
| 5 | NAMING | `factorial_smul_hasseDeriv_single` names the scalar operation, Hasse derivative, and single-coordinate index. It follows the actual `Polynomial.factorial_smul_hasseDeriv` analogue. No forbidden pattern, abbreviation, or reversed-inequality name; no rename needed. |
| 6 | LINE PACKING | Signature widths are 81 and 94 codepoints. The next complete conclusion unit is 90 codepoints (even its complete LHS is 53), so the natural conclusion break is justified. Full table below. |
| 7 | BY PLACEMENT | `:= by` ends the conclusion line. |
| 8 | FORMAT | Two-space proof indentation, no internal blank line, no semicolon chain, no `haveI`/`letI`. Extended the existing rewrite list to close the goal. |
| 9 | COMMENTS | No proof-body comments. Existing docstring and source citation preserved byte-for-byte. |
| 10 | DOCSTRING | Existing text states factorial scaling over a commutative semiring, explains its rational-algebra interpretation, and compares the univariate analogue. Preserved. |
| 11 | VISIBILITY | This is a headline public API theorem listed in the module's Main results. Source search finds no current downstream use, which does not make this advertised API an implementation helper. |
| 12 | STRUCTURE | Five proof-body lines after cleanup, down from seven. Longest branch is two tactic-text lines; no conjunction and no extraction needed. |
| 13 | MATHLIB | Univariate partial match found by multiple methods. Current recurrence proof already reuses the project's `pderiv_hasseDeriv`; direct cast/multiplication lemmas remove general normalization. Search block below. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: no existential statement or witness helper. |
| 16 | SHOW vs CHANGE | n/a: neither construct occurs. |
| 17 | PUSH_NEG | n/a: no negation-normalization tactic. |
| 18 | GENERALISE | All six parameters, including both universes and the coefficient instance, examined below. No safe weakening of the existing API; no new declaration added. |
| 19 | INEQUALITY | No inequalities in statement, binders, or proof-local hypotheses. Scan table below. |
| 20 | NORMAL-FORM | Factorial scaling on the left and iterated ordinary derivative on the right is the established characteristic-independent form, also used by the univariate theorem. |
| 21 | SYNTAX-GEN | Applied equality rewrites directly at a polynomial. A function or linear-map equality could be recovered by extensionality; no demonstrated caller need warrants adding that API. |
| 22 | IMPORT-FANOUT | n/a: no new source import. One isolated rejected experiment imported `LinearCombination`; it was not added to the file. |
| 23 | CASTS | Diff introduces no casts: 0 dropped / 0 new cross-type / 0 new load-bearing. Existing `(n.factorial : R)` is the natural-number-to-coefficient coercion; `⇑` exposes the derivation as a function for iteration. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issue fixed: unnecessary general-purpose normalization for a scalar product swap. `push_cast; ring_nf` is replaced by `Nat.cast_mul, mul_comm` inside the existing rewrite. No cross-declaration refactoring required.

## Mathlib search status

| Method | Query / action | Result |
|---|---|---|
| A — Lean-Finder | `factorial multiplied by Hasse derivative equals iterated derivative` | Found `Polynomial.factorial_smul_hasseDeriv`, `Polynomial.hasseDeriv_comp`, and `Polynomial.hasseDeriv_apply`. |
| B — Loogle | `Polynomial.hasseDeriv, Nat.factorial` | Found the univariate factorial theorem, with `[Semiring R]`. |
| C — LeanSearch | `factorial times Hasse derivative equals iterated derivative` | One request returned HTTP 500; recorded service failure, no retry or absence inference. |
| D — source search | Full target name, `factorial_smul_hasseDeriv`, `iteratedPDeriv`, `iterate_pderiv`, `pderiv_iterate`, scalar cast/factorial names in polynomial files | Found the univariate theorem in `Mathlib/Algebra/Polynomial/HasseDeriv.lean:133` and the local multivariate theorem. Read the univariate proof and the local recurrence. |
| E — local name pattern | `factorial_smul_hasseDeriv`, `Nat.cast_mul`, `iterate_succ_apply` | Positive hits for the univariate theorem, cast lemma, both iterate successor forms, and local target. Index warming; positive results independently checked in source or by `#check`. |

Auxiliary variants checked: `Polynomial.hasseDeriv_comp`, `Polynomial.hasseDeriv_apply`, `Function.iterate_succ_apply` and its prime variant, potential `iterate_pderiv`/`pderiv_iterate` names. Common-equivalents table: no discrete/finite/topological bucket matches this identity.

Conclusion: partial univariate match; preserve the multivariate API and build directly on existing recurrence/iteration/scalar lemmas. The arbitrary-variable theorem cannot be replaced by the univariate result without introducing transport to a one-variable polynomial ring over the other variables, plus compatibility results. The existing five-line induction is direct. This is not a thin 1–3-call mathlib wrapper: it establishes the relation between this project's multi-index Hasse operator and ordinary partial differentiation using induction and the project recurrence.

Live `exact?` reached the default heartbeat limit; `apply?` returned partial generic cancellation suggestions, not a closing proof. These are bounded inconclusive searches, not proofs of absence. No new theorem or global claim that mathlib lacks all equivalent formulations is made.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates / evidence | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type / universe | Variable index set, `j`, finite-support exponents, polynomial type | Already independent universe-polymorphic by explicit `#check`; deletion leaves the index type unbound. No finite, decidable, or nonempty assumption to remove. | Retain. |
| `{R : Type*}` | type / universe | Coefficient type and factorial scalar | Already independent universe-polymorphic. Deletion leaves polynomial/scalar types unbound; abstract coefficient structure already used. | Retain. |
| `[CommSemiring R]` | typeclass | Both `hasseDeriv` and `pderiv` signatures; commutativity in final scalar swap | Isolated `[Semiring R]` substitution fails to synthesize `CommSemiring R` for both operators. Full removal also fails at `hasseDeriv`. Weaker nonassociative/nonunital parents cannot supply these required instances. | Retain; actual elaboration failures recorded. |
| `(j : σ)` | structure value | Chosen coordinate for the finite-support index and partial derivative | Drop leaves two occurrences unbound; replacing with an arbitrary direction changes the operator and statement. No proposition or bundled structure to weaken. | Retain. |
| `(n : ℕ)` | structure value | Factorial, Hasse order, iterate count, induction | Drop leaves expression unbound. Replacing `ℕ` with an abstract well-founded index loses factorial/finite iteration semantics. No order or positivity hypothesis is imposed. | Retain. |
| `(P : MvPolynomial σ R)` | structure value | Arbitrary polynomial to which both operators apply | Drop leaves applied equality unbound. Extensional operator equality is an API restatement, not a weaker assumption. No degree/support restriction to remove. | Retain. |

Strict-to-weak, global-to-pointwise, decidability removal, unbundling, and unused-proposition tests: n/a, there are no proposition hypotheses or such classes. Values occur in the statement, so deletion cannot preserve its meaning. Both universe parameters are already independent.

Inversion check: the successor step uses the concrete Hasse/partial-derivative recurrence, then finishes with scalar multiplication. Abstract iterative Hasse–Schmidt systems also satisfy factorial identities, but would require an abstract family and iteration-law hypotheses, plus a bridge for these operators. No repeated local proof or downstream consumer motivates introducing that structure in this cleanup. The routine residual scalar equality is already covered by `Nat.cast_mul` and `mul_comm`, now used directly.

Big-change candidates: none warranted for the requested existing API. The user's choice to retain the current API is respected; no optional stronger degree or summed-coefficient companions are added.

### Literature search

Query: `Hasse derivative factorial iterated derivative arbitrary commutative ring generalization`.
Top three search hits recorded: [Generalised Hasse varieties and their jet spaces](https://citeseerx.ist.psu.edu/document?doi=20ec63182d074585350eda050c2377fb5fd26793&repid=rep1&type=pdf), [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5), and [Benoist, Differential schemes for rings with a Hasse derivation](https://www.ub.edu/modeltheory/modnet/slides/benoist.pdf). Opening the first PDF failed; no claim relies on its inaccessible contents.

Opened the Benoist slides (page 2), which give the iterative Hasse derivation laws over a commutative unital ring and the divided-factorial formula over a rational algebra. Also opened [Kopparty–Ta-Shma–Yakirevitch, Character sums over AG codes, §2.1, Corollary 2.1](https://eccc.weizmann.ac.il/report/2024/069/download/), which states factorial scaling equals the iterated derivative for function fields and distinguishes this from cancellation of the factorial in small positive characteristic. These primary sources support retaining the characteristic-independent scaling identity. They do not justify adding a characteristic-zero or factorial-invertibility assumption.

Read local `.mathlib-quality/references/clean.tex:119–152`: §1 defines Hasse operators over any commutative semiring and relates them to normalized iterated partial derivatives over a rational algebra. The current result directly supplies that single-coordinate relation without requiring division.

ChatGPT math MCP: skipped as explicitly allowed by parent dispatch. Literature-driven substantial changes: none warranted in this scope; general function-field/Hasse–Schmidt theories require different objects and infrastructure.

## Line packing

Explicit `#check` with `format.width 100`:

```text
@factorial_smul_hasseDeriv_single : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (j : σ) (n : ℕ)
  (P : MvPolynomial σ R), ↑n.factorial • (hasseDeriv (Finsupp.single j n)) P = (⇑(pderiv j))^[n] P
```

| Signature line | Codepoints | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 283 | 81 | Complete conclusion through `:= by` (90); complete LHS alone is 53 | 81 + 1 + 90 = 172 > 100; even 81 + 1 + 53 = 135 > 100 | ok |
| 284 | 94 | none; proof follows | n/a | ok |

The parent confirmed that the packing procedure's conclusion-unit examples govern this break: moving only the 17-character cast would strand `•` at the next line and is not required. The signature is byte-identical. Final proof line widths: 18, 16, 16, 94, 95; all within 100.

## Inequality scan

| Region | Occurrences | Rewrite | Rename |
|---|---|---|---|
| All signature parameters | 0 inequalities | n/a | none |
| Conclusion | Equality only | n/a | none |
| Proof-local hypotheses | Induction hypothesis is an equality | n/a | none |
| Name and reversed scan | No `≥`, `>`, `_ge_`, or `_gt_` | none | none |

## Golfing rule pass — all 42 rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no rewrite followed by exact. |
| 1.4 | n/a: no simp/exact chain. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | n/a: no lambda. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro chain. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no conjunction projection. |
| 1.14 | Applied: scalar cast and commutativity rewrites incorporated into the existing rewrite list, replacing two normalization tactics. |
| 1.15 | Zero branch already terminal unsqueezed simp. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | n/a: the retained rewrite list uses named equations, not applications benefiting from dot notation. |
| 1.18 | n/a: no trailing parenthesized function argument. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Tried live whole-goal grind; fails to derive the factorial/iterate identity. |
| 2.2 | n/a: no grind in retained proof. |
| 2.3 | Tested consolidated terminal simp on successor branch; compiles, same line count, but explicit rewrite is more direct. |
| 2.4 | n/a: equality of algebraic derivative values, no continuity/differentiability predicate. |
| 2.5 | n/a: no positivity/nonzero goal. |
| 2.6 | n/a: no ordered goal. |
| 2.7 | n/a: residual goal is scalar multiplication in arbitrary `R`, not Nat/Int linear arithmetic. |
| 2.8 | Tried live whole-goal aesop; fails with no progress. |
| 2.9 | Tested norm_cast after structural rewrites; leaves natural scalar products in opposite orders, closed by a further mul_comm. Direct Nat.cast_mul rewrite is shorter and retained. |
| 2.10 | n/a: arbitrary coefficient semiring, polynomial, and order; no closed decidable computation. |
| 2.11 | n/a: no denominators or field structure. |
| 2.12 | Tried linear_combination after push_cast. Initially unavailable in file imports; isolated test with its import fails to synthesize IsRightCancelAdd for the polynomial semiring. No import added. |
| 2.13 | n/a: induction cases are zero and successor, not symmetric cases. |
| 2.14 | n/a: no calc block. |
| 2.15 | n/a: base and successor have different mathematical arguments; no parallel identical subgoals. |
| 3.1 | Already rw, no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega or Nat/Int arithmetic subgoal. |
| 3.4 | n/a: no rcases/substitution. |
| 3.5 | No attribute added: factorial-scaled Hasse derivative versus iterated ordinary derivative is a choice of representation, not an unconditional simplifier normal form established by callers. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no heartbeat option. |

## Actual alternatives and step-back review

Native `lean_goal` at line 288 confirmed the successor context and the intermediate scalar-product equation. Live `lean_multi_attempt` tested grind, simp, aesop, exact?, apply?, plus successor normalization alternatives. Its line-replacement mechanism left trailing induction/continuation syntax in several trials, so those trials' parser messages are not attributed to candidate mathematics. Successful complete replacement candidates were independently compiled as full isolated examples.

| Attempt | Result |
|---|---|
| Whole-goal grind | Fails. |
| Whole-goal simp | Makes no progress. |
| Whole-goal aesop | Makes no progress. |
| Whole-goal exact? | Default heartbeat timeout; no proof obtained. |
| Whole-goal apply? | Bounded partial generic cancellation suggestions only. |
| Induction, successor terminal simp with recurrence, factorial and mul_comm | Complete isolated proof passes. |
| Induction, structural rewrites, norm_cast, then rw [mul_comm] | Complete isolated proof passes; longer than retained proof. |
| Structural rewrites, push_cast, linear_combination | Rejected: requires additive cancellation not available for arbitrary coefficient semiring. |
| Induction, successor rewrite including Nat.cast_mul and mul_comm | Complete isolated proof passes; retained, two lines saved. |

The induction follows the mathematics: order zero is the identity, and applying one more partial derivative multiplies by `n+1`. The previous final goal only swapped the factorial and `n+1` factors after casting their product. Two named rewrites express exactly that fact; full ring normalization was unnecessary. A term-mode induction would obscure the readable two-case structure. Reusing the univariate theorem through polynomial equivalences requires more infrastructure than this recurrence proof. No useful new helper, redundant have, or shorter complete one-tactic proof was found.

## Verification and gates

Native full-file `lean_diagnostic_messages`: `success=true`, `partial=false`, no failed dependencies, no errors; only inherited copyright warning at line 1. The final proof was independently redeclared as `checked`, then `@checked = @MvPolynomial.factorial_smul_hasseDeriv_single` checked by `rfl`. Both printed axiom sets are exactly `propext`, `Classical.choice`, `Quot.sound`. The scratch import reported an out-of-date informational message while the module build ran; the build subsequently completed successfully.

| New identifier in target diff | Verified by | Result |
|---|---|---|
| `Nat.cast_mul` | Local search, `#check`, complete isolated proof, module build | exists, expected natural-cast product equation |
| `mul_comm` | `#check`, complete isolated proof, module build | exists, expected commutative multiplication equation |

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.HasseDeriv`, exec session `44378`, final chunk `9d51f3`, exit 0, 1430 jobs; target built in 15s. |
| definition_protected | pass | Worker diff changes no definition/abbreviation. |
| theorem_statement_protected | pass | Snapshot comparison through `:= by` is byte-identical; no signature change. |
| structure_gate | pass | Five proof-body lines, well below headline limit 15; no conjunction and no long branch. |
| naming_gate | pass | Descriptive name mirrors verified univariate analogue; no forbidden pattern. |
| line_packing_gate | pass | Both signature rows measured; complete conclusion/LHS cannot join previous line within 100. |
| inequality_orientation_gate | pass | No inequalities or reversed names in target. |
| comments_preserved | pass | Existing docstring/source citation byte-identical; no proof comments existed. |
| identifier_verification | pass | Both introduced names checked as above. |

Overall: pass. Source finalized and successful module gate communicated to parent. Parent owns cumulative dependent builds, final review, performance pass, and publication.

## Result

Before: 9 declaration lines (7 proof lines). After: 7 declaration lines (5 proof lines). Saved: 2 lines. One concrete proof simplification; no mathematical/API change.

Audit issues found: 1. Fixed: 1. Rules applied: 1.14 and direct arithmetic normalization under 2.9. Refactoring needed: none. Renames queued: none. Comments preserved: all existing public documentation/source text; no proof comments present.

Phase checklist:

- [x] Step 1 — required references read.
- [x] Step 2 — all 24 audit slots recorded.
- [x] Step 2.5 — all five search methods recorded, including one service failure.
- [x] Step 2.6 — every parameter audited; actual instance-weakening failures and public literature recorded.
- [x] Step 2.7 — measured signature-width table.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golfing rules have a status.
- [x] Step 4 — alternate strategies tested and reviewed.
- [x] Step 5a — full LSP diagnostics, inherited header warning only.
- [x] Step 5b — gates and actual successful module-build evidence.
- [x] Step 6a — no renames required; no shared sidecar edited.

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-factorial_smul_hasseDeriv_single-build.log` and
`/private/tmp/roth-factorial_smul_hasseDeriv_single-leaneval.log`.
