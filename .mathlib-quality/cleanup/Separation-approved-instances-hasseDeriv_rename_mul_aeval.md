# Approved instance removal: `Roth.hasseDeriv_rename_mul_aeval`

Fresh revisit at HEAD `d1880c7`. I have read golfing-rules.md, proof-patterns.md,
mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, both skills,
cleanup Phase 4, and relevant style/naming/profiling references. This initial audit
is written BEFORE any source edit. Earlier report informs unchanged reasoning only;
all verification for this approved change is fresh. User approval explicitly covers
removing BOTH `[Fintype τ]` and `[DecidableEq τ]` on this theorem. Other public
contracts, both wrappers, docstrings and metadata remain protected.

## Initial 24-item audit

| # | Item | Assessment/action |
|---|---|---|
| 1 | Lint | Complete native baseline LSP: 0 errors / 20 warnings; target contributes three unused instance warnings. Remove the approved instances and recheck unfiltered. |
| 2 | Have scan | `hnone` has proof content and two uses, retain. `hdisj` is a single-use named support partition; inlining would obscure derivative composition, retain for this minimal approved pass. |
| 3 | Options | None; no limits or suppression allowed. |
| 4 | Simp | `simp` proving `hnone` and both degree side goals are terminal, unsqueezed. |
| 5 | Naming | Describes Hasse derivative, renaming, multiplication and evaluation; no forbidden scheme/abbreviation. No rename. |
| 6 | Packing | Four signature lines, widths 100/91/95/76; measure final unchanged signature table. |
| 7 | By | All introducing `by` at end of line. |
| 8 | Format | Two-space indentation, ordinary lambdas use `↦`, no blank body lines. |
| 9 | Comments | No inline comments; preserve source prose verbatim. |
| 10 | Docstring | Existing factorwise statement and source reference preserved byte-for-byte. Place `omit` BEFORE it. |
| 11 | Visibility | Public result used by `det_hasseDeriv_separated`; retain. |
| 12 | Structure | 15 body lines, not listed headline result; no conjunction or long branches. Local `classical` increases body to 16, still within 60. |
| 13 | Mathlib | Fresh five methods below; separated multivariate proof uses project derivative API plus mathlib degree/renaming. |
| 14 | Junk def | n/a theorem. |
| 15 | Exists | n/a no existential. |
| 16 | Show/change | Neither in target. |
| 17 | Push neg | Neither in target. |
| 18 | Generalise | Approved omit both, local classical if necessary. Fresh arbitrary-type exact proof and every effective binder probe. Preserve CommSemiring and Nat orders. |
| 19 | Inequality | No order comparison; `o ≠ none` is disequality; arrows are not inequalities. |
| 20 | Normal form | Canonical derivative at disjoint sum equals product of component derivatives. |
| 21 | Syntax generality | Rewrite-ready equality; arbitrary factors and derivative orders. Abstract embeddings would be different API, not this approved scope. |
| 22 | Import fanout | No new import. |
| 23 | Casts | No casts; two `X none` target ascriptions are load-bearing. |
| 24 | Instance naming | No instance declarations; omitted ambient classes anonymous. |

Issues/actions: add scoped `omit [Fintype τ] [DecidableEq τ] in` before original
docstring and `classical` at proof start, then fresh exact type, independent proof,
original explicit-class adapter, caller/axiom/LSP/build/profile checks. No helper planned.

## Fresh five-method search and literature

| Method | Actual query/result |
|---|---|
| Lean-Finder | “Hasse derivative of separated product with disjoint variables”: remote read timeout; unavailable, no absence claim. |
| Loogle | Initial malformed two-string query failed; corrected `Polynomial.hasseDeriv, _ * _` returns `hasseDeriv_mul`, `_coeff`, `_apply`, `_monomial`; univariate partial match. |
| LeanSearch | “Hasse derivative product disjoint variables” returns univariate `Polynomial.hasseDeriv_mul` and ordinary derivative product rules. |
| Source grep | `hasseDeriv|degreeOf_rename` in local HasseDeriv and mathlib polynomial HasseDeriv/degrees files, raw `/private/tmp/roth-separation-r06-source-search.log`; project disjoint composition/factor API supplies the proof. |
| Name pattern | Native `hasseDeriv` search returns `_rename`, `_single_aeval_X`, `_hasseDeriv_of_disjoint`, `_mul_of_degreeOf_eq_zero`; index unavailable, positive source hits only. |

