# Independent audit: `Roth.rescale_separated_factor_aux`

## Initial audit — recorded before any source edit

Scope: the newly added private helper at lines 451–461, compared to
`/private/tmp/roth-separation-d29-first-freeze.lean`. Source dispatch SHA:
`c55b2bf327ea8b42cda84beb9d360a70784c64d4d806a055f3af0e2dc9781bc3`.
This is an unpublished declaration-29 batch, not a published cleanup.

| Item | Initial finding / action |
|---|---|
| 1 LINT | Complete native module LSP: no helper warnings; module has preserved header warning and two public-30 instance warnings. |
| 2 HAVE | One anonymous equality `C g * C g⁻¹ = 1`, used once by linear_combination; retain as explicit inverse-cancellation certificate pending tactic probes. |
| 3 SET_OPTION | None. |
| 4 SIMP | No simp calls. |
| 5 NAMING | `rescale_separated_factor_aux` describes scalar redistribution in a separated product; snake_case, private `_aux`, no forbidden abbreviation or numeric pattern. No rename required. |
| 6 WIDTH | Measure all six signature lines and compare format.width 100; no source reformat before this audit. |
| 7 BY | `by` ends conclusion line. |
| 8 FORMAT | Two-space tactics, four-space continuation; no blank proof lines, instance bindings, semicolons or consecutive rw to merge. |
| 9 COMMENTS | No proof comments; surrounding narratives preserved. |
| 10 DOCSTRING | Private helper exempt; no new docstring needed. |
| 11 VISIBILITY | One local use in exists_int_factors; already private with `_aux`. |
| 12 STRUCTURE | Five physical proof lines, no conjunction or branches; no extraction needed. |
| 13 MATHLIB | Five actual methods performed; partial cancellation matches, no full replacement established. See raw search records below; compiled generic-route probe pending. |
| 14 JUNK DEF | n/a: lemma, not data. |
| 15 EXISTS | n/a: equality, not trivial existential witness wrapper. |
| 16 SHOW | None. |
| 17 PUSH_NEG | None. |
| 18 GENERALISE | Effective τ already universe polymorphic, both ambient finite/decidable instances omitted. Probe all three propositions; concrete-to-abstract ring/field proposal requires compiled evidence. |
| 19 INEQUALITY | `hg : g ≠ 0` is disequality; no ordered inequality anywhere in type/proof. No rewrite. |
| 20 NORMAL FORM | Multiplicative separated product, standard map/rename/aeval APIs. |
| 21 SYNTAX GEN | hUmap and hF are directly rewritable equalities; no bundled predicate to unbundle. |
| 22 IMPORT FANOUT | No new import required. |
| 23 CASTS | No cross-type casts; MvPolynomial ascriptions fix aeval's codomain and constant-one polynomial type. Probe redundant ones if editing. |
| 24 INSTANCE NAME | n/a: no instance declaration. |

Literature exemption: this is a private implementation helper, not a public result;
Phase 2.6d explicitly requires literature searches for public declarations. Its sole purpose
is to move a nonzero rational scalar between factors of an existing factorization.

Initial issues: verification and width artifacts only; no identified mathematical defect.
No source change is yet proposed. No new helper authorized or needed.

## Actual search status

Raw native responses: `/private/tmp/roth-rescale-{leanfinder,loogle,leansearch,local}.json`.

| Method | Actual query and result |
|---|---|
| A Lean-Finder | `rescale polynomial product nonzero scalar inverse`: 5 hits about scaleRoots, unrelated root rescaling. |
| B Loogle | `mul_inv_cancel₀`: exact generic GroupWithZero cancellation hit. |
| C LeanSearch | `rescale a product of polynomials by a nonzero rational scalar and its inverse`: 5 hits, including Polynomial.div_C_mul, not this multivariate map/rename product. |
| D Source | rg in Algebra/MvPolynomial, Algebra/Polynomial and GroupWithZero/Defs for rescale, mul_inv_cancel, smul_eq_C_mul: actual building-block hits, not an established full equivalent. |
| E Name pattern | `mul_inv_cancel₀`: cancellation and left/right variants found; index warming, so no absence claim from empty results. |

Auxiliary variants: mul_inv_cancel_left₀, mul_inv_cancel_right₀, smul_eq_C_mul,
Polynomial.div_C_mul. Common-equivalents table: no matching discrete/finite/topology bucket.
Six strict replacement rules: no exact equivalent established; helper is not merely 1–3
API calls (rewrites across two polynomial APIs plus a cancellation certificate and a ring
combination); no custom predicate; no replacement or import/docstring expansion warranted.
Search establishes partial matches, not certified global absence.

