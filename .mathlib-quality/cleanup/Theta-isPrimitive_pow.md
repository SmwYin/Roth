# ORIGINAL17 — `isPrimitive_pow`

## Scope, baseline, result

Dedicated fresh audit of the private helper at current `Roth/Theta.lean:170`. Immutable original:
`2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`, original lines 176–180. Initial current source
SHA256 `8527a06d9d0b2b9626ca96d23f57bceefbac4c47b96ecfe80551a3be8a1d6aa8`.
Prepared read-only, with no compiler/LSP/search/write requests before explicit RELEASE.
Parent published checkpoint `7c5bc39f4a2542eb7283c84f8b2387117d682640` and reported full build
62.585s then separate LeanEval 23.065s, both exit 0 with all 17 hashes unchanged.
Baseline complete unfiltered LSP reused by exact source hash from
`/private/tmp/roth-primitive-linear/final-lsp.json`: success, partial=false, timed_out=false,
failed_dependencies=[], zero errors, 19 warnings. No warning belongs to this private helper.
Cache fetch and extra baseline build were unnecessary; the owner supplied the frozen green baseline.

The existing induction becomes a direct `Nat.rec` term: the base is the existing primitive-one
lemma and the successor uses the existing primitive-product lemma. Declaration: 5 → 3 lines;
proof body: 3 → 1 line; total source delta −2. No helper, caller, public type, attribute,
visibility, documentation, import, definition, namespace, or section changes. No Git mutations.
All evidence files below are under `/private/tmp/roth-primitive-pow/` unless specified otherwise.

## References and mathematics

Read both Lean/mathlib-quality skills, the full cleanup worker workflow, full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, relevant style sections,
full naming-conventions and profiling references. The dispatch's Lean 4.34 profiling command
supersedes the stale `-Dprofiler=true` example in the profiling reference.

A primitive integer polynomial has only unit constant divisors. One is primitive; Gauss's
lemma gives closure under multiplication, hence induction gives closure under natural powers.
The sole caller `exists_eq_pow_mul_of_rootMultiplicity` uses this to descend divisibility from
the rationals. Its approved-unused `hR` removal awaits the caller’s own dedicated audit.

## Full 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | Zero target warnings; all 19 unrelated baseline warnings retained in complete final diagnostics. |
| 2 | HAVE SCAN | No `have` in the target, before or after. |
| 3 | SET_OPTION | No target options; no limits raised or suppressions added. |
| 4 | SIMP SQUEEZE | Old terminal `simp [isPrimitive_one]`; new terminal `simpa [pow_succ] using ih.mul hp`, appropriately unsqueezed. |
| 5 | NAMING | Describes standard IsPrimitive closure under pow, follows predicate-name casing; no forbidden abbreviation/number scheme. No needless private API rename. |
| 6 | LINE PACKING | Measured full signature table below; all breaks justified. Body line is 87 codepoints. |
| 7 | BY PLACEMENT | Term proof, inner `by simpa` inline. |
| 8 | FORMAT | 2-space body indent; no blank lines, semicolon chains, haveI/letI or trailing whitespace. Old successor semicolon removed. |
| 9 | COMMENTS | No target proof comments; surrounding caller narrative preserved byte-for-byte. |
| 10 | DOCSTRING | Private helper has none; no documentation added/removed. |
| 11 | VISIBILITY | Correctly private; one actual caller in same file; classic dialect. |
| 12 | STRUCTURE | One-line body, no conjunction or >10-line branch; no extraction needed. |
| 13 | MATHLIB | Five actual searches plus clean compiled generic-route probes below; multiplication is partial match. |
| 14 | JUNK DEF | n/a: theorem, no definition. |
| 15 | EXISTS LEMMA | n/a: target is not existential. |
| 16 | SHOW/CHANGE | None. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every effective binder probed below; viable coefficient abstraction compiled but unnecessary for sole integer caller. |
| 19 | INEQUALITY | No inequality occurrences; table below. |
| 20 | NORMAL-FORM | Standard `Polynomial.IsPrimitive` predicate on `p ^ t`; no competing custom predicate. |
| 21 | SYNTAX-GEN | Existing implicit p, explicit hp/t remain convenient for caller; no applied benefit from changing them. |
| 22 | IMPORT-FANOUT | n/a: no new import. |
| 23 | CASTS | No explicit casts/ascriptions introduced. |
| 24 | INSTANCE-NAME | n/a: no instance declarations/binders in effective type. |

## Five actual Mathlib search methods

