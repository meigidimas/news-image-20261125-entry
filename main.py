"""Entry program for news-image-20261125.

Writes the pre-rendered front page (entry.png, 1024 x 1024) to the
make.fun output directory. The image is "THE WORLD TODAY — Wednesday,
25 November 2026": eight stories from that day, each verified against
reporting dated 25 November 2026. Deterministic: the same bytes
every run.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1_048_576  # 1 MiB, the competition limit
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_png(path: Path) -> bool:
    with open(path, "rb") as fh:
        return fh.read(len(PNG_SIGNATURE)) == PNG_SIGNATURE


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    if not SOURCE.exists():
        print(f"source image not found: {SOURCE}", file=sys.stderr)
        return 1
    if not _is_png(SOURCE):
        print(f"{SOURCE} is not a PNG image", file=sys.stderr)
        return 1
    dest = Path(out_dir) / OUTPUT_NAME
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    size = dest.stat().st_size
    if size > MAX_BYTES:
        print(f"output too large: {size} bytes (limit {MAX_BYTES})", file=sys.stderr)
        return 1
    if _sha256(dest) != _sha256(SOURCE):
        print("output bytes differ from source image", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({size} bytes, sha256 {_sha256(dest)[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
