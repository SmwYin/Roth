# Cleanup audit: `MvPolynomial.hasseDeriv`

Date: 2026-10-15 (America/Chicago). Scope: `Roth/HasseDeriv.lean:51–54` only.
Baseline is the parent's validated and pushed `f234f0e` checkpoint.
Applied one notation change, `fun k : σ →₀ ℕ =>` to `fun k : σ →₀ ℕ ↦`.
Name, signature, visibility, construction, useful docstring and source citation are unchanged.
No commit or push by this worker; dependent validation and publication belong to parent.

## Workflow and reference basis

Used the parent-supplied complete Phase 4 workflow and reference analysis, supplemented
by the preceding declaration audit, direct cleanup-gates reading, and all 42 golf-rule
headings. Did not claim a fresh independent reread of all the parent's references.
Claude interfaces are adapted to direct Lean LSP MCP, source search, web search, and
shell build. Noncomputable data construction is not an arbitrary inhabitation problem:
no proof-search output is accepted as an equivalent replacement without equality evidence.

## Full audit (24 items)

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Fresh complete post-edit LSP: no errors; only pre-existing line 1 header warning. |
| 2 | HAVE SCAN | No `have` terms. |
| 3 | SET_OPTION | No options in target and none added. Scratch `format.width` only prints diagnostics. |
| 4 | SIMP SQUEEZE | No simp invocation or tactic proof. |
| 5 | NAMING | Descriptive lowerCamelCase data name agrees with `Polynomial.hasseDeriv`; no forbidden abbreviation or numbered pattern. |
| 6 | LINE PACKING | Single signature line through `:=`: 86 codepoints; complete table below. |
| 7 | BY PLACEMENT | No `by` in definition. |
| 8 | FORMAT | Mathematical lambda arrow applied; existing continuation indentation and composition parentheses retained. No whitespace defects. |
| 9 | COMMENTS | No inline comments; existing explanatory docstring and §1 source citation retained verbatim. |
| 10 | DOCSTRING | Documents action on monomials and why truncated subtraction is harmless, beyond merely restating type. |
| 11 | VISIBILITY | Public essential: used in Taylor and generalized Wronskian constructions and the surrounding derivative API. |
| 12 | STRUCTURE | Three body lines, no conjunctions/branches, no helper extraction indicated. |
| 13 | MATHLIB | Five-method search attempted; local methods succeeded, remote services failed DNS and approval retry interrupted. No duplicate established; detailed limits below. |
| 14 | JUNK DEF | Keep named mathematical operator with substantial API and downstream uses; not a single-use wrapper. |
| 15 | EXISTS LEMMA | Not an existential lemma. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Full parameter analysis below. `CommSemiring R` required by pinned `MvPolynomial` and the construction; no routine weakening established. |
| 19 | INEQUALITY | No inequality in signature/body; table below. Docstring's `d ≤ k` is already preferred orientation. |
| 20 | NORMAL-FORM | Canonical bundled R-linear operator, built from linear monomial maps and coefficient equivalence. No alternative normal-form network needed. |
| 21 | SYNTAX-GEN | Universe-polymorphic arbitrary variable type; explicit derivative multi-index and inferred coefficient semiring are appropriate. |
| 22 | IMPORT-FANOUT | No imports changed or added. |
| 23 | CASTS | 0 dropped, 1 kept as cross-type: `hasseCoeff d k : R` casts ℕ to R for R-linear scalar multiplication. Lambda type annotation identifies exponent Finsupp, not a cast. |
| 24 | INSTANCE-NAME | Not an instance. |

## Signature width and inequalities

Measured Unicode codepoints with Python `len`, not UTF-8 bytes.

| Signature line | Width through `:=` | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 51 | 86 | none | 86 ≤ 100; no second signature line | ok |

Body lines 52–54 measure 34, 76, 53 respectively after edit. Nothing omitted or repacked.
`#check @MvPolynomial.hasseDeriv` confirms exactly `{σ : Type u_1} → {R : Type u_2} →
[CommSemiring R] → (σ →₀ ℕ) → MvPolynomial σ R →ₗ[R] MvPolynomial σ R`.
The theorem-specific pretty-printer comparison does not apply to this definition.

| # | Scope | Original inequality | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Entire signature/body | none | none | none |
| 2 | Existing docstring | `d ≤ k` | already preferred | none |

## Mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | `Hasse derivative of multivariate polynomials over a commutative semiring` | DNS Errno 8. Escalated batch retry waited for approval and was interrupted; no successful response claimed. |
| B Loogle | `"hasseDeriv"` | DNS Errno 8; retry interrupted as above. |
| C LeanSearch | `multivariate Hasse derivative linear map on multivariate polynomials` | DNS Errno 8; retry interrupted as above. |
| D Source search | `def hasseDeriv`, `hasseDeriv`, `Hasse derivative` in pinned MvPolynomial and Polynomial/HasseDeriv | No MvPolynomial match; univariate `Polynomial.hasseDeriv` and API found. Inspected its definition, plus MvPolynomial/Basic and MonoidAlgebra/Module infrastructure. |
| E Local MCP name search | `hasseDeriv`, limit 100 | Success, 40 matches, index status `unavailable`; useful source matches include project MvPolynomial API, `Polynomial.hasseDeriv`, and `LaurentSeries.hasseDeriv`. |

