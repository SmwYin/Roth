# Phase 4 — `hasseDeriv_kronecker_mem`

Before: 20 declaration lines, 18 body lines. After: 16 declaration lines, 14 body lines.
Saved: 4 lines. Current location: `Roth/GenWronskian.lean:182–197`.
The successor branch now cancels the nonzero scalar in the restricted `K`-submodule,
then applies `Polynomial.hasseDeriv_comp`. The custom inverse identity and its cast/multiplication
rewrite chain are gone. No helper was added. Original mathematical type, definition values,
private visibility, documentation, and upstream `derivative_mem_kronSpan` are preserved.

Frozen source SHA256: `e71820d474dea9551ec7812650dbabd66ec497358a57dbe1a0a001589f4877bd`.
Source ownership was surrendered to the parent after module build and complete LSP success;
all subsequent experiments used `/private/tmp` files or `lean_run_code`.

## Step 1 — References

Read installed `/Users/ramin/.codex/skills/lean4/SKILL.md` and
`/Users/ramin/.codex/skills/mathlib-quality/SKILL.md`, the full worker contract
`/private/tmp/roth-genwronskian-worker-contract.md`, initial file audit, source/context, and
mathlib-quality references `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, relevant `style-rules.md`, naming conventions,
and review-stages normal-form/syntactic-generality sections. Existing private docstrings and
the missing file header are user-protected. Native Lean tools were discovered through
`ALL_TOOLS` metadata; native LSP worked, so no fallback server/process was needed.

## Step 2 — Complete audit

1. LINT: complete LSP has no warning/error in this declaration. Existing header and other
   declarations' instance warnings remain outside this worker's ownership.
2. HAVE SCAN: original `heq` was a proof-containing equality block used once in `rw [heq]`;
   replaced by scalar membership cancellation. Original `h` had no `by`, two textual uses (`simp only ... at h`, then `rw [h]`);
   normally KEEP by the use-count rule, but its entire enclosing heq proof was replaced. No `have` remains.
3. SET_OPTION: none originally or finally; no limit changes.
4. SIMP SQUEEZE: original base `by simp` and `simp [kronHasse]` are terminal. Original
   nonterminal `simp only [...] at h` removed with the auxiliary equality. Final `simpa [...] using`
   is terminal and unsqueezed. No nonterminal bare simp remains.
5. NAMING: `hasseDeriv_kronecker_mem` names the existing Hasse operator, substitution, and
   membership conclusion. No forbidden abbreviation, numerical prefix, or numeric auxiliary suffix.
   The identifier's embedded `hasseDeriv` follows the existing mathematical identifier.
6. LINE PACKING: both signature lines measured in codepoints, table below; max declaration
   width 92. Signature lambda normalized from `=>` to `↦` without type change.
7. BY PLACEMENT: `:= by` remains at the end of the conclusion line.
8. FORMAT: two-space tactics, no empty internal lines, no haveI/letI, ordinary lambdas `↦`;
   induction alternatives retain `=>`. One tactic per line. No consecutive rw remains.
9. COMMENTS: none in the original target; none removed or added. Surrounding comments untouched.
10. DOCSTRING: private helper had none; no new docstring is required. All existing docs preserved.
11. VISIBILITY: private implementation lemma used by the next theorem; stays private.
12. STRUCTURE: final body14 lines, zero conjunctions in the signature, successor branch8
    tactic/continuation lines (L190–197), base branch3. No extraction needed.
13. MATHLIB: all five methods actually run, detailed below. Existing generic scalar-membership
    and Hasse-composition API supplies the simplification; the span induction is project-specific.
14. JUNK DEF: n/a — target is a lemma, not a definition.
15. EXISTS LEMMA: n/a — conclusion is membership, not an existential witness wrapper.
16. SHOW vs CHANGE: no original show; final change removes the transparent restrictScalars
    membership wrapper before convert. This genuinely changes displayed goal form.
17. PUSH_NEG: none.
18. GENERALISE: every elaborated parameter audited below. No signature weakening applied.
    Characteristic-free Hasse chain rules may admit a different proof; failed cancellation
    without CharZero proves a limitation of this proof, not mathematical necessity.
19. INEQUALITY: zero reversed inequalities in signature or local typed hypotheses; table below.
20. NORMAL-FORM: Submodule membership is the canonical form for this operator span; no local
    alternate predicate/equivalence system introduced.
21. SYNTAX-GEN: OK — membership feeds `Finsupp.mem_span_image_iff_linearCombination` directly
    at the existing consumer; a pointwise existential would be less convenient here.
22. IMPORT-FANOUT: n/a — no imports changed or added.
23. CASTS: inverse-related casts removed with heq. Final two natural-to-K conversions are
    cross-type; their inner `: ℕ` annotations select casting the whole successor. An isolated
    removal to `(μ + 1 : K)` failed at L191: cast successor and cast μ plus one are not
    definitionally equal for `Nat.cast_ne_zero`. Thus those annotations are load-bearing.
    No redundant same-type cast survives in the diff; two cross-type casts retained, each
    with its source-type annotation. Explicit K/σ named arguments select the private span.
24. INSTANCE-NAME: n/a — no instance declaration or new local instance.

Issues fixed: custom inverse identity/cast bookkeeping, the intermediate equality block, and lambda
style. No renames queued. Refactoring needed: none. No cross-declaration changes made.

## Step 2.5 — Mathlib search-status

| Method | Actual query/search | Result |
|---|---|---|
| A Lean-Finder | `Hasse derivative composition equals binomial coefficient scalar multiplication` | `Polynomial.hasseDeriv_comp`, LaurentSeries analogues |
| B Loogle | `Polynomial.hasseDeriv, Polynomial.derivative` | `hasseDeriv_one`, `hasseDeriv_one'`, `factorial_smul_hasseDeriv` |
| C LeanSearch | `Hasse derivative composition and derivative factorial` | factorial_smul_hasseDeriv, iterate_derivative_eq_factorial_smul_sum, derivative_comp |
| D source rg | full `hasseDeriv_kronecker_mem`; Hasse/derivative/succ patterns in Mathlib and full HasseDeriv source inspection | no project-span equivalent; composition and factorial APIs inspected |
| E local names | `smul_mem_iff`, `Polynomial.hasseDeriv`, `Nat.cast_smul_eq_nsmul` | Submodule smul_mem_iff variants, Hasse composition/one/zero, cast-scalar bridge verified |

