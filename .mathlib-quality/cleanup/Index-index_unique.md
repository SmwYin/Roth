# `Roth.index_unique` — declaration checkpoint

Completed the last original declaration audit, scoped to `Roth/Index.lean:243–260`.
Proof body: **23 → 15 lines**; file: **269 → 262 lines**, 19 retained declarations.
Applied the approved `omit [DecidableEq σ] in` before the byte-preserved docstring.
Preserved `[Fintype σ]`, `[Unique σ]`, `hP`, all data binders and the public formula.
No helper, rename, definition, import, Θ edit, limit raise or trust extension.

The proof identifies evaluated Hasse derivatives with coefficients of the univariate
Taylor polynomial. Its least nonzero coefficient gives the upper bound; minimality
of `natTrailingDegree` gives the lower bound after division by the natural weight.
Removing the equivalence/evaluation/weight aliases makes those two bounds direct.

## Evidence and scope

All paths below are under `/private/tmp/` unless explicitly qualified. All Lean requests
and compiler sessions completed **before** source authority was released. The source
freeze is SHA256 `f706f41e57e50a6449b372c7ed36bc37cac254d6e52b21b94af1b03bdc5e0ee7`.
After release this worker wrote only this report. Owner handles project builds,
independent whole-file verification, separate LeanEval, caller gates and Git publication.

| Gate / evidence | Actual result |
|---|---|
| Baseline | Owner supplied clean HEAD `075587a`; native initial diagnostics had only preserved header warning and the two target decidability warnings. |
| Module | `/Users/ramin/.elan/bin/lake build Roth.Index`, exit 0; `roth-index-unique-module.log`, built target in 15s. Replayed Box/HasseDeriv/Taylor header warnings and target header warning only. |
| Complete native LSP | `roth-index-unique-lsp-final.json`: unfiltered `success=true`, `partial=false`, `timed_out=false`, no failed dependencies; only line 1 header warning, zero target errors/warnings. Direct native call independently returned the same result. MCP shutdown printed an event-loop cleanup exception after the complete successful result; it did not invalidate the returned diagnostic data. |
| Fresh ORIGINAL-type proof | `roth-index-unique-independent.lean` / `.log`, exit 0. Imports Box/Taylor and original Mathlib foundations, **never Index**. Independent `idx` is the same defining sInf; fresh direct support/sInf proof uses neither target nor same-file Index lemmas/private support helper. Original Fintype/DecidableEq/Unique/nonzero/data binders retained. |
| Exact original recovery | `roth-index-unique-recovery.lean` / `.log`, exit 0. Signature extracted from `roth-index-original.lean`, recovered using the actual built `Roth.index_unique`. |
| Actual signature / axioms | Same recovery log: actual width-100 `#check` has Fintype and Unique, **no DecidableEq**. `#print axioms` of actual target, original recovery and independent proof: exactly `propext`, `Classical.choice`, `Quot.sound`. |
| Binder probes | `roth-index-unique-drop-results.json`; nine fresh CLI probes, `autoImplicit=false`, compiled against built Index; details below. Batch exited 0 after recording expected compiler rejections. |
| Automation / generic lookup | `roth-index-unique-automation.lean` / `.log`, exit 0: guarded closing attempts with grind, simp, aesop and exact? fail; independent proof then closes, standard axioms only. Positive gcongr/positivity examples compile. |
| Definition protection | No definition/import/source outside target changed, checked against `roth-index-unique-start.lean`. |
| Statement protection | Literal theorem signature identical to start; public type changes **only** by approved section-instance omission. All docstrings mechanically compared equal. |
| Structure | 15 genuine proof lines; one tactic per line; upper/lower branches 3/4 lines; no conjunction or new helper. |
| Naming | `index_unique` describes the singleton-variable index; snake_case, no forbidden abbreviation/pattern; no rename queued. |
| Packing / inequalities | Complete tables below pass; maximum source width 100 codepoints. |

## Full audit

