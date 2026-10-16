# Declaration cleanup: `MvPolynomial.taylor_X`

Baseline: `8c39c00`, `Roth/Taylor.lean:45–46`. Scope: this declaration and this report.
Change: replace `by simp [taylor]` with the direct mathlib term `aeval_X _ _`.
Two declaration lines become one; signature, public visibility, simp attribute and docstring remain unchanged.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, together with the worker
contract, lean4 and mathlib-quality skills, mathlib-quality-principles.md,
naming-conventions.md and relevant style-rules.md sections on declarations,
formatting, documentation, visibility, imports, normal forms and API transparency.

## Full audit

1. **LINT:** no target warning; complete LSP reports only the user-preserved header warning at L1:2.
2. **HAVE SCAN:** none; original proof has only one terminal simp.
3. **SET_OPTION:** none in source or diff.
4. **SIMP SQUEEZE:** original `simp [taylor]` is terminal and correctly unsqueezed; replaced by a direct term, not squeezed.
5. **NAMING:** `taylor_X` describes the translation on the named generator `X`, in the correct subject namespace. Theorem naming preserves the embedded constant's capital X; no forbidden abbreviation, numerical scheme, single-letter name, `_auxN`, `_ge_`, or `_gt_` pattern. No rename required.
6. **LINE PACKING:** one complete signature line, measured below; no possible inter-signature repacking remains.
7. **BY PLACEMENT:** original `by` is at line end; final proof is a term, so no `by` remains.
8. **FORMAT:** final one-line term is 84 codepoints; no empty internal lines, tactical sequencing, haveI/letI or unnecessary indentation.
9. **COMMENTS:** no proof comments; existing docstring preserved byte-for-byte.
10. **DOCSTRING:** present and describes the generator image; simple result needs no further application caveats.
11. **VISIBILITY:** public simp API for the retained public translation definition; preserve the user's current public API. Explicit local use exists in `coeff_taylor`, and the simp attribute also supports automation.
12. **STRUCTURE:** one proof term, no conjunction or branches, below every decomposition threshold.
13. **MATHLIB:** direct `MvPolynomial.aeval_X` reused; five-method evidence below. Keep the user-required public translation simp rule.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: equality conclusion, no existential witness.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: none.
18. **GENERALISE:** all five elaborated parameters assessed below; no contract change.
19. **INEQUALITY:** zero inequalities; explicit table below.
20. **NORMAL-FORM:** existing simp orientation eliminates translation on a variable and yields `X j + C (α j)`; unchanged.
21. **SYNTAX-GEN:** OK: explicit vector and variable arguments support rewriting directly. Generic evaluation already exists as `aeval_X`; no additional API needed.
22. **IMPORT-FANOUT:** n/a: no new imports.
23. **CASTS:** 0 dropped / 0 kept as cross-type / 0 kept as load-bearing; diff contains no explicit coercion or ascription.
24. **INSTANCE-NAME:** n/a: no instance declaration.

Issues found: one proof simplification opportunity; fixed using the existing evaluation theorem.
Refactoring needed: none. Deleting this public simp rule would conflict with the instructed API preservation.

## Mathlib search status

| Method | Query / evidence | Result |
|---|---|---|
| A Lean-Finder | evaluation of multivariate polynomial at variable X gives substituted value | `MvPolynomial.eval₂_X`, `eval_X`, `aeval_X_left_apply` |
| B Loogle | `MvPolynomial.aeval, MvPolynomial.X` | `aeval_X`, `aeval_X_left`, `aeval_unique`, `aeval_X_left_apply`, `aeval_sumElim` |
| C LeanSearch | evaluation of the multivariate generator | unavailable: established HTTP 500 service failure, explicitly instructed not to retry; no absence inference |
| D Source | untruncated `taylor_X` across mathlib and Roth; `theorem aeval_X`, `def aeval` in MvPolynomial/Eval.lean | direct `aeval_X` at Eval.lean:587; univariate `Polynomial.taylor_X` analogue; project declaration and its explicit local use |
| E Local names | `aeval_X`, limit 8 | positive source matches including `MvPolynomial.aeval_X`; index unavailable, so no negative inference |

Auxiliary variants considered: `eval₂_X`, `eval_X`, `aeval_X_left`, `aeval_X_left_apply`,
`aeval_unique`. Common-equivalents table: no discrete/finite/separation match.
Conclusion: generic evaluation is a direct reusable building block. The final proof
uses it without unfolding tactics. The project's public simp rule is preserved per
user instruction; no new wrapper or abstract companion is added. Both native
`#check @aeval_X` and an isolated direct proof confirmed the actual signature.
`exact?`/`apply?` were tried live and reached default heartbeat limits; this is not
an absence claim, since positive mathlib evidence already suffices.

