#!/usr/bin/env python3
"""Check if large files are tracked by Git LFS."""

import subprocess
import sys
from pathlib import Path

LARGE_FILE_THRESHOLD_KB = 5120


def check_lfs():
    try:
        subprocess.check_output(["git", "lfs", "track"], text=True)
    except subprocess.CalledProcessError:
        print("Git LFS not installed or not initialized")
        sys.exit(1)

    large_files = []
    for path in Path(".").rglob("*"):
        if path.is_file() and not path.match(".git/*"):
            size_kb = path.stat().st_size / 1024
            if size_kb > LARGE_FILE_THRESHOLD_KB:
                large_files.append((path, size_kb))

    if large_files:
        print("Large files detected without LFS tracking:")
        for path, size in large_files:
            print(f"  {path} ({size:.1f} KB)")
        print("\nAdd them to LFS with: git lfs track 'path/to/file'")
        sys.exit(1)


if __name__ == "__main__":
    check_lfs()
