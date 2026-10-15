# Phase 4 — `MvPolynomial.hasseDeriv_single_aeval_X`

Dedicated declaration worker, 2026-10-15. Scope: this declaration and this report only.
Source baseline: `/private/tmp/HasseDeriv-decl23-before.lean`; declaration initially
lines 250–259, finally 250–257. No Git operations or shared-log writes.

## References read

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read the installed lean4 and
mathlib-quality skills, the complete Phase-4 worker prompt, relevant style-rules
sections, naming-conventions.md, and mathlib-review-stages.md normal-form,
syntactic-generality, and documentation sections. Source §1 was read at
`.mathlib-quality/references/clean.tex:118–152`.

## Mathematics

Embed a univariate polynomial by sending its indeterminate to `X j`. Differentiating
that image with multi-index `n e_j` equals embedding its nth univariate Hasse
derivative. Additivity reduces the claim to monomials; both sides then have exponent
`(m - n) e_j` and coefficient `choose m n * a`. This is valid over arbitrary
commutative semirings, including positive characteristic.

## Full audit

1. **LINT:** no target warning. Complete-file diagnostics retain only the known
   line-1 copyright-header warning; no new suppression added.
2. **HAVE SCAN:** original L256 `hc` has a `by` proof and one use at L259, so mandatory
   no-proof alias inlining does not apply. Tested folding its binomial computation
   into terminal simp; successful, and `hc` is now removed.
3. **SET_OPTION:** none in the target; no limit changes.
4. **SIMP SQUEEZE:** original additive branch and monomial branch end in `simp only`.
   Both now use terminal ordinary `simp`; original local hc simp is absorbed.
5. **NAMING:** `hasseDeriv_single_aeval_X` describes the operator, index shape, and
   evaluated expression using existing API names. No forbidden abbreviation,
   numeric scheme, `_ge_`, `_gt_`, or single-letter public name. No rename warranted.
6. **LINE PACKING:** all three signature lines measured below; unchanged.
7. **BY PLACEMENT:** `:= by` ends the final signature line.
8. **FORMAT:** two-space proof indent, no blank body lines, no tactic semicolon
   chains, no consecutive rewrites, no `haveI` or `letI` introduced.
9. **COMMENTS:** no proof comments existed; public docstring and source citation preserved.
10. **DOCSTRING:** existing public description explains the single-variable
    restriction and contrasts it with the following equivalence theorem; preserved.
11. **VISIBILITY:** public main result and used externally in `Roth/Separation.lean:222`;
    retain public API.
12. **STRUCTURE:** body shrinks 7→5 lines, below the 15-line main-result threshold;
    no conjunction; longest branch is three lines. No helper extraction necessary.
13. **MATHLIB:** five-method search below; keep the local compatibility theorem,
    building on existing polynomial monomial and evaluation APIs.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: no existential conclusion or witness helper.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: no negation-pushing tactic.
18. **GENERALISE:** six-parameter table and literature check below. No safe weakening.
19. **INEQUALITY:** zero occurrences; scan table below.
20. **NORMAL-FORM:** already an operator compatibility equation, reducing the
    multivariate derivative of an embedding to the univariate derivative on the RHS.
21. **SYNTAX-GEN:** OK: pointwise equality is directly usable by `rw`; replacing it
    with bundled linear-map equality would add coercion work at existing call sites.
22. **IMPORT-FANOUT:** n/a: no import added or removed.
23. **CASTS:** diff adds no ascriptions or coercions: 0 dropped / 0 cross-type / 0
    load-bearing added. Existing `MvPolynomial σ R` annotations fix evaluation's codomain.
24. **INSTANCE-NAME:** n/a: theorem introduces no instance declaration.

Issues fixed: two terminal simp squeezes and the removable local binomial calculation.
Refactoring needed: none. No substantial API change requiring a user decision was found.

## Mathlib search-status

