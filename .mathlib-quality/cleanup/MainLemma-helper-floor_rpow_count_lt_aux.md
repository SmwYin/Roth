# Private helper cleanup: `Roth.floor_rpow_count_lt_aux`

This report covers only introduced helper5. It gives no original-declaration credit, does not complete original19 or MainLemma.lean, and does not claim a final GLOBAL all-row pass. Public `pigeonhole_count`, complete `main_lemma`, Main.lean, earlier helpers, comments, paper quotations, imports, declaration order, source/configuration pins, and rename queue are preserved. Owner retains Git, publication and shared-progress ownership. No child agent, Git command, shared-progress edit or rename write occurred.

## Source and first-draft provenance

The first compiling UNGOLFED helper was saved by original19 before its first compile: 18 declaration lines / 16 proof lines, helper SHA256 `60b56ea2ba4cd61c39a981bdf33d571bfad49052f2805813216ae528bfc67b39`, entire 753-line source `f26f151e0a00fa826acc404538f2ef7f7bd53dccb1cad52a0cbf43136a6ea8ae`. Those historical facts were read in full and actual copies freshly hashed; they do not substitute for this worker's fresh gates.

Selected source: **743 lines**; helper: **8 declaration / 6 proof lines**, saving 10 lines. Source SHA256 `3fd2eb2e69cf2e3fb112cdfe992dad74a1b2a1ded6c13e11c8b395b7070e6147`; helper with ONE final newline `98c198fa18f8f315d95f8fbebd01a907a221d0076b31c99d819ce64c2e6e45f5`. Exact candidate-v5 bytes were archived before compilation and installation. Reversing ONLY the helper recovers first-draft source f26f…; removing ONLY helper plus its separator recovers exact original18 734-line entry `45dba9b58a75de21900d1100d8eb255c9449d68162739b63b58d8607258657dc`. `selected-v5.json`, `helper-only.diff`, and `final-static.json` establish the scope.

## Baseline and final builds

Cache download: n/a, existing pinned imports available; no installation/version change. Standalone runLinter: n/a, no such executable configured in lakefile.toml; ordinary mathlib-standard linters ran through builds, native diagnostics and complete profile lint roots. Missing-header warnings are retained; no authors, year, copyright or license were invented.

| Gate / actual command | Before | Final |
|---|---:|---:|
| `/Users/ramin/.elan/bin/lake build Roth.MainLemma` | 42.745s, exit 0 | 47.415s, exit 0 |
| `/Users/ramin/.elan/bin/lake build` | 80.705s, exit 0 | 70.790s, exit 0 |
| Separate `lake build Roth.LeanEval` (root excludes Eval) | n/a baseline native Eval complete | 39.434s, exit 0 |

Every cited run has complete separate strict-UTF8 stdout/stderr, exact CLI/input/pin hashes, whole exit 0, no wall-clock timeout, source immutability and actual owned-process-group drain. All failures below remain separate rejected evidence.

## Final 24-item audit

