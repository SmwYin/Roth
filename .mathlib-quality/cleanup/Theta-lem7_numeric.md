# `Roth.lem7_numeric` — original declaration 34

Status: scoped original34 audit complete; owner publication/checkpoint gates remain pending.
Sole original34 scope, minimal necessary `Θ_lt` caller change, no new helpers or Git operations.
Standing user instruction “From now on implement all changes that you recommend. Only ask me if
you can't decide” authorizes the supported strengthening. Keeping Nat/Real domains and the public
name is the worker's technical judgment, not an explicit user veto. Protected earlier API choices,
imports, header, definitions and earlier proofs are untouched.

## Baseline and preparation

Published baseline HEAD `c63a306b9fff099f37b67c8e0d650e23f4462b6c`, source SHA256
`fc354913a6695d434020810dd37299614daa2bd7ca345b0e8bac489492679337`, 947 lines.
Snapshot and all scratch evidence are in `/private/tmp/roth-numeric34-audit/`.
Inherited owner full build 105.519s THEN separate LeanEval 38.323s passed; inherited complete native
`/private/tmp/roth-phi33-audit/final-lsp.json` has 0 errors and 8 warnings on this exact source.
These inherited gates are not fresh runs by this leaf. Optional cache/linter executable not run;
no dependency changes. Full Lean/mathlib-quality skills, cleanup command, mandated core references,
relevant style/naming and profiling references read. No installed standalone simplify invocation
exists here; the holistic simplify checks are performed directly and reported below.

