# Taylor cleanup

Baseline commit: `6c4df1d1a6644e6bbaeedad9fc50fb2ebaba5e6a`. Original file:239 lines,20 declarations.
Dialect: classic imports; existing public API and all docstrings preserved.

## Phase0 baseline

- Cache: skipped; dependencies already cached.
- Full `lake build`: session9844 exit0,2587jobs; `/private/tmp/roth-taylor-baseline.log`.
- Native complete LSP: success true,partial false, no errors; one header warning at1:2.
- Standalone runLinter: not configured; mathlib standard linters run in compilation.

## Phase2 audit punch-list

A.1 COPYRIGHT: missing authoritative metadata. User explicitly chose unchanged headers; preserve warning.
A.2 MODULE DOCSTRING: present after imports, descriptive definitions/results/references.
A.3 IMPORTS: project imports reversed; alphabetize Box before HasseDeriv in Phase3.
A.4 SECTION HEADERS: no contentless headers; CommSemiring/CommRing sections have declarations.
A.5 FILE LENGTH:239 lines, below split thresholds.
A.6 SET_OPTION: none.
A.7 MECHANICAL: zero λ/$/push_neg; mathematical `fun ... =>` arrows reviewed per declaration.
B.1 L1:2 header: Copyright too short; user-preserved limitation. No declaration warnings.
C. Per-declaration inventory/light audit below. All20 names descriptive, no forbidden abbreviations;
all17 public declarations documented; three private helpers undocumented. Preserve existing public API.
Two headline proofs require structural review: coeff_taylor35bodylines; eq_sum_box_hasseDeriv16bodylines.

| # | Declaration | Original lines | Length | Light audit | Status |
|---|---|---|---:|---|---|
| 1 | `taylor` | 36–37 | 2 | definition; naming descriptive, documentation appropriate; data definition with extensive API; normalize lambda | validated; [audit](Taylor-taylor.md) |
| 2 | `taylor_apply` | 40–41 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_apply.md) |
| 3 | `taylor_X` | 45–46 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_X.md) |
| 4 | `taylor_C` | 50–51 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_C.md) |
| 5 | `taylor_monomial` | 55–57 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 6 | `coeff_aeval_X_mul` | 59–82 | 24 | private lemma; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 7 | `hasseCoeff_single_add_eq` | 84–99 | 16 | private lemma; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 8 | `prod_pow_single_add_tsub` | 101–111 | 11 | private lemma; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 9 | `coeff_taylor` | 116–150 | 35 | public theorem; naming descriptive, documentation appropriate; headline theorem: structure review required | Pending |
| 10 | `eval_taylor` | 153–155 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 11 | `taylor_taylor` | 158–160 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 12 | `taylor_zero` | 164–165 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 13 | `taylor_map` | 169–171 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 14 | `taylor_rename` | 176–178 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 15 | `degreeOf_taylor_le` | 182–186 | 5 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 16 | `taylor_neg_taylor` | 195–197 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 17 | `taylor_injective` | 200–201 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 18 | `taylor_eq_zero_iff` | 205–206 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |
| 19 | `eq_sum_box_hasseDeriv` | 210–227 | 18 | public theorem; naming descriptive, documentation appropriate; headline theorem: structure review required | Pending |
| 20 | `eval_eq_sum_box` | 231–235 | 5 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | Pending |

## Phase3 file-level actions

Alphabetize project imports. No other file-level fix: metadata decision preserved, module documentation
and sections retained, no forbidden mechanical forms or limits to remove. Native LSP required after edit.

## Phase4 checkpoints

Pending dedicated sequential workers; each declaration requires frozen-source full build and separate
LeanEval build, then exact-path commit/push before the next source edit.

## Declaration 1 checkpoint

`taylor`: Normalized the mathematical lambda arrow; original definition verified by rfl, exact public API/docstring preserved. File-level project imports alphabetized. All worker gates pass. Frozen source SHA256 `91e0b1f92db86dacca1c06b0ae8c3e87793d5a27ffafc3070db8074caa2d40ae`. Full `lake build` session54303 and separate `lake build Roth.LeanEval` session6076 exited0. Logs `/private/tmp/roth-taylor-d01-full.log` and `...-leaneval.log`.

## Declaration 2 checkpoint

`taylor_apply`: Normalized the mathematical lambda arrow; retained the minimal rfl proof, original elaborated type and docstring. All worker gates pass. Frozen source SHA256 `b09b1665ded220e46380fb7174a024f0f5d12144caafdb60a25f107d0488f56a`. Full `lake build` session35545 and separate `lake build Roth.LeanEval` session40919 exited0. Logs `/private/tmp/roth-taylor-d02-full.log` and `...-leaneval.log`.

## Declaration 3 checkpoint

`taylor_X`: Replaced simplification with direct Mathlib aeval_X term,2 to1lines; original statement, simp attribute and docstring preserved. All worker gates pass. Frozen source SHA256 `79a3459730c972e438301e511ded297cad4e10edcef816302ad1dc21cfbb5ad1`. Full `lake build` session74936 and separate `lake build Roth.LeanEval` session95276 exited0. Logs `/private/tmp/roth-taylor-d03-full.log` and `...-leaneval.log`.

## Declaration 4 checkpoint

`taylor_C`: Replaced definition-unfolding simp with direct Mathlib algHom_C term,2 to1lines; original statement, simp attribute and docstring preserved. All worker gates pass. Frozen source SHA256 `57ed0bd46f1e97a504e63e53fb570c98045df68530f25bd8f48287ed2604ff6a`. Full `lake build` session4113 and separate `lake build Roth.LeanEval` session18089 exited0. Logs `/private/tmp/roth-taylor-d04-full.log` and `...-leaneval.log`.
