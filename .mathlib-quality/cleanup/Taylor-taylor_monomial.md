# Cleanup: `MvPolynomial.taylor_monomial`

Baseline: `49abee2`; file `Roth/Taylor.lean`, worker lines 53–55 (original inventory 55–57). Scope: target declaration and this report only. Existing public API and documentation preserved; no Git operations.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Also read both skills, the full supplied worker contract, applicable style sections, and the documentation, normal-form, and syntactic-generality review sections. The conditional naming reference was not required: no naming issue in the punch list or audit.

## Result

Before: 3 declaration lines, one tactic. After: 3 declaration lines, one direct proof term. Saved: 0 lines; removed the simplifier and its unfolding/rewrite list. The proof is now `aeval_monomial _ _ _`, and the ordinary lambda uses `↦`. Two improvements found and fixed. No outstanding refactoring, rename, or generalisation proposal. Public wrapper retained under the user's current-API instruction, which overrides the generic wrapper-deletion advice.

## Full audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No target warning/error. Complete final LSP reports only the user-preserved file-header warning at L1:2. |
| 2 | HAVE SCAN | n/a: no `have` bindings. |
| 3 | SET_OPTION | n/a: no declaration options or limit overrides. |
| 4 | SIMP SQUEEZE | Original L55 terminal `simp [taylor, aeval_monomial, algebraMap_eq]` needed no squeeze. Direct mathlib term replaces it entirely. |
| 5 | NAMING | `taylor_monomial` describes the image of a monomial under Taylor translation. Snake case, no forbidden abbreviation, numeric scheme, `_auxN`, `_ge_`, `_gt_`, or single-letter public name. No rename warranted. |
| 6 | LINE PACKING | Two signature lines, fully measured below. The complete conclusion does not fit after the binders. |
| 7 | BY PLACEMENT | Original `by` ended the signature; term mode removes it. |
| 8 | FORMAT | Changed the ordinary lambda `=>` to `↦`. Continuation indent 4, term indent 2, no internal blank line or tactic chain, no `haveI`/`letI`. |
| 9 | COMMENTS | No proof comments present. No comment deleted or relocated. |
| 10 | DOCSTRING | Existing two-line description and source locator preserved byte-for-byte. The quoted source passage locates the monomial stage of Taylor's theorem; it is not new proof commentary. |
| 11 | VISIBILITY | Existing public translation API retained under user direction, although current project use is in the same file at L224. |
| 12 | STRUCTURE | One-term body; no conjunction or branches. No extraction needed. |
| 13 | MATHLIB | Generic `MvPolynomial.aeval_monomial` found, checked and applied directly; five-method record below. |
| 14 | JUNK DEF | n/a: theorem, no definition. |
| 15 | EXISTS LEMMA | n/a: equality, no existential witness. |
| 16 | SHOW vs CHANGE | n/a: neither syntax occurs. |
| 17 | PUSH_NEG | n/a: absent. |
| 18 | GENERALISE | All six inherited/explicit parameters reviewed and drop-tested; semiring weakening also tested. No admissible weakening of the fixed Taylor API. |
| 19 | INEQUALITY | No inequality in signature or parameters; occurrence table below. |
| 20 | NORMAL-FORM | Canonical substitution formula: image of monomial equals mapped coefficient times product of translated variables raised to its exponents. Matches `aeval_monomial`. |
| 21 | SYNTAX-GEN | OK: equation directly rewrites the existing Taylor expansion call site. No bundled hypothesis or alternate statement would ease it. |
| 22 | IMPORT-FANOUT | n/a: no import changes. |
| 23 | CASTS | 0 dropped / 0 kept cross-type / 0 kept load-bearing. No explicit casts/ascriptions added or removed. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues fixed: use direct evaluation lemma; replace ordinary lambda arrow. Refactoring needed: none.

## Mathlib search status

