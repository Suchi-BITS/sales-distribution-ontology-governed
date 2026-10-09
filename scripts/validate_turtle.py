from pathlib import Path
import sys
from rdflib import Graph

ROOT = Path(__file__).resolve().parents[1]
TTL_FILES = sorted((ROOT / "ontology").glob("*.ttl"))

def main() -> int:
    if not TTL_FILES:
        print("ERROR: No .ttl files found under ontology/")
        return 1
    failed = False
    for path in TTL_FILES:
        graph = Graph()
        try:
            graph.parse(path, format="turtle")
            print(f"OK   {path.relative_to(ROOT)} — {len(graph):,} triples")
        except Exception as exc:
            failed = True
            print(f"FAIL {path.relative_to(ROOT)} — {exc}")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
