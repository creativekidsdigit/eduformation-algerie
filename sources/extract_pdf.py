"""Extract text from the two official Algerian syllabus PDFs using pdfminer.six."""
import sys
from pdfminer.high_level import extract_text

inputs = [
    ("official_syllabus_annual_distribution.pdf", "official_syllabus_annual_distribution.txt"),
    ("teaching_map_all_in_one.pdf", "teaching_map_all_in_one.txt"),
]
for src, dst in inputs:
    print(f"Extracting {src} -> {dst}", file=sys.stderr)
    text = extract_text(src)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  wrote {len(text)} chars, {text.count(chr(10))} lines", file=sys.stderr)
print("done", file=sys.stderr)