## Applied change and step-back review

The inversion check found that integer coefficient maps occur only as opaque input
expressions: no step uses integrality or any special property of ℚ. A separately compiled
prototype `/private/tmp/roth-rescale-general.lean` therefore generalized ℚ to an arbitrary
field K and replaced mapped integer polynomials by arbitrary K-polynomials U,F. Applied
this private-only generalization after notifying the parent. No public contract or
documentation changed; the sole call `rescale_separated_factor_aux hg hUmap hF` elaborates
unchanged, inferring the mapped polynomials. No helper was added.

The proof retains its five-line structure: normalize map/rename/aeval, establish scalar
inverse cancellation as a polynomial equality, multiply that certificate by the remaining
product. This is clearer and cheaper than broad automation and already under the length
bar. Inlining into the main result would obscure its integrality argument and lengthen its
11-line body. No new public API or abstraction layer is needed.

## All 42 golf rules

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl. |
| 1.3 | n/a: no rw followed by exact. |
| 1.4 | n/a: no simp followed by exact. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | n/a: equality, no constructor. |
| 1.7 | n/a: no apply/exact sequence. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | n/a: no source lambdas. |
| 1.10 | Retain single anonymous have: explicit inverse-cancellation certificate; attempted term/simpa alternative reached recursion depth. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: have is equality, no conjunction projections. |
| 1.14 | Already merged initial rewrites; inner rw proves separate certificate. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | Already `this.symm`; remaining API constants have no useful receiver notation. |
| 1.18 | n/a: no trailing lambda/by argument parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential conclusion. |
| 2.1 | Actual standalone native grind probe failed with the unreduced product equality. |
| 2.2 | n/a: no source grind to absorb predecessors. |
| 2.3 | Actual standalone simp and rewrite+simp probes left inverse-constant product goals; term/simpa variant hit recursion depth. |
| 2.4 | n/a: no analytic function property. |
| 2.5 | n/a: no ordered positive goal. |
| 2.6 | n/a: no monotone inequality. |
| 2.7 | n/a: no natural/integer linear arithmetic goal. |
| 2.8 | Actual standalone aesop probe exhausted search and left scalar-product equality. |
| 2.9 | n/a: symbolic field scalar, not numeric/cast normalization. |
| 2.10 | n/a: arbitrary polynomial identity, not finite decidable computation. |
| 2.11 | n/a: inverse scalar is embedded under C, not field division in the polynomial ring; the existing cancellation certificate is the direct algebraic route. |
| 2.12 | Already explicit linear_combination of the inverse certificate; no terminal ring requiring conversion. |
| 2.13 | n/a: no symmetric case branches. |
| 2.14 | n/a: no calc block. |
| 2.15 | n/a: one equality goal, no parallel subgoals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega or lia. |
| 3.4 | n/a: no rcases/rfl substitution. |
| 3.5 | No attribute: a private one-use implementation step should not enter global automation. |
| 3.6 | n/a: no simp_all. |
| 3.7 | n/a: no limit option. |

Actual native standalone tactic responses are
`/private/tmp/roth-rescale-probe-{exact,grind,aesop,simp,rewriteSimp,term}.json`.
The generic-route `exact?` probe exhausted the default 200000 heartbeat budget; this
does not certify absence. An initial live multi_attempt targeted a continuation line
inside an rw list and produced parser errors, so its results were discarded, retained
honestly at `/private/tmp/roth-rescale-invalid-live-probes.json`, and replaced by the
standalone probes above. No native probe inserted sorry/native_decide/limits into source.

## Binder/generalisation audit

