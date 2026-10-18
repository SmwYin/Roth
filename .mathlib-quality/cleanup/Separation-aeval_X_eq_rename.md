# Fresh declaration audit: Roth.aeval_X_eq_rename

Original declaration 11; worker owns only this declaration. Starting HEAD ccfe4fc,
586 lines, 27 retained declarations. Parent provides baseline complete LSP:
0 errors, 31 warnings, and actual-module profile command 31.720 ms plus async
169.815 ms = 201.535 ms in `/private/tmp/roth-separation-d10-final-profile.log`.
This initial audit is written before any source edit.

Read both Lean 4 and mathlib quality skills, full golfing and proof-patterns
references, search/generalisation/gates/style/naming/profiling references and
cleanup Phase 4. Native Lean tools available; no delegation.

## Initial 24-item audit

| Item | Concrete finding / action |
| --- | --- |
| 1 Lint | No target-specific baseline warnings reported; final complete LSP required. |
| 2 Have scan | `hsymmX` at 129 has a proof, used once at 137; `h` at 135 has no `by`, used once at 138. Inline `h`; the mathlib equivalent eliminates both. |
| 3 Set option | None in target. |
| 4 Simp squeeze | `simp` inside the monomial index equality and `simp [hsymmX]` are terminal. No nonterminal bare simp. |
| 5 Naming | `aeval_X_eq_rename` names the two operations and their equality; capital X denotes the actual API generator, no forbidden abbreviation or numerical scheme. No rename needed. |
| 6 Line packing | Initial three signature lines measured below; repack the conclusion to the first line if the complete expression fits, keeping exact type. |
| 7 By placement | Existing `by` ends conclusion line. Direct term proof planned. |
| 8 Format | Standard two-space tactics. No haveI/letI. |
| 9 Comments | No inline proof comments. Preserve all three docstring lines exactly. |
| 10 Docstring | Existing explanation identifies one-variable embedding and source §4 Lemma 4-2. Preserve. |
| 11 Visibility | Public contract explicitly preserved by dispatch. |
| 12 Structure | 10 proof-body lines, no conjunction or branch; no helper extraction needed. |
| 13 Mathlib | Exact equivalent `Polynomial.toMvPolynomial_eq_rename_comp` found and independent direct application compiled. Retain public bridge under explicit contract; notify parent about possible future removal. |
| 14 Junk definition | Theorem, no data definition. |
| 15 Exists lemma | Public equality theorem, not a private single-use existential. |
| 16 Show vs change | Existing term-mode show in the monomial rewrite supplies an equality, not a tactic-mode goal annotation. Whole monomial calculation replaced using mathlib. |
| 17 Push neg | No push_neg occurrence. |
| 18 Generalise | Effective binders R, CommSemiring R, σ, i, f; τ/Fintype/DecidableEq absent. Probe every effective binder and parent weakening, preserve original public type. Literature search below. |
| 19 Inequality | None in signature, hypotheses, or proof; table below. |
| 20 Normal form | Equality from evaluation to variable rename is appropriate rewrite direction; bundled hom equality already mathlib canonical form. |
| 21 Syntax generality | Explicit i and f support rewriting at existing callers. No public restatement applied. |
| 22 Import fanout | No import needed; exact equivalent already available transitively. |
| 23 Casts | Existing ascriptions fix MvPolynomial target, coefficient type and Finsupp index; monomial proof ascriptions disappear with replacement. No coercion changes. |
| 24 Instance name | Theorem, no instance declaration. |

## Five actual search methods

| Method | Actual query / result |
| --- | --- |
| A Lean Finder | `polynomial evaluation at multivariate variable equals renaming uniqueAlgEquiv inverse`: exact `Polynomial.toMvPolynomial_eq_rename_comp`, plus eval₂ and unique equivalence facts. |
| B Loogle | `MvPolynomial.uniqueAlgEquiv`: six results including `eval₂_const_uniqueAlgEquiv_symm`. |
| C LeanSearch | `polynomial aeval variable mvpolynomial rename unique algebra equivalence`: `rename_polynomial_aeval_X` and rename API. |
| D Source rg | Full untruncated `aeval_X_eq_rename` mathlib search has no literal hit; Equiv source reveals toMvPolynomial equality at 891. Presence established, no absence claim. |
| E Native local | `uniqueAlgEquiv`: seven textual results; index unavailable, so not evidence of indexed absence. Source and compiled #check confirm candidates. |

