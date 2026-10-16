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
| 5 | `taylor_monomial` | 55–57 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_monomial.md) |
| 6 | `coeff_aeval_X_mul` | 59–82 | 24 | private lemma; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-coeff_aeval_X_mul.md) |
| 7 | `hasseCoeff_single_add_eq` | 84–99 | 16 | private lemma; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-hasseCoeff_single_add_eq.md) |
| 8 | `prod_pow_single_add_tsub` | 101–111 | 11 | private lemma; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-prod_pow_single_add_tsub.md) |
| 9 | `coeff_taylor` | 116–150 | 35 | public theorem; naming descriptive, documentation appropriate; headline theorem: structure review required | validated; [audit](Taylor-coeff_taylor.md) |
| 10 | `eval_taylor` | 153–155 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-eval_taylor.md) |
| 11 | `taylor_taylor` | 158–160 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_taylor.md) |
| 12 | `taylor_zero` | 164–165 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_zero.md) |
| 13 | `taylor_map` | 169–171 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_map.md) |
| 14 | `taylor_rename` | 176–178 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_rename.md) |
| 15 | `degreeOf_taylor_le` | 182–186 | 5 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-degreeOf_taylor_le.md) |
| 16 | `taylor_neg_taylor` | 195–197 | 3 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_neg_taylor.md) |
| 17 | `taylor_injective` | 200–201 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_injective.md) |
| 18 | `taylor_eq_zero_iff` | 205–206 | 2 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-taylor_eq_zero_iff.md) |
| 19 | `eq_sum_box_hasseDeriv` | 210–227 | 18 | public theorem; naming descriptive, documentation appropriate; headline theorem: structure review required | validated; [audit](Taylor-eq_sum_box_hasseDeriv.md) |
| 20 | `eval_eq_sum_box` | 231–235 | 5 | public theorem; naming descriptive, documentation appropriate; check packing, proof reuse and lambda style | validated; [audit](Taylor-eval_eq_sum_box.md) |

## Phase3 file-level actions

Alphabetize project imports. No other file-level fix: metadata decision preserved, module documentation
and sections retained, no forbidden mechanical forms or limits to remove. Native LSP required after edit.

## Phase4 checkpoints

Completed dedicated sequential workers for all20 originals and both added helpers, each with
frozen-source full build, separate LeanEval and exact-path commit/push before the next source edit.

## Declaration 1 checkpoint

`taylor`: Normalized the mathematical lambda arrow; original definition verified by rfl, exact public API/docstring preserved. File-level project imports alphabetized. All worker gates pass. Frozen source SHA256 `91e0b1f92db86dacca1c06b0ae8c3e87793d5a27ffafc3070db8074caa2d40ae`. Full `lake build` session54303 and separate `lake build Roth.LeanEval` session6076 exited0. Logs `/private/tmp/roth-taylor-d01-full.log` and `...-leaneval.log`.

## Declaration 2 checkpoint

`taylor_apply`: Normalized the mathematical lambda arrow; retained the minimal rfl proof, original elaborated type and docstring. All worker gates pass. Frozen source SHA256 `b09b1665ded220e46380fb7174a024f0f5d12144caafdb60a25f107d0488f56a`. Full `lake build` session35545 and separate `lake build Roth.LeanEval` session40919 exited0. Logs `/private/tmp/roth-taylor-d02-full.log` and `...-leaneval.log`.

## Declaration 3 checkpoint

`taylor_X`: Replaced simplification with direct Mathlib aeval_X term,2 to1lines; original statement, simp attribute and docstring preserved. All worker gates pass. Frozen source SHA256 `79a3459730c972e438301e511ded297cad4e10edcef816302ad1dc21cfbb5ad1`. Full `lake build` session74936 and separate `lake build Roth.LeanEval` session95276 exited0. Logs `/private/tmp/roth-taylor-d03-full.log` and `...-leaneval.log`.

## Declaration 4 checkpoint

