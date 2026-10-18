# Fresh independent audit: `eq_sum_aeval_basis_coeffNone_aux`

Initial audit recorded before any source edit. Scope is this private helper only, frozen original `/private/tmp/roth-d21-eq_sum_aeval_basis_coeffNone_aux.lean.txt`, original lines 248–273 (26 physical declaration lines, 18 proof lines after `:= by`; verified with `wc -l` and direct line enumeration). No public changes or new helpers authorized by this audit.

The proof deliberately consumes the existing expansion `hP`, expands each coefficient by `Basis.sum_repr`, exchanges the two finite sums, and evaluates each monomial. Recomputing `hP` would duplicate caller work. The local `a` abbreviates a repeated dependent basis coordinate; `hexp` records a mathematical stage, and `h` needs transport through subtype coercion.

Initial punch list: test removing `classical`; test narrower basis-coordinate transport and final algebraic automation; inspect signature packing; probe all effective binders and `CommSemiring` parents. No initial mathematical or visibility defect. Literature search is exempt because this is a private auxiliary lemma. Completion evidence and all audit/golf tables follow below when requests finish.

## Initial 24-item audit

| Item | Finding/action |
|---|---|
| 1 Lint | Native live goal resolves; obtain complete unfiltered module diagnostics at final gate. |
| 2 Have scan | `hexp`: retained coefficient expansion stage; `h`: subtype transport requires rewriting, test combining the two narrow rewrite steps. `a`: repeated coordinate abbreviation, retain. |
| 3 Options | No local options or limit overrides. |
| 4 Simp squeeze | `simp_rw [hexp, map_sum, Finset.mul_sum]` explicitly controlled. Terminal `simpa only` deliberately narrow: broad simp rewrites basis representation to `True`, verified by native LSP. |
| 5 Naming | Describes equality, finite sum, evaluation, basis, and `coeffNone`; `_aux` private suffix; no forbidden numerical or abbreviated pattern. |
| 6 Packing | Signature width table below; dependent basis and nested polynomial conclusion require expression-level wrapping. |
| 7 By placement | `:= by` ends signature; local `fun ν ↦ by` ends line. |
| 8 Format | Two-space proof indentation, no blank proof lines or semicolons, sequential rewrites separated by changes of subgoal. |
| 9 Comments | No original inline comments to remove. |
| 10 Docstring | Private auxiliary lemma: no public docstring requirement. |
| 11 Visibility | Private, file-local, auxiliary; correct. |
| 12 Structure | 18 proof lines including `classical`; no conjunction, no branches, two short nested sum congruences. Below 50-line ceiling. |
| 13 Mathlib | All five methods executed; partial matches `Module.Basis.sum_repr`, `Polynomial.aeval_eq_sum_range`. Existing proof already uses the former; latter would re-expand and track coefficient bounds unnecessarily. |
| 14 Junk def | Lemma, no data definition. |
| 15 Exists lemma | Equality, no trivial existential wrapper. |
| 16 Show/change | Existing `change` exposes local abbreviation definitionally. No `show`. |
| 17 Push neg | None. |
| 18 Generalise | Explicit compiler probes for τ, R, class, P, n, l, hP, b and class parents. No inherited Fintype/DecidableEq parameters in actual goal. Universes already polymorphic. |
| 19 Inequality | No `<`, `>`, `≤`, `≥` propositions in the signature or hypotheses. |
| 20 Normal form | Canonical polynomial equality to a finite separated sum, with basis coordinates. |
| 21 Syntax generality | Shared `hP` is the application-ready expansion. Preserve caller sharing rather than derive a new bound. |
| 22 Import fanout | No new imports. |
| 23 Casts | Fin→Nat powers/coefficients cross types; basis subtype→ambient polynomial is necessary; aeval argument annotation fixes coefficient algebra. No newly introduced coercions. |
| 24 Instance name | Not an instance. |

Initial action list: remove `classical` only if full proof verifies; combine narrow subtype transport if it verifies; preserve all API, existing comments and shared expansion. No new helpers proposed.

## Five-method search

