# Phase 4: `Roth.diag_eq_sum`

Target: `Roth/CoeffNorm.lean`, original L159–165; final L159–163. Dedicated single-declaration
worker. Only the proof body and this report were edited. Before: 7 declaration lines / 5 proof
lines; after: 5 / 3; saved: 2. Original public signature and docstring are byte-identical.

SOURCE FROZEN: `f3e745f4aab0b8c61c9ee4196bf8267aa97138ac57cada23aae913b0a79d31c0`.
Ownership revoked after this SHA256; no subsequent source edits by this worker.

## Step 1 — preparation

Read in full: both `mathlib-quality/SKILL.md` and `lean4/SKILL.md`, full verbatim
`/private/tmp/roth-coeffnorm-worker-contract.md`, `golfing-rules.md`, `proof-patterns.md`,
`mathlib-search.md`, `generalisation-patterns.md`, `cleanup-gates.md`; read the applicable
formatting, theorem, documentation, naming and normal-form sections of `style-rules.md`
and `mathlib-review-stages.md`. Naming reference was not additionally required: no naming
issue arose. Read target and surrounding `diag`, `abs_coeff_diag_le`, `normOne_diag_le` context.

Baseline inherited from file owner: full `lake build` and separate `lake build Roth.LeanEval`
passed (LeanEval session 37370 exit 0); complete LSP had no errors. Per dispatch these builds
were not repeated by this worker. Pinned Lean/mathlib untouched.

Mathematics: substituting the same indeterminate in every variable sends a monomial with
exponent vector k to the univariate monomial of degree the sum of k's entries. Additivity
then gives the finite support sum. Mathlib `eval₂_eq` already performs that additive expansion.

## Step 2 — full audit

| # | Audit | Concrete finding/action |
|---|---|---|
| 1 | LINT | None in target. Complete LSP returns only six known outside warnings. |
| 2 | HAVE SCAN | No `have` or `let` in either proof; nothing to inline. |
| 3 | SET_OPTION | None; no limits or linter suppressions added. |
| 4 | SIMP SQUEEZE | Original contains only `rw`; tested terminal `simp` failed because integer constants become casts. Final `simp_rw` deliberately performs only specified rewrites. |
| 5 | NAMING | `diag_eq_sum` describes the equality; snake_case, no prohibited pattern or abbreviation; no rename needed. |
| 6 | LINE PACKING | Every signature line measured in table below; both justified; maximum declaration line 88 codepoints. |
| 7 | BY PLACEMENT | `:= by` at end of conclusion line. |
| 8 | FORMAT | Two-space tactics, four-space signature continuation, no blank body lines or tactic semicolons. |
| 9 | COMMENTS | No inline comments existed; original docstring preserved verbatim. |
| 10 | DOCSTRING | Existing one sentence explains the collected monomial degree; preserved under public documentation policy. |
| 11 | VISIBILITY | Public API preserved as explicitly required; not changed to private. |
| 12 | STRUCTURE | Three proof lines, no conjunction or branches; no extraction needed. |
| 13 | MATHLIB | Five-method search below found the direct expansion `eval₂_eq`; use it instead of `P.as_sum` plus congruence. |
| 14 | JUNK DEF | n/a: theorem, no definition edited. |
| 15 | EXISTS LEMMA | n/a: no existential conclusion or helper. |
| 16 | SHOW vs CHANGE | n/a: neither occurs. |
| 17 | PUSH_NEG | n/a: no negation manipulation. |
| 18 | GENERALISE | All actual parameters examined and drop-tested below; universe already polymorphic; no local class/proposition hypotheses. |
| 19 | INEQUALITY | Zero reversed inequalities, table below. |
| 20 | NORMAL-FORM | Finite sum of univariate monomials is the desired RHS normal form for coefficient estimates; `eval₂_eq` supplies the general source expression. |
| 21 | SYNTAX-GEN | OK: downstream `rw [diag_eq_sum]` directly exposes the coefficients; no demonstrated application benefit from restating. |
| 22 | IMPORT-FANOUT | n/a: no import added or removed. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing ascriptions in diff; no explicit casts introduced. |
| 24 | INSTANCE-NAME | n/a: no instance declaration or local instance. |

Issues fixed: replace hand-expanded support proof with direct Mathlib evaluation expansion;
remove redundant congruence/lambda and monomial evaluation plumbing. No deferred required
refactoring. Optional public wrapper deletion or coefficient-ring redesign is closed under
the explicit signature/documentation preservation instruction; no required downstream benefit
was found that would justify escalating it.

## Step 2.5 — Mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `MvPolynomial evaluate polynomial sum monomials coefficients support` | `MvPolynomial.eval_eq`, `eval_eq'`, `sum_def`. |
| B Loogle | `MvPolynomial.aeval` | `aeval`, `aevalTower_id`, `aevalTower_ofId`, `Algebra.adjoin_range_eq_range_aeval`, `aeval_range`. |
| C LeanSearch | `multivariate polynomial evaluation sum support coefficients monomial` | `support_sum_monomial_coeff`, `eval₂_eq'`, `eval₂_eq`. |
| D source rg | `eval₂_eq\|aeval_def\|aeval_monomial\|eval₂.*sum\|sum.*eval₂\|aeval_eq` in Eval.lean | Verified `eval₂_eq` L72, `aeval_def` L572, `aeval_monomial` L681, `aeval_sum` L698; full untruncated results inspected. |
| E local names | `eval₂_eq`, limit 12 | Source hits included `MvPolynomial.eval`; index reported unavailable. Presence subsequently verified by native `#check MvPolynomial.eval₂_eq` and compiled use. No absence conclusion drawn from the unavailable index. |

