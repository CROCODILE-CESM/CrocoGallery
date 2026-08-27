import json
from pathlib import Path
import os
import argparse

_SKIP_DIRS = {".ipynb_checkpoints", "_build", "__pycache__"}


def load_paths(machine, json_path=None):
    """Return the path dict for the given machine key.

    json_path defaults to the bundled known_paths.json in this package.
    The file may be nested ({machine: {KEY: path}}) or flat ({KEY: path});
    a flat file is returned as-is and `machine` is ignored.
    """
    if json_path is None:
        from importlib.resources import files

        json_path = files("crocogallery") / "known_paths.json"
    with open(json_path) as f:
        db = json.load(f)
    if db and all(isinstance(v, str) for v in db.values()):
        # Flat {KEY: path} file -- no machine nesting.
        return db
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
    # Longest values first so a path that is a prefix of another (e.g. a case
    # dir and a file inside it) does not get half-replaced.
    for key, val in sorted(paths.items(), key=lambda kv: len(kv[1]), reverse=True):
        text = text.replace(val, f"<{key}>")
    return text


def process_notebook(notebook_path, paths, reverse, dry_run=False):
    import nbformat

    notebook_path = Path(notebook_path)
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
                verb = "Would modify" if dry_run else "Modified"
                print(f"  {verb} cell in {notebook_path.name}")
    if changed and not dry_run:
        nbformat.write(nb, notebook_path)
        print(f"  Saved updated notebook: {notebook_path}")
    elif changed:
        print(f"  Would update (dry run, not written): {notebook_path}")
    return changed


def gallery_root():
    """Root of the gallery repo (parent of this package directory)."""
    return Path(__file__).parent.parent


def iter_notebooks(targets=None):
    """Yield notebook Paths for the given targets.

    Each target may be a notebook file or a directory (searched recursively).
    With no targets, every notebook in the gallery is used.
    """
    if not targets:
        targets = [gallery_root()]
    for target in targets:
        target = Path(target).expanduser()
        if target.is_dir():
            candidates = sorted(target.rglob("*.ipynb"))
        else:
            candidates = [target]
        for nb_path in candidates:
            if any(part in _SKIP_DIRS for part in nb_path.parts):
                continue
            if not nb_path.exists():
                raise FileNotFoundError(f"No such notebook: {nb_path}")
            yield nb_path


def resolve_paths(
    machine="derecho", json_path=None, extra_paths=None, use_defaults=True
):
    """Build the {KEY: path} mapping used for (reverse-)injection.

    Layers, lowest precedence first: the bundled known_paths.json (unless
    `use_defaults` is False), then `json_path`, then `extra_paths`.
    """
    paths = {}
    if use_defaults:
        try:
            paths.update(load_paths(machine, None))
        except KeyError:
            # A custom json may use its own machine key that the bundled
            # table knows nothing about; only complain if it is our only source.
            if json_path is None:
                raise
    if json_path is not None:
        paths.update(load_paths(machine, json_path))
    if extra_paths:
        paths.update(extra_paths)
    if not paths:
        raise ValueError("No paths to inject: pass --set KEY=VALUE or a --paths-json.")
    return paths


def inject(
    targets=None,
    reverse=False,
    machine="derecho",
    json_path=None,
    extra_paths=None,
    use_defaults=True,
    dry_run=False,
):
    """Inject (or reverse-inject) paths into notebooks. Returns the list changed.

    With dry_run, nothing is written -- the returned list is what *would*
    have changed.
    """
    paths = resolve_paths(machine, json_path, extra_paths, use_defaults)
    changed = []
    for nb_path in iter_notebooks(targets):
        if process_notebook(nb_path, paths, reverse, dry_run):
            changed.append(nb_path)
    return changed


def _parse_set(items):
    """Turn ['KEY=/some/path', ...] into a dict."""
    out = {}
    for item in items or []:
        if "=" not in item:
            raise ValueError(f"--set expects KEY=VALUE, got: {item!r}")
        key, val = item.split("=", 1)
        out[key.strip()] = os.path.expanduser(val)
    return out


def main(
    reverse=False,
    machine="derecho",
    targets=None,
    json_path=None,
    extra_paths=None,
    use_defaults=True,
):
    if targets:
        inject(targets, reverse, machine, json_path, extra_paths, use_defaults)
        return

    paths = resolve_paths(machine, json_path, extra_paths, use_defaults)
    ci_notebook = gallery_root() / "tools" / "ci_case_setup.ipynb"
    if ci_notebook.exists():
        process_notebook(ci_notebook, paths, reverse)
    for nb_path in iter_notebooks():
        process_notebook(nb_path, paths, reverse)


def build_parser():
    parser = argparse.ArgumentParser(
        prog="crocogallery",
        description="Inject or reverse-inject paths in notebooks.",
    )
    parser.add_argument(
        "targets",
        nargs="*",
        help="Notebooks or directories to process. Default: every notebook in the gallery.",
    )
    parser.add_argument(
        "--reverse", action="store_true", help="Reverse the path injection."
    )
    parser.add_argument(
        "--machine",
        default="derecho",
        help="Which machine's paths to use (default: derecho).",
    )
    parser.add_argument(
        "--paths-json",
        default=None,
        help="Your own paths file, either {machine: {KEY: path}} or flat {KEY: path}. "
        "Replaces the bundled known_paths.json.",
    )
    parser.add_argument(
        "--set",
        dest="sets",
        action="append",
        metavar="KEY=VALUE",
        help="Add or override one placeholder, e.g. --set MYGRID=/glade/.../grid.nc. Repeatable.",
    )
    parser.add_argument(
        "--no-defaults",
        action="store_true",
        help="Ignore the bundled known_paths.json and use only --paths-json/--set.",
    )
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    main(
        reverse=args.reverse,
        machine=args.machine,
        targets=args.targets,
        json_path=args.paths_json,
        extra_paths=_parse_set(args.sets),
        use_defaults=not args.no_defaults,
    )
