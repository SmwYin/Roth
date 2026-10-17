# Fresh ORIGINAL d6 audit: `Roth.coeffNone`

Initial audit recorded before any source edits. Scope: only the original public noncomputable
definition at lines 73–74 of `Roth/Separation.lean`. Decision: retain its exact type, value,
visibility and documentation. No source change is proposed or applied.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, together with the Lean and mathlib-quality
skills, cleanup Phase 4, style/naming/profiling references. This definition returns data and
already uses direct term mode. The semantic coefficient operation has a surrounding API:
`coeff_coeffNone`, `eq_sum_X_none_pow_mul_coeffNone`, `degreeOf_coeffNone_le`, and repeated
uses in `exists_separated_representation`. One-line size alone does not make it junk.

## Initial 24-item audit

1. LINT: target-range diagnostics pending final complete LSP gate; baseline dispatch has
   0 errors / 31 warnings for the complete module.
2. HAVE SCAN: no `have`; value is a single coefficient projection.
3. SET_OPTION: none in target.
4. SIMP SQUEEZE: no simp invocation.
5. NAMING: `coeffNone` is descriptive lowerCamelCase for data, naming the distinguished
   `none` variable; accepted `coeff` matches `Polynomial.coeff`; no forbidden abbreviation,
   numerical prefix or single-letter public name. No rename needed.
6. LINE PACKING: signature is 89 characters; continuation value is 33 characters. Width
   table and exact measurements are recorded below; the value cannot fit on the signature.
7. BY PLACEMENT: n/a: term-mode data definition has no `by`.
8. FORMAT: two-space value indent; no blank line, tactic, semicolon or instance binder hack.
9. COMMENTS: exact two-line docstring and source attribution preserved; no inline comments.
10. DOCSTRING: existing description explains coefficient extraction and remaining variables;
    source quotation identifies collecting powers of the distinguished variable. Preserved.
11. VISIBILITY: public semantic API, explicitly protected by dispatch; retain public.
12. STRUCTURE: two declaration lines, one value expression, no proof branches or conjunction.
13. MATHLIB: five-method searches locate `optionEquivLeft` and its coefficient API; target
    already builds directly on them. This is a named data operation, not a wrapper theorem.
14. JUNK DEF: retain: coefficient/expansion/degree API plus multiple meaningful uses.
15. EXISTS LEMMA: n/a: data definition, no existential lemma.
16. SHOW vs CHANGE: n/a: no `show`.
17. PUSH_NEG: n/a: no negation tactics.
18. GENERALISE: effective binders are `{τ}`, `{R}`, `[CommSemiring R]`, `P`, `ν`;
    `Fintype τ` and `DecidableEq τ` are absent from compiled type. Detailed probes below.
19. INEQUALITY: no inequalities in definition signature or value; table below.
20. NORMAL-FORM: canonical polynomial coefficient after `MvPolynomial.optionEquivLeft`;
    no alternate predicate or pairwise equivalence API introduced.
21. SYNTAX-GEN: explicit polynomial and exponent are natural call-site arguments; a bundled
    linear map is possible additional API, but no downstream need justifies changing this API.
22. IMPORT-FANOUT: n/a: no added imports.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing in diff; empty source diff.
24. INSTANCE-NAME: n/a: definition, not instance.

Issues to fix: none established. Refactoring needed: none for this definition. Public
12-theorem instance proposal remains PENDING and outside this declaration's authorization.

## Five actual mathlib searches

