# Running the competency queries in Apache Jena Fuseki

## 1. Load the RDF data
1. Start Apache Jena Fuseki.
2. Create a dataset, for example `sd`.
3. Load `ontology/sales_distribution_ontology.ttl` and `data/sales_distribution_data.ttl` into the dataset. Use the dataset's upload/data-management interface or configure the dataset with both files.
4. If the ontology and data are loaded into separate named graphs, ensure your queries target the relevant graphs or configure the dataset to expose the union/default graph as intended.

## 2. Run a query
1. Open the dataset's SPARQL Query interface.
2. Open a file under `queries/`, for example `cq03_inventory_by_distributor.rq`.
3. Paste its contents into the query editor.
4. Select the SPARQL query operation and execute it.
5. Inspect the result table and record Pass/Fail against the competency question.

## 3. Run one query at a time
`competency_questions.rq` is a combined reference. It contains multiple SELECT operations, so copy and run each query block separately in Fuseki.

## 4. Interpret empty results carefully
An empty result may mean that the data is absent, the query uses a mismatched IRI, the relevant graph is not included, or inference is not enabled. It does not automatically mean that the ontology is wrong.

## 5. Important project-specific note
The sample data uses IRIs like `sd:SalesDistributionOntologyDistributor`. Keep those exact IRIs aligned with the ontology and the SHACL shapes. Similar-looking short IRIs such as `sd:Distributor` are different identifiers unless explicitly linked.
