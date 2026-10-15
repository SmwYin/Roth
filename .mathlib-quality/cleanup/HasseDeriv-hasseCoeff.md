# Cleanup audit: `MvPolynomial.hasseCoeff`

Date: 2026-10-14. Scope: `Roth/HasseDeriv.lean:44`, one public data definition.
The only source edit is eta reduction and mathematical lambda notation:

```diff
-def hasseCoeff (d k : σ →₀ ℕ) : ℕ := d.prod fun j n => (k j).choose n
+def hasseCoeff (d k : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose
```

No signature, visibility, name, docstring, citation, import, version, or mathematical meaning changed.
No commit or push was performed by this worker; publication belongs to the parent.

## Reference reading

Read the complete supplied 853-line worker prompt; all of `golfing-rules.md`,
`proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`,
`cleanup-gates.md`, `naming-conventions.md`, and `mathlib-review-stages.md`;
the applicable style sections on formatting, comments, documentation, definitions,
lambda syntax, visibility, normal forms, generality, and API completeness.
Reads used bounded ranges to avoid truncation. A truncated generalisation reference
was reread in full before the source edit.

## Full audit (24 items)

| # | Item | Concrete disposition |
|---|---|---|
| 1 | LINT | Pre- and post-edit whole-file LSP: no declaration warning or error; only the existing line 1 copyright-header warning. Root supplied the complete post-edit response; see verification. |
| 2 | HAVE SCAN | n/a: the data term contains no `have`. |
| 3 | SET_OPTION | None in this declaration; no option added. Scratch `format.width` affects only probe rendering. |
| 4 | SIMP SQUEEZE | n/a: no simplifier call or tactic proof. |
| 5 | NAMING | `hasseCoeff` is descriptive lowerCamelCase for natural-number data; `hasse` identifies its derivative use and `Coeff` matches the surrounding coefficient API. No forbidden numbered pattern, single-letter public name, `_ge_`/`_gt_`, or forbidden abbreviation. No rename needed. |
| 6 | LINE PACKING | Single signature line through `:=` is 36 Unicode codepoints; complete edited declaration is 64. No next signature line. Required table below. |
| 7 | BY PLACEMENT | n/a: no `by` in the definition. |
| 8 | FORMAT | Flush-left declaration, ordinary spaces, no blank interior line or trailing whitespace. Replaced lambda `=>` with `↦` and removed eta-redex `fun n ↦ (k j).choose n`. No `haveI`/`letI`. |
| 9 | COMMENTS | No inline comments; the existing public docstring and all surrounding source citations remain byte-identical. |
| 10 | DOCSTRING | Existing one-sentence docstring explains the binomial product and the important support-of-`d` convention, information beyond the type. Retained. |
| 11 | VISIBILITY | Public justified by direct uses in `Roth.CoeffNorm` and `Roth.Taylor`, plus the surrounding public API. |
| 12 | STRUCTURE | One-line data body; no conjunction, branch, or extractable proof block. No decomposition needed. |
| 13 | MATHLIB | Five-method status below. No confirmed replacement; no claim of exhaustive absence, since LeanSearch is unavailable and a generic proof-search absence probe is not meaningful for an arbitrary inhabitant of `ℕ`. |
| 14 | JUNK DEF | Keep: names the multivariate binomial factor, has zero/product/bound/composition API, and is used in multiple downstream files. Not a single-use wrapper. |
| 15 | EXISTS LEMMA | n/a: not an existential theorem. |
| 16 | SHOW vs CHANGE | n/a: neither appears. |
| 17 | PUSH_NEG | n/a: no negation tactic. |
| 18 | GENERALISE | Already universe-polymorphic and independent of `R`/`CommSemiring`. Scratch probe admits `k : σ → ℕ`; flagged below as a public API change requiring approval, not applied. |
| 19 | INEQUALITY | No inequality in signature or body; table below. The original lambda token `=>` was not an inequality. |
| 20 | NORMAL-FORM | Componentwise product of `Nat.choose` is the intended multi-index binomial coefficient. Retain `Finsupp.prod` over support of `d`; multinomial coefficients count a different object. No equivalence network introduced. |
| 21 | SYNTAX-GEN | Existing explicit `d k` arguments support all callers. Function-valued `k` is a possible wider API, considered separately rather than silently changing callers. |
| 22 | IMPORT-FANOUT | n/a: no new imports. Parent validated full dependent closure. |
| 23 | CASTS | 0 dropped / 0 kept as cross-type / 0 kept as load-bearing: no explicit casts or expression ascriptions in the edited body. Binder/result type annotations retained as the API. |
| 24 | INSTANCE-NAME | n/a: definition, not an instance. |

