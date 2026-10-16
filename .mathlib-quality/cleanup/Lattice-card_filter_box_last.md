# `Roth.card_filter_box_last` dedicated cleanup

Source frozen at SHA256 `d3a5301ef1c44bf385b8918923fe31d25d013840fefa4fc5764a3dbf903386a5`.
Only target proof, equivalent signature formatting/lambda spelling, and one authorized private
proof helper changed. Public type and documentation are preserved. No Git/shared ledger actions.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, the Phase 4 worker instructions,
and the relevant style/naming sections. Applied lean4 and mathlib-quality skills.

## Mathematics and initial punch list

Partition the filtered box by its last coordinate. For each coordinate value, extending a
multi-index in the smaller box gives a bijection onto that fibre. Restriction provides the
inverse. The original proof repeated the reconstruction identity twice in its surjectivity
branch. Extract the substantial fibre cardinality proof and establish reconstruction once.
No hypothesis on the predicate or positivity of the box dimensions is needed.

Baseline supplied by owner: d06 full build and separate LeanEval (51672), both exit 0;
logs `/private/tmp/roth-lattice-d06-{full,leaneval}.log`. Initial complete native LSP:
only inherited header warning at line 1, outside target. Cache/linter/full-build orchestration
belongs to owner. This worker ran the actual target module build independently.

## All 24 audit items

| # | Item | Concrete result |
|---|---|---|
| 1 | Lint | No target warning/error; inherited header warning preserved under user constraint. |
| 2 | Have scan | Original `hext` had proof content but repeated reconstruction separately; new helper has one proof-content `hext`, used in both witness obligations. Public proof has none. |
| 3 | Options | No per-declaration options, limit raises, traces, or suppressions. |
| 4 | Simp | Nonterminal simplification remains explicit `simp only`; final `simpa`/`simp` calls remain unsqueezed. |
| 5 | Naming | `card_filter_box_last` describes cardinality, filter, box and last coordinate; snake_case, no forbidden pattern/abbreviation. New private `card_filter_box_fiber_aux` describes the mathematical fibre fact. No rename required or applied. |
| 6 | Packing | Every signature line measured below, including conclusion; width-100 reference recorded in verification log. |
| 7 | By | `by` remains on preceding line everywhere. |
| 8 | Format | Two-space tactics; no empty internal lines; lambda arrows changed to `↦`; original semicolon chain eliminated. No `haveI`/`letI`. |
| 9 | Comments | No inline proof comments originally; none deleted. |
| 10 | Docs | Existing public docstring byte-preserved; private helper has no docstring. |
| 11 | Visibility | Public theorem retained as API; new proof implementation private. |
| 12 | Structure | Original public declaration 43 lines; final 11 lines, proof 7 lines. One private helper 25 lines, proof 20 lines; largest branch 9 lines. Duplicate reconstruction removed. |
| 13 | Mathlib | Five actual methods below; retain specialized box result on existing `card_eq_sum_card_fiberwise` and `card_bij`. |
| 14 | Junk def | n/a: theorem; no data declarations added. |
| 15 | Exists lemma | n/a: no single-use existential helper declaration. |
| 16 | Show/change | n/a: no `show` or `change`. |
| 17 | Push neg | n/a: no negation tactics. |
| 18 | Generalise | All four public parameters mechanically probed, below. No API changes. |
| 19 | Inequality | No reversed inequality in public signature; helper has only smaller-left `i ≤ r (Fin.last m)`. |
| 20 | Normal form | Cardinality equals sum of fibre cardinalities, the standard additive counting normal form. |
| 21 | Syntax generality | Existing predicate parameter already arbitrary; filtering syntax directly rewrites downstream. |
| 22 | Imports | n/a: no imports added. |
| 23 | Casts | 0 dropped / 0 cross-type / 0 load-bearing explicit casts in changed proof. |
| 24 | Instance names | n/a: no instance declaration. |

## Mathlib search-status

