# Phase 4: `kronHasse`

Scope: `Roth/GenWronskian.lean` lines 137–138, the existing private operator only.
Read both installed SKILL.md files, full worker contract, initial GenWronskian audit,
full golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md and cleanup-gates.md; relevant style-rules.md sections on
formatting, documentation, definitions, lambdas, visibility and API design.
Existing private docstring is explicitly protected by the user; this overrides the
reference's generic private-docstring removal rule. No source comment was removed.

## Result

Before: 2 declaration lines. After: 2. Saved: 0 lines, one character.
One issue found and fixed: ordinary lambda arrow `=>` changed to `↦`.
No public declaration, signature, definition value, documentation, import, option,
helper or instance changed. No rename, generalisation, or refactoring deferred.
Source SHA256: `8489cadc516e917c45f5d291d766f7a7af7267cd0e30573df88804ceadf0e557`.
Parent revoked source ownership after the source/module/LSP handoff; remaining work
was report-only and isolated scratch verification.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No warning in lines 137–138; full-file warnings listed below. |
| 2 | HAVE SCAN | n/a: no `have` or tactic proof. |
| 3 | SET_OPTION | None; no heartbeat, recursion, debug or linter overrides. |
| 4 | SIMP SQUEEZE | n/a: no simp call. |
| 5 | NAMING | `kronHasse` is lowerCamelCase, names the Kronecker/Hasse operator; no forbidden abbreviation or numeric pattern. |
| 6 | LINE PACKING | Single signature line, measured at 93 codepoints; table below. |
| 7 | BY PLACEMENT | n/a: term-mode data definition. |
| 8 | FORMAT | Two-space body indentation; normalized lambda arrow; no empty body lines, trailing whitespace or `haveI`/`letI`. |
| 9 | COMMENTS | Existing one-line docstring preserved byte-for-byte; no body comments. |
| 10 | DOCSTRING | Protected private docstring retained under explicit user instruction. |
| 11 | VISIBILITY | Already private; used only in this module. |
| 12 | STRUCTURE | One-line term body; no conjunction or tactic branches. |
| 13 | MATHLIB | All five actual search methods below; existing aeval and Hasse APIs are constituents. |
| 14 | JUNK DEF | KEEP: named generator family of kronSpan, derivative recursion, and zero-Hasse identification; used across three declarations rather than one local proof. |
| 15 | EXISTS LEMMA | n/a: data definition, no existential result. |
| 16 | SHOW vs CHANGE | n/a: neither occurs. |
| 17 | PUSH_NEG | n/a: none occurs. |
| 18 | GENERALISE | Every actual elaborated parameter audited below; no inline change. |
| 19 | INEQUALITY | Zero reversed inequalities; arrow tokens are function types, not comparisons. |
| 20 | NORMAL-FORM | Already the pointwise function obtained by evaluating a multivariate Hasse derivative. |
| 21 | SYNTAX-GEN | OK: function-valued operator is directly usable as span generator and in pointwise derivative equations. |
| 22 | IMPORT-FANOUT | n/a: no new import. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing in diff; diff contains no cast. |
| 24 | INSTANCE-NAME | n/a: this is not an instance and introduces none. |

## Mathlib search-status

All calls used discovered native Lean MCP tools. None stalled.

| Method | Actual queries | Evidence |
|---|---|---|
| A Lean-Finder | `Kronecker substitution of multivariate Hasse derivative as function polynomial` | Returned Polynomial.hasseDeriv_apply, Polynomial.hasseDeriv and MvPolynomial.mkDerivationₗ; these concern univariate Hasse differentiation or ordinary derivations. |
| B Loogle | `MvPolynomial.aeval, MvPolynomial.hasseDeriv`; then `MvPolynomial.aeval, _ ∘ _` | First reports unknown multivariate Hasse identifier in remote mathlib index. Second returns MvPolynomial.aeval_unique, aeval_sumElim and rename_eq. No exact replacement inferred. |
| C LeanSearch | `composition of multivariate Hasse derivative with evaluation into univariate polynomial` | Returned Derivation.compAEval, compAEval_apply and compAEval_eq; ordinary derivation of univariate polynomials, different domain/operator. |
| D Source grep | Untruncated `rg -n 'kronecker|kronHasse|hasseDeriv'` on Mathlib/Algebra/MvPolynomial | No match. Read Roth/HasseDeriv.lean: multivariate Hasse derivative is the project's existing linear map over CommSemiring. |
| E Local name | `hasseDeriv`, limit 10 | Returned project MvPolynomial.hasseDeriv and its C/map/zero/apply/rename/monomial/composition API, plus mathlib Polynomial/LaurentSeries Hasse maps. Index reported unavailable while fallback returned actual items; this is not evidence of absence. |

