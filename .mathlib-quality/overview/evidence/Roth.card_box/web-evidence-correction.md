# Web evidence URL correction — 2026-10-26

GitHub reported an AWS temporary-access-key identifier in the returned URL list of
`Roth.card_box/web-0.json`, originally published in commit `ac31324`.
The web search returned a third-party S3 signed download URL. Its query contained
credential material and its stated URL expiration was 2026-02-28 17:02:45 UTC.
The signed URL was not accessed or tested during this investigation.

Removed the entire query and fragment from that one returned URL, retaining the
base URL. Exact search requests, response SHA256/byte counts, mathematical findings,
Lean evidence, declaration verdict, and production sources remain unchanged.
Updated the current evidence manifest and independent acceptance hashes. The
original artifact hash is retained for provenance without reproducing credentials.
The historical worker manifest remains historical, not the current validation source.

A targeted scan of all Git-tracked text found one affected current file. Added
`scan_evidence_secrets.py` as a publication guard for credential-shaped values and
credential-bearing URLs. This guard also checks incoming assessment packages; it
is not an exhaustive security audit or a guarantee against every possible secret.

The correction is a normal commit on `ramin-cleanup`; earlier Git history still
contains the original URL. No history rewrite or force-push was performed.
GitHub's secret-scanning alert API returned HTTP 404 for the current account, so
the alert was not closed. A repository owner/security manager can inspect the
existing alert. URL expiration is established from metadata; credential validity
was not tested and no third-party credential was revoked.