A fresh real baseline ran BEFORE editing, with all normal compiler/native requests drained:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-numeric34-audit/baseline-prefix.lean`.
The exact production prefix ends after original34 and closes `end Lemma7`, then `end Roth`.
Exit 0. Disjoint target rows: outer command 31.437ms; async proof 1312.892ms; addDecl
8.216, 2.351, 51.297ms; linter 23.072ms; total **1429.265ms**. Nested kernel rows
8.154, 2.339, 38.190ms are included in addDecl, not added again. Nested macro commands are
not double-counted. This is prefix-only evidence, not whole-file performance.

`baseline-profile.log` is the untouched raw byte capture. It contains invalid UTF8 at offsets
144334923 (`e2`), 144335001 (`9c`), 144335002 (`85`), and zero actual U+FFFD byte sequences.
The anomaly's cause is unknown; concurrent trace interleaving is only a possible explanation.
`baseline-encoding.json` records the offsets and exact target slice boundaries.
`baseline-target-raw-utf8.log` is an exact **strict UTF8** byte slice supporting all target timing
rows. The explicitly labeled replacement-decoded full copy `baseline-profile-utf8.log` is not raw
UTF8 evidence. No original capture was rewritten. The final profiler uses the same preservation rule.

## Mathematical decision and pre-edit certificate

Put `a = δ^((1/2)^p)` and `T = 10^(p-1)`. Then `0 < a ≤ 1`, `10 ≤ T`,
`√δ ≤ a`, and the upper bound is `Φ ≤ 3*T*a²`. Multiplying `3 < T` by positive
`T*a²` yields `Φ < (T*a)²`, so `√Φ < T*a` without requiring nonnegative Φ.
Also `Φ ≤ 3*T*a`, and `√δ ≤ T*a`. Consequently the target follows from a linear
comparison, with strict slack even when δ=1 and Φ equals its bound.

Recommended and applied: `δ < 1` → `δ ≤ 1`; `Φ < bound` → `Φ ≤ bound`;
remove `0 ≤ Φ`. Keep strict positivity of δ: closed Φ and δ=Φ=0 would make the strict
conclusion false. These are compatible extensions, not claims of an optimal possible range.
The public docstring records the new range; the original source quotation and attribution remain.

Before applying the public changes, `candidate.lean` compiled exit 0, then the complete
`preapply.lean/.log` certificate compiled exit 0. It includes the full independent immutable
original Index and Theta proof blocks, exact old34 telescope adapter (including hΦ0), entire
immutable old Θ_lt proof, entire current Θ_lt proof value, and entire candidate Θ_lt proof.
It checks effective type equality with Lean Meta (not merely visible headers), opaque proof
values using `value! true`, actual standard axioms and candidate-caller dependency.
The immutable blocks remain exactly SHA256
`72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f` and
`355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`;
`immutable-blocks.json` compares them byte-for-byte with the preceding checkpoint's archive.
No current weakened type was substituted for the immutable original telescope.

The minimal Θ_lt change forwards `hδ1.le` and `hΦlt.le` and removes its precisely unused
four-line hΦ0 proof. Its other existing locals and proofs remain outside this cleanup's scope.
The final actual built constant and entire caller gates are recorded in the final verification below.

## Full 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | No inherited warning in target. Final unfiltered native warnings recorded below. |
| 2 | HAVE SCAN | Detailed scan below; inline single-use ha1, anonymous exponent bound, hΦa and hpow. |
| 3 | SET_OPTION | None in production; no limit raises or masks introduced. |
| 4 | SIMP SQUEEZE | Final `simpa [pow_two] using` is terminal; no nonterminal bare simp. |
| 5 | NAMING | `lem7_numeric` has snake_case form and identifies Lemma 7's scalar estimate. No forbidden mN/multipass/multiple-numeric/auxN/single-letter/abbreviation pattern. No rename recommended. |
| 6 | LINE PACKING | Complete signature codepoint table below. |
| 7 | BY PLACEMENT | All by at preceding line end. |
| 8 | FORMAT | Two-space indentation, no empty proof lines, no semicolon chains or haveI/letI. |
| 9 | COMMENTS | No inline proof comments existed in target; preserve source quotation and caller `-- combine` narrative. |
| 10 | DOCSTRING | Correct assumptions and note endpoint/negative-Φ extension, preserving source attribution. |
| 11 | VISIBILITY | Existing public numerical API retained; no helper added. |
| 12 | STRUCTURE | Ordinary result (not listed among module Main results); body 29 lines ≤30, all subproof blocks ≤5 lines, no conjunction output. |
| 13 | MATHLIB | Five actual methods plus clean anonymous generic probes below; use sqrt/rpow/product API directly. |
| 14 | JUNK DEF | n/a: theorem, no definitions introduced or modified. |
| 15 | EXISTS LEMMA | n/a: no existential result/helper; local successor witness substitutes p. |
| 16 | SHOW/CHANGE | No production show/change. Type ascriptions only disambiguate scalar arithmetic. |
| 17 | PUSH_NEG | No push_neg. |
| 18 | GENERALISE | Every effective original binder tested; three combined and individually adapted weakenings compiled; counterexamples reject unsupported drops. |
| 19 | INEQUALITY | All code inequalities smaller-first; scan table below. |
| 20 | NORMAL FORM | Standard Nat powers/Real.rpow and Real.sqrt, no custom predicate or duplicate equivalent form. |
| 21 | SYNTAX GENERALITY | Keep retained binder names/order/implicitness; accept `.le` at caller. |
| 22 | IMPORT FANOUT | n/a: no import/header changes. |
| 23 | CASTS | No cross-type cast added; explicit Real numeric ascriptions determine rpow/exponent/scaled-bound elaboration. |
| 24 | INSTANCE NAME | n/a: no effective section class or instance binder in target; final effective types checked. |

### Every have and set binding

`set a ... with ha` and `set T ... with hT`: meaningful repeated subterms and rewrite identities,
keep. `ha0` non-by: used repeatedly for square positivity, product sign and final comparison, keep.
Original `ha1` non-by single use: inline Real.rpow_le_one into the proof of `haa`.
`ha2` has the four-line rpow exponent identity proof: keep. `hsqrt` has its four-line
exponent-monotonicity proof: keep; inline its original one-use anonymous exponent bound with
an explicit type in `linarith only`. `hT10` non-by: used repeatedly in the strict/weak scaled comparisons, keep. `hsΦ` has the
four-line scaled strict square comparison, keep. New local `haa` has a two-line substantive
bound proof, keep; no exported/private helper. One-use non-by `hΦa` is inlined in the final
linear combination. Original `hpow` one-use proof is eliminated by direct rewrites.

## Five actual search methods and public literature/inversion

Native results archived in `searches.json` in the audit directory.

| Method | Actual query/result |
|---|---|
| A Lean-Finder | Full numerical iterated-root estimate query: five unrelated Bertrand/Behrend/Liouville results, no direct replacement. |
| B Loogle | `Real.sqrt ?x < ?y`: eight hits including `Real.sqrt_lt'`, `Real.sqrt_lt`, sqrt comparison variants. |
| C LeanSearch | Square root less than positive number iff argument less than square: `Real.sqrt_lt'` and related variants. |
| D source grep | Full untruncated grep for lem7_numeric, two_mul_add_sqrt_lt, sqrt_add_sqrt: no hits; inspect Pow/Real and Analysis/Real/Sqrt declarations, including sqrt_lt' and exponent comparisons. |
| E native local name | `sqrt_lt`: ten source matches; index **unavailable**, so no indexed absence claim. `sq_le_self`: index **warming**, no usable exact lemma found. |

