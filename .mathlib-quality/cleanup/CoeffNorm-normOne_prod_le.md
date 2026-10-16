# Phase 4: Roth.normOne_prod_le

Current amendment: the user explicitly approved the unused public-binder removals on
2026-10-16. See [approved amendment audit](CoeffNorm-api-amendment.md) for the current
source, types, warning count and verification. The original audit below records its
historical checkpoint and remains unchanged.

Dedicated declaration worker, branch ramin-cleanup, assigned HEAD 84cc582.
Scope: target block only in Roth/CoeffNorm.lean and this report. No Git mutations,
shared logs, imports, definitions, docs, instances, or other declarations changed.
Source frozen at SHA256
`76c5827a7b9a0b520e09b1012d73021c26b4a68d2c1d9d749e36b5712989b13a`.
Parent explicitly revoked source ownership after this hash; all later work was verification/report.

Baseline supplied by parent: full build passed, followed separately by LeanEval session 67825 exit 0.
Worker baseline complete native LSP: partial=false, success=true, failed_dependencies=[], zero errors.
Pinned Lean 4.34/mathlib untouched. Existing header warning, three other unused DecidableEq
warnings, and hC warning outside scope remain. The target unused DecidableEq warning is preserved
pending the scoped user decision on CoeffNorm-api-proposal.md; the prior Box decision does not apply.

Read full mathlib-quality and lean4 SKILL.md, full worker contract, golfing-rules.md,
proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md;
also relevant style-rules.md sections and mathlib-review-stages.md. No extra worker spawned.

## Result

Before: 8 declaration lines. After: 4. Saved: 4. Proof body: 6 lines to 2 term lines.
The direct generic nonnegative submultiplicative-product theorem replaces classical induction.
All public signature binders and the mathematical conclusion are unchanged.
Audit improvements: one proof simplification applied; one verified API weakening deferred.
Renames queued: none. Comments: none in body; existing docstring preserved byte-for-byte.
Refactoring needed: verified removal of [DecidableEq σ] is pending the existing user decision.
A generic theorem supplies this product machinery; deleting the public local API or changing
call sites is outside authorized scope and was not done.

## Full audit (24 items)

1. LINT: target unused [DecidableEq σ] warning remains intentionally pending decision.
2. HAVE SCAN: zero have/let declarations before and after; no single-use intermediary.
3. SET_OPTION: none; no heartbeat/recursion/linter suppression added.
4. SIMP SQUEEZE: original terminal simpa in empty case becomes terminal simpa in the
   identity-bound argument. No nonterminal simp, simp only, or residual simp? exists.
5. NAMING: normOne_prod_le describes the coefficient norm finite-product inequality,
   matches existing normOne API, contains no forbidden abbreviation or numbered pattern.
6. LINE PACKING: both signature lines measured in Unicode codepoints; table below.
7. BY PLACEMENT: outer proof is a term; inner by is adjacent to simpa on same line.
8. FORMAT: two-space term indentation, four-space continuation; no blank body lines,
   semicolon chains, haveI/letI, trailing whitespace, or lambda arrows to change.
9. COMMENTS: no proof comments existed; none removed. Docstring unchanged.
10. DOCSTRING: existing public one-sentence finite-product description preserved.
11. VISIBILITY: public API preserved by instruction; no visibility mutation.
12. STRUCTURE: two term lines, no conjunction, no branches; well below all thresholds.
13. MATHLIB: five methods below find the direct nonnegative product theorem.
14. JUNK DEF: n/a, theorem, not data definition.
15. EXISTS LEMMA: n/a, not an existential helper.
16. SHOW vs CHANGE: neither occurs.
17. PUSH_NEG: none.
18. GENERALISE: complete binder table and actual probes below; no signature edits.
19. INEQUALITY: one ≤ occurrence, no ≥ or >; table below.
20. NORMAL-FORM: normOne of a Finset product bounded by product of normOne values is
    the generic submultiplicative finite-product form; already canonical.
21. SYNTAX-GEN: OK, explicit finite set and function compose directly with downstream
    determinant estimates; unused decidability is the separately queued API decision.
