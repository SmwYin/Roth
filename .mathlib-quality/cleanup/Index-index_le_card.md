# `Roth.index_le_card` cleanup

Single-declaration leaf, entry HEAD `20e74ec`; original snapshot `/private/tmp/roth-index-original.lean` at e557886. Entry Index 268 lines/19 retained declarations. Applied only approved removals of unused σ-DecidableEq and explicit `hr`; retained hP, implicit r, hd, α, universes, conclusion, public name and byte-identical docstring. Scoped `omit` precedes the docstring. Packed signature; changed lambda arrow to ↦. Declaration remains six lines; file 268→269 solely from scoped omit. No imports/helpers/definitions/Theta/rename-queue edits.

Mathematics: take a multi-index attaining the index. Its translated-support exponents are bounded by the translated degree, which is bounded by the original degree and then r. The existing generalized `weight_le_card` bounds its weight by card σ even when some r j = 0, using real total division.

## All 24 audit items

| # | Item | Concrete result |
|---|---|---|
| 1 | Lint | Entry: unused σ-DecidableEq (two warnings) and unused hr. Final complete unfiltered native LSP: zero target diagnostics; three other warnings listed below. |
| 2 | Have scan | No `have` bindings. The existing obtain destructures an attained minimum. |
| 3 | Options | None in target; no limit raises. |
| 4 | Simp | No retained simp; actual whole-goal simp fails/no progress. |
| 5 | Naming | `index_le_card` describes index ≤ cardinality, snake_case; no forbidden abbreviation/number/ge/gt pattern. No rename needed. |
| 6 | Packing | All signature lines measured and packed; final first line exactly 100 codepoints. |
| 7 | By | `:= by` ends signature. |
| 8 | Format | Two-space proof/four-space continuation; one tactic per line; no empty proof lines; ↦ replaces lambda =>; no haveI/letI. |
| 9 | Comments | Three docstring lines byte-identical; no proof comments existed/lost. |
| 10 | Docstring | Public statement and source/application context preserved exactly. |
| 11 | Visibility | Public result used by Theta; retained public. |
| 12 | Structure | Four body lines, no conjunction or branches, below all thresholds. |
| 13 | Mathlib | Five actual searches below find support-degree API, used directly. Domain-specific index theorem retained. |
| 14 | Junk def | n/a: theorem, no definition. |
| 15 | Exists helper | n/a: inequality, no new existential helper. |
| 16 | Show/change | None. |
| 17 | Push-neg | None. |
| 18 | Generalise | Every original binder probed below; only authorized hr/DecEq omissions applied. |
| 19 | Inequality | All relations oriented ≤/<; complete table below. |
| 20 | Normal form | Index on LHS, numeric upper bound on RHS; canonical order-bound form. |
| 21 | Syntactic generality | Coordinatewise degree premise fits existing Theta callers; removing hr simplifies their applications. |
| 22 | Import fanout | n/a: no import changes. |
| 23 | Casts | 0 dropped / 0 explicit cross-type / 0 explicit load-bearing casts in diff. Existing implicit Nat→Real card cast retained. |
| 24 | Instance names | n/a: no instance declaration. |

## Five actual search methods

Native search results saved as `/private/tmp/roth-index-card-initial-{0,1,2,3}.json`.

| Method | Actual query | Observed result |
|---|---|---|
| A LeanFinder | `multivariate polynomial monomial support degreeOf bound`, 3 results | monomial_le_degreeOf, degreeOf_le_iff, degreeOf_lt_iff. |
| B Loogle | `MvPolynomial.degreeOf, MvPolynomial.support`, 3 results | degreeOf_eq_sup, le_degreeOf_of_mem_support, monomial_le_degreeOf. |
| C LeanSearch | `degree of monomial in support is at most degreeOf multivariate polynomial`, 3 results | monomial_le_degreeOf, Polynomial.le_degree_of_mem_supp, MvPolynomial.le_totalDegree. |
| D Source | Untruncated `rg -n 'index_le_card' .lake/packages/mathlib/Mathlib`; degree source inspected | Only unrelated subgroup-index cardinality results; Degrees.lean:235/268 verifies degreeOf_le_iff/monomial_le_degreeOf. |
| E Local names | `monomial_le_degreeOf`, limit10 | Exact name/file found; index unavailable, so no index-based absence inference. |