Issues fixed: mathematical lambda arrow and its inner eta-redex (two related syntax improvements).
Refactoring candidate: generalize the upper index `k` to an arbitrary function, only with approval.

## Line packing

Reference: definition (the required theorem pretty-printer comparison is inapplicable).
The successful Lean probe nevertheless printed:

```lean
@MvPolynomial.hasseCoeff : {σ : Type u_1} → (σ →₀ ℕ) → (σ →₀ ℕ) → ℕ
```

| Signature line | Codepoints through `:=` | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 44 | 36 | none; same-line body follows | n/a: no second signature line; full line 64 ≤ 100 | ok |

Measured after the edit with Python Unicode `len`, not UTF-8 byte counts.
No signature lines omitted; no repacking is possible or required.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | Complete signature and body | n/a: no `≥` or inequality `>` | none | none |

## Mathlib search status

All five methods were attempted. Initial MCP network attempts failed with DNS `Errno 8`;
an escalation retry was interrupted after waiting for approval. Root later retried the
remote methods with network permission. Evidence: `/private/tmp/roth-search-probe.jsonl`.

| Method | Query / scope | Actual result |
|---|---|---|
| A Lean-Finder | `multi-index binomial coefficient product of Nat.choose over Finsupp support`; root bounded retry | Initial DNS failure; root retry succeeded with `Finsupp.multinomial_eq`, `Finsupp.multinomial`, `Finsupp.multinomial_update`. Those concern `(sum f)! / prod(f!)`, not the two-multi-index coordinatewise binomial product; no replacement established. |
| B Loogle | `Finsupp.prod, Nat.choose`; root bounded retry | Initial DNS failure; root retry succeeded with an empty item list. |
| C LeanSearch | `multi-index binomial coefficient product of binomial coefficients`; root bounded retry | Initial DNS failure; retry reached service but returned HTTP 500. Unavailable, not a negative search result. |
| D Source search | Untruncated `hasseCoeff\|Finsupp.*choose\|def choose\|def.*[Bb]inomial` over pinned Mathlib; `prod.*choose\|choose.*prod\|multichoose` over `Data/Finsupp` and `Algebra/MvPolynomial` | No `hasseCoeff` duplicate found. Broader search found `Nat.choose`, `Ring.choose` and unrelated constructions; targeted product search returned no matches. |
| E Local name search | `lean_local_search` query `hasseCoeff`, limit 100 | Success: seven project declarations including `_eq_prod`, `_eq_zero_iff`, `_mul_succ`, `_le_two_pow`, `_single_add_eq`, `_mul_hasseCoeff`; index field says `unavailable`. Source-based matches are usable but not proof of a complete semantic index. |

Auxiliary variants: the prefix search covered all six returned suffix variants above;
source searches also covered product/binomial/multichoose alternatives. The common-equivalents
table has no matching topology/finiteness/separation/boundedness bucket.

Conclusion: keep the existing useful definition. No equivalent replacement is confirmed.
Do not conclude “not in mathlib, all methods exhausted”: remote C is unavailable and
the local index is incomplete. The body already directly uses `Finsupp.prod` and `Nat.choose`.
The six replacement rules were considered: no proven duplicate or custom class predicate,
no wrapper lemma to delete, no API extraction signal in this one-line data construction,
and no new mathlib dependency requiring module documentation. No generic `exact?` test
for an arbitrary natural number is treated as a semantic equivalence test: returning `0`
would inhabit the type but would not preserve this definition.

## Generalisation status

| # | Parameter | Class | Use | Candidates and verification | Result |
|---|---|---|---|---|---|
| 1 | `{σ : Type u_1}` | type variable | domain of both finitely supported functions and product index | Already arbitrary universe; `#check`/`#print` confirm. Dropping would leave the domain unbound; no universe weakening remains. | Keep. |
| 2 | `(d : σ →₀ ℕ)` | structure value | determines finite support and each lower binomial index | Dropping leaves `d.prod` unbound and changes the callable object. Arbitrary-function replacement lacks finite support and would require a new product convention. No proposition/class/strictness candidate applies. | Keep; no mechanical weakening. |
| 3 | `(k : σ →₀ ℕ)` | structure value | only read pointwise at `k j` | Drop leaves `k j` unbound. Isolated `lean_run_code` probe with `(k : σ → ℕ)` compiled successfully. This changes the public argument type, so no live-file substitution was attempted. | Candidate deferred for user approval. |
| 4 | surrounding `{R : Type*} [CommSemiring R]` | section context, not actual parameters | no occurrence | `#check @MvPolynomial.hasseCoeff` and `#print` show neither is captured; no redundant instance to remove. | Already absent. |

