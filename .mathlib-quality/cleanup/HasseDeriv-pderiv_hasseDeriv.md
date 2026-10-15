# Phase 4: `MvPolynomial.pderiv_hasseDeriv`

Scope: only this declaration in `Roth/HasseDeriv.lean` and this report. Starting snapshot:
`/private/tmp/HasseDeriv-decl18-before.lean`. No Git actions or shared-log changes.

## Step 1 — references

Read installed lean4 and mathlib-quality skills; full Phase-4 worker prompt;
golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md in full; relevant declaration/format/comment/cast/style sections and
naming-conventions.md in full. Source `clean.tex` derivative definition inspected.

## Step 2 — full audit (initial lines 197–205; 9 declaration lines, 7 proof lines)

1. LINT: none in target; input file warning is unchanged missing copyright header.
2. HAVE SCAN: L200 `have h := congrArg (Nat.cast : ℕ → R) (hasseCoeff_mul_succ j d e)`
   has no `by`, is transformed by `push_cast at h` and consumed once by `rw` at L203.
   Replace the entire cast bridge by `← Nat.cast_mul` and the natural-number identity.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no original simp; proposed proof uses only extensionality and rewriting.
5. NAMING: `pderiv_hasseDeriv` names the outer and inner operations in the conclusion;
   snake_case composition of existing API identifiers; no forbidden abbreviations,
   numeric schemes, single-letter name, `_ge_`, or `_gt_`. No rename warranted.
6. LINE PACKING: measured two-line signature table below; no repack.
7. BY PLACEMENT: `:= by` ends L198; retained.
8. FORMAT: two-space tactics, packed rw list; no blank proof lines or instance syntax.
9. COMMENTS: no inline proof comments; source doc preserved byte-for-byte.
10. DOCSTRING: existing public mathematical formula plus source citation preserved.
11. VISIBILITY: public main result; external use in `Roth/GenWronskian.lean:177`.
12. STRUCTURE: headline theorem, 7-line body initially; no conjunction or branches.
13. MATHLIB: five-method record below; univariate partial matches only.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, equality theorem.
16. SHOW vs CHANGE: L203 term-mode `show ... by abel` is legal but can be removed
    using `← add_assoc e d` and `add_right_comm e d`.
17. PUSH_NEG: none.
18. GENERALISE: per-parameter table and public literature audit below; no applied change.
19. INEQUALITY: equality signature, no reversed inequalities; table below.
20. NORMAL-FORM: canonical derivative-on-left, scalar multiple of next Hasse operator
    on right. No new equivalence family or normal-form attribute needed.
21. SYNTAX-GEN: applied form supports coefficient calculations and existing rewrites.
    A linear-map composition counterpart is an optional API addition, left unapplied.
22. IMPORT-FANOUT: n/a, no new imports.
23. CASTS: removing the proof's `(Nat.cast : ℕ → R)` load-bearing annotation together
    with its bridge; statement's natural-to-R coercion remains meaningful and unchanged.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues to fix: replace single-use cast bridge, normalize multi-index addition by named
identities, replace final push_cast/ring by cast multiplication and associativity.
Refactoring needed: optional abstract iterative Hasse–Schmidt API and bundled composition
counterpart; substantial API work outside this proof, not applied.

## Line packing

All widths measured as Unicode codepoints. Signature unchanged by planned proof edit.

| Signature line | Width | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 197 | 71 | conclusion through `:= by`, 93 characters excluding indentation | 71 + 1 + 93 = 165 > 100 | ok |
| 198 | 97 | no next signature line | n/a | ok |

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | complete signature and all parameters | no `≥` or `>` | n/a | no `_ge_` or `_gt_` |

## Mathlib search status

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | Hasse derivative partial derivative composition multivariate polynomial | `Polynomial.hasseDeriv_comp`, `Polynomial.hasseDeriv_mul`, `MvPolynomial.pderiv_sumToIter`; univariate/coordinate-change partial matches |
| B Loogle | `Polynomial.hasseDeriv, Polynomial.derivative` | `Polynomial.hasseDeriv_one`, `hasseDeriv_one'`, `factorial_smul_hasseDeriv`; univariate only |
| C LeanSearch | Hasse derivative partial derivative composition | HTTP 500; unavailable, no retry loop |
| D source rg | `pderiv_hasseDeriv`, `hasseDeriv_pderiv`, `derivative_hasseDeriv` over complete Mathlib source; `coeff_pderiv`, `hasseDeriv_comp`, `hasseDeriv_one` in polynomial sources | full-name search no hits; coefficient and univariate composition building blocks found |
| E local names | `hasseDeriv` | source-backed polynomial, Laurent-series and project hits; native symbol index unavailable, not evidence of absence |

