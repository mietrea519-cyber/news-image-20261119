#!/usr/bin/env python3
"""news-image-20261119 entry program.

Writes the entry image to the output directory. The image itself
(entry.png, a JPEG by its first bytes, as the rules allow) sits beside
this file in the repository; the program simply copies it, byte for
byte, so two runs always produce the same output and no network is
needed.

Output directory: $MAKEFUN_OUTPUT_DIR when set, else /output.
The file is always named entry.png.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
