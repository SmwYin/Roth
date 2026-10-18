# Initial audit — structure repair of `exists_separated_representation`

Read the Lean/mathlib-quality skills and full golfing, proof-pattern, search,
generalisation and cleanup-gates references before editing. Scope: public proof
and one substantive private finite coefficient-span basis existence lemma.
Baseline `/private/tmp/roth-separation-s21-baseline.lean`; supplied actual profile
`/private/tmp/roth-separation-r09-profile-repeat.log`: 768.639 ms.

The polynomial is expanded once in the distinguished variable. Its finitely many
coefficient polynomials span a finite-dimensional space. Nonzeroness makes its
rank positive; its generating family bounds the rank, and support containment
bounds every basis vector's individual degrees. Coordinates in that basis supply
the independent univariate family; the existing two audited helpers establish
independence and reconstruct the polynomial. Extract the rank and degree argument
as one meaningful construction, retaining the shared expansion certificate.

1. LINT: initial complete native module diagnostics: zero errors, nine warnings;
   none in the owned theorem. Header and other declarations are outside ownership.
2. HAVE: anonymous finite-dimensional instance retained in helper (instance use);
   hP' has proof content and two consumers; hl1 has proof content; hdegree has
   proof content, retained inside helper. No trivial single-use named `have`.
3. SET_OPTION: none.
4. SIMP: one terminal `simp only [h, map_zero, mul_zero, Finset.sum_const_zero]`;
   test unsqueezed `simp [h]`. Terminal `simpa` for support membership retained.
5. NAMING: descriptive snake_case public name; new private name
   `exists_coeffNone_basis_aux`, no forbidden abbreviations or numbered suffix.
6. LINE PACKING: public signature preserved byte-for-byte; measured tables follow.
7. BY: at end of signature line.
8. FORMAT: two-space proof indentation, no empty body lines, no semicolon packing.
9. COMMENTS: no existing inline narratives in owned proof; docs preserved.
10. DOCSTRING: existing public source explanation preserved; private helper has none.
11. VISIBILITY: theorem exported for downstream caller; new helper private.
12. STRUCTURE: initial main body 30 lines; extract finite basis construction to
    obtain main <=15 and private body <=30; not irreducible casework.
13. MATHLIB: actual Finder, Loogle, LeanSearch, local name search and source search
    executed. Found canonical basis, restrictSupport, finBasis and rank bounds;
    no returned complete coefficient-span construction. Compiled generic probe follows.
14. JUNK DEF: n/a, theorem and private lemma, no definition introduced.
15. EXISTS: proposed helper has substantial positive-rank and support proof, not
    a tuple of reflexivities.
16. SHOW: none.
17. PUSH_NEG: none; existing by_contra! canonical.
18. GENERALISE: public arbitrary τ and universe polymorphism already approved;
    preserve Nat codomain and declined domain/wrapper alternatives. All binder
    drop/weakening probes and results will be recorded below.
19. INEQUALITY: all Lean occurrences use ≤; explicit occurrence table follows.
20. NORMAL FORM: finite coefficient span, Module.Basis and restrictSupport canonical.
21. SYNTAX GENERALITY: public existential families directly serve the determinant caller.
22. IMPORT FANOUT: no new imports.
23. CASTS: Fin-to-Nat powers and subtype basis-to-polynomial coercions cross types;
    explicit target polynomial ascription fixes aeval's codomain.
24. INSTANCE NAME: anonymous local finite-dimensional fact; no new global instance.

Initial action: authorized private decomposition only. Public literature and final
verification artifacts follow. Fresh independent audit of the new helper remains
the parent's required next gate after source freeze.

## Five search methods and literature