Auxiliary variants: `_comp`, `_one`, `_one'`, `_pderiv`, `pderiv_`, `derivative_`,
`coeff_`; canonical-equivalents lookup has no matching bucket.
Live `exact?` and `apply?` at the theorem entry both hit the default 200000-heartbeat
bound. Thus no claim of formally established exhaustive absence: no applicable duplicate
was found with the available searches. Keep the local theorem, building on `coeff_pderiv`
and the existing project coefficient identity. No new API extraction needed after the
direct rewrite proof removes the cast-juggling signal.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates | Verification/result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | variable index and finitely supported exponents | drop; universe widening | already independent universe; dropping leaves index type unbound; no broader polynomial index than arbitrary type needed |
| `{R : Type*}` | type variable | coefficient/scalar type | drop; universe widening | already independent universe; dropping leaves coefficient type unbound |
| `[CommSemiring R]` | typeclass | pderiv, hasseDeriv, coefficients, commutative multiplication | drop; Semiring; NonAssocSemiring | isolated probes required below; interfaces require CommSemiring |
| `(j : σ)` | structure value | derivative variable and single multi-index | drop | used in conclusion; removal leaves unbound j (probe below) |
| `(d : σ →₀ ℕ)` | structure value | arbitrary Hasse order | drop; abstract index | used in conclusion; non-natural orders would redefine Hasse derivative, not a weakening |
| `(P : MvPolynomial σ R)` | structure value | polynomial being differentiated | drop; abstract algebra | used on both sides; replacing polynomials requires an abstract iterative operator system |

No proposition hypotheses, decidability parameters, ordered hypotheses, finite-variable
assumptions, pointwise-global hypotheses, or concrete universes to weaken.
Inversion diagnostic: no distinguished concrete witness; statement already quantifies
over arbitrary polynomials and coefficient semiring. The coefficient proof uses the
polynomial coordinate API; general abstract operators would require explicit iterativity.

## Public literature search

Query: “Hasse derivative partial derivative composition generalization commutative ring
Hasse Schmidt”. Top three results: Narváez-Macarro's enveloping-algebra paper,
Wikipedia's Hasse derivative entry, Moosa–Scanlon's generalized Hasse–Schmidt varieties.
Additional primary sources opened:

