# Reproducing this assessment's checks

Run source checks from the project root at the recorded source snapshot and pins:

```sh
python3 .mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/evidence/collect-sources.py
python3 .mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/evidence/audit-sources.py
```

The source collector verifies all 17 production/pin hashes against `input-manifest.json`
and refreshes excerpts/whole-source identities. The caller collector uses the supplied
reviewed declaration boundaries, strips nested comments, and disambiguates the separate
univariate `Wronskian.lean` uses. It records explicit source references, not hidden/simp
dependency closure. A changed source snapshot requires reviewing caller boundaries again.

Compiler checks were actually run by the root agent through separate persistent native
Lean documents. The raw native request/results in `evidence/` retain the actual paths,
success/partial/error fields and diagnostics. `probes/` contains exact executed sources.
The Mathlib-only probe must remain isolated: do not add a `Roth` import or import another
scratch module that defines the target.

For a future command-line reproduction, use the recorded toolchain from the project root:

```sh
lake env lean .mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/probes/TargetRisk.lean
lake env lean .mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/probes/MathlibOnly.lean
```

These are reproduction instructions, not a claim that this assessment redundantly ran
CLI compilers. No `maxHeartbeats`, recursion limit, axiom or trust override is needed.
Native receipts remain the historical evidence even if a later snapshot changes output.

`evidence/search-requests.json` has exact mathematical search API arguments and raw-result
filenames. `evidence/literature-queries.json` and the web/open records have actual queries,
titles, URLs, access failures and original concise analysis. Optional ChatGPT was unavailable;
the local elaborated name index was unavailable and only its actual source fallback was used.

Copy `report.md` to the mathlibable report path; copy every other file in the accompanying
`copy-manifest.json` into the evidence directory, preserving `evidence/` and `probes/`.
