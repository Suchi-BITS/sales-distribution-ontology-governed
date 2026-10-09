# Sales & Distribution SPARQL competency queries

This folder contains 15 SPARQL query files (`.rq`) and a combined reference file.

## Important
- These queries use the canonical `SalesDistributionOntology...` local names used by the sample data file.
- They assume that the ontology and instance data are loaded into the same Fuseki dataset, or that the endpoint exposes both.
- Run one query at a time in Fuseki. The combined file is a reference collection; it is not intended to be submitted as one query because it contains multiple `SELECT` operations.
- CQ-11 and CQ-12 are diagnostic queries for explicit owner links. SHACL remains the validation mechanism for required cardinality.
- CQ-13 to CQ-15 inspect explicitly declared ontology schema terms. Results can depend on which graphs are included in the dataset.
- The example data contains provisional mappings and source-semantic limitations documented in `data.ttl`; query results do not validate those mappings as correct.