Evidence: `/private/tmp/roth-hasseDeriv-search.jsonl` and
`/private/tmp/roth-hasseDeriv-local.json`. Service failure is not a negative mathematical
search. The univariate polynomial and Laurent-series operators are different domains;
their names do not justify deleting the multivariate operator. Existing project
`hasseDeriv_single_aeval_X`/`uniqueAlgEquiv_hasseDeriv` already provide univariate compatibility.
No common-equivalents topology/finiteness/separation bucket applies. Prefix source/local
search covers derivative suffix variants; no equivalent replacement was established.
The six replacement considerations yield no confirmed duplicate, predicate wrapper,
unnecessary standalone lemma, redundant local class predicate, missing helper signal,
or new imported API requiring module documentation. Do not claim exhaustive absence.

## Parameter-by-parameter generality and inversion

| Parameter | Classification/use | Drop/weaken analysis | Disposition |
|---|---|---|---|
| `{σ : Type u_1}` | Variable index type | Used in exponent Finsupp and polynomial domain/codomain; already arbitrary universe, no finiteness or decidability assumptions. Dropping leaves types unbound. | Keep. |
| `{R : Type u_2}` | Coefficient/scalar type | Used in both polynomial types, coefficient equivalence and scalar linear maps; independent universe. Dropping leaves types unbound. | Keep. |
| `[CommSemiring R]` | Algebraic class | Parent candidates `Semiring`, `NonUnitalCommSemiring`, `CommMonoidWithZero` do not supply the required CommSemiring instance. Pinned `MvPolynomial` abbrev itself takes CommSemiring, as do `monomial` and `LinearMap.lsmul`; successful `#check` evidence confirms signatures. | Keep; no claimed compiled weakening. |
| `(d : σ →₀ ℕ)` | Derivative multi-index | Used in `k - d` and binomial factor. Dropping changes the operator. Arbitrary functions lack finite support required by current coefficient helper and subtraction type. | Keep. |

No unused propositional assumptions, inequalities, global analytic hypotheses, bundled
equivalences or explicit decidability instances are available to weaken/localize.
Inversion check: data construction, not a theorem ignoring a special named object.
An arbitrary inhabitant of its linear-map type (such as zero) is not evidence of equivalence.
Possible broader framework over noncommutative coefficient algebras would require changing
the polynomial representation/public interface; no such change proposed or applied here.

## Literature

Web query `multivariate Hasse derivative definition commutative ring polynomials binomial coefficient`
succeeded. Top relevant returned primary sources inspected:

