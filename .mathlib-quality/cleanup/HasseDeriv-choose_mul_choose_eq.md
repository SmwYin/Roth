# Cleanup audit: `MvPolynomial.choose_mul_choose_eq`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `a8cd173`.
Target: private lemma in `Roth/HasseDeriv.lean:147`.
The four-line proof is now a two-line `simpa` from `Nat.choose_mul`.
An explicit `Nat.le_add_left` supplies its bound, simplification handles
subtraction, and instantiated `Nat.choose_symm_add` handles symmetry.
The statement, name, private visibility, surrounding documentation and all
other declarations are byte-identical.

## Workflow and 24 audit items

Dedicated Phase 4 worker following inherited mathlib-quality/lean4 references.
Native remote results supplied by parent; local search and fresh diagnostics
used the direct MCP bridge. Optional ask_chatgpt_math skipped as authorized.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module build and full diagnostics passed; existing header warning only. |
| 2 | HAVE SCAN | Removed the sole one-use h by simpa using the library theorem. |
| 3 | SET_OPTION | None present or introduced. |
| 4 | SIMP SQUEEZE | Single terminal simpa replaces rewrites and arithmetic side proofs. |
| 5 | NAMING | Existing private choose-product equality name is descriptive; preserved. |
| 6 | LINE PACKING | Both signature lines measured below. |
| 7 | BY PLACEMENT | by remains at conclusion end. |
| 8 | FORMAT | Standard two-space proof and four-space continuation. |
| 9 | COMMENTS | No proof comments to modify. |
| 10 | DOCSTRING | Private helper has no public-doc obligation; surrounding docs preserved. |
| 11 | VISIBILITY | Private, used by immediately following coefficient-product helper. |
| 12 | STRUCTURE | Two-line specialization; removal proposal deferred below. |
| 13 | MATHLIB | Five methods; exact underlying library identity reused. |
| 14 | JUNK DEF | No definition. |
| 15 | EXISTS LEMMA | No existential. |
| 16 | SHOW vs CHANGE | Removed three show expressions, including redundant rfl wrapper. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All three natural parameters unrestricted; library has broader form. |
| 19 | INEQUALITY | Replaced omega bound with exact additive-order theorem. |
| 20 | NORMAL-FORM | Orientation chosen for next coefficient-product application. |
| 21 | SYNTAX-GEN | Ordinary choose notation; no disguised predicates. |
| 22 | IMPORT-FANOUT | Existing imports sufficient; unchanged. |
| 23 | CASTS | All operations on naturals; no casts. |
| 24 | INSTANCE-NAME | Not an instance. |

## Signature width and inequality tables

Unicode codepoint lengths measured by Python len; signature byte-identical.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 147: private lemma, parameters and colon | 48 | 48 | Complete conclusion and := by, 93 characters | 48 + 1 + 93 = 142 > 100; ok. |
| 148: complete conclusion and := by | 97 | 97 | None | Complete signature under 100; ok. |

| Scope | Relation | Assessment |
|---|---|---|
| Statement | Equality of products | No strict/non-strict or inequality-direction choice. |
| Library side condition | e ≤ d + e | Nat.le_add_left e d exactly supplies this; no new assumption. |
| Former arithmetic equalities | f + d + e - e = f + d and d + e - e = d | Standard simp cancellation replaces omega proofs. |

## Five-method mathlib search

| Method | Query/scope | Result |
|---|---|---|
| A Lean-Finder | binomial product choose d from f+d times choose e from f+d+e equals choose d from d+e times choose d+e from f+d+e; limit 3 | Nat.choose_mul exact underlying identity; add_choose_eq and choose_mul_add are different identities. |
| B Loogle | "choose_mul"; limit 5 | Nat.choose_mul plus factorial, right and successor variants. |
| C LeanSearch | binomial coefficient choose multiplication nesting identity; limit 3 | HTTP 500; unavailable, not absence evidence. |
| D Pinned source/project | choose_mul, choose symmetry, additive variants, target uses | Nat.choose_mul and choose_symm_add inspected and reused; sole project caller is hasseCoeff_mul_hasseCoeff. |
| E Local MCP | choose_mul; limit 15 | Nat.choose_mul, target and related choose identities; index unavailable, source matching works. |

