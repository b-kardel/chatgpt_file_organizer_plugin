#!/usr/bin/env python3
"""Read-only local file inventory; avoids symlinked directories."""
import argparse
import json
from collections import Counter
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("folder", type=Path)
parser.add_argument("--name", default="", help="case-insensitive substring")
parser.add_argument("--max-results", type=int, default=200)
args = parser.parse_args()

root = args.folder.expanduser().resolve(strict=True)
if not root.is_dir():
    raise SystemExit("folder must be a directory")
needle = args.name.casefold()
results, extensions = [], Counter()
for path in root.rglob("*"):
    if path.is_symlink() or not path.is_file():
        continue
    if needle and needle not in path.name.casefold():
        continue
    stat = path.stat()
    extensions[path.suffix.casefold() or "[no extension]"] += 1
    if len(results) < args.max_results:
        results.append({"path": str(path), "bytes": stat.st_size, "modified": stat.st_mtime})

print(json.dumps({"root": str(root), "matches": sum(extensions.values()), "shown": len(results), "by_extension": dict(extensions.most_common()), "files": results}, ensure_ascii=False, indent=2))