Auxiliary variants searched: sqrt_lt/sqrt_lt'/sqrt_lt_sqrt_iff/_of_pos, rpow exponent `_ge`,
`_ge'`, `_ge_of_imp`, squared bounds and nonnegative product monotonicity.
Common-equivalents table has no applicable topology/discrete/finite/meromorphic pattern.
The result requires real-power exponent conversion and genuine strict numerical slack; it is not
a 1–3-call wrapper. No new lemma introduced from a search-only mathematical absence claim.

A native isolated signature probe verified Real.sqrt_lt' and rpow_mul_natCast and product lemmas;
it rejected guessed `sq_le_self₀`. This failed name was removed before production edits. The
replacement uses verified direct multiplication and terminal simpa, and the selected proofs compile.
`automation.lean/.log` uses only pre-Theta dependency imports and anonymous examples, so neither
the audited target nor named failed trials can contaminate exact?/apply?. It actually tries rfl,
simp, ring, linarith, nlinarith, lia, exact?, apply?, grind, aesop, simp_all at scratch-only 5000
heartbeats. Exit 1 is expected; exact? fails, apply? gives only incomplete product decompositions
and reaches the conservative budget; the other tactics leave goals. Timeout is inconclusive,
not evidence of global absence. Known repeated native full-Theta multi_attempt stalls were not
repeated; ordinary isolated compiler fallback is bounded by these conservative per-example limits.

Public web searches actually run: “Roth 1955 rational approximations algebraic numbers lemma 7
index polynomial 10 delta square root generalization” and “sqrt inequality x sqrt x delta power
Roth lemma 7 generalization”. Primary [Roth 1955 paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf)
opened and searched: Lemma 7 pp.12–13 has the strict dimension-dependent δ restriction and
induction's numerical absorption. The repository's authoritative `clean.tex` §5 lines1023–1039
makes the `a²≤a`, `√δ≤a` comparison explicit. Searches found no precise endpoint theorem or
replacement. The endpoint/negative-Φ extension here is the compiled algebraic deduction above,
not a theorem attributed to the literature. No ChatGPT-math MCP capability is available.

Mandatory inversion: no named polynomial or Θ construction occurs in this scalar statement.
The abstraction `(a,T)` isolates the algebra but is useful here only once and would add a helper
solely around the same comparison; no helper is needed at 29 lines. Nat p is the dimension/power
index; replacing it by Int would require zpow and a different API with no additional values under
2≤p. Real δ/Φ use Real.rpow/Real.sqrt; abstract-field restatement would require a power/sqrt
structure change. Keeping these domains is a technical recommendation, not an asserted user veto
or a claim that these constants/ranges are mathematically optimal.

## Every effective original binder

`negative.lean/.log` is an expected-failure batch (exit1), separate from successful proof/axiom
certificates. Value binder removal uses `autoImplicit false`; unknown-value errors establish
syntactic dependence only. Mathematical necessity claims use the successful counterexamples.
`polished.lean/.log` exit0 supplies the combined proof and three independent API adapters for
closed δ alone, closed Φ alone and dropping Φ nonnegativity alone. The scratch adapters retain
unused hΦ0 where appropriate and emit honest unused-variable warnings.