22. IMPORT-FANOUT: n/a, no import added; generic theorem already available.
23. CASTS: zero casts dropped, zero cross-type casts added. Existing `(0 : σ →₀ ℕ)`
    is load-bearing: fixes the exponent type in the identity monomial specialization.
24. INSTANCE-NAME: n/a, not an instance; no instance declarations introduced.

## Line packing

Width-100 native compiled reference:
```lean
@normOne_prod_le : ∀ {σ : Type u_1} [DecidableEq σ] {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ),
  normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, normOne (f i)
```

| Signature line (physical source) | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 100: theorem and all binders, ending colon | 95 | conclusion plus :=, 50 chars without indentation | 95 + 1 + 50 = 146 > 100 | ok |
| 101: conclusion through := | 54 | none; proof body follows | n/a | ok |

Python len measured all declaration lines: 95,54,70,76. Maximum 95.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | conclusion | normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, normOne (f i) | already smaller side left | none |
| — | entire signature/hypotheses | zero ≥ and zero > | n/a | no _ge_/_gt_ |

## Mathlib search-status

A. Lean-Finder query: “submultiplicative function finite product inequality”. Top three:
Finset.le_prod_of_submultiplicative, Finset.le_prod_nonempty_of_submultiplicative,
Finset.le_prod_of_submultiplicative_on_pred. Generic ordered-monoid version is unsuitable
for all real numbers because multiplication is not globally monotone there.

B. Loogle query `Finset.prod, _ ≤ _`, five returned hits included
Finset.prod_dvd_prod_of_subset, Equiv.Perm.prod_comp, Equiv.Perm.prod_comp',
Finset.eq_of_card_le_one_of_prod_eq, Finset.eventually_constant_prod. Broad query noisy;
semantic methods found the precise ordered-ring version.

C. LeanSearch query “A submultiplicative nonnegative function at a finite product is at
most the product of its values”. Top three:
Finset.le_prod_of_submultiplicative_of_nonneg,
Finset.le_prod_of_submultiplicative,
Finset.le_prod_of_submultiplicative_on_pred_of_nonneg.

D. rg source: full-name untruncated exact candidate search finds
Mathlib/Algebra/Order/BigOperators/Ring/Finset.lean:74,78. Additional searches for
prod_le_prod and prod/submultiplicative find Group/Finset, Ring/Multiset and variants.

E. Native lean_local_search `le_prod_of`, limit 20: source hits include all preceding
Finset variants plus List/Multiset versions and prod_le_prod_of_subset/injOn variants.
Index warming; positive source hits are confirmed by compiled #check/application,
not treated as a complete absence result.

Auxiliary variants: _on_pred, _of_nonneg, _nonempty, List/Multiset versions,
prod_le_prod₀, prod_le_prod_of_subset, _left/_right monotonicity helpers.
Common-equivalents table: no listed discrete/topological/finite-subset replacement;
this is a generic ordered-ring big-operator result.
Concluded: partial mathematical match becomes a direct specialization of
Finset.le_prod_of_submultiplicative_of_nonneg using normOne_nonneg,
normOne_monomial and normOne_mul_le. Public local name retained under explicit API lock.
Six rules checked: no new wrapper; exhaustive search done; variants checked; no custom
predicate introduced; public deletion deferred by user scope; module docs untouched.
No claim of absence is made.

## Generalisation status

| # | Parameter | Class/use | Mechanical candidates | Actual verification/result |
|---|---|---|---|---|
| 1 | {σ : Type*} inherited | variable index in polynomial/exponent types | drop; universe weakening | autoImplicit=false drop probe errors Unknown identifier σ; already universe polymorphic, no further weakening |
| 2 | [DecidableEq σ] | decidability only, no occurrence in conclusion | drop, local classical | native run_code example with no instance and local classical compiles; verified candidate preserved pending scoped user decision |
| 3 | {ι : Type*} | arbitrary finite-product index | drop; universe weakening | autoImplicit=false drop probe errors Unknown identifier ι; already universe polymorphic |
| 4 | (s : Finset ι) | finite product domain on both sides | drop | actual drop probe errors Unknown identifier s; value essential, no pointwise/strict proposition to weaken |
| 5 | (f : ι → MvPolynomial σ ℤ) | every factor | drop | actual drop probe errors Unknown identifier f; value essential, no typeclass parent or local proposition |