| Effective binder | Probe / mathematical reason | Result |
|---|---|---|
| τ : Type* | Arbitrary universe; no finite/decidable instance appears in independent copied type/proof. Removing τ with autoImplicit false makes polynomial variable types ill-formed. | Retain universe-polymorphic variable type. |
| ambient Fintype τ | Already omitted; independent original/final copies compile without it. | Absent. |
| ambient DecidableEq τ | Already omitted; independent original/final copies compile without it. | Absent. |
| K : Type* | ℚ replaced by arbitrary field K in compiled prototype and repository helper. | Generalized/applied. |
| Field K | Drop and DivisionRing candidates tested in isolated copies; the latter cannot supply CommSemiring K required by MvPolynomial; dropping field also loses Inv/Semiring. | Retain. |
| U' | Both input scalar relation and factorization use this polynomial; dropping its declaration with autoImplicit false is ill-formed. | Retain. |
| U | Original map(Int.castRingHom ℚ) U generalized to arbitrary target polynomial; dropping binder leaves unknown U. | Generalized/applied. |
| V' | Evaluated polynomial and rescaled polynomial both use it; drop leaves unknown V'. | Retain. |
| F | Original mapped integer F generalized to arbitrary target polynomial; drop leaves unknown F. | Generalized/applied. |
| g | Appears in scalar hypothesis and inverse rescaling; drop leaves unknown g. | Retain. |
| hg : g ≠ 0 | Copied-proof drop fails at inverse cancellation; compiled counterexample g=0,U'=1,U=0,V'=1,F=1 satisfies remaining hypotheses and violates conclusion. | Necessary; retain. |
| hUmap | Copied-proof drop fails at rw; compiled counterexample g=1,U'=1,U=0,V'=1,F=1 satisfies other hypotheses and violates conclusion. | Necessary; retain. |
| hF | Copied-proof drop fails at rw; compiled counterexample g=1,U'=U=1,V'=1,F=0 satisfies other hypotheses and violates conclusion. | Necessary; retain. |

Compiler drop-test records: `/private/tmp/roth-rescale-binder-*.lean/.log` for all
data/type/class binders; `/private/tmp/roth-rescale-drop-{hg,hUmap,hF}.lean/.log` for
propositions. Native compiled counterexamples: `/private/tmp/roth-rescale-counterexamples.json`
(success=true, no errors; scratch-only line-width warnings and transient import-refresh info).
Point-localisation, strict-to-weak, unbundling: n/a, since there are no function-property,
order, or conjunction hypotheses. Field-to-DivisionRing is a real checked failure, not an
untested mathematical claim. No claim of maximally general algebraic hierarchy is made:
replacing inverse-field syntax by units would require a different statement, offering no
local caller benefit. Literature exemption remains applicable after private generalization.

## Width and inequality artifacts

Initial type was independently printed at `format.width 100` in
`/private/tmp/roth-rescale-independent.log`. Final independent `#check @rescaleFinal`
at `format.width 100` is in `/private/tmp/roth-rescale-final-independent.log`.
Final measured signature (Unicode codepoints, including indentation):

| Line | Width | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 451 | 90 | `{V' : Polynomial K}` (20) | 90+1+20=111 | ok |
| 452 | 97 | hF binder plus colon (86) | 97+1+86=184 | ok |
| 453 | 90 | conclusion lhs `F = rename some U` (17) | 90+1+17=108 | ok |
| 454 | 77 | final evaluation argument and `:= by` (29) | 77+1+29=107 | ok |
| 455 | 35 | no next signature unit | n/a | ok |

| Inequality occurrence | Orientation | Action |
|---|---|---|
| hg : g ≠ 0 | Disequality, not an order relation | retain |
| Rest of signature/proof | No ≤,<,≥,> comparisons | none |

Ascription audit: aeval's `(X none : MvPolynomial (Option τ) K)` fixes its target algebra;
`(1 : MvPolynomial (Option τ) K)` fixes C's variable type in the cancellation certificate.
No coercion tower or redundant same-type cast added. No unused instance name introduced.

## Verification artifacts and gates

Initial complete native module LSP: `/private/tmp/roth-rescale-lsp.json`.
Final complete unfiltered native module LSP: `/private/tmp/roth-rescale-final-lsp.json`:
partial=false, timed_out=false, success=true, failed_dependencies=[], 0 errors, 3 warnings,
0 infos/hints. Warnings are the preserved header and public30's two ambient instances;
there is no helper warning. Public30 remains outside this audit's authority.

Actual initial/final module builds:
`/private/tmp/roth-rescale-build.log`, `/private/tmp/roth-rescale-final-build.log`;
both `lake build Roth.Separation` exit 0 (1876 jobs).

Exact INITIAL helper type, independent NON-SELF proof: copied into
`/private/tmp/roth-rescale-independent.lean`, no invocation of the source helper;
compile exit 0. Final rerun `/private/tmp/roth-rescale-final-axioms.log` independently
reproves that exact type and checks the ACTUAL BUILT helper, exists_int_factors, and
exists_det_eq_mul: only propext, Classical.choice, Quot.sound. Private constant found by
exact suffix traversal of the built environment, not guessed numeric name components.
Final generalized helper also independently compiled in
`/private/tmp/roth-rescale-final-independent.lean/.log` with the same standard axioms.

