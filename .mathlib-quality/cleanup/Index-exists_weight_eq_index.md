# Phase 4 — Roth.exists_weight_eq_index

Scope: one public declaration in `Roth/Index.lean`, entry lines 70–75,
release lines 71–76; entry HEAD `450b31d`, branch `ramin-cleanup`.
The user explicitly approved dropping this theorem's unused `[DecidableEq σ]`.
The sole source edit adds `omit [DecidableEq σ] in` before its existing
docstring. Name, documentation, mathematical arguments, conclusion, proof and
definitions are unchanged. No helpers, attributes, imports or version changes.

All Lean requests and compiler processes finished before source authority was
released to the owner. Release SHA256:
`a872711cb58cfec0e2bb6b24ba400001fb4f3d3e6518276b3f6f47f46f25352b`.
Release file length: 269 lines. Subsequent worker activity was report writing
only; the owner may independently change the source after this release.

## Step 1 — References and mathematics

Read lean4 and mathlib-quality SKILL.md; the complete 1,847-line cleanup.md,
including its Phase-4 worker contract; full golfing-rules, proof-patterns,
mathlib-search, generalisation-patterns and cleanup-gates; relevant style-rules
sections for formatting, signatures, proof comments, hypotheses, term-mode
show, visibility and simplification; naming-conventions. Read buzz.md and
profiling.md. This worker spawned no further agents.

The nonzero Taylor polynomial has nonempty finite support. Its real weight
image is therefore a nonempty finite set, so its infimum belongs to that image.
Unpacking that image provides an exponent whose weight equals the index.
Taylor coefficient evaluation converts its support membership to nonvanishing
of the corresponding Hasse derivative. No decidable equality or positive-weight
hypothesis is used in this argument.

## Step 2 — Full audit, all 24 items

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Entry complete native LSP returned unusedSectionVars and unusedDecidableInType warnings for this target. Approved scoped omission removes both. Final complete LSP: success=true, partial=false, timed_out=false, failed_dependencies=[], zero target diagnostics; 26 unrelated warnings remain for later workers. |
| 2 | HAVE SCAN | n/a: no have or let in the retained proof. The obtain destructures an existential and both extracted facts are consumed. |
| 3 | SET_OPTION | n/a: no target option or limit override. |
| 4 | SIMP SQUEEZE | `simpa using hP` terminates the inner nonemptiness proof; leave unsqueezed. No nonterminal bare simp. |
| 5 | NAMING | PASS: exists_weight_eq_index states existence and the weight=index equality; snake_case, no forbidden abbreviation, numeric scheme or single-letter public name. No rename queued. |
| 6 | LINE PACKING | PASS: all signature lines measured in codepoints; complete-token arithmetic below. |
| 7 | BY PLACEMENT | PASS: outer by ends the conclusion line; inner by ends the term-mode show line. |
| 8 | FORMAT | PASS: two-space tactic indent, four-space signature continuation, no internal blank line, semicolon chain, haveI or letI. |
| 9 | COMMENTS | Both docstring lines preserved byte-for-byte. No inline proof comments existed. |
| 10 | DOCSTRING | Existing public docstring describes attained index and cites §4. Preserved under Rule A and explicit task scope. |
| 11 | VISIBILITY | Keep public: index API used four times elsewhere in this file and at Roth/MainLemma.lean:522 at entry. |
| 12 | STRUCTURE | Four body lines. The conjunction lies inside an existential and records two properties of the same chosen witness; it is not a top-level conjunction API to split. No long branch or extraction signal. |
| 13 | MATHLIB | Five actual search methods attempted. Generic finite-set attainment matches found; the existing proof already uses Set.Nonempty.csInf_mem directly. No verified equivalent of this project-specific derivative/index interface. See search table. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: public, reused attainment theorem, not a private single-use trivial witness. |
| 16 | SHOW vs CHANGE | Keep term-mode show: deleting its expected type was actually tested and fails with “invalid 'by' tactic, expected type has not been provided”. It is not a tactic rewriting a goal. |
| 17 | PUSH_NEG | n/a: none. |
| 18 | GENERALISE | Every binder drop-tested; Fintype→Finite also tested. Only DecidableEq drop compiles; approved scoped omission retained. Details below. |
| 19 | INEQUALITY | PASS: no ≥ or > in the signature or hypotheses; scan below. |
| 20 | NORMAL-FORM | Already existence of an exponent with derivative nonvanishing and weight=index. Finite minimum is the generic canonical primitive. Natural weightedOrder has a different codomain and weight model. |
| 21 | SYNTAX-GEN | Existing callers need the paired derivative fact and index equality for the same witness. Support/coefficient membership would require reconstruction at each caller. No easier public restatement established. |
| 22 | IMPORT-FANOUT | n/a: no new import. |
| 23 | CASTS | Diff: 0 dropped / 0 cross-type casts kept / 0 load-bearing ascriptions added. Existing finite-support Set ascription remains unchanged. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues found: one unused class argument with two diagnostics. Fixed by one
approved scoped omission. No cross-declaration change or new public proposal.

