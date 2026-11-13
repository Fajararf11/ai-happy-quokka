#!/usr/bin/env python3
"""make.fun entry — "Make the AI judge happy".

The entry is a single pre-generated image: a very happy quokka in a party hat,
surrounded by confetti. The image was generated before the build, so this program
does not generate or edit anything — it copies the shipped ``entry.png`` to the
output directory as ``entry.png``.

The copy is verified in two ways so a corrupted or truncated entry fails loudly
instead of being submitted silently:

1. The source ``entry.png`` must have the expected SHA-256.
2. The written output must contain exactly as many bytes as the source.

Standard library only, no network. Deterministic: same bytes in, same bytes out.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"  # image shipped in the repo root
OUTPUT_NAME = "entry.png"

# SHA-256 of the approved entry image. If this changes, the entry changed.
EXPECTED_SHA256 = "89de45a4498d052f7e932243f64af39ca07c2649009bd54606d3e03289a5d4a8"


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"source image is missing: {SOURCE}")

    # 1. Refuse to ship an image that is not the approved one.
    actual = sha256_of(SOURCE)
    if actual != EXPECTED_SHA256:
        raise ValueError(
            f"source image hash mismatch for {SOURCE}: "
            f"expected {EXPECTED_SHA256}, got {actual}"
        )

    # Honour MAKEFUN_OUTPUT_DIR when set, otherwise default to /output.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_path = out_dir / OUTPUT_NAME

    # Create the output directory if it does not exist yet.
    out_dir.mkdir(parents=True, exist_ok=True)

    # Copy raw bytes only (no metadata, no re-encoding), so the result is
    # byte-identical to the source and reproducible across runs.
    shutil.copyfile(SOURCE, out_path)

    # 2. Refuse to report success if the copy is truncated or short.
    source_size = SOURCE.stat().st_size
    copied_size = out_path.stat().st_size
    if copied_size != source_size:
        raise IOError(
            f"incomplete copy: wrote {copied_size} bytes to {out_path}, "
            f"expected {source_size} bytes from {SOURCE}"
        )

    print(
        f"wrote {out_path} ({copied_size} bytes, sha256 {actual})",
        file=sys.stdout,
    )


if __name__ == "__main__":
    main()
