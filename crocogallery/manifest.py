"""Write (or check) gallery_manifest.json, the gallery's file index.

Downstream tools (e.g. `crocodash template`) fetch gallery files over HTTP
from a pinned ref and cannot glob a remote tree, so this manifest records
where everything lives: every notebook by ID, the loose template assets,
and the known_paths.json table.

    python -m crocogallery.manifest           # regenerate
    python -m crocogallery.manifest --check   # exit 1 if stale (CI)
"""

import argparse
import json
import sys

from . import list_notebooks
from .inject_paths import gallery_root
from .template import TEMPLATE_ASSETS, find_template_asset

MANIFEST_NAME = "gallery_manifest.json"


def build_manifest():
    root = gallery_root()
    return {
        "notebooks": {
            nb_id: path.relative_to(root).as_posix()
            for nb_id, path in sorted(list_notebooks().items())
        },
        "assets": {
            name: find_template_asset(name).relative_to(root).as_posix()
            for name in sorted(TEMPLATE_ASSETS.values())
        },
        "known_paths": "crocogallery/known_paths.json",
    }


def render_manifest():
    return json.dumps(build_manifest(), indent=2) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m crocogallery.manifest")
    parser.add_argument(
        "--check",
        action="store_true",
        help=f"Exit 1 if {MANIFEST_NAME} is out of date instead of rewriting it.",
    )
    args = parser.parse_args(argv)

    path = gallery_root() / MANIFEST_NAME
    expected = render_manifest()
    if args.check:
        if not path.exists() or path.read_text() != expected:
            print(
                f"{MANIFEST_NAME} is out of date. Regenerate it with:\n"
                "  python -m crocogallery.manifest",
                file=sys.stderr,
            )
            return 1
        print(f"{MANIFEST_NAME} is up to date.")
        return 0
    path.write_text(expected)
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