No propositional hypotheses, decidability assumptions, strict inequalities, pointwise/global
analytic hypotheses, or bundled equivalences occur. Natural-number upper/lower entries are
the actual binomial data, not incidental induction hypotheses. Generalized binomial rings
would require a different codomain and public mathematical formulation; not a routine cleanup.
Inversion check: n/a, this is a data definition with arbitrary multi-indices, not a theorem
whose proof discards a concrete named object.

Big-change candidate for Phase 5a: `(k : σ → ℕ)` instead of finitely supported `k`.
The body compiles in an isolated probe because only `d` supplies support. This is optional
API expansion; preserve the current signature unless the user approves. No downstream
compilation under a changed signature is claimed.

## Literature search status

Web query: `multivariate Hasse derivative multi index binomial coefficient generalization`.
Search and page opens succeeded. Top three returned hits were captured:

1. [Infinitesimal translations and a multivariate Grunwald–Letnikov calculus](https://arxiv.org/abs/1904.02710): broader fractional-calculus formalism; no required change to this discrete factor identified.
2. [ECCC report 2026/032](https://eccc.weizmann.ac.il/report/2026/032/download): contains multivariate Hasse derivative material; opened, but no detailed PDF theorem audit claimed.
3. [Generalization of Pascal’s Rule and Leibniz’s Rule for Differentiation](https://scholar.rose-hulman.edu/rhumj/vol18/iss1/12/): concerns multinomial Pascal/Leibniz identities; not evidence that this two-index product is redundant.

Also inspected the displayed [multi-index binomial convention](https://en.wikipedia.org/wiki/Multi-index_notation),
which agrees with the coordinatewise product. This is a contextual lookup; the actual
code-equivalence claim below is kernel-checked. No additional literature-driven change
was established. Optional ChatGPT mathematical MCP: skipped as authorized; no insight
from it is claimed. The function-valued `k` candidate comes from direct code inspection
and a compiled probe, not from an unverified literature assertion.

## Golfing pass (all 42 rules)

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no tactic proof. |
| 1.2 by rfl | n/a: no tactic proof. |
| 1.3 rw + exact | n/a: no rewrites. |
| 1.4 simp + exact | n/a: no simplification tactics. |
| 1.5 trailing rfl after simp | n/a: no simplification tactics. |
| 1.6 constructor chain | n/a: no constructor proof. |
| 1.7 apply + exact | n/a: no applications in tactic mode. |
| 1.8 by_contra + push_neg | n/a: no proposition proof. |
| 1.9 eta-reduce lambdas | Applied: `fun j n => (k j).choose n` becomes `fun j ↦ (k j).choose`; `rfl` equivalence compiled. |
| 1.10 single-use have | n/a: no local facts. |
| 1.11 apply + intro | n/a: term-mode data construction. |
| 1.12 redundant show | n/a: no `show`. |
| 1.13 have + projections | n/a: no `have` or pair projections. |
| 1.14 merge rw | n/a: no rewrites. |
| 1.15 terminal simp only | n/a: no simplifier calls. |
| 1.16 nonterminal bare simp | n/a: no simplifier calls. |
| 1.17 dot notation | Already uses `d.prod` and `(k j).choose`; no further change. |
| 1.18 use <\| | Already passes lambda without redundant parentheses; no trailing application parentheses to eliminate. |
| 1.19 push_neg → push Not | n/a: no negation tactic. |
| 1.20 trivial single-use existential | n/a: public natural-number definition. |
| 2.1 grind | n/a: no proof goal; synthesizing arbitrary natural data is not an equivalent definition. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa consolidation | n/a: no simp proof chain. |
| 2.4 fun_prop | n/a: no function-property proposition. |
| 2.5 positivity | n/a: no positivity goal. |
| 2.6 gcongr | n/a: no inequality goal. |
| 2.7 lia / omega | n/a: no arithmetic proposition proof. |
| 2.8 aesop | n/a: data definition, not a logic/membership proof. |
| 2.9 norm_num / norm_cast | n/a: no computation/cast proof goal. |
| 2.10 decide / decide +kernel | n/a: no decidable proposition. |
| 2.11 field_simp; ring | n/a: no field identity. |
| 2.12 linear_combination | n/a: no ring proof or hypotheses. |
| 2.13 wlog | n/a: no case branches. |
| 2.14 calc composition | n/a: no calc block. |
| 2.15 <;> multiple goals | n/a: no tactic goals. |
| 3.1 erw → rw | n/a: no rewrite tactic. |
| 3.2 continuity → fun_prop | n/a: no analytic-property proof. |
| 3.3 omega → lia | n/a: no arithmetic tactics. |
| 3.4 rcases with rfl | n/a: no case analysis. |
| 3.5 automation attributes | n/a: definition, not an equational proposition to register; neighboring API is outside this declaration's scope. |
| 3.6 simp_all | n/a: no simp_all call. |
| 3.7 remove maxHeartbeats | n/a: no option override. |

## Step back and think

The definition is already one term built from the natural API. Proof automation cannot
replace a data definition merely by inhabiting its type. Eta reduction removes the one
redundant binder while preserving the exact computational object; the outer `j` binder
is used in `k j` and is not an eta-redex. No local fact, redundant tactic, ugly proof block,
or missing structural API appears. Replacing the binomial product with a multinomial
coefficient would change the mathematical object.

## Verification and diff gates

Before editing, `lean_run_code` succeeded (`success: true`, `timed_out: false`) on:

```lean
import Roth.HasseDeriv
set_option format.width 100
#check @MvPolynomial.hasseCoeff
#print MvPolynomial.hasseCoeff
example {σ : Type*} (d k : σ →₀ ℕ) :
    MvPolynomial.hasseCoeff d k = d.prod (fun j n ↦ (k j).choose n) := rfl
example {σ : Type*} (d k : σ →₀ ℕ) :
    d.prod (fun j n => (k j).choose n) = d.prod (fun j ↦ (k j).choose) := rfl
example {σ : Type*} (d : σ →₀ ℕ) (k : σ → ℕ) : ℕ :=
  d.prod fun j ↦ (k j).choose
#print axioms MvPolynomial.hasseCoeff
```

Only standard axioms reported: `propext`, `Classical.choice`, `Quot.sound`.
No source `sorry`, axiom, unsafe evaluation tactic, or placeholder added.

Worker launched `lake build Roth.HasseDeriv` (session 73318), but its exit output was
not received before interruption. Root subsequently ran full `lake build` and
`lake build Roth.LeanEval`, both exit 0. Logs read:
`/private/tmp/roth-hasseCoeff-build.log` (2586 jobs) and
`/private/tmp/roth-hasseCoeff-leaneval.log` (2585 jobs). The full build explicitly
replayed `Roth.HasseDeriv` and covered its dependent modules; LeanEval was built separately.
This is stronger build coverage than the outstanding worker-only module invocation.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass via full build | Root `lake build`, exit 0, includes `Roth.HasseDeriv`; original worker module invocation's exit is unobserved, not claimed. |
| definition_protected | pass with explicit scope adaptation | Literal def-line grep flags this edit, but user authorized equivalent routine syntax, parent explicitly authorized eta/arrow change, and compiled `rfl` proves exact body equivalence. Signature/name/visibility unchanged. This is an explicit authorized exception, not an unnoticed definition rewrite. |
| theorem_statement_protected | pass | No theorem/lemma line changed. |
| structure_gate | pass | One-line data body, no conjunction or branches. |
| naming_gate | pass | Descriptive lowerCamelCase; no forbidden pattern or abbreviation. |
| line_packing_gate | pass | Complete measured one-row signature table; full line 64 codepoints. |
| inequality_orientation_gate | pass | Complete scan: no inequality occurrences. |
| cumulative_no_unintended_external_breakage | pass | Root full `lake build` and explicit `lake build Roth.LeanEval` both exit 0. |
| postedit LSP diagnostic checkpoint | pass | Root's fresh `lean_diagnostic_messages` completed: `success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`, no errors, exactly the existing header warning. Evidence `/private/tmp/roth-hasseCoeff-diagnostics.json`; MCP exit 0. |

Overall: pass, with external LeanSearch unavailable and the optional public-API
generalization explicitly deferred. The original worker LSP response was unobserved;
root's fresh complete response supplies the post-edit evidence. A subsequent asyncio
cleanup warning did not change the successful MCP diagnostic response or exit status.

## Result and phase checklist

Before: 1 line. After: 1 line. Saved: 0 lines; redundant lambda binder removed.
Audit issues fixed: 2 related syntax issues. Refactoring candidates deferred: 1 optional
public-API generalization. Rules applied: 1.9 and lambda notation style.
Renames queued: none. Comments: no inline comments present; public docstring preserved.

- [x] Step 1: required references read.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: all five search methods attempted, successes and service/index limits explicit.
- [x] Step 2.6: parameter-by-parameter generality analysis, compiled candidate, literature status.
- [x] Step 2.7: measured complete signature-width table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 golfing rules have concrete statuses.
- [x] Step 4: strategy reflection completed.
- [x] Step 5a: root's complete postedit LSP response confirms no errors; full builds also passed.
- [x] Step 5b: diff gates recorded, including authorized definition syntax exception.
- [x] Step 6a: no rename required; no queue mutation.

All checklist entries are satisfied for this declaration, subject to the explicitly
recorded unavailable search service and authorized equivalent-definition syntax adaptation.
The file-wide cleanup phases and publication remain the parent's responsibility.
