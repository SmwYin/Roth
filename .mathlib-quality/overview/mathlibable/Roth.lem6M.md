# Roth.lem6M — canonical182

**BORDERLINE-needs-human.** Keep this named coefficient envelope in `Roth/Theta.lean`. It is useful local notation with six explicit consuming declarations, but an independently reusable upstream object has not been established. No existing parameterized mathlib replacement or composition of at most three existing calls was identified. These are upstream scope questions, not outstanding verification tasks; production is unchanged.

## Phase 0 — baseline

`noncomputable def Roth.lem6M`, `Roth/Theta.lean:270`, resolves with full native type `ℕ → ℕ → ℝ → ℕ → ℝ`. All17 current production/pin hashes freshly match the shared successful2467-job baseline. Native original inspection is clean, partial=false, with complete body and only `propext`, `Classical.choice`, `Quot.sound`. See [baseline](../evidence/Roth.lem6M/baseline-build.txt), [fresh hashes](../evidence/Roth.lem6M/source-hashes.json), [native receipt](../evidence/Roth.lem6M/lem6m182-original-receipt.json) and [exact source](../evidence/Roth.lem6M/lem6m182-original-executed.lean.txt).

## Phase 1 — mathematical meaning

For natural numbers p,r₁,l and a real coefficient bound B, define the auxiliary scalar
`M=(r₁+1)^(p*l) * l! * B^l * 2^(p*l*r₁)`.
It bounds the coefficients of a determinant of normalized derivatives when p is the number of variables and r₁ bounds every partial degree. The powers account for products of coefficient bounds, degree counts and derivative growth; l! bounds the number of determinant summands. The definition itself imposes none of the positivity or ordering assumptions used to prove that application.

Elaborated body:
```lean
fun p r₁ B l ↦ (↑r₁ + 1) ^ (p * l) * ↑l.factorial * B ^ l * 2 ^ (p * l * r₁)
```
There are no project dependencies. The complete declaring module was read, including all its actual callers; see [module](../evidence/Roth.lem6M/source-Theta.lean.txt).

## Phase 2 — size and definition check

SMALL: auxiliary numeric notation, not a new structure or main theorem. One substantive body line.

| Exemption | Applies | Evidence |
|---|---|---|
| Avoid defeq abuse | No | Callers deliberately unfold it; native `rfl` works without reducibility attributes. |
| Avoid diamonds | No | Real-valued function, no instance registration. |
| Semantic API stability | Yes locally | `index_det_le`, `index_le_lem6`, `Θ_option_le`, `lem6M_lt`, `theta_phi_lt_aux`, `one_le_lem6M` use its stable spelling. |

ONE-LINER WITH-EXEMPTION. Local API evidence does not itself establish an upstream audience.

## Phase 3 — exhaustive literature

Every named channel was actually attempted. Exact requests, returned-response SHA256/bytes/status and returned locators are in [web0](../evidence/Roth.lem6M/web-0.json), [web1](../evidence/Roth.lem6M/web-1.json), [primary openings](../evidence/Roth.lem6M/web-2.json), [date-bounded recent search](../evidence/Roth.lem6M/web-3.json). Full search bodies were not persisted.

| Channel | Actual query or locator | Finding |
|---|---|---|
| General web, specific | `Roth theorem "(r_1+1)" "l!" polynomial M` | Roth1955 Lemma6/eq16 found; mathematical extraction garbles exponents. |
| General web, general | `Roth theorem auxiliary polynomial Wronskian determinant coefficient height bound` | Princeton lecture Chapter15 and Hindry–Silverman IX.8 describe coefficient/height control through generalized Wronskians. |
| General web, alias | `Dyson lemma Roth index polynomial coefficient bound factorial` | Related small-index method, also unrelated Dyson constant-term hits. |
| ChatGPT math | n/a | `ask_chatgpt_math` unavailable. |
| Local source | clean.tex §5 Lemma6 eq16, lines704–744 | Exact formula and its derivation from product degree bounds. |
| nLab | `site:ncatlab.org/nlab Roth theorem polynomial height` | Broad polynomial/index material; no exact envelope found. |
| nCatLab | `site:ncatlab.org/ncatlab Roth polynomial determinant height` | Returned nLab material outside requested namespace; no exact in-namespace hit. |
| Stacks | `site:stacks.math.columbia.edu polynomial height determinant bound`; supplementary quoted variant | Mostly Krull height/determinants, different invariant. |
| MathOverflow | `site:mathoverflow.net Roth theorem auxiliary polynomial index height` | Question431381 discusses Dyson replacing Roth’s small-index lemma; not this formula. |
| Recent arXiv | Initial2022–2026 query; refined `site:arxiv.org "Roth" "Diophantine" polynomial index after:2021-10-27 before:2026-10-28` | Hindes2209.09182 treats characteristic-p differences; other hits are applications or additive Roth. No exact formula hit. |

