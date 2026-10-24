# `exists_roth_approximants_aux` — necessary-helper audit

Local helper audit complete; publication remains joint with original declaration 15,
`roth_of_isIntegral`. No original-declaration completion credit or parent audit is claimed.
Scope: only the private helper declaration in `Roth/Main.lean`; both adjacent comments
are preserved. No caller, accepted helper, import, Git, or shared-progress changes.

## Genuine first draft and result

The immutable first ungolfed helper was saved before any helper Lean/golf launch:
`/private/tmp/roth-main-integral-roth/helper-approximants-FIRSTUNGOLFED.lean`, SHA256
`cc4c212cf156cb4e0950cee08bded3134fbe88eff9fdfb110fde8e81dffbf62d`.
Worker verified byte equality and saved its own copy before its first Lean invocation.
Parent `PARTIAL_END_2.json` records zero helper Lean/golf runs and released leases.

| Measure | Genuine first draft | Final |
|---|---:|---:|
| Declaration lines | 32 | 22 |
| Body lines, including signpost | 23 | 14 |
| Disjoint profile roots | 429.239 ms | 357.892 ms |
| Generated theorem family | root + induction `_proof_1_1` | root only |

Both measurements are exact source prefixes with unchanged imports and preceding commands,
namespace close and TYPE/VALUE/default observations. Both are below 750 ms; no repeat required.
They are helper measurements, not historical timing of the parent declaration.

Final `Main.lean` SHA256:
`4b2c8aba1adcdb8d3065399c202725efef9bb59222119894866b6704e246beb1`.
Final helper SHA256:
`66e532fadae8677d10eaea4b10d7fb5942e42aac7e488d353280f89354a70d2b`.
The complete signature token stream equals the genuine draft. Outside this helper the file
is byte-identical to entry `2b0e32131b9160acbd7e996a1eb561cf06dab472063b5b6c277d9b65e022c2c5`.
The frozen parameter helper still hashes to
`aee451eda7d7f95ec7b2b63684c38f0fb7221f5710bb29ff2837d430b2184120`.

## Mathematical necessity and changes

This stage chooses shared reduced approximants `h/q` and balanced positive degrees `r`.
The conclusion retains approximation, coprimality, denominator positivity, degree separation,
maximum-first-degree, and all quantitative logarithmic bounds on the same witnesses.
It is a correlated existential construction, not a trivial witness/rfl or fact-tuple wrapper.
The first draft was already under the ordinary 30-line extraction threshold; no forced
extraction is appropriate. Splitting its conjunction would duplicate witness choices.

The final proof uses `Fin.antitone_iff_succ_le` in place of manual natural-number degree
induction, applies `div_lt_iff₀'` directly to the threshold bound, and inlines the single-use
lower-degree comparison. No mathematical hypothesis or conclusion changed.

## Complete 24-item audit

| Item | Finding/action |
|---|---|
| 1 LINT | Complete initial/final LSP: no helper warnings/errors. Existing Main line-1 header warning remains outside scope. |
| 2 HAVE | Old h32: proof content replaced by direct ordered-division API; hj: one use, inlined; hstep/hr0max/key: replaced by finite antitone API. Final only hranti has genuine proof content. |
| 3 SET_OPTION | None; no limits raised. |
| 4 SIMP | Only old terminal induction-base simp; removed with induction. No nonterminal bare simp. |
| 5 NAMING | Descriptive snake_case, private, unnumbered `_aux`; no forbidden abbreviation or pattern, no rename. |
| 6 PACKING | Every signature line measured below; all natural syntactic units fit maximally within 100 codepoints. |
| 7 BY | Every by remains at preceding-line end. |
| 8 FORMAT | Two-space tactics, no blank proof lines; old semicolon case chains and lambda => disappear. |
| 9 COMMENTS | Ordinary pre-helper comment and approximants/degrees signpost both preserved, 2/2. |
| 10 DOCSTRING | Correctly no docstring on private helper; ordinary comment retained. |
| 11 VISIBILITY | Private file-local helper, no public API added. |
| 12 STRUCTURE | Body 23→14; no branch over ten lines. Shared existential conjunction is essential; no artificial extraction. |
| 13 MATHLIB | Five methods below establish the finite-order partial match; use existing approximation/degree APIs directly. |
| 14 JUNK DEF | N/a: lemma, no definition. |
| 15 EXISTS | Nontrivial shared-witness construction; not a witness/rfl wrapper. |
| 16 SHOW | None. |
| 17 PUSH_NEG | None. |
| 18 GENERALISE | Every binder examined below; no supported weakening. |
| 19 INEQUALITY | No ≥ or > tokens in signature/hypotheses; all inequalities use ≤/<. |
| 20 NORMAL FORM | Existing approxSet, IsCoprime, Fin and Real.log forms retained. |
| 21 SYNTAX GENERALITY | Shared witnesses are the form needed by the parent; no alternate restatement warranted. |
| 22 IMPORT FANOUT | N/a: no new imports. |
| 23 CASTS | No redundant same-type casts introduced; four genuine Nat/Int cross-type signature casts and one load-bearing Real numeral ascription retained. Old local hj annotation disappears with that alias. |
| 24 INSTANCE NAME | N/a: no instance declaration; NeZero binder stays anonymous. |