- [Narváez-Macarro, Hasse–Schmidt derivations versus classical derivations](https://arxiv.org/abs/1810.08075): studies multivariate operators on arbitrary commutative algebras.
- [Hoffmann–Kowalski, Integrating Hasse–Schmidt derivations](https://arxiv.org/abs/1212.5788): iterativity depends on formal group laws.
- nLab Hasse–Schmidt derivative search result mentions commutative rigs; direct page fetch
  failed with unsupported XHTML, so no stronger primary-source claim relies on it.

Inference: an abstract *additive iterative* multivariate Hasse–Schmidt API could express
this composition relation. A general Hasse–Schmidt derivation without iterativity does
not automatically satisfy it. This is a new-structure/public-API proposal, left unapplied.
Current CommSemiring generality already avoids field, characteristic, and finite-variable
restrictions. ChatGPT math MCP skipped per delegated task authorization.

## Actual experiments before editing

Direct helper: `/Users/ramin/.local/share/uv/tools/lean-lsp-mcp/bin/python
/private/tmp/roth_mcp_probe.py`; live tool session 18949.

- `lean_goal` L200: inspected full coefficient goal and casted hypothesis.
- Whole proof `grind`: failed; `simp`: residual polynomial equality; `aesop`: exhausted.
- `exact?`, `apply?`: default-heartbeat timeout, no limits raised.
- First rewrite candidate missing `← add_assoc e d`: failed at `add_right_comm e d`.
- Corrected rewrite chain: zero goals, followed only by “No goals to be solved” from
  the untouched original tail (multi-attempt replaces one tactic, not whole proof).
- `simpa` with full additive/multiplicative AC normalization and congrArg: failed to
  align the coefficient index inside the congrArg expression; rejected.
- Original final `linear_combination`: unavailable under current imports (“unknown tactic”);
  no import added. Original final `norm_cast`: residual associativity equality.
- Original final `simp [mul_assoc]`: zero goals, clean; rewrite-only chain preferred.

## Completed generalisation experiments

`lean_run_code` with `autoImplicit false` tested all eight substitutions in isolated
code. Evidence: `/private/tmp/decl18-parameters.json`; tool completed without timeout.
Drop CommSemiring, replace by Semiring, and replace by NonAssocSemiring each failed
to synthesize `CommSemiring R` (probe lines 4–6). Dropping σ, R, j, d, P produced
the respective unknown identifiers (lines 7–11). These are intended negative tests,
not source diagnostics; source was never changed for them. No small-safe weakening
was found. Universe polymorphism is shown by the successful `#check` below.

## Golfing rule pass — all 42 statuses

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: original and final proofs have multiple tactic steps |
| 1.2 by rfl | n/a: no reflexivity-only proof |
| 1.3 rw + exact | n/a: no exact tail; final rw closes directly |
| 1.4 simp + exact | tried consolidation through simpa/congrArg, rejected after index mismatch |
| 1.5 trailing rfl | n/a: absent |
| 1.6 constructor tuples | n/a: equality with no constructor steps |
| 1.7 apply + exact | n/a: absent |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 eta reduction | n/a: no retained lambdas |
| 1.10 single-use have | applied: removed cast bridge and its sole rewrite consumer |
| 1.11 apply + intro | n/a: extensional coefficient proof has no introductions of implications |
| 1.12 redundant show | applied: replaced term-mode additive identity by named rewrites |
| 1.13 have projections | n/a: no conjunction/existential local fact |
| 1.14 merge rewrites | applied: arithmetic and cast normalization form one closing rw chain |
| 1.15 terminal simp only | n/a: none in original/final proof |
| 1.16 nonterminal bare simp | n/a: no retained simp |
| 1.17 dot notation | n/a: rewrites are global identities, no object-method application |
| 1.18 use `<\|` | n/a: no retained nested proof term or trailing parentheses |
| 1.19 push_neg | n/a: absent |
| 1.20 trivial existential helper | n/a: theorem is an equality |
| 2.1 grind whole proof | tried live; failed to derive the derivative identity |
| 2.2 delete before grind | n/a: no successful grind retained |
| 2.3 simpa consolidation | tried full AC-normalized congrArg; rejected on coefficient-index mismatch |
| 2.4 fun_prop | n/a: algebraic polynomial equality, no analytic function-property goal |
| 2.5 positivity | n/a: no positivity/nonzero goal |
| 2.6 gcongr | n/a: no order/monotonicity goal |
| 2.7 lia/omega | n/a: index equality is in a Finsupp additive monoid; scalar identity uses arbitrary R, not linear Nat/Int arithmetic |
| 2.8 aesop | tried live; exhaustive search failed |
| 2.9 norm_num/norm_cast | norm_cast tried on final equality, left associativity; explicit cast rewrites accepted |
| 2.10 decide | n/a: universally quantified symbolic polynomial identity, no closed finite computation |
| 2.11 field_simp; ring | n/a: no division and only CommSemiring structure |
| 2.12 linear_combination | tried live at original ring tail; unknown tactic under existing imports; no new import needed |
| 2.13 wlog | n/a: no symmetric case split |
| 2.14 calc to term | n/a: no calc |
| 2.15 `<;>` | n/a: only one coefficient goal after ext |
| 3.1 erw→rw | n/a: no erw |
| 3.2 fun_prop replacements | n/a: no continuity/measurability tactics |
| 3.3 omega→lia | n/a: no omega |
| 3.4 rcases with rfl | n/a: no rcases |
| 3.5 automation attributes | considered; leave plain theorem because new attributes alter public normalization behavior and are unnecessary here |
| 3.6 simp_all only | n/a: no simp_all |
| 3.7 remove limit raises | n/a: no limits in source; none added during experiments |

## Step 4 — reflection

Whole-proof automation did not close the theorem, and generic exact/apply search hit
the default heartbeat bound. A term-mode congrArg route required a longer normalization
list and failed to align indices. The accepted proof states the coefficient argument
directly: align the exponent sum, move the successor coefficient next to the Hasse
factor, combine their natural casts, use `hasseCoeff_mul_succ`, then reassociate.
It has no local bookkeeping, no final polynomial normalization, and no missing API
extraction signal. A bundled composition theorem could help future operator arguments,
but current call sites use this applied form directly; leave that API choice unapplied.

## Final gates

| Gate | Result | Evidence |
|---|---|---|
| fresh complete LSP | pass | session 18949 `lean_diagnostic_messages` after edit: success=true, partial=false, timed_out=false, failed_dependencies=[]; only unchanged line-1 copyright warning |
| lake_build_file | pass | actual `lake build Roth.HasseDeriv`, session 83601, exited 0; Built Roth.HasseDeriv (8.3s), 1430 jobs, only copyright warning |
| isolated proof | pass | direct helper `lean_run_code` on source prefix through renamed isolated target, including final proof; session 45897 exited 0, success=true, timed_out=false; `/private/tmp/decl18-isolated.json` |
| type/axioms | pass | separate importing `lean_run_code`: successful typed example of exact original statement; `#print axioms` = `[propext, Classical.choice, Quot.sound]`; isolated proof has identical standard axioms |
| definition_protected | pass | unified snapshot diff has no definition/abbreviation/signature changes |
| theorem_statement_protected | pass | Python substring comparison of complete signature through `:= by` true; full source prefix/suffix outside target identical |
| structure_gate | pass | 4 proof lines ≤15 headline bound; no conjunction or branches |
| naming_gate | pass | descriptive composition name; no forbidden pattern or abbreviation |
| line_packing_gate | pass | measured signature widths 71 and 97; 71+1+93=165; both rows ok; final proof widths 7,80,92,49 |
| inequality_orientation_gate | pass | zero reversed inequalities in whole signature, no order-name suffix |
| source scope/doc preservation | pass | prefix_identical=True, suffix_identical=True, signature_identical=True against worker snapshot |

Overall: pass. Full-project and `Roth.LeanEval` cumulative builds belong to the parent,
not claimed by this worker. Source finalized and parent notified before those builds.

Width-reference output from successful `set_option format.width 100 in #check`:

```lean
@pderiv_hasseDeriv : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (j : σ) (d : σ →₀ ℕ)
  (P : MvPolynomial σ R), (pderiv j) ((hasseDeriv d) P) = ↑(d j + 1) • (hasseDeriv (d + Finsupp.single j 1)) P
```

An initial scratch probe used nonexistent `pp.width`; corrected to `format.width` and
the complete type probe then succeeded. One oversized terminal request was interrupted
before execution and reissued through bounded subprocess arguments; it contributed no
proof evidence. No source edits or toolchain changes were used for either repair.

Final casts: one proof function-ascription removed with its whole bridge; zero added
explicit casts/ascriptions in proof; statement's natural-to-R coercion and natural-number
annotation preserved. Existing source docstring preserved exactly; no inline comments.

## Result and phase checklist

Before: 9 declaration lines / 7 body lines. After: 6 declaration lines / 4 body lines.
Saved: 3 lines. Three proof issues fixed; no mandatory refactoring deferred.
Optional proposals: abstract iterative Hasse–Schmidt API; bundled composition counterpart.
Renames queued: none. No shared logs or Git operations.

- [✓] Step 1 — reference docs read.
- [✓] Step 2 — all 24 audit slots recorded.
- [✓] Step 2.5 — five-method search status, partial matches, and explicit tool limitations recorded.
- [✓] Step 2.6 — all parameters, actual negative tests, literature and inversion check recorded.
- [✓] Step 2.7 — complete measured signature-width table, unchanged final signature.
- [✓] Step 2.8 — complete inequality-occurrence table.
- [✓] Step 3 — all 42 golfing rules have statuses and reasons.
- [✓] Step 4 — strategy reflection and actual alternatives recorded.
- [✓] Step 5a — fresh complete LSP, no target errors or warnings.
- [✓] Step 5b — module build, isolated proof/type/axioms, diff and content gates passed.
- [✓] Step 6a — no required rename; no shared sidecar action.

## Dependent checkpoint validation

The file owner ran `lake build` (2586 jobs) and `lake build Roth.LeanEval`
(2585 jobs), sequentially; both exited 0. Logs:
`/private/tmp/roth-pderiv_hasseDeriv-build.log` and
`/private/tmp/roth-pderiv_hasseDeriv-leaneval.log`.
