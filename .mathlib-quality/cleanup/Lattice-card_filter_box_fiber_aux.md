# NEWHELPER audit: `Roth.card_filter_box_fiber_aux`

Dedicated Phase-4 audit of `Roth/Lattice.lean` L94–118. Starting owner snapshot:
`ramin-cleanup`, `e118d1f`, clean. This is a new-helper audit, not an increment to
the original 264-declaration tally. Source ownership ended explicitly after the
owner accepted the frozen source hash. No Git mutations, shared progress edits,
rename queue edits, caller edits, public API changes, or adjacent source edits.

Frozen source SHA256:
`eabdd704d625fcba80e9529642866d57f0cd6e0274746224209ed37074981414`.

## References and baseline

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, together with the Lean and
mathlib-quality skills, the full Phase-4 worker prompt from the installed cleanup
command, and relevant style/naming sections. User/owner scope overrides broad
workflow suggestions about headers, public APIs, profiling, and shared files.

The owner supplied a green project baseline: d07 full build and separate LeanEval
33681, both exit 0 (102.58s / 38.00s), logs
`/private/tmp/roth-lattice-d07-{full,leaneval}.log`. Cache retrieval and a second
worker full build are unnecessary: owner exclusively runs final project gates.
Initial complete native LSP diagnostics: `partial=false`, `success=true`, no
failed dependencies, no warnings in this declaration. The sole file warning is
the existing header warning at L1, preserved as directed. Classic file dialect.

## Result

Before: 25 declaration lines / 20 proof lines. After: 25 / 20; zero lines saved.
Two clarity/style fixes, both tested in the live proof before contextual patches:

* Unsqueeze the terminal simplification inside `obtain`:
  `by simpa only [Finset.mem_filter, mem_box] using hd` becomes
  `by simpa [mem_box] using hd`.
* Close the final membership goal with `simp [mem_box, hext, hdp, hdr]`, removing
  an explicit `And.intro` construction and its `Fin m` binder annotation.

The extension identity `hext` retains proof content and has two uses: the
surjectivity witness and final membership simplification. No helper extraction
is justified: the longest branch has nine lines and the body has twenty lines.

## Complete 24-item audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No declaration warnings initially or finally; preserve external L1 header warning. |
| 2 | HAVE SCAN | L112 `hext := by ...`: proof content, two uses L117/L118; keep. No other `have`. |
| 3 | SET_OPTION | None; no limits, debug options, or suppression introduced. |
| 4 | SIMP SQUEEZE | L103 nonterminal `simp only` retained; all closing simplifications unsqueezed; L111 fixed. |
| 5 | NAMING | Describes filtered-box fibre cardinality; snake_case, American `fiber`, private `_aux`; no forbidden patterns/abbreviations. No rename needed or applied. |
| 6 | LINE PACKING | Five signature lines measured below, including conclusion; each next semantic unit overflows. |
| 7 | BY PLACEMENT | Both declaration and `hext` put `by` at end of preceding line. |
| 8 | FORMAT | Consistent existing indentation, no internal blank lines, no consecutive rewrites or inline-instance syntax. |
| 9 | COMMENTS | None in target; no comments/docs removed. |
| 10 | DOCSTRING | Private helper appropriately has none. |
| 11 | VISIBILITY | Private and used only by `card_filter_box_last`; appropriate. |
| 12 | STRUCTURE | 20 proof lines, no conjunction in statement, largest branch 9; no decomposition flag. |
| 13 | MATHLIB | All five actual searches below; keep explicit bijection built on `Finset.card_bij`. |
| 14 | JUNK DEF | n/a: a proof, not a data definition. |
| 15 | EXISTS LEMMA | n/a: conclusion is cardinality equality, not a trivial existential. |
| 16 | SHOW/CHANGE | No `show` or `change`. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Six-binder mechanical audit below; no mathematical weakening adopted. |
| 19 | INEQUALITY | One `≤` in signature; zero `≥`/`>`; scan table below. |
| 20 | NORMAL FORM | Canonical Finset cardinal equality and membership bounds, using standard Finsupp extension. |
| 21 | SYNTAX-GEN | Existing `r`, predicate, and last-coordinate bound fit the current caller directly. |
| 22 | IMPORT FANOUT | n/a: no new imports. |
| 23 | CASTS | No cross-type casts in target. Removed one binder type annotation through final simp; no remaining explicit cast in diff. |
| 24 | INSTANCE NAME | n/a: no instance declaration; existing anonymous decidability binder retained. |

Issues found: 2; fixed: 2; refactoring deferred: 0. Renames queued: none.

## Mathlib search status

