# Sources

The original Algerian Ministry of National Education syllabus documents and
their plain-text extractions used to derive every artefact in
`../curriculum/`. **Do not edit these files** — they are the canonical
source of truth.

## Files

| File | Type | Purpose |
|------|------|---------|
| `official_syllabus_annual_distribution.pdf` | PDF (bilingual Arabic / English) | Year-by-year, week-by-week pacing for every grade and stream |
| `official_syllabus_annual_distribution.txt` | UTF-8 text | Pdfminer.six extraction of the above |
| `teaching_map_all_in_one.pdf` | PDF | Per-unit teaching maps (tasks, phases, productive language, aims, projects, glossaries) |
| `teaching_map_all_in_one.txt` | UTF-8 text | Pdfminer.six extraction of the above |
| `first_year_syllabus_distribution_presentation.pps` | PowerPoint 97-2003 | 1AS slide deck (image-based; minimal extractable text) |
| `second_year_syllabus_distribution_presentation.pps` | PowerPoint 97-2003 | 2AS slide deck (image-based) |
| `third_year_syllabus_distribution_presentation.pps` | PowerPoint 97-2003 | 3AS slide deck (image-based) |
| `*_distribution_presentation.txt` | UTF-8 text | Olefile extraction (limited — slides are mostly rasterised images) |

## Extraction scripts

| Script | What it does |
|--------|---------------|
| `extract_pdf.py` | Uses `pdfminer.six` to extract text from the two PDFs |
| `extract_pps.py` | Walks each .pps OLE2 PowerPoint Document stream and pulls TextChars / TextBytes / CString atoms |
| `inspect_pps.py` | Lists all OLE streams and their sizes (used during diagnosis) |
| `strings_pps.py` | Brute-force "strings"-style scan for printable runs (used during diagnosis; output not committed) |

## Provenance

All five files are public, hosted at:
https://salemzemali.weebly.com (teacher-resource portal).

See `../docs/02-source-attribution.md` for full citation and the fidelity
policy.
