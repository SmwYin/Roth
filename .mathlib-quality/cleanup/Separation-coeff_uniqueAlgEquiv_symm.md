# Fresh audit: Roth.coeff_uniqueAlgEquiv_symm (original declaration 17)

Initial audit written before any source edit. Scope: Roth/Separation.lean:156–158, original snapshot:228–230. The proof identifies the unique variable’s exponent and applies mathlib’s arbitrary-exponent coefficient formula.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md; also Lean4/mathlib-quality skills, cleanup Phase 4, style/naming/profiling references. Original public effective type and documentation are protected by dispatch.

## Full 24-item audit

| # | Item | Concrete result |
| --- | --- | --- |
| 1 | LINT | No target warning in baseline; complete fresh unfiltered LSP required below. |
| 2 | HAVE SCAN | No have in the one-line proof. |
| 3 | SET_OPTION | No local options or limits. |
| 4 | SIMP SQUEEZE | No simp in original; one terminal rw. |
| 5 | NAMING | Descriptive coefficient/unique algebra equivalence/inverse name; no forbidden abbreviations, numeric scheme or single-letter name. No rename necessary. |
| 6 | LINE PACKING | Two signature lines; measured table below. |
| 7 | BY PLACEMENT | by ends the conclusion line. |
| 8 | FORMAT | Two-space indentation, single tactic, no internal blanks or instance tactics. |
| 9 | COMMENTS | No inline proof comments. Both existing docstring lines preserved exactly. |
| 10 | DOCSTRING | Existing source §5 Lemma 6 citation and interpretation retained. |
| 11 | VISIBILITY | Original public contract retained; public wrapper deletion requires compiled proposal and approval. |
| 12 | STRUCTURE | One-line proof, no conjunction/branches; no decomposition. |
| 13 | MATHLIB | Direct specialization of MvPolynomial.coeff_uniqueAlgEquiv_symm and Finsupp.single_eq_same; five actual searches recorded below. |
| 14 | JUNK DEF | Theorem, not data definition. |
| 15 | EXISTS LEMMA | Public coefficient equality, no existential helper. |
| 16 | SHOW vs CHANGE | No show. |
| 17 | PUSH_NEG | No push_neg. |
| 18 | GENERALISE | Every effective binder and weakening probed below; no public statement change authorized. |
| 19 | INEQUALITY | Zero comparison operators; explicit occurrence table below. |
| 20 | NORMAL-FORM | Coefficient equality already canonical. Mathlib generalizes from singleton exponent to arbitrary finitely supported exponent. |
| 21 | SYNTAX-GEN | Explicit polynomial and exponent convenient for rewriting; broader mathlib theorem already exists. |
| 22 | IMPORT-FANOUT | No import needed. |
| 23 | CASTS | No coercions or ascriptions in proof, no diff casts. |
| 24 | INSTANCE-NAME | Not an instance declaration. |

Issues to fix: none established. Pending investigation: compile direct mathlib replacement as optional public deletion proposal; retain theorem until approval. No helper planned.

## Five actual search methods and six-rule decision

| Method | Actual evidence |
| --- | --- |
| A Lean Finder | Semantic query `coefficient of univariate polynomial under inverse uniqueAlgEquiv at single default exponent` returned related pUnit equivalence/monomial lemmas. `/private/tmp/roth-separation-d17-finder.json`. |
| B Loogle | `MvPolynomial.uniqueAlgEquiv`, eight hits including coefficient formula and inverse evaluation formulas. `/private/tmp/roth-separation-d17-loogle.json`. |
| C LeanSearch | `coefficient uniqueAlgEquiv inverse single default`, returned algebra equivalence infrastructure. `/private/tmp/roth-separation-d17-search.json`. |
| D Source search | Full untruncated `rg -n coeff_uniqueAlgEquiv_symm Roth .lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Equiv.lean` finds exact broader theorem at Equiv.lean:115–118. Its RHS is `P.coeff (d default)` for arbitrary `d`. Source neighbourhood and inverse-evaluation alternatives checked. |
| E Native local search | `coeff_uniqueAlgEquiv`, positive hits for exact MvPolynomial theorem and related monoid algebra lemmas. Index warming; positive source hits verified with compiled #check. `/private/tmp/roth-separation-d17-local.json`. |