| # | Item | Finding / action |
|---|---|---|
| 1 | LINT | Removed the unused-section-variable and unused-decidability target warnings through the approved omission; header warning explicitly preserved. |
| 2 | HAVE SCAN | Original `hevalQ`: no by, one use → inline in coefficient bridge. `key`: proof content, two uses → retain as parameterized fact. `hq`: proof content, one use → retain readable nonzero argument. `hw`: proof content, two uses → eliminate via terminal simplification. `hN`: no by, one use → inline trailing-coefficient fact. `h1`: no by, one use → inline upper bound. `e` set-alias eliminated; `q` retained to name the Taylor polynomial. |
| 3 | SET_OPTION | None in target; none added. |
| 4 | SIMP SQUEEZE | Original `simp [weight]` and `simpa using hN` terminal. Final three simpa calls terminal; retained unsqueezed. No nonterminal bare simp. |
| 5 | NAMING | Pass: mathematical subject `index` plus `unique` hypothesis; no forbidden names or `_ge_`/`_gt_`; queue untouched. |
| 6 | LINE PACKING | All three signature lines measured below; justified breaks, actual built width-100 reference. |
| 7 | BY PLACEMENT | All by tokens terminate the preceding statement line. |
| 8 | FORMAT | Two-space tactics; no empty proof lines, semicolon packing, haveI/letI, or trailing whitespace. Ordinary lambda changed to ↦. |
| 9 | COMMENTS | No inline proof comments initially or finally. Existing target docstring and every other docstring byte-identical. |
| 10 | DOCSTRING | Existing one-variable multiplicity explanation/source citation preserved exactly as required. |
| 11 | VISIBILITY | Public headline result, external use in Θ; visibility retained. Classic namespace file. |
| 12 | STRUCTURE | 23→15 by genuine alias elimination/direct bounds; no decomposition deferral. |
| 13 | MATHLIB | Five actual methods below; partial building blocks found and used directly. Custom Roth index theorem retained; guarded generic lookup fails to close its independent defining formula. No claim of exhaustive absence from unavailable remote services. |
| 14 | JUNK DEF | n/a: theorem, no new definition. |
| 15 | EXISTS LEMMA | n/a: public equality theorem, no existential wrapper. |
| 16 | SHOW vs CHANGE | Neither occurs in target. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every original binder checked below. Approved decidability omission only; other public binders preserved. |
| 19 | INEQUALITY | No reversed inequalities in signature; table below. Proof inequalities use ≤. |
| 20 | NORMAL-FORM | RHS rootMultiplicity divided by the weight is the intended one-variable normal form. Uses Mathlib's Taylor/natTrailingDegree bridge internally. |
| 21 | SYNTAX-GEN | Existing equality supports rewriting at Θ; no restatement needed/applied. |
| 22 | IMPORT-FANOUT | n/a: no import changes. |
| 23 | CASTS | 0 redundant casts introduced/dropped. Public rootMultiplicity ℕ→ℝ cast preserved; lower-bound exact_mod_cast and natural-denominator cast are genuine type bridges. |
| 24 | INSTANCE-NAME | n/a: no instance declaration; no named or global decidability instance introduced. |

## Five-method Mathlib search

| Method | Actual query / result |
|---|---|
| A Lean-Finder | `univariate polynomial order of vanishing equals least nonzero Taylor coefficient`, 3 requested: actual bounded MCP request returned DNS `nodename nor servname provided`; unavailable, not evidence of absence. |
| B Loogle | `Polynomial.rootMultiplicity, Polynomial.taylor`, 3 requested: actual bounded MCP request returned DNS failure; unavailable. |
| C LeanSearch | `root multiplicity equals Taylor polynomial trailing degree`, 3 requested: actual bounded MCP request returned DNS failure; unavailable. |
| D source search | Untruncated rg of `rootMultiplicity_eq_natTrailingDegree`, `uniqueAlgEquiv_hasseDeriv`, `eval₂_uniqueAlgEquiv`, `natTrailingDegree_le_of_ne_zero`, `index_unique` in polynomial/MvPolynomial/Taylor sources. Positive hits in RingDivision:133, Equiv:196 and TrailingDegree:121. |
| E name pattern | Actual native `lean_local_search rootMultiplicity_eq`, limit 10, returned seven declarations including `_eq_zero`, `_eq_zero_iff`, `_eq_multiplicity`, `_eq_rootMultiplicity`, `_eq_natFind_of_ne_zero`, and both `_eq_natTrailingDegree` forms. Symbol index reported unavailable; positive source hits remain valid, empty-result absence not claimed. |

Raw remote/name responses: `roth-index-unique-lean_{leanfinder,loogle,leansearch,local_search}.json`.
Auxiliary variants inspected: root multiplicity at zero, general translated version,
`_of_ne_zero`, coefficient/trailing-degree bounds and unique-equivalence evaluation.
Common-equivalents catalogue: no applicable discrete/finite/separation/bornology bucket.
Compiled #checks in recovery log verify the equivalence/evaluation/Taylor identifiers.
All referenced identifiers in added source already occurred in the original proof;
there is no newly invented external lemma name. Generic `exact?` was also tested in
the no-Index independent environment. Conclusion: partial Mathlib match, used directly;
the Roth-specific minimum-to-multiplicity identification remains substantive.