Six search rules: exact equivalent found; use mathlib directly in retained proof.
Public deletion is a proposal to parent, not applied because explicit original contract
preservation takes precedence over wrapper deletion. Auxiliary variants searched;
typeclass-based formulation already used; no custom predicate or new mathlib import.
No claim that mathlib lacks the result. Common-equivalents lookup has no relevant
topological/finite/bornological disguise.

## Actual literature search

Web queries: `polynomial ring one variable evaluation universal property substitution
multivariate polynomial` and `Takloo Bighash Yin Formalizing Roth theorem Lemma 4-2 polynomial`.
Primary course sources found: Matthew Macauley, Clemson, Polynomial Rings §2.3,
https://www.math.clemson.edu/~macaule/classes/f18_math8510/slides/f18_math8510_lecture-rings-03_h.pdf
and Tom Leinster's algebra notes hosted at McGill,
https://www.math.mcgill.ca/darmon/courses/24-25/algebra4/leinster.pdf .
Search extracts describe uniqueness of evaluation homomorphisms fixing coefficients
and assigning generators. This supports the bundled hom equality formulation; it
introduces no extra finite-variable, decidability, nonzero, domain or field assumptions.
No claim that the second query found the exact cited Roth manuscript. Existing local
source citation remains unchanged. The broader algebra universal property is already
represented in mathlib; no new public generalisation proposed.

## Initial inequality occurrence table

| Region | Occurrences | Action |
| --- | --- | --- |
| Signature and all hypotheses | 0 of ≥, >, ≤, < | None |
| Entire proof | 0 comparison operators | None |
| Name | No _ge_ or _gt_ | None |

## Generalisation status: every effective binder

Native `lean_run_code` actually elaborated all six negative variants, with
`autoImplicit false`; raw code and complete diagnostics:
`/private/tmp/roth-separation-d11-binder-probes.json`. These were isolated probes,
never applied to the public source. The native scratch server reported an import
staleness info while the module build ran; positive and axiom gates are also repeated
against the fresh built module using the compiler below.

| Binder | Use | Candidate actually tried | Verified outcome |
| --- | --- | --- | --- |
| `{R : Type*}` | Coefficient type in f and equivalence | Drop R | Compiler: unknown R, three occurrences. Already universe polymorphic; no widening beyond Type*. |
| `[CommSemiring R]` | rename, aeval and uniqueAlgEquiv | Drop; weaken to Semiring | Drop: Semiring and CommSemiring synthesis fail. Semiring: CommSemiring synthesis fails in target. NonAssocSemiring is weaker than this failed parent and cannot type this API. |
| `{σ : Type*}` | Variable type and i | Drop σ | Compiler: unknown σ in binder and target. Already universe polymorphic. |
| `(i : σ)` | Chosen target variable | Drop i | Compiler: unknown i in both sides and proof. No proposition to localise or weaken. |
| `(f : Polynomial R)` | Polynomial being embedded | Drop f | Compiler: unknown f in both sides and proof. No proposition to localise or weaken. |

Section τ, Fintype τ and DecidableEq τ are absent from the original and final
effective signature, confirmed by `#check @Roth.aeval_X_eq_rename`; there is nothing
to remove. Strict-to-weak, point-localisation, nonzero/domain/field weakenings and
bundled-hypothesis splits do not apply: none occur. Inversion review identifies the
already-existing abstract mathlib hom equality rather than any missing theorem.
ChatGPT math MCP is unavailable (actual tool inventory has no chatgpt-math tool).
No public binder generalisation or pending instance removal is applied.

## Line packing: measured codepoints