| Binder | Class / role | Actual probe and result |
|---|---|---|
| `{p : ℕ}` | value, Nat exponent/dimension | drop with autoImplicit false fails unknown p in formula; p=1 weakening refuted below; keep Nat. |
| `hp : 2 ≤ p` | proposition, T≥10 | drop fails successor/nonzero-exponent arithmetic; weakening to 1≤p false at p1, δ81/100, Φ9/4. |
| `{δ : ℝ}` | value, Real.rpow/sqrt | drop with autoImplicit false fails unknown δ; no abstract-field API recommended. |
| `hδ0 : 0 < δ` | proposition, strict a positivity | drop fails explicit rpow/sign uses; changing to nonnegative with closed Φ is false at δ=Φ=0. |
| `hδ1 : δ < 1` | proposition, a≤1 and √δ≤a | drop fails proof and is mathematically false at δ16, p2, Φ100; closed δ≤1 compiles, applied. |
| `{Φ : ℝ}` | value, arbitrary scalar | drop with autoImplicit false fails unknown Φ in formula; negative Φ accepted by selected proof. |
| `hΦ0 : 0 ≤ Φ` | proposition | original broad nlinarith proof without it fails final arithmetic; revised explicit square-bound proof removes it successfully, applied. |
| `hΦ : Φ < bound` | proposition | drop fails rewriting/proof and is false e.g.p2 δ1/16 Φ100 under the original strict δ assumptions; closed Φ≤bound compiles, applied. |

`counterexamples.lean/.log` corrected exit0 proves: δ=Φ=0 rejects simultaneous nonnegative δ
and closed Φ; omitting Φ bound fails at p2 δ1 Φ100; the additional local-golf probe also certifies failure at p2 δ1/16 Φ100 under the original strict δ assumptions; p=1 fails with **original strict** δ and
Φ hypotheses at δ81/100, Φ9/4 (left side9.3, right9); removing upper δ bound fails even with
original open Φ at p2 δ16 Φ100 (left side228, right200). The first scratch run had missing
nonnegativity arguments to sqrt_eq_iff_eq_sq and incomplete sqrt evaluations; its errors are
preserved separately in `counterexamples-initial.log` and are not positive evidence.

## Signature packing and inequality scan

Actual width100 #check is captured in final compatibility output. Codepoint measurement:

| Sig line | Width | Next atomic signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 701 | 85 | `(hΦ : Φ ≤ 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1)))` (57) | 85+1+57=143>100 | ok |
| 702 | 63 | whole atomic conclusion through `:= by` (56) | 63+1+56=120>100 | ok |
| 703 | 60 | no next signature line | n/a | ok |

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | entire signature | n/a — zero ≥ or > in Lean code | none | no _ge_/_gt_ name |

The proof's inequalities also use ≤/< throughout. Documentation uses natural mathematical prose.

## All 42 golfing rules

| Rule | Actual action/result |
|---|---|
| 1.1 by exact | n/a: none. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw+exact→rwa | n/a: no exact proof matching a trailing rewrite. |
| 1.4 simp+exact→simpa | Applied to squared a bound as terminal simpa using direct multiplication. |
| 1.5 simp+rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: no conjunction construction. |
| 1.7 apply+exact | Strict sqrt step is composed directly via `.2 (hΦ.trans_lt ?_)`. |
| 1.8 by_contra! | n/a: no contradiction/negation phase. |
| 1.9 eta reduction | n/a: no lambdas in target. |
| 1.10 one-use have | Inline ha1, anonymous exponent bound, hΦa; eliminate hpow by rewrites. |
| 1.11 refine+fun | n/a: no universal tactic introduction. |
| 1.12 redundant show | n/a: no show. |
| 1.13 obtain tuple | Existing obtain substitutes successor witness directly; no projection pair. |
| 1.14 merge rw | Final pow_succ/hT/commutativity rewrites combined. |
| 1.15 terminal simp | Terminal simpa remains unsqueezed. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | Use hΦ.trans_lt, hsqrt.trans, hΦ.trans. |
| 1.18 <| | No parenthesized lambda to simplify; retain parentheses around compound bound terms. |
| 1.19 push Not | n/a: none. |
| 1.20 trivial ∃ helper | n/a: no existential helper. |
| 2.1 grind whole | Actually fails in clean anonymous batch. |
| 2.2 delete before grind | Whole-goal grind already fails, no production grind to shorten. |
| 2.3 simpa consolidation | Direct terminal simpa for a²≤a; no separate simp/closing step. |
| 2.4 fun_prop | n/a: no regularity/property goals. |
| 2.5 positivity | Used for positive rpow/product and numeric signs, replacing generic search. |
| 2.6 gcongr | Actual local-golf probe closes the scalar product bound; retain direct named product applications for their explicit sign inputs and direct composition. |
| 2.7 lia | Replace both original omega calls by successful lia. |
| 2.8 aesop | Actually fails after exhaustive search in clean batch. |
| 2.9 norm_num/cast | Norm_num discharges exact scalar sign bounds; push_cast remains only in rpow exponent identity. |
| 2.10 decide | n/a: arbitrary Real inequalities are not computably decidable finite problems. |
| 2.11 field_simp/ring | n/a: no variable denominators, ring handles exponent identity directly. |
| 2.12 linear_combination | Actual local-golf probe closes the exact exponent scalar identity with hypotheses in scope; retain ring since the identity needs no hypothesis. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 collapse calc | n/a: no calc block. |
| 2.15 <;> | n/a: no multiple equivalent subgoals. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 regularity tactics | n/a: no continuity/measurability. |
| 3.3 omega→lia | Applied at both Nat arithmetic sites. |
| 3.4 substitution | Existing obtain with rfl substitutes p; no redundant subst. |
| 3.5 attributes | No simp/grind attribute recommended for a specialized strict iterated-root estimate. |
| 3.6 simp_all | Actually fails whole goal in clean batch; no production simp_all only. |
| 3.7 limits | None in production; scratch conservative lower budget only. |

