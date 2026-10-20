# Original17 literature addendum

This is a later metadata-only correction after the original17 END. Owner review found
that the dispatch required three literature queries with their top three results, while
the frozen report recorded only two. The original report and manifest are preserved
byte-for-byte; this addendum does not imply the new searches occurred before the API edit,
independent proof, profiling, or original release.

The third actual query was:
`site.stacks.math.columbia.edu polynomial ring infinitely many variables monomials finite support`.
Its actual top three results, in returned order, were:

1. [Stacks commutative algebra PDF](https://stacks.math.columbia.edu/download/algebra.pdf).
2. [Stacks054A, Flatness and finiteness conditions](https://stacks.math.columbia.edu/tag/054A).
3. [Wikipedia, Polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring).

This repeated the first historical query's top-three URLs. The Stacks algebra result
uses finite products of variables to describe monomials with infinite ambient indexing;
this is consistent with the selected finite-support formulation. It is not an exact
finite-box theorem. The flatness result concerns module presentation, so it supplies no
replacement for this proof. Wikipedia is retained only as an actual returned result and
is not used as proof evidence.

To seek more specific alternatives, an additional actual follow-up query was:
`site.leanprover-community.github.io/mathlib4_docs MvPolynomial restrictDegree finite coefficients finite_of_degree_le`.
Its actual top three results were:

1. [Mathlib4 RingTheory.MvPolynomial.Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPolynomial/Basic.html).
2. [Mathlib4 FieldTheory.Finite.Polynomial, .html URL](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Polynomial.html).
3. [Mathlib4 FieldTheory.Finite.Polynomial, extensionless URL](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Polynomial).

The latter two are duplicate documentation routes, retained rather than silently
replaced by another result. The Basic documentation's degree-restricted finite-module
instance assumes finite ambient indices and concerns Module.Finite. It does not directly
establish set finiteness of integer polynomials with finite coefficient choices and
finite support of coordinate bounds. The finite-field result concerns evaluation over a
finite field, also a different coefficient domain and property. These are consistent with
the partial standard alternatives already considered. This is an inference from the
returned documented signatures, not a new compiled API verification. No finding warrants
a source change; the existing Finset.finsupp enumeration remains appropriate. No compiler,
native, profile, or Git command was run in this metadata-only resume.

Both complete actual raw tool results and exact queries/top3 metadata are saved in
`/private/tmp/roth-mainlemma-box-family-finite-literature-addendum`. The supplementary
manifest binds those new files, this addendum, the unchanged original report/manifest,
and the original22-PGID absence check. All423 old local manifest references and24793
external current catalog references were actually rehashed unchanged at this correction;
that does not change their original provenance timing or catalog scope. Final source
remains `ff29cc40cece7f7432c7a2ddc64fd9cc73ceafd995b37b6927b7f3d2897bbac7`.
