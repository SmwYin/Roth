# Cleanup: `Roth.lem6M` (original 21)

Outcome: retain unchanged. The one-line data expression names the paper's important coefficient bound. No source edits, helpers, callers, imports, visibility changes, API changes, or renames.

## Baseline and scope

Release: owner checkpoint `d383b852a555586931b85fb19fca94c96d0ff97b`, pushed before this leaf. Owner reports full build 39.883s then separate LeanEval 15.025s, both exit 0. These are inherited baseline evidence, not this worker's commands. Matching inherited complete LSP: `/private/tmp/roth-theta-log-helper/final-lsp.json`. Source SHA256 throughout: `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`.

Read leaf instructions, both skills, complete cleanup workflow, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, naming/profiling, relevant style sections, current declaration/context and immutable original `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Preparation was read-only until RELEASE. Dialect: classic.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | None at target lines 263–266; full final diagnostics retained below. |
| 2 | Have scan | None: arithmetic data expression. |
| 3 | Options | No declaration options or raised limits. |
| 4 | Simp squeeze | No tactic calls. |
| 5 | Naming | `lem6M` is lowerCamelCase data naming; no forbidden numeric/aux/abbreviation pattern. It identifies the documented paper constant M. No beneficial rename recommended. |
| 6 | Packing | Measured table below; one signature line. |
| 7 | By placement | No `by`: direct term mode. |
| 8 | Format | Two-space body, no blanks or trailing whitespace, 67-character body. |
| 9 | Comments | No inline comments; docstring preserved byte-for-byte. |
| 10 | Docstring | Existing two-line explanation identifies formula and source equation (16); retained. |
| 11 | Visibility | Named public constant in module Main definitions, used across main statements; keep public. |
| 12 | Structure | One body line, no branches or conjunction. No extraction needed. |
| 13 | Mathlib | Actual five-method search below; generic ingredients found, no replacement identified. |
| 14 | Junk def | Not junk: names paper eq16, appears in several public statements and proofs, has `one_le_lem6M` and `lem6M_lt` API. |
| 15 | Exists lemma | Not an existential lemma. |
| 16 | Show/change | Neither occurs. |
| 17 | Push neg | None. |
| 18 | Generalise | Every effective binder tested below. Semiring restatement compiles but public real constant should remain stable. |
| 19 | Inequality | Zero occurrences in signature, table below. |
| 20 | Normal form | Exact paper factor order and natural exponents; no competing canonical object identified. |
| 21 | Syntax generality | Explicit p, r₁, B, l supports existing partial/full applications; preserve order. |
| 22 | Import fanout | No imports introduced. |
| 23 | Casts | Existing `(r₁ : ℝ)` is genuine Nat-to-Real conversion determining real addition/powers; factorial also coerces Nat-to-Real. No diff casts. |
| 24 | Instance names | Definition, not an instance; no names to remove. |

Issues fixed: none needed. Refactoring needed: none recommended. Comments preserved: existing docstring unchanged; no inline comments present.

## Line packing

`#check @Roth.lem6M` at `format.width 100`: `Roth.lem6M : ℕ → ℕ → ℝ → ℕ → ℝ`.

| Signature line | Characters | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 265 | 57 | None: next line is term body | n/a; complete signature | ok |

The 65-character body expression excluding indentation would make a combined line 57 + 1 + 65 = 123 > 100; separate term line is justified.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | Entire signature | No `≥` or `>` | n/a | n/a |

## Five actual mathlib search methods