Raw first four native results: `/private/tmp/roth-separation-r06-search.json`.
Corrected Loogle result appears in this turn's complete native transcript. Auxiliary
variants inspected: `_rename`, `_mul`, `_coeff`, `_of_disjoint`, `_single_aeval_X`.
Common-equivalents catalogue has no matching bucket. Partial matches support existing
proof; this is not a one-to-three-mathlib-call wrapper. No new helper/API is introduced.
Fresh live `exact?`/`apply?` each hit existing 200000-heartbeat limit; these are failed
search probes, not evidence that no replacement exists. No limit changed.

Public literature query “Hasse derivative multivariate product rule disjoint variables
generalization” returned the Sydney thesis *Algorithmic Aspects*, the canonical Hasse
derivative entry, and [ECCC 2024/069](https://eccc.weizmann.ac.il/report/2024/069/download/).
Also opened [Bhandari–Harsha–Kumar–Sudan, §3.2](https://eccc.weizmann.ac.il/report/2020/179/download).
Coefficient extraction and Hasse product rules explain factorwise differentiation when
variable groups are disjoint. The inference here is that finite support of each polynomial
and multi-index suffices; a finite ambient index type is unnecessary. No characteristic-zero,
division, field or nonzero-factor hypothesis is required by our semiring proof. A second
query “site.ncatlab.org nlab Hasse Schmidt derivation” returned
[the canonical Hasse–Schmidt formulation](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivation),
its derivative redirect and derivation entry. ChatGPT math MCP unavailable: no callable tool.
Abstract disjoint embeddings are a possible separate theorem, outside this approved removal.
Inversion check: factors/orders already arbitrary; `some`/`none` remain essential throughout
the proof, so no hidden concrete witness is abstracted away. No new public proposal.

## Width and inequality tables

Actual `#check @Roth.hasseDeriv_rename_mul_aeval` runs at `format.width 100` in
`/private/tmp/roth-separation-r06-independent.lean` and the native fixed proof JSON.
It explicitly prints only `{τ} {R} [CommSemiring R]` before `d ν U V`.

| Signature line | Codepoints | Next syntactic token/argument | Arithmetic | Action |
|---|---:|---|---|---|
| 140 | 100 | `hasseDeriv` (10) | 100 + 1 + 10 = 111 | ok |
| 141 | 91 | `(X none : MvPolynomial (Option τ) R)` (36) | 91 + 1 + 36 = 128 | ok |
| 142 | 95 | `(X none : MvPolynomial (Option τ) R)` (36) | 95 + 1 + 36 = 132 | ok |
| 143 | 76, including `:= by` | no following signature line | n/a | ok |

Initial and final signature text is identical; only scoped omission and proof-local
classical were added. Parenthesized target annotations are kept as intact arguments.

| Location | Occurrence | Action |
|---|---|---|
| Statement and all binders | No `≥`, `>`, `<`, `≤` order propositions | n/a |
| `hnone` | `o ≠ none` | Disequality retained |
| Types/lambdas | `→₀`, `→`, `↦` | Arrows, not inequalities |

No `_ge_` or `_gt_` name; no rename queue entry.

## All 42 golfing rules, fresh review

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: not a reflexivity proof. |
| 1.3 | n/a: rw closes, no trailing exact. |
| 1.4 | n/a: no simp-then-exact pair. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor block. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no by_contra. |
| 1.9 | Lambdas consume support hypotheses, none eta-reducible. |
| 1.10 | `hnone` reused twice; `hdisj` names precise dependent support partition. Retain both for readability and minimal approved change. |
| 1.11 | n/a: no apply/intro pair. |
| 1.12 | n/a: no redundant show. |
| 1.13 | n/a: no projected existential. |
| 1.14 | Existing one rewrite chain; inner rw belongs to distinct degree side goal. |
| 1.15 | All three scoped terminal simp calls unsqueezed already. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Existing `.2`, `.1` projections concise; no clearer dot rewrite. |
| 1.18 | n/a: no avoidable trailing tactic parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Fresh live grind failed on derivative identity. |
| 2.2 | n/a: no retained grind. |
| 2.3 | Fresh live simp made no progress on whole identity; scoped terminal simplifications already concise. |
| 2.4 | n/a: no analytic function property. |
| 2.5 | n/a: no positivity goal. |
| 2.6 | n/a: no inequality/monotonicity goal. |
| 2.7 | n/a: no arithmetic comparison. |
| 2.8 | Fresh live aesop made no progress on derivative identity. |
| 2.9 | n/a: no concrete arithmetic or numeric casts. |
| 2.10 | n/a: symbolic polynomial equality over arbitrary types is not finite computation. |
| 2.11 | n/a: no denominators, CommSemiring cannot support field_simp. |
| 2.12 | n/a: no ring-ending block/equality hypotheses. |
| 2.13 | n/a: no symmetric case branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: rewrite side goals differ; no repeated parallel goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases-rfl substitution. |
| 3.5 | No attribute added: explicit specialized rewrite in determinant proof; global automation changes outside scope. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no limits present or introduced. |

Step-back review: a coefficient-level proof would reconstruct convolution rather than use
the existing disjoint-support API. Whole grind/simp/aesop fail, exact?/apply? hit the existing
limit. Live line replacement also leaves the original nested block as an expected parser
leftover; full compiled independent proofs below are authoritative. Maintain the two support
facts and one rewrite chain. Term-mode inlining would obscure those facts. No helper is added.

## Effective-binder generalisation probes

All scratch sources use `autoImplicit false`. They reproduce the statement and an independent
non-self proof, using explicit shared universes `u v`. Prefix for sources/logs is
`/private/tmp/roth-separation-r06-`; result manifest `probes.json` records actual exits.

| Effective binder | Mechanical candidates and evidence |
|---|---|
| `{τ : Type*}` | Already universe-polymorphic. `drop_tau` and `sort_tau` test deletion and Sort weakening; polynomial/Finsupp domains require Type. No artificial universe identification imposed. |
| `[Fintype τ]` | `drop_fintype`, `drop_both`, and `finite` test no finiteness / Finite replacement; complete omission is the weakest successful form and explicitly approved. |
| `[DecidableEq τ]` | `drop_deceq` / `drop_both`; local classical handles finite supports. Explicitly approved omission applied. |
| `{R : Type*}` | Already independent universe. `drop_R` and `sort_R` test omission and Sort; polynomial coefficient objects require Type. |
| `[CommSemiring R]` | `drop_class` and `semiring` test omission/weakening. Missing required CommSemiring at expression elaboration; retain. Non-unital/non-associative ancestors cannot supply required polynomial/aeval structure; not separately compiler-tested. |
| `(d : τ →₀ ℕ)` | `drop_d` tests deletion: unknown d. Arbitrary finitely supported natural derivative order, no smaller assumption. Generic exponents require changing Hasse API/mathematics. |
| `(ν : ℕ)` | `drop_nu` tests deletion: unknown ν. Arbitrary natural derivative order, fixed by Polynomial.hasseDeriv API. |
| `(U : MvPolynomial τ R)` | `drop_U` tests deletion: unknown U. Arbitrary factor, no nonzero/degree/monicity hypothesis. |
| `(V : Polynomial R)` | `drop_V` tests deletion: unknown V. Arbitrary factor, no support/nonzero hypothesis. |

No proposition assumptions, strict inequalities, continuity/localization, bundled
injectivity or fixed finite index set to weaken. Natural codomain is preserved.
Actual compiler outcomes: independent, drop_fintype, drop_deceq, drop_both and finite all
exit 0. Semiring/drop_class, both Sort probes, both type deletions and all four data-binder
deletions exit 1 with genuine typeclass/Type-vs-Sort/unknown-identifier diagnostics. All
probe jobs drained before the final profile; no negative result is inferred from timeout.

## Fresh exact type, independent proof and original adapter

`/private/tmp/roth-separation-r06-independent.lean` contains:

1. An independent proof over arbitrary τ, with no Fintype/DecidableEq instance binders,
   reproducing the source derivative argument without invoking the target.
2. An exact arbitrary-τ statement instantiated from the actual built target.
3. An original-context adapter retaining `[Fintype τ] [DecidableEq τ] [CommSemiring R]`.
4. A fully explicit adapter supplied the original `τ ft de R cs d ν U V` arguments.
5. `#check @` at `format.width 100` and actual target/caller/independent axiom checks.

First scratch native bundle failed because separate `Type*` binders inside adapter lambdas
introduced unrelated universes. Preserved failure:
`/private/tmp/roth-separation-r06-native-independent.json`. Corrected shared-universe bundle
passes natively (`success=true`, `timed_out=false`), raw
`/private/tmp/roth-separation-r06-native-independent-fixed.json`; six long-line warnings are
scratch-only and no warning is suppressed. Exact printed signature has only `{τ} {R}` and
`[CommSemiring R]`. Actual retained target, actual determinant caller and independent proof
each report exactly `[propext, Classical.choice, Quot.sound]`.

Direct-call scan `/private/tmp/roth-separation-r06-callers.log` finds only
`Roth.det_hasseDeriv_separated` in this module. There is no direct external caller requiring
an additional file build/LSP check. The actual module build covers the real caller, and its
axioms are checked from the built environment. Caller source/public contract is unchanged.

## Verification gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exit 0, 1876 jobs,
`/private/tmp/roth-separation-r06-build.log`. Complete unfiltered native LSP raw
`/private/tmp/roth-separation-r06-lsp.json`: partial=false, timed_out=false, success=true,
failed_dependencies=[], **0 errors / 18 warnings**. Target's three unused-instance warnings
disappear; one newly exposed unused-section warning occurs in determinant caller, whose
contract is intentionally protected until its own approved pass. No warnings suppressed.

| Gate | Result/evidence |
|---|---|
| lake_build_file | Pass: actual module build exit 0. |
| definition_protected | Pass: no definition/abbrev edits. |
| theorem_statement_protected | Pass with exact user approval: omit two effective instance binders, statement tokens otherwise identical to original snapshot. |
| structure_gate | Pass: 16 body lines, 20 keyword-to-body declaration lines, no conjunction/branches. Not a module headline result. |
| naming_gate | Pass: operation-based descriptive name, no forbidden pattern or rename. |
| line_packing_gate | Pass: all four measured rows above justify breaks. |
| inequality_orientation_gate | Pass: no reversed order comparison. |
| comments/docs | Pass: docstring byte-identical to original snapshot and immediate HEAD. |
| import/cast/instance | Pass: no import change, two load-bearing target annotations retained, no named/global instance. |
| cumulative caller check | Module build, complete LSP and actual determinant axioms pass; no external direct caller. Parent owns full-project/cumulative-original checks. |
| scaffolding | Pass: no sorry, new axiom, native_decide, limits, haveI/letI, suppression or profiling scaffold. |

`git diff --check` passes. Source diff exactly **2 additions / 0 deletions**: scoped omit and
local classical, entirely in owned target. Module **578 → 580**, theorem **19 → 20** lines,
proof body **15 → 16**, scoped command adds one further source line. No helper created.
Original docstring and statement tokens compare equal by actual extraction; original
explicit-class call compatibility is provided by the compiled adapter above.

## Actual repository performance

Supplied immediate baseline `/private/tmp/roth-separation-r05-profile.log(.json)`:
outer target command 44.929 ms + outer async proof 353.707 ms = **398.636 ms**.
Final actual-module command (all search/MCP/compiler probe jobs drained beforehand):

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Raw `/private/tmp/roth-separation-r06-profile.log`, parser
`/private/tmp/roth-separation-profile-table.py`, parsed table raw-log path plus `.json`.
Target anchors: outer command **40.276 ms**, outer async proof **341.592 ms**, conservative
total **381.868 ms**. Two outer command anchors (scoped omit wrapper plus inner declaration)
are combined by maximum; one outer async proof anchor. Nested timings are not double-counted.
Below 750 ms repeat threshold and 1000 ms budget. No speedup claim from these wall-clock samples;
the useful outcome is the approved assumption weakening and elimination of target warnings.

Final profile compiler exited **0**; final parser rerun confirms the same target anchors.
Actual unchanged determinant caller: command 84.137 ms + async proof 405.262 ms =
**489.399 ms** (one command and one proof anchor), also below threshold.

## Eleven completion steps and freeze

- [x] Step 1: both skills and required reference material read.
- [x] Step 2: full initial 24-item audit written before source edit.
- [x] Step 2.5: five actual search methods; remote failures reported honestly.
- [x] Step 2.6: all effective binders, actual compiler probes, public literature and inversion check.
- [x] Step 2.7: all signature lines measured, actual format.width 100 #check.
- [x] Step 2.8: per-occurrence inequality table.
- [x] Step 3: all 42 golf rules reviewed with concrete statuses.
- [x] Step 4: fresh whole-proof automation and alternate-strategy review.
- [x] Step 5a: complete unfiltered native LSP, actual module build, exact new type/independent
  proof, explicit original-class adapters, actual target and caller standard axioms.
- [x] Step 5b: focused diff/doc/signature gates and actual repository timing anchors.
- [x] Step 6a: no rename required; parent owns shared logs, Git and cumulative publication gates.

ALL Lean/MCP/compiler/search/profile requests are drained. No helper has been created and
no concrete public proposal or user input remains pending for this declaration.
**ALL source ownership is revoked; this worker is report-only. No further source edit follows.**
Frozen `Roth/Separation.lean` SHA256:
`187f69cba6b1e16d665130375348c4038f3aa5cd7a3cb8d650e3e055b2a5bf7d`.

Parent owns the fresh whole-original/all-public/all-retained checks, sequential full project
and separate LeanEval builds, exact-path commit and successful push before the next source edit.

## Owner cumulative publication gates

Source FROZEN SHA256 `187f69cba6b1e16d665130375348c4038f3aa5cd7a3cb8d650e3e055b2a5bf7d`; leaf ownership revoked and requests drained before owner gates. Owner probe `98402` exit0,43.30s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r06-compatibility.{lean,log,json}`. Owner build session `84517` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.76s/28.80s; source hash stable. `/private/tmp/roth-separation-r06-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