Auxiliary variants inspected: aeval_unique, aeval_sumElim, rename_eq,
hasseDeriv_apply, hasseDeriv_hasseDeriv, map and monomial forms.
Common-equivalents table: no predicate/finiteness/topology bucket matches a
polynomial-valued operator. The six replacement rules were considered: no new
wrapper lemma or custom predicate; constituents reused directly; no exact matched
mathlib duplicate established; no module documentation change needed for this
one-character private syntax edit. Conclusion: partial matches exist (aeval and
Hasse APIs); keep the meaningful private operator used across declarations. This
is not a claim that five searches prove global mathematical absence.

## Generalisation status

`#check @kronHasse` at `format.width 100` in the isolated clone:

```lean
@kronHasse : {K : Type u_1} →
  [inst : Field K] → {σ : Type u_2} → [Fintype σ] → ℕ → (σ →₀ ℕ) →
    MvPolynomial σ K → Polynomial K
```

The source section's `l` is not an elaborated parameter of this definition.

| Parameter | Class | Mechanical candidates / precise dependency | Result |
|---|---|---|---|
| `{K : Type*}` | Type variable | Drop is not a well-formed same-type declaration: K indexes domain coefficients, result coefficients, Field and kronecker. Universe weakening already present, independent of σ. | Keep; exact original polymorphic type checked. |
| `[Field K]` | Typeclass | Drop; Field→DivisionRing; CommRing+IsField; CommSemiring considered. The unchanged public `@kronecker` takes `[Field K]`, so each body still requires that exact instance. DivisionRing alone also lacks commutative coefficient multiplication for this aeval. CommSemiring would require generalizing the public kronecker definition first. | Keep; precise constant dependency, not a claim that field axioms are mathematically minimal. No public generalisation applied. |
| `{σ : Type*}` | Type variable | Drop is ill-formed: σ indexes the input polynomial, Finsupp d and enumeration. Universes already independent/general. | Keep. |
| `[Fintype σ]` | Typeclass/data | Drop / Finite / point-localization considered. Public kronecker uses the supplied Fintype.equivFin σ; replacing by a classical Fintype.ofFinite can change which variable is assigned which exponent. A two-element enumeration swap exchanges X and X^k when k differs from 1. | Keep; enumeration data is value-relevant. A finite-type existence assertion alone does not preserve this chosen substitution. |
| `(k : ℕ)` | Structure value | Drop considered: on two variables, d=0, the variable enumerated as 1 maps to X^k, so k=1 and k=2 differ. Abstract-index exponent restatement would be a different substitution interface. | Keep: genuine value dependence; no strict/global proposition to weaken. |
| `(d : σ →₀ ℕ)` | Structure value | Drop considered: on a nonempty variable type and P=1, d=0 gives 1 whereas d=single j 1 gives 0. Changing exponent coefficient type changes the Hasse-derivative domain. | Keep: genuine operator-order dependence; no pointwise/strict proposition to weaken. |

No proposition or decidability parameter was omitted. Point-localisation,
strict→weak and bundled-proposition unbundling have no applicable parameter here.
Inversion check: n/a as a theorem extraction; this is already the defining
composition and has no proof that outruns a concrete statement.
Literature: n/a: private declaration, literature search not required.
Big-change candidates: none required. The theoretical CommSemiring extension and
bundled LinearMap presentation would require broader public API work and are not
needed for this cleanup. Optional representation redesign closed as unnecessary.

## Signature packing

Reference: definition; additionally the full implicit type was checked at width 100 above.

| Sig line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 137 | 93 | None: body follows `:=` | n/a, only one signature line | ok |