## Step 2.5 — Five-method mathlib search

| Method | Actual query | Observed result |
|---|---|---|
| A Lean-Finder | `infimum of a nonempty finite set of real numbers belongs to the set`, 3 results requested | Tool returned isError=true: read operation timed out. This is an attempted method with a disclosed failure, not evidence of absence. |
| B Loogle | `sInf ?s ∈ ?s`, 5 results | IsLeast.csInf_mem; csInf_mem under WellFoundedLT; Set.Nonempty.csInf_mem for a finite set; Nat.sInf_mem; sInf_mem_of_not_isPredPrelimit. |
| C LeanSearch | `infimum of a finite nonempty set is attained`, 3 results | Finset.exists_mem_eq_inf; Finset.exists_mem_eq_inf'; Finset.Nonempty.csInf_eq_min'. |
| D mathlib source rg | Untruncated full-name `exists_weight_eq_index`; `csInf_mem`, `sInf_mem`, `exists_min_image`, `exists_isMinOn` in conditional-complete lattice and finite-minimum sources | No exact-name text hit; positive generic csInf_mem and its finite-set API. Finset.lean generates the Set.Nonempty.csInf_mem dual from csSup_mem by to_dual. |
| E native local name search | `csInf_mem`, limit 10 | Positive hits include Set.Nonempty.csInf_mem, Finset.Nonempty.csInf_mem, IsLeast.csInf_mem, Int.csInf_mem and closure variants. Index was warming; this limits empty-result interpretations, not these positive source hits. |

Auxiliary variants inspected: IsLeast.csInf_mem, finite-set csInf_eq_min',
exists_mem_eq_inf', generated dual csSup_mem, and basic well-founded csInf_mem.
Common-equivalents table: no direct discrete/separation/bornology replacement;
the generic finite-set minimum primitive is already used directly.

Conclusion: **partial generic match**, chiefly Set.Nonempty.csInf_mem. The
retained public result connects the project's definitions to Hasse derivatives.
No declaration is introduced and no exhaustive absence claim is made. The
non-self exact?/apply? probes below do not furnish a complete replacement.
No new generic wrapper is extracted, since that minimum API already exists.

## Step 2.6 — Generalisation status and actual probes

Native lean_run_code snippets used autoImplicit=false. To avoid proving a goal
by rediscovering the imported target, the search and binder probes imported
only Roth.Box, Roth.Taylor and the real/order dependencies, then defined EW.index
with the exact index body. The final independentBuilt proof additionally used
the actual built Roth.index and did not call this target or its private helper.

| # | Binder | Class/use | Mechanical candidates actually tested | Result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable, exponent and polynomial variable type | Drop with autoImplicit=false | Fails: unknown σ. Already universe polymorphic. |
| 2 | `[Fintype σ]` | class, weight sum and index type | Drop; replace by `[Finite σ]` | Both fail to synthesize Fintype σ in weight/index. No computational parent supplies it. |
| 3 | `[DecidableEq σ]` | decidability, unused | Drop in independent proof; live omit | Both compile. Explicitly approved omission applied. |
| 4 | `{P : MvPolynomial σ ℝ}` | structure value, Taylor polynomial | Drop | Fails: unknown P. Coefficient abstraction changes protected definitions and is outside this declaration edit. |
| 5 | `(hP : P ≠ 0)` | proposition, nonempty Taylor support | Drop | Fails: unknown hP at the nonemptiness proof. A separate compiled zero-polynomial example proves that the desired existential is false for P=0. No order-strength or pointwise hypothesis to weaken. |
| 6 | `(α : σ → ℝ)` | data, evaluation point and Taylor shift | Drop | Fails: unknown α. No global function-property hypothesis occurs to localize. |
| 7 | `(r : σ → ℕ)` | data, weight denominators | Drop | Fails: unknown r. There is no positivity assumption to weaken. |

