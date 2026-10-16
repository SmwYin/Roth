# Phase 4: `Roth.kronecker`

Scope: `Roth/GenWronskian.lean` L48–49 only; start snapshot
`/private/tmp/roth-kronecker-before.lean`. Both installed skills, full worker contract,
golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md, relevant style-rules.md sections, naming-conventions.md and
mathlib-review-stages.md read. Initial file audit read. No other declaration owned.

## Full audit (before edit)

1. LINT: no target warning. Complete native LSP baseline: success=true, partial=false,
   timed_out=false, no errors or failed dependencies. Five warnings outside scope preserved:
   header metadata; two unused Fintype warnings for dependent-zero theorem; unused
   DecidableEq in det_sum_rows; unused Fintype in existence theorem.
2. HAVE SCAN: none; body is a single construction term.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no simp calls.
5. NAMING: `kronecker` names the standard substitution; one-word lowerCamelCase data
   definition, no forbidden pattern or abbreviation. No rename.
6. LINE PACKING: signature is one 76-codepoint line; table below.
7. BY PLACEMENT: no tactic-mode `by`.
8. FORMAT: normalize ordinary lambda `=>` to `↦`; remove redundant outer power parentheses.
   Keep two-line term definition and 2-space body indentation.
9. COMMENTS: no body comments; existing two-line docstring preserved byte-for-byte.
10. DOCSTRING: present; specifies enumeration and source formula; protected.
11. VISIBILITY: public mathematical API; preserve.
12. STRUCTURE: one-line body; no conjunction, branch, or decomposition need.
13. MATHLIB: five methods below; retain domain-specific substitution using `aeval`.
14. JUNK DEF: KEEP. Established monomial, coefficient, bounded injectivity/vanishing and
    linear-independence API, plus Hasse/Wronskian users. This names a nontrivial mathematical
    construction, not a single-use wrapper. Repository search finds users throughout module.
15. EXISTS LEMMA: n/a, this is a data definition.
16. SHOW vs CHANGE: no show/change.
17. PUSH_NEG: none.
18. GENERALISE: every elaborated parameter examined below; public type protected.
19. INEQUALITY: zero reverse-oriented inequalities; scan table below.
20. NORMAL-FORM: bundled algebra homomorphism via canonical `MvPolynomial.aeval`.
21. SYNTAX-GEN: OK; bundled map supports map_sum/map_smul and evaluation directly.
22. IMPORT-FANOUT: n/a, no new import.
23. CASTS: 0 dropped, 1 kept as genuine Fin→Nat coercion. Removing `: ℕ` in scratch fails
    with `HPow ℕ (Fin (Fintype.card σ))`; keep it. Outer parentheses around the power are
    redundant by right associativity; scratch rfl confirms unchanged value.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues to fix: (1) ordinary lambda arrow; (2) redundant outer exponent parentheses.
Refactoring needed: none. No new helper.

## Mathlib search-status

| Method | Actual query | Findings |
|---|---|---|
| A Lean-Finder | Kronecker substitution multivariate polynomials into univariate polynomials powers of a base | `MvPolynomial.expand`, `expand_X`, `coe_expand`; same-variable expansion, different target |
| B Loogle | `MvPolynomial.aeval` | canonical aeval plus aevalTower forms and range API |
| C LeanSearch | Kronecker substitution multivariate polynomial univariate polynomial | `Polynomial.toMvPolynomial`, `MvPolynomial.pUnitAlgEquiv`, `finSuccEquiv`; different constructions |
| D source rg | kronecker, kroneckerSubstitution, def aeval, def eval₂Hom, aeval_X, aeval_monomial in Algebra/MvPolynomial and RingTheory/MvPolynomial | Eval.lean defines aeval and eval₂Hom, with generator/monomial API |
| E local name search | kronecker; MvPolynomial.aeval | Roth target and matrix Kronecker products; aeval/_C/_X/_def/_sum/Tower present |

