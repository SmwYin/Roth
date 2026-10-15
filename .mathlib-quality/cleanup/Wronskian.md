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
| 2 | `wronskian` | 58–58 | 1 | pending |
| 3 | `wronskian_eq_zero_of_not_linearIndependent` | 63–70 | 8 | pending |
| 4 | `det_choose_eq` | 77–92 | 16 | pending |
| 5 | `sum_range_card_le_sum` | 94–104 | 11 | pending |
| 6 | `coeff_prod_of_natDegree_le'` | 106–117 | 12 | pending |
| 7 | `sum_range_le_sum_of_injective` | 121–126 | 6 | pending |
| 8 | `coeff_wronskian_of_natDegree_injective` | 134–162 | 29 | pending |
| 9 | `wronskian_ne_zero_of_natDegree_injective` | 168–175 | 8 | pending |
| 10 | `wronskian_update_sub_smul` | 181–190 | 10 | pending |
| 11 | `span_range_update_sub_le` | 192–201 | 10 | pending |
| 12 | `linearIndependent_update_sub_smul` | 207–217 | 11 | pending |
| 13 | `sum_natDegree_update_lt` | 224–246 | 23 | pending |
| 14 | `wronskian_ne_zero_of_linearIndependent` | 251–261 | 11 | pending |
| 15 | `wronskian_eq_zero_iff` | 266–269 | 4 | pending |

## Declaration 1 checkpoint

`wronskianMatrix`: Normalized lambda arrow and removed redundant explicit Fin-to-Nat ascription; original definition verified by rfl, API retained. All worker gates pass; full `lake build` session77119 and separate `lake build Roth.LeanEval` session65973 exited0. Logs `/private/tmp/roth-wronskian-d1-full.log` and `...-leaneval.log`.
