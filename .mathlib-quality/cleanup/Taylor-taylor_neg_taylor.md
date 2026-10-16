# Audit: `MvPolynomial.taylor_neg_taylor`

Original assigned lines 195–197; current lines 177–179, three lines before and after.
Read the worker contract, both skills, golfing-rules.md, proof-patterns.md,
mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, style-rules.md,
and naming-conventions.md. No Git commands, shared-log edits, or public API deletion.

Mathematics: translating a polynomial by α and then −α gives the original polynomial.
Composition adds the translation vectors; coordinatewise additive cancellation gives zero,
and translation by zero is the identity. The existing one-tactic proof captures this.

## Full 24-item audit

1. LINT: no target diagnostics. Complete native LSP returned success=true, partial=false,
   timed_out=false, failed_dependencies=[]; only the existing line-1 copyright warning.
2. HAVE SCAN: none; no bindings to inline.
3. SET_OPTION: none in target; no limits or linter settings added.
4. SIMP SQUEEZE: the sole `simp [taylor_taylor]` is terminal; retain unsqueezed.
5. NAMING: `taylor_neg_taylor` describes the nested operations and their negated argument,
   is snake_case, and contains no forbidden abbreviations, numbered patterns, or inequality
   suffixes. Pass without a rename queue.
6. LINE PACKING: corrected the first line from 62 to 99 codepoints; table below.
7. BY PLACEMENT: `by` ends the second signature line.
8. FORMAT: normalize mathematical lambda `=>` to `↦`; two-space proof indentation,
   four-space signature continuation, no blank lines, no semicolons, no haveI/letI.
9. COMMENTS: no inline proof comments; existing docstring preserved byte-for-byte.
10. DOCSTRING: existing one-sentence inverse-translation description is accurate and kept.
11. VISIBILITY: public cancellation API retained as explicitly required; it is used by
    `taylor_injective` and the expansion proof in this file.
12. STRUCTURE: one tactic, no conjunction or branches; no decomposition needed.
13. MATHLIB: five methods below found univariate analogues and generic building blocks;
    no verified drop-in multivariate replacement. Preserve the existing public API.
14. JUNK DEF: n/a: theorem, not a definition.
15. EXISTS LEMMA: n/a: equality, not a private existential helper.
16. SHOW vs CHANGE: n/a: neither occurs.
17. PUSH_NEG: n/a: no negation-pushing tactic.
18. GENERALISE: parameter table and compiled weakening experiments below; none kept.
19. INEQUALITY: table below; no inequality occurrence or reversed inequality name.
20. NORMAL-FORM: already in cancellation normal form, nested translations equal the
    polynomial; no equivalence graph or new normal-form lemma introduced.
21. SYNTAX-GEN: OK; direct equality rewrites nested translation expressions at callers.
22. IMPORT-FANOUT: n/a: no imports changed.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing; no casts in the diff.
24. INSTANCE-NAME: n/a: theorem introduces no instances.

Issues fixed: lambda-arrow style; underpacked signature. No mathematical changes.
Refactoring needed: none. No rename queued.

## Line packing

Width-100 elaborator reference, from isolated prefix compilation:

```lean
@taylor_neg_taylor : ∀ {σ : Type u_3} {A : Type u_4} [inst : CommRing A] (α : σ → A) (P : MvPolynomial σ A),
  (taylor fun j => -α j) ((taylor α) P) = P
```

Original first line: 62; moving the whole original conclusion (45 nonindent characters) gives
62+1+45=108, but its initial expression can be moved, hence repacking was required.
The final split uses the equality as a natural operator break.

| Signature line | Codepoints | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 177 | 99 | `P` (1) | 99+1+1=101 >100 | ok |
| 178 | 11 | none; proof follows | n/a | ok |

The complete conclusion, including `:= by`, participates in packing. Proof line 179 is 22.

## Inequality scan

| Scope | Occurrences of `<`, `≤`, `>`, `≥` | Rewrite |
|---|---:|---|
| Signature, inherited hypotheses, proof | 0 | none |
| Declaration `_ge_` / `_gt_` names | 0 | none |

Function arrows and lambda arrows are not order relations.

## Mathlib search status