Raw native responses: `/private/tmp/roth-d21-helper3-search.json`; source search: `/private/tmp/roth-d21-helper3-source-search.log`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | Expand polynomial coefficient basis representation sum aeval polynomial | `Polynomial.aeval_eq_sum_range`, `expand_eq_sum`, evaluation sums; partial matches. |
| B Loogle | `Module.Basis.sum_repr` | Exact basis expansion API, already used. |
| C LeanSearch | basis expansion of multivariate polynomial using univariate evaluation and sum of coefficients | Evaluation sum API, partial matches only. |
| D Mathlib source | `sum_repr`, `sum.*repr`, `repr.*sum`, `aeval.*sum`, `sum.*aeval`; full `eq_sum_aeval_basis_coeffNone` | `Basis.sum_repr`, `sum_repr_mul_repr`; no full-name match. |
| E Local name patterns | `sum_repr` | Source matches include `Basis.sum_repr` and bilinear forms; index unavailable, so no symbol-index absence claim. |

Auxiliary variants checked: `sum_repr_mul_repr`, `aeval_eq_sum_range'`; these address basis products or evaluation bounds rather than the two-index basis/monomial interchange. Common-equivalents table: basis/finite-sum bucket; no disguised topology or quotient concept. Conclusion: partial matches; retain the substantive assembly on the existing Mathlib basis API. Whole-goal `exact?` timed out, so no claim of a compiler-certified absence. The helper is more than a 1–3-call wrapper: it transports dependent coordinates and combines two distinct expansions. No new public API extraction is needed: one coercion pass plus sum congruences is ordinary assembly, with no repeated wrapper round trip or typeclass plumbing.

## Signature packing and inequalities

Reference: `/private/tmp/roth-d21-helper3-original.log`, actual `#check @probe` with `set_option format.width 100`. Original signature and final signature are byte-identical. Token groups below are complete binders or coherent expression continuations, not arbitrary word fragments.

```lean
@probe : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] {P : MvPolynomial (Option τ) R} {n l : ℕ},
  P = ∑ ν, X none ^ ↑ν * (rename some) (coeffNone P ↑ν) →
    ∀ (b : Module.Basis (Fin l) R ↥(Submodule.span R (Set.range fun ν => coeffNone P ↑ν))),
      P =
        ∑ ρ,
          (Polynomial.aeval (X none)) (∑ ν, Polynomial.C ((b.repr ⟨coeffNone P ↑ν, ⋯⟩) ρ) * Polynomial.X ^ ↑ν) *
            (rename some) ↑(b ρ)
```

| Signature line | Width | Next group width | Arithmetic | Action |
|---|---:|---:|---|---|
| 248 | 75 | `{P : MvPolynomial (Option τ) R}` 31 | 75 + 1 + 31 = 107 | Keep |
| 249 | 45 | `hP` binder 76 | 45 + 1 + 76 = 122 | Keep |
| 250 | 80 | basis binder prefix 27 | 80 + 1 + 27 = 108 | Keep |
| 251 | 31 | dependent span continuation 71 | 31 + 1 + 71 = 103 | Keep |
| 252 | 77 | conclusion prefix 82 | 77 + 1 + 82 = 160 | Keep |
| 253 | 86 | coefficient monomial prefix 73 | 86 + 1 + 73 = 160 | Keep |
| 254 | 81 | polynomial power continuation 68 | 81 + 1 + 68 = 150 | Keep |
| 255 | 78 | none; `:= by` already packed | n/a | Keep |

All lines have width ≤100, including the 100-character `hexp` proof line. Inequality occurrence table: zero inequality propositions in every binder, hypothesis and conclusion; no reversed `≥`/`>` occurrence, and no `_ge_`/`_gt_` name.

| Location scanned | Inequality occurrence | Required rewrite |
|---|---|---|
| All eight signature lines and every effective binder/hypothesis | None | None |

## All 42 golf rules

