
#!/usr/bin/env python3
"""
notebook_path_scan.py
---------------------
List all occurrences of hardcoded paths in code cells:
- "Reference/..." (inputs)
- "Graphs/..."    (outputs)

Usage:
  python notebook_path_scan.py --dir notebooks
"""
import argparse
from pathlib import Path
import nbformat

def scan_notebook(path: Path):
    nb = nbformat.read(path, as_version=4)
    findings = []
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        lines = cell.source.splitlines()
        for ln, line in enumerate(lines, start=1):
            if "Reference/" in line or "Graphs/" in line:
                findings.append((idx, ln, line.strip()))
    return findings

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="notebooks")
    args = ap.parse_args()

    target = Path(args.dir)
    assert target.exists(), f"Directory not found: {target}"
    ipynbs = sorted(target.glob("*.ipynb"))
    if not ipynbs:
        print(f"No notebooks found in {target}")
        return

    total = 0
    for nbp in ipynbs:
        f = scan_notebook(nbp)
        if not f:
            continue
        print(f"\n=== {nbp.name} ===")
        for cell_idx, line_no, text in f:
            total += 1
            print(f"  Cell {cell_idx:02d}, Line {line_no:02d}: {text}")
    if total == 0:
        print("No hardcoded 'Reference/' or 'Graphs/' found in code cells.")
    else:
        print(f"\nTotal matches: {total}")

if __name__ == "__main__":
    main()
