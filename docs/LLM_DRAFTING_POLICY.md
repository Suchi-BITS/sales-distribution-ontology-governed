# LLM-Assisted Ontology Drafting Policy

## Purpose

Use an LLM as a drafting assistant, not as an autonomous semantic authority. Human reviewers remain accountable for domain meaning and approval.

## Allowed assistance

- Suggest candidate labels and definitions based on supplied business requirements.
- Propose mappings from source columns to existing ontology terms.
- Draft SHACL shapes, SPARQL queries, tests, and documentation.
- Summarize Git diffs and identify possible semantic impacts.
- Identify duplicate terms and naming inconsistencies.

## Not allowed without human approval

- Replacing the canonical ontology wholesale.
- Inventing source semantics or treating unknown mappings as facts.
- Automatically approving or merging changes.
- Declaring classes disjoint or properties transitive/functional, or adding exact cardinalities, without a documented business rule.
- Uploading credentials, sensitive data, or restricted business records to an unapproved model.

## Reusable prompt

> You are assisting with a governed Sales & Distribution OWL ontology. Treat the supplied ontology, business rules, source headers, and competency questions as authoritative evidence. Do not invent classes, properties, identifiers, mappings, or business meanings.
>
> Propose the smallest possible patch. For every proposed change, provide: (1) the business requirement; (2) existing terms checked for reuse; (3) proposed Turtle change; (4) domain, range, datatype, and cardinality rationale; (5) expected inferences and possible unintended consequences; (6) SHACL/SPARQL tests; and (7) evidence and uncertainties.
>
> If evidence is insufficient, label the item `NEEDS BUSINESS CONFIRMATION` and do not assert it as fact. Do not modify unrelated ontology content. Return a patch/diff, not a replacement file.

## Human acceptance checklist

- [ ] Business owner confirms the meaning.
- [ ] Existing canonical terms were considered first.
- [ ] No duplicate class/property was introduced without justification.
- [ ] Domain/range and axioms have a written rationale.
- [ ] Source mapping is traceable to a real column/rule.
- [ ] Turtle syntax validation passes.
- [ ] SHACL validation was reviewed.
- [ ] HermiT consistency and important inferences were checked in Protégé.
- [ ] A human reviewer approved the pull request.
