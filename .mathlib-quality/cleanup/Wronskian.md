# Wronskian cleanup

Baseline: d259f95, `ramin-cleanup`; classic dialect,271 lines,15 original declarations.

## Phase 0

- Cache fetch skipped: dependencies cached.
- Full `/Users/ramin/.elan/bin/lake build` session9164 exited0; log `/private/tmp/roth-wronskian-baseline.log`.
- Complete LSP returned success with no errors, partial=false.
- Dedicated runLinter unavailable in project; standard build/LSP linters active.

## Phase 2 audit punch-list

A.1 COPYRIGHT: missing; user explicitly chose leave unchanged. No invented metadata/suppression.
A.2 MODULE DOCSTRING: present after imports; preserve.
A.3 IMPORTS: Mathlib only, alphabetically ordered; no speculative removal.
A.4 SECTION HEADERS: none contentless; module headings preserved.
A.5 FILE LENGTH:271, below1000.
A.6 FILE-LEVEL OPTIONS: none.
A.7 MECHANICAL: zero λ/$/push_neg; ordinary lambda arrows handled per declaration.

B.1 L1 header copyright warning, preserved by user decision.
B.2 L134 unused hφ on coeff_wronskian_of_natDegree_injective: dedicated worker to verify removal proposal; do not silently change API.
B.3 L135 unused hd on same declaration: same treatment.

## Phase 3

No file-level edits required under the user-preserved header policy. Existing docs and import order retained.

## Declaration inventory and light audit

Every public declaration has an existing docstring, preserved. Private helpers have none. Names describe mathematical objects/facts, with no forbidden pattern. No instance or existential helper. Definitions name domain objects used repeatedly; not junk. All public visibility preserved pending explicit proposal. Coefficient identity is24 body lines and has an inner case branch; dedicated worker must check branch lengths and attempt simplification. Other proofs below30lines; headline det_choose_eq below15bodylines.

| # | Declaration | Original lines | Decl length | Status |
|---|---|---|---|---|
| 1 | `wronskianMatrix` | 54–55 | 2 | validated; [audit](Wronskian-wronskianMatrix.md) |
| 2 | `wronskian` | 58–58 | 1 | validated; [audit](Wronskian-wronskian.md) |
| 3 | `wronskian_eq_zero_of_not_linearIndependent` | 63–70 | 8 | validated; [audit](Wronskian-wronskian_eq_zero_of_not_linearIndependent.md) |
| 4 | `det_choose_eq` | 77–92 | 16 | validated; [audit](Wronskian-det_choose_eq.md) |
| 5 | `sum_range_card_le_sum` | 94–104 | 11 | validated; [audit](Wronskian-sum_range_card_le_sum.md) |
| 6 | `coeff_prod_of_natDegree_le'` | 106–117 | 12 | validated; [audit](Wronskian-coeff_prod_of_natDegree_le.md) |
| 7 | `sum_range_le_sum_of_injective` | 121–126 | 6 | validated; [audit](Wronskian-sum_range_le_sum_of_injective.md) |
| 8 | `coeff_wronskian_of_natDegree_injective` | 134–162 | 29 | validated; [audit](Wronskian-coeff_wronskian_of_natDegree_injective.md) |
| 9 | `wronskian_ne_zero_of_natDegree_injective` | 168–175 | 8 | validated; [audit](Wronskian-wronskian_ne_zero_of_natDegree_injective.md) |
| 10 | `wronskian_update_sub_smul` | 181–190 | 10 | validated; [audit](Wronskian-wronskian_update_sub_smul.md) |
| 11 | `span_range_update_sub_le` | 192–201 | 10 | validated; [audit](Wronskian-span_range_update_sub_le.md) |
| 12 | `linearIndependent_update_sub_smul` | 207–217 | 11 | validated; [audit](Wronskian-linearIndependent_update_sub_smul.md) |
| 13 | `sum_natDegree_update_lt` | 224–246 | 23 | pending |
| 14 | `wronskian_ne_zero_of_linearIndependent` | 251–261 | 11 | pending |
| 15 | `wronskian_eq_zero_iff` | 266–269 | 4 | pending |

## Declaration 1 checkpoint

`wronskianMatrix`: Normalized lambda arrow and removed redundant explicit Fin-to-Nat ascription; original definition verified by rfl, API retained. All worker gates pass; full `lake build` session77119 and separate `lake build Roth.LeanEval` session65973 exited0. Logs `/private/tmp/roth-wronskian-d1-full.log` and `...-leaneval.log`.

## Declaration 2 checkpoint