[A] Lean-Finder: actual query "Finsupp on Fin (n+1) split into restriction Fin.castSucc and
single Fin.last"; remote read timed out. This is tool failure, not evidence of absence.
[B] Loogle: `Finsupp.mapDomain, Finsupp.single`; returned `mapDomain_single`,
`mapDomain_fintype`, `mapDomain_apply` (partial building blocks).
[C] LeanSearch: "cardinality finite box filter sum fibers last coordinate";
returned `Finset.card_eq_sum_card_fiberwise`, `sum_card_fiberwise_eq_card_filter`,
`Fintype.card_filter_piFinset_eq_of_mem`, and constant variants.
[D] Source rg: full names `card_filter_box_last`, `card_filter_box_fiber`,
`castSucc.*single`, `lastCases` searched without truncation in relevant Finsupp/Fin/
BigOperators files; no duplicate specialized identity found in those files.
[E] Native local name search: `card_eq_sum_card_fiberwise` returned exact mathlib source.
Index reported unavailable, so no absence claim is based on an empty name result.
Auxiliary variants considered: fibrewise filtered count, piFinset filter count,
mapDomain application/single/fintype. Common-equivalents table: no matching disguised concept.
Conclusion: partial match found; retain specialized public statement and build directly on
mathlib's partition/cardinality API. New helper contains a substantive extension/restriction
bijection, not a 1–3-call convenience wrapper. No generic absence claim is made.
Native `exact?`/`apply?` public-goal probes found no closing replacement; `apply?` offered
only generic equality/cardinality subgoals. Initial mispositioned multi_attempt results were
discarded; later exact-column attempts had suffix parse errors and are not compilation gates.

## Generalisation status

| Parameter | Role | Mechanical probe | Result |
|---|---|---|---|
| `{m : ℕ}` | finite dimension | Drop with `autoImplicit false`, actual shell Lean | Rejected: unknown `m`; indexed construction needs dimension. No class parent or universe binder applies. |
| `(r : Fin (m + 1) → ℕ)` | arbitrary bounds | Native minimal-hypothesis and shell drop | Rejected: dependent type/application mismatch and unknown `r`. No strict/global hypothesis to weaken. |
| `(p : (Fin (m + 1) →₀ ℕ) → Prop)` | arbitrary predicate | Native minimal-hypothesis and shell drop | Rejected: predicate/type information required. Already universally arbitrary. |
| `[DecidablePred p]` | filter decidability | Shell drop | Rejected at statement: failed `DecidablePred p`; proof-local classical arrives too late. No meaningful parent class. |

Logs: `/private/tmp/card_last_drop_{m,r,p,dec}.log`. Native minimal-hypothesis tool
also checked new helper explicit `r`, `p`, `hi`; all load-bearing. Owner will assign
fresh dedicated audit to that helper; this report does not count it as another declaration.
No safe typeclass, pointwise, strict-to-weak, or universe weakening applies to the remaining
concrete natural/index values. Inversion check: generic partition mathematics is already
provided by mathlib; specialized part uses coordinate extension and box bounds throughout.
No new abstraction with a current downstream benefit was identified.