The first body token does not participate in signature packing. Existing body is
one line of 38 codepoints after normalization.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | Entire signature and parameters | No `≥` or comparison `>` | n/a | None: no `_ge_`/`_gt_` name |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no tactic wrapper. |
| 1.2 by rfl | n/a: direct data term. |
| 1.3 rw+exact | n/a: no rw. |
| 1.4 simp+exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: no tactic proof. |
| 1.6 constructor | n/a: no constructor proof. |
| 1.7 apply+exact | n/a: no apply. |
| 1.8 contradiction | n/a: no propositional contradiction. |
| 1.9 eta reduction | Lambda is not `fun P ↦ f P`: P occurs inside hasseDeriv. Composition form was independently compiled equal by rfl; retained the explicit pointwise body, avoiding needless extra Function.comp unfolding in downstream simp-only proofs. |
| 1.10 single-use have | n/a: no have. |
| 1.11 apply+intro | n/a: no apply/intro. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have projections | n/a: no have/projections. |
| 1.14 consecutive rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: no simp. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | n/a: coercions already apply the named algebra/linear maps directly. |
| 1.18 pipe | n/a: parentheses delimit the inner map application; removing them changes parsing. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial existential | n/a: data definition. |
| 2.1 grind | n/a: mathematical data construction, not a proof goal. |
| 2.2 pre-grind tactics | n/a: no tactics. |
| 2.3 simpa consolidation | n/a: no simp proof. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | n/a: no sign goal. |
| 2.6 gcongr | n/a: no inequality goal. |
| 2.7 lia/omega | n/a: no arithmetic proposition. |
| 2.8 aesop | n/a: no logic/membership proof. |
| 2.9 norm_num/norm_cast | n/a: no numeric/cast proof. |
| 2.10 decide | n/a: not a decidable proposition. |
| 2.11 field_simp/ring | n/a: no equality goal. |
| 2.12 linear_combination | n/a: no ring proof/hypotheses. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc | n/a: no calc. |
| 2.15 multi-goal close | n/a: no generated goals. |
| 3.1 erw | n/a: none. |
| 3.2 legacy analytic tactics | n/a: none. |
| 3.3 omega→lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | n/a: private function construction; no new lemma needed. |
| 3.6 simp_all | n/a: none. |
| 3.7 option removal | n/a: no local options. |

Step-back reflection: already one direct term. Automation/exact?/apply? would search
for arbitrary data and cannot improve the intended mathematical value; no proof
search is applicable. Composition is definitionally equal (compiled probe), but
there is no need to redesign the function-valued span generators as bundled
maps or replace the shared operator with repeated expressions. Kept its body,
changing only the lambda syntax.

## Verification and diff gates

Worker diff against `/private/tmp/roth-kronHasse-start.lean` is exactly:

```diff
-  fun P => kronecker k (hasseDeriv d P)
+  fun P ↦ kronecker k (hasseDeriv d P)
```

`lake build Roth.GenWronskian` session 80469 exited 0, built module in 17 seconds,
1838 jobs complete. Complete native `lean_diagnostic_messages` after edit:
`success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`,
zero errors, no warnings within target. All five full-file warnings retained:

1. L1 missing authoritative copyright metadata (user-preserved).
2. L36 unused Fintype section parameter in dependent-zero theorem.
3. L32 unused Fintype in that theorem's type.
4. L224 unused DecidableEq in det_sum_rows.
5. L242 unused Fintype in final existence theorem.

No suppression was added and no outside declaration was changed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build session80469 exit0. |
| definition_protected | pass | Signature unchanged, value definitionally identical; only authorized routine lambda syntax normalized. |
| theorem_statement_protected | pass | No theorem statement touched. |
| structure_gate | pass | One body line; no conjunction/branch. |
| naming_gate | pass | No forbidden name pattern/abbreviation. |
| line_packing_gate | pass | Complete 93-codepoint signature row above. |
| inequality_orientation_gate | pass | Explicit empty occurrence table above. |
| comments/documentation | pass | Existing docstring and all other comments byte-identical. |

Overall: pass. Parent owns cumulative full-build and separate LeanEval gates.

## Independent checking

The exact current source was cloned to `/private/tmp/roth-kronHasse-probes.lean`
so the existing private constant is accessible in its original file context.
The clone is outside the repository and adds checks only. The original full
polymorphic type is assigned directly to `@kronHasse`. `originalValue` proves
equality to the ORIGINAL pre-worker lambda expression by rfl.
`independentReconstruction` proves the operator agrees with aeval applied to
the explicit Hasse-coefficient monomial sum, via existing hasseDeriv_apply.
`compositionCandidate` independently verifies the composition option by rfl.
Final `lake env lean /private/tmp/roth-kronHasse-probes.lean` session73690
exited 0. All three check theorems report exactly
`[propext, Classical.choice, Quot.sound]`; no sorryAx or nonstandard axiom.
The initial isolated tail needed `open MvPolynomial` after reopening namespace
Roth; that scratch-only namespace issue was corrected before the successful run.

## Required 11-step checklist

- [x] Step 1: reference documents read.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: five actual search methods recorded.
- [x] Step 2.6: all elaborated parameters audited, precise dependencies/counterexamples recorded.
- [x] Step 2.7: every signature line measured.
- [x] Step 2.8: per-occurrence inequality table recorded.
- [x] Step 3: all 42 rule statuses recorded.
- [x] Step 4: step-back reflection and composition alternative considered.
- [x] Step 5a: complete LSP clean of errors, all warnings retained.
- [x] Step 5b: diff-gate table recorded with actual module build.
- [x] Step 6a: no rename needed; no sidecar mutation.

Renames queued: none. Comments preserved: 1 of 1 protected docstring.
Refactoring needed: none.
