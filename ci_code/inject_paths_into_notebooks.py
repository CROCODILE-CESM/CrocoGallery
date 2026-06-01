import json
from pathlib import Path
import os
import nbformat
import argparse


def process_notebook(notebook_path, paths, inject_setup, reverse):
    print(f"Processing: {notebook_path}")
    nb = nbformat.read(notebook_path, as_version=4)
    changed = False
    for cell in nb.cells:
        if cell.cell_type in ("code", "Python"):
            original_source = cell.source
            for key, real_path in paths[inject_setup].items():
                full_str = "<" + key + ">"
                if not reverse:
                    if full_str in cell.source:
                        cell.source = cell.source.replace(full_str, real_path)
                        changed = True
                else:
                    if real_path in cell.source:
                        cell.source = cell.source.replace(real_path, full_str)
                        changed = True
            if original_source != cell.source:
                print(f"  Modified cell in {notebook_path.name}")
    if changed:
        nbformat.write(nb, notebook_path)
        print(f"  Saved updated notebook: {notebook_path}")


def main(reverse=False, inject_setup="cirrus"):

    with open(Path(__file__).parent / "path_to_datasets.json", "r") as f:
        paths = json.load(f)
    notebooks_path = Path(__file__).parent.parent / "gallery" / "notebooks"

    # Process ci_case_setup.ipynb in code/
    ci_notebook = Path(__file__).parent / "ci_case_setup.ipynb"
    if ci_notebook.exists():
        process_notebook(ci_notebook, paths, inject_setup, reverse)

    for root, _, files in os.walk(notebooks_path):
        for name in files:
            if not name.endswith(".ipynb"):
                continue  # Skip non-notebook files
            process_notebook(Path(root) / name, paths, inject_setup, reverse)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inject or reverse-inject paths in notebooks."
    )
    parser.add_argument(
        "--reverse", action="store_true", help="Reverse the path injection."
    )
    parser.add_argument(
        "--inject_setup",
        default="cirrus",
        help="Which inject setup to use (default: cirrus).",
    )
    args = parser.parse_args()
    main(reverse=args.reverse, inject_setup=args.inject_setup)