All failed probes returned success=false, timed_out=false; the dropped-DecEq
proof returned success=true, timed_out=false. Long-line warnings in some scratch
headers are formatting noise from the probe generator, not retained source.
The first independent scratch attempt lacked Real's conditionally complete
order import; a second used the incorrect qualification Roth.coeff_taylor.
Both were corrected before accepting any proof: the final proof uses the
verified MvPolynomial.coeff_taylor and has no error/sorry diagnostic.

Inversion check: the mathematical core is the existing generic finite-set
minimum theorem. No missing abstract API is inferred. Abstract coefficient or
real-denominator variants would alter protected definitions; no such change is
applied or presented as a new checked proposal.

### Public literature search

Actual queries:
`Roth polynomial index minimum nonzero derivative attained generalization` and
`finite set infimum attained minimum linearly ordered set`.

| Query | First three returned leads | Finding |
|---|---|---|
| Roth index generalization, repeated separately to record order | [Fields Medal preface](https://www.maths.ed.ac.uk/~jmf/MaOv/fieldsmedals.pdf); [Roth ICM mirror](https://paperzz.com/doc/7033317/h---rl-h.); [Transcendental number theory text](https://www.infophysics.net/nt.pdf) | Discovery leads; no new theorem or generalization accepted merely from these snippets. |
| finite ordered set minimum, initial combined query | [mathlib finite minimum documentation](https://math.iisc.ac.in/~gadgil/PfsProgs25doc/Mathlib/Data/Finset/Max.html); [Axioms of Set Theory](https://u.cs.biu.ac.il/~tsaban/ST/ST09/J11-33.pdf); Fields Medal preface above | Mixed relevance; the actual generic minimum API was checked in local mathlib and by Lean. |

Follow-up opened primary [Min Ru, Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf),
p. 3, whose definition takes the minimum of weighted derivative orders with
nonzero evaluation. Also opened [Infimum and supremum](https://en.wikipedia.org/wiki/Infimum_and_supremum)
for the requested canonical-order context. Local project source clean.tex
530–556 explicitly explains nonempty finite derivative support and attainment.
Inference from the checked finite-set argument: decidable equality is an
implementation assumption that this result does not need. No further public
API change follows from these searches.

ChatGPT math MCP: n/a — no callable such tool was available in ALL_TOOLS.
Literature-driven big-change candidates introduced by this worker: none.

## Step 2.7 — Line packing, complete signature

Actual compiled #check at format.width=100:

```lean
@exists_weight_eq_index : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 → ∀ (α : σ → ℝ) (r : σ → ℕ), ∃ d, (eval α) ((hasseDeriv d) P) ≠ 0 ∧ weight r d = index P α r
```

| Signature line at release | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 71 | 92 | existential conclusion through `:= by`, 65 codepoints | 92 + 1 + 65 = 158 > 100 | ok |
| 72 | 69 | none; proof body follows | n/a, no further signature token | ok |

The ∃ binder and its body form the complete conclusion; moving only `∃ d,`
would split the quantified conclusion rather than move a complete signature
argument. Both signature lines remain byte-identical to the original.
Omission line: 23 codepoints. Body widths: 24, 73, 84, 45.

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | all signature lines and hypotheses | no ≥ or > occurrences | n/a | no _ge_ or _gt_ name |

## Step 3 — Golfing pass, all 42 rules

Live lean_goal exposed the expected existential before obtain and the support
witness afterwards. The first live multi_attempt replaced only the obtain line,
leaving its continuation and causing parse errors; those results are explicitly
not accepted as complete whole-proof tests. Correct isolated, non-self probes
then tested grind, simp, aesop, exact? and apply?. Grind failed; simp and aesop
left the existential unsolved; exact? could not close. apply? reported
success=true but supplied partial suggestions and a sorry-category diagnostic,
so it is rejected as an incomplete proof. No generated automation proof was
copied into source and no limits were raised.

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no by-exact wrapper. |
| 1.2 by rfl | n/a: no reflexivity wrapper. |
| 1.3 rw+exact | n/a: no rewrite tactic. |
| 1.4 simp+exact→simpa | Already inner terminal simpa using hP. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 anonymous constructor | Already final ⟨d, ..., ...⟩. |
| 1.7 apply+exact | n/a: no apply tactic. |
| 1.8 by_contra! | n/a: no contradiction chain. |
| 1.9 eta reduction | n/a: no lambda. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply+intro | n/a: neither tactic. |
| 1.12 redundant show | Actual removal test fails without expected type; keep term annotation. |
| 1.13 obtain | Already obtain destructuring needed support witness. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 terminal simp unsqueeze | n/a: no terminal simp only. |
| 1.16 squeeze nonterminal simp | n/a: inner simpa closes its goal. |
| 1.17 dot notation | Already .csInf_mem, .finite_toSet.image. |
| 1.18 use <\| | n/a: existing show needs parentheses as dot-notation receiver; no trailing by argument suitable for this transformation. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 inline trivial ∃ lemma | n/a: public theorem with five caller occurrences, not trivial private singleton witness. |
| 2.1 grind whole proof | Actually tried in non-self isolated context; failed. |
| 2.2 delete before grind | n/a: retained proof has no grind. |
| 2.3 simpa consolidation | Existing inner simpa already consolidated; whole simp leaves witness unsolved. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | n/a: nonvanishing here is polynomial-specific, not a positivity consequence. |
| 2.6 gcongr | n/a: no inequality goal or monotonicity chain. |
| 2.7 lia/omega | n/a: no integer arithmetic goal. |
| 2.8 aesop | Actually tried; leaves existential, depth warning. No limit increase. |
| 2.9 norm_num/norm_cast | n/a: no numeric computation/cast goal. |
| 2.10 decide | n/a: existential over unbounded exponents and arbitrary real coefficients has no finite decision computation. |
| 2.11 field_simp;ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring-ending proof or algebraic certificate. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 <;> | n/a: no repeated similar subgoals. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 fun_prop modernization | n/a: no continuity/measurability. |
| 3.3 omega→lia | n/a: no arithmetic tactic. |
| 3.4 rfl substitution | n/a: no rcases-rfl. |
| 3.5 automation attributes | No attribute added: witness existence is not a simplification normal form and adding global search rules lacks a demonstrated need. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 heartbeat overrides | n/a: none. |

## Step 4 — Reflection

The proof expresses exactly the mathematics: attain the finite infimum, then
translate support membership. Whole-goal automation does not improve it.
Deleting the term-mode expected type actually fails. A composed Exists.imp
term would hide the two witness properties without eliminating mathematical
steps. No redundant tactic or missing generic API is exposed. Retain the
existing four-line body under the minimum-value/no-churn rule.

## Step 5 — Verification and gates

Actual `lake build Roth.Index`: session 88704, exit 0, ending
“Build completed successfully (1501 jobs).” Existing unrelated warnings remain.
Final native complete LSP: success=true, partial=false, timed_out=false,
failed_dependencies=[]; zero diagnostics on target lines 68–77, 26 elsewhere.
git diff --check returned clean. Diff against the worker entry snapshot has
exactly the one omission line. No definition or theorem source signature line,
proof line, docstring or comment changed.

Actual built-import snippet compiled at success=true, timed_out=false:

```lean
example {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0)
    (α : σ → ℝ) (r : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r :=
  @Roth.exists_weight_eq_index σ _ P hP α r
example {σ : Type*} [Fintype σ] [DecidableEq σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0)
    (α : σ → ℝ) (r : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r :=
  @Roth.exists_weight_eq_index σ _ P hP α r
```

The second example recovers the exact original public type from the original
snapshot. Independently, this stronger proof against the actual built index
also compiled, without target calls or the private support helper:

```lean
theorem independentBuilt {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0)
    (α : σ → ℝ) (r : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by
  obtain ⟨d, hd, hw⟩ :=
    (show (weight r '' ((taylor α P).support : Set (σ →₀ ℕ))).Nonempty by
      simpa using hP).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))
  exact ⟨d, by simpa only [Finset.mem_coe, mem_support_iff, coeff_taylor] using hd, hw⟩
```

Actual #print axioms for both Roth.exists_weight_eq_index and independentBuilt:
`[propext, Classical.choice, Quot.sound]`. No sorryAx or new axiom.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual lake build Roth.Index, exit 0, session 88704 |
| definition_protected | pass | no def/abbrev/body edit |
| theorem_statement_protected | pass, approved generalisation | sole scoped DecidableEq omission; literal theorem signature lines unchanged; stronger proof and exact old-type recovery compiled |
| structure_gate | pass | four-line body; one existential witness with paired properties, no top-level conjunction API or long branch |
| naming_gate | pass | descriptive snake_case, no forbidden pattern; no rename needed |
| line_packing_gate | pass | two measured signature rows and complete-token arithmetic above |
| inequality_orientation_gate | pass | complete signature scan has no ≥/> |
| cumulative_no_unintended_breakage | owner checkpoint | internal callers passed module build; external MainLemma caller and whole-project cumulative gates are owned by the file owner |

Overall worker gates: pass. Full-project cumulative checkpoint is deliberately
not claimed here. No full build was run by this worker, as instructed.

New-identifier verification: no new proof identifier. Added DecidableEq is the
existing Lean class already present in the entry section; the scoped omit was
accepted by both the actual module build and complete native LSP.

## Simplify review

Native `/simplify` Skill invocation is unavailable in this environment. Performed
the available direct holistic review: the finite-set API is already direct,
no duplicated helper or redundant proof step remains, and no proof edit improves
the checked alternatives. Outcome: PASS-THROUGH by direct review; not claimed
as a native Skill-tool invocation. File-level final simplify review remains
with the owner.

## Buzz pass — target scope

Outcome: FAST-BOARD, budget 1000 ms. No proof performance edit.

The native lean_profile_proof attempt failed because its standalone extraction
did not preserve same-file dependencies/scoped omit syntax. A plain
`lake env lean --profile Roth/Index.lean` completed with exit 0 but printed
cumulative timings; those aggregate numbers are not used as target timings.
Fallback actual command completed with exit 0:

```
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean
```

Raw log: `/private/tmp/roth-index-exists-profile-trace.log`.
Parsed anchors: `/private/tmp/roth-index-exists-profile-table.json`, generated
by `/private/tmp/roth-index-profile-parse.py exists` after compiler completion.

| Declaration | Release line | Command | Proof | Anchored command plus async total | Dominant tactic |
|---|---:|---:|---:|---:|---|
| Roth.exists_weight_eq_index | 71 | 10.30 ms | 172.16 ms | 188.45 ms | obtain, 122.165 ms |

The total is attributed from named Elab.command/Elab.async trace roots, not
the compiler's cumulative category summary. No speedup claim is made.
No limits raised, no source profiling scaffolding introduced, no deferrals,
no new instance/attribute/generalisation proposed for performance.

## Step 6 — Result and checklist

Before: 6 declaration lines; after: 6 declaration lines. Four-line proof body
unchanged. Scoped omission adds one source line: file 268→269. Relative to
the original 21-declaration baseline, earlier helper inlining had expanded
this proof; that earlier work is not attributed to this worker.

Audit issues: one unused argument (two warnings), fixed. Rules applied to
proof: none; existing direct API and terminal simpa retained. Generalisation:
approved DecidableEq omission only. Renames-queued: none.
Comments-preserved: none present in proof; both existing docstring lines kept.
Refactoring needed: none. Owner retains shared report, cumulative compatibility,
full builds, project-end rename pass and final evaluation ownership.

- [✓] Step 1 — references read.
- [✓] Step 2 — all 24 audit items recorded.
- [✓] Step 2.5 — five actual search methods, failure disclosed.
- [✓] Step 2.6 — every binder probed, literature search recorded.
- [✓] Step 2.7 — all signature lines measured with arithmetic.
- [✓] Step 2.8 — inequality scan table recorded.
- [✓] Step 3 — all 42 golfing rules have status.
- [✓] Step 4 — mathematical reflection and alternatives considered.
- [✓] Step 5a — complete native diagnostics, no target warnings/errors.
- [✓] Step 5b — actual module build and diff gates recorded.
- [✓] Step 6a — no rename needed, no queue mutation.


## Owner checkpoint d06

Frozen SHA256 `a872711cb58cfec0e2bb6b24ba400001fb4f3d3e6518276b3f6f47f46f25352b`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session35801 exit0, `/private/tmp/roth-index-d06-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval56008 both exit0(147.16s/34.47s),
Index+Theta hashes stable; `/private/tmp/roth-index-d06-{full,leaneval}.log`.
Worker complete Index LSP: success=true partial=false timed_out=false, 0target diagnostics/26unrelated warnings. External MainLemma complete native LSP functions cell146: success=true partial=false timed_out=false, 0errors/3inherited warnings, noinfos, no faileddependencies. MainLemma:522 caller accepted; raw /private/tmp/roth-index-d06-mainlemma-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