The exact standard in this project's reference is a convenient coefficient majorant. Its surrounding lemma assumes p≥2 and positive, decreasing degrees, but the expression is meaningful without those assumptions. Generalized determinant and polynomial height estimates are broader mathematical constructions; they are not automatically an existing definition of this specific constant. The original primary [Roth1955 paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf), Lemma6 eq16, was opened; unreliable extracted exponents are not asserted to agree literally with clean.tex. [Local excerpt](../evidence/Roth.lem6M/clean-lem6-excerpt.tex.txt) supplies exact formula evidence. [Princeton lecture](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), Chapter15, supports the broader method, not uniqueness of the numerical envelope.

## Phase 4a — parameters

| Parameter | Current | Standard role | Weakening assessment |
|---|---|---|---|
| p | ℕ, unrestricted | number of variables, positive in application | No hypothesis to drop; changing to arbitrary integer loses exponent meaning. |
| r₁ | ℕ, unrestricted | degree upper bound | No positivity condition present; degree representation appropriate. |
| B | ℝ, unrestricted | coefficient height bound, positive in application | Semiring expression compiles, but loses ordered analytic height interpretation. |
| l | ℕ, unrestricted | determinant size and factorial index | No positivity condition present; natural index essential. |
| ambient section classes | none in elaborated type | τ is absent | No inherited Fintype/DecidableEq constraints. |

## Phase 4b — generality result

MAXIMALLY GENERAL within the current real-bound interface: no redundant hypotheses. The [isolated probe](../evidence/Roth.lem6M/lem6m182-isolated-executed.lean.txt) defines the same arithmetic expression over any `Semiring A`, specializes to ℝ by `rfl`, and checks natural-cast normalization at B=1. This proves representation reachability, not a literature-driven recommendation to add a semiring-valued `lem6M`. There is no unverified claimed weakening.

## Phase 4c — nine modern idiom checks

| # | Question | Answer and diagnostic |
|---|---|---|
| 1 | Typeclasses replace hypotheses? | No hypotheses; inherited classes are already absent. |
| 2 | Filters replace sequences/metric notions? | No topology or sequence. |
| 3 | Universal property? | No object characterized by a universal property; chosen scalar majorant. |
| 4 | Bundled substructure? | No closure predicates or substructures. |
| 5 | Field-specific algebra? | Yes expression can be interpreted in a semiring, mechanically checked; no demonstrated downstream gain for height/index estimates. |
| 6 | Higher category? | No categorical content. |
| 7 | Concrete indices? | Natural exponents and factorial express combinatorial counts; arbitrary additive indices change content. |
| 8 | Concrete-via-abstract? | Body contains no theorem proof and no occurrences of `lem6M`; inspected directly: only ring arithmetic and factorial. Abstract semiring expression is possible, but construction-only widening is not new upstream mathematics. |
| 9 | False-generalization guard | A semiring expression specializes correctly, but an ordered real height bound is additional structure. Replacing the height/index theorem by bare semiring syntax would erase its purpose. |

No justified modern upstream restatement is proposed. Prefer the real-bound interface for existing consumers.

## Phase 4.5 — six infrastructure risks