[A] Lean-Finder query: “multivariate polynomial translation by a then negative a equals
original polynomial”. Three hits: `Polynomial.taylorEquiv_symm`,
`Polynomial.taylorLinearEquiv_symm`, `Polynomial.taylor_apply`; all univariate analogues.
[B] Loogle type query: `Polynomial.taylor (-?r) (Polynomial.taylor ?r ?p) = ?p`:
empty items, isError=false.
[C] LeanSearch: “polynomial Taylor translation negative inverse”: hits
`Polynomial.taylorLinearEquiv_symm`, `Polynomial.taylorEquiv`,
`Polynomial.algEquivAevalNegX_symm_apply`.
[D] Source search: `taylor`/`taylor_neg`/`neg_taylor` in multivariate directories returned
no matching declarations. Untruncated full-tree `taylor_neg_taylor|neg_taylor|taylor_neg`
returned no hits. Read univariate Taylor source: `Polynomial.taylor_taylor` at line 157
and `taylor_zero` at line 55 supply the analogous argument.
[E] `lean_local_search("taylor")` found this project's multivariate declarations and
univariate mathlib declarations. Index=unavailable, so empty/index results cannot certify
absence; source and compiled checks provide the local evidence instead.

Auxiliary variants examined: `taylor_taylor`, `taylor_zero`, `taylorEquiv_symm`,
`taylorLinearEquiv_symm`, `algEquivAevalNegX_symm_apply`. Common-equivalents lookup:
no discrete, finiteness, boundedness, or topology bucket applies.

Concluded: partial match in the univariate API; retain the public multivariate result and
its existing composition/cancellation proof. No claim of exhaustive absence is made:
`exact?` and `apply?` both hit the default 200000-heartbeat ceiling. No limits raised.
No new wrapper or definition was created. Module docs/imports preserved by ownership scope.

## Generalisation status

| Parameter | Class | Role | Drop/weakening assessment | Verified result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | indexes α and P | dropping σ makes these dependent types unformed; universe already arbitrary | elaborated `#check` shows independent universes u_3/u_4; retain |
| `{A : Type*}` | type variable | coefficient ring and target of α | dropping A makes the class and dependent types unformed; already Type* | same universe evidence; retain |
| `[CommRing A]` | typeclass | commutative polynomial evaluation and additive cancellation | drop; Ring; CommSemiring | all three isolated prefix CLI probes exit 1: CommSemiring missing, or Neg missing; retain |
| `(α : σ → A)` | structure value | translation vector used twice | drop-test with autoImplicit=false; no point-local or strict/weak candidate | compiled omission reports unknown α; retain |
| `(P : MvPolynomial σ A)` | structure value | polynomial on both sides | drop-test with autoImplicit=false; type follows σ,A | compiled omission reports unknown P; retain |

The first binder-drop probe had a scratch-only docstring/`set_option` placement error;
removed that scratch docstring once and reran to isolate the intended unknown-identifier
failures. Scratch failures were never installed in source. Typeclass weakening probes
used the actual pre-target prefix and changed only the relevant section class. These
are CLI experiments, not falsely claimed live LSP substitutions.

Pointwise/global and strict/weak weakening: n/a: no propositions of these forms.
Unbundling: n/a: no bundled hypothesis. Inversion check: no specialized concrete witness;
σ, A, α and P are arbitrary, and the proof's translation operation is its stated subject.
No literature-driven big-change candidate established. An abstract additive action would
require a new interface and a restatement, without weakening this existing polynomial API.

## Public literature search

