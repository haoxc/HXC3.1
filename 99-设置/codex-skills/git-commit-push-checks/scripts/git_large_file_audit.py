#!/usr/bin/env python3
"""Audit Git file sets for files larger than a configured threshold."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(["git", *args], check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def split_z(data: bytes) -> list[str]:
    return [item.decode("utf-8", "surrogateescape") for item in data.split(b"\0") if item]


def repo_root() -> Path:
    result = run_git(["rev-parse", "--show-toplevel"])
    return Path(result.stdout.decode().strip())


def upstream_ref() -> str | None:
    result = run_git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], check=False)
    if result.returncode != 0:
        return None
    return result.stdout.decode().strip()


def staged_files() -> list[str]:
    result = run_git(["diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR"])
    return split_z(result.stdout)


def ahead_files() -> list[str]:
    upstream = upstream_ref()
    if upstream:
        result = run_git(["diff", "--name-only", "-z", "--diff-filter=ACMR", f"{upstream}...HEAD"])
        return split_z(result.stdout)

    # No upstream means every tracked file in HEAD would be pushed on first publish.
    result = run_git(["ls-files", "-z"])
    return split_z(result.stdout)


def file_size(root: Path, rel: str) -> int | None:
    path = root / rel
    if not path.exists() or not path.is_file():
        return None
    return path.stat().st_size


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f}{unit}" if unit != "B" else f"{int(value)}B"
        value /= 1024
    return f"{value:.1f}GB"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit staged or push-ahead files above a size threshold.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="Audit staged files.")
    mode.add_argument("--ahead", action="store_true", help="Audit files that would be pushed ahead of upstream.")
    parser.add_argument("--threshold-mb", type=float, default=15.0)
    parser.add_argument("--confirm-large", action="store_true", help="Return success even when large files are present.")
    args = parser.parse_args()

    root = repo_root()
    threshold = int(args.threshold_mb * 1024 * 1024)
    files = staged_files() if args.staged else ahead_files()

    large: list[tuple[int, str]] = []
    for rel in files:
        size = file_size(root, rel)
        if size is not None and size > threshold:
            large.append((size, rel))

    label = "staged" if args.staged else "push-ahead"
    if not large:
        print(f"OK: no {label} files larger than {args.threshold_mb:g}MB.")
        return 0

    print(f"REVIEW REQUIRED: {len(large)} {label} file(s) larger than {args.threshold_mb:g}MB:")
    for size, rel in sorted(large, reverse=True):
        print(f"- {human_size(size)}\t{rel}")

    if args.confirm_large:
        print("Large-file review was explicitly confirmed by flag.")
        return 0

    print("Stop here and ask the user to confirm before commit/push.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