Raw native results: `searches.json`. Every request completed; no requests abandoned.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `A power of a primitive polynomial is primitive` | `Polynomial.IsPrimitive.mul` partial match; Monic.pow/Separable results irrelevant. |
| B Loogle | `Polynomial.IsPrimitive (_ ^ _)` | Empty result, not an absence proof. |
| C LeanSearch | `A power of a primitive polynomial is primitive` | IsPrimitive.mul, isPrimitive_of_dvd, Monic.isPrimitive and content-ideal equivalence; no direct power result. |
| D source rg | `IsPrimitive.*pow`, `isPrimitive.*pow`, `pow.*[Ii]sPrimitive`, `isPrimitive_submonoid`; inspected Content.lean and targeted full-name variants | No primitive polynomial power result; root-of-unity matches are unrelated. Content.lean supplies primitive one and mul. |
| E native local-name | `IsPrimitive` (limit 100) | Returns Polynomial.IsPrimitive.mul and associated APIs; index unavailable, so no indexed absence claim. |

Auxiliary variants: `Polynomial.IsPrimitive.pow`, `Polynomial.isPrimitive_pow`,
`isPrimitive_pow`, primitive/submonoid, primitive/product, content, Monic.pow, isPrimitive_of_dvd.
Untruncated full-name/source searches returned no power match. Common-equivalents table:
no applicable bucket (this already uses Mathlib's canonical predicate).

`trials.lean` ends the exact source prefix BEFORE the audited target and uses anonymous examples,
so searches cannot cite this target or earlier named failed trials. Actual compiler trials:
`simp [hp]` no progress; `grind` fails (unexpected polynomial ring instance); `aesop` no progress;
`exact?` cannot close; `apply?` offers only unfinished Monic/Irreducible/content/divisor routes;
`hp.pow t` is invalid (no Function.pow field on the unfolded predicate). `apply?` generates a
scratch sorry for its unfinished suggestion; this expected-failure file is never axiom evidence.
`trials.log` exit 1 records all failures and suggestions. Native multi_attempt was not repeated
because the standing workflow records its repeated full-Theta stalls; ordinary isolated
compiler exploration is the instructed bounded fallback.

Conclusion: no complete replacement found in available searches and compiled routes.
Retain the small inductive closure helper using existing primitive-one/mul API. This is not
a wrapper around an existing equivalent theorem. No absolute absence claim about newer indexes.

## Generalisation, all effective binders, literature and inversion

Compiled positive file `positive.lean` (exit 0, `positive.log`) independently proves original
and selected candidate, checks their equality by proof irrelevance at the same type, and also
compiles the coefficient abstraction `[CommRing R] [NormalizedGCDMonoid R]`.
Negative batch `negative.lean`/`negative.log` exits 1 as expected; it is not soundness evidence.

| Binder | Class/use | Compiled drop/weakening probe | Result/action |
|---|---|---|---|
| `{p : Polynomial ℤ}` | Structure value in hp, base and conclusion | Remove binder with autoImplicit=false | Unknown p/p.IsPrimitive; binder is necessary to state result. Keep exact type/BinderInfo. |
| `hp : p.IsPrimitive` | Proposition used in successor `ih.mul hp` | Drop hp; additionally replace with `p ≠ 0` | Drop fails to supply p.IsPrimitive; nonzero weakening is type-incompatible at mul. Keep. The zero/t=1 obstruction was also explored in the negative batch and is not used as successful verification evidence. |
| `t : ℕ` | Structure value indexing recursion and conclusion | Remove binder with autoImplicit=false | Unknown t; necessary to state result. Natural iteration is the mathematical operation; keep explicit argument. |

Effective type recovery confirms no inherited σ/Fintype/DecidableEq binders. There are no
effective universe/typeclass/decidability binders to drop. No strict inequality or global
pointwise hypothesis exists to weaken/localise. `p.content = 1` is an equivalent predicate,
not a weaker mathematical hypothesis, and would make the sole caller less direct.

Inversion check: the coefficient ring ℤ is concrete but never used specifically by the
induction. The generic ring/GCD version compiles in positive.lean. It adds three private
binders without helping the sole integer caller, so preserve this focused helper rather than
churn the private API; parent agreed this choice. No new general helper is introduced.
Literature status: n/a — private declaration, public literature search exemption applies.
No public abstraction or changed public contract is proposed. No unresolved choice remains.

## Measured signature packing and inequality table

Compiled width-100 reference: `@candidate : ∀ {p : Polynomial ℤ}, p.IsPrimitive → ∀ (t : ℕ),
(p ^ t).IsPrimitive` (`positive.log`). Codepoint measurements, not UTF-8 bytes:

| Signature line | Chars | Next signature token | Arithmetic/action |
|---|---:|---|---|
| 170 | 79 | `(p ^ t).IsPrimitive :=` (22) | 79 + 1 + 22 = 102 > 100; ok |
| 171 | 26 | none; proof body next | n/a; ok |

The old second signature line was 29 chars with `by`; its conclusion also did not fit on
the first line. The final body is 87 chars. No signature underpacking remains.

| # | Location | Original inequality | Rewrite | Rename |
|---|---|---|---|---|
| — | Entire signature/hypotheses | n/a: no ≥/> or any inequality | none | none |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw/exact→rwa | Replaced whole inductive syntax with Nat.rec; successor uses terminal simpa. |
| 1.4 simp/exact→simpa | Applied successor `simpa [pow_succ] using ih.mul hp`. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor tuple | n/a: no product goal. |
| 1.7 apply/exact | n/a: none. |
| 1.8 by_contra! | n/a: no contradiction. |
| 1.9 eta lambdas | Successor lambda uses both t and ih; cannot eta reduce. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply/intro | n/a: none. |
| 1.12 redundant show | n/a: none. |
| 1.13 obtain | n/a: no projections. |
| 1.14 merge rw | n/a: no consecutive rewrites. |
| 1.15 terminal simp only | n/a: unsqueezed terminal simplification. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | `ih.mul hp` retained. |
| 1.18 <\| | n/a: no removable trailing application parentheses. |
| 1.19 push Not | n/a: none. |
| 1.20 existential inline | n/a: not existential. |
| 2.1 grind | Actual clean whole-goal trial fails; trials.log. |
| 2.2 delete before grind | n/a: no successful grind. |
| 2.3 simpa consolidation | Applied to successor. Whole `simp [hp]` fails. |
| 2.4 fun_prop | n/a: no analytical property. |
| 2.5 positivity | n/a: no positive/nonnegative/nonzero goal. |
| 2.6 gcongr | n/a: no ordered comparison. |
| 2.7 lia/omega | n/a: no linear arithmetic goal. |
| 2.8 aesop | Actual clean whole-goal trial fails. |
| 2.9 norm_num/cast | n/a: symbolic primitive-polynomial property. |
| 2.10 decide | n/a: arbitrary polynomial primitivity is not finite computation. |
| 2.11 field_simp/ring | n/a: no denominators/equality. |
| 2.12 linear_combination | n/a: no ring-ending identity. |
| 2.13 wlog | n/a: zero/successor are not symmetric branches. |
| 2.14 calc composition | n/a: no calc. |
| 2.15 <;> | n/a: dependent base/successor proofs are distinct. |
| 3.1 erw | n/a: none. |
| 3.2 continuity | n/a: none. |
| 3.3 omega→lia | n/a: none. |
| 3.4 rcases rfl | n/a: none. |
| 3.5 attributes | No new automation attribute for a private single-caller helper. |
| 3.6 simp_all | n/a: no simp_all only; hp gives no whole-goal simplification. |
| 3.7 options | No limits/options to remove. |

Step back: exact?/apply? do not provide a complete existing theorem. Direct recursion expresses
the same induction without a semicolon or extra proof block; the 87-character successor term
remains readable. No alternative strategy reduces the mathematical argument. Generic private
API expansion gives no caller benefit. No independent branch merits extraction.

## Soundness, actual constants, public compatibility and gates

`lake build Roth.Theta` executed after the edit, exit 0: `module.log` ends
`Build completed successfully (2423 jobs).` Final native COMPLETE unfiltered diagnostics saved
in `final-lsp.json`: success=true, partial=false, timed_out=false, failed_dependencies=[],
zero errors, 19 warnings. No diagnostic range/severity filter was used.

`actual.lean` imports the actual built module and reproduces the immutable original linear,
primitive-power and caller proofs in namespace Original17, independently of the current helper.
It locates exactly one private built constant programmatically:
`_private.Roth.Theta.0.Roth.isPrimitive_pow`. It compares the full old/actual type by defeq
and checks every binder name and BinderInfo. It does the same full type/binder check for
`Roth.exists_eq_pow_mul_of_rootMultiplicity`, including hR. `actual.log` exit 0 certifies this
and rejects any nonstandard axiom for all four old/actual helper/caller constants. All use only
`propext`, `Classical.choice`, `Quot.sound`. Independent old proofs do not invoke current
versions of themselves. `positive.log` is separately successful selected-proof evidence.

| Gate | Result/evidence |
|---|---|
| lake_build_file | pass — actual `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit 0. |
| final complete LSP | pass — final-lsp.json, zero errors, complete 19-warning baseline. |
| definition_protected | pass — worker.diff contains no def/abbrev edits. |
| theorem_statement_protected | pass — same exact private type/binders and byte-identical caller; actual.log. |
| structure_gate | pass — one-line body, no conjunction/long branch. |
| naming_gate | pass — descriptive standard property; no forbidden patterns/abbreviations. |
| line_packing_gate | pass — both signature lines measured above. |
| inequality_orientation_gate | pass — explicit zero-occurrence table above. |
| cumulative caller compatibility | pass — independent old caller full type/binders and standard axioms verified. |
| no sorry/new axioms | pass — actual built constants checked; expected-failure scratch suggestions excluded. |
| full project + separate LeanEval | Pending owner after freeze; not claimed as worker gates. |

New identifier `Nat.rec` is Lean's inductive eliminator; its use is compiler-verified in
positive.lean and the actual module. Existing Polynomial.isPrimitive_one, pow_succ, and
Polynomial.IsPrimitive.mul already occurred in the original proof and are compiler-verified.

## Simplify and buzz

Simplify outcome: PASS-THROUGH after direct in-thread holistic review; no separate simplify
tool/skill is available. No duplicated skeleton, unnecessary local fact, or useful extraction
remains. No production changes followed this review.

Buzz outcome: FAST-BOARD. Exact uncontended prefix timing (seconds converted to milliseconds):

| Target | Outer lemma command | Async proof | Async kernel/addDecl | Total excluding linters |
|---|---:|---:|---:|---:|
| Before | 5.928 ms | 25.255 ms | 0.131 + 0.925 ms | 32.239 ms |
| Final | 3.950 ms | 41.740 ms | 1.152 ms | 46.842 ms |

The underlying `private theorem` command is nested inside the outer `private lemma` macro and
is not counted twice. Associated nested Kernel nodes are covered by their async addDecl totals.
Linter async totals are 4.058 ms before and 2.854 ms final (including them: 36.297/49.696 ms).
No separate target compiler node. Both target totals are far below 750/1000 ms; no borderline
repeat or performance repair is needed. The 14.603 ms measured increase buys a direct shorter
term and has no material budget impact; no speedup is claimed. Anchors are the actual
`private lemma isPrimitive_pow` command and `_private._stdin.0.Roth.isPrimitive_pow` proof.
The first before-profile.log was discarded as timing evidence because a later isolated ordinary
probe briefly overlapped it. Only before-profile-uncontended.log and after-profile.log certify
the comparison. Both use exact source prefixes through the target with all preceding context,
and `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 FILE`. No raised limits. This is prefix-only evidence, not a
whole-module profile; owner retains the actual final whole-module sweep obligation.

## Eleven-step completion checklist

- [x] Step 1: reference docs read.
- [x] Step 2: full 24-item audit recorded.
- [x] Step 2.5: five actual searches plus clean compiled generic routes recorded.
- [x] Step 2.6: all effective binders, generality, private literature exemption/inversion recorded.
- [x] Step 2.7: every signature line measured in codepoints.
- [x] Step 2.8: inequality occurrence table recorded.
- [x] Step 3: all 42 golfing rules individually resolved.
- [x] Step 4: step-back reflection and direct recursion evaluated.
- [x] Step 5a: final complete unfiltered LSP successful.
- [x] Step 5b: module, exact type/binders, old independent proof, actual axioms and diff gates pass.
- [x] Step 6a: no rename required; no queue/shared-log/Git writes.

Refactoring needed: none. Comments-preserved: none present in target; surrounding narratives
untouched. New helpers: none. Full owner builds and publishing follow this worker's freeze.

Final source SHA256: `4365647e579ced2904bca87d28d47cff60cb3bd3e5052b17032133a829605c08`.
Source edits frozen/revoked at handoff. All terminal/compiler/native requests completed; no
orphan requests remain. Only the assigned source proof and this report were modified in the
repository. The module and soundness gates preceded the final uncontended profile; no source
edit followed those gates.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (64.388 s),
then separate `lake build Roth.LeanEval` (24.164 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `4365647e579ced2904bca87d28d47cff60cb3bd3e5052b17032133a829605c08`.
Raw logs: `/private/tmp/roth-theta-d17-full.log`, `/private/tmp/roth-theta-d17-leaneval.log`; machine record
`/private/tmp/roth-theta-d17-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 17/35, overall 198/264 original
declarations, 9/14 completed files. No new production helper.