Web query: “polynomial ring translation automorphism inverse negative arbitrary commutative ring”.
Top three returned hits: [inverse-automorphism paper](https://www.sciencedirect.com/science/article/pii/S0747717108800909),
[affine substitution theorem](https://androma.org/theorems/17392), and
[polynomial automorphism thesis](https://people.math.ethz.ch/~pink/Theses/2018-Bachelor-Ajith-Kumaran.pdf).
Primary-source paper search excerpt explicitly allows any commutative coefficient ring;
this supports retaining arbitrary CommRing rather than specializing to fields/domains.
No stronger generalisation is inferred from search snippets. ChatGPT math MCP: n/a:
no callable matching tool exposed in ALL_TOOLS. No unnecessary domain, characteristic,
finiteness, decidability, or field hypotheses occur in the present theorem.

## Golfing rule pass (all 42)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no exact wrapper |
| 1.2 by rfl | n/a: no rfl wrapper |
| 1.3 rw+exact | n/a: no rewrite chain |
| 1.4 simp+exact | n/a: simp already closes |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructors | n/a: no constructor |
| 1.7 apply+exact | n/a: neither tactic |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 eta reduction | n/a: `fun j ↦ -α j` negates an application, not eta-expand f j |
| 1.10 single-use have | n/a: none |
| 1.11 apply+intro | n/a: none |
| 1.12 show | n/a: none |
| 1.13 have projections | n/a: none |
| 1.14 merge rw | n/a: none |
| 1.15 terminal simp only | n/a: already unsqueezed |
| 1.16 nonterminal simp | n/a: sole simp terminal |
| 1.17 dot notation | n/a: no explicit method application |
| 1.18 `<|` | n/a: no avoidable trailing application parentheses |
| 1.19 push Not | n/a: no push_neg |
| 1.20 existential inlining | n/a: not existential |
| 2.1 grind | actually tried `grind [taylor_taylor]`; failed cancellation goal |
| 2.2 delete before grind | n/a: no preceding steps |
| 2.3 simpa consolidation | n/a: only one terminal simp |
| 2.4 fun_prop | n/a: algebraic equality, no analytic property |
| 2.5 positivity | n/a: no positivity goal |
| 2.6 gcongr | n/a: no ordered relation |
| 2.7 lia/omega | n/a: no integer/natural arithmetic |
| 2.8 aesop | actually tried; failed, made no progress |
| 2.9 norm_num/norm_cast | n/a: no numeral computation or cast |
| 2.10 decide | n/a: arbitrary coefficient ring equality is not finite decidable computation |
| 2.11 field_simp/ring | n/a: no denominator identity; translation needs composition API |
| 2.12 linear_combination | n/a: no ring-ending proof or polynomial relation hypotheses |
| 2.13 wlog | n/a: no symmetric cases |
| 2.14 calc to term | n/a: no calc |
| 2.15 multiple goals | n/a: one equality goal |
| 3.1 erw/rw | n/a: no erw |
| 3.2 continuity/measurability | n/a: neither |
| 3.3 omega/lia | n/a: no omega or arithmetic |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation attributes | considered: avoid changing public normal-form registration in routine cleanup |
| 3.6 simp_all | n/a: no simp_all only; no local propositional hypotheses |
| 3.7 maxHeartbeats | n/a: no limit option |

Step-back reflection: existing proof is already one tactic. Bare simp makes no progress;
LSP multi-attempt confirmed `simp [taylor_taylor]` succeeds with no diagnostics.
`grind` and `aesop` fail; `exact?`/`apply?` exhaust default heartbeats. Retaining the direct
composition/cancellation proof is clearer than introducing a longer composed term.

## Local verification and freeze

Actual `/Users/ramin/.elan/bin/lake build Roth.Taylor` exited 0 after the final packing
change: Built Roth.Taylor (6.1s), Build completed successfully (1439 jobs). Existing
copyright warnings in Roth.Box, Roth.HasseDeriv, and Roth.Taylor preserved.
Native `lean_diagnostic_messages` after final edit: success=true, partial=false,
timed_out=false, only line-1 copyright warning.

`/Users/ramin/.elan/bin/lake env lean /private/tmp/decl16-final.lean` exited 0.
This file consists of the actual source prefix strictly before the target plus the
replacement declaration and closing namespace/section, excluding the target from imports
and all later declarations. It re-elaborates the exact original mathematical type and
proof, checks the fully quantified signature at format.width=100, and prints axioms:
`[propext, Classical.choice, Quot.sound]`. No sorryAx, custom axiom or native_decide.

Source frozen immediately after local gates. Whole-file SHA256:
`0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`.
Target SHA256 (without trailing newline):
`ffb55fcd66f8ef7f86c9a63db5009734dda28d9d358846452214acebff5c3568`.
Source ownership revoked; only this report edited thereafter. Parent owns the ordered
full project build followed by separate LeanEval; these are not claimed as worker results.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual final module build exit 0 |
| definition_protected | pass | no def/abbrev edits |
| theorem_statement_protected | pass | only arrow spelling and whitespace; exact original type re-elaborated |
| structure_gate | pass | one tactic; no conjunction/branches |
| naming_gate | pass | descriptive snake_case; no forbidden pattern |
| line_packing_gate | pass | table: 99+1+1=101, final line 11 |
| inequality_orientation_gate | pass | zero occurrences in scan table |
| docs/comments/API | pass | existing docstring/public theorem retained |

## Required eleven-check phase checklist

- [x] Step 1: reference docs read.
- [x] Step 2: all 24 audit items reported.
- [x] Step 2.5: all five search methods executed and qualified accurately.
- [x] Step 2.6: every parameter examined; compiled weakening evidence and literature supplied.
- [x] Step 2.7: complete signature-width table supplied and repacking applied.
- [x] Step 2.8: inequality scan table supplied.
- [x] Step 3: all 42 rules have individual statuses.
- [x] Step 4: one-tactic and alternative-proof reflection supplied.
- [x] Step 5a: complete native LSP diagnostics checked.
- [x] Step 5b: diff gates supplied; actual module build and isolated check exit 0.
- [x] Step 6a: no rename required; no shared queue mutation.

Result: 3→3 lines, 0 saved; two style issues fixed, proof unchanged; local gates pass.