| Method | Query/action | Result |
|---|---|---|
| A Lean-Finder | `evaluation of a multivariate polynomial monomial is coefficient times product of powers` | Found `MvPolynomial.eval_monomial`, `eval₂_monomial`, `aeval_monomial`, `eval₂Hom_monomial`, `eval₂_mul_monomial`. |
| B Loogle | `MvPolynomial.aeval, MvPolynomial.monomial` | Found `MvPolynomial.aeval_monomial` with the exact general algebra-evaluation formula. |
| C LeanSearch | No repeated call | Unavailable: parent's established HTTP 500 in this cleanup session; explicitly instructed not to retry. No absence inference. |
| D Source | Untruncated `rg` for `aeval_monomial`, `eval₂_monomial`, `eval_monomial`, `algebraMap_eq` in MvPolynomial/Eval; `taylor_monomial` across project/mathlib | `Eval.lean:681` states `aeval_monomial`; source read. Other variants at 92, 267, and generic hom version. Univariate `Polynomial.taylor_monomial` is a different namespace/type. Project use at Taylor L224. |
| E Name pattern | Native `lean_local_search` for `aeval_monomial` | Found MvPolynomial and Polynomial source declarations; index reported unavailable. Positive hits verified by `#check` and compilation, not interpreted as absence evidence. |

Auxiliary variants checked: `eval_monomial`, `eval₂_monomial`, `eval₂Hom_monomial`, and `algebraMap_eq`. Common-equivalents table: none of its discrete/finiteness/separation/boundedness buckets applies. The abstract result exists and is used directly. No custom predicate, new wrapper, new import, absence claim, or module-docstring mutation. The user explicitly wants the current public API preserved, so removing the existing project theorem is not an outstanding task.

## Generalisation status

Mechanical drop and weakening probes used native `lean_run_code`, `autoImplicit false`, and scratch examples importing `Roth.Taylor`. They never altered live source. These intentionally failing probes test whether the original signature remains meaningful; their diagnostics are negative evidence, not shipped errors.

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | Index type of translation and exponent vector | Drop; universe widening reviewed | yes (drop) | Unknown identifier `σ`; already universe-polymorphic, no restriction to remove. |
| 2 | `{R : Type*}` | type variable | Coefficient type | Drop; universe widening reviewed | yes (drop) | Unknown identifier `R`; independent universe already allowed. |
| 3 | `[CommSemiring R]` | typeclass | Types of `taylor`, `monomial`, `C`, product | Drop; weaken to `[Semiring R]` | yes | Both fail synthesis of `CommSemiring R` in the statement. Retain. |
| 4 | `(α : σ → R)` | structure value | Translation on both sides | Drop | yes | Unknown identifier `α` (and consequential default-heartbeat timeout on proof elaboration). Arbitrary function already allowed; no pointwise property to localise. |
| 5 | `(k : σ →₀ ℕ)` | structure value | Monomial exponent and finite product index | Drop | yes | Unknown identifier `k` / `k.prod`; its natural exponents are the polynomial monomial structure, not an extraneous arithmetic restriction. |
| 6 | `(a : R)` | structure value | Coefficient on both sides | Drop | yes | Unknown identifier `a`; arbitrary coefficient, no sign/nonzero condition to weaken. |

No proposition or decidability binders. No strict-to-weak, analysis, topology, or bundled-predicate candidate applies. No small-safe weakening retained; no big-change proposal warranted.

Mandatory inversion check: after unfolding translation, the proof is the generic algebra-evaluation formula for a monomial. That abstraction already exists as `aeval_monomial`, over arbitrary commutative semiring algebras and variable assignment. The final proof uses it directly, so a new abstract companion would duplicate mathlib.

## Public literature search