`wronskian`: Definition already minimal, retained unchanged; complete dedicated audit and definitional equality/type checks passed. All worker gates pass; full `lake build` session73364 and separate `lake build Roth.LeanEval` session97956 exited0. Logs `/private/tmp/roth-wronskian-d2-full.log` and `...-leaneval.log`.

## Declaration 3 checkpoint

`wronskian_eq_zero_of_not_linearIndependent`: Packed signature, normalized two lambdas and removed redundant Nat ascription; direct determinant proof and contract preserved,8lines retained. All worker gates pass; full `lake build` session22706 and separate `lake build Roth.LeanEval` session1146 exited0. Logs `/private/tmp/roth-wronskian-d3-full.log` and `...-leaneval.log`.

## Declaration 4 checkpoint

`det_choose_eq`: Oriented the scaling equality toward the transposed evaluation matrix, removed redundant h2 and normalized lambdas; declaration16→13lines, statement preserved. All worker gates pass; full `lake build` session6371 and separate `lake build Roth.LeanEval` session37787 exited0. Logs `/private/tmp/roth-wronskian-d4-full.log` and `...-leaneval.log`.

## Declaration 5 checkpoint

`sum_range_card_le_sum`: Packed signature to100codepoints and normalized lambdas/ascription;11→10lines. Verified Mathlib replacement queued for Phase5a, public API unchanged. All worker gates pass; full `lake build` session4157 and separate `lake build Roth.LeanEval` session51137 exited0. Logs `/private/tmp/roth-wronskian-d5-full.log` and `...-leaneval.log`.

## Declaration 6 checkpoint

`coeff_prod_of_natDegree_le'`: Simplified the inserted-bound premise once and reused projections, eliminating repeated membership lambdas;12→11lines, exact signature preserved. All worker gates pass; full `lake build` session84949 and separate `lake build Roth.LeanEval` session56529 exited0. Logs `/private/tmp/roth-wronskian-d6-full.log` and `...-leaneval.log`.

## Declaration 7 checkpoint

`sum_range_le_sum_of_injective`: Replaced single-use h/rwa with direct simpa and hd.injOn, removed unnecessary classical;6→4lines with original contract retained. All worker gates pass; full `lake build` session28169 and separate `lake build Roth.LeanEval` session83466 exited0. Logs `/private/tmp/roth-wronskian-d7-full.log` and `...-leaneval.log`.

## Declaration 8 checkpoint

`coeff_wronskian_of_natDegree_injective`: Eliminated hD through direct sum rewrites and replaced final simp-only/ring with terminal simp;29→22lines,18bodylines. Both unused hypotheses retained pending explicit user decision on compiled removal proposal and sole caller repair. All worker gates pass; full `lake build` session10237 and separate `lake build Roth.LeanEval` session38808 exited0. Logs `/private/tmp/roth-wronskian-d8-full.log` and `...-leaneval.log`.

## Declaration 9 checkpoint

`wronskian_ne_zero_of_natDegree_injective`: Direct simpa from coefficient identity replaces h1/rewrite chain, signature packed and redundant cast removed;8→5lines. Final-source closure rerun after premature freeze, earlier full36477 not counted. All worker gates pass; full `lake build` session80038 and separate `lake build Roth.LeanEval` session58989 exited0. Logs `/private/tmp/roth-wronskian-d9-full-final.log` and `...-leaneval.log`.

## Declaration 10 checkpoint

`wronskian_update_sub_smul`: Composed determinant congruence with Mathlib column-operation invariance and used one terminal conditional simp;10→7lines, signature/documentation unchanged. All worker gates pass; full `lake build` session21216 and separate `lake build Roth.LeanEval` session9301 exited0. Logs `/private/tmp/roth-wronskian-d10-full.log` and `...-leaneval.log`.

## Declaration 11 checkpoint

`span_range_update_sub_le`: Reduced span-membership proof to structural rewrites and aesop;10→5lines, exact signature unchanged. Compiled Mathlib span-update equality replacement in sole caller queued for Phase5a helper deletion. All worker gates pass; full `lake build` session15006 and separate `lake build Roth.LeanEval` session18366 exited0. Logs `/private/tmp/roth-wronskian-d11-full.log` and `...-leaneval.log`.

## Declaration 12 checkpoint

`linearIndependent_update_sub_smul`: Replaced inverse-update/span machinery with direct Mathlib span preservation,11→6lines and8→3bodylines; signature/docs unchanged. Private span helper now unused, scheduled for Phase5a deletion. All worker gates pass; full `lake build` session37876 and separate `lake build Roth.LeanEval` session72281 exited0. Logs `/private/tmp/roth-wronskian-d12-full.log` and `...-leaneval.log`.
