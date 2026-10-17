# `Roth.index_rename` cleanup

Single-declaration leaf; entry HEAD `3f4f130`. Entry file 266 lines/19 retained declarations; target 218–225. Original snapshot: `/private/tmp/roth-index-original.lean` (e557886), target 227–234. Only approved API change: remove both DecidableEq instance binders, retaining both Fintype binders and all data/injectivity arguments. `omit [DecidableEq σ] in` precedes the byte-identical docstring; proof gains local `classical`. Signature repacked; lambda uses `↦`. Target now 219–227 (8→9 declaration lines; file 266→268). No rename/helper/import/definition/Theta edit.

Mathematics: injective renaming carries translated support to its image under `Finsupp.mapDomain`; corresponding multi-indices have the same weight, hence their sets of weights and infima agree. This works for zero polynomials and zero weights under the existing real-valued definition; no positivity or nonvanishing assumption was introduced.

## Audit: all 24 items

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | Lint | Entry target had unused σ-DecidableEq and unusedDecidableInType for both instances; final complete native LSP has zero target diagnostics. |
| 2 | Have scan | No `have` bindings. |
| 3 | Options | No local options/limit raises. |
| 4 | Simp squeeze | No simp in retained proof; bare simp trial makes no progress. |
| 5 | Naming | `index_rename` describes the operation, snake_case, no forbidden abbreviation/number/ge/gt pattern; no rename queued. |
| 6 | Packing | Every signature line measured below; first line packed after approved binder removal. |
| 7 | By | `:= by` ends conclusion line. |
| 8 | Format | Two-space body, four-space signature continuation, one tactic per line, no empty body lines; `=>`→`↦`; no haveI/letI. |
| 9 | Comments | All three docstring lines byte-identical; no inline proof comments existed or were removed. |
| 10 | Docstring | Existing public statement/source/application context preserved exactly. |
| 11 | Visibility | Public main result listed in module documentation; retained public. |
| 12 | Structure | Five proof-body lines; no conjunction or case branches; below headline ≤15 bound. |
| 13 | Mathlib | Five actual methods below; support API is a partial match, retained domain theorem uses it directly. |
| 14 | Junk def | n/a: theorem, no definition introduced. |
| 15 | Exists lemma | n/a: equality theorem, no existential helper. |
| 16 | Show/change | Neither occurs. |
| 17 | Push-neg | None. |
| 18 | Generalise | Every original binder classified/probed below; only authorized decidability removal applied. |
| 19 | Inequality | Zero inequality occurrences; table below. |
| 20 | Normal form | Renamed index on LHS, original polynomial with composed point/weights on RHS; appropriate rewrite direction. |
| 21 | Syntactic generality | Bare injective function composes directly; no equivalence/surjectivity bundle required. |
| 22 | Import fanout | n/a: no import changes. |
| 23 | Casts | 0 dropped / 0 cross-type / 0 load-bearing in diff. |
| 24 | Instance names | n/a: no instance declaration introduced. |

## Five actual search methods

| Method | Actual query | Result |
|---|---|---|
| A LeanFinder | `multivariate polynomial support rename injective` (3 results) | `MvPolynomial.support_rename_of_injective`, `rename_injective`, `exists_rename_eq_of_vars_subset_range`. |
| B Loogle | `MvPolynomial.rename, MvPolynomial.support` | `support_rename_of_injective`, `support_rename_killCompl_subset`. |
| C LeanSearch | `support of multivariate polynomial under injective renaming variables` | `support_rename_of_injective`, `supportedEquivMvPolynomial`, `exists_rename_eq_of_vars_subset_range`. |
| D Source | Untruncated `rg -n 'index_rename' .lake/packages/mathlib/Mathlib`; relevant rename source inspected | No exact-name text hit; support theorem at Rename.lean:381–384. |
| E Local names | `support_rename`, project root, limit 10 | Both support lemmas found; index reported unavailable, so no absence inferred from the index. |

Auxiliary variants: `_of_injective`, `_killCompl_subset`, `rename_injective`, `_of_vars_subset_range`; actual source and compiled #checks verify the support theorem. Common-equivalents buckets do not match this polynomial invariant. Exact?/apply? compiled probes and live attempts did not close the target. This establishes the relevant partial match, not an exhaustive mathematical absence claim. No custom predicate, wrapper, or missing-API helper added. The retained theorem involves the project-specific index and is expressly requested by the source's Lean note.