No absence claim. Rules 1/5 identify an optional public-wrapper deletion, compiled as
an isolated full-module proposal. Original public contract preservation takes precedence
until approval, so theorem retained. Rule 2: five methods actually run, positive generic
compiled application below. Rule 3: coefficient/inverse/monomial/evaluation alternatives
checked. Rule 4: already typeclass formulation, no custom predicate. Rule 6: document
mathlib usage here; source module docs are user-preserved. Common-equivalents table:
no hidden topological, compactness, bornological or discreteness condition.

## Actual literature search and generalisation

Actual web query `polynomial ring one variable coefficients commutative semiring universal property`.
Primary author-hosted textbook found and opened: W. Frank Moore, Mark Rogers, Sean
Sather-Wagstaff, *Monomial Ideals and Their Decompositions*, Appendix A.2,
[author-hosted PDF](https://ssather.people.clemson.edu/DOCS/monomial.pdf).
Theorem A.2.1 and Definition A.2.2 describe coefficient sequences and independence
of monomials; Corollary A.2.6 treats the multivariable counterpart. This supports the
coefficient identification interpretation; the textbook's commutative-ring presentation
is stronger than the current commutative-semiring theorem. No weaker hypothesis or
new mathematical claim inferred from the textbook. Mathlib already states the broader
arbitrary-exponent version. Original Roth source citation unchanged. No claim to have
located the precise Roth manuscript in this search.

All effective binders were actually tested in native isolated code under
`autoImplicit false`. Full code `/private/tmp/roth-separation-d17-binder-probes.lean`,
complete native response `/private/tmp/roth-separation-d17-binder-probes.json`;
completed, timed_out=false. Negative probes deliberately fail elaboration and were
never applied to repository source.

| Effective binder | Actual candidate(s) | Compiler result / decision |
| --- | --- | --- |
| `{R : Type*}` | Drop R | Unknown R in instance, polynomial and equivalence. Already universe polymorphic. |
| `[CommSemiring R]` | Drop; weaken to `[Semiring R]` | Drop fails Semiring and CommSemiring synthesis; weaker parent fails CommSemiring synthesis at uniqueAlgEquiv. No use of subtraction or field assumptions to weaken. |
| `{σ : Type*}` | Drop σ | Unknown σ in Unique and equivalence. Already universe polymorphic. |
| `[Unique σ]` | Drop; weaken to `[Inhabited σ]`; unbundle to Inhabited + Subsingleton | Each fails Unique synthesis for existing uniqueAlgEquiv API. Unbundling needs explicit derived Unique construction, offering no strictly weaker mathematical content. |
| `(f : Polynomial R)` | Drop f | Unknown f and f.coeff; data argument essential. |
| `(n : ℕ)` | Drop n | Unknown n twice; natural exponent essential to polynomial monomials. |

Original effective type excludes section τ/Fintype τ/DecidableEq τ, confirmed by
compiled #check. No unused section instance in this target to omit. No pointwise/global,
strict/weak, nonzero/domain/field or conjunction hypothesis occurs. Inversion check:
a more general exponent `d : σ →₀ ℕ` already exists in mathlib; the proof is precisely
its specialization. No new helper or public generalisation applied. Tool inventory
contains no chatgpt-math tool; literature handled by actual web search.

## Signature width and inequality gates

Actual `set_option format.width 100; #check @Roth.coeff_uniqueAlgEquiv_symm`:

```lean
@Roth.coeff_uniqueAlgEquiv_symm : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} [inst_1 : Unique σ]
  (f : Polynomial R) (n : ℕ), ((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n
```

Widths measured in codepoints, not bytes. Keep the complete LHS application together
as the next expression unit; moving it to the binder line would exceed 100.

| Signature line | Width | Next signature expression unit | Arithmetic | Action |
| --- | --- | --- | --- | --- |
| 156 | 85 | LHS application `((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n)`, 62 | 85 + 1 + 62 = 148 > 100 | ok |
| 157 | 84 | None: proof body follows | n/a | ok |

| Occurrence | Location | Original | Rewrite | Rename |
| --- | --- | --- | --- | --- |
| 0 | Full signature, every effective hypothesis and proof | No ≥, >, ≤ or < | None | No _ge_/_gt_ in name |

## All 42 golfing rules

| Rule | Concrete status |
| --- | --- |
| 1.1 by exact | No exact-wrapper in existing single rw proof. |
| 1.2 by rfl | Goal needs theorem and singleton formula, not whole-goal reflexivity. |
| 1.3 rwa | No rw/exact sequence: rw already closes. |
| 1.4 simpa using | Corrected typed mathlib specialization compiles independently; longer than existing rw proof, retained as removal replacement evidence. |
| 1.5 trailing rfl | No trailing rfl. |
| 1.6 anonymous constructor | No constructor. |
| 1.7 exact application | Direct exact tested, initially omitted explicit R; corrected R still needed σ annotation. Independent fully typed simpa compiled; no shorter exact proof established. |
| 1.8 by_contra! | No contradiction or negation. |
| 1.9 eta reduction | No lambda. |
| 1.10 inline have | No have. |
| 1.11 refine fun | No intro or apply. |
| 1.12 redundant show | No show. |
| 1.13 obtain projections | No pair/existential projections. |
| 1.14 merge rw | Already exactly one rw with two lemmas. |
| 1.15 unsqueeze terminal simp | No original simp. Bare simp with formula actually fails by unfolding equivalence before formula can fire. |
| 1.16 squeeze nonterminal simp | No nonterminal simp. |
| 1.17 dot notation | No receiver-based application to shorten. |
| 1.18 parentheses | No trailing tactic/lambda parentheses. Statement parentheses encode applications and remain exact. |
| 1.19 push Not | No push_neg. |
| 1.20 inline existential | Public equality, no private witness lemma. |
| 2.1 grind | Actual live `grind [MvPolynomial.coeff_uniqueAlgEquiv_symm, Finsupp.single_eq_same]` closes without diagnostics; longer and less direct than existing rw. |
| 2.2 delete before grind | No preceding tactic and no existing grind. Whole-goal grind already tested. |
| 2.3 simpa consolidation | Typed specialization compiles, but no preceding simp/closing chain to consolidate. |
| 2.4 fun_prop | No analytic function property. |
| 2.5 positivity | No ordered, positivity or nonzero goal. |
| 2.6 gcongr | No inequality or monotonicity. |
| 2.7 lia/omega | No integer/natural arithmetic goal, exponent merely indexes coefficients. |
| 2.8 aesop | Actually tried at live whole proof; failed with unsolved eval₂ coefficient equality. |
| 2.9 norm_num/norm_cast | No concrete numeric/cast computation. |
| 2.10 decide +kernel | Arbitrary symbolic polynomial coefficient equality not finite decidable computation. |
| 2.11 field_simp/ring | No denominator, field structure or ring identity to normalize. |
| 2.12 linear_combination | No ring/ring_nf ending or algebraic hypotheses. |
| 2.13 wlog | No case branches. |
| 2.14 collapse calc | No calc. |
| 2.15 multiple goals | Existing rw directly closes a single goal. |
| 3.1 erw to rw | Already rw. |
| 3.2 legacy fun_prop | No continuity/measurability tactic. |
| 3.3 omega to lia | No omega; arithmetic inapplicable as 2.7 records. |
| 3.4 rcases rfl | No rcases. |
| 3.5 automation attributes | No attribute added: broader mathlib formula already exists; avoid overlapping specialized rewrite registration. |
| 3.6 simp_all | No contextual simp_all chain. |
| 3.7 heartbeat limits | None present or added. |

Raw live experiments: `/private/tmp/roth-separation-d17-attempts.json` and
`/private/tmp/roth-separation-d17-attempts-corrected.json`. `exact?` was actually
tried and failed. Two correction rounds expose argument-inference requirements;
those failures are not reported as successful proofs. Positive complete-snippet
native and CLI proof below supplies both explicit R and σ.

## Step-back review

Existing proof already is a single tactic with two established API facts and no
intermediate state, casts, duplicate proof skeleton or helper opportunity. Generic
mathlib arbitrary-exponent formula is the right abstraction. The native simp and
aesop alternatives fail, grind succeeds but is longer, and simpa specialization
is longer. Keep the original direct rw proof under the minimum-value filter.
No source edit is warranted. Holistic simplify pass: PASS-THROUGH, no remaining
proof simplification identified. No new private helper needs an additional audit.

## Concrete public deletion proposal (pending, unapplied)

The public theorem is a wrapper around mathlib. The concrete replacement proof is:

```lean
by
  simpa using
    MvPolynomial.coeff_uniqueAlgEquiv_symm R (σ := σ) f (Finsupp.single default n)
```

Full current-module copy with ONLY this public theorem and its two-line docstring
removed: `/private/tmp/roth-separation-d17-delete-proposal.lean`, compiled exit 0;
raw log `/private/tmp/roth-separation-d17-delete-proposal.log`. Repository-wide
untruncated search finds no use of the Roth wrapper; other source uses explicitly
qualify MvPolynomial. Therefore proposal requires no caller substitutions. This
is a compiled proposal, not an applied API deletion. Parent notified before any
application; no approval assumed. Exact original public theorem and documentation
retained. Existing 12-theorem instance omission and aeval_X_eq_rename deletion
proposals also remain pending and unapplied.

## Verification and gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, full raw
`/private/tmp/roth-separation-d17-build.log`, `Build completed successfully (1876 jobs)`.
Complete unfiltered native module LSP: `/private/tmp/roth-separation-d17-final-lsp.json`,
partial=false, timed_out=false, success=true, failed_dependencies=[], 0 errors,
31 warnings, 0 infos. All warnings retained in raw response; none in target range.
Header warning is user-preserved metadata; other warnings concern pending public
instance omissions. No warning suppression introduced.

Isolated exact ORIGINAL effective type assignment and independent non-self proof:
`/private/tmp/roth-separation-d17-independent.lean`, native response
`/private/tmp/roth-separation-d17-independent-native.json` reports success=true,
timed_out=false. Native scratch has one whitespace warning for a leading space
before its independent theorem keyword, unrelated to repository source. Built CLI
repeat exited 0: `/private/tmp/roth-separation-d17-independent-final.log` contains
both expected signatures and exactly `[propext, Classical.choice, Quot.sound]`
for independent proof AND actual built `Roth.coeff_uniqueAlgEquiv_symm`.
No affected private declaration or caller: source unchanged. Earlier failed
inference experiment log `/private/tmp/roth-separation-d17-independent.log` is
superseded by the final log and explicitly NOT used as a successful gate.

| Gate | Result | Evidence |
| --- | --- | --- |
| lake_build_file | Pass | Actual module build exit 0. |
| definition_protected | Pass | No source diff or definition edit. |
| theorem_statement_protected | Pass | Entire original target block byte-identical; exact original effective type assignment compiles. |
| structure_gate | Pass | One proof-body line; no conjunction or branch. |
| naming_gate | Pass | Descriptive coefficient/inverse equivalence name; no forbidden pattern or abbreviation. |
| line_packing_gate | Pass | Both measured signature rows ok, full expression unit cannot share first line. |
| inequality_orientation_gate | Pass | Explicit zero-occurrence table above. |
| cumulative_no_unintended_external_breakage | Target/module pass | Parent owns cumulative original30/public20/all-retained-axiom and sequential full project + separate LeanEval checks after freeze. |

No rename needed or sidecar edit. No imports, pins, limits, attributes, instances,
public binders, documentation or proof narratives changed. No `sorry`, custom
axiom, native_decide, haveI/letI or profiler scaffold introduced in repository.
Expected failures in isolated negative probes are not successful theorem artifacts.

## Actual-module profile and size arithmetic

Source target unchanged, so dispatch-authorized valid actual-module profile reuse:
`/private/tmp/roth-separation-d16-final-profile-fixed.log`, parsed using
`/private/tmp/roth-separation-profile-table.py` into same log name plus `.json`.
Actual original command:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Anchors: line 186404 `[Elab.command] [0.011337]` encloses exact retained theorem
at 186407–186409; line 188121 `[Elab.async] [0.010160] elaborating proof of
Roth.coeff_uniqueAlgEquiv_symm`. Exactly one outer command and one outer async
proof anchor; nested work not double-counted.

| Actual retained target | Command ms | Async proof ms | Conservative total ms |
| --- | --- | --- | --- |
| Baseline = unchanged final | 11.337 | 10.160 | 21.497 |

FAST-BOARD: below 750 ms resweep threshold and 1000 ms budget; no extra sweep
required for unchanged target. No whole-project performance improvement claimed.
Source `wc -l` 553 before and after, retained declaration count 23 before and after.
Owned declaration 3 lines and proof body 1 line before and after. Git source diff:
0 added, 0 removed, net 0. Docstring two lines unchanged byte-for-byte against
original snapshot, as is entire original target block. `git diff --check` exits 0.
Only the dedicated audit report is a repository write in this worker run.

## All eleven completion steps

- [x] Step 1: required reference documents read, plus relevant style/naming/profiling references.
- [x] Step 2: complete 24-item audit written before source edits (no source edits occurred).
- [x] Step 2.5: all five actual search methods and six-rule decision recorded.
- [x] Step 2.6: every effective binder drop/weakening probed; literature, universes and inversion reviewed.
- [x] Step 2.7: complete signature width table and compiled format.width 100 reference.
- [x] Step 2.8: explicit full inequality occurrence table.
- [x] Step 3: all 42 golfing rules with actual applicable experiments and concrete statuses.
- [x] Step 4: step-back and holistic simplify pass; retain direct minimal proof.
- [x] Step 5a: complete unfiltered native module LSP, original-type/non-self proof, actual target axioms.
- [x] Step 5b: actual module build, protected signature/definitions, structure/naming/width/inequality gates.
- [x] Step 6a: no rename needed; concrete compiled public deletion proposal reported pending/unapplied.

## Freeze and release

Source SHA256:
`a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`.
No source edits made. ALL Lean/MCP/compiler/profile requests completed and drained:
five searches, live goal and tactic attempts, negative native binder probes,
positive native proof, complete module diagnostics, actual module build, all
initial/failed/final compiler sessions and full deletion-proposal compiler session.
No background request remains. Reused profile has no live request.

I explicitly revoke ALL source ownership, including the declaration and ALL call
sites, and become report-only. No source edit after this freeze. Parent owns Git,
shared logs, exact-path commit/push, cumulative original30/public20/allactualaxioms,
sequential full project and separate LeanEval gates. Public deletion and previously
pending public proposals remain unapplied; no approval inferred.

## Owner cumulative publication gates

Source FROZEN SHA256 `a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`; leaf ownership revoked and requests drained before owner gates. Owner probe `80848` exit0,37.50s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d17-compatibility.{lean,log,json}`. Owner build session `63509` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,6.89s/3.08s; source hash stable. `/private/tmp/roth-separation-d17-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
