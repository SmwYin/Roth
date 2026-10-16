# Phase 4 — Roth.eval_diag

Target: `Roth/CoeffNorm.lean:188–191`, C20 diagonal-evaluation compatibility.
Dedicated single-declaration ownership; only target and this report touched. No Git operations,
shared logs, imports, dependencies, instances, definition values or documentation changed.
Baseline inherited from owner: full `lake build` and separate `lake build Roth.LeanEval`
(session 47412) exited 0; complete LSP clean of errors. These builds were not repeated here.
Pinned Lean 4.34/mathlib retained.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read both full SKILL.md files,
the full worker contract, style-rules.md, naming-conventions.md, and mathlib-review-stages.md.

## Result

Four declaration lines before and after; one proof line before and after. Only change:
`fun _ => x` → `fun _ ↦ x`. This is binder notation, with the exact original type preserved.
Existing docstring and source citation preserved verbatim. One syntax issue fixed; no proof
churn. No renames queued. Refactoring needed: none within the preservation contract.

SOURCE FROZEN after final source edit, whole-file SHA256:
`815a7a525d0a6ec34149da5b5d141cf978321d242abbefb9eb50bbcad4fe2cd8`.
Owner explicitly revoked source ownership at this hash. All later work was probes/report/checks.

## Full audit

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | No warning/error in target. Six existing outside warnings: header; DecidableEq on normOne_mul_le, normOne_prod_le, normOne_det_le, abs_coeff_det_hasseDeriv_le; hC. Preserved per owner. |
| 2 | HAVE SCAN | Zero `have` declarations; no single-use binding to inline. |
| 3 | SET_OPTION | No target options or resource increases. |
| 4 | SIMP SQUEEZE | One terminal `simp_all [diag]`, closing all induction cases; unsqueezed correctly. |
| 5 | NAMING | `eval_diag` describes evaluation of diag, snake_case, no banned patterns/abbreviations. |
| 6 | LINE PACKING | All three signature lines measured below; conclusion applications cannot share preceding lines. |
| 7 | BY PLACEMENT | `:= by` on final statement line. |
| 8 | FORMAT | Two-space proof indentation; no blank internal lines or trailing whitespace. Lambda arrow normalized to ↦. |
| 9 | COMMENTS | No proof comments; two-line docstring/source retained verbatim. |
| 10 | DOCSTRING | Public result documents diagonal substitution and cites Lemma 9. Existing API documentation preserved. |
| 11 | VISIBILITY | Public compatibility API preserved; no visibility change authorized. |
| 12 | STRUCTURE | One-line proof; three induction branches each closed by simp_all; no conjunction or long branch. |
| 13 | MATHLIB | All five search methods below; partial general composition match, not exact named diag API. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: equality, no existential. |
| 16 | SHOW vs CHANGE | No show in retained proof. Composition alternative used change in scratch only. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All three parameters analyzed/probed below. Optional abstract-target candidate closed under preservation instruction. |
| 19 | INEQUALITY | Zero ≥ or > operators; scan table below. |
| 20 | NORMAL-FORM | Applied equality removes diagonal substitution by evaluation; matches eval_map/comp normal forms. No new equivalence web. |
| 21 | SYNTAX-GEN | Existing applied form supports rewriting at call sites; bundled general law exists in mathlib. No required public restatement. |
| 22 | IMPORT-FANOUT | n/a: zero imports changed. |
| 23 | CASTS | Zero explicit coercions/ascriptions added or removed; Int.castRingHom is the necessary coefficient hom. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: lambda notation, applied. No new helper justified for a one-line proof.

## Line packing

Actual CLI `set_option format.width 100; #check @Roth.eval_diag`:

```lean
@eval_diag : ∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) (x : ℝ),
  Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (diag P)) = (eval fun x_1 => x) ((map (Int.castRingHom ℝ)) P)
```

The pretty-printer leaves an unbreakable equality line wider than the requested width; source
uses natural application boundaries to respect the 100-codepoint source limit.
Measured by Python `len`, not UTF-8 bytes. Next token means the complete application at the
natural break; splitting inside its function head merely to fill a line worsens readability.

| Sig line | Chars | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 188 | 50 | `Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (diag P))` (63) | 50 + 1 + 63 = 114 > 100 | ok |
| 189 | 69 | `eval (fun _ ↦ x) (map (Int.castRingHom ℝ) P)` (44) | 69 + 1 + 44 = 114 > 100 | ok |
| 190 | 56 | none; proof body next | n/a | ok |

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | complete signature/hypotheses | n/a: zero ≥/> operators | none | no `_ge_`/`_gt_` |

