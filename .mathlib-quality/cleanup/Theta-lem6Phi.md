# `Roth.lem6Φ` — original22 dedicated cleanup

Scope: only the public noncomputable definition at `Roth/Theta.lean:270–271`.
The selected implementation is the sum of the one-variable and remaining-variable Θ quantities
in source equation (15). The only source edit changes three ordinary lambda arrows `=>` to `↦`.
Body length: 1 → 1; total declaration: 2 → 2; line delta 0. No helper, caller, import,
name, visibility, argument, class, domain, docstring, or mathematical value changes.

## Baseline and instructions

Read `lean4/SKILL.md`, `mathlib-quality/SKILL.md`, full cleanup workflow,
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, relevant style sections (formatting,
lambda notation, documentation, definitions/API, normal forms, profiling), full naming and
profiling references, and `/private/tmp/roth_theta_leaf_instructions.md`.
The read-only preparation respected the original21 owner compiler window: no writes,
compilers, native searches, LSP, or profile requests until explicit RELEASE.

Released checkpoint: `94d4492799e5c1b163dfbff2a38245ca755ecce2`.
Released Theta SHA256: `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`.
Inherited baseline complete unfiltered LSP:
`/private/tmp/roth-theta-lem6M/final-lsp.json`: success=true, partial=false,
timed_out=false, failed_dependencies=[], 0 errors, 17 warnings, none on this declaration.
The owner reported baseline whole build 5.980s, then separate LeanEval 3.018s, both exit 0.
These are inherited baseline facts, not this worker's final owner gates.
No optional cache/linter command was necessary: cached module dependencies and complete LSP
provide the baseline doctor evidence. The public header metadata remains protected.

## Full 24-item audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No target diagnostics in inherited baseline or fresh final complete LSP. The 17 module warnings are pre-existing and outside this leaf. |
| 2 | HAVE SCAN | No `have` declarations; expression-mode data definition. |
| 3 | SET_OPTION | None on target; no limit increase or profiler scaffolding introduced. |
| 4 | SIMP SQUEEZE | No simp calls. |
| 5 | NAMING | `lem6Φ` identifies the named Φ of Lemma 6 and is explicitly protected paper API. Not a forbidden numeric-prefix, numbered-aux, single-letter, or forbidden abbreviation pattern. No rename recommended. |
| 6 | LINE PACKING | Single complete 67-codepoint signature, body 90 codepoints; measured table below. |
| 7 | BY PLACEMENT | No tactic mode or `by`. |
| 8 | FORMAT | Two-space body indentation and direct term retained; three ordinary lambda arrows normalized to `↦`. No `haveI`/`letI`. |
| 9 | COMMENTS | No body comments; original two-line docstring preserved byte-for-byte. |
| 10 | DOCSTRING | Describes Φ and equation (15), including the two summands. Retained exact text. |
| 11 | VISIBILITY | Public module-listed definition with downstream mathematical uses. Retain public. |
| 12 | STRUCTURE | One body line, no branches, conjunctions, existential witnesses, or extraction need. |
| 13 | MATHLIB | Five actual search methods below; no applicable replacement was returned. No global decidability instance or coset machinery. |
| 14 | JUNK DEF | Reused across `index_det_le`, `index_le_lem6`, `Θ_option_le`, and `Θ_lt`; named source constant with repeated unfolding uses. Retain. |
| 15 | EXISTS LEMMA | Not an existential theorem. |
| 16 | SHOW/CHANGE | Neither present. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Six effective binders probed; Fintype→Finite construction compiled as isolated API candidate, retained Fintype API. Details below. |
| 19 | INEQUALITY | Zero inequality occurrences in signature/body. |
| 20 | NORMAL-FORM | Direct addition of the two source Θ expressions is the canonical paper formula. No equivalence layer needed. |
| 21 | SYNTAX-GEN | Existing `(q r) M l` interface directly supports current callers; bundling/splitting parameters adds conversion work. No restatement recommended. |
| 22 | IMPORT-FANOUT | No new imports. |
| 23 | CASTS | No explicit coercion/cast change. `Unit` annotation fixes the one-variable domain and remains load-bearing. |
| 24 | INSTANCE-NAME | Not an instance; no named instance introduced. |

## Measured line packing and inequality tables

`#check @Roth.lem6Φ` from independently compiled final probe (format.width=100):

```lean
@Roth.lem6Φ : {τ : Type u_1} → [Fintype τ] →
  (Option τ → ℕ) → (Option τ → ℕ) → ℝ → ℕ → ℝ
```

The output is shown wrapped for this report; raw output is `positive-final.log`.

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 270, complete declaration header through `:=` | 67 | none, body starts next | n/a: no further signature line; whole body has 88 non-indent codepoints, 67+1+88=156>100 | ok |