1. [Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025): search result gives Definition 3.4 over a commutative ring; publisher page returned 403.
2. [Improved PIR Schemes using Matching Vectors and Derivatives](https://www.math.utoronto.ca/swastik/PIR.pdf): PDF opened; Definition 3.5 uses the coefficient of the auxiliary multi-index in a translated polynomial over a field.
3. [Author copy of Fast Multivariate Multipoint Evaluation](https://mrinalkr.bitbucket.io/papers/MME2.pdf): PDF opened; the corresponding definition uses coefficient extraction after translation.

These are contextual evidence for the usual operator, not kernel-equivalence evidence.
Our inference: finite-variable ring/field presentations do not demand stronger hypotheses
than the current arbitrary-index commutative-semiring construction. The existing binomial
action is the familiar expanded formulation; switching to translation would be a substantive
construction rewrite, not needed for this syntax cleanup. No literature-driven API change
established. Optional `ask_chatgpt_math` skipped as authorized.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | n/a: no tactic proof. |
| 1.2 by rfl | n/a: no tactic proof. |
| 1.3 rw + exact | n/a: no rewrite. |
| 1.4 simp + exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: no simp/rfl proof. |
| 1.6 constructor chain | n/a: no proposition construction. |
| 1.7 apply + exact | n/a: no tactics. |
| 1.8 by_contra + push_neg | n/a: no negation proof. |
| 1.9 eta reduction | Lambda k used in both subtraction and coefficient; not an eta-redex. |
| 1.10 single-use have | n/a: none. |
| 1.11 apply + intro | n/a: term-mode construction. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: none. |
| 1.14 merge rw | n/a: none. |
| 1.15 terminal simp only | n/a: none. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | `.comp` and `.toLinearMap` already used naturally. |
| 1.18 `<\|` | Lambda argument is followed by outer composition; parentheses delimit that scope. Keep. |
| 1.19 push Not | n/a: no negation tactic. |
| 1.20 trivial existential | n/a: not existential. |
| 2.1 grind | n/a: data construction; arbitrary linear map would not preserve meaning. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa | n/a: no proof chain. |
| 2.4 fun_prop | n/a: no property goal. |
| 2.5 positivity | n/a: no positivity goal. |
| 2.6 gcongr | n/a: no inequality goal. |
| 2.7 lia/omega | n/a: no arithmetic proof. |
| 2.8 aesop | n/a: constructing arbitrary data is not proving equivalence. |
| 2.9 norm_num/norm_cast | n/a: no computation proposition; the natural-number cast is necessary. |
| 2.10 decide/kernel | n/a: no decidable proposition. |
| 2.11 field_simp/ring | n/a: no field identity. |
| 2.12 linear_combination | n/a: no equational proof goal. |
| 2.13 wlog | n/a: no branches. |
| 2.14 calc | n/a: no calc chain. |
| 2.15 `<;>` | n/a: no tactic goals. |
| 3.1 erw/rw | n/a: no rewrite tactic. |
| 3.2 fun_prop | n/a: no continuity/measurability proof. |
| 3.3 omega/lia | n/a: no arithmetic tactics. |
| 3.4 rcases rfl | n/a: no case analysis. |
| 3.5 automation attributes | Definition is not an equational lemma; neighboring simp API outside scope. |
| 3.6 simp_all | n/a: absent. |
| 3.7 maxHeartbeats | n/a: no override. |

Step back: the existing three-line term already expresses the linear extension from
monomials. No redundant proof structure exists. Preserve its transparent construction;
the only necessary style edit is the mathematical lambda arrow.

## Verification and gates

Successful `lean_run_code` (success true, timed_out false) compiled the equality below
against the original imported definition, with no warnings/errors:

```lean
example {σ R : Type*} [CommSemiring R] (d : σ →₀ ℕ) :
    MvPolynomial.hasseDeriv d =
      Finsupp.lsum R (fun k : σ →₀ ℕ ↦
        (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) ∘ₗ
          (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap := rfl
```

Probe uses `import Roth.HasseDeriv` and `open MvPolynomial`; evidence JSON is
`/private/tmp/roth-hasseDeriv-code-result.json`. Axiom inspection reports only
`propext`, `Classical.choice`, `Quot.sound`. No source axioms/placeholders added.

| Gate | Status/evidence |
|---|---|
| lake_build_file | PASS: `lake build Roth.HasseDeriv`, exit 0, 1430 jobs, worker session 49493. Parent subsequently reused `/private/tmp/roth-hasseDeriv-build.log` for stronger full-build evidence (2586 jobs, exit 0). |
| postedit LSP | PASS: fresh full-file response success=true, partial=false, timed_out=false, failed_dependencies=[]; only existing header warning. `/private/tmp/roth-hasseDeriv-diagnostics.json`. Process exit 0; subsequent asyncio destructor warning did not invalidate response. |
| definition_protected | PASS under explicitly authorized routine syntax adaptation: exact compiled `rfl` equality; signature/name/visibility unchanged. Only body arrow changes. |
| theorem_statement_protected | PASS: no theorem edits. |
| structure_gate | PASS: 3 body lines, no conjunction/branches. |
| naming_gate | PASS: mathematical descriptive name, no forbidden pattern. |
| line_packing_gate | PASS: complete measured signature table, 86 ≤ 100. |
| inequality_orientation_gate | PASS: none in signature/body; docstring already ≤. |
| exact scoped diff | PASS: Python comparison against `git show HEAD:Roth/HasseDeriv.lean` asserts file equality after precisely the one arrow substitution. All other declarations/comments unchanged. |
| dependent closure | PASS via parent-supplied completion: full `lake build`, exit 0, 2586 jobs, `/private/tmp/roth-hasseDeriv-build.log`; `lake build Roth.LeanEval`, exit 0, 2585 jobs, `/private/tmp/roth-hasseDeriv-leaneval.log`. |

## Result/checklist

Before/after: 4 declaration lines, 0 lines saved. One notation issue fixed. No rename,
generalization or decomposition candidate requiring a queue entry. Remote-search availability
is the only unresolved research limitation; it does not weaken the compiled equivalence.

- [x] Step 1: inherited reference analysis plus scoped reference verification.
- [x] Step 2: all 24 audit items, concrete dispositions.
- [x] Step 2.5: all five search methods attempted; remote failures explicit, local evidence recorded.
- [x] Step 2.6: every actual parameter inspected, inversion and literature considered.
- [x] Step 2.7: complete measured signature-width table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 golf-rule dispositions.
- [x] Step 4: strategy reflection.
- [x] Step 5a: post-edit diagnostics and module build succeeded.
- [x] Step 5b: definition equivalence and scoped diff gates passed.
- [x] Step 6a: naming acceptable, no rename queue entry required.

Worker phase complete with honest external-search limitation. Parent completed dependent
builds and retains file-wide phases, shared log update and commit/push responsibility.