`=>` before cleanup was a lambda token, not an inequality. After edit zero ASCII > occurs in the signature; `<;>` in the proof is a tactic combinator.

## Mathlib search-status

[A] Lean-Finder: “multivariate polynomial evaluation after substitution composition ring
homomorphism” returned `MvPolynomial.comp_eval₂Hom`, `eval₂_comp`, `eval₂_comp_right`.
[B] Loogle: initial malformed placeholder query rejected; corrected
`MvPolynomial.eval₂, RingHom.comp` returned `hom_eval₂`, `eval₂_comp_left`, `eval₂_map`.
[C] LeanSearch: “multivariate polynomial evaluation composition ring homomorphism” returned
`eval₂Hom`, `comp_eval₂Hom`, `eval`.
[D] Source rg: full untruncated `eval₂_comp_left|eval_map|eval₂Hom|eval₂_comp` in
Algebra/MvPolynomial/Eval.lean and Polynomial/Eval/Defs.lean. Verified source lines 214, 432,
and Polynomial/Eval/Defs.lean:577. Local diag definition at CoeffNorm.lean:156.
[E] Native lean_local_search query `eval₂_comp_left` consulted source but reported index
unavailable; it returned the enclosing eval declaration. No absence claim drawn from that.
Names independently confirmed by source and actual CLI #check, including Polynomial.eval_map,
MvPolynomial.eval₂_comp_left, aeval_eq_eval₂Hom, Polynomial.eval₂RingHom.

Auxiliary variants: `_left`, `_right`, `comp_eval₂Hom`, `hom_eval₂`, `eval₂_map`,
`eval₂_eq_eval_map`. Common-equivalents table: no matching topology/finite/bounded bucket.
Six strict rules considered: no new wrapper/predicate; all searches executed; auxiliary variants
searched; no exact duplicate deletion authorized; library usage documented here because existing
module documentation is protected. Public declaration and local diag API preserved as required.

Conclusion: partial match in general composition API. Tested direct composition proof (below),
which takes four tactics and extra bundling; existing one-line induction remains better.
`exact?` failed; `apply?` offered only Real.ext_cauchy subgoals, not a closed generic proof.
No claim that all general mathematical content is absent from mathlib.

## Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable/universe | Variable domain of P and constant assignment | Drop σ with autoImplicit false; universe polymorphism already present | yes CLI | Drop fails unknown σ; keep Type* with independent universes. No class parent/strict/pointwise hypothesis here. |
| 2 | `(P : MvPolynomial σ ℤ)` | structure-value | Both sides and induction subject | Drop P with autoImplicit false; coefficient generality requires changing diag definition | yes CLI | Drop fails unknown P on both sides. No bundled proposition to unbundle or order hypothesis to weaken. Definition abstraction out of scope. |
| 3 | `(x : ℝ)` | structure-value/concrete target | Both evaluations | Drop x; ℝ → A with CommRing A; parent probes Ring A and CommSemiring A | yes CLI | Drop fails unknown x. CommRing target compiles with same proof. Ring fails CommSemiring A; CommSemiring fails NonAssocRing A needed by Int.castRingHom. Original public signature retained. |

No explicit proposition, decidability parameter, global function-property hypothesis, strict
inequality, or structure-valued equivalence occurs, so point-localisation/strict→weak/unbundling
catalogue entries have no applicable syntactic input. Inversion check: concrete diag is unfolded
once and the remainder is homomorphism compatibility, already supplied abstractly by mathlib.
The ℝ→CommRing target variant is optional, changes the explicit call signature, and has no
required benefit in this task. Closed under owner instruction, not left awaiting approval.

Actual candidate probe `/private/tmp/eval_diag_drop.lean`, lake env lean exit 1 as expected:
σ drop L5 unknown σ; P drop L11/L12 unknown P; x drop L15/L16 unknown x; Ring target L20
failed CommSemiring A; CommSemiring target L24/L25 failed NonAssocRing A. No failed candidate
was installed in source. Successful abstract target `/private/tmp/eval_diag_verify.lean`, exit 0.

### Literature search status