Auxiliary variants inspected: degreeOf_le_iff, le_degreeOf_of_mem_support, degreeOf_eq_sup, degreeOf_lt_iff, le_totalDegree. Compiled #checks confirm monomial_le_degreeOf, degreeOf_taylor_le and weight_le_card. Common-equivalents lookup: no topology/finiteness/bornology predicate bucket applies. Exact?/apply? live probes do not finish the index bound (apply? supplies generic order/ceil subgoals only). Conclusion: partial match, retain local theorem using existing support-degree API. No claim of mathematical absence from empty search; no wrapper/helper/custom predicate or documentation change introduced.

## Every original binder: mechanical generalisation

`/private/tmp/roth-index-card-probes.py` writes isolated literal-index scratch variants with `autoImplicit false`; aggregate `/private/tmp/roth-index-card-probes.json`, per-probe `.lean`/`.log` artifacts. These import Box/Taylor and real/order API, never Index, and define idx by the original sInf formula. Failed scratch proofs are rejected, never axiom evidence for accepted proofs.

| Binder | Class/use | Candidate and result |
|---|---|---|
| `{σ : Type*}` | Type variable; polynomial/weight domain | Drop: unknown σ with autoImplicit=false. Already universe polymorphic. |
| `[Fintype σ]` | Typeclass; index/weight/card | Drop and weakening to `[Finite σ]`: cannot synthesize Fintype in statement/proof. Finite does not supply this concrete Fintype structure; retained. |
| `[DecidableEq σ]` | Decidability; unused | Independent original proof and simultaneous no-DecEq/no-hr proof compile; approved scoped omission applied. |
| `{P : MvPolynomial σ ℝ}` | Structure value; translated support | Drop: unknown P. No parent-class weakening applies to a polynomial value. Real coefficient generalisation requires changing protected index definition. |
| `hP : P ≠ 0` | Proposition; nonempty translated support | Mechanical drop fails at hP use. A fresh P=0 case split DOES compile without hP (below), but hP retained per explicit scope. Replacing nonzero by nonnegativity has no polynomial order here. |
| `{r : σ → ℕ}` | Structure value; weights/degree cap | Drop: unknown r. No typeclass parent; arbitrary real weights require definition/API restatement. |
| `hr : ∀ j, 0 < r j` | Proposition; unused | Drop compiles; strict→weak `∀ j, 0 ≤ r j` compiles; zero `∀ j, r j = 0` compiles. Approved drop is weakest and retained. No point-local positivity premise needed. |
| `hd : ∀ j, degreeOf j P ≤ r j` | Proposition; coordinate bounds | Drop: unknown hd in proof. Point-local trial `∀ j ∈ P.vars, degreeOf j P ≤ r j` fails at hd j (needs membership); not applied. Already weak ≤, no strict premise to weaken. |
| `α : σ → ℝ` | Structure value; translation | Drop: unknown α. No continuity/global analytical premise to point-localise. |

Inversion check: support-degree and finite-sum bounds carry the argument after choosing a translated-support witness; these are already supplied by degreeOf_taylor_le, monomial_le_degreeOf and weight_le_card. No missing abstract helper warranted.

Optional unapproved/out-of-scope nonblocking observation, NOT applied: `without_nonzero` in `/private/tmp/roth-index-card-independent.lean` handles P=0 by simp[idx], otherwise uses the fresh independent nonzero proof; standard axioms only. Removing hP would be a separate public API change beyond this approval. Recorded for owner; hP is explicitly required to remain in this cleanup and no API proposal was expanded or applied.

## Public literature

| Actual single query | First three displayed leads, in displayed order |
|---|---|
| `Roth theorem polynomial index at most number variables degree weights generalization` | 1. Min Ru, *Roth’s Theorem*; 2. Stanford, *17 Roth’s Theorem III* (TransNotes); 3. Wikipedia, Roth’s theorem. |

