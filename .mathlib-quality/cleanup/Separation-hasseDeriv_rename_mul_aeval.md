# Fresh audit: `Roth.hasseDeriv_rename_mul_aeval` (original 16)

Baseline: HEAD `db045bc`, source 555 lines; theorem lines 134–154 (21 lines, 16 body lines).
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, plus both skills, cleanup Phase 4,
and relevant naming/style/profiling references. This initial audit precedes any source edit.
The original effective signature and documentation are protected. The public instance omission
menu and deletion of `aeval_X_eq_rename` remain pending; neither is authorized here.

## Initial 24-item audit

| # | Item | Concrete assessment/action |
|---|---|---|
| 1 | Lint | Baseline module: 0 errors / 31 warnings; obtain complete native final diagnostics. |
| 2 | Have scan | `hnone`: support exclusion, reused in `hdisj` and final degree proof; retain. `hdisj`: single-use typed disjointness proof, keeps derivative composition readable; test alternative/inlining before deciding. |
| 3 | Set option | None in target; no limits permitted. |
| 4 | Simp squeeze | L141 `simp at ho` closes contradiction; L148 and L151–153 close each degree side goal. All terminal, retain unsqueezed. |
| 5 | Naming | `hasseDeriv_rename_mul_aeval` identifies derivative, renaming, product, and evaluation; matches operation names, no forbidden abbreviation/pattern; no rename. |
| 6 | Line packing | All four explicit binders packed onto exactly 100 characters. Measure all five signature lines below; RHS structured multiplication continuations require explicit review. |
| 7 | By placement | `:= by` at signature end; nested `by` at end of introducing line. |
| 8 | Format | Two-space tactic indentation; no blank body lines, one rewrite chain. Two ordinary lambda arrows use `=>`; replace with `↦` if source edit is justified. |
| 9 | Comments | No inline comments to move/delete; preserve all documentation and header metadata. |
| 10 | Docstring | Present, explains factorwise action and cites source Lemma 2; preserved verbatim. |
| 11 | Visibility | Public contract retained. Used by `det_hasseDeriv_separated`; not a trivial wrapper. |
| 12 | Structure | 16 body lines, below 60; not a listed main result; no conjunction or long case branch. Two support facts and one derivative rewrite chain; no helper required. |
| 13 | Mathlib | Native searches find univariate Hasse product rule only; local multivariate derivative API is in `Roth/HasseDeriv.lean`. Record all five methods below. |
| 14 | Junk def | n/a: theorem. |
| 15 | Exists lemma | n/a: equality theorem, not an existential helper. |
| 16 | Show/change | Neither occurs. |
| 17 | Push neg | Neither deprecated nor replacement tactic occurs. |
| 18 | Generalise | Probe every effective binder; Fintype/DecidableEq omissions remain proposal-only. Semiring weakening must be tested at statement and proof. |
| 19 | Inequality | Statement has equality; no order inequality hypothesis. Body has `o ≠ none` support exclusion; no `≥` or `>` comparisons. |
| 20 | Normal form | Canonical Hasse derivative indexed by sum of disjoint multi-indices; RHS is product of component derivatives. |
| 21 | Syntax generality | Direct equality supports `rw` in determinant proof. Abstract disjoint variable embeddings would be a separate API, not an automatic restatement. |
| 22 | Import fanout | No additional import needed. |
| 23 | Casts | No numeric coercions; two `X none : MvPolynomial (Option τ) R` annotations fix evaluation target; keep as load-bearing. |
| 24 | Instance name | n/a: no instance declaration. Effective ambient instances anonymous. |

Initial issues: test automation and support simplifications, then perform all verification gates.
No new helper is planned. No public signature/docs/visibility change is planned.


## Five actual search methods

