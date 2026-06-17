"""Brute-force extract printable text runs from each PPS PowerPoint stream.

Looks for both 8-bit (cp1252) and 16-bit (UTF-16LE) printable runs of >=3 chars.
This catches text embedded in shapes, smart-art, and other non-standard atoms.
"""
import olefile, re, sys

ASCII_RUN = re.compile(rb"[\x20-\x7E\xa0-\xff\t\r\n]{3,}")
# UTF-16LE printable: byte0 in printable range, byte1 == 0x00
UTF16_RUN = re.compile(rb"(?:[\x20-\x7E\xa0-\xff]\x00){3,}")

for src, dst in [
    ("first_year_syllabus_distribution_presentation.pps",
     "first_year_syllabus_strings.txt"),
    ("second_year_syllabus_distribution_presentation.pps",
     "second_year_syllabus_strings.txt"),
    ("third_year_syllabus_distribution_presentation.pps",
     "third_year_syllabus_strings.txt"),
]:
    ole = olefile.OleFileIO(src)
    data = ole.openstream(["PowerPoint Document"]).read()
    ole.close()

    out_lines = []
    out_lines.append(f"### UTF-16LE runs ###")
    seen = set()
    for m in UTF16_RUN.finditer(data):
        try:
            s = m.group(0).decode("utf-16-le", errors="replace").strip()
        except Exception:
            continue
        if s and len(s) >= 3 and s not in seen:
            seen.add(s)
            out_lines.append(s)

    out_lines.append("")
    out_lines.append(f"### CP1252/ASCII runs ###")
    seen = set()
    for m in ASCII_RUN.finditer(data):
        s = m.group(0).decode("cp1252", errors="replace").strip()
        if not s or len(s) < 3:
            continue
        # Skip pure binary noise / file refs we already saw
        if s in seen:
            continue
        seen.add(s)
        out_lines.append(s)

    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    print(f"{src} -> {dst}: {len(out_lines)} lines")