| Method | Query / evidence | Result |
|---|---|---|
| A Lean-Finder | Hasse derivative multivariate polynomial evaluated at one variable agrees with univariate Hasse derivative | Found `Polynomial.hasseDeriv_apply`, `_one'`, `_mul`; partial matches only |
| B Loogle | `Polynomial.hasseDeriv, Polynomial.aeval` | Successful response, zero hits |
| C LeanSearch | n/a: parent reports persistent HTTP 500 for this service in this run | Known failed service deliberately not retried; other searches and compiled search used |
| D source grep | full `hasseDeriv_single_aeval_X` across Mathlib; `hasseDeriv.*aeval`, reverse form; `prod_single_index`, `single_tsub` | No full match; Finsupp index arithmetic and polynomial Hasse monomial API found |
| E local name search | `hasseDeriv` | Polynomial, LaurentSeries, and project APIs; only local theorem matches target; index unavailable, source results used, not an absence claim |

Auxiliary variants checked: `_map`, `_monomial`, `_apply`, `_comp`, `_single`,
and `aeval` combinations. Read the univariate HasseDeriv source and MvPolynomial
evaluation source hits. Common-equivalents lookup: no bucket matches.
Live `exact?` before the declaration failed to close the goal; `apply?` reached
the default 200000-heartbeat limit. Thus no generic one-step replacement was found.
No theorem was added on the strength of absence alone. The local definition of
the multivariate derivative requires this compatibility proof; this is not a
wrapper around an existing mathlib compatibility theorem.

## Generalisation status

| Parameter | Class | Used as | Candidates / evidence | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | type of j and multivariate indices | Already independent universe; dropping would leave j and MvPolynomial ill-typed; no stronger structure assumed | Keep |
| `{R : Type*}` | type variable | coefficient type of both polynomial types | Already independent universe; dropping leaves the semiring instance and f ill-typed | Keep |
| `[CommSemiring R]` | typeclass | MvPolynomial, hasseDeriv, and Polynomial.aeval | Isolated drop test fails Semiring/CommSemiring synthesis; isolated `[Semiring R]` test fails CommSemiring synthesis at both evaluation codomains | Keep; weakest available signature |
| `(j : σ)` | structure value | chosen variable and Finsupp.single | Isolated drop test with autoImplicit false reports unknown j | Keep; no point/global hypothesis to localise |
| `(n : ℕ)` | structure value | Hasse order and multi-index entry | Isolated drop test with autoImplicit false reports unknown n | Keep; ℕ is essential to binomial derivative order, not merely induction structure |
| `(f : Polynomial R)` | structure value | polynomial being differentiated | Isolated drop test with autoImplicit false reports unknown f | Keep; arbitrary polynomial already |

Tests used separate `lean_run_code` examples rather than temporarily breaking the
public file. No proposition, decidability assumption, strict inequality, bundled
bijectivity, or concrete coefficient field occurs. No parent-class weakening beyond
Semiring is viable once Semiring already fails to express the unchanged statement.
Inversion check: X is the defining generator of the embedding, and the monomial
argument uses X powers explicitly; an arbitrary substitution requires a chain rule
and changes the theorem rather than dropping a hidden restriction. No warranted
big-change candidate or new helper was found.

### Literature

