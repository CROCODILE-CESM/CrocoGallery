import json
from pathlib import Path
import os
import nbformat
import argparse


def load_paths(machine, json_path=None):
    """Return the path dict for the given machine key.

    json_path defaults to the bundled known_paths.json in this package.
    """
    if json_path is None:
        from importlib.resources import files

        json_path = files("crocogallery") / "known_paths.json"
    with open(json_path) as f:
        db = json.load(f)
    if machine not in db:
        available = ", ".join(db.keys())
        raise KeyError(f"Unknown machine '{machine}'. Available: {available}")
    return db[machine]


def inject_into_text(text, paths):
    """Replace <KEY> placeholders in a plain string."""
    for key, val in paths.items():
        text = text.replace(f"<{key}>", val)
    return text


def reverse_inject_text(text, paths):
    """Replace real paths with <KEY> placeholders (reverse of inject_into_text)."""
    for key, val in paths.items():
        text = text.replace(val, f"<{key}>")
    return text


def process_notebook(notebook_path, paths, reverse):
    print(f"Processing: {notebook_path}")
    nb = nbformat.read(notebook_path, as_version=4)
    changed = False
    for cell in nb.cells:
        if cell.cell_type in ("code", "Python"):
            original_source = cell.source
            if not reverse:
                cell.source = inject_into_text(cell.source, paths)
            else:
                cell.source = reverse_inject_text(cell.source, paths)
            if original_source != cell.source:
                changed = True
                print(f"  Modified cell in {notebook_path.name}")
    if changed:
        nbformat.write(nb, notebook_path)
        print(f"  Saved updated notebook: {notebook_path}")


def main(reverse=False, machine="derecho"):
    paths = load_paths(machine)
    # gallery/notebooks/ is sibling to this package directory
    notebooks_path = Path(__file__).parent.parent / "gallery" / "notebooks"
    # ci_case_setup.ipynb lives in tools/ alongside the package
    ci_notebook = Path(__file__).parent.parent / "tools" / "ci_case_setup.ipynb"

    if ci_notebook.exists():
        process_notebook(ci_notebook, paths, reverse)

    for root, _, files in os.walk(notebooks_path):
        for name in files:
            if not name.endswith(".ipynb"):
                continue
            process_notebook(Path(root) / name, paths, reverse)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inject or reverse-inject paths in notebooks."
    )
    parser.add_argument(
        "--reverse", action="store_true", help="Reverse the path injection."
    )
    parser.add_argument(
        "--machine",
        default="derecho",
        help="Which machine's paths to use (default: derecho).",
    )
    args = parser.parse_args()
    main(reverse=args.reverse, machine=args.machine)
