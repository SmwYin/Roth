# Approved Finite warning follow-up

Entry: clean published `49e593d`. The user explicitly approved replacing `[Fintype σ]` by
`[Finite σ]` for `exists_genWronskian_ne_zero` and `[Fintype τ]` by `[Finite τ]` for
`exists_det_eq_mul`. Finiteness, conclusions, other hypotheses, documentation, names and
pins are preserved. Enumeration is constructed locally only where the existing proof needs it.
This is a two-theorem amendment; no original-declaration audit or count is reopened.

## Checkpoint 1: GenWronskian

The section Fintype instance is omitted from `exists_genWronskian_ne_zero`; its new Finite
instance supports a local `Fintype.ofFinite σ`, followed by the unchanged proof. Its sole
project caller, a private Separation helper already accepting Finite, no longer needs its
local enumeration. Complete diagnostics pass: GenWronskian has only its header warning;
Separation has its header and the pending second-theorem Fintype warning.
Fresh independent Astra HIGH review confirms the exact authorized patch and unchanged
conclusion, other hypotheses, documentation and proof: PASS, no actionable finding.
**PASS:** full project build (exit 0, 139.096 s), subsequent separate LeanEval build
(exit 0, 31.650 s), and exact old-contract/new-independent-proof/body/axiom audit (exit 0,
78.323 s). All 28 actual GenWronskian and 36 Separation constants use only standard axioms.
Both required whole-file performance samples pass as recorded below. Checkpoint 1 was
published as `0bd9ce1`; the second theorem and final gates follow.

## Evidence

Scratch: `/private/tmp/roth-finite-amendment/`. The exact clean entry's fourteen sources and
three configuration/pin files are recorded under `before/` and `source-before.json`.
The actual two original complete TYPE/VALUE records were captured and checked by `Before.lean`
(exit 0, 62.150 s). Cumulative compiler probes recover the exact old contracts (including
binder order, modulo universe-name alpha-renaming), independently replay the new proofs,
infer actual opaque bodies, and check closedness and standard axioms without raised limits.

## GenWronskian performance

PASS: 19/19 written declaration payloads matched; all 28 actual module constants have
kernel coverage. All measured rows are strictly below 1,000 ms. Maxima: 877.750 ms / 943.543 ms.
The first sample required a same-source repeat because a row reached 750 ms. Both pass.
Actual whole-file command: `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/GenWronskian.lean`; wall times: 82.230 s / 84.893 s.
All source, direct imported project objects and pins remained frozen. Timing sums disjoint
outer command/asynchronous/root costs, including nested kernel costs once via their parents.
Pretty-printed payload matching normalizes whitespace, standalone comments and, when needed,
parentheses; remaining tokens agree. On-demand equation checks retain their caller costs.
No speedup or unmeasured performance claim is made.

| Declaration | Line | A (ms) | B (ms) | Dominant outer category, A |
|---|---:|---:|---:|---|
| `genWronskian` | 26 | 61.707 | 83.384 | `Elab.async` |
| `genWronskian_eq_zero_of_not_linearIndependent` | 35 | 551.980 | 637.603 | `Elab.async` |
| `kronecker` | 47 | 27.221 | 35.351 | `Elab.command` |
| `kroneckerExp` | 51 | 29.977 | 19.885 | `Elab.async` |
| `kronecker_monomial` | 54 | 189.146 | 214.247 | `Elab.async` |
| `kroneckerExp_injOn` | 63 | 159.668 | 185.404 | `Elab.async` |
| `coeff_kronecker` | 82 | 122.630 | 133.751 | `Elab.async` |
| `kronecker_eq_zero_iff` | 100 | 117.304 | 109.938 | `Elab.async` |
| `linearIndependent_kronecker` | 111 | 427.405 | 495.273 | `Elab.async` |
| `derivative_aeval` | 127 | 799.775 | 855.515 | `Elab.async` |
| `kronHasse` | 139 | 30.222 | 31.867 | `Elab.command` |
| `kronSpan` | 143 | 28.228 | 22.019 | `Elab.command` |
| `derivative_kronHasse_aux` | 147 | 877.750 | 943.543 | `Elab.async` |
| `derivative_mem_kronSpan` | 156 | 353.652 | 363.377 | `Elab.async` |
| `hasseDeriv_kronecker_mem` | 184 | 448.742 | 466.512 | `Elab.async` |
| `exists_hasseDeriv_kronecker_eq_sum` | 208 | 175.998 | 183.226 | `Elab.async` |
| `det_sum_rows` | 222 | 182.804 | 162.442 | `Elab.async` |
| `wronskian_kronecker_eq_sum_aux` | 232 | 431.088 | 447.320 | `Elab.async` |
| `exists_genWronskian_ne_zero` | 248 | 342.714 | 356.841 | `Elab.async` |