## Mechanical generalisation: every original binder

All data-drop probes use `autoImplicit false`; scratch code imports only original imports (Box/Taylor, no Index), defines `idx` by the literal original sInf formula, and uses no Index theorem/helper. Artifact family: `/private/tmp/roth-index-rename-*.lean` and `.lean.log`; aggregate results `/private/tmp/roth-index-rename-probes.json`. Failed probes are rejected candidates, never successful proof/axiom evidence.

| Binder | Class/use | Candidate and observed result |
|---|---|---|
| `{σ : Type*}` | Type variable; polynomial domain | Explicit removal with τ retained: unknown σ. Already universe-polymorphic; no universe restriction to weaken. |
| `[Fintype σ]` | Typeclass; index/weight domain | Drop and `[Finite σ]`: cannot synthesize Fintype σ in statement. Retained; rebuilding index around chosen finite structures would change API. |
| `[DecidableEq σ]` | Decidability; unused in type | Original independent and simultaneous no-DecEq proofs compile. Approved omission applied. |
| `{τ : Type*}` | Type variable; codomain/point/weights | Explicit removal with σ retained: unknown τ. Already independent universe. |
| `[Fintype τ]` | Typeclass; renamed index/weight domain | Drop and `[Finite τ]`: cannot synthesize Fintype τ in statement. Retained. |
| `[DecidableEq τ]` | Decidability; support-image proof | Drop compiles with local classical (independent and actual module). Approved removal applied. |
| `{f : σ → τ}` | Structure value; renaming/composition | Drop: unknown f, with autoImplicit disabled. No parent typeclass applies. |
| `hf : Function.Injective f` | Proposition; support preservation/weight identity | Drop fails at the support rewrite. Properly scoped `Set.InjOn f (P.vars : Set σ)` trial after P fails: support API requires global Injective. No unbundling needed; LeftInverse adds a retract and is stronger. No strict inequality to weaken. |
| `P : MvPolynomial σ ℝ` | Structure value; support | Drop: unknown P. No algebra-class binder to weaken; coefficient field is fixed by protected index definition. |
| `α : τ → ℝ` | Structure value; translation | Drop: unknown α. No continuity/global analytic premise to point-localise. |
| `r : τ → ℕ` | Structure value; weights | Drop: unknown r. No positivity hypothesis present; strict→weak inapplicable. |

Inversion check: after unfolding index the argument is support/image functoriality, already supplied by support_rename and weight_mapDomain. Extracting a new general sInf-image wrapper would duplicate existing congrArg/image_congr; no abstract helper warranted. Possible arbitrary real weights require changing the protected weight/index definitions and are outside this approved API change.

## Public literature

Initial combined search returned blended rankings; these are recorded without assigning a false per-query rank: first displayed leads were Min Ru's Roth notes, Wikipedia Roth theorem, Ghosh–Lasota equivariant polynomial ideals. The following single-query requeries provide explicit displayed rankings (rankings are not endorsements).

| Query/requery | First displayed lead | Second | Third |
|---|---|---|---|
| Q1 requery: `Roth polynomial index invariant renaming variables Lemma 4.2 generalization` | Vojta *Diophantine Approximations in Algebraic Geometry* (Scribd mirror) | Ghosh–Lasota *Equivariant ideals of polynomials* (arXiv:2402.17604) | Bombieri–Gubler *Heights in Diophantine Geometry* (Scribd mirror) |
| Q2 requery: `Roth theorem index polynomial weighted order variable embedding invariance` | Min Ru, *Roth’s Theorem* | Bombieri–Gubler (same mirror) | Wikipedia, Roth's theorem |

