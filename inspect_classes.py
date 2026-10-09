from rdflib import Graph, URIRef, RDFS

ONTOLOGY_FILE = "ontology/sales_distribution_ontology.ttl"

g = Graph()
g.parse(ONTOLOGY_FILE, format="turtle")

SD = "https://abhigya.ai/ontology/sales-distribution#"

distributor = URIRef(SD + "SalesDistributionOntologyDistributor")
business_org = URIRef(SD + "SalesDistributionOntologyBusinessOrganization")

def show_ancestors(cls, visited=None, level=0):
    if visited is None:
        visited = set()

    if cls in visited:
        return

    visited.add(cls)
    print("  " * level + str(cls))

    for parent in g.objects(cls, RDFS.subClassOf):
        if isinstance(parent, URIRef):
            show_ancestors(parent, visited, level + 1)

print("Distributor superclass hierarchy:")
show_ancestors(distributor)

print("\nBusinessOrganization direct superclasses:")
for parent in g.objects(business_org, RDFS.subClassOf):
    print(" ", parent)