## Five-method search

| Method | Actual search/result |
|---|---|
| A Lean-Finder | “A function on Fin n is antitone if it decreases at each successor”: Fin.antitone_iff_succ_le, strictAnti variant, list sorted alternative. |
| B Loogle | `Fin, Antitone`: Fin.antitone_iff_succ_le and Fin.rev_anti. |
| C LeanSearch | Successor-decreasing finite map: same lemma plus antitone_nat_of_succ_le/int variants. |
| D Source search | Order/Fin/Basic.lean:163 confirms the characterization; ordered GroupWithZero Basic:1465 supplies div_lt_iff₀'; field Basic:38 supplies le_div_self. |
| E Name pattern | Local Fin.antitone_iff_succ_le lookup found source declaration; symbol index reported unavailable, so no absence claim from that index. |

Auxiliary variants considered: successor characterization, strictAnti, sorted-list,
natural-number antitone API, primed/unprimed positive division API. Common-equivalents table
has no specialized logarithmic approximation construction. Conclusion: partial API found
and used. No claim that an exhaustive compiled absence certificate was established.
New names are confirmed by source and actual final project/native compilations.

## Per-binder mechanical generalisation

| Binder | Class/use | Candidate disposition |
|---|---|---|
| α : Real | Structure value, irrationality/approxSet/logarithmic constants | Cannot drop dependent value; changing field restates specialized upstream APIs. |
| κ : Real | Structure value in approxSet and positivity | Cannot drop dependent value; already arbitrary Real. |
| hα | Proposition, passed to exists_approximants | Dropping leaves that API obligation unmet; no weaker API found. |
| hκ : 0 < κ | Proposition, strict upstream obligation | 0≤κ does not supply exists_approximants' strict hypothesis; no supported weakening. |
| hinf | Proposition, source of approximants | Dropping removes the existence input. |
| m : Nat | Structure value, dimension and quantitative conclusion | Dependent Fin signature cannot omit it. |
| NeZero m | Typeclass, Fin zero/reversal/nonempty dimension | Dropping makes the signature ill-typed. No weaker parent class. |
| δ : Real | Structure value in division and growth constraints | Dependent conclusion requires it. |
| hδ0 : 0 < δ | Proposition, positive division and le_div_self | Nonnegativity cannot supply strict denominator positivity. |
| hδ1 : δ ≤ 1 | Proposition, degree choice and le_div_self | Already weak, explicitly required by both APIs. |
| A : Real | Structure value, lower logarithmic threshold | Already arbitrary, appears in conclusion. |

No point-localisation/universe/typeclass-parent catalogue applies to these concrete APIs.
No speculative ambient generalisation or unsupported compile-success claim was made.
Inversion check: the specialized approximation choices and logarithms remain essential
throughout; no concrete-object-unfolding/abstract-proof pattern. Literature: n/a private helper.

## Line packing and inequalities

Widths are Unicode codepoints. Next units preserve complete binders/conjuncts and attach
the return-type colon to its final binder. The actual width-100 #check reference is captured
in both profile stdout files.

| Line | Width | Next unit width | Sum with space | Action |
|---|---:|---:|---:|---|
| 425 | 85 | 33 (hinf binder) | 119 | ok |
| 426 | 92 | 9 ((A : Real) :) | 102 | ok |
| 427 | 86 | 34 (coprimality conjunct) | 121 | ok |
| 428 | 94 | 58 (degree-step conjunct) | 153 | ok |
| 429 | 83 | 94 (growth comparison conjunct) | 178 | ok |
| 430 | 100 | 58 (lower logarithmic conjunct) | 159 | ok |
| 431 | 64 | 77 (final quantified comparison and := by) | 142 | ok |
| 432 | 84 | — | — | ok, final signature line |

| Inequality occurrence | Rewrite | Rename |
|---|---|---|
| N/a: zero ≥/> tokens in signature/hypotheses | None | None |