Width-100 reference, actual `set_option format.width 100; #check @Roth.aeval_X_eq_rename`:

```lean
@Roth.aeval_X_eq_rename : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} (i : σ) (f : Polynomial R),
  (Polynomial.aeval (X i)) f = (rename fun x ↦ i) ((uniqueAlgEquiv R Unit).symm f)
```

Each next unit below is the full next application/equality side, keeping application
arguments together; the equality cannot share the binder line (66 + 1 + 45 = 112).
No hypothesis is unnecessarily separated from its neighbours.

| Signature line | Before chars | After chars | Next complete expression unit | Arithmetic | Action |
| --- | --- | --- | --- | --- | --- |
| 126 | 66 | 66 | LHS application and equality sign, 45 chars | 66 + 1 + 45 = 112 > 100 | Keep break |
| 127 | 49 | 49 | RHS application and :=, 62 chars (65 with by originally) | 49 + 1 + 62 = 112 > 100 | Keep break |
| 128 | 71 | 68 | Proof term, 63 chars, proof begins next line | 68 + 1 + 63 = 132 > 100 | Keep break |

Final term line 129 is 65 chars. No >100 codepoint line introduced. No statement
token changed other than removal of tactic introducer `by` at the proof boundary.

## All 42 golfing rules

| Rule | Concrete status |
| --- | --- |
| 1.1 by exact | Applied more generally: tactic proof replaced by direct congr_fun term. |
| 1.2 by rfl | Not applicable: original whole goal not definitional; internal rfl removed with obsolete calculation. |
| 1.3 rwa | No rw followed by exact of a rewritten hypothesis. |
| 1.4 simpa using | No matching simp/exact chain; direct mathlib term chosen. |
| 1.5 trailing rfl | Existing rfl follows rw, not simp; entire monomial block removed. |
| 1.6 constructors | No constructor proof. |
| 1.7 exact application | Final proof is one direct application; no apply/exact chain remains. |
| 1.8 by_contra! | No contradiction or push-neg chain. |
| 1.9 eta reduction | Constant lambda `fun _ : Unit => i` cannot eta reduce; retained exact contract. |
| 1.10 inline have | Applied: single-use h replaced by direct mathlib equality; hsymmX obsolete too. |
| 1.11 refine fun | No apply/intro chain. |
| 1.12 redundant show | Removed term-mode show along with monomial plumbing, not changed to tactic change. |
| 1.13 obtain | No pair projections. |
| 1.14 merge rw | One rw block originally, none remain. |
| 1.15 terminal simp | Both old simp calls terminal and unsqueezed; removed with old proof. |
| 1.16 nonterminal simp | None present. |
| 1.17 dot notation | congr_fun is the established namespace operation on hom equality; final term clear. |
| 1.18 less parentheses | Existing nested parentheses around equality theorem application are needed as congr_fun argument; no trailing tactic/lambda parentheses to drop. |
| 1.19 push Not | No push_neg. |
| 1.20 existential inline | Equality theorem, no private existential witness helper. |
| 2.1 grind | Actually tried natively at original live goal; failed to close; stale trailing body also produced parsing errors. Direct equivalent compiles independently. |
| 2.2 delete before grind | No grind in original or final proof; whole-goal attempt already fails. |
| 2.3 simpa consolidation | Native attempted eval₂ rewrite variant encountered stale-body error and deprecated rename_eq; not adopted. Direct term is shorter and compiled. |
| 2.4 fun_prop | No continuity, measurability or differentiability proposition. |
| 2.5 positivity | No order, positivity or nonzero goal. |
| 2.6 gcongr | No inequalities. |
| 2.7 lia/omega | No arithmetic goal; numeral-index subgoal already closed by simp in original. |
| 2.8 aesop | Actually tried at live goal; exhaustive search left the equality unsolved and trailing old-body parse errors. Not adopted. |
| 2.9 norm_num/norm_cast | No concrete arithmetic or cast equality goal; old trivial index subgoal disappears. |
| 2.10 decide | Symbolic polynomial equality over arbitrary semiring is not finite decidable computation. |
| 2.11 field_simp/ring | No denominators or field operations. |
| 2.12 linear_combination | No ring/ring_nf ending or relevant algebraic hypotheses. |
| 2.13 wlog | No symmetric branches. |
| 2.14 collapse calc | No calc. |
| 2.15 multiple goals | Direct term has no generated parallel subgoals. |
| 3.1 erw to rw | No erw. |
| 3.2 fun_prop legacy | No continuity/measurability tactic. |
| 3.3 omega to lia | No omega, already inapplicable under 2.7. |
| 3.4 rcases rfl | No rcases. |
| 3.5 automation attrs | No new simp/grind rule: broader hom equality already mathlib API; avoid adding a redundant public rewrite attribute. |
| 3.6 simp_all | No contextual simp_all chain; one direct term needs no automation. |
| 3.7 heartbeat limits | None present or added. |

