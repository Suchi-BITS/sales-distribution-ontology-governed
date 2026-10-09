# Chapter 2 — Version Control and Governance for Ontologies

## Goal

Treat the ontology as a governed software artifact: changes are traceable, reviewable, testable, and reversible. LLMs may accelerate drafting, but they do not independently approve semantic changes.

## Version-control principles

- Keep the canonical ontology in Git.
- Use meaningful commits and focused branches.
- Review semantic diffs, not only text diffs.
- Record why a class, property, restriction, or mapping changed.
- Validate every pull request.
- Use tags for reviewed releases.
- Keep credentials, private customer records, and production data out of Git.

## Branch and commit examples

Branches: `feat/add-delivery-date-property`, `fix/quotation-shape-cardinality`, `docs/update-business-definitions`.

Commits: `ontology: define goods issue date semantics`, `shacl: validate non-negative inventory quantity`, `docs: record project-to-opportunity decision`.

## Change lifecycle

```text
Business requirement
        |
        v
Issue / competency question
        |
        v
Feature branch
        |
        v
Edit ontology / shapes / data
        |
        v
Turtle syntax validation
        |
        v
SHACL data validation
        |
        v
HermiT consistency check in Protégé
        |
        v
Pull request + human review
        |
        v
Merge + release tag
```

## What CI can and cannot prove

Turtle parsing catches malformed syntax. SHACL checks explicit data-quality constraints. These checks do not prove that the conceptualization is correct. Run HermiT in Protégé to check OWL consistency and inspect inferences. Review whether domain/range, disjointness, transitivity, equivalence, and cardinality axioms express true business rules.

## Semantic review checklist

- Is the business meaning documented?
- Is this a new concept or an existing concept under a different name?
- Does a similar class/property already exist?
- Are domain and range correct?
- Are cardinality, disjointness, transitivity, equivalence, and inverse axioms justified?
- Could the change cause unintended inferred types or inconsistencies?
- Does the data mapping preserve the source meaning?
- Are competency questions and SHACL shapes updated where needed?
- Is there a sample demonstrating the intended behavior?

## Releases

As a project convention, use PATCH for documentation/non-semantic corrections, MINOR for backward-compatible additions, and MAJOR for breaking changes such as removing terms or changing meaning/cardinality in ways that break consumers. Record the rationale in `CHANGELOG.md`.

## Safe LLM-assisted drafting

LLMs may propose definitions, labels, candidate mappings, competency questions, SHACL shapes, SPARQL queries, tests, and change summaries. They must not be treated as the source of truth for business semantics. See `LLM_DRAFTING_POLICY.md` for controls and a reusable prompt.
