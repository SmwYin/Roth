# Roth.index_mul_left_weights — fresh declaration audit

Checkpoint: `ramin-cleanup`, incoming HEAD `3994c03`; target only, originally Index:205–212,
now 206–213. Read the leaf contract and lean4/mathlib-quality skills; cleanup.md in full,
cleanup-all worker contract, golfing rules, proof patterns, search, generalisation, gates,
relevant style sections, naming, review stages, profiling and buzz references.

Applied the two separately approved API changes: omit sigma `DecidableEq` before the
preserved docstring, and remove unused explicit `hl : 0 < l`, retaining `{l : ℕ}`.
Packed parameters and normalized three lambda arrows. No other declaration changed.
Declaration 8 → 8 lines; file 265 → 266 because the scoped `omit` adds one line; 19 retained.
Existing docstring byte-identical; inline proof comments 0/0; outside-target bytes identical.
No helper, rename, import, attribute, option, axiom or definition added.

Frozen Index SHA256: `c7ecc3d5d361a6f72515e0b4b400045466f6b79da07159eb003eca394addc402`.
SOURCE AUTHORITY RELEASED; owner acknowledged revocation. Every compiler/native request
finished before release. This report was written afterward without further Lean/source/build work.

## Audit: all 24 items

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | Baseline two target unused-DecidableEq warnings; both resolved. Complete final diagnostics contain zero target warnings/errors. |
| 2 | Have scan | Only `himg`, explicit `:= by`, used once by final rewrite; retains mathematical proof content, keep. |
| 3 | Set option | None in target; no limit raises. |
| 4 | Simp squeeze | No simp in retained proof. Alternative terminal simp leaves scalar-image sInf goal; guarded CLI verifies failure to close. |
| 5 | Naming | `index_mul_left_weights`: snake_case; subject index, operation multiplication of left weights; no forbidden abbreviation, digit scheme, `_ge_` or `_gt_`. No rename needed. |
| 6 | Line packing | Both signature lines measured below; final width100 built #check provided. |
| 7 | By placement | Signature and `himg` both end in `:= by`. |
| 8 | Format | Two-space tactics, four-space signature continuation, no internal blank line, no haveI/letI; three lambdas changed to ↦. |
| 9 | Comments | No inline comments to remove; docstring preserved literally. |
| 10 | Docstring | Existing source/scaling statement retained by explicit preservation requirement; no prose rewrite. |
| 11 | Visibility | Public API has two Theta uses; keep public. Classic import dialect. |
| 12 | Structure | Six body lines, `himg` branch three tactic lines; no conjunction, no long branch; no decomposition. |
| 13 | Mathlib | Five actual methods below; generic scalar sInf API found and used. Exact target is project-specific index, not an existing direct generic lemma. |
| 14 | Junk def | n/a: theorem, no data definition. |
| 15 | Exists lemma | n/a: equality theorem, no existential wrapper. |
| 16 | Show/change | Neither in retained proof. Alternative change pins scalar-set notation; not needed in source. |
| 17 | Push neg | None. |
| 18 | Generalise | Every binder table below; approved DecidableEq and hl removal verified. Strongened theorem covers l=0. |
| 19 | Inequality | No reversed inequalities; table below. Original hl had correctly oriented `0 < l`. |
| 20 | Normal form | `index scaled = index / l` is the useful rewrite form; uses existing weight scaling and real sInf scalar API. |
| 21 | Syntax generality | Dropping hl makes rewrite usable without positivity, including zero; original formulas/P/α/r unchanged. |
| 22 | Import fanout | n/a: no new imports. |
| 23 | Casts | Zero dropped; `(l : ℝ)` kept as cross-type cast/load-bearing scalar type. No new coercion in diff. |
| 24 | Instance name | n/a: no instance declaration introduced or modified. |

## Mathlib search: five actual methods

All direct MCP helpers were bounded (45 seconds for remote searches). Remote failure means
unavailable, never evidence of absence. Artifacts use prefix `/private/tmp/roth-index-scale-`.