Original live exact? was actually attempted and hit the normal 200000 heartbeat
budget. Bare simp reduced to an eval₂ identity but did not close. The multi-attempt
tool replaced only the first tactic line, leaving following original-body tokens;
those additional parsing errors are recorded as tool-context limitations, not clean
whole-proof experiment results. Successful independent complete-snippet compilation
is the positive replacement evidence.

## Step-back review and simplify

The right abstraction is equality of the two algebra homomorphisms, already supplied
by mathlib. Applying that equality to f removes all custom generator/monomial work.
Term mode is shorter and clearer than one `exact` tactic. There are no remaining have
blocks, redundant rewrites, duplicated skeletons, imports, casts or helper candidates.
The final proof uses neither itself nor another Roth bridge. No new private helper
requires independent audit. The unavailable built-in simplify tool is replaced by
this explicit holistic review: PASS-THROUGH, no additional issue found.

## Concrete unapplied API option

Removing the public bridge would require substituting
`AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f` at callers.
Source search finds four Separation use lines (one line has two uses) and two Theta
use lines (490 and 574). Parent explicitly instructed retaining the bridge and docs,
and confirmed this after notification; no deletion, caller edit, or Theta edit applied.
This is a concrete optional public API proposal, not a blocked cleanup task.

## Worker verification evidence

`/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0; complete raw output
`/private/tmp/roth-separation-d11-build.log`: Build completed successfully (1876 jobs).
Complete unfiltered native module LSP saved to
`/private/tmp/roth-separation-d11-final-lsp.json`: partial=false, timed_out=false,
success=true, 0 errors, 31 warnings, no failed dependencies. No warning at target.
Header metadata and pending public instance warnings are explicitly preserved.

Native isolated exact ORIGINAL type assignment and independent non-self proof saved
to `/private/tmp/roth-separation-d11-independent.json`. Both compile successfully.
Repeated with fresh built artifacts via
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-separation-d11-independent.lean`,
exit 0, log `/private/tmp/roth-separation-d11-independent.log`. Actual built target
and independent proof both print precisely `[propext, Classical.choice, Quot.sound]`.
There are no affected private declarations. Parent owns the whole-original/public
compatibility and every-retained-declaration cumulative axiom gates; not duplicated.

| New identifier | Verification | Result |
| --- | --- | --- |
| Polynomial.toMvPolynomial_eq_rename_comp | Native local search (warming index, positive source hit), Equiv.lean:891, compiled #check and independent application | Pass |
| AlgHom.congr_fun | Existing source identifier; compiled #check and final application | Pass |

Search raw responses: `/private/tmp/roth-separation-d11-search-{finder,loogle,search,local}.json`.
Source diff checks: `git diff --check` exits 0; only owned declaration proof changes.
All three docstring lines byte-preserved; zero inline comments before and after.
No definition, public binder, import, pin, attribute, limit or instance changed.

