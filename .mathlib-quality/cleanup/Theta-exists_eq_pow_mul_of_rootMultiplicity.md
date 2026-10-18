# Original 18: exists_eq_pow_mul_of_rootMultiplicity

Dedicated audit of `Roth.exists_eq_pow_mul_of_rootMultiplicity`, Roth/Theta.lean, original baseline `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Preparation was read-only until owner RELEASE at checkpoint `b7806acc3b5fa15eef3f5424cbc2451b67162ff2`.

Applied approved C: remove only the unused explicit `hR : R ≠ 0`. Retain the public theorem, integer coefficient domain, remaining names/order/implicitness and conclusion. Inline the single-use primitive-power proof and remove the `hdvd` intermediate by applying Gauss's lemma directly. Target proof 14 → 12 lines, declaration 18 → 16 lines, whole file 976 → 974. No new production helpers, imports, definitions, attributes, renames, axioms, sorry, limit raises, or profiling scaffolding.

The sole routine caller `pow_rootMultiplicity_le` changes only `exists_eq_pow_mul_of_rootMultiplicity hR hq hcop` to `exists_eq_pow_mul_of_rootMultiplicity hq hcop`. Its own nonzero hypothesis and entire original public contract remain intact. This caller is NOT counted as a dedicated original-19 audit.

## Baseline and scope

Owner supplied full build 64.388 s then separate LeanEval 24.164 s, both exit 0, before release. Baseline complete LSP `/private/tmp/roth-primitive-pow/final-lsp.json` matches supplied Theta SHA `4365647e579ced2904bca87d28d47cff60cb3bd3e5052b17032133a829605c08`: success true, partial false, timed_out false, failed_dependencies [], 0 errors, 19 warnings. Reused this evidence per dispatch. File dialect classic. Header metadata and all existing documentation protected and unchanged. File-wide fixes, shared logs, rename queue and Git mutations belong to owner and were not performed.

Read lean4 and mathlib-quality SKILL.md in full; full cleanup command; full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates; relevant full style/naming/profiling references. Read current Theta and immutable original helper/target/caller source. No subagents spawned.

## Mathematical reading and inversion

Let t be the rational root multiplicity. Coprimality makes qX-h primitive, hence its power primitive. Over Q its image is q^t times (X-h/q)^t. The latter divides the rational polynomial by root multiplicity; the nonzero scalar is a unit, and Gauss's lemma transfers divisibility to Z. Divisibility is exactly the requested existential factorization. The argument also works for R=0; its multiplicity convention is zero, so Q=0 works. This explains the approved drop.

Inversion check: integer and rational polynomial operations, rootMultiplicity, primitive linear polynomial, and Gauss's lemma remain throughout the proof; there is no one-time unfolding of a project-specific named object leaving an unrelated abstract proof. A UFD/fraction-field statement is a possible broader API, but would change domains and uses standard generic Gauss/root-multiplicity API already; not recommended as scope churn here. No concrete-to-abstract extraction needed.

## Full substantive 24-item audit

| # | Item | Result/action |
|---|---|---|
| 1 | Lint | Baseline target hR warning resolved; final target and caller ranges have no warnings/errors. Remaining 18 file warnings outside scope preserved. |
| 2 | Have scan | Original hprim no-by used once: inline. hq' proof by exact_mod_cast, used in hmap and C_mul_dvd: retain. hmap has nontrivial proof and used once: retain proof-bearing block. hdvd has proof, used once: replace intermediate with direct apply/rw/exact, preserving reasoning. |
| 3 | set_option | None in production; none added. Scratch automation lowers budget only. |
| 4 | Simp squeeze | One terminal simp in hmap, kept unsqueezed. No nonterminal bare simp. |
| 5 | Naming | Descriptive exists_eq_pow_mul_of_rootMultiplicity, mirrors existing rootMultiplicity definition casing; no forbidden patterns/abbreviations. No rename. |
| 6 | Line packing | Four signature lines measured below; hq moved to first line and existential prefix to second. |
| 7 | by placement | End of statement and hmap type line. |
| 8 | Format | Two-space tactic indentation, four-space signature continuation with equation-expression indentation; no blank proof lines, semicolon chains, haveI or letI. |
| 9 | Comments | No inline target proof comments to preserve; all five existing docstring lines byte-preserved. Caller docstring byte-preserved. |
| 10 | Docstring | Existing public theorem docstring retained verbatim under explicit protection; it describes the nonzero special case and remains true. |
| 11 | Visibility | Public retained under standing explicit wrapper/domain choice; useful integer factorization API. |
| 12 | Structure | 12-line proof, hmap branch four lines, no branches over ten; no conjunction in conclusion. ∃Q and equation remain together with their shared witness. No helper needed. |
| 13 | Mathlib | Five actual searches and auxiliary routes below; partial building blocks used directly. No exact replacement established. |
| 14 | Junk def | n/a: theorem, no definition. |
| 15 | Exists lemma | Public nontrivial factorization, not private single-use rfl-witness lemma. Retain. |
| 16 | Show/change | Neither present. |
| 17 | Push_neg | None. |
| 18 | Generalise | Every effective original binder probed below; approved hR drop applied, others retained. |
| 19 | Inequality | hq uses 0<q; no reversed inequalities. Table below. |
| 20 | Normal form | Equality expresses integral factorization; divisibility is used internally via Gauss. No new equivalences or competing simp forms. |
| 21 | Syntax generality | Explicit factor witness is directly destructured by sole caller. Existing API shape retained. |
| 22 | Import fanout | n/a: no imports added. |
| 23 | Casts | q:Int and h:Rat casts are cross-type; Int.castRingHom Q is substantive coefficient map. No introduced redundant cast. |
| 24 | Instance names | n/a: no instances declared; compiled effective target type has no section instances. |

## Five-method mathlib search and public literature

Raw complete results: `/private/tmp/roth-rootmult-factor/search.json`.

| Method | Actual query | Evidence |
|---|---|---|
| A Lean-Finder | integer polynomial factor power of primitive rational root linear polynomial root multiplicity | rootMultiplicity, pow_rootMultiplicity_dvd, rootMultiplicity_mul_X_sub_C_pow; partial matches. |
| B Loogle | Polynomial.rootMultiplicity, _ ∣ _ | pow_rootMultiplicity_dvd and le/upper multiplicity divisibility characterizations. |
| C LeanSearch | integer polynomial primitive polynomial divides if divides over rational numbers root multiplicity | generic primitive Gauss divisibility and integer specialization. Remote result signature is older (extra primitive dividend hypothesis); actual local source and compiler confirm current signature. |
| D source rg | full target name; pow_rootMultiplicity_dvd; C_mul_dvd; dvd_iff_map_cast_dvd_map_cast | No mathlib occurrence of complete target name; local GaussLemma.lean:324 integer specialization, Div.lean:538 multiplicity divisor. Read relevant sources. |
| E native local search | rootMultiplicity | 20 concrete declaration hits, including X_sub_C, zero, map-related/multiplication variants; index unavailable. Empty-index absence never claimed. |

Auxiliary variants inspected: le_rootMultiplicity_iff, exists_eq_pow_rootMultiplicity_mul_and_not_dvd, rootMultiplicity_X_sub_C_pow, rootMultiplicity_zero, primitive fraction-map divisibility, C_mul_dvd, map_pow/map_C. Common-equivalents table has no specific matching bucket. Existing standard building blocks already supply the rational divisor and primitive descent. Public specialized integral factorization combines them with a genuine rational linear-factor calculation; retained per explicit public-wrapper choice.

Clean anonymous exact? and apply? probes use exact preceding source prefix ending before the audited declaration, and both stop at conservative 20000 heartbeats. grind, aesop and simp also fail the whole existential. These are bounded failed search attempts, not a global proof of absence. No self-reference or suggestion from previously failed named declarations accepted. Native multi_attempt not retried because session limitation already established; isolated compiler exploration used as authorized.

Public literature search query `Gauss lemma primitive polynomial rational root multiplicity integer factorization` returned, among others, Oxford lecture notes, Beachy's NIU algebra notes, and Knapp's algebra text. [NIU polynomials notes](https://faculty.niu.edu/math_beachy/aaol/polynomials.shtml) describe primitive products and transfer of rational factorization to integer factorization. [Oxford rings and modules notes](https://www.maths.ox.ac.uk/system/files/attachments/lectures%20rings%20and%20modules.pdf) formulate primitive products and their role in Z[X]/Q[X] factorization. [Knapp, Advanced Algebra](https://www.math.stonybrook.edu/~aknapp/download/b2-alg-clickable.pdf) states the UFD version of Gauss's lemma. These support the standard abstract generality; no new result or domain change recommended. ChatGPT math MCP unavailable (no matching exposed tool).

## Effective-binder compiled drop/weakening table

`candidate.lean` compiled exit 0 before source edit. Corrected `negative.lean` compiled exit 1 intentionally; exact named ranges show each failed probe. `actual.lean` positive evidence compiled exit 0 after module build. No negative run is used to certify axioms.

| Original effective binder | Role | Compiled probe and result | Applied decision |
|---|---|---|---|
| {R : Polynomial Z} | Polynomial being factored | drop_R with autoImplicit false: unknown R/R.map; dependent data cannot be erased from unchanged conclusion | retain |
| hR : R ≠ 0 | unused proposition | candidate removes hR and entire selected proof compiles; zero-polynomial positive application compiled in actual.lean | approved removal |
| {h : Z} | rational numerator / linear constant | drop_h autoImplicit false: unknown h in types and proof | retain |
| {q : N} | denominator / linear coefficient | drop_q autoImplicit false: unknown q | retain |
| hq : 0<q | invertibility of rational q scalar | drop_hq fails unknown hq.ne'; weaken to 0≤q fails .ne'; equivalent q≠0 application compiles through Nat.pos_of_ne_zero | retain 0<q, equivalent nonzero spelling gives no useful API improvement |
| hcop : IsCoprime h ↑q | primitive integer linear factor | drop_hcop unknown hcop; weaken to True fails primitive lemma application | retain |

No omitted σ/Fintype/DecidableEq binder: actual compiled original and final types confirm these section variables are not effective in either theorem. Only selected hR removed. The drop/weakening failures describe the unchanged proof and types, not a mathematical impossibility theorem. No claim that hq is logically minimal beyond the existing positive-denominator API.

## Packing and inequality artifacts

Reference actual `#check @Roth.exists_eq_pow_mul_of_rootMultiplicity` at `format.width 100` is in actual.log and displays R/h/q then positivity and coprimality then the existential equality.