`taylor_C`: Replaced definition-unfolding simp with direct Mathlib algHom_C term,2 to1lines; original statement, simp attribute and docstring preserved. All worker gates pass. Frozen source SHA256 `57ed0bd46f1e97a504e63e53fb570c98045df68530f25bd8f48287ed2604ff6a`. Full `lake build` session4113 and separate `lake build Roth.LeanEval` session18089 exited0. Logs `/private/tmp/roth-taylor-d04-full.log` and `...-leaneval.log`.

## Declaration 5 checkpoint

`taylor_monomial`: Replaced simp and definition unfolding with direct Mathlib aeval_monomial term; mathematical lambda normalized,3lines retained, original contract/docstring preserved. All worker gates pass. Frozen source SHA256 `a913c9258bdcb0630d0d3398f34626f52c2d9f9504a7077e443ef2f24f1090a4`. Full `lake build` session63285 and separate `lake build Roth.LeanEval` session31201 exited0. Logs `/private/tmp/roth-taylor-d05-full.log` and `...-leaneval.log`.

## Declaration 6 checkpoint

`coeff_aeval_X_mul`: Direct evaluation expansion and Finsupp erase cancellation replace two intermediate proofs; single-use inequality inlined,24 to18lines, exact statement retained. All worker gates pass. Frozen source SHA256 `f4a686acc2e188a3bea162eb6bff0afd5079cd162d2297afbe1ce2b0d830529a`. Full `lake build` session53572 and separate `lake build Roth.LeanEval` session61138 exited0. Logs `/private/tmp/roth-taylor-d06-full.log` and `...-leaneval.log`.

## Declaration 7 checkpoint

`hasseCoeff_single_add_eq`: Used Mathlib mul_prod_erase and support_erase to remove explicit disjointness and case splitting; packed unchanged signature,16 to9lines. All worker gates pass. Frozen source SHA256 `72a52b08db494fd445a13c5716fc1afd32fbf315b1e41dccffe81f230ef1f7bd`. Full `lake build` session6797 and separate `lake build Roth.LeanEval` session18199 exited0. Logs `/private/tmp/roth-taylor-d07-full.log` and `...-leaneval.log`.

## Declaration 8 checkpoint

`prod_pow_single_add_tsub`: Terminal simp replaces rewrite/congr/exact assembly with local single_tsub exclusion; lambda syntax and signature packed,11 to8lines, original contract preserved. All worker gates pass. Frozen source SHA256 `58a982948ba48df089ea5e4a00e8050fb00566e381e9a942279484ac88e0818e`. Full `lake build` session26690 and separate `lake build Roth.LeanEval` session78586 exited0. Logs `/private/tmp/roth-taylor-d08-full.log` and `...-leaneval.log`.

## Declaration 9 checkpoint

`coeff_taylor`: Separated monomial expansion into two private helpers; headline33 to3bodylines, original public contract/docs preserved, source net+2lines. New helpers await fresh dedicated audits. All worker gates pass. Frozen source SHA256 `339ca8621ef76a233dab2c5f86002e6a1016b9116616266e78b9a5d311177b39`. Full `lake build` session19265 and separate `lake build Roth.LeanEval` session62727 exited0. Logs `/private/tmp/roth-taylor-d09-full.log` and `...-leaneval.log`.

## Added helper1 checkpoint

Fresh GPT-6 Astra Medium worker independently audited `coeff_taylor_monomial_single_add_aux`
under the user-requested model setting. Removed redundant classical and a redundant terminal
simp argument;19→18declarationlines, exact signature retained. All24audit/42rules/search/
generalisation/width/inequality/checklist artifacts and module/completeLSP/isolatedproof/type/
standardaxiom gates pass. [Dedicated audit](Taylor-coeff_taylor_monomial_single_add_aux.md).
Full `lake build` session38813 and separate `lake build Roth.LeanEval` session94812 exit0
(2587/2586jobs); `/private/tmp/roth-taylor-newhelper01-{full,leaneval}.log`.
Frozen source SHA256 `9a4189e83c942dbf021d9c6f831a4d4a17384e5b7ad8a88e1ded62dbba73cdd8`.
Original tally unchanged: Taylor9/20, overall64/264. Second new helper audit remains pending.