| Risk | Assessment | Evidence |
|---|---|---|
| Typeclass diamond | NONE | No instance declaration or new carrier; arithmetic uses existing ℝ instances. `#synth lem6M` would be ill-typed since it is not a class. |
| Reducibility leak | LOW | Ordinary semireducible def; exact expansion equality passes `rfl`; no reducible attribute. |
| Noncanonical unfolding | LOW | Formula has many equivalent association/exponent normal forms; callers intentionally unfold at280,473,662. No simp tag registered. |
| Instance priority | NONE | No priority or instance registration. |
| Universes | NONE | Original takes only ℕ/ℝ values; no universe parameter or carrier. Type0/Type1 instantiations do not apply. |
| Coercion ambiguity | NONE | Returns ℝ, registers no CoeFun/CoeSort. Casts are ordinary ℕ→ℝ. |

Overall LOW. No fabricated synthesis/coercion tests: these are source-level negative structural checks, with the meaningful reducibility check executed natively.

## Phase 4.6 — proof strategy

| # | Strategy question | Assessment |
|---|---|---|
| 1 | ε-δ vs filters | n/a: definition has no topology proof. |
| 2 | Elements vs subobjects | n/a: arithmetic scalar expression. |
| 3 | Sequences vs nets | n/a: no limit proof. |
| 4 | Construction vs universal property | No relevant universal property. |
| 5 | Helpers mathlib should have | Definition needs no helpers beyond arithmetic. General determinant coefficient infrastructure concerns subsequent independently assessed declarations. |

MATHLIB-IDIOMATIC as local arithmetic notation; no proof refactor or missing helper required for this definition.

## Phase 5 — five actual mathlib search methods

[Complete formal receipts](../evidence/Roth.lem6M/formal-search.json) preserve12 actual requests: Finder, Loogle, LeanSearch, local for each current/standard/abstract form. [Current rg](../evidence/Roth.lem6M/rg-current.json), [standard rg](../evidence/Roth.lem6M/rg-standard.json), [abstract rg](../evidence/Roth.lem6M/rg-abstract.json) complete the15 method/form cells.

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | Exact formula query returns unrelated additive Roth | Determinant coefficient query returns Chevalley bounds | Semiring factorial query returns Pochhammer facts |
| Loogle | `"lem6M"`: empty | `Nat.factorial, _ * _ ^ _`: factorial/power inequalities | `"pow_mul"`: generic power-related names |
| LeanSearch | Exact formula returns additive Roth/regularity bounds | `Matrix.det_le`, root coefficient bounds | `Semiring.npow`, finite product identities |
| rg | No `lem6M`/`lem6Φ` in pinned mathlib | Factorial and determinant inequality candidates | Generic arithmetic infrastructure |
| local | Project lem6M and lem6M_lt | Nat.factorial and related names | one_le_mul_of_one_le_of_one_le |

Local index reports unavailable; source matches remain useful positive evidence, not absence evidence. External snapshot may differ from pin. Native isolated `#check` confirms exact pinned signatures of `Nat.factorial`, `pow_mul`, `mul_right_comm`, `Nat.cast_pow`, `one_le_pow₀`, `one_le_mul_of_one_le_of_one_le`, `Nat.factorial_pos`. `Matrix.det_le` bounds an actual determinant using entry absolute-value hypotheses; it does not construct this scalar formula and is not an exact replacement. This assessment does not assert global nonexistence from unsuccessful search.

## Phase 5.5 — statement shape

Normal form: OK for local notation. Product association follows source eq16; no equivalence theorem misoriented. Syntactic alternatives tried: direct inline formula and semiring expression; the named real-valued function is easiest for repeated local statements. Its explicit argument order mirrors source dependence; changing it yields no demonstrated application improvement. All four arguments occur essentially: p in exponents, r₁ in base and exponent, B in its power, l in factorial and exponents. There are no hypotheses/typeclasses to remove. SHIP-AS-STATED locally, no upstream ship recommendation.

## Phase 6.0 — complete caller and inline audit