Native local search returned index=unavailable, so no absence inference is made from it.
Auxiliary variants checked: aeval_X, aeval_C, aeval_def, aeval_eq_eval₂Hom,
aeval_monomial, expand_X, coe_expand, aevalTower_id/ofId, aeval_range.
Common-equivalents lookup: no bucket match. Conclusion: partial match `MvPolynomial.aeval`;
the current definition already uses it directly. Keep this established substitution API;
no assertion of exhaustive mathematical absence, no new lemma or API wrapper.
Six replacement rules considered: no duplicate theorem introduced; all five searches performed;
auxiliary variants inspected; no custom predicate; no exact replacement to delete; existing
module documentation protected rather than rewriting it to add an unsolicited usage list.

## Generalisation status

The exact elaborated original type has `{K : Type u₁} [Field K] {σ : Type u₂}
[Fintype σ] (k : ℕ)`; section variable `l` is not included.

| # | Parameter | Class | Used as | Mechanical candidates considered/tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{K : Type*}` | type-variable | coefficient field in domain/base/codomain | drop cannot preserve dependent type; universe already polymorphic | structural | keep |
| 2 | `[Field K]` | typeclass | coefficient algebra structure for aeval | drop loses polynomial/algebra instances; parents DivisionRing, CommRing, CommSemiring considered; CommSemiring scratch compiles | scratch yes | broader coefficient API is optional, closed as unnecessary for current callers; protected type retained |
| 3 | `{σ : Type*}` | type-variable | variable index and enumeration | drop cannot preserve MvPolynomial σ; universe already polymorphic | structural | keep |
| 4 | `[Fintype σ]` | typeclass/data | Fintype.equivFin σ and card σ in value | drop removes enumeration; Finite replacement changes chosen enumeration and actual value, not a small-safe weakening | structural | keep |
| 5 | `(k : ℕ)` | structure-value | base of natural-number exponent | drop destroys parameterized family; concrete→abstract changes exponents/object; no proposition to point-localize or weaken | structural | keep |

No proposition or decidability parameter, strict inequality, bundled predicate, or global
analytic assumption occurs. Point-localization/strict→weak/unbundling have no candidates.
Inversion diagnostic: n/a, construction directly uses its coefficient structure and chosen
enumeration; no concrete witness is unfolded away in a proof. No inline generalisation applied.
Big-change candidates pending: none. Coefficient-ring abstraction is mathematically possible,
confirmed in scratch, but unnecessary without a current caller need and deliberately closed.

## Literature search status

