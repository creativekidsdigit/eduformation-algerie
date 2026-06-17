"""List every stream inside each .pps OLE container with size."""
import olefile, sys, os
for f in [
    "first_year_syllabus_distribution_presentation.pps",
    "second_year_syllabus_distribution_presentation.pps",
    "third_year_syllabus_distribution_presentation.pps",
]:
    print("=" * 70)
    print(f)
    print("=" * 70)
    ole = olefile.OleFileIO(f)
    for s in ole.listdir():
        try:
            sz = ole.get_size(s)
        except Exception:
            sz = "?"
        print(f"  {sz:>10}  /{'/'.join(s)}")
    ole.close()