Step-back reflection: clean whole-proof automation does not resolve the real-power/square-root
conversion. The selected proof follows the mathematics: exponent conversion, root bounds, then
one linear comparison. No meaningful shared proof or duplicated API warrants a helper.

## Final verification, simplify, buzz and gates

Scoped module, actual certificate, native diagnostics and both final real profiles passed, as recorded below.
Owner full build THEN separate LeanEval/cumulative public checkpoint gates remain owner work;
this worker never claims these pending gates passed. Earlier mandatory performance repair queue
(index29 repeats1068.193/1115.157ms and whole Θ_lt profiling stalls) remains; no all-file PASS is
claimed from this target's prefix. Original35 is reserved for its fresh audit.

Module gate actually run: `/Users/ramin/.elan/bin/lake build Roth.Theta` → exit0,
Roth.Theta rebuilt in34s, 2423 jobs; complete output `final-module-build.log`.
Then `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-numeric34-audit/final-compatibility.lean`
→ exit0, `final-compatibility.log`. The final source's independent complete Θ_lt proof is
recompiled in this certificate. Actual built `Roth.lem7_numeric`, exact-old adapter, immutable
original34, immutable original Θ_lt, actual built Θ_lt and independent candidate Θ_lt all have
opaque values of exactly their effective types and standard axioms only
`propext`, `Classical.choice`, `Quot.sound`. Actual Θ_lt's full proof value depends on actual
`Roth.lem7_numeric`. All expected PASS markers appear; no error/PANIC/sorryAx in the positive log.
The final candidate proof includes the final one-use-bound inlining, not merely the earlier draft.

Complete **unfiltered** native `lean_diagnostic_messages` on live Roth/Theta.lean:
`final-lsp.json`, `success:true`, `partial:false`, `timed_out:false`, `failed_dependencies:[]`,
zero errors, all eight warnings:

| Location | Full warning substance |
|---|---|
| 1:2 | Copyright too short (`linter.style.header`). |
| 93:43 | Variable `hr` not explicitly referenced (`linter.unusedVariables`). |
| 101:27 | Variable `hB` not explicitly referenced (`linter.unusedVariables`). |
| 101:64 | Variable `hr` not explicitly referenced (`linter.unusedVariables`). |
| 109:28 | Variable `hB` not explicitly referenced (`linter.unusedVariables`). |
| 129:81 | Variable `hr` not explicitly referenced (`linter.unusedVariables`). |
| 252:6 | Variable `hr` not explicitly referenced (`linter.unusedVariables`). |
| 547:47 | Variable `hq` not explicitly referenced (`linter.unusedVariables`). |

Every raw warning, hint and linter note is preserved without filtering in final-lsp.json.
These warnings are unchanged and outside original34's edit scope. The header metadata and some
named API hypotheses have explicit earlier preservation choices; the 93/252 warnings are earlier
owner scope choices, not claimed as user vetoes. No warning suppression was added.

### Holistic simplify review