All remote queries returned actual results immediately, with no outage/rate-limit result. Local
name lookup reported `index: warming`; positive source-backed hits were usable, but its empty
results would not establish absence. Full-name rg was untruncated.
Auxiliary variants inspected: smul_mem_iff, smul_mem_iff', smul_mem_iff'', smul_mem_iff_of_isUnit,
Polynomial.isUnit_C, hasseDeriv_one', hasseDeriv_comp, factorial_smul_hasseDeriv.
Common-equivalents lookup: no discrete/finite/separation/bornology bucket applies.

Conclusion: partial generic matches; keep the project-specific induction and build directly on
`Submodule.restrictScalars`, `Submodule.smul_mem_iff`, `Polynomial.hasseDeriv_comp` and
`Nat.cast_smul_eq_nsmul`. It is not a wrapper of one to three generic calls: it proves membership
for every derivative order by induction using the bespoke derivative-stability theorem. No new
predicate or generic wrapper introduced. No claim of exhaustive semantic absence is made:
whole-goal exact?/apply? reached the default 200000-heartbeat bound. Whole-goal grind/simp/aesop
failed. No limit was raised. Existing docs were protected, so no module-doc edits were made.

## Step 2.6 — Generalisation status

The actual elaborated type has seven parameters and two independent universes; `l` is absent.
Scratch parameter probes use fresh types L/τ with `autoImplicit false`; they cannot accidentally
recover dropped parameters from the section. Artifacts:
`/private/tmp/roth-d16-parameter-probes.lean`,
`/private/tmp/roth-d16-parameter-probes-final.json`, and
`/private/tmp/roth-d16-drop-charzero.{lean,json}`.
Failed scratch elaborations automatically print recovery placeholders; none is source code or a
certified result, and none is used by the final theorem.

