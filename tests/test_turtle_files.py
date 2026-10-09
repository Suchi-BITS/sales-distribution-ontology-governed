from pathlib import Path
from rdflib import Graph

ROOT = Path(__file__).resolve().parents[1]

def test_all_ontology_turtle_files_parse():
    ttl_files = list((ROOT / "ontology").glob("*.ttl"))
    assert ttl_files, "No Turtle files found under ontology/"
    for path in ttl_files:
        graph = Graph()
        graph.parse(path, format="turtle")
        assert len(graph) > 0, f"{path.name} parsed but contained no triples"