| Gate | Status/evidence |
|---|---|
| lake_build_file | PASS, actual final module build exit 0. |
| definition_protected | PASS, no def/abbrev changed. |
| theorem_statement_protected | PASS, sole authorized private generalization; all public signatures unchanged. |
| structure | PASS, helper proof 5 lines, main29 proof 11 lines; no branches/conjunction. |
| naming | PASS, mathematical snake_case private `_aux`, no forbidden patterns. |
| line_packing | PASS, all five final signature lines measured above. |
| inequality_orientation | PASS, no reversed order relation. |
| comments/docs | PASS, no narrative/documentation changes. |
| no unintended caller breakage | PASS, main29 unchanged and actual module build includes main29/caller30. |
| no suspicious source changes | PASS, no sorry, axiom, native_decide, limit, instance-binding or profiler scaffolding added. |
| whole project / LeanEval / commit / push | Parent's cumulative final gates; not claimed by this worker. |

Arithmetic: dispatched file 562 lines → 561 (-1); retained declaration count 27 unchanged.
Target initial 11 physical declaration lines → final 10 (-1); proof body 5 → 5.
No newly added helper, rename, public proposal, import, or caller adjustment.

## Eleven completion steps

1. Read target, baseline and worker contract; preserve public contracts/header/docs.
2. Read Lean/mathlib skills, full golf/proof-pattern references, search/generalisation/
   gates, relevant style/naming/profiling instructions.
3. Record initial 24-item audit before edits (top of this report).
4. Execute actual five-method search, auxiliary variants and compiled generic-route probe.
5. Audit every effective binder, private literature exemption, order and width tables.
6. Apply only the compiled private generalization; unchanged caller elaborates.
7. Record all 42 golf rules and actual failed automation/term probes.
8. Step-back simplify review: preserve short transparent cancellation proof; no new helper.
9. Compile independent initial/final proofs and actual built target/main29/caller30 axioms.
10. Complete module build, unfiltered LSP and actual anchored performance checks.
11. Drain all requests, record final SHA, revoke all source ownership and report only.

## Actual performance and final freeze

Accepted baseline actual-module logs supplied with dispatch:
`/private/tmp/roth-d29-{final,repeat}-profile.log(.json)`.
Fresh actual-module sweeps, both exit 0:
`/private/tmp/roth-rescale-final-profile.log(.json)` and
`/private/tmp/roth-rescale-drained-profile.log(.json)`.
The latter began after ALL binder, native MCP, independent-proof and compiler requests
had completed and is the **only accepted final timing sample**. The earlier `final-profile`
sweep overlapped binder probes and is listed only as provisional historical evidence;
its measurements are not used to pass the final performance gate. Command used exactly:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`.
Parser: `/private/tmp/roth-separation-profile-table.py`; only outer Elab.command and
outer Elab.async proof anchors count, using the maximum enclosing command to avoid
double-counting nested private/omit expansion commands. No extracted-namespace timing.

| Actual declaration | Baseline / repeat total ms | Fresh / drained total ms | Drained outer command + proof ms |
|---|---:|---:|---:|
| rescale_separated_factor_aux | 499.121 / 513.159 | 508.500 / 521.669 | 55.345 + 466.324 |
| exists_int_factors | 498.457 / 486.618 | 423.382 / 484.287 | 74.209 + 410.078 |
| exists_det_eq_mul | 511.974 / 536.891 | 449.816 / 583.871 | 123.759 + 460.112 |

Buzz status: target and affected callers below 750 ms in the accepted drained sweep; no ≥1000 ms
fix obligation, no limit increase, no profiler scaffolding. Timing variation provides no
claim of performance improvement or whole-project improvement. Other declarations outside
this worker's authority remain for the parent's cumulative performance audit.

Final exact comparison `/private/tmp/roth-rescale-diff.patch` shows only the audited
private helper changed against the first-freeze baseline; main29, caller30, all definitions,
public contracts and docs are unchanged. All Lean/MCP/compiler/profile requests have now
completed: none remain running or pending. No source edit followed the final profiling sweep.

Frozen source SHA256:
`416818ba201bb2ffbd465d7f8f73750f7cb13f769c3df5e70457f562c8c7da02`.

**I revoke ALL source ownership and am report-only.** Parent owns subsequent source work,
cumulative gates, project/LeanEval builds, exact-path commit and successful push. No
pending proposal, blocker, new helper, Git mutation or publication is claimed by this audit.