Raw responses: `/private/tmp/roth-theta-lem6M/searches.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | Roth theorem determinant coefficient bound constant (r+1)^(p*l) factorial l B^l 2^(p*l*r) | Returned unrelated corners/Szemeredi/Hermite bounds; no equivalent identified. |
| B Loogle | `"factorial", "pow"` | `Nat.factorial_le_pow`, descendant/ascending factorial inequalities: generic ingredients, not this definition. |
| C LeanSearch | Roth theorem auxiliary determinant coefficient bound factorial powers | `Matrix.det_le`, `Matrix.det_sum_le`, unrelated Behrend bound: partial mathematical ingredients only. |
| D Source rg | `lem6M|roth.*factorial|factorial.*roth` over all Mathlib | No textual matches. Read factorial/power variants in Data.Nat.Factorial.Basic; no exact named constant. |
| E Native local search | `lem6M` | Found project definition and its bound; `index=unavailable`, so this is a source-backed hit, not an indexed absence claim. |

Auxiliary variants: factorial_le_pow, ascFactorial_le_factorial_mul_pow, factorial_mul_pow_le_factorial; determinant absolute-value bounds. Common-equivalents table has no matching bucket. All five methods executed, but no global absence proof is claimed. This is retained existing named data, not a newly invented theorem requiring an `exact?` absence certificate. There is no proposition to solve via exact?/apply? and no new wrapper to create/delete. Known full-Theta multi_attempt stall was not repeated.

## Generalisation and compiled binder probes

Effective original type is exactly `ℕ → ℕ → ℝ → ℕ → ℝ`; no σ/τ/universe/Fintype/DecidableEq section binders occur. Exact type AST comparison against independently elaborated immutable original passed.

| Binder | Class/use | Compiled drop probe | Value-sensitivity certificate | Decision |
|---|---|---|---|---|
| p : ℕ | Natural exponent parameter | drop0: unknown p in exponents | M(0,1,1,1) ≠ M(1,1,1,1) | retain |
| r₁ : ℕ | Degree parameter in base and exponent | drop1: unknown r₁ | M(1,0,1,1) ≠ M(1,1,1,1) | retain |
| B : ℝ | Coefficient bound base | drop2: unknown B | M(1,1,1,1) ≠ M(1,1,2,1) | retain |
| l : ℕ | Factorial and exponent parameter | drop3: unknown l/l.factorial | M(1,1,1,0) ≠ M(1,1,1,1) | retain |

`negative.lean` compiled exit 1 with only expected unknown identifier failures; `autoImplicit false` ensures omitted variables cannot be silently rebound. `positive.lean` separately compiled exit 0 (`positive-final.log`) including all four nonconstancy certificates.

Catalogue: no propositional hypotheses/typeclasses, strict inequalities, pointwise assumptions, or universe parameters to weaken. Generalizing p/r₁/l away from Nat would change natural powers/factorial meaning. A scratch semiring-codomain candidate `abstractCandidate {K} [Semiring K]` compiled, and its real specialization equals current M by rfl. This mechanical abstraction is not recommended for the published real coefficient bound: its downstream Θ/log/real-power API remains real, and it adds a class/type parameter without an identified application. Candidate retained only in scratch. No production change.

Inversion: not applicable to a proposition/proof; M is directly the explicit arithmetic construction, so there is no post-unfolding proof secretly establishing a broader theorem. The semiring construction above checks the only obvious abstract arithmetic form without inventing helper API.

## Public literature search

Read local primary manuscript `.mathlib-quality/references/clean.tex` lines 704–744: equation `roth:eq16` is exactly `M= (r_1+1)^{pl} l! B^l 2^{plr_1}`. The proof uses it as a determinant coefficient bound. It is deliberately named in the statement of Lemma 6, so inlining it would degrade correspondence.

Actual web searches: `"Formalizing Roth" "Takloo" Yin`; `Roth theorem lemma 6 determinant coefficient bound factorial M`; `Nakamaye Roth theorem lecture notes filetype:pdf`; `"Takloo-Bighash" "Yin" "Roth" formalizing`. Results included several unrelated additive-combinatorics Roth theorems and mirrors of Nakamaye notes; they do not justify changing this specific constant. [Nakamaye's research article](https://archive.numdam.org/item/JTNB_1999__11_2_439_0/) concerns broader Diophantine approximation but supplies no reason to alter the manuscript's exact eq16 definition. No claim of exhaustive literature absence. ChatGPT math MCP is unavailable (no matching callable tool). Literature-driven changes: none recommended.

## All 42 golf rules

Each rule was checked against the actual term definition. There is no proof block to replace by automation; adding tactics to construct this real value would regress direct term mode.

| Rule | Status/reason |
|---|---|
| 1.1 by exact | n/a: no tactic wrapper |
| 1.2 by rfl | n/a: no proof |
| 1.3 rw+exact | n/a: no tactics |
| 1.4 simp+exact | n/a: no tactics |
| 1.5 trailing rfl | n/a: no tactics |
| 1.6 constructor | n/a: no proposition/structure construction |
| 1.7 apply+exact | n/a: no tactics |
| 1.8 by_contra | n/a: data construction |
| 1.9 eta reduction | n/a: no lambda |
| 1.10 single-use have | n/a: no have |
| 1.11 apply+intro | n/a: no tactics |
| 1.12 redundant show | n/a: no show |
| 1.13 obtain | n/a: no paired proof |
| 1.14 merge rw | n/a: no rewrites |
| 1.15 terminal simp | n/a: no simp |
| 1.16 nonterminal simp | n/a: no simp |
| 1.17 dot notation | already `l.factorial`; remaining operations are standard infix |
| 1.18 trailing parentheses | n/a: parentheses specify arithmetic grouping |
| 1.19 push Not | n/a: no negation tactic |
| 1.20 existential inlining | n/a: named arithmetic constant |
| 2.1 grind | n/a: no proposition/proof block; direct real data term |
| 2.2 delete pre-grind | n/a: no grind |
| 2.3 simpa | n/a: no closing proof |
| 2.4 fun_prop | n/a: no function property |
| 2.5 positivity | n/a: no positivity goal |
| 2.6 gcongr | n/a: no inequality goal |
| 2.7 lia/omega | n/a: no arithmetic proposition |
| 2.8 aesop | n/a: no proof search goal |
| 2.9 norm_num/cast | n/a: symbolic data term; norm_num used only in binder sensitivity probes |
| 2.10 decide | n/a: not decidable proposition |
| 2.11 field_simp/ring | n/a: definition construction, no equality/denominator |
| 2.12 linear_combination | n/a: no hypotheses or ring proof |
| 2.13 wlog | n/a: no cases |
| 2.14 calc term mode | n/a: already term mode |
| 2.15 multiple goals | n/a: no goals |
| 3.1 erw/rw | n/a: neither |
| 3.2 fun_prop | n/a: neither continuity nor measurability |
| 3.3 omega/lia | n/a: neither |
| 3.4 rcases rfl | n/a: neither |
| 3.5 automation registration | no new lemma/normal form warranting an attribute |
| 3.6 simp_all | n/a: no simp_all |
| 3.7 limits | no raised options |

Step-back reflection: the formula is already one direct arithmetic term with the paper's factor order; no tactics, single-use subterms, or proof skeletons to shorten. Preserve the named public definition and domain. No replacement was identified; do not churn the API.

## Independent original and actual built verification

Worker command `/Users/ramin/.elan/bin/lake build Roth.Theta` exit 0, 2423 jobs (`module.log`). No source edits preceded it. Scratch `positive.lean` re-elaborates the original definition text extracted by read-only git show from immutable original into namespace ImmutableOriginal21, independently of the current constant, and checks both the unapplied functions by rfl and the explicit original formula by rfl. It additionally compares exact original/current type AST and definitional equality of their values. Both actual built/current and independent original report only `[propext, Classical.choice, Quot.sound]`.

Initial raw value-AST structural equality reported `values differ`; this was an overly strict representation check despite both rfl equalities passing. It was corrected to definitional equality of the two independently elaborated values; only the fresh exit-0 `positive-final.log` certifies this gate. Initial failed `positive.log` remains available as honest exploration history. Declaration and documentation text separately compare byte-identical against immutable original. No self-theorem proof substitutes for independent construction.

Fresh complete unfiltered native live Theta diagnostics: `/private/tmp/roth-theta-lem6M/final-lsp.json`, success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors, 17 pre-existing warnings, none at lem6M. Source hash matches inherited baseline. No callers changed; complete module build checks existing call contracts. No new identifiers introduced in production.

## Simplify pass

PASS-THROUGH by direct holistic review (built-in Skill invocation tool unavailable): one expression, no duplicated proof skeleton or unjustified abstraction. Files modified: this report only.

## Buzz and freeze

FAST-BOARD: exact-prefix real command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-lem6M/prefix.lean` exited 0 twice. All normal module/probe/native-LSP requests had completed before profiling; owner confirmed no competing compiler requests. OS `ps` inspection was denied by the sandbox, so drain evidence is completed owned tool sessions plus owner coordination, not a process-list claim.