| Signature line | Width incl. :=by where present | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 179 | 93 | (hcop : IsCoprime h (q : Z)) = 28 | 93+1+28=122>100 | ok |
| 180 | 58 | (Polynomial.C (q : Z) * Polynomial.X - Polynomial.C h) ^ = 56 | 58+1+56=115>100 | ok |
| 181 | 62 | rootMultiplicity application = 69 | 62+1+69=132>100 | ok |
| 182 | 85 | none | n/a | ok |

Measurements are Unicode codepoints; expression applications/factors are treated as complete syntactic units rather than splitting qualified names from their arguments. No wide-hyp exception used.

| # | Location | Inequality | Rewrite | Rename |
|---|---|---|---|---|
| 1 | hq | 0 < q | already correct | none |
| 2 | entire signature/hypotheses | no ≥ or > | n/a | none |

## All 42 golfing rules

| Rule | Result |
|---|---|
| 1.1 by exact | n/a: no redundant wrapper |
| 1.2 by rfl | n/a: none |
| 1.3 rw+exact→rwa | Retained final rw then exact: changes divisibility goal before applying named universal divisor; no single local exact fact to rewrite in place. |
| 1.4 simp+exact→simpa | n/a: hmap terminal simp, no adjacent exact |
| 1.5 trailing rfl | n/a |
| 1.6 constructor triples | n/a: existential supplied by divisibility |
| 1.7 apply+exact | Applied direct Gauss .2 to goal, followed by substantive rw; not a trivial adjacent pair |
| 1.8 by_contra | n/a |
| 1.9 eta lambdas | n/a |
| 1.10 inline have | Applied hprim inlining; removed hdvd intermediate via direct goal |
| 1.11 apply+intro | n/a |
| 1.12 redundant show | n/a |
| 1.13 have projections | n/a |
| 1.14 merge rw | Each existing rewrite group already merged |
| 1.15 terminal simp only | n/a: terminal simp already unsqueezed |
| 1.16 nonterminal simp | n/a |
| 1.17 dot notation | Current .2 Gauss application and hq.ne' appropriate; no redundant namespace calls with obvious receiver |
| 1.18 <| | No trailing parenthesized block removable without disrupting .2 application |
| 1.19 push_neg | n/a |
| 1.20 trivial existential | n/a: nontrivial public arithmetic factorization |
| 2.1 grind | Actual clean-prefix whole-proof probe failed |
| 2.2 delete before grind | n/a: no grind in selected proof |
| 2.3 simpa consolidation | n/a: no simp followed by closing tactic |
| 2.4 fun_prop | n/a: no analytic function property |
| 2.5 positivity | Actual isolated q:Q nonzero bridge probe compiled (positivity.log); retained explicit exact_mod_cast hq.ne' because both are one line and the existing term states the precise cast bridge. Minimum-value filter: no unsupported clarity/performance claim or production churn. |
| 2.6 gcongr | n/a: no monotonicity goal |
| 2.7 lia/omega | n/a: no linear arithmetic subgoal; cast bridge already exact |
| 2.8 aesop | Actual whole-proof probe failed exhaustive search |
| 2.9 norm_num/norm_cast | No concrete numeric identity; exact_mod_cast hq.ne' gives substantive cast bridge |
| 2.10 decide | n/a: arbitrary polynomial existential |
| 2.11 field_simp;ring | No denominator polynomial identity beyond single q*(h/q)=h handled by mul_div_cancel₀; no field_simp expansion needed |
| 2.12 linear_combination | n/a: no ring/ring_nf terminal proof |
| 2.13 wlog | n/a: no symmetric cases |
| 2.14 calc | n/a |
| 2.15 <;> | n/a: no repeated sibling goals |
| 3.1 erw→rw | n/a: rw already used |
| 3.2 legacy analytics | n/a |
| 3.3 omega→lia | n/a: none |
| 3.4 rcases rfl | n/a |
| 3.5 automation attributes | No canonical new rewrite or global attribute needed |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 limits | No production limits present or introduced |