All searches actually executed using native tool calls; search results establish
partial matches rather than a universal claim that no equivalent theorem exists.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `cardinality of a filtered finite box fiber last coordinate finsupp extension restriction` | `Fintype.card_filter_piFinset_const`, `Finset.card_snocEquiv_filter_piFinset`, `Fintype.card_filter_piFinset_eq`, and `_const_eq_of_mem`. These count function products under restricted predicates; they do not directly cover this Finsupp box with arbitrary predicate on the extension. |
| B Loogle | `Finset.card ?s = Finset.card ?t` | `card_map`, `card_image_of_injective`, `card_subtype`, `card_attach`; generic cardinal tools, no discharge of restriction/extension obligations. |
| C LeanSearch | `finite set cardinality equal by bijection with inverse restriction of functions` | `Finset.card_nbij'`, `card_bijective`, `Set.BijOn.finsetCard_eq`, `Fintype.card_eq`; partial matches. |
| D Source grep | `card_filter_box_fiber_aux`, `card_filter.*(fiber|box)`, `card_bij`, `card_nbij` in Mathlib Finset cardinal source/project; separate unrestricted full-name Mathlib grep | `card_bij`, `card_bij'`, `card_nbij`, `card_nbij'` found and inspected; no full-name target hit in Mathlib. |
| E Native name search | `card_bij` | Actual hits `Finset.card_bij`, `card_bij'`, `card_bijective`; index unavailable, so results prove presence only. |

Auxiliary variants considered: inverse-style `card_bij'`/`card_nbij'`, nondependent
`card_nbij`, `card_bijective`, `card_equiv`, and function-product fixed-coordinate
variants. Common-equivalents table: no disguised topology/bornology/etc. bucket.
The whole-proof live `exact?` failed to close; `apply?` suggested generic cardinal
bijection frameworks with the same unproved mapping/inverse obligations.
This probe was at the initial proof position, so cannot invoke the declaration
being audited. The compiled independent reproof below also cannot invoke it.

Conclusion: partial match `Finset.card_bij` already used appropriately. This is
not a 1–3-call wrapper: the content is the concrete extension/restriction
bijection. Rules 1/5 (delete equivalent wrappers) do not require deletion;
Rule 2 has actual five-method searches and non-self elaborator probes;
Rule 3 variants checked; Rule 4 no disguised typeclass hypothesis;
Rule 6 no newly adopted API needs a module-documentation edit. No repeated cast
plumbing, wrapper round trips, or manual typeclass plumbing requires a new API.
Optional abstract reindexing/box APIs have no current caller benefit and are
closed in this scope.

## Generalisation status: every binder

Native `lean_minimal_hypotheses` tested the three explicit binders on live scratch
documents. Additional compiled scratch variants tested all implicit/instance
binders. Scratch files live only under `/private/tmp`.

| # | Binder | Class/use | Candidate/probe | Verified result |
|---|---|---|---|---|
| 1 | `{m : ℕ}` | Dimension, controls `Fin`, `last`, and extension | Drop explicit binder; dimension abstraction catalogue considered | Compile exit 0, but autoImplicit regenerates the identical `{m : ℕ}` binder: no weakening; keep explicit declaration. Abstract finite-index restatement adds no caller benefit. |
| 2 | `(r : Fin (m + 1) → ℕ)` | Structure value, box bounds | Native drop | Load-bearing: dimension/application mismatch at `r (Fin.last m)`; keep. Type fixed by existing box API, no parent class/pointwise weakening. |
| 3 | `(p : (Fin (m + 1) →₀ ℕ) → Prop)` | Arbitrary predicate used in both filters | Native drop | Load-bearing: filter/function type mismatch; keep. Already arbitrary, so no stronger global premise to localise. |
| 4 | `[DecidablePred p]` | Decidability required in statement filters | Compiled drop | Exit 1: failed synthesis `DecidablePred p`; proof-local `classical` cannot supply a signature instance. No parent weakening. |
| 5 | `{i : ℕ}` | Last-coordinate value used in singleton/filter/bound | Drop explicit binder | Compile exit 0, but autoImplicit reintroduces `i` as an implicit Nat and changes binder order: no mathematical weakening; keep current explicit position. |
| 6 | `(hi : i ≤ r (Fin.last m))` | Bounds the new coordinate in first bijection branch | Native drop and compiled replacement by `True` | Both fail at L105; bound already non-strict and pointwise. No strict-to-weak or global-to-local candidate remains. |

Native explicit-drop results: `r`, `p`, `hi` all `load-bearing`; no tool errors.
Implicit variants: `/private/tmp/roth-fiber-{drop_m,drop_i,drop_decidable,weaken_hi}.lean`.
Sessions 55504/24462 exited 0; 26617/25961 exited 1 with the expected diagnostics.
Failing scratch variants are negative experiments, not accepted proofs. No
statement, hypothesis, typeclass, universe, or argument-order changes accepted.
There are no type variables to universe-generalise, no algebra/analysis
typeclasses to weaken, and no bundled conjunction premise to unbundle.