Primary sources actually inspected: [Min Ru's notes](https://www.math.uh.edu/~minru/fields/roth.pdf), p.3, define the derivative-weight minimum for complex evaluation points and positive integral weights; [Milojević's exposition](https://aleksa-milojevic.github.io/expository/roth.pdf) was opened as a supplementary primary exposition. Exact project source `.mathlib-quality/references/clean.tex`:532–556 defines the index; :616–634 explains unchanged index when embedding into extra variables and explicitly asks for a separate variable-renaming lemma. Equality in this implementation follows without positivity from the support identity; classical decidability is a proof implementation detail, absent from the mathematical sources. Wider coefficient/weight domains would require changes to definitions; none applied. ChatGPT math MCP unavailable in exposed tools. Nonprimary search leads were not used as technical evidence.

## Packing (Unicode codepoints)

Actual compiled `set_option format.width 100; #check @Roth.index_rename`, saved in `/private/tmp/roth-index-rename-built.log`:

```lean
@index_rename : ∀ {σ : Type u_1} [inst : Fintype σ] {τ : Type u_2} [inst_1 : Fintype τ] {f : σ → τ},
  Function.Injective f →
    ∀ (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ), index ((rename f) P) α r = index P (α ∘ f) (r ∘ f)
```

Pretty-printing exposes implicit binders, so its lines differ from declaration syntax. Every actual signature line is included here; units are complete next binder/conclusion, not bytes.

| Signature line | Codepoints | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 219 | 84 | `(P : MvPolynomial σ ℝ)` (22) | 84+1+22=107>100 | ok |
| 220 | 52 | full conclusion through `:= by` (54) | 52+1+54=107>100 | ok |
| 221 | 58 | none; proof follows | n/a | ok |

## Inequality scan

| Occurrence | Location | Original | Rewrite/name action |
|---|---|---|---|
| none | complete signature/hypotheses/body | no ≥, >, ≤, < relations | n/a; no `_ge_`/`_gt_` name |

## All 42 golf rules

| Rule | Status/evidence |
|---|---|
| 1.1 by-exact | n/a: no wrapper. |
| 1.2 by-rfl | n/a: no trivial reflexive proof. |
| 1.3 rw/exact→rwa | n/a: rw changes support representation, remaining proof constructs image equality. |
| 1.4 simp/exact→simpa | Tested simp/direct simpa live; target not closed. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: no conjunction/product construction. |
| 1.7 apply/exact | n/a: refine supplies the congruence obligation; final exact is weight identity. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta | Lambda needs element and membership binder; cannot eta-reduce. Changed arrow to ↦. |
| 1.10 have inline | n/a: no have. |
| 1.11 refine/fun | Already `refine ... (Set.image_congr fun ...)`. |
| 1.12 redundant show | n/a: none. |
| 1.13 obtain | n/a: no pair-valued have. |
| 1.14 rw merge | Already one rewrite sequence. |
| 1.15 terminal simp | n/a: no retained simp. |
| 1.16 nonterminal simp | n/a: no retained simp. |
| 1.17 dot notation | `Set.image_congr` receives a lambda, congrArg receives sInf; namespace form clear. |
| 1.18 parens/<\| | Parentheses around image proof required as congrArg argument; no trailing tactic parens. |
| 1.19 push Not | n/a: no negation tactic. |
| 1.20 existential helper | n/a: none. |
| 2.1 grind | Actual live whole-goal trial fails; independent trial also recorded. |
| 2.2 pre-grind deletion | n/a: no retained grind. |
| 2.3 simpa consolidation | Actual direct `simpa using weight_mapDomain hf r` type mismatch; explicit support-image transport retained. |
| 2.4 fun_prop | n/a: no analytic function property. |
| 2.5 positivity | n/a: equality, no positive/nonzero subgoal. |
| 2.6 gcongr | n/a: no ordered monotonicity step. |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic goal. |
| 2.8 aesop | Actual live trial fails/no progress. |
| 2.9 norm_num/cast | n/a: no computation or casts. |
| 2.10 decide | n/a: arbitrary polynomial/real equality, no executable finite proposition. |
| 2.11 field_simp/ring | n/a: goal is infimum over support, no exposed rational identity. |
| 2.12 linear_combination | n/a: no ring-ending block. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 calc | n/a: no calc. |
| 2.15 <;> | n/a: one congruence goal. |
| 3.1 erw | n/a: plain rw already works. |
| 3.2 legacy continuity | n/a: none. |
| 3.3 omega→lia | n/a: neither present/arithmetic needed. |
| 3.4 rfl substitution | n/a: no rcases. |
| 3.5 attributes | No simp/grind registration added: RHS changes point/weights, no demonstrated global automation benefit. |
| 3.6 simp_all | n/a: none. |
| 3.7 limits | No override present/added. |

Step-back/scoped simplify: support transport plus preservation of weights remains the clear mathematical argument with the current API. A single terminal `simp [idx, taylor_rename, support_rename_of_injective hf, Set.image_image, weight_mapDomain hf]` does compile independently, but its measured cost is over twice the explicit proof (below), so it was rejected. Bare rfl/simp/grind/aesop/exact? fail; apply? only suggests real Cauchy extensionality and does not discharge the theorem. No duplication, helper, import, or changed definition warranted. A built-in simplify skill is not exposed here; scoped manual review completed, file-final independent simplify remains owner-controlled.


## Verification and gates

| Gate | Result and actual evidence |
|---|---|
| Module build | PASS: `/Users/ramin/.elan/bin/lake build Roth.Index`, exit 0, `/private/tmp/roth-index-rename-build.log`; build completed successfully (1501 jobs). No full project build run by leaf. |
| Complete native LSP | PASS: unfiltered `lean_diagnostic_messages(file_path="Roth/Index.lean", timeout_s=60)`; success=true, partial=false, timed_out=false, failed_dependencies=[]; complete artifact `/private/tmp/roth-index-rename-lsp.json`. Zero target errors/warnings. |
| Original independent proof | PASS: `lake env lean /private/tmp/roth-index-rename-old-independent.lean`, exit 0; explicit original Fintype+DecidableEq binders on both domains, literal index definition, fresh proof, no Index import or same-file theorem shortcuts. `.lean.log` prints exactly propext/Classical.choice/Quot.sound. |
| Independent generalized proof | PASS: `lake env lean /private/tmp/roth-index-rename-independent.lean`, exit 0; neither DecidableEq binder, literal index, fresh support/image proof; same standard axioms only. |
| Exact old built-type recovery | PASS: `/private/tmp/roth-index-rename-built.lean`, final CLI exit 0. Its example reproduces original full type (σ Fintype/DecidableEq, τ Fintype/DecidableEq, f/hf/P/α/r) and closes with actual imported `Roth.index_rename`. Both original DecidableEq instances retained in this recovery test. |
| Actual signature/axioms | PASS: built-module #check at actual format.width100 above; Expr telescope checks exactly 9 binders and rejects any DecidableEq binder. Actual theorem prints only propext/Classical.choice/Quot.sound; built log cited above. This is an authorized public-type change (11→9), not a claim of unchanged public type. |
| Definition protection | PASS: exact pre/post block comparison verified all bytes outside target block unchanged; no def/abbrev changes. |
| Statement protection | PASS with explicit approval: only two DecidableEq omissions; both Fintype instances, hf/P/α/r, universes, equation, and documentation protected. Exact old full type recovered above. |
| Structure | PASS: five proof-body source lines, ≤15 headline limit; no ∧ or branches. |
| Naming | PASS: descriptive index_rename, no forbidden pattern; no source rename/queue mutation. |
| Packing | PASS: all three signature rows/arithmetic and actual compiled width100 output above. |
| Inequality | PASS: zero reverse inequalities; complete scan table above. |
| Comments/new names | PASS: docstring byte-identical; no proof comments present/lost. Only new proof syntax is `classical` and ↦, no new lemma reference; actual built checks confirm support_rename_of_injective, weight_mapDomain, taylor_rename, Set.image_congr. |
| Scoped simplify | PASS-THROUGH: manual scoped review found no additional issue; no callable built-in simplify exposed. Independent file-final simplify belongs to owner. |
| Limits/scaffolding | PASS: no option/limit/attribute/temporary wrapper added to source; no sorry/new axiom/native_decide. |
| Full build/callers/LeanEval | Owner checkpoint gates after source revocation; deliberately not claimed by leaf. |

Complete final native warnings, unfiltered (all outside target):

| Line | Warning |
|---|---|
| 1 | Header copyright too short (user-preserved metadata). |
| 231 | index_le_card automatically included unused σ-DecidableEq. |
| 231 | index_le_card unused hr. |
| 228 | index_le_card unusedDecidableInType σ-DecidableEq (diagnostic anchored to its docstring). |
| 241 | index_unique automatically included unused σ-DecidableEq. |
| 238 | index_unique unusedDecidableInType σ-DecidableEq (docstring anchor). |

## Buzz: actual anchored profiling

Both actual source commands completed exit 0 before parsing:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean`

Logs `/private/tmp/roth-index-rename-{before,after}-profile-trace.log`; parser `/private/tmp/roth-index-profile-parse.py rename-before` / `rename-after` asserts all 19 retained declarations are anchored and writes corresponding `-profile-table.json` artifacts. These are per-declaration command+async totals, not aggregate categories.

| Target | Entry | Final | Final proof time | Dominant final tactic |
|---|---:|---:|---:|---|
| Roth.index_rename | 81.623ms | 105.050ms | 71.747ms | support/image rw, 57.619ms |

FAST-BOARD: 105.050ms <750ms borderline threshold and <1000ms budget. This was an API/style cleanup, not a claimed speed optimization. No override removed/added; no deferral. Final file sweep maximum 557.644ms (index_unique), informational only; file-final sweep remains owner duty.

A successful nontrivial alternative was measured in the same standalone compilation: `/private/tmp/roth-index-rename-alternatives.lean`, CLI --profile+trace command exit0, log `/private/tmp/roth-index-rename-alternatives-profile.log`, parsed totals `/private/tmp/roth-index-rename-alternatives-profile.json`:

| Fresh literal-index proof | Command+async total | Decision |
|---|---:|---|
| Explicit support/image congruence | 76.912ms | Retain the source's readable mathematical steps. |
| Terminal simp with the five supplied identities | 161.552ms | Reject extra simplifier cost for marginal line compression. |

Failures disclosed: native profile extraction failed on scoped omit/same-file context (`cannot omit referenced section variable`, `unexpected end of input`); actual CLI anchored trace above is fallback. A premature initial parse before the baseline process exited correctly failed the all-declaration assertion; it was rerun successfully after exit0. Initial built probe used the wrong qualification Roth.taylor_rename and expected 10 rather than 9 binders; corrected to MvPolynomial.taylor_rename/9, then final exit0. Initial point-local probe referenced P before binding it and is invalid evidence; corrected P-before-hf probe in `/private/tmp/roth-index-rename-extra-probes.lean` actually fails at the expected Injective-vs-InjOn mismatch. `apply?` scratch exits0 while leaving a sorryAx declaration: explicitly rejected as incomplete, never counted as an independent proof. Every failed probe's sorryAx is confined to rejected scratch declarations; the three accepted original/generalized/actual proofs are standard-only.

## Eleven checked leaf steps

- [✓] Step 1: mandatory skill/cleanup/cleanup-all and relevant search/generalisation/style/golf/proof-pattern/gate/review/profiling/buzz references read.
- [✓] Step 2: all 24 audit items answered above.
- [✓] Step 2.5: five actual search methods plus auxiliary variants and local compiled verification recorded.
- [✓] Step 2.6: every original binder mechanically probed/classified; public literature/requery top-three table recorded.
- [✓] Step 2.7: all signature lines measured in codepoints; actual built width100 check recorded.
- [✓] Step 2.8: complete inequality occurrence table recorded.
- [✓] Step 3: all 42 golf rules answered; applicable whole-proof automation and successful simp alternative tested/measured.
- [✓] Step 4: step-back/scoped simplify review completed; readable explicit proof retained for clarity/cost.
- [✓] Step 5a: complete native LSP succeeds with zero target diagnostics; every other warning listed.
- [✓] Step 5b: actual module build, independent original/generalized proofs, exact old built-type recovery, actual new signature/arity/axioms, profile and protection gates pass.
- [✓] Step 6a: no target rename required; unrelated existing queue entry untouched.

No refactoring deferred by this leaf. Owner controls remaining declarations, final whole-file checks, full build, LeanEval, Git and publication. Source authority released and revoked at frozen SHA256 `8b24b3d3662da1a203889b8987874a03d11038f39578339564209e7e6b0d6718`; all native/CLI requests and compiler processes finished beforehand. After release only this canonical report was edited; no further Lean request, source read/edit, or build.


## Owner checkpoint d19

Frozen SHA256 `8b24b3d3662da1a203889b8987874a03d11038f39578339564209e7e6b0d6718`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session74452 exit0, `/private/tmp/roth-index-d19-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval43968 both exit0(149.84s/37.90s),
Index+Theta hashes stable; `/private/tmp/roth-index-d19-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/6other warnings; /private/tmp/roth-index-rename-lsp.json. Owner COMPLETE Theta native LSP0errors/25warnings after bounded partial+complete retry:24previous plus newly exposed unused-section σ-DecEq on private indexSet_comp_subset:134; Θinstances retained for its later audit. Callers148/495 accepted; raw /private/tmp/roth-index-d19-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