| Method | Actual query | Result/evidence |
|---|---|---|
| Lean-Finder | Hasse derivative of product of polynomials with disjoint variables | Hits: `Polynomial.hasseDeriv_mul`, `MvPolynomial.pderiv_mul`, ordinary derivative product rules. No direct separated multivariate Hasse theorem returned. Raw `roth-separation-d16-search4.json`. |
| Loogle | `MvPolynomial.hasseDeriv, MvPolynomial.rename` | Remote index rejects unknown `MvPolynomial.hasseDeriv` (local project definition); unavailable for this symbol, not evidence of absence. Raw `search2.json`. |
| LeanSearch | Hasse derivative of separated product in disjoint variables | Hits: univariate `Polynomial.hasseDeriv_mul`; not this target. Raw `search3.json`. |
| Source grep | `hasseDeriv`, `degrees_rename_of_injective`, `degreeOf_rename` in mathlib MvPolynomial and local HasseDeriv | Multivariate Hasse operator and composition/factor rules are project API; mathlib degree/renaming theorem directly used. Raw `roth-separation-d16-source-search.log`. |
| Name pattern | Native `lean_local_search` for `hasseDeriv` | Actual hits include project `hasseDeriv_rename`, `_single_aeval_X`, `_hasseDeriv_of_disjoint`, `_mul_of_degreeOf_eq_zero`, plus univariate mathlib rules. Symbol index unavailable; source-backed results are positive evidence, no index-absence claim. Raw `search1.json`. |

All raw paths above are under `/private/tmp/`. Auxiliary variants inspected: `_rename`,
`_mul`, `_of_disjoint`, `_single_aeval_X`, `_mul_of_degreeOf_eq_zero`, `degreeOf_rename`.
Common-equivalents catalogue: no matching replacement bucket.
Conclusion: partial matches supply the derivative composition/factor API; retain this theorem
and its direct degree/renaming substitutions. It is substantial separated-variable reasoning,
not a wrapper around one to three existing mathlib calls. No cast round-trip or typeclass
plumbing signals justify another helper. No new helper has been introduced.

## Literature search