Inversion check: `box` expands to coordinatewise inequalities, but the remaining
proof uses `Fin.castSucc`, `Fin.last`, their cases, and Finsupp extension
throughout. Generic cardinality is already delegated to `card_bij`; additional
abstract API does not improve the sole caller. Big-change candidates: none open.
Literature search: n/a, private declaration, literature search not required.

## Line packing

Independent exact-type clone checked under `set_option format.width 100 in
#check @fiberAuditOriginal`; its rendered type is:

```lean
@fiberAuditOriginal : ∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop) [inst : DecidablePred p] {i : ℕ},
  i ≤ r (Fin.last m) →
    #({d ∈ box (r ∘ Fin.castSucc) | p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}) =
      #({d ∈ filter p (box r) | d (Fin.last m) = i})
```

Measured source codepoint widths, not bytes; every signature line included.
Units preserve complete binders and complete filter predicate applications;
they are the first meaningful signature unit of the next line.

| Sig line | Chars | Next semantic unit, width | Arithmetic | Action |
|---|---:|---|---|---|
| 94 | 69 | `(p : (Fin (m + 1) →₀ ℕ) → Prop)`, 31 | 69 + 1 + 31 = 101 > 100 | ok |
| 95 | 89 | `((box (r ∘ Fin.castSucc)).filter fun d ↦`, 40 | 89 + 1 + 40 = 130 > 100 | ok |
| 96 | 44 | `p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card =`, 68 | 44 + 1 + 68 = 113 > 100 | ok |
| 97 | 74 | `(((box r).filter p).filter fun d ↦ d (Fin.last m) = i).card := by`, 65 | 74 + 1 + 65 = 140 > 100 | ok |
| 98 | 73 | Proof body next | n/a | ok |

No signature changes/repacking necessary; in particular the first binder break
is justified by a one-column overflow. No isolated `:= by`. Entire target max
width is below 100. No single-wide-hypothesis escape claimed.

## Inequality scan

| Location | Lean occurrence | Orientation/action |
|---|---|---|
| L95 | `i ≤ r (Fin.last m)` | Smaller side left; preserve. |
| Signature L94–98 | `≥`: 0; `>`: 0 | No reversal or rename needed. |
| Proof bound at L105 | Derived via `hi` | Same oriented bound; no arithmetic inequality normalisation. |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no `rw` followed by `exact`. |
| 1.4 | Existing `simpa using` already consolidates closing steps; final one improved to simp. |
| 1.5 | n/a: no trailing `rfl`. |
| 1.6 | Existing nested anonymous constructor used; no constructor/exact chain. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction/negation chain. |
| 1.9 | All lambdas select coordinates or carry membership arguments; none is `fun x ↦ f x`. |
| 1.10 | `hext` has proof content and two uses, retained. |
| 1.11 | n/a: no apply/intro chain. |
| 1.12 | n/a: no redundant `show`. |
| 1.13 | Existing `obtain` destructures source membership appropriately. |
| 1.14 | n/a: no rewrites. |
| 1.15 | Applied L111: unsqueezed terminal simp inside obtain. |
| 1.16 | Nonterminal simp L103 already `simp only`; all other simp calls close their goals. |
| 1.17 | Tested anonymous conjunction successfully; chose stronger final simp removing construction entirely. |
| 1.18 | n/a: parentheses around tactic term inside `Fin.lastCases` are needed to separate subsequent arguments; no beneficial trailing-paren transformation. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not a trivial existential helper. |
| 2.1 | Whole proof `grind` failed; first bijection branch grind with both extension lemmas also failed. |
| 2.2 | n/a: no retained grind/preparatory chain. |
| 2.3 | Applied final `simp [mem_box, hext, hdp, hdr]`, simplifying membership directly. |
| 2.4 | n/a: no analytic function property. |
| 2.5 | n/a: no positivity goal. |
| 2.6 | n/a: no monotone inequality chain; bound goal is a coordinate case split using assumptions. |
| 2.7 | n/a: no Nat/Int arithmetic subgoal after coordinate simplification; no lia/omega candidate. |
| 2.8 | Whole `aesop` failed; first branch aesop failed; final aesop succeeded but terminal simp is clearer. |
| 2.9 | n/a: no numeric computation or cast goal. |
| 2.10 | n/a: arbitrary predicate/cardinality identity cannot be closed by finite computation. |
| 2.11 | n/a: no denominators or ring identity. |
| 2.12 | n/a: no ring/ring_nf ending or polynomial identity. |
| 2.13 | n/a: mapping/injectivity/surjectivity branches prove different obligations; no symmetric duplicate cases. |
| 2.14 | n/a: no calc. |
| 2.15 | Existing hext applies one simp to both coordinate cases with `<;>`; retained. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy continuity/measurability tactic. |
| 3.3 | n/a: no omega and no arithmetic-goal replacement. |
| 3.4 | n/a: no rcases-with-rfl followed by redundant substitution. |
| 3.5 | No automation attribute added: one-use private helper for a specific box fibre. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no heartbeat/recursion option. |

