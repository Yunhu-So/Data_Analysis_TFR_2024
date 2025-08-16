
#!/usr/bin/env python3
"""
notebook_path_refactor.py  (v3)
----------------------------------
Usage:
  python notebook_path_refactor.py --dir notebooks --dry-run
  python notebook_path_refactor.py --dir notebooks --apply
Options:
  --dir         Target directory containing .ipynb files (default: notebooks)
  --dry-run     Show planned changes without writing files
  --apply       Write changes
  --no-backup   Do not create .bak backups (default: backups enabled)

What it does:
  1) Inserts a bootstrap "paths" cell at the top of each notebook (if missing)
  2) Rewrites hardcoded paths in code cells (with tolerant whitespace):
     - pd.read_excel("Reference/xyz.xlsx", ...)
     - pd.read_csv("Reference/xyz.csv", ...)
     - pd.read_pickle("Reference/xyz.pkl", ...)
     - open("Reference/xyz.ext", ...)
     - plt.savefig("Graphs/fig.png", dpi=200, ...)
     - Image("Graphs/fig.png", width=800)
"""
import argparse, re, shutil
from pathlib import Path
import nbformat

BOOTSTRAP_CODE = """from pathlib import Path
import pandas as pd

def find_root(start: Path = Path.cwd()) -> Path:
    # Look for a directory that has 'data' and 'reports', walk up from current working dir
    for p in [start, *start.parents]:
        if (p / "data").exists() and (p / "reports").exists():
            return p
    return start

ROOT = find_root()
DATA_DIR = ROOT / "data" / "raw"
FIG_DIR  = ROOT / "reports" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
"""

# tolerant patterns (allow spaces around dots and before "(" )
READ_EXCEL_RE = re.compile(r'pd\s*\.\s*read_excel\s*\(\s*["\']Reference/([^"\']+)["\'](?P<rest>\s*,[^)]*)?\)')
READ_CSV_RE   = re.compile(r'pd\s*\.\s*read_csv\s*\(\s*["\']Reference/([^"\']+)["\'](?P<rest>\s*,[^)]*)?\)')
READ_PKL_RE   = re.compile(r'pd\s*\.\s*read_pickle\s*\(\s*["\']Reference/([^"\']+)["\'](?P<rest>\s*,[^)]*)?\)')
OPEN_RE       = re.compile(r'(?:\w+\s*\.\s*)?open\s*\(\s*["\']Reference/([^"\']+)["\'](?P<rest>\s*,[^)]*)?\)')
SAVEFIG_RE    = re.compile(r'plt\s*\.\s*savefig\s*\(\s*["\']Graphs/([^"\']+)["\'](?P<rest>\s*,[^)]*)?\)')
IMAGE_RE      = re.compile(r'(?:\w+\s*\.\s*)?Image\s*\(\s*["\']Graphs/([^"\']+)["\'](?P<rest>\s*,[^)]*)?\)')

REPLACERS = [
    (READ_EXCEL_RE, r'pd.read_excel(DATA_DIR / "\1"\g<rest>)'),
    (READ_CSV_RE,   r'pd.read_csv(DATA_DIR / "\1"\g<rest>)'),
    (READ_PKL_RE,   r'pd.read_pickle(DATA_DIR / "\1"\g<rest>)'),
    (OPEN_RE,       r'open(DATA_DIR / "\1"\g<rest>)'),
    (SAVEFIG_RE,    r'plt.savefig(FIG_DIR / "\1"\g<rest>)'),
    (IMAGE_RE,      r'Image(str(FIG_DIR / "\1")\g<rest>)'),
]

def insert_bootstrap_if_missing(nb):
    if not nb.cells:
        nb.cells = []
    first_src = nb.cells[0].source if nb.cells and nb.cells[0].cell_type == "code" else ""
    already_has = ("DATA_DIR" in first_src and "FIG_DIR" in first_src) or any(
        ("DATA_DIR" in c.source and "FIG_DIR" in c.source) for c in nb.cells if c.cell_type=="code"
    )
    if not already_has:
        nb.cells.insert(0, nbformat.v4.new_code_cell(BOOTSTRAP_CODE))
        return True
    return False

def rewrite_paths_in_code(source: str) -> (str, int):
    changes = 0
    new = source
    for pattern, repl in REPLACERS:
        new2, n = pattern.subn(repl, new)
        if n:
            changes += n
        new = new2
    return new, changes

def process_notebook(path: Path, apply: bool, make_backup: bool) -> dict:
    nb = nbformat.read(path, as_version=4)
    summary = {"file": str(path), "inserted_bootstrap": False, "cell_changes": 0, "path_rewrites": 0}

    # 1) insert bootstrap if missing
    if insert_bootstrap_if_missing(nb):
        summary["inserted_bootstrap"] = True
        summary["cell_changes"] += 1

    # 2) rewrite paths in code cells
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        new_src, n = rewrite_paths_in_code(cell.source)
        if n:
            summary["path_rewrites"] += n
            cell.source = new_src

    if apply and (summary["inserted_bootstrap"] or summary["path_rewrites"]):
        if make_backup:
            backup = path.with_suffix(path.suffix + ".bak")
            shutil.copy2(path, backup)
        nbformat.write(nb, path)
    return summary

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="notebooks")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--no-backup", action="store_true")
    args = ap.parse_args()

    target = Path(args.dir)
    assert target.exists(), f"Directory not found: {target}"
    ipynbs = sorted(target.glob("*.ipynb"))
    if not ipynbs:
        print(f"No notebooks found in {target}")
        return

    totals = {"files": 0, "bootstraps": 0, "rewrites": 0}
    for nb_path in ipynbs:
        s = process_notebook(nb_path, apply=args.apply, make_backup=not args.no_backup)
        totals["files"] += 1
        totals["bootstraps"] += int(s["inserted_bootstrap"])
        totals["rewrites"] += s["path_rewrites"]
        action = "WOULD CHANGE" if args.dry_run and (s["inserted_bootstrap"] or s["path_rewrites"]) else "OK"
        if args.apply and (s["inserted_bootstrap"] or s["path_rewrites"]):
            action = "UPDATED"
        print(f"[{action}] {Path(nb_path).name}  (+bootstrap={s['inserted_bootstrap']}, path_rewrites={s['path_rewrites']})")

    print("-" * 60)
    mode = "DRY-RUN" if args.dry_run else ("APPLIED" if args.apply else "NO-OP")
    print(f"Mode: {mode}")
    print(f"Processed notebooks: {totals['files']}")
    print(f"Inserted bootstrap cells: {totals['bootstraps']}")
    print(f"Total path rewrites: {totals['rewrites']}")
    print("Done.")

if __name__ == "__main__":
    main()