The initial profile parser inventory omitted the two `private noncomputable` definitions;
its prefix handling was corrected before accepting the sweep. Both final complete streams
cover all 19 written declarations and all 28 actual constants. No production compile failed.

## Checkpoint 2: Separation

`exists_det_eq_mul` now omits the section Fintype and accepts Finite directly. Its complete
proof, conclusion, other hypotheses and docstring are unchanged; no local enumeration is
needed. Complete Separation diagnostics show zero errors and only its existing header warning.
Fresh independent final source review: **PASS**, no actionable finding. Exact inverse-patch
checks recover both original files byte-for-byte; all other sources and pins are unchanged.
Full project build passes (exit 0, 152.422 s), followed by the separate LeanEval build
(exit 0, 29.314 s). Cumulative exact old-contract/new-independent-proof/body checks pass
(exit 0, 77.196 s), with only standard axioms for all 64 actual constants across both modules.
The actual full-build warning inventory is twelve header metadata warnings; both Fintype
warnings are resolved. Both Separation profiles and final complete native diagnostics pass.

## Separation performance

PASS: 27/27 written declaration payloads matched; all 36 actual module constants have
kernel coverage. All measured rows are strictly below 1,000 ms. Maxima: 755.157 ms / 804.818 ms.
The first sample required a same-source repeat because a row reached 750 ms. Both pass.
Actual whole-file command: `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Separation.lean`; wall times: 126.022 s / 129.833 s.
All source, direct imported project objects and pins remained frozen. Timing sums disjoint
outer command/asynchronous/root costs, including nested kernel costs once via their parents.
Pretty-printed payload matching normalizes whitespace, standalone comments and, when needed,
parentheses; remaining tokens agree. On-demand equation checks retain their caller costs.
No speedup or unmeasured performance claim is made.

