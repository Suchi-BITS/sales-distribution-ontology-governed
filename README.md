# Sales & Distribution Ontology Engineering

This repository manages the Sales & Distribution (S&D) ontology, validation shapes, sample instance data, and ontology change governance.

## Repository structure

```text
sales-distribution-ontology/
├── .github/
│   ├── pull_request_template.md
│   └── workflows/ontology-validation.yml
├── docs/
│   ├── CHAPTER_2_ONTOLOGY_GOVERNANCE.md
│   ├── LLM_DRAFTING_POLICY.md
│   └── CHANGELOG.md
├── ontology/
│   ├── sales_distribution_ontology.ttl
│   ├── sales_distribution_shapes.ttl
│   └── sales_distribution_data.ttl
├── scripts/validate_turtle.py
├── tests/test_turtle_files.py
├── validator.py
├── requirements.txt
└── README.md
```

## Ontology file versus `data.ttl`

RDF/Turtle does not require schema and instance data to be in separate files. A Turtle file can contain classes, properties, OWL axioms, and individuals together. Your existing Protégé ontology can contain individuals and still be valid.

The separation is a project governance choice:

| File | Responsibility | Typical content |
|---|---|---|
| `sales_distribution_ontology.ttl` | TBox / canonical semantic model | Classes, properties, hierarchy, domains/ranges, OWL restrictions and axioms |
| `sales_distribution_shapes.ttl` | Data-quality contract | SHACL node shapes and property constraints |
| `sales_distribution_data.ttl` | ABox / sample or imported facts | Individuals, literal values, relationships between individuals |

Separating them lets reviewers distinguish schema changes from data changes, refresh data without rewriting the ontology, and validate each artifact independently. It is not necessary to extract every individual immediately; if your current ontology contains individuals, retain it as-is until a planned and tested migration. Avoid maintaining two independently edited copies of the same ontology.

## What is `saved.ttl`?

`saved.ttl` is not a special RDF/OWL/Protégé format; it is just a filename. It does not tell us whether the file contains TBox, ABox, or both. Use `sales_distribution_ontology.ttl` as the descriptive canonical filename and Git history/tags for historical snapshots, rather than an ambiguous `saved.ttl` that can drift out of sync.

## Local setup

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/validate_turtle.py
python validator.py
```

The GitHub workflow parses the Turtle files and runs SHACL validation. A failure is a review signal; do not weaken constraints merely to make CI green. HermiT is not run by this Python workflow; run it in Protégé.

## Recommended workflow

1. Create a focused branch.
2. Edit in Protégé or draft a small patch.
3. Save/export Turtle and inspect the diff.
4. Run Turtle parsing, SHACL, and HermiT consistency checks.
5. Open a pull request describing the business reason and expected inference impact.
6. Obtain domain/ontology review.
7. Merge after required checks pass and tag deliberate releases.

The workbook currently contains only a sample row per business sheet, so `sales_distribution_data.ttl` is a sample ABox, not a production import. Review the validation report and ontology gaps before treating the sample as conformant.