Evidence: `/private/tmp/roth-choose_mul_choose_eq-native-search.json` and
`/private/tmp/roth-choose_mul_choose_eq-local.json`.
Pinned candidates inspected in `Mathlib/Data/Nat/Choose/Basic.lean`:
choose_mul (line159) gives nested choosing; choose_symm_add (203) exchanges
the complementary indices; factorial variants (140,180) would add unnecessary
factorials; choose_mul_succ_eq (220), choose_mul_add (230), and choose_mul_right
(249) concern a single coefficient scaled by a successor/multiplier.
`Mathlib/Data/Nat/Choose/Vandermonde.lean:31` gives a sum over an antidiagonal,
not this pointwise product identity. No new import is needed.

Replacement checklist: inspected definitions and actual pinned lemma types;
searched both local formulation and nested-choice formulation; identified exact
library specialization and used it; no predicate alias or topological separation
hypothesis. This helper is composable from library API, not new mathematics.
Deleting it and inlining the specialization in its caller would change a second
declaration, outside this worker's scope. Record this candidate for file-level
review: the short named identity may also make the following product proof
easier to read. Removing a tiny private wrapper is not automatically a substantial
structure change requiring user approval; that decision belongs to file-level review.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| f : ℕ | Arbitrary remaining count, including zero; no positivity needed. |
| d : ℕ | Arbitrary first selected count, including zero. |
| e : ℕ | Arbitrary second selected count, including zero. |
| Ambient σ, R and CommSemiring R | Not used or included in elaborated theorem type; no hidden assumptions. |

Nat.choose_mul is the more general reusable principle, with arbitrary n,k,s
subject only to s ≤ k. Setting n=f+d+e, k=d+e and s=e yields this subtraction-free
version after symmetry and commutativity. Inversion therefore points back to
existing mathlib, not a new general helper. Integer/generalized binomial
coefficients would change the underlying object and mathematical statement;
no such restatement is applied. No hypotheses were strengthened.