Live final-goal probes: anonymous `⟨fun j : Fin m ↦ hdr j.castSucc, hdp⟩`
worked; deleting `Fin m` from the old `And.intro` version failed unresolved
`j.castSucc`; direct simp and aesop-with-simp both worked. Direct simp removes
the elaboration issue rather than adding an annotation. Bare simp in obtain
without `mem_box` failed downstream because `hdr` remained a membership proof.

Step-back reflection: whole-proof `grind`, `simp [mem_box]`, `aesop`, and `exact?`
do not prove the required bijection. `apply?` only rediscovered cardinality
frameworks. A complete function-product/equivalence restatement would add
transport plumbing; the current card_bij proof directly records the mathematical
bijection and shares its extension identity. Term mode adds no clarity.

## Verification and gates

`/Users/ramin/.elan/bin/lake build Roth.Lattice`, session 65137, exit 0:
`Built Roth.Lattice (34s)` and `Build completed successfully (2214 jobs)`.
Only the preserved Box/Lattice header warnings occurred. Complete native LSP
after both source changes: `success=true`, `partial=false`, `timed_out=false`,
`failed_dependencies=[]`, no target warnings/errors.

Independent exact-signature reproof:
`/private/tmp/roth-fiber-independent.lean`, importing only `Roth.Box`, recreates
the two elementary extension facts and the target proof under a fresh name.
Session 50270: `lake env lean` exit 0, `#check` and `#print axioms` succeeded;
axioms exactly `[propext, Classical.choice, Quot.sound]`. It neither imports nor
calls the target theorem. Initial and final signature source is byte-identical.
Native `lean_verify` on `Roth.card_filter_box_fiber_aux`: standard trust,
same three axioms, no nonstandard axioms, no source warnings.

Actual built-environment private check: `/private/tmp/roth-fiber-built.lean`
imports `Roth.Lattice`, enumerates environment constants by the exact target
suffix, and calls `Lean.collectAxioms` on the found name (no guessed numeric
private identifier syntax). Session 81255, exit 0, found
`_private.Roth.Lattice.0.Roth.card_filter_box_fiber_aux`; axioms exactly
`[propext, Classical.choice, Quot.sound]`.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build session 65137 exit 0. |
| definition_protected | pass | Diff has no definitions/abbreviations. |
| theorem_statement_protected | pass | Exact initial signature byte-identical; independent exact-type reproof compiles. |
| structure_gate | pass | Body 20, max branch 9, no statement conjunction. |
| naming_gate | pass | Descriptive snake_case private `_aux`; no forbidden pattern; no rename. |
| line_packing_gate | pass | All five measured rows above, no repack row. |
| inequality_orientation_gate | pass | Zero reversed inequalities. |
| cumulative_no_unintended_external_breakage | worker pass | Sole caller in same successfully compiled module; final full project checks reserved to owner. |
| source_integrity | pass | Contextual patch only two proof lines; no sorry/axiom/limit/suppression, diff --check clean. |

Overall worker gates: pass. File-wide simplify/performance and final full/LeanEval
checks belong to owner after source freeze; no optional profiling performed here.

## Required eleven-check checklist

* [x] Step 1: reference documents read.
* [x] Step 2: all 24 audit items answered.
* [x] Step 2.5: all five actual searches and six strict replacement rules recorded.
* [x] Step 2.6: every binder mechanically audited; private literature exemption recorded.
* [x] Step 2.7: width-100 check plus five-row packing arithmetic.
* [x] Step 2.8: per-occurrence inequality scan.
* [x] Step 3: all 42 golfing rules reported.
* [x] Step 4: strategy/automation reflection completed.
* [x] Step 5a: complete final native LSP diagnostics clean in target.
* [x] Step 5b: actual module build and diff gates recorded.
* [x] Step 6a: no rename required; no shared queue mutation.

No pending refactoring, no caller changes, no public restatement proposal.

Owner checkpoint: explicit source edit revocation before sequential full/separate LeanEval session46779; both exit0 (84.53s/29.47s), frozen hash unchanged. Logs `/private/tmp/roth-lattice-helper-fiber-{full,leaneval}.log`. Original264 tally unchanged.