| Method | Actual query | Result/evidence |
|---|---|---|
| A LeanFinder | `infimum of a set multiplied by a nonnegative real scalar`, 3 results requested | DNS unavailable; `lean_leanfinder.json`. |
| B Loogle | `Real.sInf (_ • _)`, 3 requested | DNS unavailable; `lean_loogle.json`. |
| C LeanSearch | `infimum scales by nonnegative real multiplication`, 3 requested | DNS unavailable; `lean_leansearch.json`. |
| D Source rg | Full `sInf_smul_of_nonneg` across mathlib; also sInf_mul/image_smul in order files; weight_mul_left in Box | Positive: Mathlib/Basic/Real/Pointwise.lean:41, plus consumers Gauge:269/295. Its source explicitly handles empty sets and scalar zero. |
| E Native local search | `sInf_smul`, limit10 | Positive: `Real.sInf_smul_of_nonneg`, `Real.sInf_smul_of_nonpos`; index unavailable but source results positive, `lean_local_search.json`. |

Auxiliary variants: nonneg/nonpos, image_smul/image_image/image_congr, weight_mul_left.
Common-equivalents catalogue: no discrete/compact/finite predicate match; order/scalar
API is the relevant abstraction. Compiled #checks in `recovery.log` verify every used
lemma. No new source identifier beyond syntax `omit`/↦. The generic sInf result is
already used directly; this theorem packages index-specific weight conversion, not a
duplicate generic scalar lemma. No API helper extraction signal remains.

Actual standalone `alternatives.lean` compiles with `fail_if_success solve |` guards for
`grind [literalIndex]`, terminal `simp [literalIndex, Roth.weight_mul_left,
div_eq_inv_mul, ← Set.image_image]`, `aesop`, and `exact?`, then closes by the fresh proof.
No earlier scaling theorem is in scope in that file. Thus failures to close are checked
in a successful compilation; searches do not establish universal library absence.
Initial native multi-attempt hit continuation-line parser errors; it is not accepted
as validation. A first scratch guard used bare simp (success without closing), and a
later exact? found a preceding scratch strengthened theorem; both were corrected in
the final independent alternatives file. No failed scratch evidence is used as a gate.

## Every binder: mechanical probes

`binders.lean` has `autoImplicit false`; each negative deletion is an actual
`#check_failure` assertion in an exit0 run. Its printed error terms contain synthetic
`sorry` from intentionally rejected expressions; no admitted theorem is introduced.
Positive independent proofs and their standard axiom lists are separate artifacts.

| Binder | Class/use | Probe and result |
|---|---|---|
| `{σ : Type*}` | Universe-polymorphic variable indexing all data | Delete σ: checked unknown-identifier failure. Already Type*, no smaller-universe restriction to remove. |
| `[Fintype σ]` | Finite sum in weight/index's type | Delete: checked Fintype synthesis failure. Replace with `[Finite σ]`: same checked failure. Finite-to-Fintype reconstruction would change representation/API; not applied. |
| `[DecidableEq σ]` | Decidability, unused | Remove: strengthened independent proof and actual built #check compile without it; approved omission applied. No parent class weaker than absence. |
| `{l : ℕ}` | Scale appears on both sides | Delete with autoImplicit=false: checked unknown l. Retain implicit Nat scale. Abstract real scale needs a changed weight definition/API, beyond approval. |
| `(hl : 0 < l)` | Proposition, unused | Drop entirely: independently proved. Strict→weak `0 ≤ l`: actual fresh literal-sInf proof in binders.lean compiles; absence is weaker still. Separate l=0 cases compile independently and against actual built theorem. |
| `(P : MvPolynomial σ ℝ)` | Polynomial determining Taylor support | Delete: checked unknown P. Not a proposition/class/global regularity hypothesis; no point-localization applicable. |
| `(α : σ → ℝ)` | Point selecting Taylor expansion | Delete: checked unknown α. Already a single point; no global-to-point assumption to weaken. |
| `(r : σ → ℕ)` | Weight function used both sides | Delete: checked unknown r. No positivity assumption on r to weaken; arbitrary zero entries already supported. |

Inversion check: after weight conversion, the proof is scalar sInf preservation for an
arbitrary set; mathlib's `Real.sInf_smul_of_nonneg` already supplies that abstraction.
No new abstract wrapper needed. A real-positive weight version is literature-supported
but requires a new definition and broader public restatement; follow-up only, not applied.
No other generalisation candidate changes this checkpoint.

