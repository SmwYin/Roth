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
Both required whole-file performance samples pass as recorded below. Checkpoint 1 is ready
for publication; the second public theorem and final inventory/report remain pending.

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