## Every original binder

Drop files are `roth-index-unique-drop-<label>.lean` with corresponding `.log`.
Data probes explicitly disable autoImplicit; rejected deletions therefore cannot silently
reintroduce parameters. Only scoped DecidableEq omission was authorized for application.

| Binder | Classification / use | Mechanical probe | Result / disposition |
|---|---|---|---|
| `{σ : Type*}` | Universe-polymorphic type; index and default domain | drop `sigma` | Rejected: unknown σ; already Type*, no universe widening needed. |
| `[Fintype σ]` | Finite sum in index/weight type | drop `fintype` | **Compiled**: Unique supplies a finite enumeration. Retained exactly per user scope; no further public change applied. Fintype is data, not a class with a weaker inherited parent. |
| `[DecidableEq σ]` | Section decidability, absent from mathematical type | approved scoped omit; candidate and actual module compilation | Compiled and applied; actual built #check confirms absence. |
| `[Unique σ]` | uniqueAlgEquiv, default and singleton coordinate reduction | drop `unique`; parent-only `inhabited`; parent-only `subsingleton` | All rejected: required Unique/default instances unavailable. Retained. |
| `{P : MvPolynomial σ ℝ}` | Polynomial data in conclusion/nonzero hypothesis | drop `P` | Rejected: unknown P with autoImplicit=false. Coefficient-field restatement would require changing preserved definitions/API. |
| `(hP : P ≠ 0)` | Nonzero translated polynomial and lower-bound characterization | drop `hP` | Rejected at nonzero obligation and unknown hP use. Retained. No hP-free zero-convention theorem applied or proposed. Nonzero polynomial is not an ordered scalar strict-positivity hypothesis. |
| `(α : σ → ℝ)` | Taylor center and root | drop `alpha` | Rejected: unknown α. No global proposition to point-localize. |
| `(r : σ → ℕ)` | Weight function/denominator | drop `r` | Rejected: unknown r. No positivity assumption exists to weaken; zero weight is already allowed. |

No applicable continuity/global-to-point or strict-to-weak hypotheses exist. Inversion
check: the proof continues to use the concrete index bound/characterization, the unique
polynomial equivalence and Taylor coefficients; it does not become an abstract argument
after one unfolding. Literature suggests field-level multiplicity theory but extending
the real-valued index framework is a separate API project, not an inline change here.

## Public literature

Two search query strings were issued in a combined request and then reissued separately
to retain clearly displayed per-query rankings. The table records **the separately
displayed repeat rankings**, not a reconstructed ordering of the combined response.