Auxiliary variants: `eval₂_eq'` (adds unneeded Fintype), `aeval_sum` / `eval₂_sum` (the
original route), `aeval_monomial`, `aeval_def`, `aeval_eq_eval₂Hom`, and product/degree
normalization. Common-equivalents table: no topology, finiteness, separation or bornology
bucket applies; this is an algebra-homomorphism evaluation expansion.

Concluded: partial/general match `MvPolynomial.eval₂_eq`; keep required public API and
build directly on it. Rules 1/5 (delete wrapper) are overridden by explicit preservation;
rule 2 five searches performed, with no unsupported absence claim; rule 3 variants checked;
rule 4 no custom predicate; rule 6 record usage here because module docs are preserved.
Native `exact?` at the original goal failed; `apply?` suggested coefficient extensionality
and other partial routes only. No newly claimed missing API and no new local lemma.

## Step 2.6 — generalisation status

| # | Parameter | Class | Used as | Mechanical candidates/probes | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type u_1}` | type variable | Variable index for P and its exponent vectors | Drop σ under `autoImplicit false`; universe polymorphism `Type v` reproof; no class parent, pointwise or strict-weak candidate applies to a type binder | yes | Drop fails `Unknown identifier σ` L4. Arbitrary universe v compiles; original already has this generality. |
| 2 | `(P : MvPolynomial σ ℤ)` | structure value | Both sides use P, its support and coefficients | Drop P under `autoImplicit false`; no property/class weakening or localisation of a structure value; abstract ℤ→R would also require restating fixed `diag` | yes | Drop fails `Unknown identifier P`, `P.support`, `P.coeff` L5. Keep explicit binder. |

No proposition, decidability, typeclass or hidden section instance occurs in the checked
full type. All actual drop probes ran through `lean_run_code`, with errors inspected; no
unverified successful weakening is claimed. Arbitrary universe v was checked both in native
MCP and fresh CLI exact-type assignment and independent reproof. None of the catalogue's
continuity/strictness/unbundling entries apply: there are no such hypotheses.

Inversion check: `diag` unfolds once; the remaining argument is the general Mathlib
evaluation expansion plus product powers. The abstract result already exists as `eval₂_eq`;
no extra abstraction needs to be added. Generalising `diag` itself is outside this declaration
and would change its fixed public coefficient ring. Big-change candidates requiring action:
none; optional coefficient-ring API redesign closed under the preservation instruction.

### Literature search status

Actual web query: `multivariate polynomial diagonal substitution monomial total degree
generalization`. Top three returned hits captured:

1. [Diagonally-reduced tensor-product polynomials: Dimensions and boundary–diagonal matching](https://doi.org/10.1016/j.cam.2026.117913): concerns boundary interpolation, not an assumption weakening here.
2. [An alternative equation for generalized monomials](https://link.springer.com/article/10.1007/s00010-022-00917-y): diagonalisation of multi-additive functions, a different meaning of monomial.
3. [Alfarano thesis, §8.2](https://user.math.uzh.ch/alfarano/PhdThesis.pdf): polynomial generalisation in a different setting; no relevant weakening extracted.

These hits do not establish an alternative theorem; no unsupported literature inference made.
The relevant local source `.mathlib-quality/references/clean.tex` L1449 explicitly discusses
replacing all x_i by the same x and bounding resulting coefficients. The direct generality
evidence is the checked Mathlib `eval₂_eq`, over commutative semirings and arbitrary ring maps.
ChatGPT math MCP: n/a, no matching callable tool in `ALL_TOOLS` metadata.

## Step 2.7 — line packing

Native and fresh CLI `#check @diag_eq_sum` at `format.width := 100`:

```lean
@diag_eq_sum : ∀ {σ : Type u_1} (P : MvPolynomial σ ℤ),
  diag P = ∑ k ∈ P.support, (Polynomial.monomial (Finsupp.degree k)) (P.coeff k)
```

| Sig line | Chars | Next complete signature token/group | Arithmetic | Action |
|---|---:|---|---|---|
| 159 | 44 | conclusion through `:= by`, 72 chars without continuation indent | 44 + 1 + 72 = 117 > 100 | ok |
| 160 | 76 | no next signature line; proof follows | n/a | ok |

No repacking necessary. All widths are Python Unicode character counts, not bytes.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | whole signature and every parameter | n/a: no ≥ or > | none | none: no `_ge_` or `_gt_` |

## Step 3 — all 42 golfing rules

| Rule | Status/evidence |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no `rw; exact`. |
| 1.4 | n/a: no simp followed by exact. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction argument. |
| 1.9 | Original `fun k _ => ?_` was not eta-reducible; eliminated entirely with direct expansion. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no conjunction projection. |
| 1.14 | General API replaces original expansion rewrites; retained a single initial rw plus targeted simp_rw. |
| 1.15 | Tried terminal simp (native isolated probe); fails with integer-cast/product sum goal, so final uses explicit `simp_rw` rather than terminal simp only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | n/a: no remaining suitable dot-notation application. |
| 1.18 | n/a: no trailing parenthesized argument to remove. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not a private existential helper. |
| 2.1 | Actual native multi-attempt `grind` failed at whole goal. |
| 2.2 | n/a: no grind in retained proof. |
| 2.3 | Compiled `simpa only [...] using eval₂_eq ... P`; valid but longer and introduces explicit map/lambda; selected simpler rw/simp_rw. |
| 2.4 | n/a: no function regularity property. |
| 2.5 | n/a: no positivity goal. |
| 2.6 | n/a: no inequality or monotonicity goal. |
| 2.7 | n/a: no Nat/Int linear arithmetic proposition; exponent sum is structural product identity. |
| 2.8 | Actual native multi-attempt aesop failed, made no progress. |
| 2.9 | n/a: no concrete numeric computation or cast-equality goal. |
| 2.10 | n/a: arbitrary symbolic polynomial identity, no finite executable decision procedure. |
| 2.11 | n/a: no denominators. |
| 2.12 | n/a: no ring/ring_nf ending or algebraic hypotheses. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc block. |
| 2.15 | n/a: no multiple similar subgoals in final proof. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega or arithmetic tactic. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No new simp/grind attribute: explicit rewrite API already serves downstream coefficient proofs; attribute changes outside preserved public interface. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no heartbeat option. |

## Step 4 — reflection

Whole-goal grind, simp and aesop were tried; none closes. `exact?` failed and `apply?`
offers extensionality without resolving the evaluation. One `simp only` with all definitions
and expansion lemmas compiles, but targeted `rw` plus `simp_rw` expresses the same deterministic
normalization without conflicting global cast simplification. A term-mode `simpa only`
proof also compiled but needs an explicit algebra map and constant lambda, making it longer.
No have blocks, redundant goal changes, private helpers or missing API remain. The selected
strategy directly follows the algebra and removes the need for a support-sum congruence.

## Step 5 — verification and gates

Actual command `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 48754, exited 0:
`Built Roth.CoeffNorm (15s)` and `Build completed successfully (1658 jobs)`.
Complete native `lean_diagnostic_messages` after edit and again after build:
`partial=false`, `success=true`, `timed_out=false`, no failed dependencies and zero errors.
Six warnings outside target: header L1; DecidableEq at L89, L99, L112, L266; unused hC L115.
These are inherited/scoped out by dispatch, not suppressed or counted as fixed.

Native exact-type/reproof probe succeeded but reported stale imports; therefore ran fresh
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-diag-evidence.lean`, session 20109,
exit 0. It imports the final built module, assigns `@diag_eq_sum` to its exact original
universe-polymorphic type, and reproves it without referring to `diag_eq_sum`, using the
independent monomial-sum route. Both print only `[propext, Classical.choice, Quot.sound]`.
No sorry, axiom, suppression, definition, import, instance or documentation added to source.

Actual Python difflib/gate check against the captured original target returned:
statement-byte-identical True; definition-lines-changed False; body-lines 3; bad-name False;
reverse-inequalities 0; max-width 88; signature-widths [44,76]; full next token width 72;
whole-file SHA256 matches frozen value. Target diff contains only the five old proof lines
replaced by the three new ones. No Git mutation or shared log writes performed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build session 48754 exit 0. |
| definition_protected | pass | Only theorem proof-body lines edited; no def/abbrev. |
| theorem_statement_protected | pass | Byte-identical signature comparison and exact original-type assignment. |
| structure_gate | pass | Three proof lines, no conjunction or branches. |
| naming_gate | pass | Actual forbidden-pattern scan false; no rename. |
| line_packing_gate | pass | Complete two-row table, 117-character joined signature would overflow. |
| inequality_orientation_gate | pass | Actual signature scan zero; full occurrence table above. |

Overall: pass. Refactoring needed: none. Renames queued: none. Comments preserved: no inline
comments present, original declaration docstring preserved. Required module/LSP validation
complete; whole-project/publication builds remain the file owner's responsibility.

## Phase checklist

- [✓] Step 1 — full required references read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five-method search and variants reported.
- [✓] Step 2.6 — all parameters audited, actual drop/universe probes and literature status reported.
- [✓] Step 2.7 — complete measured signature packing table and width-100 #check reported.
- [✓] Step 2.8 — complete inequality scan table reported.
- [✓] Step 3 — all 42 golfing rules reported with actual applicable probes.
- [✓] Step 4 — strategy reflection completed.
- [✓] Step 5a — complete native LSP diagnostics, zero errors.
- [✓] Step 5b — actual module build and diff gates pass; independent fresh CLI evidence pass.
- [✓] Step 6a — no rename required; no shared sidecar modified.