Actual web query: “Hasse derivative multivariate disjoint variables product rule divided derivatives”.
Top relevant research results included Bhandari–Harsha–Kumar–Sudan,
[Decoding Multivariate Multiplicity Codes on Product Sets](https://eccc.weizmann.ac.il/report/2020/179/download),
the ECCC 2024/069 Hasse derivative section, and the authors’ mirror of the first paper.
Also opened [Polynomials, Divided Differences, and Codes](https://drops.dagstuhl.de/storage/00lipics/lipics-vol325-itcs2025/html/LIPIcs.ITCS.2025.93/LIPIcs.ITCS.2025.93.html).
The research formulations use Hasse coefficient extraction and the product rule. Separating
independent variable groups makes all cross terms vanish; this explains the current identity.
An nLab Hasse–Schmidt page was queried/opened but its open returned an internal error.
ChatGPT math MCP: unavailable (no callable tool). No unsupported claim of exhaustive literature
absence. The current coefficient class already avoids field, characteristic-zero, division,
and nonzero-factor assumptions. Abstract disjoint embeddings would require a separate API
proposal; no such public change is applied. The source’s factorial prose is preserved.

## Generalisation status (every effective binder)

Compiler probe sources/logs use prefix `/private/tmp/roth-separation-d16-`.
`autoImplicit false` prevents a deleted parameter from silently reappearing.

| Binder | Role and catalogue candidates | Evidence/result |
|---|---|---|
| `{τ : Type*}` | Index type, already universe-polymorphic; `Sort*` candidate | `sort_tau.lean`: tested; polynomial/Finsupp variable type must be a Type. |
| `[Fintype τ]` | Not mathematically needed; drop, `Finite τ` | `drop_fintype.lean`, `finite.lean` and joint drop probes; public omission remains PENDING, not applied. |
| `[DecidableEq τ]` | Support simplification/degree machinery; drop and use local `classical` | `drop_deceq.lean`, joint drop; public omission remains PENDING, not applied. |
| `{R : Type*}` | Coefficient type, already universe-polymorphic; `Sort*` | `sort_R.lean`: tested; algebraic/polynomial APIs require Type. |
| `[CommSemiring R]` | Needed by MvPolynomial/aeval and commutativity; drop, `Semiring R` | `drop_class.lean`, `semiring.lean`: tested negative at expression/typeclass elaboration. Parent classes such as non-unital/non-associative variants cannot supply the required CommSemiring; no claim of independently testing every ancestor class. |
| `(d : τ →₀ ℕ)` | Arbitrary finitely supported derivative index | `drop_d.lean`: tested negative (unknown `d`). General abstract exponent types change Hasse API/mathematics; no mechanical weakening. |
| `(ν : ℕ)` | Arbitrary univariate derivative order | `drop_nu.lean`: tested negative (unknown `ν`). Generic order types have no corresponding polynomial Hasse operator. |
| `(U : MvPolynomial τ R)` | Arbitrary factor | `drop_U.lean`: tested negative (unknown `U`); no nonzero, degree, monicity, or support assumptions to weaken. |
| `(V : Polynomial R)` | Arbitrary other factor | `drop_V.lean`: tested negative (unknown `V`); no nonzero, degree, monicity, or support assumptions to weaken. |

There are no proposition binders, strict inequalities, continuity/localization assumptions,
or bundled injectivity hypotheses. Universe parameters are already independent. The support
lemmas are local consequences, not public assumptions. These scratch tests do not authorize
changing the original public contract.

## Signature width table

Widths count Unicode codepoints. Existing first binder line is exactly 100. Initial widths
were 100, 57, 83, 36, 95; the two short expression continuations were repacked.
Final width table uses syntactic application arguments as tokens (parenthesized annotations
remain intact), rather than breaking an annotation between `none` and its `:`.

| Final signature line | Characters | Next token / argument | Arithmetic | Action |
|---|---:|---|---|---|
| 134 | 100 | `hasseDeriv` (10) | 100 + 1 + 10 = 111 | ok |
| 135 | 91 | `(X none : MvPolynomial (Option τ) R)` (36) | 91 + 1 + 36 = 128 | ok |
| 136 | 95 | `(X none : MvPolynomial (Option τ) R)` (36) | 95 + 1 + 36 = 132 | ok |
| 137 | 76 | no following signature line | n/a | ok |

The compiler’s actual `#check @Roth.hasseDeriv_rename_mul_aeval` was run with
`set_option format.width 100`, preserved in the independent-proof log. No `pp.width` was used.

## Inequality occurrence table

| Location | Occurrence | Orientation/action |
|---|---|---|
| Public statement/hypotheses | No `<`, `≤`, `>`, `≥` proposition | n/a; an equality for arbitrary factors/indices. |
| Local `hnone` | `o ≠ none` | Disequality, not order; retains exclusion of distinguished variable. |
| Body | `→₀`, `→`, `↦` | Type/lambda arrows, not order comparisons. |

No `_ge_`/`_gt_` name, reverse inequality, or rename queue entry.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: target needs multiple proof steps. |
| 1.2 by rfl | n/a: no definitional reflexivity proof. |
| 1.3 rw/exact→rwa | n/a: rewrite chain closes, no trailing exact. |
| 1.4 simp/exact→simpa | Applied idea: support contradiction intro+simp became one terminal `simp`; no residual exact. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 anonymous constructor | n/a: equality, no product/conjunction construction. |
| 1.7 apply/exact | n/a: no apply/exact pair. |
| 1.8 by_contra! | n/a: no contradiction tactic. |
| 1.9 eta reduction | All lambdas consume hypotheses in dependent support/degree terms; none eta-reducible. Ordinary arrows normalized to `↦`. |
| 1.10 inline have | `hnone` reused twice, retain. `hdisj` is single-use but records the exact support partition for composition; inlining its dependent Finset argument obscures the derivative chain, so retain. |
| 1.11 refine/fun | n/a: no apply/intro pair. |
| 1.12 redundant show | n/a: absent. |
| 1.13 projections→obtain | n/a: no projected existential/product have. |
| 1.14 merge rw | Already one main chain; inner rw changes a side goal before terminal simp, cannot merge across that scope. |
| 1.15 terminal simp | All three terminal simplifications remain unsqueezed. |
| 1.16 nonterminal simp | n/a: all simp invocations close their scoped goals. |
| 1.17 dot notation | Existing `Finset.disjoint_left.2`, support projections already concise; no clearer further change. |
| 1.18 `<|` | n/a: no avoidable parenthesized terminal tactic/lambda application. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential | n/a: no existential helper. |
| 2.1 grind whole | Actual live attempt failed; raw attempts JSON. |
| 2.2 remove before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Whole `simp` made no progress; scoped support goal `simp` succeeds, applied. |
| 2.4 fun_prop | n/a: polynomial identity, no analytic function property. |
| 2.5 positivity | n/a: no positivity/nonzero numerical goal. |
| 2.6 gcongr | n/a: no monotonicity/order goal. |
| 2.7 lia/omega | n/a: no arithmetic comparison; derivative indices remain symbolic API arguments. |
| 2.8 aesop | Whole proof failed; scoped support goal succeeded but `simp` is smaller, retained. |
| 2.9 norm_num/cast | n/a: no concrete numeric arithmetic or numeric cast goal. |
| 2.10 decide | n/a: universally symbolic polynomial equality is not finite computation. |
| 2.11 field_simp/ring | n/a: CommSemiring theorem has no division; missing derivative identities are not ring normalization. |
| 2.12 linear_combination | n/a: no ring-ending block or equality hypotheses for combination. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc term | n/a: no calc. |
| 2.15 `<;>` | n/a: no repeated parallel goals; each rw side condition is different. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 legacy analysis | n/a: no continuity/measurability. |
| 3.3 omega→lia | n/a: neither occurs. |
| 3.4 rfl substitution | Removed explicit `rintro _ ho rfl` because `simp` closes whole support implication. |
| 3.5 automation attributes | No new attribute: specialized rewriting result is explicitly invoked in determinant proof; adding global simp/grind behavior needs API consideration. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 heartbeat limits | n/a: none present or added. |

## Step-back review

Whole-proof live `grind`, `simp`, and `aesop` fail at the derivative identity itself;
`exact?` and `apply?` hit the existing 200000-heartbeat limit (no limit changed).
The native line-replacement tool also emits expected parse leftovers after replacing only
the first tactic line; these are recorded unfiltered, not presented as successful full proofs.
Support-goal live attempts show simp/aesop closure with the old following tactic reported as
“No goals to be solved”; the subsequent actual source `simp` edit was checked by live goal
inspection and complete native diagnostics. `grind` fails on that support goal.
An alternate coefficient/monomial proof would reconstruct the Hasse convolution and obscure
an already existing disjoint-support composition API. Keep the two named support facts and
single rewrite chain. No missing standalone wrapper API is introduced.

Applied changes: one support-proof line removed, signature continuation packed by one line,
two ordinary lambda arrows normalized. Original signature tokens (modulo whitespace), docs,
public binders, derivative decomposition and factorwise equality all preserved.


Generalisation inversion check: no fixed named polynomial/witness is hidden by the statement;
`U`, `V`, `d`, and `ν` are arbitrary, while `some`/`none` occur essentially throughout the
support and degree argument. Abstract disjoint embeddings are a possible different theorem,
not a mechanical dropped hypothesis. No new public proposal beyond the pending instance menu.

Confirmed compiler results: isolated `drop_fintype`, `drop_deceq`, and `drop_both` exit 0;
`Finite τ` replacement exits 0 (unused-section warning). All four data-binder removals and
`CommSemiring` drop / Semiring weakening exit 1 with actual unknown-identifier or missing
CommSemiring diagnostics. The first Sort probes raced a rebuild and reported missing olean;
those runs are invalid as negative evidence. They are replaced by after-build verified logs.
The complete result manifest is `/private/tmp/roth-separation-d16-probes.json`, with rechecks
in `/private/tmp/roth-separation-d16-recheck.json`.


## Verification and gates

Actual `lake build Roth.Separation` completed successfully (1876 jobs), exit 0:
`/private/tmp/roth-separation-d16-final-build-fixed.log`. No warnings were suppressed.
Complete unfiltered native LSP raw response:
`/private/tmp/roth-separation-d16-final-native-lsp.json`: `partial=false`, `success=true`,
`timed_out=false`, zero failed dependencies, **0 errors / 31 warnings**. Three target warnings
are the preserved Fintype section variable and Fintype/DecidableEq unused-in-type warnings.
The header warning is user-preserved metadata, and public omission remains pending.

Independent exact original-type check and non-self proof source:
`/private/tmp/roth-separation-d16-final-independent.lean`. The `example` statement is copied
from the ORIGINAL target signature, with its original ambient binder context. The `independent`
theorem reproves the identity using the current proof and never invokes the target theorem.
The source token comparison (whitespace-normalized) confirms exact original signature;
both original and immediate-baseline docstrings compare equal byte-for-byte.
Actual `#print axioms Roth.hasseDeriv_rename_mul_aeval` and `#print axioms independent`
report exactly `[propext, Classical.choice, Quot.sound]`. The after-final-build log is recorded
below when its process completes. No affected private helper exists and no helper was created.

| Gate | Status / concrete evidence |
|---|---|
| lake_build_file | Pass: actual final module build exit 0. |
| definition_protected | Pass: no def/abbrev change. |
| theorem_statement_protected | Pass: original signature tokens and effective binders preserved. |
| structure_gate | Pass: 15 body lines, 19 declaration lines, no ∧, no case branches. |
| naming_gate | Pass: descriptive operation-based name, no forbidden pattern. |
| line_packing_gate | Pass: full four-line table above; arguments/annotations kept intact. |
| inequality_orientation_gate | Pass: no reversed order comparison. |
| comments/docs | Pass: original docstring byte-identical; no inline narrative removed. |
| imports/casts/instances | Pass: imports unchanged; two load-bearing evaluation annotations retained; no instance name added. |
| cumulative external breakage | Parent owns sequential full project and separate LeanEval plus cumulative original compatibility checks after freeze. Worker module and exact target checks pass. |
| scaffolding | Pass: no sorry, axiom, native_decide, limits, haveI/letI, profiler scaffolding or warning suppression added. |

## Performance

Supplied actual-module baseline, valid at this unchanged starting proof:
`/private/tmp/roth-separation-d15-final-profile-fixed.log`: target outer command 40.551 ms,
outer async proof 234.941 ms, conservative total **275.492 ms**.
Actual final-module profile command:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`,
raw `/private/tmp/roth-separation-d16-final-profile-fixed.log`.
Its actual target anchors are outer command **101.919 ms**, outer async proof **602.561 ms**,
conservative total **704.480 ms** (one command anchor and one proof anchor). The parser is
`/private/tmp/roth-separation-profile-table.py`; parsed table is the profile log plus `.json`.
Nested timings were not double-counted. This is below the 750 ms repeat threshold and 1000 ms
budget; no limit raise or helper extraction is needed. Concurrent compiler work makes these
wall-clock samples unsuitable for a speedup claim. This pass claims proof/style simplification,
not performance improvement. The earlier `d16-final-profile.log` predates the last simp edit
and is superseded; only the `-fixed` log is final evidence.

## Eleven completion steps

- [x] Step 1: read both skills and all required reference material.
- [x] Step 2: initial full 24-item audit before editing.
- [x] Step 2.5: all five actual mathlib search methods, with index failures honestly recorded.
- [x] Step 2.6: every effective binder considered/tested, literature search and inversion check.
- [x] Step 2.7: initial/final signature widths plus actual format.width 100 output reference.
- [x] Step 2.8: per-occurrence inequality scan.
- [x] Step 3: all 42 golfing rules with concrete statuses.
- [x] Step 4: whole-proof automation and alternate-strategy reflection.
- [x] Step 5a: complete native unfiltered module LSP, module build, isolated proof, actual axioms.
- [x] Step 5b: focused diff gates and actual timing anchors.
- [x] Step 6a: no rename needed; parent owns shared rename log, so no shared-log write.

Final arithmetic: module **555 → 553** (−2 lines); target **21 → 19** declaration lines,
body **16 → 15** lines. 23 retained declarations. Diff: 6 additions / 8 deletions in source;
all edits lie within the owned target. `git diff --check` exit 0. No Git mutation by worker.
Concrete pending proposal: omit Fintype/DecidableEq only under the existing public12 menu;
`aeval_X_eq_rename` deletion also remains pending. Neither was applied.


## Freeze and drained requests

After-build verified independent proof/type/actual-axiom run exited 0:
`/private/tmp/roth-separation-d16-final-independent.lean.verified.log`.
The explicit copied ORIGINAL type check compiled; actual retained target and independent
proof each use exactly `propext`, `Classical.choice`, `Quot.sound`.
After-build `Sort*` probes each exit 1 with real Type/Sort mismatches, replacing invalid
missing-olean runs; `/private/tmp/roth-separation-d16-recheck.json` records those results.
Final actual module profiling process exited 0; anchors and totals above are complete.

**ALL Lean/MCP/compiler/profile requests are drained. ALL source ownership is revoked.**
Worker is report-only from this freeze; no source edits will follow.
Frozen source SHA256:
`a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`.
Parent owns all remaining Git/shared logs, the fresh whole-original compatibility and
all-retained axiom probe, and sequential full-project/LeanEval builds, commit and push.

## Owner cumulative publication gates

Source FROZEN SHA256 `a934daecc81ea79ce62d9f8ad460b98c4f49d80806659fa4311add86962c1b4a`; leaf ownership revoked and requests drained before owner gates. Owner probe `94037` exit0,34.72s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL23 actual retained standardaxiom checks. `/private/tmp/roth-separation-d16-compatibility.{lean,log,json}`. Owner build session `72373` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,111.23s/28.20s; source hash stable. `/private/tmp/roth-separation-d16-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