| # | Item | Concrete final result |
|---|---|---|
| 1 | Lint | Before/final FULL UNFILTERED ML/Main/Eval native complete, nonpartial, nontimeout, zero errors/no failed dependencies. ML header warning; Main header and existing unused hδ/hQ/hc warnings; Eval none. No helper warning. |
| 2 | Have scan | Initial hu direct 2 uses retained; hsum terminal proof retained. Initial hfloor/hsq/hstrict/hrpow each used once and eliminated by upfront exponent normalization plus one arithmetic closing step. Final hu used by square positivity and floor bound, hsum once but has proof content. |
| 3 | Options | No per-declaration or new global limits/debug/scaffolding options. Default effective 200000 / 20000 / 512 verified. |
| 4 | Simp | Sole final simpa is terminal and unsqueezed. No nonterminal bare simp. |
| 5 | Naming | Descriptive snake_case, private `_aux`, correct `_lt_` orientation, no forbidden abbreviations/numeric pattern. No rename recommended/queued. |
| 6 | Packing | Measured complete signature table below; every helper line ≤100 codepoints. |
| 7 | By | Every by ends preceding line. |
| 8 | Format | Two-space proof indentation, no blank proof lines, no semicolon chain, no haveI/letI, one tactic per line. |
| 9 | Comments | No helper comments initially. All foreign comments/signposts/paper quotations exactly preserved by byte recovery. |
| 10 | Documentation | Private implementation: no docstring required or added. Existing documentation untouched. |
| 11 | Visibility | Classic dialect; private scalar implementation with no existing caller. Actual compiled inventory below. |
| 12 | Structure | Six proof lines, no conjunction, no branch; below ordinary ≤30 / branches≤10 thresholds. Private helper is not a module headline. No extraction or new subhelper. |
| 13 | Mathlib | Five actual methods plus guarded exact?/apply? probes performed; partial API matches used directly. No existing direct replacement found. Selected proof has genuine floor/strict-square content, not a 1–3-call convenience wrapper or missing coercion API workaround. |
| 14 | Junk def | n/a theorem, no def/abbrev added or altered. |
| 15 | Exists helper | n/a no existential. |
| 16 | Show/change | n/a none. |
| 17 | Push negation | n/a none. |
| 18 | Generality | Every outer and inner local hypothesis examined; certified countercases and status below. No new weakening selected. |
| 19 | Orientation | No ≥ or > in helper signature, hypotheses or local typed facts; every occurrence uses ≤/<. |
| 20 | Normal form | Natural floor count coerced once to real, shifted real base and real exponent 2*c match the prospective counting caller. Square form is internal. |
| 21 | Syntactic generality | Implicit x/c inferred from application; positive real base and c≥1 are direct caller premises. NNReal/positive subtype or abstract floor-free bound adds caller conversions/obligations. |
| 22 | Imports/fanout | No production import added. MeanInequalitiesPow already supplies the used law; other imports protected/outside this single-declaration scope. |
| 23 | Casts | One Nat→Real count bridge retained; its :ℕ annotation fixes natural arithmetic and the exact contract. Two repeated bridge occurrences disappeared with removed intermediate facts; no new redundant proof casts. Redundant scratch `(2 : ℝ)` was removed before selection. |
| 24 | Instance name | n/a no instance declaration. |

### Signature packing and inequality scan

Width-100 reference comes from final independent harness `#check @Roth.ExpectedH5.expectedH5`, whose FULL actual TYPE is independently AST-equal/isDefEq to the actual private helper, including all written/inner binder names/order/BinderInfo/universes.

```lean
@Roth.ExpectedH5.expectedH5 : ∀ {x c : ℝ}, 0 < x → 1 ≤ c → ↑(2 * ⌊x ^ c⌋₊ + 1) < (x + 1) ^ (2 * c)
```

| Signature line | Codepoints | Next complete expression group | Arithmetic | Action |
|---|---:|---|---|---|
| 363 | 75 | `((2 * ⌊x ^ c⌋₊ + 1 : ℕ) : ℝ)` (28) | 75 + 1 + 28 = 104 > 100 | ok |
| 364 | 58 | proof body follows | n/a | ok |

Initial signature is identical and has the same table. Inequality scan: one n/a row — zero ≥/> occurrences; no orientation rename needed. All local typed inequalities were also scanned.

## Generalisation 2.6a–e, including every binder

| Binder | Kind / actual role | Candidates and actual result |
|---|---|---|
| `{x : ℝ}` | Structure value: both real bases and floor input | Cannot drop a value occurring in the conclusion; removing its written annotation cannot remove its quantification. A general ordered field lacks this Real.rpow API; NNReal/positive subtype changes representation and adds caller coercions. Retain ℝ. |
| `{c : ℝ}` | Structure value: arbitrary real exponent | Conclusion depends on c. Natural exponents specialize rather than generalize; retain real c. No universe/typeclass/decidability weakening applies to these fixed scalar types. |
| `hx : 0 < x` | Proposition: positive power and strict square gap; floor nonnegativity | Drop / 0≤x / -1<x fail at x=0,c=1; x≠0 fails at x=-1,c=1. Closed actual countercertificates checked. Mechanical substitutions in guarded autoImplicit-false negative harness rejected. |
| `hc : 1 ≤ c` | Proposition: real-power superadditivity | Drop/nonnegative fail at x=1,c=0; positive exponent alone fails at x=1,c=1/2. c=1 explicitly passes. Mechanical substitutions in guarded autoImplicit-false negative harness rejected. Retain this clean elementary API bound; **no claim that 1 is the globally optimal floor-sensitive real threshold**. |