| Rule | Concrete status |
|---|---|
| 1.1 `by exact` | n/a: no trivial proof wrapper. |
| 1.2 `by rfl` | n/a: substantive sum identity. |
| 1.3 `rw; exact` | n/a: no such sequence. |
| 1.4 `simp; exact` | Combined `rw [Submodule.coe_sum] at h` with following `simpa only` into one narrow terminal `simpa only`. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: equality, no constructor sequence. |
| 1.7 apply/exact | n/a: none. |
| 1.8 by_contra! | n/a: no contradiction. |
| 1.9 eta reduction | `fun ν ↦ by` and sum-congruence functions introduce essential variables; not eta wrappers. |
| 1.10 single-use have | `h` cannot be removed without long nested transport expression; retained as readable input to the now single coercion simplification. |
| 1.11 refine/fun | Already used for both sum congruences. |
| 1.12 redundant show | n/a: none; `change` exposes abbreviated coordinates. |
| 1.13 have projections | n/a: no `.1`/`.2`. |
| 1.14 consecutive rw | Rewrites are separated by sum congruences; existing map rewrites already merged. |
| 1.15 terminal simp unsqueeze | Native broad transport `simpa using …` fails because `Basis.sum_repr` simplifies the source to `True`; narrow coercion list retained. |
| 1.16 nonterminal simp squeeze | Existing `simp_rw` carries explicit list; no bare nonterminal simp. |
| 1.17 dot notation | `b.sum_repr`, `h.symm` already used. |
| 1.18 `<|` | n/a: no trailing parenthesized tactic/function argument suitable for replacement. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial exists | n/a: not an existential helper. |
| 2.1 whole grind | Native attempt fails, cannot derive basis reorganization automatically. |
| 2.2 before grind | n/a: no grind retained. |
| 2.3 simpa consolidation | Applied narrow sum/smul coercion consolidation. |
| 2.4 fun_prop | n/a: no analytic property. |
| 2.5 positivity | n/a: no ordered/nonzero goal. |
| 2.6 gcongr | n/a: no monotonicity/inequality. |
| 2.7 lia/omega | n/a: no arithmetic proposition; Fin exponents are symbolic polynomial atoms. |
| 2.8 aesop | Native whole-proof attempt reaches recursion limit; rejected, no limit change. |
| 2.9 norm_num/cast | n/a: no numeric computation/cast identity. |
| 2.10 decide | n/a: arbitrary semiring equality, not finite computation. |
| 2.11 field_simp | n/a: no denominator, no field. |
| 2.12 linear_combination | Actual final live goal attempt fails `IsRightCancelAdd` synthesis over general CommSemiring. |
| 2.13 wlog | n/a: no duplicate branches. |
| 2.14 calc/term | n/a: no two-step calc; full proof is not a simple composition. |
| 2.15 shared `<;>` | n/a: one goal at each congruence step, no parallel branches. |
| 3.1 erw | n/a: only rw. |
| 3.2 legacy function tactics | n/a: none. |
| 3.3 omega→lia | n/a: neither used. |
| 3.4 rcases rfl | n/a: none. |
| 3.5 attributes | No attributes: basis-dependent expression duplicates indices on RHS and is unsuitable as a global simp normal form. |
| 3.6 simp_all | n/a: none. |
| 3.7 limits | No options or profiler scaffolding introduced. |

Further holistic simplification: final goal is only permutation/reassociation of three factors. Native `ac_rfl` closes without diagnostics, replacing `ring`; `simp [mul_comm, mul_left_comm, mul_assoc]` also closes but warns that `mul_assoc` is unused. Removed unnecessary `classical`, verified by a complete isolated proof. Native raw local attempts are `/private/tmp/roth-d21-helper3-transport.json` and `/private/tmp/roth-d21-helper3-end-attempts.json`. A first final-tactic request used line 272, the continuation of the prior rewrite list, and produced parser errors; this was a position error, not tactic evidence, and the corrected request used final line 271. The reported algebraic outcomes are from that corrected request.

Step-back review: no one-tactic whole proof succeeds (`rfl`, `grind`, `aesop`, `simp`, `exact?` tried); broad automation obscures dependent basis terms and can hit heartbeat/recursion limits. Retain the explicit mathematical stages. `hP` is intentionally shared input. New helpers: none. Renames: none. Public proposals: none from this worker.

## Every-binder mechanical generalisation

Isolated source and compiler logs: `/private/tmp/roth-d21-helper3-{case}.lean` and `.log`, generated by `/private/tmp/roth-d21-helper3-probes.py`. All probes disable `autoImplicit` to prevent accidental recreation of a deleted type parameter. These are proof/signature dependency tests, not claims that every deleted hypothesis has a mathematical counterexample.