Fresh [rg](../evidence/Roth.lem6M/callers.json) and [git grep](../evidence/Roth.lem6M/git-callers.json) agree exactly, avoiding ignore-rule omissions. Excluding the declaration and module-doc mention gives19 source lines across six declarations, all in Theta. No external-to-file explicit caller. [Structured callers](../evidence/Roth.lem6M/callers-structured.json) retain every line/excerpt.

| Caller and lines | Use and hypothetical inline refactor |
|---|---|
| one_le_lem6M279–280 | Replace conclusion's scalar with formula and delete unfolding; actual complete arithmetic proof tested. |
| index_det_le467,472–473,478,483 | Replace M at conclusion and coefficient bounds; remove lem6M from normalization list. Keep substantive determinant argument. |
| index_le_lem6562–563,574 | Use a local let M for formula and reuse it within Φ. |
| Θ_option_le597–598,602–603 | Local let or explicit scalar inside finite supremum; no change to bound. |
| lem6M_lt651,660,662 | Expand formula in statement/calc and remove unfolding; substantive exponent estimates remain. |
| theta_phi_lt_aux853,865 | Replace the two let-bound expressions; existing positive/larger bound lemmas still relevant locally. |

No independent full-form inline rederivation found. Natural prefactor inequality `factorial_coefficient_le_two_pow_aux` is a related estimate, not a second definition. The canonical kernel audit independently reports seven direct value consumers and six direct type consumers: the six above, plus `theta_lt_succ_aux` as a value consumer. The latter enters through kernel elaboration of downstream rewrite/application proofs; no explicit source token. These counts are not the entire transitive or simp closure.

## Phase 6 — actual composition experiments

1. Exact `Roth.lem6M` expansion compiles by `rfl`. This is definitional inlining, not a ≤3-existing-mathlib-call construction.
2. Isolated semiring formula and its real specialization compile, including natural cast normalization. `formula` is a NEW scratch definition, not an existing mathlib replacement.
3. Actual `one_le_lem6M` caller is proved on the inlined formula using only pinned arithmetic API; then its original statement is obtained through definitional equality. [Project execution](../evidence/Roth.lem6M/lem6m182-project-executed.lean.txt) and [clean receipt](../evidence/Roth.lem6M/lem6m182-project-receipt.json) establish this exact caller experiment.

Strict accounting: the formula has three scalar multiplications, three powers, factorial, casts/addition, and natural exponent arithmetic. Counting zero *theorem* calls would conceal these construction calls. Its lower-bound theorem likewise uses more than three calls. NOT-COMPOSABLE under the ≤3-existing-call gate; a closing normalization `simp` does not change this to automatic NO. No `exact?` absence claim is needed: no missing theorem is being introduced and the verdict records scope ambiguity rather than proving absence.

## Phase 7 — actionable verdict

BORDERLINE-needs-human. The one-line semantic-name exemption is real, but local convenience alone does not settle whether mathlib should name this particular nonminimal envelope. No cost-based downgrade, exact-replacement claim, or fabricated short composition is used. Retain at `Roth/Theta.lean` for current development. Future upstream design questions:

1. If Roth's auxiliary-polynomial infrastructure moves upstream, should this numeric envelope receive a public name rather than remain a local let?
2. Should that API expose individual degree bounds and derive this uniform-degree envelope, rather than expose both as independent primary constructions?
3. Should the named real envelope stay next to its index estimate, rather than be generalized to semiring-valued syntax with no demonstrated additional consumer?

These are concrete future API choices; the assessment is complete and does not await user input. No PR title/home/grouping is proposed for a non-YES verdict. In particular, any substantive determinant/index declaration receives its own later assessment; this report does not prejudge it.

## Phase 8 — verification and handoff

All phases PASS, unresolved[]. Three clean native records (original/project/isolated), complete ordered canonical293 audit, fresh17 source/pin hashes,15 search cells, all literature channels, caller inventory, source archives and portable manifest validation are preserved. [Verification](../evidence/Roth.lem6M/verification.json), [assessment](../evidence/Roth.lem6M/assessment.json), [portable validator](../evidence/Roth.lem6M/validate.py), [manifest](../evidence/Roth.lem6M/copy-manifest.json). Root acceptance pending; root alone integrates.