Web query: “polynomial evaluation substitution universal property generalization semiring”.
Top three returned hits captured:
1. [RWTH Brinke thesis](https://logic.rwth-aachen.de/pub/brinke/masterarbeit.pdf), universal
   property of polynomial semirings.
2. [Semiring Provenance for Büchi Games](https://lmcs.episciences.org/13205/pdf), polynomial
   semiring universal property/evaluation.
3. [Elementary equivalence versus isomorphism in semiring semantics](https://www.researchgate.net/publication/349195393_Elementary_equivalence_versus_isomorphism_in_semiring_semantics), polynomial semirings/universal property.
The third is a secondary hosting page and used only as a captured search hit, not authority.
Also returned [Polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring), explicitly
states arbitrary variable sets/free commutative algebras, and
[the authors' arXiv paper](https://arxiv.org/abs/2102.05473).
Inference: evaluation compatibility belongs at the ring/semiring homomorphism level; no order
or analysis on ℝ is intrinsic. The compile-tested CommRing target confirms the applicable
integer-coefficient specialization. No public restatement made.
ChatGPT math MCP: n/a, no such tool in ALL_TOOLS metadata. No invented second opinion.

## Golfing rule pass (all 42)

- [1.1] by exact: n/a, no wrapper.
- [1.2] by rfl: n/a, no reflexivity proof; actual rfl probe failed.
- [1.3] rw + exact: n/a, neither in retained proof.
- [1.4] simp + exact: n/a, simp_all closes directly.
- [1.5] trailing rfl: n/a, none.
- [1.6] constructor/exact: n/a, equality only.
- [1.7] apply + exact: n/a, none.
- [1.8] by_contra/push_neg: n/a, none.
- [1.9] eta-reduction: n/a, constant lambda is not eta-shaped; arrow syntax normalized.
- [1.10] inline have: n/a, zero have.
- [1.11] apply/intro: n/a, none.
- [1.12] redundant show: n/a, none.
- [1.13] have projections: n/a, none.
- [1.14] consecutive rw: n/a, none in retained proof.
- [1.15] terminal simp only: n/a, already unsqueezed simp_all.
- [1.16] nonterminal bare simp: n/a, terminal all-goal simplification.
- [1.17] dot notation: n/a, no composed lemma term to shorten.
- [1.18] <|: n/a, no avoidable terminal parentheses.
- [1.19] push Not: n/a, no negation manipulation.
- [1.20] trivial existential lemma: n/a, not existential.
- [2.1] grind: actual live `grind [diag]` failed; retained induction.
- [2.2] delete before grind: n/a, no grind in original.
- [2.3] simpa consolidation: n/a, no following closing tactic; direct simp [diag] failed.
- [2.4] fun_prop: n/a, equality of evaluated values, no analytic property.
- [2.5] positivity: n/a, neither positivity nor nonzero goal.
- [2.6] gcongr: n/a, no inequality/monotonicity.
- [2.7] lia/omega: n/a, arbitrary polynomial/real equality, no linear arithmetic goal.
- [2.8] aesop: actual live attempt failed exhaustive search with unsolved eval₂ equality.
- [2.9] norm_num/norm_cast: n/a, no concrete numeric computation or coercion identity.
- [2.10] decide/+kernel: n/a, universally quantified real evaluation is not finite computation.
- [2.11] field_simp/ring: n/a, no denominator; evaluation on abstract polynomial needs compatibility.
- [2.12] linear_combination: n/a, original does not end in ring/ring_nf and has no equations to combine.
- [2.13] wlog: n/a, constructor induction cases are not symmetric.
- [2.14] calc collapse: n/a, no calc.
- [2.15] <;>: already applies terminal simp_all to all three induction cases.
- [3.1] erw/rw: n/a, no erw.
- [3.2] continuity/measurability: n/a, none.
- [3.3] omega/lia: n/a, no arithmetic tactic.
- [3.4] rcases/rfl: n/a, none.
- [3.5] automation registration: no new attribute needed for compatibility API; preserve public attributes.
- [3.6] simp_all over only: already in preferred form; actual removing [diag] fails all three cases.
- [3.7] maxHeartbeats: n/a, no option in target.

## Reflection and actual probes

Native live lean_multi_attempt at line 191 tested rfl, simp [diag], grind [diag], aesop,
exact?, apply?, explicit eval-map/composition simplification, original induction/simp_all,
induction/simp_all without diag, and induction/simp [diag, *]. Only original closes all goals
without extra infrastructure. Failed simp [diag,*] does not rewrite induction hypotheses
consistently after unfolding, so simp_all is useful. Removing diag leaves constant/add/mul_X
cases. Bare direct composition simp leaves nested evaluation. `apply?` scratch result carries
sorry because partial; it was rejected and never installed.

An initial goal/attempt at line 192 hit the blank line (source shifted since dispatch); corrected
to live line 191 before drawing any proof conclusion. Fallback Python MCP was tested and
returned the same blank-line context; native tools then worked normally at the right line.

Independent exact-original-type reproof in `/private/tmp/eval_diag_verify.lean`:

```lean
  rw [Polynomial.eval_map, MvPolynomial.eval_map]
  change (Polynomial.eval₂RingHom (Int.castRingHom ℝ) x)
    (eval₂ Polynomial.C (fun _ ↦ Polynomial.X) P) = _
  rw [MvPolynomial.eval₂_comp_left]
  simp [Function.comp_def]
```

This is mathematically direct but longer than one-line structural induction, needs explicit
bundling and composition unfolding. No new helper or term-mode version offers a required
benefit. Simplify reflection complete: retained shortest successful maintainable proof.

## Performance

Actual CLI profiler `/private/tmp/eval_diag_profile.lean` exited 0. Same one-line proof,
`set_option profiler true in` isolated outside repository; cumulative typeclass inference
114ms, simp 68.7ms, type checking 22.9ms, tactic execution 16.2ms. No indication of a
one-second elaboration bottleneck; no resource increases or profiling scaffolding in source.
This is the available in-thread performance pass; no separate simplify/buzz tool is exposed.

## Verification and gates

Actual `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm` session 1379 exited 0,
1658 jobs; CoeffNorm built in 8.7s, with precisely six pre-existing outside warnings.
Actual native full-file lean_diagnostic_messages after final edit: partial=false,
success=true, timed_out=false, failed_dependencies=[]; zero errors and only those six
outside warnings. Live goal at line 191 shows original context before, zero goals after.

Actual fresh CLI `/Users/ramin/.elan/bin/lake env lean /private/tmp/eval_diag_verify.lean`
session 34678 exited 0. It contains exact original-type assignment `:= @Roth.eval_diag`,
independent nonself composition reproof, and generic CommRing target proof.
All three `#print axioms` outputs are exactly `[propext, Classical.choice, Quot.sound]`.
No new axiom, sorry, suppression or changed definition value is in repository source.

Target comparison against the dispatch-original four-line block was mechanically asserted:
replacing the new lambda arrow by the old one gives the original block exactly. Assertions
also checked widths ≤100, no trailing whitespace, four lines, no conjunction, no ≥/> in the signature,
no sorry/admit/axiom/options/haveI/letI. All passed on the corrected signature-scoped inequality assertion. The initial overly broad scan
matched the `>` in tactic `<;>`; this was corrected to scan the signature only. No Git commands used.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | session 1379 exit 0, `lake build Roth.CoeffNorm` |
| definition_protected | ✓ pass | target theorem only; no definition/abbrev/instance touched |
| theorem_statement_protected | ✓ pass | exact original-type assignment compiles; only lambda token changed |
| structure_gate | ✓ pass | one proof line; no conjunction; three immediately closed branches |
| naming_gate | ✓ pass | descriptive eval_diag; zero forbidden patterns |
| line_packing_gate | ✓ pass | all three measured rows ok, application boundaries exceed 100 |
| inequality_orientation_gate | ✓ pass | per-occurrence scan zero, actual assertion passed |
| diagnostics | ✓ pass | complete native LSP, no errors or target warnings |
| standard_axioms | ✓ pass | exported theorem and independent proof standard axioms only |
| scope/freeze | ✓ pass | post-check SHA256 equals frozen hash above |

Overall: pass. Before 4 lines, after 4, saved 0. One notation issue fixed. Rules newly
applied: lambda-arrow syntax; 2.15 and 3.6 already satisfied. No rename, helper extraction,
or public restatement needed. Comments-preserved: existing two-line docstring verbatim;
no inline comments existed. Optional abstract-target variant closed without API change.
Six outside warnings remain under owner's existing preservation/approval handling.

## Required phase checklist

- [✓] Step 1 — required reference docs and both skills read in full.
- [✓] Step 2 — all 24 audit items recorded concretely.
- [✓] Step 2.5 — all five mathlib search methods, auxiliary variants and strict rules recorded.
- [✓] Step 2.6 — every parameter analyzed, applicable candidates actually compiled; literature top three captured.
- [✓] Step 2.7 — complete signature width table and width-100 #check recorded.
- [✓] Step 2.8 — inequality occurrence table and final assertion recorded.
- [✓] Step 3 — all 42 golfing rules have explicit statuses.
- [✓] Step 4 — whole-proof alternatives, independent composition route and performance reflection completed.
- [✓] Step 5a — complete clean-of-errors LSP diagnostics, no target warning.
- [✓] Step 5b — actual module build and all diff/protection/content gates pass.
- [✓] Step 6a — no rename needed; no shared sidecar changed.