Primary source inspected: [Min Ru's notes](https://www.math.uh.edu/~minru/fields/roth.pdf), p.3, defines index via normalized nonzero derivatives at complex points with positive integral weights. Project primary source `.mathlib-quality/references/clean.tex`:650–667 gives the exact coordinate-degree argument bounding index by m. The zero-weight extension is a verified implementation inference from total real division, not a claim that these sources define division by zero. Complex/coefficient-field or real-weight extensions require protected-definition changes and were not applied. Nonprimary displayed leads were not used for technical claims. ChatGPT math MCP absent from available tools.

## Signature packing and inequalities

Actual built-module `set_option format.width 100; #check @Roth.index_le_card`, `/private/tmp/roth-index-card-built.log`:

```lean
@index_le_card : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 → ∀ {r : σ → ℕ}, (∀ (j : σ), degreeOf j P ≤ r j) → ∀ (α : σ → ℝ), index P α r ≤ ↑(Fintype.card σ)
```

| Signature line | Codepoints | Next complete unit | Arithmetic | Action |
|---|---:|---|---|---|
| 232 | 100 | `(α : σ → ℝ)` (11) | 100+1+11=112>100 | ok |
| 233 | 52 | none; proof follows | n/a | ok |

Initial no-hr packing had first line69 and next hd binder30: 69+1+30=100, so repacked before final gates. Pretty-printer exposes implicit binders; declaration syntax packs those binders left of the colon.

| Occurrence | Location | Relation | Rewrite/name action |
|---|---|---|---|
| 1 | hd | degreeOf j P ≤ r j | already smaller-left |
| 2 | conclusion | index P α r ≤ Fintype.card σ | already smaller-left |
| old hr | removed approved premise | 0 < r j | already smaller-left before removal |
| reversed | entire signature/hypotheses/body | zero ≥ and zero > relations | none; no `_ge_`/`_gt_` name |

## All 42 golf rules

| Rule | Status/evidence |
|---|---|
| 1.1 by-exact | n/a: multi-step proof, no wrapper. |
| 1.2 by-rfl | n/a: no reflexive equality; live rfl fails. |
| 1.3 rw/exact→rwa | n/a: no rewrite/exact pair; equality transports via ▸. |
| 1.4 simp/exact→simpa | Direct simpa using weight_le_card tested, stuck implicit Fintype; no retained pair. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor | n/a: no conjunction. |
| 1.7 apply/exact | n/a: no apply sequence. |
| 1.8 by_contra! | n/a: no contradiction argument. |
| 1.9 eta | Lambda constructs a bound using j three times; no eta reduction. Arrow changed to ↦. |
| 1.10 have inline | n/a: no have. |
| 1.11 refine/fun | Already supplies coordinate-bound lambda directly to weight_le_card. |
| 1.12 show | n/a: none. |
| 1.13 obtain | Already obtains d/nonzero/equality directly. |
| 1.14 rw merge | n/a: no rewrites. |
| 1.15 terminal simp | n/a: none retained. |
| 1.16 nonterminal simp | n/a: none retained. |
| 1.17 dot notation | Existing `.trans` chains retained. |
| 1.18 <\| | Lambda already unparenthesized; nested trans argument requires parentheses. |
| 1.19 push Not | n/a: none. |
| 1.20 ∃ helper | n/a: no trivial existential wrapper. |
| 2.1 grind | Actual live bare grind and hinted grind fail. |
| 2.2 pre-grind deletion | n/a: no retained grind. |
| 2.3 simpa | Actual direct trial fails; no simp/exact chain to consolidate. |
| 2.4 fun_prop | n/a: no analytic function property. |
| 2.5 positivity | n/a: target is general upper bound, no exposed positivity subgoal. |
| 2.6 gcongr | Actual whole-goal trial makes no progress. |
| 2.7 lia/omega | n/a: no isolated Nat/Int arithmetic goal; real infimum bound needs API. |
| 2.8 aesop | Actual live trial fails exhaustive search. |
| 2.9 norm_num/cast | n/a: no numeric computation/explicit cast goal. |
| 2.10 decide | n/a: arbitrary polynomial/real bound cannot be finite-computed. |
| 2.11 field_simp/ring | n/a: no exposed denominator equality. |
| 2.12 linear_combination | n/a: no ring-ending block. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc | Already trans-composed inequalities; no calc block. |
| 2.15 <;> | n/a: no parallel subgoals. |
| 3.1 erw | n/a: none. |
| 3.2 legacy continuity | n/a: none. |
| 3.3 omega→lia | n/a: neither arithmetic tactic present. |
| 3.4 rcases/rfl | n/a: no equality-pattern substitution. |
| 3.5 attributes | No global simp/grind registration justified by this conditional upper-bound theorem. |
| 3.6 simp_all | n/a: none retained. |
| 3.7 limits | No local override present/added. |

Step-back/scoped simplify: retain the readable four-line attained-minimum proof. The independent direct-support strategy also compiles but measured slower (62.106ms vs45.643ms for comparable standalone proofs); no compression/performance reason to replace source. No duplicated skeleton/new helper needed. Built-in simplify capability is unavailable; scoped manual holistic review is PASS-THROUGH, independent file-final simplify remains owner's gate. Actual live automation trials are tool-session evidence; second batch saved `/private/tmp/roth-index-card-attempts.json`. apply? only suggests incomplete generic order refinements, never accepted proof evidence.

## Verification and diff gates

| Gate | Actual evidence/result |
|---|---|
| lake_build_file | PASS `/Users/ramin/.elan/bin/lake build Roth.Index`, exit0, final `/private/tmp/roth-index-card-build.log` (1501 jobs). |
| Complete native LSP | PASS final unfiltered diagnostic_messages Index timeout60: success=true, partial=false, timed_out=false, failed_dependencies=[]; `/private/tmp/roth-index-card-final-lsp.json`. Zero target diagnostics. |
| Original independent proof | PASS `/private/tmp/roth-index-card-probe-old.lean` with original explicit σ/Fintype/DecEq/P/hP/r/hr/hd/α binders; literal original idx; fresh direct support proof, no Index import/target/private helper/same-file Index shortcuts; CLI exit0, standard axioms only. |
| Strengthened independent proof | PASS `/private/tmp/roth-index-card-independent.lean`, CLI exit0; no hr/DecEq, literal idx, direct csInf/support proof; only propext/Classical.choice/Quot.sound. |
| Exact old built type | PASS `/private/tmp/roth-index-card-built.lean`, CLI exit0; original full type including hr and DecEq recovered by actual built target. Recovery is separate from axiom verification. |
| Actual new signature/axioms | PASS built log above: 7 Expr telescope binders, no DecidableEq, no positivity premise; actual target depends exactly on propext/Classical.choice/Quot.sound. Approved public type changed 9→7 binders. |
| definition_protected | PASS byte comparison verifies source outside target block identical to entry; no def/abbrev edits. |
| theorem_statement_protected | PASS with explicit approved hr/DecEq removal; hP/r/hd/α/formula/docs retained. |
| structure_gate | PASS four body lines, no conjunction/case branches. |
| naming_gate | PASS descriptive snake_case; no forbidden patterns, queue unchanged. |
| line_packing_gate | PASS all two signature lines measured; first line100. |
| inequality_orientation_gate | PASS complete table, no reverse relations. |
| Comments/new identifiers | PASS all target doc bytes retained; no proof comments lost; no new lemma references. Existing references compiled in built probe. |
| no-limit/scaffolding | PASS no overrides, trace/diagnostics/count wrappers, sorry/new axioms/native_decide introduced. |
| Scoped simplify | PASS-THROUGH manual review, unavailable built-in capability disclosed above. |
| Full/callers/LeanEval | Owner checkpoint gates only; leaf makes no project-wide claim. Theta's precisely two hr argument removals remain owner-controlled after source release. |

Complete final unfiltered Index warnings (all outside target): line1 copyright-too-short (user-preserved metadata); line242 index_unique unused σ-DecidableEq; line239 index_unique unusedDecidableInType. Entry warnings saved `/private/tmp/roth-index-card-initial-4.json`; final raw evidence above retains all messages.

## Buzz/profile

Actual source commands each exit0: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean`, logs `/private/tmp/roth-index-card-{before,final}-profile-trace.log`. Parser `python3 /private/tmp/roth-index-profile-parse.py card-before` / `card-final` asserts all19 source anchors and writes corresponding profile-table.json.

| Target | Entry total | Final total | Final proof | Dominant final step |
|---|---:|---:|---:|---|
| index_le_card | 70.990ms | 38.970ms | 24.290ms | obtain attained witness,11.148ms |

FAST-BOARD: under750ms borderline and1000ms budget; no override removed/added, no deferral. Wall jitter means this is API/style cleanup, not a claimed optimization. Final file max447.218ms, informational only; owner's file-final sweep remains separate. Native profile extraction failed on scoped omit/same-file context (`cannot omit referenced section variable`, unexpected end); anchored CLI trace is actual fallback.

Successful nontrivial alternatives compiled/profiled in `/private/tmp/roth-index-card-alternatives.lean` (exit0, only standard axioms); log and parsed totals in `.log`/`.json`: attained strategy45.643ms, direct-support62.106ms. Retained existing attained strategy. Initial independent scratch lacked the real order import and failed InfSet synthesis; added original Real.Basic import, then accepted proof exit0 with standard axioms. An initial baseline parse ran before completion; rerun after compiler exit0 is the recorded final baseline. Rejected binder/automation scratch failures are never accepted proof/axiom evidence.

## Eleven checked leaf steps

- [x] Step 1: mandatory skill/cleanup/cleanup-all and relevant golf/proof/search/generalisation/gate/style/naming/review/profiling/buzz references read.
- [x] Step 2: all24 concrete audit items recorded.
- [x] Step 2.5: five actual search methods, auxiliary variants and compiled verification recorded.
- [x] Step 2.6: every original binder mechanically classified/probed; public literature/top-three table recorded.
- [x] Step 2.7: every signature line measured, repacked, actual built width100 output recorded.
- [x] Step 2.8: complete inequality occurrence table recorded.
- [x] Step 3: all42 golf rules considered; applicable live automation and measured alternative completed.
- [x] Step 4: step-back/scoped manual simplify completed; readable proof retained.
- [x] Step 5a: complete unfiltered native LSP passes with zero target diagnostics; other warnings listed.
- [x] Step 5b: module build, original/strengthened independent proofs, original built-type recovery, actual signature/axioms/profile and protection gates pass.
- [x] Step 6a: no target rename needed; existing queue entry untouched.

SOURCE AUTHORITY RELEASED at frozen Index SHA256 `e05d2a8a8a08c937ab43f96999efb4e9476b9a8ce47c08f9e6267459b236f190`. All native requests and compiler/probe processes finished beforehand, including final built-module recovery rerun after the last packing build. After release: report writing only, no Lean requests, source reads/edits or builds. Owner controls full build, precisely two Theta hr caller removals with all Theta contracts/instances/positivity retained, original whole-file/actual-expression checks, separate LeanEval, shared logs, Git and publication.


## Owner checkpoint d20

Frozen SHA256 `e05d2a8a8a08c937ab43f96999efb4e9476b9a8ce47c08f9e6267459b236f190`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session27382 exit0, `/private/tmp/roth-index-d20-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval93853 both exit0(97.14s/39.29s),
Index+Theta hashes stable; `/private/tmp/roth-index-d20-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/3other warnings; /private/tmp/roth-index-card-final-lsp.json. Owner COMPLETE Theta LSP0errors/28warnings after bounded partial+complete retry:25previous +3new preserved-contract warnings (unused section instance and hr at86, hr at109). Exactly2caller repairs accepted; no suppression/Theta contract removal. Raw /private/tmp/roth-index-d20-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