| Effective binder | Use | Candidates tested/considered | Verification/result |
|---|---|---|---|
| `{τ : Type*}` | Both polynomial variable types and `rename some` | Drop; universe polymorphism | Drop gives unknown `τ`; already universe-polymorphic. A transient missing-import failure was excluded and retried in `retry-drops.log`. |
| `{R : Type*}` | Scalar semiring, basis coordinates and polynomial coefficients | Drop; universe polymorphism | Drop gives unknown `R`; already universe-polymorphic. |
| `[CommSemiring R]` | `MvPolynomial`, polynomial aeval and commutation | Drop, `[Semiring R]`, `[NonUnitalCommSemiring R]` | All fail required class synthesis; retained. Dropped-class transient import failure was excluded and retried in `retry-drops.log`. |
| `{P : MvPolynomial (Option τ) R}` | Equality's LHS and all coefficients | Drop | Unknown `P`; no pointwise analogue of a polynomial value parameter. |
| `{n : ℕ}` | `Fin (n+1)` degree-index family | Drop; arbitrary finite index considered | Unknown `n`; arbitrary index cannot replace natural exponents without adding an exponent map and restating the lemma. No small mechanical weakening. |
| `{l : ℕ}` | Index type of the basis and separated sum | Drop; arbitrary finite basis index considered | Unknown `l`; changing the index structure is a restatement, not removal of an unused parameter. Current caller requires `Fin l`. |
| `hP` | The already computed polynomial expansion | Drop; point-localise/strict→weak | Dropping leaves unknown `hP` at `conv_lhs`; no strict inequality or global function property to weaken. Recomputing expansion would discard shared caller work and require a new degree hypothesis. |
| `b` | `repr`, coordinates and spanning basis vectors | Drop; weaken to family | Unknown `b`; a family has no `repr`, so replacing it would change the conclusion and add a spanning reconstruction hypothesis. |

Inherited `[Fintype τ]` and `[DecidableEq τ]` are already omitted: the actual native goal and compiled independent `#check` show neither is an effective binder. Thus no silent drop test is claimed for them. Proof-local `classical` successfully removed. No redundant decidability parameter remains.

Literature status: n/a, private declaration; web and external math-MCP literature search exempt under the explicit scope rule. Inversion check: no fixed concrete witness is named; `P` and `b` are arbitrary and their coefficients occur in both abbreviation and expansion stage. An arbitrary coefficient family or arbitrary finite basis index would require a new syntactic contract and provides no further use in this file; no public restatement proposed or applied.

## Verification gates and phase checklist

