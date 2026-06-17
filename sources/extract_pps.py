"""
Extract text from binary PowerPoint 97-2003 (.pps/.ppt) files by parsing
the 'PowerPoint Document' OLE stream and pulling out the relevant text atoms.

Atom record types we care about (MS-PPT spec):
  TextCharsAtom    rh.recType = 0x0FA0  (text as UTF-16LE)
  TextBytesAtom    rh.recType = 0x0FA8  (text as ANSI / cp1252)
  CStringAtom      rh.recType = 0x0FBA  (UTF-16LE, used for slide titles, notes, etc.)
  TextHeaderAtom   rh.recType = 0x0F9F  (small header, contains txType)

Each record header is 8 bytes:
  recVer (4 bits) | recInstance (12 bits)  -> 2 bytes LE
  recType (16 bits)                        -> 2 bytes LE
  recLen  (32 bits)                        -> 4 bytes LE
"""
import struct
import sys
import olefile

TEXT_ATOM_TYPES = {
    0x0FA0: "TextCharsAtom",   # UTF-16LE
    0x0FA8: "TextBytesAtom",   # cp1252
    0x0FBA: "CStringAtom",     # UTF-16LE
}


def extract_text_from_stream(data: bytes) -> list[tuple[str, str]]:
    """Walk every 8-byte record header in the stream and pull out text atoms."""
    out: list[tuple[str, str]] = []
    i = 0
    n = len(data)
    while i + 8 <= n:
        ver_inst, rec_type, rec_len = struct.unpack_from("<HHI", data, i)
        # Sanity: declared length must fit
        if rec_len > n - (i + 8):
            i += 1
            continue
        if rec_type in TEXT_ATOM_TYPES:
            payload = data[i + 8 : i + 8 + rec_len]
            try:
                if rec_type == 0x0FA8:
                    text = payload.decode("cp1252", errors="replace")
                else:
                    text = payload.decode("utf-16-le", errors="replace")
            except Exception:
                text = payload.decode("latin-1", errors="replace")
            text = text.replace("\r", "\n").replace("\x0b", "\n").replace("\x0d", "\n")
            text = text.strip("\x00 \t\n")
            if text:
                out.append((TEXT_ATOM_TYPES[rec_type], text))
            i += 8 + rec_len
        else:
            # Container records (recVer high bits) have nested records, so don't skip body.
            rec_ver = ver_inst & 0x000F
            if rec_ver == 0xF:
                # container -> step into children
                i += 8
            else:
                i += 8 + rec_len
    return out


def extract_pps(path: str) -> str:
    ole = olefile.OleFileIO(path)
    streams = ole.listdir()
    # The main stream is "PowerPoint Document"
    main = ["PowerPoint Document"]
    if not ole.exists(main):
        # try the first stream that contains 'PowerPoint'
        for s in streams:
            if any("powerpoint" in p.lower() for p in s):
                main = s
                break
    data = ole.openstream(main).read()
    atoms = extract_text_from_stream(data)

    # Also pull text from the "Pictures" / "Current User" / notes streams if helpful?
    # For the syllabus presentations the main stream is enough.

    # Concatenate, preserving order, with separators between atoms
    lines: list[str] = []
    for kind, txt in atoms:
        # Split on internal newlines so we have one logical line per text fragment
        for sub in txt.splitlines():
            sub = sub.strip()
            if sub:
                lines.append(sub)
    return "\n".join(lines)


if __name__ == "__main__":
    files = [
        ("first_year_syllabus_distribution_presentation.pps",
         "first_year_syllabus_distribution_presentation.txt"),
        ("second_year_syllabus_distribution_presentation.pps",
         "second_year_syllabus_distribution_presentation.txt"),
        ("third_year_syllabus_distribution_presentation.pps",
         "third_year_syllabus_distribution_presentation.txt"),
    ]
    for src, dst in files:
        print(f"Extracting {src} -> {dst}", file=sys.stderr)
        text = extract_pps(src)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  wrote {len(text)} chars, {text.count(chr(10))+1} lines", file=sys.stderr)