Outcome: ISSUES-FOUND-AND-FIXED, performed directly because no separate built-in simplify tool
is exposed. Inline single-use arithmetic facts and replace the broad arithmetic proof by scaled
product/square bounds. Check reuse, dependency direction, caller contraction, signs and strictness.
No duplicated proof skeleton, new definition, needless helper or hidden instance change remains.
The complete independent caller/value/axiom and actual module/native gates above verify the result.

### Buzz diagnosis

Root cause4, heavy terminal automation: raw baseline target trace has two nlinarith hotspots
400.026ms and409.340ms, plus a148.270ms broad linarith exponent comparison. `baseline-hotspots.json`
and exact strict-UTF8 target slice record these nodes; nested tactic nodes are diagnostic only,
not added again to the1429.265ms target total. The fix provides the explicitly multiplied square
inequality and uses `nlinarith only` on that certificate; the final comparison is `linarith only`
on three prepared bounds. The exponent comparison also uses only its exact power≤1 certificate.
No limit raises, no production profiler/scaffolding, no new helper. No unrelated performance
repair is silently folded into this target cleanup.


Additional applicable alternatives were actually compiled in `local-golf.lean/.log`, exit0:
linear_combination closes the post-rewrite exponent identity with hypotheses in scope; gcongr
closes a*a≤1*a. Retain the direct selected proof: these alternatives give no additional structural
simplification. The same file certifies that dropping the Φ bound fails while retaining the
**original strict** δ assumptions at p2, δ1/16, Φ100. Its only warning is an intentionally unused
scratch hδ0 in the pure ring identity. No production source changed after any final gate.

First final uncontended exact-prefix real trace: `final-profile.log`, exit0, untouched and entirely
strict UTF8 (zero invalid sequences and zero literal U+FFFD), with explicit byte-escaped companion
and `final-encoding.json`. Source SHA256 is a98740b5b006547f5deafca6cbb12c6b4972dbfc130eae64645e67bdd9b8d800.
Disjoint rows outer26.460ms; async proof683.212ms; addDecl0.150/5.011/1.641/22.389ms;
linter18.819ms; total **757.682ms**. Nested kernel0.131/4.965/1.629/17.390ms not added again.
`final-profile.json` and `final-profile-target-raw-utf8.log` retain exact declaration anchors and
raw byte boundaries. This is below1000ms but ≥750ms, so a mandatory same-final-source repeat ran
after all ordinary probes drained. Both measurements are retained; no cherry-picked third sweep.

### Scoped diff gates

| Gate | Result / actual evidence |
|---|---|
| lake_build_file | PASS: actual `lake build Roth.Theta`, exit0; final-module-build.log, rebuilt34s. |
| definition_protected | PASS: zero def/abbrev/import/header/earlier-proof changes; exact prefix equality in scope-check.json. |
| theorem_statement_protected | PASS with authorized strengthening: concrete pre-edit candidate, exact immutable old34 adapter and entire-caller certificate passed; retained names/order/implicitness unchanged. |
| structure_gate | PASS: target29 lines≤30, longest mathematical subproof≤5, no conjunction output/new helper. Θ_lt is only minimally adapted and reserved for original35. |
| naming_gate | PASS: forbidden patterns absent; no rename recommended or queue write. |
| line_packing_gate | PASS: all3 signature lines measured; every row ok. |
| inequality_orientation_gate | PASS: complete scan table, zero ≥/> in target code. |
| cumulative_no_unintended_breakage | PASS at leaf scope: only repository caller is Θ_lt; actual module plus entire original/current/independent caller type/value/axiom certificate. Owner broader cumulative/full project gates remain pending. |
| axiom/value/original-proof gate | PASS: final-compatibility.log, exact immutable original blocks72cf/355a, standard3 axes, actual opaque values and dependencies. |
| native diagnostics | PASS: complete unfiltered final-lsp.json, 0errors,8 unchanged warnings; no partial result. |
| no-limit/no-scaffolding | PASS: no source limits, no profiler wrappers, no new axioms/sorry/native_decide, no helper. |

Scoped simplified proof and API checks are complete. The required performance repeat also passed; final handoff below records its actual outcome.


### Required final same-source repeat and frozen handoff