| Parameter | Class/use | Mechanical candidates actually checked | Verification/result |
|---|---|---|---|
| `{K : Type*}` | coefficient type throughout operators/span | drop; universe widening | fresh binder-drop gives unknown L; already arbitrary universe u_1, no widening available |
| `[Field K]` | coefficient algebra and current kronecker/kronSpan API | drop; DivisionRing; CommRing (weaker infrastructure possibility) | scratch #check targets fail Field synthesis; DivisionRing also lacks commutative polynomial infrastructure; no definition restatement authorized |
| `{σ : Type*}` | variable index type of operator domain | drop; universe widening | fresh binder-drop gives unknown τ; already arbitrary independent u_2 |
| `[Fintype σ]` | enumeration in kronecker/span definition | drop; Finite | scratch targets both fail Fintype τ synthesis; installing chosen enumeration would change implementation/API, not an inline drop |
| `[CharZero K]` | nonzero cast of μ+1 in scalar cancellation | drop | full independent-proof scratch without it fails CharZero synthesis at L191 and leaves CharZero goal; keep original assumption |
| `(k : ℕ)` | substitution exponent and span parameter | drop | fresh target gives unknown k; replacing natural exponent by abstract type is a construction restatement, not mechanical weakening |
| `(μ : ℕ)` | Hasse order, span bound, induction | drop | fresh target gives unknown μ; natural-valued Hasse/finsupp orders preclude point-local/strict→weak variants |

No proposition, decidability, global continuity/monotonicity, or structure-equivalence parameter
is present; their weakening catalogues do not apply. Field→CommRing+IsField would restate the
dependent definitions/instance presentation and is outside the permitted exact-API cleanup;
DivisionRing/drop/CommRing failures show that the present statement requires its Field instance.
Already Type* in independent universes; no universe restriction to remove.

Inversion check: the target proof still mentions kronecker in the scalar goal and composition
evaluation, and kronSpan in the membership cancellation; its decisive inductive step is
derivative_mem_kronSpan. An abstract derivative-stable filtration theorem could factor out this
pattern, but requires new objects/hypotheses and has no second present user. Optional extension
closed under the current API-preserving scope. Likewise a characteristic-free higher chain-rule
proof is plausible but is not a required cleanup and is not disproved by cancellation failure.
Big-change candidates requiring action: none within the authorized cleanup.

Literature search status: A WebSearch and B math MCP both n/a — private declaration,
literature search not required by the scope rule. No public mathematical generality claim made.

## Step 2.7 — Line packing

Reference actual built `#check` with explicit `set_option format.width 100`:
`/private/tmp/roth-d16-check-width.log` prints the complete private
constant with `{K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] [CharZero K] (k μ : ℕ)`.
Widths below count Unicode codepoints, including indentation. The first next unit is the complete
parenthesized lambda expression (49 characters), not the individual lexical word `fun`.

| Signature line | Characters | Next indivisible signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 182 | 63 | `(fun P ↦ Polynomial.hasseDeriv μ (kronecker k P))`, 49 chars | 63 + 1 + 49 = 113 > 100 | ok |
| 183 | 92 | proof body next | n/a — last signature line | ok |

No wide-hyp escape used; no remaining repack row. Complete target max width92.

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 0 | signature L182–183 and all local typed hypotheses | n/a — no ≥ or > inequalities | none | no _ge_/_gt_ in name |

`=>` in match alternatives is syntax, not a reversed inequality. The only degree bound used in
the base witness is ≤. No reversed inequality or rename remains.

## Step 3 — Every golfing rule