Literature: actual web query "cardinality finite set sum cardinalities fibers generalization
counting principle" found the finite disjoint addition rule in [Cornell course notes](https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec16-combinatorics.html),
[SFU counting notes](https://www2.cs.sfu.ca/CourseCentral/101.MACM/manuelz/l/07/07x6.pdf),
and [ETSU notes](https://faculty.etsu.edu/gardnerr/3000/notes-MR/Gerstein-4-1.pdf).
Inference: this specialized fibre decomposition is an instance of that rule, already modeled
by `Finset.card_eq_sum_card_fiberwise`. No literature-driven missing hypothesis found.
ChatGPT math MCP: n/a, no callable connected tool exposed. Big-change candidates: none pursued;
abstract finite-index partition APIs are already available and optional restatements lack a
current benefit. Existing API/docs locked by user instruction.

## Width tables (codepoints, final source)

Next token means the complete next binder or coherent conclusion fragment, as in the cleanup
reference; lexical fragments are not arbitrarily peeled from expressions.

| Public line | Width | Next binder/fragment width | Arithmetic | Action |
|---|---:|---:|---|---|
| 125 | 90 | `[DecidablePred p]`: 17 | 90 + 1 + 17 = 108 | ok |
| 126 | 83 | filtered-box expression through `↦`: 40 | 83 + 1 + 40 = 124 | ok |
| 127 | 46 | predicate application through `:= by`: 72 | 46 + 1 + 72 = 119 | ok |
| 128 | 80 | no next signature line | n/a | ok |

| Helper line | Width | Next binder/fragment width | Arithmetic | Action |
|---|---:|---:|---|---|
| 94 | 69 | `(p : (Fin (m + 1) →₀ ℕ) → Prop)`: 31 | 69 + 1 + 31 = 101 | ok |
| 95 | 89 | filtered-box expression through `↦`: 40 | 89 + 1 + 40 = 130 | ok |
| 96 | 44 | predicate application through `=`: 68 | 44 + 1 + 68 = 113 | ok |
| 97 | 74 | fibre cardinality through `:= by`: 65 | 74 + 1 + 65 = 140 | ok |
| 98 | 73 | no next signature line | n/a | ok |

Inequality scan:

| Declaration | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| public | signature/hypotheses | no `≥`/`>` | n/a | n/a |
| helper | `hi` | `i ≤ r (Fin.last m)` | already smaller-left | n/a |

## All 42 golfing rules

| Rule | Result |
|---|---|
| 1.1 | n/a: no `by exact` declaration wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | Applied: eliminated original `rw [hext]; exact hdp` via one terminal `simpa`. |
| 1.4 | Applied: reconstruction and membership consolidated with `simpa`. |
| 1.5 | n/a: no trailing `rfl`. |
| 1.6 | Applied: witness uses anonymous conjunction/constructor. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction/negation. |
| 1.9 | n/a: evaluation/extension lambdas depend genuinely on arguments. |
| 1.10 | n/a: sole final `have hext` has proof content and two uses. |
| 1.11 | Applied: direct `sum_congr rfl fun ...` and direct lastCases. |
| 1.12 | n/a: no `show`. |
| 1.13 | Applied: membership destructured immediately by `obtain`. |
| 1.14 | n/a: no consecutive rw calls remain. |
| 1.15 | n/a: only nonterminal `simp only`; terminal `simpa` unsqueezed. |
| 1.16 | n/a: no nonterminal bare simp remains. |
| 1.17 | Applied: final fibre identity `.symm`. |
| 1.18 | n/a: no avoidable `$`/trailing-parenthesis proof chain. |
| 1.19 | n/a: no `push_neg`. |
| 1.20 | n/a: no private trivial existential lemma. |
| 2.1 | Actual native `grind` whole-goal attempt failed to close cardinality identity. |
| 2.2 | n/a: no existing grind prefix. |
| 2.3 | Applied: two coordinate branches use `simpa` directly. |
| 2.4 | n/a: no analytic function property. |
| 2.5 | n/a: no positivity goal. |
| 2.6 | n/a: no monotonicity chain. |
| 2.7 | n/a: natural bound transported exactly by `Nat.lt_succ_iff`, no arithmetic search needed. |
| 2.8 | Actual native aesop attempt did not supply a valid replacement (suffix parser errors); explicit bijection retained. |
| 2.9 | n/a: no concrete numeral or cast goal. |
| 2.10 | n/a: arbitrary predicate and unbounded dimensions preclude closed finite decision. |
| 2.11 | n/a: no denominators. |
| 2.12 | n/a: no polynomial equality/ring ending. |
| 2.13 | n/a: reconstruction coordinate cases are structurally different, not symmetric. |
| 2.14 | n/a: no calc. |
| 2.15 | Applied: both reconstruction coordinate goals closed by `<;> simp [...]`. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases-rfl. |
| 3.5 | No new global attribute: private proof helper not an intended simp normal form. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no limits/options to remove. |

Step-back/simplify review: the public result now directly partitions and sums the substantive
fibre lemma. The helper's extension is injective by evaluating castSucc coordinates and
surjective by restriction; one reconstruction proof serves both uses. A bundled equivalence
would add data/API for a single use; no current benefit. No wrapper, new data definition,
or public module split is necessary. No pending rename/decomposition/API action.

## Verification, gates and phase checklist

`/Users/ramin/.elan/bin/lake build Roth.Lattice` exited 0, actual module rebuilt in 34s:
`/private/tmp/roth-card-last-build2.log`. Complete native LSP, after final edit, returned
`success: true`, `partial: false`, `timed_out: false`; only inherited line-1 copyright
warning remains. Target end-position goal inspection returned no remaining goals.

Original exact-type assignment compiled, exit 0:
`/private/tmp/card_last_exact_clean.lean` and `.log`. Independent original `card_bij`
proof, using no reference to the target theorem or new fibre helper, compiled exit 0:
`/private/tmp/card_last_independent.lean` and `.log`. Actual public and actual private
helper were both checked by native `lean_verify`; both returned `trust: standard`,
`[propext, Classical.choice, Quot.sound]`, zero nonstandard axioms and zero warnings.
The independent theorem has exactly the same standard axiom list.

Width reference from actual `set_option format.width 100; #check @Roth.card_filter_box_last`:

```lean
@Roth.card_filter_box_last : ∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop) [inst : DecidablePred p],
  (Finset.filter p (Roth.box r)).card =
    ∑ i ∈ Finset.range (r (Fin.last m) + 1),
      {d ∈ Roth.box (r ∘ Fin.castSucc) | p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}.card
```

The configured printer still emits an oversized binder line; source follows measured
100-codepoint packing rather than copying that oversized rendered line.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Lattice`, exit 0. |
| definition_protected | pass | No def/abbrev or data construction declaration changed/added. |
| theorem_statement_protected | pass | Original exact public type compiled; only equivalent whitespace/lambda syntax changed. |
| structure_gate | pass | Public proof 7 lines; helper proof 20; largest branch 9; no public conjunction. |
| naming_gate | pass | Both descriptive snake_case names; no forbidden pattern; no renames. |
| line_packing_gate | pass | All four public signature lines measured; all five helper signature lines included. |
| inequality_orientation_gate | pass | Public zero inequalities; helper only `≤`, no reversed symbol. |
| docstring protection | pass | Existing docstring retained verbatim; no comments removed. |
| trust/no scaffolding | pass | Actual public/helper standard axioms; no new axioms/sorry/limits/traces/options in source. |
| cumulative_no_unintended_breakage | owner final gate | Public type preserved; source edit ownership revoked; full build/separate LeanEval reserved to owner after explicit freeze. |
| optional docstring_only_changes | n/a | Authorized proof cleanup, not docstrings-only. |

All eleven Phase-4 checks:

- [x] Step 1 — required references read.
- [x] Step 2 — all 24 audit items recorded with concrete status.
- [x] Step 2.5 — five actual search methods, honest timeout/index limitations recorded.
- [x] Step 2.6 — every public parameter drop-probed, literature search and inversion check recorded.
- [x] Step 2.7 — per-line signature widths/arithmetic recorded.
- [x] Step 2.8 — per-occurrence inequality scan recorded.
- [x] Step 3 — all 42 golfing rules assigned a status.
- [x] Step 4 — mathematical step-back/simplify review recorded.
- [x] Step 5a — final complete LSP clean except inherited out-of-scope header warning.
- [x] Step 5b — actual module build and scoped diff/protection/content gates recorded.
- [x] Step 6a — no rename necessary; no sidecar mutation.

Performance: two actual whole-file profiling compiles exited 0:
`lake env lean -Dprofiler=true -Dprofiler.threshold=1 Roth/Lattice.lean`
(`/private/tmp/roth-card-last-profile.log`), and `lake env lean --profile Roth/Lattice.lean`
(`/private/tmp/roth-card-last-decl-profile.log`). The latter reports import 29.3s,
file-total simp 203ms, tactic execution 376ms, type checking 115ms, typeclass inference 878ms.
Native per-declaration profiler could not compile its standalone extraction because it omits
the same-file private helper. These file totals do not establish an exact per-declaration
wall time; final owner buzz may use a contextual extraction if exact attribution is required.
No source profiling scaffolding added; profiling was entirely CLI flags. No source edits
are permitted after freeze, so this limitation is reported explicitly, not hidden as a
measured per-declaration timing.

New helper requiring its own fresh dedicated audit, after owner checkpoint:
`Roth.card_filter_box_fiber_aux` at lines 94–118, and no others. This public declaration
cleanup makes no additional 264-declaration tally increment for the helper.

Final result: public declaration 43 → 11 lines (7-line proof); substantial private fibre
bijection 25 lines (20-line proof), replacing duplicated reconstruction with one local fact.
Source remains frozen at the hash above. Report-only work may overlap owner's builds.

Owner checkpoint: explicit source edit revocation before sequential full/separate LeanEval session33681; both exit0 (102.58s/38.00s), frozen hash unchanged. Logs `/private/tmp/roth-lattice-d07-{full,leaneval}.log`. New helper fresh dedicated audit follows this publication.