Inner local facts: hu supplies both strict positivity and floor nonnegativity; weakening to nonnegativity loses the strict square gap. hsum only needs ≤ (strictness would unnecessarily exclude c=1). The former hfloor/hsq/hstrict/hrpow were derived local scalar facts, not extra ambient assumptions, and are eliminated. No hidden universe, decidability, function-global, bundled, or typeclass hypotheses exist. All inner TYPE binders are scanned recursively by the exact-contract harness. Inversion check n/a: no concrete project object is unfolded; this is already scalar arithmetic.

2.6b: False mechanical substitutions are compiler-negative evidence, with open/admitted values rejected; independent closed countercertificates establish mathematical falsity rather than merely failure of the chosen proof. Selected file native diagnostics complete/clean of errors. 2.6c: no recommended big restatement. A floor-free stronger estimate or an abstract y≤x^c formulation moves the floor obligation to callers without improving this counting API; generic field/RCLike substitution is not a safe mechanical replacement. 2.6d: **n/a private declaration, literature search not required**. Optional ChatGPT math service unavailable. 2.6e: no new small-safe weakening; original real x/c, positive x and non-strict c≥1 preserved.

## Five actual search methods and step-back result

A Lean-Finder: exact floor/power/shifted-base estimate; related `mul_pow_le_nat_floor_pow`/Bernoulli-type results, no matching replacement. B Loogle: `Real.rpow, Nat.floor, _ < _`, no result. C LeanSearch: natural-language estimate; related floor/ceiling bounds, no direct theorem. D full untruncated rg of full helper name and floor/rpow/add_rpow/one_add/multiplication variants in actual pinned sources; relevant Real.add_rpow_le_rpow_add, rpow_mul_natCast, rpow_mul and rpow_two verified. E native name-pattern searches: floor_rpow, add_rpow_le_rpow_add, rpow_mul_natCast, pow_le_pow_left₀ and Real.rpow_two. Returned source hits are presence evidence; index warming/error was retained and never counted as absence. Remote indexes are search aids, not an assertion that they equal the pinned v4.34 source snapshot.

Auxiliary variants covered real/NNReal/ENNReal, one_add/add, floor/power, natural-cast multiplication and real-power-two forms. Common-equivalents table has no matching bucket. Concluded: **partial mathlib matches; keep the local substantive estimate and build directly on the existing superadditivity/floor/power API**. Guarded exact? found no close; apply? partial admission was rejected. Whole grind/simp/aesop/positivity/gcongr/linarith/nlinarith probes failed; even empty-goal grind-with-error was rejected.

New external identifier verification: Real.rpow_mul is already used in the file and source-verified; Real.rpow_two has an actual local-source hit and compiled #check. Both plus pow_le_pow_left₀/Nat.floor_le are checked in the final actual whole0 independent harness. No unchecked guessed identifier enters selected source.

The shorter strategy normalizes the target real exponent product into a square, bounds it by (x^c+1)^2, and combines the positive x^(2c) gap with floor≤x^c. Term mode would embed the simpa/arithmetic blocks and obscure those two facts. No missing wrapper/coercion API or further helper is recommended.

## Correctness, actual consumer inventory and eight boundaries

Fresh initial, full-candidate-v5 and final installed-module harnesses independently check exact FIRSTDRAFT/current/expected FULL TYPE AST, every written and inner binder name/order/BinderInfo, universe list, actual isDefEq, closed TYPE and actual opaque VALUE (`value! true`), inferred VALUE type, and only propext/Classical.choice/Quot.sound. Raw names/types/values are logged before only generated macroScopes are erased on both sides. No arity/name-map or proof-irrelevance DATA shortcut. The independently replayed immutable FIRSTDRAFT proof's complete transitive TYPE+actualVALUE closure contains 16965 constants and bans the current helper; no new production subhelper exists. The expected-contract theorem is an actual adapter through the current helper.