| Diff gate | Result |
| --- | --- |
| lake_build_file | Pass, actual command and exit 0 above |
| definition_protected | Pass, no definition edits |
| theorem_statement_protected | Pass, original effective type assignment compiles |
| naming_gate | Pass, descriptive equality name, no forbidden patterns |
| structure_gate | Pass, 10 proof-body lines to 1; no branch or conjunction |
| line_packing_gate | Pass, measured full signature table above |
| inequality_orientation_gate | Pass, zero reversed inequalities |
| cumulative_no_unintended_breakage | Exact target type and module pass; full-project/cumulative gate belongs to parent after freeze |

Phase 5a: proof-only replacement with existing mathlib equality; optional public removal
reported but unapplied. Phase 5b: no rename queued or applied, zero caller files edited.
File-level changes: none; preserved header and docs. No forbidden proof trust mechanism,
warning suppression or profiling scaffold introduced.

## Eleven completion steps

- [x] Step 1: references read.
- [x] Step 2: full 24-item audit written before edits.
- [x] Step 2.5: five actual search methods and six-rule decision recorded.
- [x] Step 2.6: every effective binder, failed weakening, literature and inversion reviewed.
- [x] Step 2.7: every signature line measured, width-100 compiled reference printed.
- [x] Step 2.8: inequality occurrence table printed.
- [x] Step 3: all 42 golfing rules given concrete statuses.
- [x] Step 4: step-back review and holistic simplify pass done.
- [x] Step 5a: complete unfiltered native LSP, independent proof and actual axioms pass.
- [x] Step 5b: actual module build and diff gates recorded; parent-scoped gates clearly assigned.
- [x] Step 6a: no renames needed; no sidecar write.

## Size arithmetic

Owned declaration 13 lines (126–138) to 4 (126–129), saving 9.
Proof body 10 lines to 1. File `wc -l`: 586 to 577, saving 9.
`git diff --numstat -- Roth/Separation.lean`: 2 added, 11 removed, net -9.
Retained declarations: 27 before and after. No claim of whole-project performance gain.

## Buzz pass: actual module profile

Actual repository command, exit 0:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Raw `/private/tmp/roth-separation-d11-final-profile.log`, parser output
`/private/tmp/roth-separation-d11-final-profile.log.json`, produced by the supplied
`/private/tmp/roth-separation-profile-table.py`. Actual final anchors:

- Log line 116174: `[Elab.command] [0.024091]`, containing this theorem and final term.
- Log line 119098: `[Elab.async] [0.018511] elaborating proof of Roth.aeval_X_eq_rename`.

| Declaration | Baseline command | Baseline async | Final command | Final async | Conservative final |
| --- | --- | --- | --- | --- | --- |
| Roth.aeval_X_eq_rename | 31.720 ms | 169.815 ms | 24.091 ms | 18.511 ms | 42.602 ms |

Baseline total 201.535 ms, final 42.602 ms. One command and one proof anchor each;
no nested nodes double-counted. FAST-BOARD: target far below 750 ms resweep threshold
and 1000 ms budget. No raised limits, no deferrals, no profiling scaffolding in source.
Only this target's cost is certified; no whole-project performance claim.

## Freeze and ownership release

Final source SHA256:
`9ca5d14b3bcfba066fa924fc0f6eca5aa5b13d88dbabeab9a281a749bbd689c1`.
All Lean/MCP/compiler/profile requests have completed and drained: native searches,
live attempts, negative probes, positive snippet, complete LSP, module build, fresh
independent compiler, and profile. No running worker request remains.

I explicitly revoke ALL source ownership, including this declaration and all call
sites, and become report-only. No further source edit after this freeze. Parent owns
Git/shared logs, sequential full project and separate LeanEval builds, whole-original
compatibility, cumulative actual axioms, exact-path commit and successful push.

## Owner cumulative publication gates

Source FROZEN SHA256 `9ca5d14b3bcfba066fa924fc0f6eca5aa5b13d88dbabeab9a281a749bbd689c1`; leaf ownership revoked and requests drained before owner gates. Owner probe `23627` exit0,42.59s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d11-compatibility.{lean,log,json}`. Owner build session `63999` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.32s/32.64s; source hash stable. `/private/tmp/roth-separation-d11-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