## All 42 golfing-rule slots

| Rule | Disposition |
|---|---|
| 1.1 | N/a: no by-exact wrapper. |
| 1.2 | N/a: no by-rfl wrapper. |
| 1.3 | Rewrite/closing chain replaced by direct division lemma. |
| 1.4 | N/a: no simp/exact chain. |
| 1.5 | N/a: no simp/rfl chain. |
| 1.6 | Existing anonymous existential/conjunction constructor retained. |
| 1.7 | N/a: no apply/exact chain. |
| 1.8 | N/a: no contradiction. |
| 1.9 | Nontrivial argument-using lambdas retained; old key lambda removed with induction. |
| 1.10 | Single-use hj inlined; h32 replaced directly. |
| 1.11 | Refine finite antitone characterization with function. |
| 1.12 | N/a: no show. |
| 1.13 | Existing obtain destructuring retained. |
| 1.14 | N/a: no consecutive rewrites remain. |
| 1.15 | Old terminal simp removed with induction; no terminal simp only remains. |
| 1.16 | N/a: no nonterminal bare simp. |
| 1.17 | Direct .trans/.le projections used. |
| 1.18 | N/a: necessary parenthesized trans operands, no trailing tactic-argument candidate. |
| 1.19 | N/a: no push_neg. |
| 1.20 | N/a: nontrivial correlated existential stage. |
| 2.1 | Old h32-line grind attempt failed; see probe qualification below. No retained grind. |
| 2.2 | N/a: no grind preceding tactics. |
| 2.3 | N/a: no simplification/closing sequence. |
| 2.4 | N/a: no regularity goal. |
| 2.5 | Positivity supplies square positivity in the direct division application. |
| 2.6 | N/a: direct le_div_self expresses required inequality, no monotonicity calc. |
| 2.7 | Old omega goals removed entirely by finite-order API. |
| 2.8 | Old h32-line aesop attempt failed; see qualification below. |
| 2.9 | norm_num proves concrete bounds; exact_mod_cast crosses Nat/Real. |
| 2.10 | N/a: existential logarithmic construction is not closed finite computation. |
| 2.11 | N/a: no rational identity goal. |
| 2.12 | N/a: no ring/ring_nf ending. |
| 2.13 | N/a: no symmetric branches. |
| 2.14 | N/a: no calc, existing trans composition is direct. |
| 2.15 | N/a: final refine leaves one cast goal. |
| 3.1 | N/a: no erw. |
| 3.2 | N/a: no legacy regularity tactic. |
| 3.3 | Omega removed with induction, no arithmetic automation needed. |
| 3.4 | Dimension obtain/rfl substitutes directly, no redundant substitution simp. |
| 3.5 | N/a: private existential stage should not be global automation rule. |
| 3.6 | N/a: no simp_all. |
| 3.7 | N/a: no raised options. |

Probe qualification: the initial multi-attempt at old h32 line 437 tested grind, aesop,
and exact?. Each failed and additionally had multiline suffix-parser errors. It did not
replace the whole proof and is not credited as a valid whole-proof or absence probe.
The bounded direct API replacement then passed complete diagnostics on its first proof edit.
Step-back review confirms explicit shared choices remain useful; no artificial wrapper,
further extraction, ambient generalisation or additional imports are warranted.

## Validation and semantic evidence

All compiler/native/LSP/semantic/profile work was serial; next work started only after
actual terminal completion. Source stayed frozen throughout final validation.

| Actual invocation | Result |
|---|---|
| `lake build` via run.py final-full-build | exit 0, 62.959 s |
| Separate `lake build Roth.LeanEval` | exit 0, 30.740 s |
| Fresh `lake env lean Roth/Main.lean` | exit 0, 29.298 s |
| Fresh `lake env lean Roth/LeanEval.lean` | exit 0, 33.583 s |
| Fresh `lake env lean Roth.lean` | exit 0, 30.391 s |
| Complete unfiltered Main/Eval/root LSP | terminal/full/nonpartial, 0 errors; Main header warning only |
| Independent manual-induction proof | exit 0, 39.357 s |
| Actual family enumeration before row guards | exit 0, 76.763 s |
| Semantic aggregate | exit 1 at final generated-TYPE guard only; required root TYPE and all three VALUE rows already valid |
| Only outstanding generated TYPE supplement | exit 0, 54.883 s; no VALUE reinference |