The same final-prefix command ran uncontended a second time after every normal request drained,
without changing source. `final-profile-repeat.log` exit0; disjoint outer35.445ms,
async proof779.485ms, addDecl0.188/5.804/1.773/24.272ms, linter18.864ms:
**865.831ms**. Nested kernel0.169/5.755/1.756/20.840ms is already included and not added again.
Full raw repeat capture is also strict UTF8 with zero invalid sequences and zero literal U+FFFD;
`final-repeat-encoding.json` records this, and the untouched raw log, byte-escaped companion,
exact strict-UTF8 target slice and JSON rows remain in the audit directory.

Buzz outcome: **FIXED, scoped original34** — 1429.265ms → 757.682ms and mandatory repeat865.831ms,
both below1000ms. The first was≥750ms, so the repeat was required and actually performed.
No third sweep, no raised/masked limits, no new helper, no whole-file performance PASS.
The known earlier index29 repeat1068.193/1115.157ms and Θ_lt whole-profile stalls remain
mandatory owner/file-final repair work, not silently fixed or waived by this leaf.

| Result | Before | After | Delta |
|---|---:|---:|---:|
| Target proof body | 25 | 29 | +4 lines; within ordinary30-line cap |
| Whole source | 947 | 948 | +1 line |
| New helper declarations | 0 | 0 | 0 |

Source frozen at SHA256 **a98740b5b006547f5deafca6cbb12c6b4972dbfc130eae64645e67bdd9b8d800**.
All source edit authority for this leaf is revoked; only this report was completed after freeze.
All owned shell/native requests completed and drained: **pending_requests=[]**.
`/private/tmp/roth-numeric34-audit/handoff.json` records the same frozen hash, totals, no helpers
and owner-pending gates. No Git/shared-progress writes were performed.

The owner must now run the cumulative approved-public checks, full `lake build` THEN a separate
`lake build Roth.LeanEval`, update shared progress, exact-stage/commit/push this checkpoint before
original35. These are pending owner gates, not leaf claims of completed publication.

### Required eleven-step checklist

- [✓] Step1: full mandated skills/workflow/reference reads.
- [✓] Step2: all24 audit items, every have/set and concrete action.
- [✓] Step2.5: allfive actual search methods, variants and clean generic probes.
- [✓] Step2.6: every effective binder, compiled weakenings/drops, public literature and inversion.
- [✓] Step2.7: complete measured signature packing table and width100 actual #check.
- [✓] Step2.8: complete inequality scan, zero reversed code inequalities.
- [✓] Step3: all42 rules; applicable whole-goal/local alternatives actually tried.
- [✓] Step4: mathematical/structural step-back and holistic simplify review.
- [✓] Step5a: complete unfiltered native live diagnostics,0 errors,8 unchanged warnings.
- [✓] Step5b: scoped diff/module/actual opaque values/standard axioms/entire caller and both real performance gates.
- [✓] Step6a: no rename recommended; no queue write; final frozen/drained report and handoff.

Comments-preserved: no target inline comments existed; the source attribution/quotation and
caller `-- combine` narrative remain. Refactoring needed within original34 scope: none.
Owner broader checkpoint and mandatory queued performance repairs remain explicit above.


## Owner cumulative exact-original recovery

Owner regenerated the final34-aware adapter probe before running it. Actual `d34-values`
compiled exit0 in50.626s with frozen source: all29 original public adapters, all5 original
definition values,87 opaque body-type checks,87 actual standard-axiom sets, and29 final
public PASS markers. Both complete original Index/Theta proof blocks remain byte-identical
SHA72cf/355a. No error, PANIC or sorryAx appears in the positive log. Exact archived input
`/private/tmp/ThetaApprovedOriginalFinalProbe-d34-values.lean`,
SHAdf89dc269811de74901c772a70a4ccf9fb0b0a9c2d1ebd2bb4c66063c14ad5b1;
raw log/record `/private/tmp/roth-theta-d34-values-cumulative29.{log,json}` and owner
count/block check `/private/tmp/roth-theta-d34-owner-cumulative-checked.json`.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (108.121 s),
then separate `lake build Roth.LeanEval` (33.707 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `a98740b5b006547f5deafca6cbb12c6b4972dbfc130eae64645e67bdd9b8d800`.
Raw logs: `/private/tmp/roth-theta-d34-full.log`, `/private/tmp/roth-theta-d34-leaneval.log`; machine record
`/private/tmp/roth-theta-d34-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 34/35, overall 215/264 original
declarations, 9/14 completed files. No new helper; existing separately audited helpers unchanged. No original-count inflation from helper/revisit audits.