## Generalisation status

| # | Parameter | Class | Use | Mechanical candidates | Verification and result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | domain of α and type of j/X | drop; universe weakening | already universe-polymorphic; drop with autoImplicit false leaves unknown σ; retain |
| 2 | `{R : Type*}` | type variable | coefficient type and α codomain | drop; universe weakening | already independent universe; drop leaves unknown R; retain |
| 3 | `[CommSemiring R]` | typeclass | required by taylor, X, C and aeval | drop; weaken to Semiring | both fail synthesis of CommSemiring R; retain |
| 4 | `(α : σ → R)` | structure value | vector supplied to taylor and α j | drop | missing α with autoImplicit false; arbitrary vector already, no pointwise/strict weakening applies |
| 5 | `(j : σ)` | structure value | variable index and α j | drop | missing j with autoImplicit false; arbitrary index already, no decidability/finiteness constraint |

No proposition hypotheses, order assumptions, concrete scalar field, bundled
bijectivity, topology or decidability assumption to weaken. Tested candidates are
scratch-only; rejected weakenings never reached production source.
Inversion check: the abstract generator-evaluation fact is already exactly
`MvPolynomial.aeval_X`; reuse that existing fact. No new abstract result is warranted.
Big-change candidates: none consistent with the user's retained current API.

## Literature search status