## Added helper2 checkpoint

Fresh GPT-6 Astra Medium worker independently audited `coeff_taylor_monomial_aux`.
Existing hasseDeriv_C replaces manual constant-case coefficient expansion and vanishing;
11→10declarationlines, exact signature retained. All24audit/42rules/search/generalisation/
width/inequality/checklist artifacts and module/completeLSP/isolatedproof/type/standardaxiom
gates pass. [Dedicated audit](Taylor-coeff_taylor_monomial_aux.md).
Full `lake build` session74901 and separate `lake build Roth.LeanEval` session24217 exit0
(2587/2586jobs); `/private/tmp/roth-taylor-newhelper02-{full,leaneval}.log`.
Frozen source SHA256 `61807d7fe836eb95dbcea48055b0c9a5f5747d3c98b8d15f0d82fe33aee3f81d`.
Both added helpers now have fresh dedicated audits/publication gates; original tally remains
Taylor9/20, overall64/264. Original declaration10 resumes next.
LeanSearch recovered in this audit and returned a verified univariate partial match; this
supersedes the earlier service-unavailable status for future searches without claiming an
environment repair.

## Declaration 10 checkpoint

`eval_taylor`: Direct Mathlib evaluation composition replaces induction; lambda arrow normalized,3 declaration lines retained, exact public contract and docstring preserved. All worker gates pass. Frozen source SHA256 `fbd691573b1e1fa3dd2c4f33449095583791028ee6cbd25a8d92df2175e9ab39`. Full `lake build` session26144 and separate `lake build Roth.LeanEval` session9704 exited0. Logs `/private/tmp/roth-taylor-d10-full.log` and `...-leaneval.log`.

## Declaration 11 checkpoint

`taylor_taylor`: Direct Mathlib algebra evaluation composition replaces induction; lambda normalized, exact public contract and documentation retained. All worker gates pass. Frozen source SHA256 `c3b13e052d8ffa6af70404bf29d2853cce67a99b36cd0dc4a8584f5bfbf23020`. Full `lake build` session87659 and separate `lake build Roth.LeanEval` session70984 exited0. Logs `/private/tmp/roth-taylor-d11-full.log` and `...-leaneval.log`.

## Declaration 12 checkpoint

`taylor_zero`: Direct Mathlib identity-evaluation simplification replaces induction; equivalent lambda notation normalized, original public API and docstring preserved. All worker gates pass. Frozen source SHA256 `a2f43a6a92cc7e8cee595b4fdb1047638cc7f8a9d1d031e050f72a95f086a6af`. Full `lake build` session11614 and separate `lake build Roth.LeanEval` session44120 exited0. Logs `/private/tmp/roth-taylor-d12-full.log` and `...-leaneval.log`.

## Declaration 13 checkpoint

`taylor_map`: Evaluation-map naturality replaces polynomial induction; equivalent lambda notation normalized, exact public API and docs retained. All worker gates pass. Frozen source SHA256 `d4a821b4ee428a5e8b052cb7a6cd0a62a9830b3fdb5a3d78557b86bd29d2dd74`. Full `lake build` session53057 and separate `lake build Roth.LeanEval` session18619 exited0. Logs `/private/tmp/roth-taylor-d13-full.log` and `...-leaneval.log`.

## Declaration 14 checkpoint

`taylor_rename`: Direct substitution composition replaces induction; exact public signature and documentation unchanged. All worker gates pass. Frozen source SHA256 `4cd871acc4a0ad26ceba2c01bef9ee5c88e0f5117254a50d24a895b56af32f7a`. Full `lake build` session21806 and separate `lake build Roth.LeanEval` session71085 exited0. Logs `/private/tmp/roth-taylor-d14-full.log` and `...-leaneval.log`.

## Declaration 15 checkpoint