`actual-families-before-guards.json` records the actual complete production root and
independent root + `_proof_1_1` families. All their universe lists were observed as `[]`
before guards; none was assumed empty. All three actual opaque VALUEs were checked in
memory: closed, inferred against actual TYPE, no sorry, standard axioms only
(propext/Classical.choice/Quot.sound), defaults 200000/20000/512. VALUEs are hash/length
receipts, not full raw dumps or proof-identity claims. Local graph is acyclic; production
and independent families do not depend on each other. External origins are strictly
upstream; accepted preceding project APIs are reused without reproof.

Complete old/current/independent root TYPE comparison uses strict recursive Name, Level,
BinderInfo, metadata, literal and projection comparison, with no ExprBEq shortcut.
Actual raw TYPEs are unequal solely at the seventh anonymous NeZero binder (body^6):
old `_stdin/932137741/_hyg24`, current `Roth.Main/932137741/_hyg24`, independent
`IndependentApproximants/2067479520/_hyg24`. Two literal finite pairs alone are allowed;
both Names have macro scopes, equal erased Names, matching instImplicit at that exact path.
All remaining raw TYPE bytes and the complete strict Expr comparison match.

The extra generated old/independent TYPE guard initially failed solely at body^3's default
anonymous binder: `a._@._internal/0/_stdin/932137741/_hyg760` versus the actual independent
module `IndependentApproximants/2067479520/_hyg760`. The supplement checks that one concrete
pair, both macro-scoped/equal erased, exact BinderInfo/path, and all remaining complete raw
bytes and strict Expr equality. The prior run is not called a whole pass. Its three valid
rows were preserved; the exit-0 supplement closes the only outstanding comparison.
No API weakening occurred, so no caller recovery proof was needed. This full build validates
the current parent source but does not replace the parent's full declaration audit.

## Simplify and performance

Built-in /simplify is unavailable; no actual invocation is claimed. Manual substantive
review considered reuse, mathematical structure and efficiency and found no further issue.
A fresh whole-file reviewer remains part of the owner's later workflow.

Buzz outcome: FAST-BOARD, genuine 429.239 ms → final 357.892 ms; no limit raises,
no native_decide, no profiling scaffolding in production. Both exact-prefix captures followed
HOLD/ACK before preparation, actual raw-unparsed child/driver drain, and explicit owner
RELEASE before parsing. Defaults/environment/frozen inputs passed. Full environment bytes
were compared only in memory; persisted fields use the approved safe allowlist.

Actual outer command + asynchronous proof + kernel-parent + linter roots were counted
without nested double-counting. There were no compiler or lazy prior-DATA roots in this
helper's canonical root group. Actual generated families were observed in each capture.
The complete expanded `private theorem` payload matches the canonical lemma after expansion;
source-bound Mathlib expandLemma and Lean recursive command/trace-flush evidence establishes
nesting despite the inner command printing unindented before its outer command. Existing
accepted implementation-source hashes were checked exactly; no new capture/replay was used
for this binding.

## Gates and phase checklist

| Gate | Result |
|---|---|
| lake_build_file / lake_build | PASS, actual full and separate downstream builds above |
| definition_protected | PASS, no definitions touched |
| theorem_statement_protected | PASS, exact genuine signature tokens; strict TYPE comparison qualified above |
| structure | PASS, 14-line coherent shared-witness proof |
| naming | PASS, private descriptive snake_case `_aux` |
| packing | PASS, complete codepoint table, max 100 |
| inequality | PASS, zero reversed inequality tokens |
| no unintended breakage | PASS, full project, Eval, native three modules, complete diagnostics |
| no trust/resource/scaffolding regression | PASS, defaults and actual VALUE guards |

- [x] Full required skills/workflows/references read.
- [x] Full 24-item audit, HAVE scan, five-method search, per-binder review.
- [x] Complete signature packing and inequality tables.
- [x] All 42 golfing slots, bounded direct proof cleanup and step-back review.
- [x] Complete diagnostics and actual build/diff gates.
- [x] Non-rename/rename review: no further actions or queued renames.
- [x] Manual substantive simplify review, unavailable invocation truthfully qualified.
- [x] Exact genuine-first-draft and final buzz measurements, under budget.
- [x] Actual-family/default/strict TYPE/opaque VALUE/independence checks complete.
- [x] Report complete. No helper-only publication or parent-completion claim.

Evidence directory: `/private/tmp/roth-main-roth-approximants`.
`semantics-receipt.json` binds preserved rows and the successful supplement; each profile
has source bindings, actual drain/release receipts, complete canonical payload, roots and
expanded-command nesting evidence. FINAL/END receipts record actual final drain and released
leases. Owner must resume the same parent author after local acceptance; joint publication
waits for completion of the parent and all necessary helpers.