## Step-back and holistic simplify

Whole-proof automation and lemma search did not produce a shorter complete proof. Direct primitive descent is clearer than retaining a one-use hdvd value. hmap is the real normalization bridge and remains a short proof-bearing fact; hq' is shared by two steps. Term mode would package these same facts into a larger expression with no clarity or performance benefit. No duplicated new skeleton or new helper to audit. Built-in `/simplify` callable unavailable in this host; performed the holistic reuse/quality/efficiency review directly, PASS-THROUGH after selected simplification. Buzz measurement uses actual Lean 4.34 profiling below, not the obsolete profiler option from the reference.

## Verification and compatibility

- `lake build Roth.Theta` exit 0, module.log ends `Build completed successfully (2423 jobs).`
- Complete fresh unfiltered native `lean_diagnostic_messages` final-lsp.json: success true, partial false, timed_out false, failed_dependencies [], 0 errors, 18 warnings. Target/caller warning-free. Header and other pending theorem warnings are outside this leaf's authorized scope.
- `lake env lean actual.lean` corrected final exit 0. Independently replays immutable original helper, original target and original caller in namespace Original18. Original target proof AST does not reference actual target; original caller proof AST does not reference actual caller. Full-old lambda adapter invokes actual new theorem. Definitional equality against immutable original full type checked. Reconstructed expected new type by filtering only old hR binder, then checked actual type, all retained binder names/order/BinderInfo, and exactly one selected AST binder removal.
- Actual built target, actual built caller, original target, original caller and adapter each have only `[propext, Classical.choice, Quot.sound]`.
- Caller exact immutable original type and all binder metadata verified, including own hR. No implicit instance lost.
- Initial scratch diagnostic issue (dangling target docstring preceding set_option) corrected before definitive negative/automation probes. Initial metaprogram used value! without allowOpaque; although exit0 it emitted PANIC, so that run is NOT accepted. Preserved actual-beforefix.log; corrected final uses allowOpaque=true and has no PANIC/errors. Definitive actual.log alone certifies compatibility.
- New-identifier verification: no previously unused mathematical identifier introduced; every proof lemma already present in original body and actual compilation validates all. Nat.pos_of_ne_zero exists and compiles only in positive scratch.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | actual module command exit0 above |
| definition_protected | PASS | no def/abbrev changed |
| theorem_statement_protected | PASS, approved C | exactly hR removed; remaining old type adapter and AST checks passed |
| structure | PASS | target12 lines, no long branch, shared witness retained |
| naming | PASS | descriptive existing name, no forbidden patterns |
| packing | PASS | complete codepoint table |
| inequality | PASS | no reversed code inequalities |
| caller compatibility | PASS | immutable original exact type/nonselfproof and actual standard axioms |
| external breakage | owner gate pending | sole direct caller checked; full project and LeanEval belong to owner |