| Declaration | Line | A (ms) | B (ms) | Dominant outer category, A |
|---|---:|---:|---:|---|
| `eq_mapDomain_some_add_single` | 51 | 136.924 | 162.214 | `Elab.async` |
| `coeff_X_none_pow_mul_rename` | 58 | 241.285 | 244.897 | `Elab.async` |
| `coeffNone` | 74 | 26.776 | 30.361 | `Elab.async` |
| `coeff_coeffNone` | 79 | 125.945 | 117.991 | `Elab.async` |
| `eq_sum_X_none_pow_mul_coeffNone` | 92 | 112.412 | 111.700 | `Elab.async` |
| `degreeOf_coeffNone_le` | 108 | 46.237 | 48.067 | `Elab.async` |
| `coeff_rename_mul_aeval` | 117 | 202.682 | 206.289 | `Elab.async` |
| `aeval_X_eq_rename` | 131 | 44.147 | 43.454 | `Elab.async` |
| `hasseDeriv_rename_mul_aeval` | 140 | 400.149 | 372.064 | `Elab.async` |
| `coeff_uniqueAlgEquiv_symm` | 163 | 35.743 | 36.885 | `Elab.command` |
| `degreeOf_uniqueAlgEquiv_symm` | 168 | 58.760 | 50.524 | `Elab.async` |
| `degreeOf_rename_mul_aeval` | 191 | 164.551 | 145.511 | `Elab.async` |
| `degreeOf_none_rename_mul_aeval` | 207 | 179.563 | 180.071 | `Elab.async` |
| `linearIndependent_coordinate_polynomials_aux` | 229 | 313.970 | 324.283 | `Elab.async` |
| `eq_sum_aeval_basis_coeffNone_aux` | 259 | 755.157 | 804.818 | `Elab.async` |
| `exists_coeffNone_basis_aux` | 285 | 729.930 | 757.167 | `Elab.async` |
| `exists_separated_representation` | 319 | 417.319 | 423.533 | `Elab.async` |
| `det_hasseDeriv_separated` | 345 | 456.498 | 484.600 | `Elab.async` |
| `exists_sum_mul_eq_gcd` | 368 | 83.327 | 91.245 | `Elab.async` |
| `exists_nat_smul_eq_map` | 374 | 321.827 | 332.859 | `Elab.async` |
| `exists_primitive_smul_eq` | 400 | 638.552 | 674.311 | `Elab.async` |
| `exists_int_eq_of_gcd_eq_one` | 437 | 146.229 | 142.208 | `Elab.async` |
| `rescale_separated_factor_aux` | 451 | 258.712 | 265.085 | `Elab.async` |
| `exists_int_polynomial_of_primitive_factor_aux` | 460 | 307.198 | 315.551 | `Elab.async` |
| `exists_int_factors` | 479 | 589.238 | 601.910 | `Elab.async` |
| `exists_rat_factors_det_hasseDeriv_aux` | 504 | 509.676 | 549.196 | `Elab.async` |
| `exists_det_eq_mul` | 536 | 320.213 | 261.110 | `Elab.async` |

## Final validation and publication handoff

**PASS.** Checkpoint 1 is published as `0bd9ce1`. The final checkpoint combines the
validated second theorem with the separately approved [header amendment](Header-warning-amendment.md).
The following evidence records the Finite changes before the header-only additions;
subsequent warning-free builds are recorded in that header report.

- Final full project build: exit 0, 152.422 s; subsequent separate LeanEval build:
  exit 0, 29.314 s. The actual warning inventory is **12**, all existing header metadata
  warnings, down from 14. Both targeted Fintype warnings are absent; none was suppressed.
- Complete native GenWronskian/Separation/Theta/MainLemma/Main/LeanEval/root diagnostics:
  success, nonpartial, no timeout or failed dependency, zero errors. The first five have
  only their header warning; LeanEval and root are clean.
- Full original compiler types are compared by definitional equality after aligning universe
  names. Old Fintype contracts (including binder order) are recovered through adapters;
  independent proofs establish the actual new Finite types. Actual opaque bodies are closed
  and inferred against their types. All 64 module constants use only standard axioms;
  default resource limits are unchanged.
- Fresh independent review of both sequential patches passes with no actionable finding.
  This is the available substitute for `/simplify`; no unavailable invocation is claimed.
- Both whole-file performance pairs pass all 46 written rows and cover all 64 actual constants.
  GenWronskian maxima: 877.750 / 943.543 ms; Separation: 755.157 / 804.818 ms.
  GenWronskian source, direct imported objects and pins still match its accepted profiles
  after the subsequent downstream Separation edit. No repeat beyond the required pair was run.
- Exact inverse patches recover the two entry source files byte-for-byte. The other twelve
  sources and all three pins remain unchanged at this handoff. Documentation, imports,
  conclusions and other hypotheses are preserved; only the two instance requirements and
  the corresponding local enumerations change. GenWronskian has 266 lines, Separation 555;
  both remain within 100 columns with no trailing whitespace or trust/resource escape.

Scratch evidence includes `Audit2.lean`, `step2-contracts` and `final-{build,eval-build}`
receipts/raw streams, module constant inventories, `step1-diagnostics.json`,
`final-diagnostics.json`, `source-final.json`, `final-warning-inventory.json`, and all four
complete profile receipts/streams/row inventories. Earlier exhaustive audits and unchanged
source evidence remain accepted; no new original-declaration credit or broader audit is claimed.
No Finite source change or required validation remains. The approved header additions
preserve the validated Lean source bytes after their six-line comment prefixes.