Raw initial native results: `/private/tmp/roth-separation-s21-initial-native.json`.
A. Finder query: nonzero multivariate polynomial separated representation basis
span coefficient polynomials. Hits: basisMonomials, basisRestrictSupport,
Polynomial.Sequence.basis; these do not give the required coefficient-span basis.
B. Loogle: `Module.Basis, Submodule.span, Fin`. Hits include
Module.basisOfFiniteTypeTorsionFree and Submodule.basisOfPidOfLESpan, with stronger
PID/torsion-free hypotheses and no degree/positive-rank result.
C. LeanSearch: nonzero polynomial separated sum linearly independent coefficient
span basis. Hits: Sequence.linearIndependent, Separable.ne_zero,
coeffs_nonempty_iff; no complete representation theorem returned.
D. Full source `rg` for candidate names, rank positivity/range cardinality,
restrictSupport and coefficient basis. Found canonical restrictSupport and
finrank_range_le_card; no hit for exists_coeffNone_basis_aux or coefficient-basis
existence wrapper. Auxiliary variants: restrictSupport, basisRestrictSupport,
span_le, finBasis and positive finrank. Build on these directly inside the
substantive (>10-line) construction. No custom degree submodule or predicate.
E. Native local `finrank_range_le_card`: exact source declaration found; index
was warming, so no absence claim is made about generated declarations.
Generic-route `exact?` checked on live public proof and isolated private signature.