## Performance — exact prefix only

Buzz outcome: FAST-BOARD. Baseline and accepted final profiles each ran alone, with owner compiler window reserved and no other outstanding compiler/LSP/search requests. The baseline was measured after the original normal gates drained; after one later positivity trial, the accepted final profile was rerun after that trial drained. Earlier final sample retained as historical measurement only.

Actual command for all samples: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-rootmult-factor/{before,after}-prefix.lean`, stdout/stderr raw UTF-8 logs. Before-prefix is exact frozen pre-edit source through the complete caller; after-prefix is exact frozen final source through complete caller; only closing `end Lemma5`/`end Roth` appended. Both declarations are public and their source/docstring anchors appear verbatim in logs. All three invocations exited 0. This is prefix-only evidence, not a complete-module profile claim.

| Declaration/sample | Outer command ms | Async proof ms | Async addDecl/kernel ms | Async linter ms | Conservative total ms | Raw log line anchors in same column order |
|---|---:|---:|---:|---:|---:|---|
| exists_eq_pow_mul_of_rootMultiplicity / before | 32.247 | 332.888 | 16.166 | 13.901 | 395.202 | before-profile.log:175609,179236,305998,306006 |
| pow_rootMultiplicity_le / before | 21.686 | 236.603 | 8.676 | 12.983 | 279.948 | before-profile.log:306066,308558,335908,335910 |
| exists_eq_pow_mul_of_rootMultiplicity / earlier final | 37.813 | 284.918 | 15.145 | 10.111 | 347.987 | after-profile.log:175721,179242,259135,259137 |
| pow_rootMultiplicity_le / earlier final | 29.458 | 214.514 | 6.625 | 10.960 | 261.557 | after-profile.log:259197,261693,289016,289018 |
| exists_eq_pow_mul_of_rootMultiplicity / accepted final | 35.990 | 299.001 | 15.393 | 11.355 | 361.739 | final-profile.log:175753,179258,259033,259035 |
| pow_rootMultiplicity_le / accepted final | 21.392 | 217.916 | 7.836 | 12.771 | 259.915 | final-profile.log:259095,261588,289001,289003 |

Totals sum only non-nested outer command and its associated async proof/addDecl/linter top-level tasks. Nested value/header/kernel traces are not separately double-counted. No separate theorem compiler task occurs in these target/caller spans. Linter time is included conservatively; excluding linter, target 381.301 → 350.384 ms and caller 266.965 → 247.144 ms. Accepted conservative totals target 395.202 → 361.739 ms and caller 279.948 → 259.915 ms. Both comfortably under 1000 ms and 750 ms repeat trigger; no performance repair/deferral necessary. No maxHeartbeats raises removed or added. Owner retains final whole-module sweep responsibility.


## Checklist and freeze

- [x] Step1 full references read
- [x] Step2 full 24-item audit recorded
- [x] Step2.5 five actual search methods recorded with limitations
- [x] Step2.6 every effective binder compiled drop/weakening probes; public literature and inversion
- [x] Step2.7 every signature line measured
- [x] Step2.8 inequality artifact
- [x] Step3 all42 rules considered with concrete applicability
- [x] Step4 step-back/holistic review
- [x] Step5a fresh complete unfiltered final LSP
- [x] Step5b module/compatibility/axiom/diff/performance gates
- [x] Step6a no renames required; sidecar untouched

Source edits frozen/revoked after selected changes. Theta SHA256 `718711f6e77fd4aaee62970a7447b67cfdac545c42fc1dc2a22158efa1741a5f`. No Git/shared log/rename queue writes. All raw evidence under `/private/tmp/roth-rootmult-factor/`. Owner full build, separate LeanEval, final whole-module performance sweep and publication remain owner duties, not claimed here.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (58.997 s),
then separate `lake build Roth.LeanEval` (23.527 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `718711f6e77fd4aaee62970a7447b67cfdac545c42fc1dc2a22158efa1741a5f`.
Raw logs: `/private/tmp/roth-theta-d18-full.log`, `/private/tmp/roth-theta-d18-leaneval.log`; machine record
`/private/tmp/roth-theta-d18-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 18/35, overall 199/264 original
declarations, 9/14 completed files. No new production helper.
