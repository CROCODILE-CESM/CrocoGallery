from pathlib import Path

from .inject_paths import (
    load_paths,
    inject_into_text,
    reverse_inject_text,
    process_notebook,
)

# Root of the gallery repo (parent of this package directory).
# Works for editable installs where the source tree is on sys.path directly.
_GALLERY_ROOT = Path(__file__).parent.parent

_SKIP_DIRS = {".ipynb_checkpoints", "_build", "__pycache__"}


def list_notebooks() -> dict:
    """Return {notebook_id: Path} for every .ipynb in the gallery.

    ID format: dot-separated path relative to the gallery root, no extension.
    Example: "crocodash.tutorials.crocodash_tutorial"
    """
    result = {}
    for nb_path in sorted(_GALLERY_ROOT.rglob("*.ipynb")):
        if any(part in _SKIP_DIRS for part in nb_path.parts):
            continue
        rel = nb_path.relative_to(_GALLERY_ROOT)
        nb_id = ".".join(rel.with_suffix("").parts)
        result[nb_id] = nb_path
    return result


def get_notebook_path(notebook_id: str) -> Path:
    """Return the absolute Path for a gallery notebook given its dot-separated ID.

    Raises KeyError with a helpful message listing available IDs if not found.
    """
    notebooks = list_notebooks()
    if notebook_id not in notebooks:
        available = "\n  ".join(sorted(notebooks))
        raise KeyError(
            f"Unknown notebook {notebook_id!r}. Available:\n  {available}"
        )
    return notebooks[notebook_id]


__all__ = [
    "load_paths",
    "inject_into_text",
    "reverse_inject_text",
    "process_notebook",
    "list_notebooks",
    "get_notebook_path",
]