Query 1: `Kronecker substitution polynomial generalization coefficient ring`.
Top three returned hits:
1. [Fontana–Loper, generalization of Kronecker function rings](https://citeseerx.ist.psu.edu/document?doi=00b840bcfeac531d2d511454c5938e807706186a&repid=rep1&type=pdf): different subject; exclude.
2. [Kronecker substitution](https://en.wikipedia.org/wiki/Kronecker_substitution): integer packing variant; not used as evidence for a ring-general construction.
3. [Fontana–Loper arXiv version](https://arxiv.org/abs/math/0604040): same unrelated function-ring paper; exclude.

Query 2: `"Kronecker substitution" "multivariate" "ring" generalization`.
Top three returned hits:
1. [Arnold–Roche, randomized Kronecker substitutions](https://www.researchgate.net/publication/259914885_Multivariate_sparse_interpolation_using_randomized_Kronecker_substitutions): paper describes classical substitution over a ring and randomized exponents.
2. [Sparse polynomial interpolation and testing, chapter 5](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/b213e882-3fe9-4ae4-8df3-2d889c18a18d/content): author thesis discusses arbitrary-ring interpolation and randomized substitution.
3. [Classical algorithms, §3.4.1](https://raw.githubusercontent.com/wlcsm/Honours-Thesis/master/thesis.pdf): mixed-radix substitution variant; no need to replace uniform-base enumeration here.

Math MCP: n/a, no ChatGPT math capability exposed in ALL_TOOLS.
Primary local source: clean.tex §2 L225–253 gives
`h_ν(t) = φ_ν(t, t^k, …, t^{k^{p-1}})` and bounded base-k digits.
Lean matches this generator assignment through the chosen finite enumeration. The definition
itself correctly accepts every k; the lower bound and partial-degree bound belong to the
injectivity API. Literature supports optional ring coefficients but no requested current use
justifies changing the public field signature or adding a speculative extension.
Literature-driven pending big changes: none.

## Line packing

Reference: definition (n/a exemption), additionally inspected `#check @Roth.kronecker`
with `set_option format.width 100` in scratch:
```
@Roth.kronecker : {K : Type u_1} →
  [inst : Field K] → {σ : Type u_2} → [Fintype σ] → ℕ → MvPolynomial σ K →ₐ[K] Polynomial K
```

| Sig line | Chars | Next signature token | current + 1 + next ≤ 100? | Action |
|---|---:|---|---|---|
| 48 | 76 | none; `:=` ends signature, body next | n/a; complete type already one line | ok |

Whole definition on one line would be 139 codepoints before cleanup; body is not a signature
token, and the natural term-body break remains. Final widths are verified separately.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | signature/all parameters | n/a: no ≥ or > | none | none |

## Golfing rule pass

- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl wrapper.
- [1.3] n/a: no rw/exact.
- [1.4] n/a: no simp/exact.
- [1.5] n/a: no simp/rfl.
- [1.6] n/a: no tactic constructor.
- [1.7] n/a: no apply/exact.
- [1.8] n/a: no contradiction proof.
- [1.9] n/a: lambda transforms j via enumeration, power and polynomial power; cannot eta-reduce.
- [1.10] n/a: no have.
- [1.11] n/a: no apply/intro.
- [1.12] n/a: no show.
- [1.13] n/a: no have/projection.
- [1.14] n/a: no rewrites.
- [1.15] n/a: no terminal simp only.
- [1.16] n/a: no nonterminal simp.
- [1.17] n/a: no eligible method notation simplifies the construction.
- [1.18] n/a: aeval already takes unparenthesized lambda; power parentheses removed by associativity.
- [1.19] n/a: no push_neg.
- [1.20] n/a: not an existential lemma.
- [2.1] n/a: data construction in term mode, no proof block for grind.
- [2.2] n/a: no grind.
- [2.3] n/a: no simp/closing tactic.
- [2.4] n/a: no analytic function-property goal.
- [2.5] n/a: no positivity/nonzero goal.
- [2.6] n/a: no inequality goal.
- [2.7] n/a: no arithmetic proof goal.
- [2.8] n/a: no logic/membership/structure proof goal.
- [2.9] n/a: no numeric/cast proof goal; explicit Fin→Nat coercion tested separately.
- [2.10] n/a: result is algebra-hom data, not decidable proposition.
- [2.11] n/a: no algebraic equality goal/denominator.
- [2.12] n/a: no ring proof or hypotheses for linear combination.
- [2.13] n/a: no symmetric branches.
- [2.14] n/a: no calc.
- [2.15] n/a: no generated proof goals.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability tactic.
- [3.3] n/a: no omega.
- [3.4] n/a: no rcases.
- [3.5] n/a: definition, not a proposition to register with automation.
- [3.6] n/a: no simp_all.
- [3.7] n/a: no limit option.

## Step back

Canonical aeval term is already minimal mathematical construction. Replacing it with tactic
search would obscure the generator assignment and could alter a data value. Exact?/apply?
would only search for an arbitrary map of this type, not certify its required assignment;
there is no proof block to close. The existing API justifies the name. No extraction needed.

## Verification and diff gates

Applied exactly two syntactic fixes on L49:
```diff
-  aeval fun j => Polynomial.X ^ (k ^ (Fintype.equivFin σ j : ℕ))
+  aeval fun j ↦ Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)
```
Start-snapshot comparison confirms no other source edit. Final signature remains 76 codepoints;
body is 61 codepoints; a single-line definition would be 136, so the natural body break is kept.
The final line-packing table is therefore unchanged: sole signature L48, 76 chars, no next
signature token, action ok. Final reverse-inequality count in signature/hypotheses: zero.

Complete post-edit native `lean_diagnostic_messages` returned success=true, partial=false,
timed_out=false, failed_dependencies=[], zero errors, no target warning and the exact same five
outside warnings. No LSP fallback needed. The native tool schemas were discovered in ALL_TOOLS.

`/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session74890, exit0;
module built in 23s. No full build or Roth.LeanEval build performed by this worker.

Independent external scratch `/private/tmp/roth-kronecker-verify.lean` compiled with
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-kronecker-verify.lean`, session94911,
exit0. It checks the exact original implicit/instance/explicit type, compares the complete
function to a verbatim original-value reconstruction by rfl, and compares by rfl with an
independently assembled AlgHom using eval₂Hom and its coefficient-commutation proof. It also
checks the generator formula and the optional CommSemiring construction. Only a scratch-only
universe-alias lint warning occurs; no source warning was introduced. An earlier scratch pass
needed explicit universe parameters on the type alias; corrected only in scratch.
`#print axioms Roth.kronecker` reports exactly `[propext, Classical.choice, Quot.sound]`.
Removing the Fin→Nat coercion was independently tried and rejected by the elaborator;
no failed candidate was applied to the source.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | actual module build session74890 exit0 |
| definition_protected | ✓ pass | declaration line/type/visibility unchanged; body changes are rfl-equal to original |
| theorem_statement_protected | ✓ pass | no theorem/lemma lines changed |
| structure_gate | ✓ pass | one-line body, no conjunction or branch |
| naming_gate | ✓ pass | standard descriptive lowerCamelCase name, no forbidden pattern |
| line_packing_gate | ✓ pass | complete single-line signature table, 76 codepoints, no repack |
| inequality_orientation_gate | ✓ pass | scan table emitted, zero ≥/> in code |

Overall: pass.

Source SHA256 at ownership handback:
`0def23fb49d7e7ceab911c7637391c7e343b5f71307b503855950a1757d14fe2`.
Parent explicitly revoked source ownership after receiving this hash; subsequent work was
limited to this report and isolated scratch verification. No fresh helper was introduced,
so fresh-helper audit is n/a.

## Result

Before: 2 lines. After: 2 lines. Saved: 0 lines; 3 codepoints removed from body.
Audit issues found: 2. Fixed: 2. Refactoring deferred: 0.
Rules applied: formatting/lambda normalization and associativity-parenthesis cleanup;
no tactic golfing rule applies to the single construction term.
Gates: pass. Renames queued: none. Comments preserved: two-line existing docstring exactly;
no body comments present. Refactoring needed: none. Optional coefficient extension closed,
not pending. Public type, mathematical value, docs, and established API preserved.

Phase checklist:
- [✓] Step 1 — reference docs read.
- [✓] Step 2 — full 24-item audit emitted.
- [✓] Step 2.5 — five actual search methods and auxiliary variants recorded.
- [✓] Step 2.6 — every parameter, catalogue applicability, and public literature recorded.
- [✓] Step 2.7 — every signature line measured with codepoint arithmetic/exhaustion.
- [✓] Step 2.8 — inequality scan table emitted and final scan checked.
- [✓] Step 3 — all 42 golfing rules individually assessed with reasons.
- [✓] Step 4 — step-back reflection recorded.
- [✓] Step 5a — complete successful LSP diagnostics, all warnings disclosed.
- [✓] Step 5b — actual module gate and all protection/content gates passed.
- [✓] Step 6a — no rename needed, so no sidecar mutation.