| Rule | Concrete disposition |
|---|---|
| 1.1 | n/a — no by-exact wrapper |
| 1.2 | n/a — no by-rfl wrapper |
| 1.3 | superseded original rw heq / exact smul_mem by direct scalar-membership cancellation |
| 1.4 | applied: original simp-at-h plus rw chain replaced with terminal simpa using composition |
| 1.5 | n/a — no trailing rfl after simp |
| 1.6 | n/a — no constructor/exact/exact chain |
| 1.7 | n/a — new apply has genuine subsequent conversion goal, not immediate exact |
| 1.8 | n/a — no contradiction proof |
| 1.9 | checked; lambdas retain kronecker composition and evaluation, so eta-reduction does not apply |
| 1.10 | strategy supersedes: original h has two textual uses, so not mechanically inlined; entire heq removed and composition fed directly to simpa |
| 1.11 | n/a — no apply/intro pair |
| 1.12 | n/a — no show |
| 1.13 | n/a — no projected pair have |
| 1.14 | n/a — original rw calls separated by heq scope; rewritten proof has none |
| 1.15 | applied by strategy: removed nonterminal simp-only chain; all final simp/simpa unsqueezed |
| 1.16 | n/a — no final nonterminal bare simp |
| 1.17 | applied: restrictScalars then .smul_mem_iff and .mp, composition equality .symm |
| 1.18 | checked; parentheses in apply enclose the iff before .mp, in simpa they select .symm; removing them would alter parse |
| 1.19 | n/a — no push_neg |
| 1.20 | n/a — not an existential helper |
| 2.1 | whole-goal native multi_attempt grind failed at membership, no limit raise |
| 2.2 | n/a — no grind retained |
| 2.3 | applied: terminal simpa with cast-scalar bridge and add_comm replaces manual cancellation algebra |
| 2.4 | n/a — no analytic function property goal |
| 2.5 | isolated exact base degree-zero inequality proved by positivity; keep simpler existing simp; inline multi_attempt was parser-contaminated and not counted as verification |
| 2.6 | n/a — no monotonicity/calc inequality step; base bound is just zero degree |
| 2.7 | isolated lia on exact base degree inequality failed (degree not normalized); simp retained; no need for omega |
| 2.8 | whole-goal native multi_attempt aesop failed with no progress |
| 2.9 | isolated norm_num proves base degree inequality, but does not improve existing simp; no cast-goal norm_cast chain remains |
| 2.10 | n/a — arbitrary polynomial-function span membership is not a finite computation; base normalization already simp |
| 2.11 | n/a after strategy replacement — inverse denominator identity removed entirely |
| 2.12 | n/a — no ring/ring_nf ending or ring combination goal; scalar action identity handled directly by API |
| 2.13 | n/a — zero/successor induction alternatives are not symmetric cases |
| 2.14 | n/a — no calc |
| 2.15 | checked — base creates different degree and function-equality goals; one requires funext/kronHasse, so same closer is not appropriate |
| 3.1 | n/a — no erw |
| 3.2 | n/a — no continuity/measurability tactics |
| 3.3 | satisfied by 2.7: lia tested, no omega introduced |
| 3.4 | n/a — no rcases/rfl pattern |
| 3.5 | n/a — private project-specific membership fact has no suitable simplifier normal form to register |
| 3.6 | n/a — no simp_all only |
| 3.7 | n/a — no maxHeartbeats/maxRecDepth option, no increase introduced |

## Step 4 — Reflection and failed experiments

The mathematical argument is induction on derivative order, using derivative stability of the
operator filtration. Replacing the explicit reciprocal formula with scalar cancellation expresses
this argument directly. A factorial-based proof would still need an iterated-stability induction
and adds bookkeeping, so the successor composition API is preferable. No new API extraction
is needed after this simplification: the final equality is a single existing composition identity.

Whole-proof native `lean_multi_attempt` tested grind/simp/aesop/exact?/apply? at original L184.
grind/simp/aesop did not solve the actual target; exact?/apply? hit default heartbeats. Replacing
only the induction line also left branch-parser errors, so those synthetic files are not
claimed clean independent compiled absence probes. The actual independent replacement proof,
on the exact original statement and without referring to this theorem, compiled separately.

