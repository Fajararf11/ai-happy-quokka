#!/usr/bin/env python3
"""make.fun entry: copy the pre-generated image to /output/entry.png.

The image was generated before the build; this program only copies it.
Standard library only, no network. Deterministic: same bytes in, same bytes out.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"  # image shipped in the repo root
OUTPUT_NAME = "entry.png"


def main() -> None:
    # Honour MAKEFUN_OUTPUT_DIR when set, otherwise default to /output.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")

    # Create the output directory if it does not exist yet.
    out_dir.mkdir(parents=True, exist_ok=True)

    # Copy raw bytes only (no metadata, no re-encoding), so the result is
    # byte-identical to the source and reproducible across runs.
    shutil.copyfile(SOURCE, out_dir / OUTPUT_NAME)


if __name__ == "__main__":
    main()