Public literature searches: (1) “Takloo Bighash Yin Formalizing Roth theorem
Lemma 2 polynomial separated linearly independent” returned unrelated works;
(2) “tensor rank order two matrix rank minimal sum simple tensors basis
decomposition field linear algebra” returned matrix-rank, WIAS tensor-rank
preprint and tensor-rank lecture notes. The primary source
[Jan Draisma, Tensor Rank](https://math-unibe.ch/jdraisma/publications/mlappl.pdf)
states the rank decomposition interpretation over a field. Our application is
its finite coefficient-matrix construction; no characteristic restriction is
introduced. Local `.mathlib-quality/references/clean.tex:347–436` explicitly
requests the coefficient-span basis construction. No additional public restatement
is proposed. Math ChatGPT MCP unavailable (no matching tool exposed).
Private helper literature: n/a, private auxiliary construction.

## All 42 golfing rules

| Rule | Concrete status for the main proof and extracted helper |
|---|---|
| 1.1 | n/a: no by-exact wrapper |
| 1.2 | n/a: no by-rfl proof |
| 1.3 | n/a: the expansion rw changes to a different equality; following exact is substantive |
| 1.4 | support bound already uses terminal simpa; no simp/exact chain |
| 1.5 | n/a: no trailing rfl |
| 1.6 | tuple constructor already used |
| 1.7 | n/a: apply hP is followed by rewriting/simplification, not exact |
| 1.8 | by_contra! retained in positive-rank argument |
| 1.9 | n/a: all lambdas compute coordinates/bounds and depend on their bound arguments |
| 1.10 | no trivial single-use named have; anonymous finite-dimensional instance required |
| 1.11 | span_le and degree bound already take direct functions |
| 1.12 | no redundant show |
| 1.13 | obtain destructures basis and rank/degree certificate directly |
| 1.14 | no consecutive rw calls on the same goal |
| 1.15 | changed terminal simp only to simp [h] after folding expansion to v |
| 1.16 | no nonterminal bare simp |
| 1.17 | trans_eq, map', and subtype dot notation used |
| 1.18 | n/a: no trailing tactic parenthesis that benefits from <\| |
| 1.19 | n/a: no push_neg |
| 1.20 | helper has nontrivial positive-rank/support proof; not a reflexivity witness |
| 2.1 | native live main grind failed; existential families need construction |
| 2.2 | n/a: no grind in retained proof |
| 2.3 | support membership already terminal simpa using monomial bound |
| 2.4 | n/a: no analytic function-property goal |
| 2.5 | positivity cannot infer a nonzero coefficient span from a polynomial; rank witness required |
| 2.6 | direct transitive natDegree inequality, no monotone expression to traverse |
| 2.7 | direct Nat.lt_succ_iff.1 used; arithmetic automation is unnecessary |
| 2.8 | native live main aesop failed (rule-depth reached; families unconstructed) |
| 2.9 | n/a: no concrete numeric or numeric-cast calculation |
| 2.10 | n/a: no closed decidable finite proposition |
| 2.11 | n/a: no division identity |
| 2.12 | n/a: no ring/ring_nf goal with algebraic hypotheses |
| 2.13 | n/a: no symmetric branches |
| 2.14 | rank/cardinal bound already trans_eq; natDegree bound already trans |
| 2.15 | n/a: no repeated similar tactic goals; coordinate-degree goal alone remains |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no continuity/measurability |
| 3.3 | n/a: no omega in changed source |
| 3.4 | n/a: no rcases-rfl |
| 3.5 | private one-use construction does not warrant global automation registration |
| 3.6 | n/a: no simp_all only |
| 3.7 | no maxHeartbeats or other limit changes |

Step-back review: a matrix-rank/tensor route would require additional conversions
and imports. The finite coefficient-span basis is the canonical direct argument.
The two existing independent/reconstruction helpers remain untouched. New helper
is meaningful: it simultaneously constructs a bounded nonempty basis with degree
control, with 21 proof lines rather than 1–3 wrapper calls. The public proof is a
14-line outline; no tactics were joined by semicolons or hidden in a local block.

## Signature widths and inequality occurrences

All widths count Unicode codepoints. Next unit is the complete following binder
or conclusion clause (never split an application/type into dangling identifiers).
Public signature remains byte-identical, confirmed by extracting both signatures.
`#check @Roth.exists_separated_representation` rendered with `format.width 100`
is retained in `/private/tmp/roth-separation-s21-axioms.log`.

| Declaration/signature line | Width | Next binder/clause width | Sum | Action |
|---|---:|---:|---:|---|
| helper 285 | 93 | 79 | 173 | ok |
| helper 286 | 83 | 33 | 117 | ok |
| helper 287 | 37 | 69 | 107 | ok |
| helper 288 | 75 | 90 | 166 | ok |
| helper 289 | 96 | end | n/a | ok |
| main 319 | 92 | 28 | 121 | ok |
| main 320 | 32 | 85 | 118 | ok |
| main 321 | 89 | 76 | 166 | ok |
| main 322 | 82 | 49 | 132 | ok |
| main 323 | 55 | 94 | 150 | ok |
| main 324 | 100 | end | n/a | ok |

| Occurrence | Inequality | Orientation/action |
|---|---|---|
| helper 289, 1 | 1 ≤ l | canonical, retain |
| helper 289, 2 | l ≤ n + 1 | canonical, retain |
| helper 289, 3 | degreeOf j (b ρ) ≤ degreeOf (some j) P | canonical, retain |
| helper 295 | 1 ≤ Module.finrank K V | canonical, retain |
| helper 304, 1 | V ≤ restrictSupport ... | canonical, retain |
| helper 304, 2 | d j ≤ degreeOf (some j) P | canonical, retain |
| main 320 | degreeOf none P ≤ n | canonical, retain |
| main 321, 1 | 1 ≤ l | canonical, retain |
| main 321, 2 | l ≤ n + 1 | canonical, retain |
| main 322 | (φ ν).natDegree ≤ n | canonical, retain |
| main 323 | degreeOf j (ψ ν) ≤ degreeOf (some j) P | canonical, retain |

No ≥ or > in either declaration's Lean code. The conjunctions package dependent
existential witnesses; splitting them into public companion results would duplicate
construction and changes the approved API. User authorized only private decomposition.

## Generalisation/binder review

Raw fresh compiler variants: `/private/tmp/roth-separation-s21-probes.py`,
`/private/tmp/roth-separation-s21-probe-results.json`, per-variant `.lean`/`.log`.
The positive copied proof has no Fintype/DecidableEq τ assumptions at all. These
are already omitted in actual source and are not effective public binders.

| Binder | Use | Fresh mechanical probe | Result |
|---|---|---|---|
| τ : Type* | variable type of coefficients, Option and rename | remove with autoImplicit false | fails unknown τ |
| K : Type* | scalar/coefficient type | remove with autoImplicit false | fails unknown K |
| Field K | finite-dimensional basis and commutative polynomials | drop; DivisionRing; CommRing; CommRing+IsField | compiler logs below |
| P | target/coefficient polynomials | remove from main and helper separately | compiler logs below |
| hP : P ≠ 0 | positive coefficient-span rank | remove from main and helper separately | compiler logs below |
| n : ℕ | finite coefficient index and degree bound | remove from main and helper separately | compiler logs below |
| hn : degreeOf none P ≤ n | finite expansion certificate | remove from main | compiler logs below |
| hP' : finite expansion | nonzero rank certificate without repeating expansion | remove from helper | compiler logs below |

Type* already allows independent universes. Point-localisation does not apply:
there is no global continuity/order predicate. Weakening P ≠ 0 to P=0 would
change the result: a zero polynomial cannot have a positive separated rank with
both families independent. Replacing the degree hypothesis by an unrelated weaker
predicate would not certify the finite expansion. Nat codomain remains approved.
Inversion check: the coefficient functions and polynomial support occur throughout
the helper; abstract bounded generators would require new support-containment and
nonzero-family inputs. It would not be an unchanged-proof corollary, and no public
abstract companion is authorized. Declined wrapper/domain alternatives preserved.

## Verification and completion checklist

1. Read required skills/references and full target proof before edits; initial audit
   is the first section, written before touching Lean source.
2. Full 24-item audit recorded, including every have, canonical forms, casts,
   visibility and import fanout.
3. All 42 golf rules considered above. Additional live rank automation raw result:
   `/private/tmp/roth-separation-s21-rank-automation.json`: positivity reports not a
   positivity goal; grind/lia cannot construct the positive-rank witness; aesop
   reaches recursion depth. No limits raised. Expected follow-on parsing errors
   from replacement of an indented block are retained in the raw result.
4. Step-back mathematical review chose finite coefficient span, rather than tensor
   conversions or a bespoke degree submodule.
5. Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0;
   `/private/tmp/roth-separation-s21-build.log` ends “Build completed successfully
   (1876 jobs).” Ordinary compiler exit-0 check is
   `/private/tmp/roth-separation-s21-third.log`.
6. Complete unfiltered native LSP: `/private/tmp/roth-separation-s21-final-native.json`:
   success true, partial false, timed_out false; 0 errors, 9 warnings, 0 sorry.
   Warnings: preserved short header; det_hasseDeriv_separated unused section,
   DecidableEq and Fintype; exists_int_factors unused section, DecidableEq and
   Fintype; exists_det_eq_mul unused DecidableEq and Fintype. None in changed code.
7. Current public signature checked byte-identical against pre-edit snapshot. The
   isolated independent proof `/private/tmp/roth-separation-s21-independent.lean`
   uses the prior full coefficient-basis proof and never calls the target. Compiler
   exited 0; `/private/tmp/roth-separation-s21-independent.log` confirms only
   propext, Classical.choice, Quot.sound. Its arbitrary-τ statement is the exact
   current public type. Parent retains cumulative whole-original-file gate.
8. Actual built constants checked by exact suffix lookup in environment;
   `/private/tmp/roth-separation-s21-axioms.lean` and `.log`: the new helper,
   both retained existing helpers, main, and exists_det_eq_mul each have only
   propext, Classical.choice, Quot.sound. No sorry, new axioms or native_decide.
9. Scope/diff: only new private helper and owned main proof changed; both existing
   helpers, public docs/type, definitions and imports unchanged. Git reports
   +32/-20 lines; file 585→597 lines (+12). Main body 30→14 lines (31→15 if
   counting the := by signature line); new helper body 21 lines (22 with := by).
10. Performance: preliminary actual repository sweep
    `/private/tmp/roth-separation-s21-diagnose.log` plus `.json` shows main
    399.221ms, new helper696.376ms, caller576.881ms. Brief initial import-stage
    overlap means this is diagnostic evidence only; isolated final sweep follows.
    The first implicit subtype-map draft reached default whnf heartbeats;
    specifying `(Submodule.span K (Set.range v)).subtype` repaired inference,
    with no limit/statement change. Source no longer contains the failed draft.
11. Freeze/drain and independent fresh helper audit: final record follows below.

Gate review: definition_protected and theorem_statement_protected pass (unchanged
public signature); naming passes (new descriptive private `_aux` name); inequality
passes (all occurrences tabled); structure length target passes (main15 including
by, helper22). Existing dependent existential conjunction type is user-preserved.
Line-width measurements and build/LSP gates are recorded above. No renames,
public companions, wrapper deletions or public generalisations are pending.
The single new private helper still requires the parent's fresh independent audit
before publication. No Git or shared-progress mutations were made by this worker.

Fresh binder-probe outcomes: positive copied proof exits0; all drop/weakening
variants exit1. Compiler-verified details (full errors in raw logs):

| Variant | Exit | First error |
|---|---:|---|
| positive | 0 | none |
| drop_tau | 1 | error(lean.unknownIdentifier): Unknown identifier `τ` |
| drop_K | 1 | error(lean.unknownIdentifier): Unknown identifier `K` |
| drop_field | 1 | error(lean.synthInstanceFailed): failed to synthesize instance of type class |
| divisionRing | 1 | error(lean.synthInstanceFailed): failed to synthesize instance of type class |
| commRing | 1 | error(lean.synthInstanceFailed): failed to synthesize instance of type class |
| isField | 1 | error: invalid binder annotation, type is not a class instance |
| drop_P | 1 | error(lean.unknownIdentifier): Unknown identifier `P` |
| drop_hP | 1 | error(lean.unknownIdentifier): Unknown identifier `hP` |
| drop_n | 1 | error(lean.unknownIdentifier): Unknown identifier `n` |
| drop_hn | 1 | error(lean.unknownIdentifier): Unknown identifier `hn` |
| helper_drop_P | 1 | error(lean.unknownIdentifier): Unknown identifier `P` |
| helper_drop_hP | 1 | error(lean.unknownIdentifier): Unknown identifier `hP` |
| helper_drop_n | 1 | error(lean.unknownIdentifier): Unknown identifier `n` |
| helper_drop_hPprime | 1 | error(lean.unknownIdentifier): Unknown identifier `hP'` |
| helper_generic_exact | 1 | error: `exact?` could not close the goal. Try `apply?` to see partial suggestions. |

The IsField experiment is unavailable as an instance-binder weakening in
this pin: IsField is not a type class. DivisionRing fails CommSemiring; CommRing
fails DivisionRing. Effective τ/K/P/n removals fail unknown identifiers with
autoImplicit false; hP/hn/hP' removals break the actual proof. No untested
negative binder claim is presented as compiler-verified. Generic exact? cannot
close the new helper, so no inferred Mathlib construction replaces it directly.

## Final isolated performance and source freeze

Final actual repository sweep (sole active compiler/LSP request) exited0:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`.
Raw `/private/tmp/roth-separation-s21-final-profile.log` (120378802 bytes), parsed
`.log.json` and `/private/tmp/roth-separation-s21-final-profile-table.log`.
The table sums maximum outer command and outer async proof, without nested costs:

| Actual declaration | Command ms | Async proof ms | Conservative ms |
|---|---:|---:|---:|
| exists_coeffNone_basis_aux | 55.134 | 591.316 | 646.450 |
| exists_separated_representation | 58.943 | 292.125 | 351.068 |
| exists_det_eq_mul | 97.288 | 385.275 | 482.563 |

All affected declarations are below750ms, so no threshold-triggered final repeat
is needed. Supplied unchanged baseline main768.639ms had already been repeated.
This is a structural split; no whole-project performance improvement is claimed.
The sum of helper+main costs is not compared to a single old declaration as if
extraction made all mathematical work disappear.

All requests drained: native search/diagnostic/multi-attempt calls finished;
ordinary compilations, binder probe subprocesses, module build, independent proof,
built axiom probe, diagnostic profile, and final isolated profile completed. The
first abandoned draft compiler was explicitly interrupted and drained. No profiler
or temporary diagnostic instrumentation remains in Lean source.

**Frozen SHA256 of Roth/Separation.lean:**
`dc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e`.

I revoke **ALL source ownership** now and become report-only. No source edits after
this freeze. Parent must freshly audit `exists_coeffNone_basis_aux` independently,
then rerun affected gates, cumulative original/public/all-actual checks and
sequential full-project/LeanEval builds, and commit/push before original22.


## Fresh independent new-helper review

The new helper's separate fresh worker completed the full24/42/five actual searches/every effective binder/private literature exemption/width/inequality/11-step workflow and retained it unchanged. Exact original helper type was independently re-elaborated and compared with the actual built constant; independent nonself proof and actual helper/main/caller standard-axiom checks pass. Complete unfiltered native `/private/tmp/roth-s21-helper-native-final.json`: success=true, partial=false, timed_out=false, no failed dependencies,0errors/9preservedwarnings. All requests drained and all source ownership revoked. SHA remains `dc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e`.

The correlated existential basis certificate cannot split into independently chosen existential witnesses while preserving its usable shared basis; coordinator confirms the conjunction-split rule is inapplicable. No decompose flag remains. Main14body/15includingby; helper21body/22includingby.

## Owner cumulative publication gates

Source FROZEN SHA256 `dc56a933be9df1d8a0e3f3c0bc7257befbb90b29998742c1898c4f03c0e7a82e`; leaf ownership revoked and requests drained before owner gates. Owner probe `99185` exit0,53.66s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-s21-compatibility.{lean,log,json}`. Owner build session `68108` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.18s/31.57s; source hash stable. `/private/tmp/roth-separation-s21-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