Freshly inspected `.mathlib-quality/references/clean.tex:571–588`: the proof
of the index-of-derivative lemma uses the Hasse composition coefficient product.
This scalar identity is its componentwise combinatorial ingredient.
Public source inspected: [NIST DLMF §26.3, equation 26.3.1](https://dlmf.nist.gov/26.3.E1)
gives symmetry and the factorial formula for binomial coefficients.
Inference from that formula: both products here equal
(f+d+e)! / (f! d! e!), with all parameters nonnegative. This explains the
identity without claiming DLMF states this exact Lean formulation.
The existing theorem's natural-number scope is appropriate.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No exact wrapper. |
| 1.2 by rfl | Symbolic binomial identity is not definitional. |
| 1.3 rw + exact | Replaced whole rewrite chain with simpa using. |
| 1.4 simp + exact | Single simpa uses the library theorem. |
| 1.5 trailing rfl | Removed redundant show ... from rfl inside old symmetry proof. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda. |
| 1.10 single-use have | Applied: h removed. |
| 1.11 apply + intro | No binders introduced in proof. |
| 1.12 redundant show | Applied: old arithmetic and reflexive show terms removed. |
| 1.13 have projections | None. |
| 1.14 merge rw | All rw calls replaced. |
| 1.15 terminal simp only | Final simpa unrestricted already. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | .symm selects the needed equality orientation. |
| 1.18 `<\|` | No nested application requiring it. |
| 1.19 push Not | No negation. |
| 1.20 trivial existential | None. |
| 2.1 grind | Direct named identity plus simp closes goal deterministically. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | Applied: h, three side proofs and rewrites consolidated. |
| 2.4 fun_prop | No function property. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Equality, not monotonicity. |
| 2.7 lia/omega | All three omega calls removed using library bound/cancellation. |
| 2.8 aesop | No need for search after direct identity succeeds. |
| 2.9 norm_num/norm_cast | Symbolic coefficients; no casts or numerals to normalize. |
| 2.10 decide/kernel | Symbolic naturals; closed decision procedure inapplicable. |
| 2.11 field_simp/ring | Ring cannot establish choose identities; no denominators in Lean goal. |
| 2.12 linear_combination | No equation-combination goal after named identity. |
| 2.13 wlog | No symmetry case reduction. |
| 2.14 calc | One library identity suffices; calc adds a layer. |
| 2.15 `<;>` | No independent goals to distribute over. |
| 3.1 erw/rw | No coercion-sensitive rewrite. |
| 3.2 fun_prop | No analytic tactic. |
| 3.3 omega/lia | Removed omega entirely. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | No attributes changed or added. |
| 3.6 simp_all | No local hypotheses to saturate. |
| 3.7 maxHeartbeats | None present or introduced. |

Strategy reflection: the first isolated candidate with unconstrained
Nat.choose_symm_add failed to normalize the middle binomial coefficient.
The explicitly instantiated reverse symmetry rule succeeded. Failed attempt
exit 1 and error-recovery sorryAx stayed in scratch only. Accepted experiment
exit 0 confirms original type and exactly propext, Classical.choice, Quot.sound.
It copies only the original file prefix, then the candidate; target's original
proof and all downstream project declarations are excluded, avoiding circular
proof reuse. Evidence: `/private/tmp/roth-choose_mul_choose_eq-probe.log` and
`/private/tmp/roth-choose_mul_choose_eq-probe-final.log`.

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0,1430 jobs; /private/tmp/roth-choose_mul_choose_eq-module-build.log. |
| fresh LSP | PASS: exit 0; success=true,partial=false,timed_out=false,failed_dependencies=[]; zero errors, existing header warning only. /private/tmp/roth-choose_mul_choose_eq-postedit-diagnostics.json. |
| proof/type/axioms | PASS: isolated final proof exit 0; original full type and only standard axioms. |
| definition_protected | PASS: no definition changed. |
| theorem_statement_protected | PASS: byte-identical full signature. |
| structure_gate | PASS for applied proof cleanup; helper deletion explicitly deferred. |
| naming_gate | PASS: private descriptive existing name retained. |
| line_packing_gate | PASS: 48/97 signature lengths; combined 142 exceeds 100. |
| inequality_orientation_gate | PASS: explicit standard proof of e ≤ d+e. |
| scoped diff | PASS: byte-identical prefix/suffix and signature; git diff --check exit 0. |
| dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-choose_mul_choose_eq-build.log` and `/private/tmp/roth-choose_mul_choose_eq-leaneval.log`. |

The bridge emitted an asynchronous subprocess shutdown warning after successful
complete diagnostics and exited0. Existing copyright-header warning is deferred
pending ownership/license information. No sorry, new axiom, native_decide,
option, import, version, mathematical statement, visibility or structure changed.

## Phase 4 checklist

- [x] Step 1: inherited workflow/references and target context reviewed.
- [x] Step 2: all 24 audit items assessed.
- [x] Step 2.5: five searches, actual candidates inspected, service failure disclosed.
- [x] Step 2.6: parameters, generalisation, inversion and local/public literature.
- [x] Step 2.7: complete signature-width table.
- [x] Step 2.8: inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: isolated proof alternatives and strategy reflection.
- [x] Step 5a: module and complete fresh diagnostics passed.
- [x] Step 5b: protection, naming, packing and scoped-diff gates passed.
- [x] Step 6a: helper-removal proposal deferred; no rename queue.

Parent owns dependent validation, shared logs, commit/push and file-wide phases.
