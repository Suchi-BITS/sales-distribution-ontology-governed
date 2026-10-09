from pathlib import Path
import sys

from pyshacl import validate
from rdflib import Graph


BASE_DIR = Path(__file__).resolve().parent
ONTOLOGY_FILE = BASE_DIR / "ontology" / "sales_distribution_ontology.ttl"
SHAPES_FILE = BASE_DIR / "ontology" / "sales_distribution_shapes.ttl"
DATA_FILE = BASE_DIR / "ontology" / "sales_distribution_data.ttl"


def load_graph(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def main() -> int:
    print("Sales & Distribution semantic validation")
    print("=" * 55)

    ontology_graph = load_graph(ONTOLOGY_FILE)
    shapes_graph = load_graph(SHAPES_FILE)
    data_graph = load_graph(DATA_FILE)

    print(f"Ontology triples : {len(ontology_graph):,}")
    print(f"Shapes triples   : {len(shapes_graph):,}")
    print(f"Data triples     : {len(data_graph):,}")
    print()

    print("Starting SHACL validation...", flush=True)
    conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shapes_graph,
    #ont_graph=ontology_graph,
    inference="none",
    abort_on_first=False,
    allow_infos=True,
    allow_warnings=True,
    meta_shacl=False,
    advanced=False,
    debug=False,
)
    print("Starting SHACL validation...", flush=True)

    print(results_text)

    if conforms:
        print("RESULT: CONFORMS")
        return 0

    print("RESULT: VALIDATION FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