| Query | First three displayed leads on repeat |
|---|---|
| `polynomial index multiplicity root Taylor coefficients order vanishing generalization` | 1 [Polynomials—ECG](https://commeunjeu.org/cours/fr-ecgapprofondies-polynomials/?lang=en); 2 [Vaia exercise solution](https://www.vaia.com/en-us/textbooks/math/a-course-in-calculus-and-real-analysis-2-edition/chapter-4/problem-49-let-fx-be-a-polynomial-of-degree-n-given-any-a-in/); 3 [Salnikov course notes](https://www.vladimir-salnikov.org/files/alg_14_notes_de_cours.pdf). Leads only; secondary commercial material not used as technical authority. |
| `site.stacks.math.columbia.edu order vanishing polynomial multiplicity root` | 1 [Stacks orders of vanishing](https://stacks.math.columbia.edu/tag/02MB); 2 [Stacks definition](https://stacks.math.columbia.edu/tag/02MD); 3 [Kiwix mirror of 02MB](https://kiwix.presumenothing.net/content/stacks.math.columbia.edu_en_all_2024-12/stacks.math.columbia.edu/tag/02MB). Third is a mirror, not independent authority. |

Primary evidence: [Kopparty, List-decoding Multiplicity Codes, §2.2](https://www.math.toronto.edu/swastik/part2.pdf)
defines Hasse derivatives through translated coefficients and multiplicity through the
first nonzero derivative over a field. [Stacks §10.121](https://stacks.math.columbia.edu/tag/02MB)
places orders of vanishing in a broader local-ring setting; it does not directly replace
this finite weighted real index theorem. The project's primary source `clean.tex:679–680`
identifies the one-variable index with root multiplicity divided by the weight.
No literature-driven public change is applied. Math ChatGPT MCP: unavailable in exposed
tool inventory; no second-opinion response fabricated.

## Signature packing and inequalities

Measured in Unicode codepoints, with complete semantic next-clause widths (indentation
excluded from the next clause). No theorem-signature text was repacked or altered.

| Signature line | Width | Next signature clause | Arithmetic | Action |
|---|---:|---|---|---|
| 243 | 93 | `index P α r =` (13) | 93 + 1 + 13 = 107 > 100 | ok |
| 244 | 17 | Entire rootMultiplicity/division RHS through `:= by` (86) | 17 + 1 + 86 = 104 > 100 | ok |
| 245 | 92 | Proof body next | n/a | ok |

Actual compiled `set_option format.width 100 in #check @Roth.index_unique`:

```lean
@Roth.index_unique : ∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : Unique σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 →
    ∀ (α : σ → ℝ) (r : σ → ℕ),
      Roth.index P α r = ↑(Polynomial.rootMultiplicity (α default) ((uniqueAlgEquiv ℝ σ) P)) / ↑(r default)
```

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | Entire signature and hypotheses | No ≥ or > | n/a | No `_ge_` / `_gt_` name |

## All 42 golf rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no outer by-exact wrapper. |
| 1.2 by rfl | n/a: no reflexive proof wrapper. |
| 1.3 rw + exact → rwa | Retained hq's existing rwa; coefficient bridge exact uses definitional eval conversion and does not combine into a matching rewrite. |
| 1.4 simp + exact | Upper/lower bounds consolidated as terminal simpa. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: equality proved by ordered antisymmetry, no constructor pair. |
| 1.7 apply + exact | n/a: antisymmetry introduces two different bounds. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | Removed evaluation alias lambda; key parameter binder replaces lambda; remaining dependent lambda is necessary. |
| 1.10 single-use have | Inlined hevalQ, hN and h1; removed e/hw indirection. |
| 1.11 apply + intro | Lower bound uses refine with function binder directly. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain pair | n/a: no projected conjunction aliases. |
| 1.14 merge rw | Bridge merges three rewrites; lower-bound rewrite of hd eliminated by substitution. |
| 1.15 terminal simp only | n/a: none squeezed. |
| 1.16 nonterminal simp | n/a: final simp/simpa calls are terminal. |
| 1.17 dot notation | `.symm`, `.injective`, `.2` used directly where meaningful. |
| 1.18 <\| | n/a: nested by arguments are inside named/parenthesized applications; removing parentheses would change the following argument's scope. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential inline | n/a: no existential helper. |
| 2.1 whole grind | Actual guarded independent-goal attempt fails to close; native live attempt also failed. |
| 2.2 remove pre-grind | n/a: no grind retained in source. |
| 2.3 simpa consolidation | Applied to both bounds and coefficient nonvanishing. |
| 2.4 fun_prop | n/a: algebraic equality, no analytic function-property goal. |
| 2.5 positivity | Positive compiled natural-cast nonnegativity probe; explicit Nat.cast_nonneg retained for directness. Nonzero q is not structural positivity. |
| 2.6 gcongr | Positive compiled division-monotonicity probe; targeted div_le_div_of_nonneg_right retained, explicitly displaying the denominator condition. |
| 2.7 lia / omega | n/a: no remaining linear arithmetic obligation; minimal-degree inequality comes from polynomial coefficient nonvanishing. |
| 2.8 aesop | Actual guarded independent whole-goal attempt fails to close. |
| 2.9 norm_num / norm_cast | Genuine ℕ→ℝ inequality transported once by exact_mod_cast; no concrete numeric computation. |
| 2.10 decide | n/a: arbitrary real-polynomial equality, no finite computation. |
| 2.11 field_simp; ring | n/a: equality is about index/root multiplicity; denominator may be zero, and no ring identity remains. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or polynomial algebraic certificate goal. |
| 2.13 wlog | n/a: upper and lower bounds are mathematically different, no symmetric cases. |
| 2.14 calc composition | n/a: no calc chain. |
| 2.15 <;> | n/a: two bounds need different arguments. |
| 3.1 erw → rw | n/a: only rw/rwa present. |
| 3.2 legacy fun_prop | n/a: no continuity/measurability tactics. |
| 3.3 omega → lia | n/a: neither arithmetic tactic retained. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | No new global attributes: source-specific rewrite theorem does not require an attribute/API change. |
| 3.6 simp_all | n/a: no simp_all only; guarded whole-goal simp fails to close. |
| 3.7 heartbeat removal | n/a: no override initially or finally. |

Step-back review: the mathematical strategy is already the direct minimum-coefficient
argument. Guarded whole-goal grind/simp/aesop/exact? cannot replace it. Native apply?
suggested division reductions requiring nonzero weights absent from the theorem, so it
does not provide a valid replacement. Term-only composition would obscure the coefficient
bridge. The two retained haves carry real mathematical content; there is no wrapper API
or artificial private split. Scoped simplify review found no remaining duplicated logic;
file-final independent simplify is the owner's separate gate.

## Performance, failures and final status

Actual CLI measurement for both snapshots:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean`.
Both processes exited 0, then `roth-index-profile-parse.py unique-before` / `unique-final`
asserted every current declaration anchored. Artifacts:
`roth-index-unique-{before,final}-profile-trace.log` and corresponding `-profile-table.json`.

| Target | Before | Final | Budget | Outcome |
|---|---:|---:|---:|---|
| index_unique total anchored command + async | 265.69ms | 393.905ms | 1000ms | FAST-BOARD; below 750ms borderline threshold |
| Proof elaboration | 212.34ms | 336.83ms | — | Terminal bound simplification dominates final (108.805ms largest step). |

The shorter proof is modestly slower in this run; retained for clearer direct bounds and
the required headline structure bound, not claimed as a speedup. No performance fix or
heartbeat-count speedup is claimed. CLI traces were used directly; aggregate profiler
categories were not substituted for target timings. No profiling scaffolding remains.
File-final resweep belongs to owner. No over-budget target or performance deferral.

Failed scratch attempts were repaired before their evidence was accepted: rewriting the
eval₂ lemma under Polynomial.eval did not match (fixed with exact/symmetry); broad simp
alone did not transfer the polynomial nonzero fact (fixed with injectivity rewrite);
`rw [q]` could not use the local value as a rewrite (fixed with its explicit equation);
independent upper bound needed `idx` unfolded for the sInf conversion. An initial guarded
simp probe incorrectly tested tactic success rather than closure; corrected to
`fail_if_success solve | simp [idx]` and the entire probe file then compiled. Initial
profile parsing while the compiler was still running rejected incomplete anchors; parsing
after exit 0 succeeded. These failed/intermediate outputs do not certify any gate.

Issues fixed: target decidability lint, redundant aliases, lambda style and headline
structure. Renames queued: none; existing queue untouched. Refactoring needed: none for
this checkpoint. Fintype-drop scratch is a nonblocking observation, explicitly unapplied.
All target gates pass; no whole-project or owner-publication claim is made here.

- [x] Step 1 — mandatory skills, cleanup contract and relevant audit/golf/search/generalisation/style/naming/gates/profiling/buzz references read.
- [x] Step 2 — all 24 audit items recorded with concrete actions or inapplicability.
- [x] Step 2.5 — five actual search methods, positive fallback and remote failures recorded.
- [x] Step 2.6 — every original binder mechanically probed; public literature and repeat top-three leads recorded.
- [x] Step 2.7 — all signature lines measured; actual built width-100 check included.
- [x] Step 2.8 — complete reversed-inequality occurrence table included.
- [x] Step 3 — every one of the 42 golf rules recorded.
- [x] Step 4 — alternative automation and mathematical strategy reviewed with compiled evidence.
- [x] Step 5a — complete unfiltered native diagnostics clean on target, preserved header warning disclosed.
- [x] Step 5b — actual module, independent original proof, original recovery, standard axioms, anchored profile and source/diff protection gates passed before freeze.
- [x] Step 6a — no rename necessary; queue untouched; source authority released, report complete.


## Owner checkpoint d21

Frozen SHA256 `f706f41e57e50a6449b372c7ed36bc37cac254d6e52b21b94af1b03bdc5e0ee7`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session27558 exit0, `/private/tmp/roth-index-d21-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval99632 both exit0(169.65s/41.84s),
Index+Theta hashes stable; `/private/tmp/roth-index-d21-{full,leaneval}.log`.
Complete unfiltered native Index diagnostics: header warning only; Theta caller254 checked, success=true/partial=false/timed_out=false,0errors/28warnings, unchanged from d20. Evidence /private/tmp/roth-index-d21-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