Web query: “Hasse derivative multivariate polynomial single variable generalization
commutative ring”. Top three returned hits recorded: the JACM paper
*Fast Multivariate Multipoint Evaluation over All Finite Fields*
([publisher](https://doi.org/10.1145/3652025)); *Polynomial Identity Testing of
Read-Once* (Citeseer result); and the authors' PDF of the first paper. The author's
PDF fetch timed out; its [arXiv full text](https://arxiv.org/html/2205.00342v1#S3.SS2)
was read successfully. Definition 3.4 defines Hasse derivatives by coefficient
extraction over commutative rings; Lemma 3.7 discusses general curve substitutions.
Inference: restriction to a coordinate variable gives this theorem's compatibility,
while arbitrary substitutions require additional chain-rule expressions. The existing
semiring result already avoids the source's ring restriction.

The nLab search result describes commutative rigs; opening its page failed because
the web reader rejected XHTML. A secondary check of
[Moreno Maza's course notes](https://www.csd.uwo.ca/~mmorenom/AM583/Lectures/Newton2Hensel.html/node17.html)
confirmed that univariate-to-partial-derivative compatibility is standard over
commutative rings. Local source §1 explicitly permits commutative semirings.
ChatGPT math MCP: skipped as instructed. Literature-driven substantial changes: none.

## Measured line packing

`#check @MvPolynomial.hasseDeriv_single_aeval_X` with `format.width := 100`:

```text
@MvPolynomial.hasseDeriv_single_aeval_X : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (j : σ) (n : ℕ)
  (f : Polynomial R),
  (MvPolynomial.hasseDeriv (Finsupp.single j n)) ((Polynomial.aeval (MvPolynomial.X j)) f) =
    (Polynomial.aeval (MvPolynomial.X j)) ((Polynomial.hasseDeriv n) f)
```

Widths measured by Python `len`, counting Unicode codepoints. Next unit means the
complete mathematical application rather than a lone function identifier.

| Signature line | Chars | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 250 | 70 | `hasseDeriv (Finsupp.single j n)` (31) | 70 + 1 + 31 = 102 > 100 | ok |
| 251 | 83 | `Polynomial.aeval (X j : MvPolynomial σ R)` (41) | 83 + 1 + 41 = 125 > 100 | ok |
| 252 | 81 | no next signature line | n/a | ok |

Before and after signature bytes are identical, so this is also the final table.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | full signature and parameters | no ≥ or > | n/a | no `_ge_` or `_gt_` |

## Golfing rule pass — all 42 rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: no reflexivity proof |
| 1.3 rw + exact | n/a: no rewrite chain |
| 1.4 simp + exact | n/a: no trailing exact |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor | n/a: no product proposition |
| 1.7 apply + exact | n/a: none |
| 1.8 by_contra | n/a: no contradiction proof |
| 1.9 eta reduction | n/a: no lambda |
| 1.10 single-use have | Applied optional strengthening: hc has proof content but folds into terminal simp |
| 1.11 apply + intro | n/a: no such sequence |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: no projected conjunction |
| 1.14 merge rw | n/a: no rw |
| 1.15 unsqueeze terminal simp | Applied to both induction branches |
| 1.16 squeeze nonterminal simp | n/a: all final simp calls close goals |
| 1.17 dot notation | n/a: no dot-notation improvement |
| 1.18 trailing parentheses | n/a: no term application to tactic block |
| 1.19 push_neg | n/a: none |
| 1.20 existential helper | n/a: none |
| 2.1 grind whole proof | Tried live; fails the compatibility equality |
| 2.2 delete before grind | n/a: retained proof has no grind |
| 2.3 simpa consolidation | Considered; no supplied theorem closes the compatibility goal; direct terminal simp handles each branch |
| 2.4 fun_prop | n/a: no analytic function property |
| 2.5 positivity | n/a: no positivity goal |
| 2.6 gcongr | n/a: equality, no monotonicity |
| 2.7 lia / omega | n/a: no residual arithmetic goal |
| 2.8 aesop | Tried live; fails without polynomial induction |
| 2.9 norm_num / norm_cast | n/a: symbolic coefficient formula; no numeric computation goal |
| 2.10 decide | n/a: arbitrary symbolic polynomials over arbitrary semiring |
| 2.11 field_simp; ring | n/a: no division or ring arithmetic goal |
| 2.12 linear_combination | n/a: no ring-ending proof or arithmetic hypotheses |
| 2.13 wlog | n/a: additive and monomial branches are structurally different |
| 2.14 calc collapse | n/a: no calc |
| 2.15 shared <;> | n/a: branches need different simp arguments |
| 3.1 erw → rw | n/a: neither occurs |
| 3.2 legacy analytic tactics | n/a: none |
| 3.3 omega → lia | n/a: no arithmetic tactic |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation registration | Considered; no attribute change needed for two explicit rewrite consumers; preserving public normal forms |
| 3.6 simp_all | n/a: no simp_all only; induction hypotheses already supplied explicitly |
| 3.7 heartbeat option | n/a: none introduced or present |

## Actual alternatives and reflection

Live whole-proof probes `grind`, `simp`, `aesop`, `exact?` all fail;
`apply?` hits the default heartbeat limit. Line replacement leaves original
induction branches behind, so those attempts also report parser errors after the
probe; the tactic failures themselves occur at the probe position.

Tested the monomial branch with ordinary simp and progressively explicit monomial,
Finsupp, and multiplication lemmas. Without `-map_natCast`, simplification leaves
`monomial k (↑c * a) = ↑c * monomial k a`. Reversing or disabling `map_mul` does not
solve that issue. Disabling only `map_natCast` and using `mul_assoc` does close it.
Explicit `Polynomial.aeval_monomial` and `Finsupp.prod_single_index` were tested and
found unnecessary. A two-stage alternative (original restricted monomial
normalisation, then `simp [hasseCoeff, Finsupp.prod_single_index]`) also closed,
but was longer. The final independently compiled theorem avoids leftover source
artifacts and proves exactly the original statement.

Induction is mathematically direct and genuinely needed by the available API.
There is no beneficial term-mode conversion or missing reusable bridge helper:
this public theorem is itself the reusable bridge and its body is five lines.

## Verification and diff gates

`lean_run_code` compiled independently named `MvPolynomial.decl23_checked` with
the final proof (`success: true`, `timed_out: false`), checked it against an
explicit copy of the original full type, and printed exactly
`[propext, Classical.choice, Quot.sound]`. No use of the target theorem occurs
in that proof. An initial formatting probe mistakenly used `pp.width`; rerunning
with `format.width` corrected the diagnostic and passed.

New source identifiers: `map_natCast`, `mul_assoc`. Both verified by compiled
`#check`; local search for `map_natCast` returned related names with a warming
index, so that search was not used as the verification. All other identifiers
already occur in the baseline proof.

Final full-file `lean_diagnostic_messages`: `partial: false`, `success: true`,
`timed_out: false`; only known copyright-header warning. `lake build
Roth.HasseDeriv`, command session 1565, completed exit 0: 1430 jobs,
module compilation 9.2 seconds. No passed check was rerun absent a change or failure.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.HasseDeriv`, exit 0, 9.2s |
| definition_protected | pass | Snapshot diff changes only target proof lines |
| theorem_statement_protected | pass | Three signature lines and public documentation byte-identical |
| structure_gate | pass | Five-line main proof; no conjunction or long branch |
| naming_gate | pass | Mathematical name; no forbidden pattern |
| line_packing_gate | pass | All three lines measured above; no repack action |
| inequality_orientation_gate | pass | No forbidden orientation in signature/hypotheses |

Overall: pass. Project-wide build and LeanEval are parent-owned final checks.

## Result and phase checklist

Before: 10 declaration lines / 7 body lines. After: 8 declaration lines / 5 body
lines. Saved: 2 lines. Three audit issues fixed; no refactoring deferred.
Rules applied: 1.10 (optional proof-have folding), 1.15.
Renames queued: none. Comments preserved: none inside proof; public docstring and
source preserved. Refactoring needed: none.

- [x] Step 1 — required reference docs read
- [x] Step 2 — all 24 audit slots reported
- [x] Step 2.5 — five-method search-status block, including known service limitation
- [x] Step 2.6 — per-parameter generalisation and public literature search
- [x] Step 2.7 — measured signature table
- [x] Step 2.8 — inequality scan table
- [x] Step 3 — all 42 golfing rule statuses
- [x] Step 4 — actual alternative proofs and reflection
- [x] Step 5a — complete LSP diagnostics, only baseline header warning
- [x] Step 5b — diff gates and actual module build
- [x] Step 6a — no rename warranted; no shared queue mutation

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-hasseDeriv_single_aeval_X-build.log` and
`/private/tmp/roth-hasseDeriv_single_aeval_X-leaneval.log`.