## Literature and first three displayed leads

Actual searches were made for the four queries below. The first two were initially
batched (pooled response), then reissued individually to obtain attributable rankings.
Q2 was repeated again with short output after a combined long output truncated; its
listed ranking is explicitly that final repeat. Only relevant primary material informs
the mathematics; irrelevant displayed leads are recorded, not cited as support.

| Query/run | #1 displayed | #2 displayed | #3 displayed |
|---|---|---|---|
| Q1 `polynomial index weights scaling Roth theorem index l r` (individual repeat) | [A quantitative version](https://citeseerx.ist.psu.edu/document?doi=33a890c43d5e72df58279f0070b4884f7dc5c504&repid=rep1&type=pdf), relevant definition | [Weighted projective lines](https://arxiv.org/abs/2610.17589), different weighted projective construction | [Ru: Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf), relevant |
| Q2 `Roth polynomial index weighted order generalization scaling` (final short repeat) | [Generalized scalings](https://www.sciencedirect.com/science/article/pii/0024379589904928), unrelated | [Quantargo transform_weights](https://www.quantargo.com/help/r/latest/packages/gpindex/0.2.5/transform_weights), unrelated | [ETH gpindex](https://www.stat.math.ethz.ch/CRAN/web/packages/gpindex/refman/gpindex.html), unrelated |
| Q3 `"Roth" "index" "scaling" polynomial weights` | [Cornell CAHRS](https://ecommons.cornell.edu/bitstreams/1d3d9139-235c-40d3-bfcf-a4d3b8702795/download), unrelated | [Nuclear production costs](https://research.cbs.dk/files/95987529/bj_rn_steigerwald_et_al_uncertainties_in_estimating_production_costs_nuclear_technologies_publishersversion.pdf), unrelated | [Strategic I/O psychology](https://citeseerx.ist.psu.edu/document?doi=57c90f4212fa5c1ba6b58e2ba155368f88c28b7b&repid=rep1&type=pdf), unrelated |
| Q4 `Roth theorem "index" "positive" "weights" polynomial` | [Ru: Roth's Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf) | [Vojta: Applications of Arithmetic Algebraic Geometry](https://math.berkeley.edu/~vojta/ftp/cime.pdf) | [Bombieri–Gubler, Heights](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MA/MAg/Bombieri%20E.%2C%20Gubler%20W.%20Heights%20in%20diophantine%20geometry%20%28CUP%2C%202006%29%28669s%29_MAg_.pdf) |

Ru defines the index by minimum normalized derivative degree with positive integer
weights. Vojta's author-hosted exposition uses positive real weights and local power
series coefficients on products of varieties. Thus reciprocal scaling for positive
scales follows from the definition; this is an inference, not a quoted separate theorem.
The local source `clean.tex:636–641` explicitly gives scaling for l>0 in extended
nonnegative reals. The approved zero-scale extension instead follows Lean's total
division and real sInf conventions, independently compiled; it is not attributed to
the positive-weight literature. No other library redesign is applied.
ChatGPT math MCP: unavailable (no corresponding tool in ALL_TOOLS).

## Complete signature line packing

Final codepoint measurements (not bytes):

| Source line | Width | First next signature expression | Arithmetic | Action |
|---|---:|---|---|---|
| 206 | 87 | `index P α (fun j ↦ l * r j)` (27) | 87+1+27=115>100 | ok |
| 207 | 55 | none; body next | n/a | ok |

Before: line205 width86 with next `(r : σ → ℕ)` (11), 86+1+11=98≤100:
repack was required; line206 width70, terminal. After approved hl deletion, r packs onto line206.
The final conclusion cannot fit on the parameter line; no residual repack row.
Actual built `set_option format.width 100; #check @Roth.index_mul_left_weights`:

```lean
@Roth.index_mul_left_weights : ∀ {σ : Type u_1} [inst : Fintype σ] {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ)
  (r : σ → ℕ), (Roth.index P α fun j => l * r j) = Roth.index P α r / ↑l
```

The check confirms both approved arguments absent and remaining arity unchanged.

## Inequality scan

| Occurrence | Location | Before | Final | Rename |
|---|---|---|---|---|
| 1 | original hl | `0 < l` | approved binder removed | none |
| — | final signature/hypotheses | no ≥ or > | no ≥ or > | no `_ge_`/`_gt_` in name |

## All 42 golf rules

| Rule | Status/evidence |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper. |
| 1.3 | n/a: no rw followed by exact. |
| 1.4 | n/a: no simp followed by exact. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: equality, no constructor pair. |
| 1.7 | n/a: no apply-exact pair. |
| 1.8 | n/a: no contradiction/negation tactics. |
| 1.9 | Lambda arguments l*r j and d-dependent goal not eta-redexes; normalize ↦. |
| 1.10 | himg has by and mathematical proof content, keep. |
| 1.11 | image_congr already uses refine with lambda; no apply-intro pair. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected conjunction/existence have. |
| 1.14 | Existing consecutive rewrite list already merged where possible; intervening refine is needed. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal bare simp in source. |
| 1.17 | Set.image_congr has no useful receiver here; no dot transformation. |
| 1.18 | Parenthesized scalar-set expression fixes type/grouping; no excess trailing lambda parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Tried grind [literalIndex], guarded failure in exit0 alternatives. |
| 2.2 | n/a: no grind retained, nothing preceding it to delete. |
| 2.3 | Tried terminal simp normalized image; fails to close scalar-image sInf; explicit API retained. |
| 2.4 | n/a: no function regularity goal. |
| 2.5 | Existing positivity proves nonnegative inverse Nat cast even without hl; verified built and independent. |
| 2.6 | n/a: no monotonicity inequality goal. |
| 2.7 | n/a: no Nat/Int arithmetic goal; scale merely cast. |
| 2.8 | Tried aesop, guarded failure to close. |
| 2.9 | n/a: no concrete numeric/cast normalization goal. |
| 2.10 | n/a: abstract noncomputable sInf equality, no finite decision computation. |
| 2.11 | No algebraic denominator goal remains after weight API; field_simp cannot commute sInf. |
| 2.12 | n/a: no ring/ring_nf ending or polynomial hypothesis combination. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: only one goal per refine, no repeated subgoal closing. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega/lia arithmetic. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No global attribute added: project rewrite theorem has explicit callers and existing normal form. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | No maxHeartbeats override present or introduced. |

Step-back reflection/scoped simplify: normalized unfolded-image proof is a valid alternate
five-tactic route (independent strengthened proof), but its measured proof184.98ms versus
retained186.35ms is negligible; explicit himg keeps the two mathematical conversions visible.
No holistic issue or reusable helper required. Built-in simplify tool unavailable; scoped
manual review done, independent file-final simplify sweep remains the owner's gate.

## Actual verification and performance

Artifact prefix below is `/private/tmp/roth-index-scale-`.

| Gate | Result and actual invocation/evidence |
|---|---|
| Module build | PASS: `/Users/ramin/.elan/bin/lake build Roth.Index`, exit0 session60179, `build.log`; 1501 jobs successful. |
| Complete native LSP | PASS: unfiltered file request, success=true, partial=false, timed_out=false; `lsp.json`; 0 target warnings/errors. |
| Independent original proof | PASS: fresh literalIndex definition, no Roth.Index import, no target/private/same-file theorem shortcut; `independent.lean`, final profiled compile exit0 session4657. Original DecidableEq+hl signature proved directly by function equality and scalar-image sInf. |
| Independent strengthened proof | PASS: same scratch file, no DecidableEq/hl; direct simp_rw/image_image route; zero specialization included; standard axioms printed. |
| Original exact public type recovery | PASS: `recovery.lean` imports ACTUAL BUILT Roth.Index, explicit full original universe/Fintype/DecidableEq/l/hl/P/α/r type reconstructed from e557886 snapshot, implemented by new theorem; exit0 session39499. |
| Built actual arity/axioms | PASS: `recovery.log` actual #check @target has no DecidableEq or hl; target/original adapter axioms exactly propext, Classical.choice, Quot.sound. Independent proofs same standard set in `independent-profile.log`. |
| Every binder/weakening | PASS: `binders.lean/.log`, final exit0 session35822; negative #check_failure assertions, explicit weak-hl proof; independent and built zero-scale checks separate. |
| Automation alternatives | PASS: standalone `alternatives.lean/.log`, exit0 session21124; guarded failures plus complete independent proof; standard axioms. |
| Definition protection | PASS: no definition/abbreviation or other declaration changed. |
| Statement protection | PASS with explicitly authorized DecidableEq/hl removals; P/α/r, implicit l, formula and documentation preserved. |
| Structure/naming/packing/inequality | PASS: concrete tables above; six-line body and clean mathematical name. |
| New identifier/comment preservation | PASS: no new proof lemma names, existing names checked in recovery.log; outside-target byte assertion and docstring equality passed; comments0/0. |
| No limit/scaffolding/trust change | PASS: no source options/debug wrappers, no sorry/new axiom/native_decide. |

Final LSP's eight non-target warnings remain honestly recorded: preserved copyright
metadata; sigma DecidableEq on rename/card/unique, tau DecidableEq on rename, and card's hr.
These belong to other declaration checkpoints. No filtering or suppression applied.

Actual anchored profiling commands, each exit0:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-scale-{before,final}-profile-trace.log`

Then `/private/tmp/roth-index-profile-parse.py scale-before` and `scale-final`, which assert
all 19 current declarations anchored and write corresponding profile-table.json files.

| Target | Before | Final | Budget |
|---|---:|---:|---:|
| command+async total | 251.15ms | 205.02ms | 1000ms |
| proof | 229.20ms | 186.35ms | — |

Final dominant tactic final rw137.97ms; all-file maximum389.14ms (weightedOrder theorem).
These are anchored declaration timings, not aggregate profiler categories. Alternative
independent strengthened proof184.98ms, original independent proof68.98ms; contexts differ,
so no speedup claim from those scratch timings. FAST-BOARD for this target, no borderline
resweep needed, no deferral, no limit raise. File-final profiling resweep remains owner work.

Owner-only gates PENDING at this report: exactly two Theta rewrite argument deletions,
preserving every Theta theorem contract, positivity assumption and instance; Theta module
and original-contract compatibility, original whole-Index/18-public recovery checks,
full project build and separate LeanEval under source freeze. This leaf makes no full-project claim.

## Required eleven checked steps

- [x] Step 1 — References: read required references before edit.
- [x] Step 2 — Audit: all24 concrete rows.
- [x] Step 2.5 — Search: all5 actual methods, DNS unavailability disclosed and local positives verified.
- [x] Step 2.6 — Generalise: every binder probed/classified; public literature and zero/weak cases covered.
- [x] Step 2.7 — Packing: every signature line arithmetic and actual width100 #check.
- [x] Step 2.8 — Inequality: occurrence table and final no reversed inequality.
- [x] Step 3 — Golf: all42 status rows and real automation attempts.
- [x] Step 4 — Reflection: measured independent alternative; scoped holistic simplify review.
- [x] Step 5a — LSP: complete native diagnostics, zero target diagnostics.
- [x] Step 5b — Gates: actual module/independent/originaltype/axioms/profile evidence above; owner gates explicitly pending.
- [x] Step 6a — Rename: none needed; existing one-entry queue untouched.

Issues fixed: unused DecidableEq, unused positivity argument, lambda syntax/packing.
Refactoring needed in this leaf: none beyond owner-coordinated approved caller repair.


## Owner checkpoint d18

Frozen SHA256 `c7ecc3d5d361a6f72515e0b4b400045466f6b79da07159eb003eca394addc402`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session37175 exit0, `/private/tmp/roth-index-d18-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval97631 both exit0(101.23s/35.65s),
Index+Theta hashes stable; `/private/tmp/roth-index-d18-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/8other warnings; /private/tmp/roth-index-scale-lsp.json. Owner COMPLETE Theta native LSP0errors/24warnings/noinfos after bounded partial+complete retry; both repaired callers accepted. Raw /private/tmp/roth-index-d18-theta-lsp.json. Theta docs/definition/theorem signatures untouched; only2exact rewrite argument deletions.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