The body line has 90 codepoints including its two-space indentation. All signature arguments
and the result type are already on the same line; none can be packed further.

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | full signature and body | no `≥` or `>` relation | n/a | none |

The three former `=>` tokens were lambda syntax, not strict inequality occurrences.

## Five-method actual mathlib search

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Roth theorem auxiliary Phi sum supremum polynomial index one variable remaining variables` | Returned Chevalley numerical/degree bounds and additive Roth-number definition; none is this quantity. |
| B Loogle | `"lem6Φ"`; then `(Option ?a → ℕ) → (Option ?a → ℕ) → ℝ → ℕ → ℝ` | Both returned empty items. |
| C LeanSearch | `Roth theorem auxiliary Phi sum indices of polynomials` | Returned Polynomial.sum, additive rothNumberNat_add_le, Polynomial.ctorIdx; no relevant replacement. |
| D full source rg | `lem6Φ|lem6Phi|Roth.*index|index.*Roth` over all Mathlib | No hits, exit 1; untruncated log retained. |
| E native local name search | `lem6`, project root supplied | Returned project lem6M/lem6M_lt; index=unavailable. This is an attempted native search with a documented index limitation, not evidence of absence. |

Raw A/B/C/E results: `/private/tmp/roth-theta-lem6Phi/search0.json` through `search3.json`.
The second Loogle call is also recorded in the session tool result. Source search raw log:
`source-search.log`. Auxiliary alternatives considered: Φ/Phi spelling, Roth polynomial index,
one-variable/restricted-variable Θ sum. The common-equivalents table has no matching bucket.
Conclusion: the performed searches found no replacement for the named paper constant.
No absolute library-absence claim is made; no new mathematical declaration was added.
Generic automation/`exact?`/`apply?` absence probes are not proof searches for this data-valued
definition: arbitrary real inhabitants do not certify this required value. The independent
compiled exact-value `rfl` checks below are the meaningful replacement-compatibility probes.
The known stalled full-Theta `lean_multi_attempt` path was not repeated.

## Effective-binder generalisation probes

Actual effective original/current telescope:
`{τ : Type u_1} [Fintype τ] (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : ℝ`.
The section's `[DecidableEq τ]` and all σ binders are already absent from this definition's
effective type. They were not silently removed by this cleanup.

Every effective binder has an actual compiled drop probe in `negative.lean`, with
autoImplicit=false. The expected-failure batch exits 1 and is not positive certification.

| # | Binder | Role/use | Compiled candidate | Result |
|---|---|---|---|---|
| 1 | `{τ : Type*}` | Domain of q/r and remaining-variable Θ | drop | unknown τ at line 3. Already universe-polymorphic; broader Sort cannot serve Option/MvPolynomial Type domains. |
| 2 | `[Fintype τ]` | Finite-variable index underlying remaining Θ | drop; replace by `[Finite τ]` with local `Fintype.ofFinite τ` | Drop fails synthesis at line 6. Finite candidate independently elaborates in positive.lean; no API change recommended. |
| 3 | `q` | q none and q ∘ some | drop | unknown q at line 8. Domain fixed by source denominators and Θ interface; no weaker proposition to test. |
| 4 | `r` | degree weights in both summands | drop | unknown r at line 10. Natural weights are the definition's prescribed domain. |
| 5 | `M` | coefficient bound supplied to both Θ terms | drop | unknown M at line 12. Θ takes real bounds; abstracting the codomain would require replacing Θ itself. |
| 6 | `l` | scales both sets of degree weights | drop | unknown l at line 14. Natural scaling is prescribed; no proposition to weaken. |

Finite reconstruction is a viable elaboration candidate, not an automatically warranted new
public definition: it changes the class presentation and inserts a reconstructed finite
enumeration into the value. No independently certified semantic upgrade or caller benefit
was established. Retain the protected original class and all domains/order/names.
No strict/weak, local/global, bundled-hypothesis, or algebraic-parent hypothesis exists here.
No artificial use of an unused class or public argument was introduced.

## Public literature and inversion

Read local authoritative source `clean.tex:705–724`: equation (15) explicitly defines Φ as
exactly this sum. The current definition already accepts every real M and every natural l,
without the positivity/growth assumptions of the later bounding theorem; adding those would
restrict the definition unnecessarily.

Actual web queries: `"Formalizing Roth" "Phi"` and
`Roth theorem index polynomials Lemma 6 Phi generalization`. Relevant returned references:
[AMS chapter preview](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf),
[Roth’s theorem notes](https://www.math.uh.edu/~minru/fields/roth.pdf), and
[Roth’s ICM exposition](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf).
Search snippets concern the polynomial index method; none supplied a useful replacement or
broader formulation of this specific named constant. The local paper equation is the direct
formula evidence. ChatGPT mathematical MCP: n/a, no such tool available in tool metadata.
No literature-driven API change recommended.

Inversion check: this is a data definition, not a proof whose first unfolding hides an
abstract theorem. Its body uses Θ twice and the q/r/M/l parameters throughout. Replacing
the summands by arbitrary reals would merely name addition and lose the paper meaning;
it would not generalize useful mathematical content. No abstract helper recommended.

## All 42 golfing rules

The body is already a direct data expression, so tactic-based alternatives would need to
be tested against a fixed value, not merely the inhabited type ℝ. No tactic proof is present.

| Rule | Status/reason |
|---|---|
| 1.1 by exact | n/a, direct term already. |
| 1.2 by rfl | n/a, no equality proof wrapper. |
| 1.3 rw + exact | n/a, no rewrites. |
| 1.4 simp + exact | n/a, no simplification. |
| 1.5 trailing rfl | n/a, no tactics. |
| 1.6 constructor | n/a, real addition expression. |
| 1.7 apply + exact | n/a, no tactics. |
| 1.8 by_contra | n/a, not a proposition proof. |
| 1.9 eta reduction | Lambdas genuinely select none or scale weights; none is an eta-redex. Retained. |
| 1.10 have inline | n/a, no have. |
| 1.11 apply + intro | n/a. |
| 1.12 show | n/a. |
| 1.13 projections | n/a. |
| 1.14 consecutive rw | n/a. |
| 1.15 terminal simp | n/a. |
| 1.16 nonterminal simp | n/a. |
| 1.17 dot notation | Addition/composition already direct; no applicable projection/application conversion. |
| 1.18 `<|` | Existing final lambda needs no parentheses; `<|` would add syntax. |
| 1.19 push_neg | n/a. |
| 1.20 trivial existential | n/a, public named real quantity. |
| 2.1 grind | n/a, data-valued expression; not a multi-line proposition proof. |
| 2.2 delete before grind | n/a, no tactics. |
| 2.3 simpa | n/a, no proof chain. |
| 2.4 fun_prop | n/a, no function-property goal. |
| 2.5 positivity | n/a, no inequality goal. |
| 2.6 gcongr | n/a, no monotonicity goal. |
| 2.7 lia/omega | n/a, no arithmetic proposition goal. |
| 2.8 aesop | n/a, no logic/membership goal. |
| 2.9 norm_num/cast | n/a, symbolic definition, no numeric/cast goal. |
| 2.10 decide | n/a, real quantity not decidable proposition. |
| 2.11 field_simp/ring | n/a, no identity proof or denominator. |
| 2.12 linear_combination | n/a, no proof with hypotheses. |
| 2.13 wlog | n/a, no symmetric case branches. |
| 2.14 calc collapse | n/a. |
| 2.15 close goals | n/a. |
| 3.1 erw | n/a. |
| 3.2 legacy function tactics | n/a. |
| 3.3 omega→lia | n/a. |
| 3.4 rcases rfl | n/a. |
| 3.5 automation attributes | No new attribute warranted for an auxiliary numerical definition. |
| 3.6 simp_all | n/a. |
| 3.7 maxHeartbeats | None to remove; none added. |

Step back: it already is the desired single composed expression. Keeping it avoids a
pointless helper, proof wrapper, altered API, or expanded sum. The notation normalization
is the only zero-risk style improvement recommended and applied.

## Independent original, built constant, and gates

`positive.lean` extracts immutable source definitions RSet/indexSet/Θ/lem6Φ from commit
`2b64544bf9f77a8ff957bf1bcaf693ac72217ff6` into `ImmutableOriginal22`.
These are independent data definitions; the original Φ is not defined by invoking current
`Roth.lem6Φ`. They use the imported polynomial index foundation (already independently
audited by the owner), matching its original qualified reference.
The final probe imports the freshly built actual Roth.Theta artifact and verifies:

- Exact original/current elaborated telescope AST, including names/order/BinderInfo/classes.
- Definitional equality of the independently elaborated type and value, via Lean Meta isDefEq.
- Kernel-checked equality by `rfl` of whole original/current functions and of the displayed formula.
- Actual built `Roth.lem6Φ` and independent original use only propext, Classical.choice, Quot.sound.

The positive probe passed before editing; its separate final rebuilt run is recorded below.
Expected-failure negative probes are separated and cannot certify any positive gate.
No new identifiers are introduced in production, so the hallucinated-identifier table is empty.
Diff is only the three lambda arrows; original docs and public header are byte-identical.

| Gate | Result/evidence |
|---|---|
| module build | `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit 0, `module-final.log`, Theta rebuild 61s. |
| complete unfiltered fresh final LSP | `final-lsp.json`: success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors/17 baseline warnings, no target warnings. |
| definition protected | Exact type/value probes and rfl; only syntax normalization. |
| theorem statements protected | No theorem or caller changes. |
| structure | 1 body line ≤15 and ≤30; no branches. |
| naming | Protected named source constant, no forbidden pattern; no rename. |
| line packing | Full single signature row measured above, 67; body90. |
| inequality orientation | Zero relation occurrences, table above. |
| comments/docs | All original text preserved. |
| new helpers | None, so no separate helper audits needed. |
| whole build and LeanEval | Pending owner sequential gates after worker freeze; not claimed here. |

## Simplify and buzz

Simplify: PASS-THROUGH after direct holistic review; no duplicated proof skeleton or new
abstraction needed. A standalone built-in `/simplify` callable is not provided in this
environment; this is the explicit local review fallback, not a claim that tool ran.
Buzz uses the required real Lean 4.34 profiler command after all normal requests drain.
Raw final profile and final positive probe outcomes are appended below before handoff.
No maxHeartbeats changes, no native_decide/sorry/new axioms, no global attributes/instances,
and no profiling scaffolding in source. Prefix profiling certifies only the target prefix,
not a whole-module profile; owner retains the final whole-file sweep responsibility.

## Eleven-step checklist

- [x] 1: required references read.
- [x] 2: all 24 audit items documented.
- [x] 2.5: five actual search methods and limitations documented.
- [x] 2.6: every effective binder compiled drop/weakening probes, public literature/inversion.
- [x] 2.7: measured complete signature table.
- [x] 2.8: inequality scan table.
- [x] 3: all 42 rules individually addressed.
- [x] 4: step-back review and direct-expression decision.
- [x] 5a: fresh complete unfiltered LSP passed, inherited warnings disclosed.
- [x] 5b: gate table and actual module build above; final positive/profile below.
- [x] 6a: no renames needed or queued; no shared log/Git writes.

Frozen source SHA256: `ad8d2553390a9af55ecec731f216e8bab23702ec79229af1331cfe87e6f1079f`.
Source-edit authority revoked after the notation edit; only this report and scratch evidence
may be updated during the remaining gate drain.

## Final completed gate evidence and handoff

Final rebuilt `positive.lean` invocation:
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-theta-lem6Phi/positive.lean`
exited 0; raw `positive-final.log` prints exact original/current telescope and independent
value equality passed, together with actual built and independent original axiom lists:
`[propext, Classical.choice, Quot.sound]`. The pre-edit positive run also exited 0.
All six negative drop trials completed with their expected errors and overall exit 1.

Fresh final post-drain real profiler:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true \
  -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-lem6Phi/prefix.lean
```

Exit 0. The prefix preserves every exact source line through target body line271 and
adds only the required section/namespace terminators. Normal module/LSP/probe requests
were completed and their sessions drained before this single profile was launched; the
owner confirmed no competing compiler/native requests. `ps` inventory is unavailable under
the sandbox, so drain evidence is the completed tool sessions and owner coordination.
Raw UTF-8 log: `/private/tmp/roth-theta-lem6Phi/profile-final.log`.
Declaration/async/kernel anchors: `profile-anchors.txt`, raw lines418201–419148.

| Target event | Time |
|---|---:|
| outer `Elab.command` containing original docstring and `noncomputable def lem6Φ` | 10.139ms |
| associated separate `Elab.async` addDeclCore, including nested kernel check 0.275ms | 0.341ms |
| associated separate asynchronous linters | 9.272ms |
| conservative total without nested double counting | **19.752ms** |

No proof/compiler event beyond the displayed associated tasks applies to this noncomputable
data definition. FAST-BOARD: comfortably under1000ms and750ms repeat trigger; no repeat,
no performance-change claim, no deferral. Only notation changed and exact elaborated value
was certified, so an extra near-identical baseline profile would add no meaningful evidence.
The target command is not confused with the module-docstring mention of its name.

Final source SHA256 rechecked unchanged:
`ad8d2553390a9af55ecec731f216e8bab23702ec79229af1331cfe87e6f1079f`.
Overall leaf gates: PASS. Owner whole-project build, separate Roth.LeanEval, publishing,
and ultimate whole-Theta profiler sweep remain owner responsibilities and are not reported
as completed by this worker. No outstanding worker compiler/LSP/native/profile requests
remain; source edit authority remains revoked.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (65.683 s),
then separate `lake build Roth.LeanEval` (26.314 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `ad8d2553390a9af55ecec731f216e8bab23702ec79229af1331cfe87e6f1079f`.
Raw logs: `/private/tmp/roth-theta-d22-full.log`, `/private/tmp/roth-theta-d22-leaneval.log`; machine record
`/private/tmp/roth-theta-d22-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 22/35, overall 203/264 original
declarations, 9/14 completed files. No new production helper; the prior helper remains separately audited.