[A] Web search query: `polynomial ring universal property evaluation indeterminate
commutative semiring generalization`. Top three returned hits were ProofWiki's
[one-variable polynomial ring](https://proofwiki.org/wiki/Definition%3APolynomial_Ring_in_one_Indeterminate),
[polynomial ring](https://proofwiki.org/wiki/Definition%3APolynomial_Ring), and
[University of Miami algebra notes, §18.1](https://www.math.miami.edu/~armstrong/562sp24/562sp24textbook.pdf).
The primary lecture-note result describes evaluation through the universal property;
this supports the interpretation of the theorem as the specified generator image.
The actual semiring generality and implementation choice are verified by mathlib's
compiled `aeval_X` signature. No additional hypothesis weakening follows from these hits.
[B] ChatGPT math MCP: n/a, no corresponding tool is available in this session.
Literature-driven big changes: none.

## Line packing

Width reference (`format.width = 100`):

```lean
@taylor_X : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (j : σ),
  (taylor α) (X j) = X j + C (α j)
```

| Version / sig line | Chars through `:=` | Entire physical line | Next signature token | Arithmetic | Action |
|---|---:|---:|---|---|---|
| Before L45 | 72 | 75 | none; proof body next | n/a; final signature line | ok |
| After L45 | 72 | 84 | none; term on same line | n/a; final signature line | ok |

Widths measured with Python `len`, counting Unicode codepoints, not bytes.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | signature and all parameters | n/a: no ≥ or > occurrence | none | none; no `_ge_`/`_gt_` in name |

## Golfing rule pass

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | direct term chosen after `exact aeval_X _ _` succeeded; no wrapper retained |
| 1.2 by rfl | tried rfl; not definitionally equal |
| 1.3 rw + exact | n/a: no rewrite sequence |
| 1.4 simp + exact | n/a: original simp already terminal |
| 1.5 trailing rfl | n/a: none |
| 1.6 anonymous constructor | n/a: equality, no constructor sequence |
| 1.7 apply + exact | n/a: no sequence; direct theorem term used |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 eta reduction | n/a: no lambda in target proof |
| 1.10 inline have | n/a: none |
| 1.11 apply + intro | n/a: none |
| 1.12 redundant show | n/a: none |
| 1.13 obtain projections | n/a: none |
| 1.14 merge rw | n/a: no rw |
| 1.15 unsqueeze terminal simp | original terminal simp unsqueezed; replaced by term |
| 1.16 squeeze nonterminal simp | n/a: no nonterminal simp |
| 1.17 dot notation | n/a: aeval_X takes function and index, no useful receiver notation |
| 1.18 avoid parentheses | n/a: no parenthesized proof argument |
| 1.19 push Not | n/a: no push_neg |
| 1.20 inline existential lemma | n/a: no existential helper |
| 2.1 grind | tested live; failed to close the translation equation |
| 2.2 delete before grind | n/a: no production grind |
| 2.3 simpa consolidation | n/a: no simp-plus-closing sequence; direct term avoids simplification |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | n/a: no sign/nonzero goal |
| 2.6 gcongr | n/a: no inequality |
| 2.7 lia/omega | n/a: no integer/natural arithmetic goal |
| 2.8 aesop | tested live; failed, no progress |
| 2.9 norm_num/norm_cast | n/a: no numerals or casts |
| 2.10 decide/kernel | n/a: symbolic equality over arbitrary commutative semiring, no decidable computation |
| 2.11 field_simp/ring | n/a: no denominators, no field; equation requires evaluation API |
| 2.12 linear_combination | n/a: no ring ending or algebraic equality hypotheses |
| 2.13 wlog | n/a: no symmetric cases |
| 2.14 collapse calc | n/a: none |
| 2.15 close multiple goals | n/a: a single equation |
| 3.1 erw→rw | n/a: no erw |
| 3.2 fun_prop upgrade | n/a: no continuity/measurability tactics |
| 3.3 omega→lia | n/a: no omega |
| 3.4 rcases rfl | n/a: no case decomposition |
| 3.5 automation registration | existing simp attribute retained; no additional registration needed |
| 3.6 simp_all | n/a: no simp_all only or useful extra hypotheses |
| 3.7 remove limits | n/a: no per-declaration limits; failed search limits were not raised |

## Step back and think

The original proof is already one tactic. Bare simp made no progress, and rfl,
grind and aesop failed in the live pre-declaration goal. The direct existing
mathlib theorem succeeds and expresses precisely the reason for the equation.
The replacement was also checked in an isolated snippet importing only Roth.Box
and Roth.HasseDeriv, defining a fresh translation and proving its generator
identity before any equivalent local theorem was present. This excludes circular
simp reuse. The original `[taylor]` argument was necessary for that simp strategy;
it becomes unnecessary when the proof is a direct theorem application.

## Verification and gates

- Actual `lake build Roth.Taylor`: exit 0, 1439 jobs, target 14s;
  `/private/tmp/roth-taylor-X-module.log`.
- Complete native `lean_diagnostic_messages`: success true, partial false,
  timed_out false, no failed dependencies; sole header warning at L1:2.
- Isolated direct proof: native `lean_run_code` success true, timed_out false;
  `probe_X` has only propext, Classical.choice, Quot.sound. One scratch long-line
  warning on the temporary definition has no production counterpart.
- Final compiled declaration's contract and axiom check: see completion record below.
- Native final import-based scratch reported stale imports despite the completed
  build; CLI fallback checks the built module directly. This was not counted as
  a successful check.

| Gate | Result | Details |
|---|---|---|
| lake_build_file | pass | actual module command exit 0 |
| definition_protected | pass | no definition or abbrev changed |
| theorem_statement_protected | pass | signature through `:=` byte-identical; only proof changed |
| structure_gate | pass | one term; no conjunction or branch |
| naming_gate | pass | descriptive operation/generator name; no forbidden pattern |
| line_packing_gate | pass | complete measured one-line table, width 84 |
| inequality_orientation_gate | pass | explicit zero-occurrence scan; no reversed inequality |
| comments/docstring/attributes | pass | all preserved |

Overall: pass. Actual final CLI completion is recorded below.
No rename queued. No decomposition, API replacement, or generalisation pending.
Full dependent-project builds belong to the parent file worker.

## Result and phase checklist

Before: 2 lines. After: 1 line. Saved: 1 line.
Audit issues found: 1 proof simplification; fixed: 1. Refactoring deferred: 0.
Applied: direct mathlib reuse, term-mode proof (1.1/Step 4).
Comments preserved: no inline comments; original docstring unchanged.
Source frozen after the final edit at SHA256
`79a3459730c972e438301e511ded297cad4e10edcef816302ad1dc21cfbb5ad1`.
No source edits after freeze; report-only ownership thereafter.

- [x] Step 1 — references read.
- [x] Step 2 — all 24 audit items answered.
- [x] Step 2.5 — five-method search status recorded.
- [x] Step 2.6 — every parameter, weakening and literature status recorded.
- [x] Step 2.7 — per-signature width table measured.
- [x] Step 2.8 — inequality occurrence scan recorded.
- [x] Step 3 — all 42 golfing rules have explicit status.
- [x] Step 4 — automation/direct-term alternatives considered and tested.
- [x] Step 5a — complete LSP clean except user-preserved header warning.
- [x] Step 5b — actual module build and all diff gates recorded.
- [x] Step 6a — no rename required; sidecar unchanged.

## Final CLI completion record

`lake env lean /private/tmp/roth-taylor-X-contract.lean` exited 0. The final
`#check` output is the width reference above. Explicit application to the exact
original statement compiled. `#print axioms MvPolynomial.taylor_X` returned
`[propext, Classical.choice, Quot.sound]` only.

`lake env lean /private/tmp/roth-taylor-X-weaken.lean` exited 1 as expected for
negative probes: L6 (Semiring) and L10 (dropped instance) fail CommSemiring
synthesis; L14/L15 report unknown α/j; L19/L23 report unknown σ/R. No proposed
weakening passed. Temporary error-recovery terms in the failed scratch output
are not source axioms or proofs and were never copied into the repository.