Intermediate source experiments: restrictScalars + convert initially produced an iff goal rather
than function equality; explicit change fixed that. A broad simp with forward cast_smul bridge
expanded nsmul to multiplication asymmetrically; reversing the bridge solved it. A multiline
multi_attempt equality replacement retained original continuation lines and produced parser
errors; not counted as a successful proof. Final live diagnostics and independent file establish
the retained proof, not those exploratory outputs. Isolated arithmetic artifact records
positivity and norm_num succeeding and lia failing. Cast-drop artifact records a real type mismatch.

## Step 5 — Verification and gates

Actual commands, all from repository root:

- `/Users/ramin/.elan/bin/lake build Roth.GenWronskian > /private/tmp/roth-d16-module.log 2>&1`
  session6284 exited0, `Build completed successfully (1838 jobs)`.
- Complete native `lean_diagnostic_messages` on target file, timeout_s40:
  success=true, partial=false, timed_out=false, zero errors, failed_dependencies=[];
  `/private/tmp/roth-d16-lsp.json`. Only five pre-existing out-of-scope warnings.
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d16-independent.lean >
  /private/tmp/roth-d16-independent.log 2>&1`, session54709 exit0. It contains the original
  signature copied from baseline (including original lambda spelling), fresh proof named
  independentProof using only preceding source, and no reference to hasseDeriv_kronecker_mem.
  Axioms exactly `[propext, Classical.choice, Quot.sound]`.
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d16-axioms.lean >
  /private/tmp/roth-d16-axioms.log 2>&1`, session38591 exit0. Imports actual built module,
  finds private constant by environment suffix, prints its actual type and axioms.
  `_private.Roth.GenWronskian.0.Roth.hasseDeriv_kronecker_mem` uses exactly the standard three.
- Width-reference scratch first tried unknown option `pp.width` (session51551 exit1);
  corrected to Lean's `format.width 100`; isolated check session32109 exited0,
  `/private/tmp/roth-d16-check-width.log`. No repository source
  or resource limits were changed.
- Captured precise worker diff `/private/tmp/roth-d16-source.diff` against worker-start snapshot
  `/private/tmp/roth-d16-start.lean`. Only assigned declaration changed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module command session6284 exit0 |
| definition_protected | pass | no definition changed; source diff confined to lemma |
| theorem_statement_protected | pass | original exact type independently proved; lambda notation only surface change |
| structure_gate | pass | body14, longest branch8, no signature conjunction |
| naming_gate | pass | descriptive identifier, no forbidden patterns/abbreviations |
| line_packing_gate | pass | both lines measured; 63+1+49=113, final width92 |
| inequality_orientation_gate | pass | required zero-occurrence table; no reversed inequalities |
| axiom gate | pass | independent and actual built private constant both standard3 |

Overall: pass. Parent owns cumulative full-project and separate Lean evaluation gates;
no full-project build or concurrent shared build was run by this worker.

## Step 6 — Result

Audit issues found3, fixed3; refactoring deferred0. Rules applied: 1.4,1.15,1.17,2.3,
plus lambda normalization and direct scalar-restriction API. Renames-queued: none.
Comments-preserved: none present in target; surrounding documentation byte-preserved.
Refactoring needed: none. No pending routine worker work.

Phase checklist:

- [✓] Step 1 — installed skills, reference docs, full contract, initial audit and context read.
- [✓] Step 2 — complete 24-item audit printed.
- [✓] Step 2.5 — actual five-method search and auxiliary variants reported.
- [✓] Step 2.6 — every parameter, universes, inversion, private literature exemption audited.
- [✓] Step 2.7 — every signature line measured with next-unit codepoint arithmetic.
- [✓] Step 2.8 — inequality occurrence table printed.
- [✓] Step 3 — all 42 golfing rules have concrete status.
- [✓] Step 4 — complete-proof automation/API alternatives and reflection performed.
- [✓] Step 5a — complete live LSP clean, no partial/timeout.
- [✓] Step 5b — focused diff, actual module build, type/nonself proof and axiom gates pass.
- [✓] Step 6a — no rename needed; no sidecar mutation.