Raw native results: `/private/tmp/roth-separation-d06-{finder,loogle,leansearch,names}.json`.
Source results: `/private/tmp/roth-separation-d06-source-search.log` (untruncated).

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | multivariate polynomial coefficient in one distinguished variable as multivariate polynomial in remaining variables | `MvPolynomial.coeff`, `lcoeff`, `lcoeff_apply`, `coeff_single_X`, `finSuccEquiv_coeff_coeff` |
| B Loogle | `MvPolynomial.optionEquivLeft` | `optionEquivLeft`, natDegree/support and generator images |
| C LeanSearch | MvPolynomial Option coefficient polynomial optionEquivLeft | `optionEquivLeft_coeff_coeff`, `optionEquivLeft_coeff_some_coeff_none`, `optionEquivLeft_X_some`, support coefficient API |
| D Source | full `def coeffNone`; `optionEquivLeft.*coeff`; `coeff.*optionEquivLeft` | existing equivalence and its coefficient/support/degree API in `Mathlib/Algebra/MvPolynomial/Equiv.lean`; no exact-name definition found in this bounded source scope |
| E Name pattern | `optionEquivLeft`, limit 20 | 17 source-backed matches, including all needed operations; index unavailable, so empty results would not prove absence |

Auxiliary variants inspected: `finSuccEquiv_coeff_coeff`, `lcoeff`, generator images,
`optionEquivLeft_coeff_some_coeff_none`, support and degree variants. Common-equivalents
table has no relevant topology/finiteness/bornology bucket. Conclusion: partial library
match; retain the semantic definition built directly on `optionEquivLeft` and
`Polynomial.coeff`. Their exact types were compiled with `#check` (signature JSON).
No claim that this function is absent from every generic or generated mathlib route.
The no-wrapper-lemma rules do not justify deleting a public data operation with this API.
No new definition, custom predicate, bridge theorem or import was introduced. Therefore
the compiled absence probe prerequisite for *introducing* a supposedly missing result
does not arise. An `exact?` test for this data return type could simply produce zero and
would not establish equality with the prescribed value; independent value recovery is the
meaningful test here.

## Generalisation: every effective binder

Compiled `#check @Roth.coeffNone` (native signature JSON and actual-built axiom log) gives:

```lean
{τ : Type u} → {R : Type v} → [CommSemiring R] →
  MvPolynomial (Option τ) R → ℕ → MvPolynomial τ R
```

| Binder | Class | Use / candidate | Verification / decision |
|---|---|---|---|
| `{τ : Type u}` | type variable | Variable type used in input, output and equivalence; drop test; independent universes | Drop fails unknown τ; independent u/v recovery compiles; already universe polymorphic |
| `{R : Type v}` | type variable | Coefficient type in input, output, equivalence; drop test | Drop fails unknown R; no special coefficient ring fixed |
| `[CommSemiring R]` | algebra typeclass | Required by optionEquivLeft and MvPolynomial API; drop and Semiring parent test | Both fail synthesizing CommSemiring R; retain |
| `(P : MvPolynomial (Option τ) R)` | structure value | The polynomial from which coefficient is extracted; drop test | Drop fails unknown P; arbitrary value type changes mathematical operation |
| `(ν : ℕ)` | value | Polynomial exponent for coeff; drop test | Drop fails unknown ν; arbitrary ordered exponent changes polynomial representation rather than weakening an assumption |
| `[Fintype τ]` in surrounding section | not effective | Definition elaborator excludes unused section instances automatically | Compiled actual type and independent recovery have no Fintype/Finite; no omission edit required |
| `[DecidableEq τ]` in surrounding section | not effective | Definition elaborator excludes unused section instances automatically | Actual type and recovery have no DecidableEq; no classical local instance edit required |

Raw independently compiled variants: `/private/tmp/roth-separation-d06-binder-probes.json`.
No proposition/function-property assumption exists, so strict→weak, point localisation,
bijective unbundling and analytic typeclass weakenings are inapplicable. Inversion check:
n/a, typeclass-parametric data operation, no concrete witness theorem or unfolding proof.
No successful further weakening, public restatement or new helper is proposed.

## Public literature search

Actual web queries: (1) `site.stacks.math.columbia.edu polynomial ring R[x_1 x_n]
R[x_1 x_n-1][x_n] coefficients`; (2) `site.mathlib.org MvPolynomial optionEquivLeft
coefficient`; (3) `polynomial ring iterated polynomial ring arbitrary set variables
commutative semiring coefficients generalization`.