| Sample | Total target ms | Status |
|---|---:|---|
| Fresh unchanged baseline | 41.686 | below 1000 ms |
| Fresh final | 37.516 | below 1000 ms |

Raw UTF-8 logs: `profile-baseline.log`, `profile-final.log`; exact outer-command/async anchors and sums: `profile-anchors.txt` in `/private/tmp/roth-theta-lem6M/`. Each total counts the outer Elab.command plus separate associated Elab.async kernel/declaration/linter tasks; nested child timings are excluded to avoid double counting. The target command is anchored by its preserved docstring and `Roth.lem6M` header/value/actual declaration names. Prefix consists of exact current source through lem6M, then closes existing sections. Prefix SHA256 `3c73faff275bfc1d45ddf1601d2b51d434a04666c6ea4dc965c6ec837021998a`. This is target prefix-only performance evidence, not a whole-file profile claim. A second sample was already started before owner clarified one unchanged-source sample sufficed; no third sample run.

Limits raised: 0; scaffolding in production: 0; slow targets/decomposition deferrals: none. Source edits frozen (none made), all owned tool sessions drained. Final Theta SHA256 remains `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| module build | pass | `lake build Roth.Theta`, exit 0, module.log |
| fresh complete live LSP | pass | final-lsp.json, flags recorded above |
| definition type/value protected | pass | immutable byte comparison, exact type AST, independent value defeq/rfl |
| actual built axioms | pass | positive-final.log, standard three only |
| theorem statements/callers | pass | no edits; complete module build |
| structure | pass | 1 body line; no branches/conjunction |
| naming | pass | lowerCamelCase named paper M, no forbidden pattern |
| packing | pass | complete measured signature table |
| inequality orientation | pass | complete zero-occurrence table |
| final target performance | pass | fresh final real prefix measurement above, exit 0 |
| owner full build + LeanEval + publication | pending owner | not run or claimed by worker |

Production line delta: 2 → 2, 0. New helpers: 0. Renames queued: none; shared queue/log/Git not modified.

## Eleven-step checklist

- [x] Step 1: required references read.
- [x] Step 2: all 24 audit items addressed.
- [x] Step 2.5: five actual search methods and limitations recorded.
- [x] Step 2.6: all effective binders probed; generalisation/literature/inversion recorded.
- [x] Step 2.7: measured complete signature packing table.
- [x] Step 2.8: complete inequality occurrence table.
- [x] Step 3: all 42 golf rules assessed.
- [x] Step 4: holistic alternative-strategy reflection.
- [x] Step 5a: fresh complete unfiltered diagnostics succeed.
- [x] Step 5b: module/protection/axiom/content gates recorded; owner cumulative gates explicitly pending.
- [x] Step 6a: no rename needed; no shared queue mutation.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (5.980 s),
then separate `lake build Roth.LeanEval` (3.018 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`.
Raw logs: `/private/tmp/roth-theta-d21-full.log`, `/private/tmp/roth-theta-d21-leaneval.log`; machine record
`/private/tmp/roth-theta-d21-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 21/35, overall 202/264 original
declarations, 9/14 completed files. No new production helper; the previously added helper remains separately audited.