Actual before/final compiled inventory uses true private-name discovery and all project constant TYPE plus opaque VALUE usedConstants, not a guessed .0 constant or pre-entry module. It finds `_private.Roth.MainLemma.0.Roth.floor_rpow_count_lt_aux` and **0 direct project users** on each side. Therefore helper-only profiling scope is correct; source references were also inspected. No imported-constant universe was gratuitously scanned for consumers.

Eight final boundaries are whole0, closed TYPE+actual VALUE/inferred TYPE/std3: c=1, x=1, c=2, tiny positive x=1/100 (all require actual current helper constant); x=0,c=1, x=1,c=0, x=1,c=1/2 and x=-1,c=1 countercertificates. No partial PASS from a failing run is accepted.

## Matched scoped performance / buzz

Exact CLI on both sides: `/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.

| Scope | Before | After | Outcome |
|---|---:|---:|---|
| Private helper, no actual direct consumers | 213.894 ms | 145.625 ms | <1000 ms; both <750, no required repeat |

Frozen observed parent environment SHA `a155a1578e910881bc51d37ee227264abe75fc7340a035498cee070983347c56` is supplied identically by subprocess on both sides. Actual lake env before/after each run is byte-identical, and the paired raw hashes match. Complete actual private-lemma outer source command, exact-qualified proof async, compiler/kernel and lint roots count ONCE; one inclusive private-theorem macro-expansion root is excluded on each side. No Meta/nested/next-declaration/trailing-end root is added. `parseH5.py` delegates to immutable owner anchored_profile_span.py and verify_profile_roots_exact.py; source recovery/scaffold/input-after hashes bind the actual canonical bytes. Target under budget: FAST BOARD, no limit raise, no deferral. No heartbeat measurement/wrapper was used. Whole-file all-row GLOBAL profiling remains the owner's later gate; pre-existing public19/main/delta slow queues are not cleared by this helper result.

## Environment, artifact coverage and failures retained

Before-golf actual source/configuration pins, all 104 project companions AND copied bytes, full setup/options/name/isModule/plugins/dynlibs/importArts JSONs, raw env, actual --deps, dynamic setup/package availability union and installed pinned-toolchain compiled-artifact SUPERSET were captured. Initial pre-build cache observation is explicitly distinguished from ready current-helper cache observation. Ready package union: 12201 artifacts / 1803668888 bytes; initial pre-build package bytes were 1803613128. Core superset: 12592 / 2125623224. These are actual observed counts, not forced totals, not an exact loaded closure, and setup.importArts availability is not proof of actual import availability. Final/pre-postprofile package union: 12201 / 1803649672 bytes; the sole ready-to-final availability-union change is own MainLemma.olean. Final pre/postprofile package and core hashes are identical. The direct --deps raw bytes and fresh actual imported-input hashes match; final-pair-provenance.json records these comparisons. Actual Lake/Lean binaries and both Elan launcher paths are rehashed; the launchers are one physical shared proxy, not two distinct physical executables. Actual compiled deps are verified; project-own outputs may change, actual imported input bytes remain pinned.

The first historical valid 224.899ms scoped capture is retained separately. A ready/postprofile raw-env comparison differed ONLY in duplicated MANPATH manual directories; it was never relabeled byte-equal. The new explicit frozen-env pair brackets installation and repairs provenance, not a slow-sample cherry-pick. Prelaunch recovery invocation failed because argparse.REMAINDER consumed the option after its positional label; no compiler PID was created. The corrected runner asserts its arguments and records actual input-after/environment hashes.

The first mechanical-negative harness already reported missing hx/hc identifiers and weak-assumption errors, with all partial results rejected. As an additional safeguard v2 explicitly disables autoImplicit before all six mechanical variants and confirms the same missing/weak-assumption failures; its actual-value guard rejects incomplete constants. Independent closed countercertificates supply the semantic falsity checks.

Other rejected evidence retained: inventory-v1 inferred MessageData counter (fixed explicit Nat); properties-v1 negative-base norm_num residue plus admission guard (all partial PASS rejected, repaired positivity); exact? no close; apply? partial sorry admission; candidate-v3/v4 natural-cast rewrite inference/matching failures (no partial proof credit). Candidate-v1/v2/v3-independent preliminary variants were archived but not compiled/selected. Candidate-v5 real rpow_mul+rpow_two full guarded context passed before installation. The transient native tool TypeError occurred before a request launched; a later fresh direct callable worked. Reconstructed stdio fallback source was never executed or counted as evidence. All raw logs/source variants/reversible diffs remain in this evidence root.

## Final gates and phase checklist

| Required check | Result |
|---|---|
| 1 Reference/workflow read | Full installed Lean/mathlib-quality skills, cleanup/cleanup-all/buzz, mandatory references, full 854-line worker prompt and 112-line profiler supplement read; copies/hashes in read-inputs.json. |
| 2 Full24 audit / packing / inequality | pass, above; complete measured tables and no orientation defect. |
| 3 Five-method search / 2.6a–e / all42 golf | pass, actual results above and every rule below; private literature n/a explicitly. |
| 4 Proof and structure | pass, six proof lines/no branch; no conjunction, no new helper. |
| 5 Exact contract and actual proof semantics | pass, independent FIRSTDRAFT/current/expected TYPE+VALUE/inferredtype/std3/nonself closure; all outer/inner TYPE binders. |
| 6 Properties / meaningful boundaries | pass, eight final closed certificates; mechanical negative candidates rejected. |
| 7 Affected/full/separate Eval builds | pass, actual session commands/whole exits above. |
| 8 Full unfiltered native | pass, all three final responses complete/nonpartial/nontimeout/zero errors/no failed dependencies; warnings honestly retained. |
| 9 Diff protection / metadata | pass, only target proof changed; Main/other16 pins and rename queue exact, no def/abbrev/API/doc/import/order change, no limit raise or profiling scaffold in production. |
| 10 Matched scoped performance and provenance | pass, actual complete root accounting, frozen identical environment/CLI, actual artifact/binary hashes and input/source immutability. No >=750 repeat triggered. |
| 11 Final freeze / drain / report | final-drain.json and artifact-manifest.json bind all actual artifacts, strict UTF8 or explicit binary exceptions, exact source/report hashes and all owned groups absent; no pending requests at END. |

Mode A single declaration: file-wide phases 1–3/5b/cumulative ALL declarations and final GLOBAL/simplify/publication are the owner's later file workflow, not falsely marked complete here. Scoped step-back/holistic review found no further recommended helper change. Built-in /simplify is not installed as a callable skill here; full file-wide simplify remains pending with owner. Renames none; no queue mutation. Refactoring needed for this helper: none. All private helper requirements complete, subject to owner's independent evidence review. No original264 count increment or file-complete claim.

## All 42 golfing rules and scoped holistic review

# Every golfing rule, helper5

Final selected-proof statuses. All acceptance gates are complete above.

1.1 Remove by-exact: selected proof removes hsq's trivial by/exact wrapper entirely.
1.2 by-rfl: n/a no such wrapper.
1.3 rw+exact→rwa: n/a final trans_eq eliminated by normalizing goal first; no rw+exact pair remains.
1.4 simp+exact→simpa: n/a hsum already terminal simpa.
1.5 trailing rfl: n/a absent.
1.6 constructor→tuple: n/a no conjunction/construction.
1.7 apply+exact: n/a no such pair.
1.8 by_contra!: n/a no contradiction proof.
1.9 eta reduction: n/a no lambda.
1.10 single-use have: selected proof eliminates hfloor/hsq/hstrict/hrpow; hu retained multiple uses, hsum retained because its terminal simplification is proof content.
1.11 refine+fun: n/a no apply/intro.
1.12 redundant show: n/a no show.
1.13 obtain: n/a no product projections.
1.14 merge rw: n/a no consecutive rw remain.
1.15 unsqueeze terminal simp only: n/a no simp only.
1.16 squeeze nonterminal simp: n/a no nonterminal bare simp.
1.17 dot notation: hx.le, hu.le retained; no useful namespace conversion remains.
1.18 <| for trailing parentheses: inspected all calls. Remaining parentheses are arguments followed by more arguments, type ascriptions, or syntax required by rw/nlinarith list. None is a trailing functional argument replaceable by <|. This rule is NOT cast-ascription removal.
1.19 push Not: n/a no push_neg.
1.20 inline existential helper: n/a no existential.

2.1 Whole grind: actual native probe failed with explicit error despite empty goals; REJECTED.
2.2 delete before grind: n/a no selected grind.
2.3 simpa consolidation: hsum already terminal simpa; selected proof drops redundant Real.one_rpow since terminal simp already knows it, verified by whole0 independent and build gates.
2.4 fun_prop: n/a no continuity/differentiability/measurability goal.
2.5 positivity: whole inequality is not a positivity goal (actual native rejection). Selected proof uses positivity only for nonnegativity prerequisites; old hrpow positivity arithmetic replaced. Negative-base scratch counterexample repair uses positivity.
2.6 gcongr: actual native whole attempt did not progress. Selected proof uses exact standard pow monotonicity as a nlinarith input; no manual monotonicity chain remains to shorten.
2.7 lia/omega: n/a selected arithmetic is nonlinear real arithmetic, not Nat/Int linear arithmetic. Natural arithmetic crosses its cast once.
2.8 aesop: actual native exhaustive search failed; REJECTED.
2.9 norm_num/norm_cast: concrete boundary certificates use norm_num; no concrete numeric or cast-only goal replaces the entire variable real-power estimate. push_cast is necessary once to normalize the natural-count cast.
2.10 decide/+kernel: n/a not a finite computational proposition; arbitrary real bases/exponents with hypotheses.
2.11 field_simp/ring: n/a no denominators; original final ring identity eliminated by mul_comm, Real.rpow_mul and Real.rpow_two.
2.12 linear_combination: original last ring goal can be closed by ring; selected proof removes that whole exponent identity. Actual final alternatives probe verifies linear_combination on that former identity; no ring/ring_nf remains in selected proof.
2.13 wlog: n/a no symmetric cases/branches.
2.14 two-step calc→term: n/a no calc. The original final hstrict.trans_eq step disappears after upfront rewrite.
2.15 <;>: n/a selected proof does not create parallel similar subgoals.

3.1 erw→rw: n/a no erw.
3.2 fun_prop: n/a no legacy continuity/measurability.
3.3 omega→lia: n/a no omega; real nonlinear arithmetic only.
3.4 rcases rfl: n/a no destructuring.
3.5 automation attribute: n/a private scalar estimate intended for one downstream proof; no stable global simplification/rewrite normal form or recurring automation hook warrants an attribute.
3.6 simp_all: native whole simp/aesop fail; no selected simp_all only to unsqueeze. Selected proof is direct API plus arithmetic.
3.7 limit raise: no maxHeartbeats/maxRecDepth/synthInstance raise exists or is added; all guarded compiler runs retain 200000/20000/512.

# Step back

Whole generic tactics fail because the conclusion requires nontrivial real-power superadditivity. Five-method search found foundational partial matches, not a direct replacement. The shorter strategy normalizes (x+1)^(2*c) into a square once, applies superadditivity once and uses the positive square gap together with the natural-floor bound. A single giant term would embed simpa and arithmetic proof blocks and obscure this structure; two local facts express the mathematical content. No additional helper or public API is recommended. All final gates passed as recorded above.

## Evidence index

Full byte/SHA256/strict-UTF8 manifest: `/private/tmp/roth-mainlemma-floor-rpow-count-helper/artifact-manifest.json`. Binary cache artifacts/executables have explicit binary exceptions. External original first-draft and immutable owner-parser references are separately freshly hashed. All phase source copies, complete raw streams, package/core catalogues and actual setup JSON copies are retained; no lost hash-only candidate. Report is helper-only; owner resumes the same original19 after review and explicit END.