Relevant top results retained: the [mathlib equivalence documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Equiv.html),
the [mathlib multivariate polynomial phrasebook](https://leanprover-community.github.io/mathlib-phrasebook/Polynomials/Multivariate-polynomials/),
and [Stacks Lemma 10.115.2](https://stacks.math.columbia.edu/tag/051N). The first documents
the exact arbitrary-variable commutative-semiring equivalence underlying this definition;
the phrasebook supports arbitrary variable types. Stacks discusses a polynomial regarded
in one selected variable over the others, but its ring hypothesis is stronger, so it does
not furnish a weakening. The third query's top three results were Wikipedia Polynomial
ring, Encyclopedia of Mathematics Polynomial ring, and Alphabeta Polynomial Rings; these
were search leads only, not authority for a code change. Native math ChatGPT MCP is not
available (`ALL_TOOLS` contains no matching tool), recorded as unavailable rather than a
negative mathematical conclusion. Local source `clean.tex:374` explicitly collects powers
of x_p, confirming the existing docstring's semantic role. No literature-driven public
change candidate emerged; current τ-general and semiring-general formulation is broader
than the local rational-polynomial application.

## All 42 golf rules

Every n/a below is structural, not an unperformed tactic test: this is a data definition
whose exact prescribed value is already a single direct term. Replacing it by proof
automation on the inhabited return type would not preserve that value.

| Rule | Concrete status |
|---|---|
| 1.1 remove by exact | n/a: no tactic wrapper |
| 1.2 remove by rfl | n/a: no rfl wrapper |
| 1.3 rw + exact → rwa | n/a: no rw or exact |
| 1.4 simp + exact → simpa | n/a: no simp or exact |
| 1.5 trailing rfl after simp | n/a: no simp/rfl chain |
| 1.6 anonymous constructor | n/a: no constructor proof |
| 1.7 apply + exact | n/a: no apply |
| 1.8 by_contra! | n/a: no contradiction reasoning |
| 1.9 eta reduction | n/a: no written lambda; two explicit inputs provide public API |
| 1.10 inline have | n/a: no have |
| 1.11 refine + fun | n/a: no apply/intro chain |
| 1.12 redundant show | n/a: no show |
| 1.13 obtain tuple | n/a: no have/projections |
| 1.14 merge rw | n/a: no rewrite |
| 1.15 terminal simp unsqueeze | n/a: no simp |
| 1.16 nonterminal simp squeeze | n/a: no simp |
| 1.17 dot notation | satisfied: `.coeff ν` projection already used |
| 1.18 use <\| | n/a: parentheses around equivalence application are needed for `.coeff` receiver; no trailing lambda/tactic parentheses |
| 1.19 push Not | n/a: no negation tactic |
| 1.20 inline existential helper | n/a: no existential or private helper |
| 2.1 grind | n/a: direct data value, no multi-line proof goal |
| 2.2 delete before grind | n/a: no tactics |
| 2.3 simpa consolidation | n/a: no simplifier chain |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability proposition |
| 2.5 positivity | n/a: no order proposition |
| 2.6 gcongr | n/a: no inequality proposition |
| 2.7 lia/omega | n/a: exponent parameter is data, no arithmetic goal |
| 2.8 aesop | n/a: no logic/membership proof |
| 2.9 norm_num/norm_cast | n/a: no numeric computation or cast proof |
| 2.10 decide | n/a: output is MvPolynomial, not a decidable proposition |
| 2.11 field_simp; ring | n/a: no denominator identity proof |
| 2.12 linear_combination | n/a: no ring proof or hypotheses |
| 2.13 wlog | n/a: no branches or symmetry proof |
| 2.14 collapse calc | n/a: no calc |
| 2.15 <;> | n/a: no tactic-generated subgoals |
| 3.1 erw → rw | n/a: no erw |
| 3.2 fun_prop over legacy | n/a: no legacy continuity/measurability tactics |
| 3.3 omega → lia | n/a: no omega |
| 3.4 rcases rfl | n/a: no case analysis |
| 3.5 automation attributes | n/a: data definition, no proposition to register; no global unfolding attribute justified |
| 3.6 simp_all | n/a: no simp_all |
| 3.7 remove limits | satisfied: no local/global limit introduced or target limit present |

## Width and inequality tables

Codepoint measurements (not byte lengths):

| Source line | Kind | Width | Next item | Arithmetic / result |
|---|---|---:|---|---|
| 73 | full signature including `:=` | 89 | no remaining signature token; value is 31 chars without indent | complete signature; 89 + 1 + 31 = 121 > 100, so value stays below |
| 74 | value (included for completeness) | 33 | none | one value line, two-space indent |

Actual `format.width 100` signature output is in signature JSON and built axiom log.

| Scope | Occurrences of ≥ or > | Other inequalities | Action |
|---|---:|---:|---|
| signature / effective binders | 0 | 0 | no orientation rewrite |
| value expression | 0 | 0 | no orientation rewrite |
| target name | 0 `_ge_` / `_gt_` | n/a | no inequality rename |

## Step-back / simplify review

The operation selects the ν-th coefficient under the standard equivalence, exactly
expressing the polynomial in one variable with coefficients in the others. There is no
proof strategy to replace or hidden extraction opportunity. Its named semantic API avoids
repeating that representation in expansion and degree results; removing it would change
the public definition and document surface, expressly outside authorization. No narrower
notation, map bundle or helper is needed. No new helper was added, so no independent-helper
audit is due. Built-in `/simplify` is unavailable among installed skills/tools; the
substantive direct review above performs the required simplification check without
inventing an invocation. Suggestions applied: none. Suggestions pending: none for target.

## Verification gates and performance

| Gate | Outcome | Evidence |
|---|---|---|
| lake_build_file | PASS | `/Users/ramin/.elan/bin/lake build Roth.Separation`, exit 0, `/private/tmp/roth-separation-d06-build.log` |
| complete unfiltered LSP | PASS | native `lean_diagnostic_messages`, partial=false, timed_out=false, failed_dependencies=[], 0 errors / 31 warnings / 0 infos; `/private/tmp/roth-separation-d06-final-lsp.json` |
| target lint | PASS | no diagnostic at lines 73–74; existing warnings belong to preserved header or other declarations |
| definition_protected | PASS | target docstring, signature and value byte-identical to ORIGINAL; `/private/tmp/roth-separation-d06-record.json` |
| theorem_statement_protected | PASS | empty source diff; no theorem touched |
| structure_gate | PASS | two code lines: one signature and one value, no proof branch/conjunction |
| naming_gate | PASS | descriptive lowerCamelCase; no forbidden pattern/abbreviation |
| line_packing_gate | PASS | full signature fits at 89 codepoints; table above; no remaining signature token |
| inequality_orientation_gate | PASS | zero relevant inequalities; table above |
| no unsafe constructs/scaffolding | PASS | no source diff; no new sorry, axiom, native_decide, options, haveI/letI, trace, import or helper |
| independent ORIGINAL type/value | PASS | `/private/tmp/roth-separation-d06-independent.lean` imports only Mathlib.Algebra.MvPolynomial.Equiv, reconstructs same type and prescribed value independently of target; `lake env lean` exit 0, `.log` |
| actual built target/value/axioms | PASS | `/private/tmp/roth-separation-d06-axioms.lean`, `lake env lean` exit 0; actual `#print` and rfl value equality; `.log` shows only propext, Classical.choice, Quot.sound |
| actual target profile | PASS | unchanged actual module baseline `/private/tmp/roth-separation-d05-final-profile.log{,.json}`: command at log L53293 = 12.094ms, zero async proof anchors, conservative total 12.094ms <750ms and <1000ms |
| diff arithmetic | PASS | `git diff --numstat -- Roth/Separation.lean` empty and `git diff --check` exit 0; `wc -l -c` 602 / 31114, unchanged |
| cumulative whole project / separate LeanEval | parent-owned | dispatch supplies green baseline; parent runs sequential final builds and whole-original compatibility after freeze; no duplicate full-original probe performed |

The independent scratch harness initially failed because a data-valued example needed
noncomputable section, then because the added anonymous section required its own `end`.
Those harness errors were fixed only in `/private/tmp`, and the final command exits 0.
Initial logs retained as `...-independent-initial-failure.log` and
`...-independent-section-failure.log`; neither is counted as a passing test. No source
failure or change resulted. Binder tests completed: base exit 0, six intended negative
tests exit 1 with exactly the dependency errors reported in the table. No untested
negative test is represented as compiler-verified.

No changed declaration needs a fresh performance run: supplied trace was generated for
the exact current actual module by `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Separation.lean`. Only the target's outer command is
counted; no nested profiler nodes are added. No project-wide speedup is claimed.

## Result and eleven required completion steps

Before 2 code lines; after 2; saved 0 (0%). Audit issues established 0; fixed 0;
target refactoring deferred 0. Rules applied: none; 1.17 already satisfied. Existing
two-line documentation preserved verbatim. No rename queued; no new helper; no source
edit. Retaining an already suitable semantic definition is the applied audit result.

| Required step | Status / artifact |
|---|---|
| 1: references | complete: full required docs plus relevant style, naming, profiling |
| 2: all 24 audit items | complete: initial audit before any source mutation (none made) |
| 2.5: five search methods | complete: actual native/source results and query table |
| 2.6: generalisation | complete: every effective binder, section-instance exclusion, actual negative tests and public literature |
| 2.7: signature width | complete: codepoint table, actual format.width 100 output |
| 2.8: inequality scan | complete: zero-occurrence table, name checked |
| 3: all 42 golf rules | complete: separate status for every rule; proof-only rules concretely inapplicable to direct data value |
| 4: step-back reflection | complete: semantic/API necessity and simplify review above |
| 5a: module LSP | complete: unfiltered, nonpartial 0 errors / 31 warnings |
| 5b: diff gates | complete: gate table plus module/independent/value/axiom/profile evidence |
| 6a: rename disposition | complete: none needed, no shared sidecar mutation |

Overall workflow disposition: doctor uses parent's green full/module/LeanEval baseline;
prepare/audit complete; file-level edits none; deep cleanup complete; non-rename
refactoring none; renames none; worker final verification complete; simplify reviewed;
buzz satisfied with valid unchanged actual-module trace; report complete. Parent retains
final full-project, LeanEval, compatibility, exact-path publication and push responsibility.

## Source freeze and ownership handoff

All my Lean/MCP/compiler/profile requests have returned; no outstanding request, process
or source edit remains. I explicitly revoke ALL source ownership, including this target,
the surrounding file, substitutions and any other source. I am report-only from this
freeze onward. Source SHA256:
`c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`.

Pending proposal: `.mathlib-quality/cleanup/Separation-instance-proposal.md` remains
PENDING for the existing 12 public theorems; no public omission/type/value/docs/visibility
change is applied or authorized by this d6 audit. No Git/shared-log mutation was made.

## Owner cumulative publication gates

Source FROZEN SHA256 `c6488cc1c5738d1f9e69b7267a0ad182c823f7bacd02c347e644d710ff559c3f`; leaf ownership revoked and requests drained before owner gates. Owner probe `43989` exit0,34.00s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d06-compatibility.{lean,log,json}`. Owner build session `69566` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,5.86s/2.87s; source hash stable. `/private/tmp/roth-separation-d06-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