The statement comparison in `/private/tmp/roth-d21-helper3-diff.patch` and generation script verifies the exact original signature is unchanged. Original isolated proof `/private/tmp/roth-d21-helper3-original.lean` compiled independently. Final `/private/tmp/roth-d21-helper3-independent-final.lean` restates that exact original type and proves it without calling the target or caller; its log also checks built actual constants by exact suffix. The first attempted final check raced a rebuild removing its `.olean`; that failed import was excluded, then the identical check reran successfully after the build.

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` succeeded (exit 0): `/private/tmp/roth-d21-helper3-build-final.log`. Final native unfiltered module LSP is complete (`partial=false`, `timed_out=false`, no failed dependencies), with 0 errors and 31 baseline warnings, none on the target: `/private/tmp/roth-d21-helper3-lsp-final.json`. The original proof, final independent proof, actual private helper, and actual public caller all use only `propext`, `Classical.choice`, `Quot.sound`: `/private/tmp/roth-d21-helper3-original.log` and `/private/tmp/roth-d21-helper3-independent-final.log`.

| Gate | Result |
|---|---|
| Module build | Pass, actual module build exit 0. |
| Definition protected | Pass, no definition edits. |
| Theorem statement protected | Pass, exact original signature preserved. |
| Structure | Pass, final proof 16 lines, no conjunction or long branch. |
| Naming | Pass, descriptive private auxiliary name; no forbidden pattern. |
| Packing | Pass, eight signature rows above; max line width 100. |
| Inequality orientation | Pass, zero inequality occurrences. |
| Documentation/comments | Pass, no source documentation/comment changes. |
| Scope | Pass, only owned helper proof changed; no imports, new helpers, caller changes, public APIs or Git mutations. |

| Completion phase | Evidence |
|---|---|
| 0 Doctor | Supplied actual 631.408 ms baseline and fresh module build; responsive native LSP. |
| 1 Prepare | Original helper snapshot, current caller context and required reference documents read. |
| 2 Audit | Initial audit and all 24 findings recorded before mutation. |
| 3 File-level fixes | Not this worker's scope; no file-wide edit. |
| 4 Deep golf | Five searches, per-binder probes, all 42 rules, signature/inequality artifacts. |
| 5a Refactor | Narrow coercion consolidation; no extraction/removal or API change. |
| 5b Rename | No naming defect or rename queue item. |
| 6 Final gates | Actual module, complete native LSP, independent exact-original proof, actual standard axioms. |
| 6.5 Simplify | Direct holistic review led to unnecessary-classical removal and `ring`→`ac_rfl`; no available separate built-in simplify callable. |
| 6.6 Buzz | Actual repository anchored final profiling below, after all compiler/MCP jobs drain. |
| 7 Report | This dedicated report plus exact worker diff, line arithmetic and source freeze below. |

Applied change: 26→24 physical declaration lines, 18→16 proof lines; three semantic proof stages preserved. Source line count at the helper-only freeze is 573. This is a fresh audit of a newly introduced helper, not another original-declaration audit count. Parent owns cumulative original compatibility, project/LeanEval builds and publication.

All isolated probe processes have completed: `/private/tmp/roth-d21-helper3-probe-summary.json`. Original proof, removal of `classical`, and consolidated narrow transport compiled (exit 0); dependency-removal, class-parent, and final `linear_combination` probes failed (exit 1) as documented. The excluded early drop-class/drop-τ import races were rerun together in `/private/tmp/roth-d21-helper3-retry-drops.lean` and `.log`, producing the expected class/unknown-variable errors. Failed exploratory proof artifacts are not accepted axiom certificates; only the successfully compiled independent-final and actual-built checks are certificates.

Casts in the worker diff: 0 added, 0 dropped; all original subtype and Fin→Nat crossings and aeval target annotations retained. No warning suppression, limits, new helper, source comment change, definition change, public type change, or instance modification.

## Buzz results and final freeze

Supplied actual original baseline: helper outer command 115.476 + outer async proof 515.932 = 631.408 ms, `/private/tmp/roth-d21-final-profile1.log` anchors 330269/330508. Actual final repository command (both sweeps):

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Both sequential sweeps exited 0 and were isolated after every other worker/compiler/MCP request drained. The second was required because the first helper and caller totals were ≥750 ms. Only outer command plus outer async proof is counted; nested elaboration, kernel and tactic nodes are not added again. Exact anchors are saved in `/private/tmp/roth-d21-helper3-profile-anchors.json`.

| Actual declaration | Sweep | Outer command / log line | Outer async / log line | Total ms |
|---|---|---|---|---:|
| Private target | final | 131.503 / 315794 | 653.721 / 316031 | 785.224 |
| Public caller | final | 37.449 / 397258 | 807.480 / 406782 | 844.929 |
| Private target | repeat | 105.239 / 315769 | 642.174 / 316006 | 747.413 |
| Public caller | repeat | 31.590 / 397164 | 821.747 / 406697 | 853.337 |

Raw logs: `/private/tmp/roth-d21-helper3-profile-final.log` and `/private/tmp/roth-d21-helper3-profile-repeat.log`. Every target/caller sample is below the 1000 ms budget. Caller remains borderline after its repeat; parent will independently repeat final cumulative profiling. No whole-project or target performance improvement is claimed: final target timings exceed the supplied earlier sample. The retained changes remove redundant proof work and use a direct associativity/commutativity certificate, while remaining within the specified budget.

All Lean, native MCP, compiler, build and profiling requests launched by this worker are now drained; both final profile sessions returned exit 0. Source SHA256: `36a381873357317a18cc528ac03d6d55739d5487e00c3daa8fbf568d9dcdbc17`. Final owned declaration lines 248–271; whole source `wc -l` 573. All source ownership is revoked: this worker is report-only and will perform no further source edits. No pending proposal from this audit; public instance menu, wrapper deletions and Domain coefficient weakening remain outside this worker's scope.