Drop tests executed in isolated native run_code, never changing live signature. Last malformed
f-drop also reached the default heartbeat bound after unknown-identifier errors; no limit was raised.
The positive no-DecidableEq probe passed. There are no algebraic class hypotheses to weaken,
no strict inequalities, continuity/localisation conditions, injectivity/bijectivity bundles,
or concrete finite index type to generalise. ℤ/ℝ coefficient-norm abstraction would require
restating the existing normOne definition and theorems, outside single-declaration scope.
Inversion check: proof depends only on identity bound, nonnegativity and multiplicative bound;
Mathlib already contains precisely that abstraction, used directly. No missing API introduced.

## Public literature search

Web query: “polynomial coefficient l1 norm submultiplicative product generalization”.
Top three returned hits recorded:
1. [Products of polynomials and a priori estimates for coefficients in polynomial decompositions](https://www.sciencedirect.com/science/article/pii/S0747717110800069): weighted polynomial-norm context; not the exact unweighted finite-product result.
2. [On lp1,p2 antinorms of nonnegative matrices](https://www.sciencedirect.com/science/article/pii/0024379590902207): unrelated matrix antinorm generalisation; no actionable change.
3. [Sherstov, Algorithmic Polynomials](https://web.cs.ucla.edu/~sherstov/pdf/algopoly-sicomp.pdf): author-hosted paper defines coefficient absolute-sum norm and states binary submultiplicativity; finite-product iteration is the same abstract mechanism.

ChatGPT math MCP: n/a, no callable math second-opinion tool exposed in this worker's tool metadata.
Literature-driven big changes: potentially coefficients over normed rings with the matching l1
construction; not applied because it restates the norm definition/public API. The finite-product
abstraction is already present in Mathlib. No literature-based weakening of the finite domain needed.

## Actual proof probes and reflection

Native multi_attempt at the assigned body line returned parsing errors (it substituted into the
wrong context: Unknown identifier grind/simp/exact and unexpected using). These are tool-position
failures, not evidence that the tactics fail mathematically. Corrected by isolated native run_code
using the exact pre-target source prefix, without importing the target theorem itself.

The corrected complete positive probe uses fail_if_success solve around grind, simp [normOne],
aesop, exact?: none closes the target; direct generic theorem finishes. Native result success=true,
timed_out=false, only the existing normOne_mul_le unused-DecidableEq warning.
An initial fail_if_success simp test merely detected that simp made progress; it was corrected
to solve-wrapped simp before drawing a conclusion. apply? was also actually tried; it proposes the
generic theorem with nonnegative/identity/multiplication obligations, among many alternatives.
It is a search suggestion, not a smaller trusted proof. No unfinished suggestion was adopted.

Separate actual probe: positivity cannot establish nonnegativity of opaque normOne by itself;
explicit normOne_nonneg closes it. gcongr proves the original induction-step monotonicity when
supplied normOne_nonneg. Generic theorem removes that whole induction step, so gcongr adds no value.
Independent tactic-mode application of the generic theorem compiles, but term form is shorter.
No redundant have blocks or hidden definition unfolding remain. The identity-bound monomial
specialization is the only mathematical side argument; no new helper is warranted.

## Golfing rule pass (all 42)

| Rule | Status |
|---|---|
| 1.1 by exact | applied strategically: direct outer term replaces induction |
| 1.2 by rfl | n/a: no rfl proof |
| 1.3 rw + exact | n/a: original rw is followed by inequality composition, not a single rewrite application; induction removed |
| 1.4 simp + exact | terminal simpa already used for identity bound; retained |
| 1.5 trailing rfl | n/a: absent |
| 1.6 constructors | n/a: no conjunctive/structure result |
| 1.7 apply + exact | direct term application used instead of tested tactic-mode generic application |
| 1.8 by_contra | n/a: no contradiction |
| 1.9 eta lambdas | n/a: no lambda |
| 1.10 inline have | n/a: none |
| 1.11 apply + intro | n/a: no introduction chain |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: none |
| 1.14 merge rw | n/a: already single rw with two prod_insert rewrites; induction removed |
| 1.15 terminal simp only | n/a: no squeezed terminal simp |
| 1.16 nonterminal simp | n/a: none; simpa is terminal |
| 1.17 dot notation | original .trans and .le used; final .le retained |
| 1.18 <\| | n/a: term arguments fit naturally; no terminal parenthesized by argument |
| 1.19 push Not | n/a: no negation push |
| 1.20 existential | n/a: not existential |
| 2.1 grind | actual corrected solve-wrapped test cannot close whole target |
| 2.2 pre-grind deletion | n/a: final proof contains no grind |
| 2.3 simpa | retained direct identity-bound specialization; whole-target simp does not close |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability predicate |
| 2.5 positivity | actual probe fails on opaque normOne; explicit nonnegative lemma supplied |
| 2.6 gcongr | actual original monotonicity probe succeeds with normOne_nonneg; generic theorem removes step |
| 2.7 lia/omega | n/a: real polynomial-norm estimate, no Nat/Int linear arithmetic goal |
| 2.8 aesop | actual corrected solve-wrapped test cannot close whole target |
| 2.9 norm_num/norm_cast | n/a: no cast computation; literal identity already handled by simpa |
| 2.10 decide | n/a: universally quantified infinite polynomial estimate, no finite decision procedure |
| 2.11 field_simp/ring | n/a: no denominators/equality goal |
| 2.12 linear_combination | n/a: no ring/ring_nf conclusion or polynomial equality hypotheses |
| 2.13 wlog | n/a: no symmetric case pair |
| 2.14 calc collapse | n/a: no calc; original .trans already composed |
| 2.15 <;> | n/a: no repeated subgoals in final term |
| 3.1 erw | n/a: none |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactic |
| 3.3 omega→lia | n/a: neither used and no discrete arithmetic subgoal |
| 3.4 rcases rfl | n/a: none |
| 3.5 automation attributes | no attribute change: public normal forms locked; generic theorem explicit application sufficient |
| 3.6 simp_all | n/a: no local conjunction facts or simp_all only |
| 3.7 maxHeartbeats | n/a: none added or present in declaration |

## Verification and actual gates

`/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 80686, exit 0:
Built Roth.CoeffNorm (21s), 1658 jobs. No worker full-project build invoked.
Complete final native lean_diagnostic_messages: partial=false, success=true,
timed_out=false, failed_dependencies=[], zero errors, six preserved warnings.
Native isolated import probe assigns the original polymorphic type to Roth.normOne_prod_le
and proves independentProd by Finset induction without using Roth.normOne_prod_le.
Both print axioms exactly [propext, Classical.choice, Quot.sound]. No sorry/new axiom.
No stale-import info appeared in the final probe, so fallback CLI not needed.

Actual Python diff gate against /private/tmp/d11-prod-before.lean:
only target block differs; 8→4 declaration lines; signature string through := equal;
maximum width95; zero inverted inequality symbols; SHA matches freeze.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | actual lake build Roth.CoeffNorm session80686 exit0 |
| definition_protected | ✓ pass | diff changes no def/abbrev or definition value |
| theorem_statement_protected | ✓ pass | Python original/final pre-:= equality True |
| structure_gate | ✓ pass | two term lines, no ∧ or branch |
| naming_gate | ✓ pass | descriptive normOne_prod_le, no forbidden token/pattern |
| line_packing_gate | ✓ pass | both signature rows measured, no repack |
| inequality_orientation_gate | ✓ pass | one ≤, zero ≥/> |

Overall: pass, with the already-pending API decision explicitly deferred.

- [✓] Step 1 — reference docs read
- [✓] Step 2 — full 24-item audit printed
- [✓] Step 2.5 — five-method mathlib search-status printed
- [✓] Step 2.6 — every-parameter generalisation analysis and actual applicable probes printed
- [✓] Step 2.7 — per-line codepoint packing table printed
- [✓] Step 2.8 — per-occurrence inequality scan table printed
- [✓] Step 3 — all 42 golfing rules have status
- [✓] Step 4 — step-back reflection and independent proof strategy checked
- [✓] Step 5a — complete native diagnostics, zero errors
- [✓] Step 5b — actual diff/build gates pass
- [✓] Step 6a — no renames required or queued