`degreeOf_taylor_le`: Retained direct coefficient-vanishing degree proof after search; normalized two mathematical lambda arrows, exact signature and docs preserved. All worker gates pass. Frozen source SHA256 `1f69c55d06c8b562930bb9bbc90e9ab3a676f2491d6ddbf4f8dd4c08b8fe3de8`. Full `lake build` session9544 and separate `lake build Roth.LeanEval` session22563 exited0. Logs `/private/tmp/roth-taylor-d15-full.log` and `...-leaneval.log`.

## Declaration 16 checkpoint

`taylor_neg_taylor`: Retained minimal composition-cancellation simp; normalized lambda and packed signature, exact mathematical type and docstring preserved. All worker gates pass. Frozen source SHA256 `0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`. Full `lake build` session58028 and separate `lake build Roth.LeanEval` session88498 exited0. Logs `/private/tmp/roth-taylor-d16-full.log` and `...-leaneval.log`.

## Declaration 17 checkpoint

`taylor_injective`: Retained direct LeftInverse.injective proof after tested alternatives; no source change, complete dedicated audit and exact API verification. All worker gates pass. Frozen source SHA256 `0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`. Full `lake build` session30998 and separate `lake build Roth.LeanEval` session69947 exited0. Logs `/private/tmp/roth-taylor-d17-full.log` and `...-leaneval.log`.

## Declaration 18 checkpoint

`taylor_eq_zero_iff`: Retained minimal injectivity eq_iff term after compiled alternatives; no source change, exact public simp API and docs verified. All worker gates pass. Frozen source SHA256 `0a6ab3437c5950f4d2e800b78f03e7a53b7ce97f6cc248c3bff71fcf00a46f22`. Full `lake build` session21654 and separate `lake build Roth.LeanEval` session88267 exited0. Logs `/private/tmp/roth-taylor-d18-full.log` and `...-leaneval.log`.

## Declaration 19 checkpoint

`eq_sum_box_hasseDeriv`: Consolidated coefficient rewriting into one squeezed simp, reducing headline proof16 to15 lines including by; lambdas normalized, no helper or public contract change. All worker gates pass. Frozen source SHA256 `eda896cd346e776d923237cdc4235045d1dd2e4fe32a8d039f561ca6068221a6`. Full `lake build` session8153 and separate `lake build Roth.LeanEval` session30826 exited0. Logs `/private/tmp/roth-taylor-d19-full.log` and `...-leaneval.log`.

## Declaration 20 checkpoint

`eval_eq_sum_box`: Applied evaluation congruence directly with simpa; body2 to1lines and signature packed, exact public type/docs preserved. All worker gates pass. Frozen source SHA256 `4878106187d61fe102f4f1b52582772cbc6938085e3e1e1845843279cfd356de`. Full `lake build` session80735 and separate `lake build Roth.LeanEval` session37852 exited0. Logs `/private/tmp/roth-taylor-d20-full.log` and `...-leaneval.log`.

## Taylor independent simplify checkpoint

Fresh GPT-6.1 Sol Medium review found one compiled degree-bound proof improvement, now applied: terminal simp replaces rw/contradiction,3→2bodylines. [Review](Taylor-simplify.md) in the cleanup directory. Final source218lines, original20/20 and overall75/264 unchanged. Module87739/full91300/separateLeanEval69418 exit0, complete LSP only preserved header warning, exact17publicconstant compatibility session7752 exit0. Frozen SHA256 `31af75afd28f840ddee51978509ba63b28536aa84bba56dc047df2aa4b23fbdc`. Profiling and final report remain pending.

## Final file-level completion

All final phases complete; [consolidated final report](Taylor-final.md) supersedes historical pending notes. Final source218lines, all17 public constants compare by rfl against baseline, docs byte-identical. Fresh independent review fix applied and fully revalidated. Actual profiler covers22 retained declarations; maximum672.30ms, all below750ms. No pending refactor or rename; header warning preserved by user decision. Overall75/264 original declarations.