Query 1: `multivariate polynomial monomial substitution commutative semiring generalization`. First three returned hits were [MvPolynomial.CommRing (IISc 2025 mirror)](https://math.iisc.ac.in/~gadgil/PfsProgs25doc/Mathlib/Algebra/MvPolynomial/CommRing.html), [Data.MvPolynomial.CommRing (IISc 2023 mirror)](https://math.iisc.ac.in/~gadgil/proofs-and-programs-2023/doc/Mathlib/Data/MvPolynomial/CommRing.html), and [RingTheory.MvPolynomial.Basic (IISc 2023 mirror)](https://math.iisc.ac.in/~gadgil/proofs-and-programs-2023/doc/Mathlib/RingTheory/MvPolynomial/Basic.html). Recorded as discovery results, not relied on for toolchain-specific claims.

Query 2: `polynomial ring universal property substitution monomial site:stacks.math.columbia.edu`. First three returned hits were [Artin's axioms](https://stacks.math.columbia.edu/download/artin.pdf), [Lemma 54.2.1](https://stacks.math.columbia.edu/tag/0ADZ), and [Lemma 10.149.1](https://stacks.math.columbia.edu/tag/04EB). These are applications of substitution/universal algebra maps; none supplies a missing generalisation for this elementary formula.

Opened the primary [mathlib evaluation documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Eval.html). Its algebra-evaluation monomial formula agrees with the pinned local source and checked type. Generality already permits arbitrary commutative semirings, arbitrary variable types and arbitrary algebra evaluation maps; no characteristic, finiteness or field hypothesis is needed. The direct term specialises this existing result. ChatGPT math MCP: n/a, no callable mathematical-second-opinion tool found in tool metadata. Literature-driven big-change candidates: none.

## Line packing

`#check @taylor_monomial` at `format.width 100`, from a source-prefix isolation probe:

```lean
@taylor_monomial : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (k : σ →₀ ℕ) (a : R),
  (taylor α) ((monomial k) a) = C a * k.prod fun j n ↦ (X j + C (α j)) ^ n
```

Widths measured using Python `len` on source Unicode strings, hence codepoints, not bytes. The next syntactic signature unit after the binder line is the conclusion, as in the contract's conclusion-packing example.

| State / signature line | Codepoints | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| Before L53 | 58 | Complete conclusion through `:= by`: 75 without indent | 58 + 1 + 75 = 134 > 100 | ok |
| Before L54 | 79 | none; tactic body next | n/a; 79 ≤ 100 | ok |
| After L53 | 58 | Complete conclusion through `:=`: 71 without indent | 58 + 1 + 71 = 130 > 100 | ok |
| After L54 | 75 | none; proof term next | n/a; 75 ≤ 100 | ok |

Both final signature lines covered; no repack row remains. The term line is 22 codepoints.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | Complete signature and inherited parameters | No `≥`/`>` inequalities, nor `<`/`≤` | n/a | none; no `_ge_` or `_gt_` in name |

The original ASCII lambda `=>` was syntax, not a greater-than comparison; now replaced by `↦`.

## Golfing rule pass

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | Applied term-mode endpoint after successful `exact aeval_monomial _ _ _` live and isolated probes. |
| 1.2 by rfl | n/a: no `by rfl` wrapper; formula is supplied by the generic evaluation theorem. |
| 1.3 rw + exact | n/a: no rewrite chain. |
| 1.4 simp + exact | n/a: original simp already terminal. |
| 1.5 trailing rfl | n/a: no trailing tactic. |
| 1.6 constructor chain | n/a: no constructor chain. |
| 1.7 apply + exact | n/a: no apply chain. |
| 1.8 by_contra + push_neg | n/a: no contradiction proof. |
| 1.9 eta-reduce lambdas | n/a: translated power depends nontrivially on both binders; ordinary lambda arrow changed separately. |
| 1.10 inline single-use have | n/a: no `have`. |
| 1.11 apply + intro | n/a: no introductions/applications. |
| 1.12 redundant show | n/a: no `show`. |
| 1.13 have projections | n/a: no conjunction binding. |
| 1.14 merge consecutive rw | n/a: no `rw`. |
| 1.15 unsqueeze terminal simp only | n/a: original terminal simp was unsqueezed. Direct term removes it. |
| 1.16 squeeze nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | n/a: three explicit arguments to namespace evaluation lemma, no natural receiver shortening. |
| 1.18 use `<|` | n/a: no removable trailing parentheses. |
| 1.19 push_neg | n/a: absent. |
| 1.20 inline existential lemma | n/a: no existential/helper declaration. |
| 2.1 grind whole proof | Tried live; failed to prove contradiction of the desired equality. |
| 2.2 delete tactics before grind | n/a: no existing grind. |
| 2.3 simpa consolidation | n/a: original proof was one terminal simp, no following fact to consolidate; direct term is simpler. |
| 2.4 fun_prop | n/a: no analytic/function-property goal. |
| 2.5 positivity | n/a: no positivity/nonzero goal. |
| 2.6 gcongr | n/a: no ordered congruence. |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic proposition. |
| 2.8 aesop | Tried live; failed with no progress. |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric computation or cast equality. |
| 2.10 decide/kernel | n/a: arbitrary symbolic polynomial equality, no finite decision problem. |
| 2.11 field_simp/ring | n/a: no denominators, coefficient structure only CommSemiring, and evaluation must first be exposed. |
| 2.12 linear_combination | n/a: no ring-ending proof and no equality hypotheses. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc to term | n/a: no calc. Direct term chosen independently. |
| 2.15 close multiple goals | n/a: single goal. |
| 3.1 erw to rw | n/a: no `erw`. |
| 3.2 continuity/measurability | n/a: no legacy analytic tactic. |
| 3.3 omega to lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no case split. |
| 3.5 automation attributes | Reviewed: preserve current attribute set; expanding every monomial translation globally is unnecessary for the explicit rewrite caller. |
| 3.6 simp_all | n/a: no `simp_all only` or proof hypotheses. |
| 3.7 remove limits | n/a: no source limit overrides. |

## Step back and experiments

Native `lean_multi_attempt` at original L55 completed all seven attempts: direct `exact aeval_monomial _ _ _` succeeds; `simp [taylor]` and `simp [taylor, algebraMap_eq]` leave the evaluation equation (the latter also reports an unused argument); bare `grind` and `aesop` fail; `exact?` and `apply?` reach the unchanged default 200000-heartbeat limit. No limits raised. A bounded direct-MCP duplicate probe was started while the native call was slow; it timed out without adding evidence and did not modify source. The native result subsequently completed and is the recorded evidence.

The existing proof was already one tactic; the useful improvement is replacing that tactic with the known generic theorem. No have blocks or redundant proof steps remain, and no alternate structural strategy is needed. An independent scratch definition with only Box/Hasse imports first confirmed the direct term, its fully general type, and standard axioms. A second probe used the exact live source prefix through L55, then checked the theorem type, printed its axioms, and applied it to the original statement using the original ASCII lambda. This excludes circular reliance on the target or later declarations and establishes that the syntax change preserves the original type.

## Gate status — Phase 4

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | `/Users/ramin/.elan/bin/lake build Roth.Taylor`, session 92571 exit 0; 1439 jobs, Taylor target 7.8s. Log `/private/tmp/roth-taylor-monomial-build.log`. |
| definition_protected | ✓ pass | No def/abbrev/import change. |
| theorem_statement_protected | ✓ pass | Name, binders, visibility, conclusion preserved; lambda glyph and proof-boundary syntax only. Original-type application independently compiled. |
| structure_gate | ✓ pass | One-term body, no conjunction/branch. |
| naming_gate | ✓ pass | Descriptive `taylor_monomial`, no forbidden pattern or abbreviation. |
| line_packing_gate | ✓ pass | All signature lines measured above; natural conclusion unit does not fit binder line. |
| inequality_orientation_gate | ✓ pass | Zero reversed inequalities; scan above. |
| complete LSP | ✓ pass | Native diagnostics: success=true, partial=false, timed_out=false, failed_dependencies=[]; only user-preserved header L1:2. |
| isolated pre-target proof | ✓ pass | Exact source prefix through target, importing only Roth.Box and Roth.HasseDeriv, compiled with success=true/timed_out=false. |
| type and axioms | ✓ pass | Original-type example compiles; only `propext`, `Classical.choice`, `Quot.sound`. |
| comments/docs | ✓ pass | Existing docstring byte-identical; no proof comments existed. |

Overall: pass. Full dependent build and separate LeanEval build belong to the parent checkpoint, not claimed by this worker.

SOURCE FROZEN: SHA256 `a913c9258bdcb0630d0d3398f34626f52c2d9f9504a7077e443ef2f24f1090a4` for `Roth/Taylor.lean`. Source ownership relinquished; report-only work thereafter.

## Phase checklist

- [✓] Step 1 — mandatory references and relevant style/review sections read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five-method search, variants, strict-rule disposition and common-equivalents status.
- [✓] Step 2.6 — every parameter, actual drop/weakening probes, inversion check and public literature search.
- [✓] Step 2.7 — complete before/after signature-width table.
- [✓] Step 2.8 — inequality occurrence table.
- [✓] Step 3 — all 42 golfing rules given concrete status.
- [✓] Step 4 — direct term, smaller simp sets, automation and discovery tactics tested; reflection recorded.
- [✓] Step 5a — complete final LSP succeeds, only user-preserved header warning.
- [✓] Step 5b — all diff/module/isolation/type/axiom gates pass.
- [✓] Step 6a — no rename warranted; no queue mutation.
