#!/usr/bin/env python3
"""
Generates the notebook status badge table in gallery/crocodash_index.md.
Reads the 'run' list and optional 'names' from .github/notebooks.yml, then
replaces content between the marker comments in crocodash_index.md.

Markers in crocodash_index.md:
    <!-- NOTEBOOK_BADGES_START -->
    <!-- NOTEBOOK_BADGES_END -->
"""

import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_FILE = REPO_ROOT / ".github" / "notebooks.yml"
INDEX_FILE = REPO_ROOT / "gallery" / "notebook_status.md"

REPO = "CROCODILE-CESM/CrocoGallery"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/badges"
SHIELDS_BASE = "https://img.shields.io/endpoint"

START = "<!-- NOTEBOOK_BADGES_START -->"
END = "<!-- NOTEBOOK_BADGES_END -->"


def notebook_key(path):
    """gallery/notebooks/CrocoDash/features/add_chl.ipynb -> CrocoDash_features_add_chl"""
    return path.replace("gallery/notebooks/", "").replace(".ipynb", "").replace("/", "_")


def notebook_link(path):
    """gallery/notebooks/CrocoDash/tutorials/crocodash_tutorial.ipynb -> notebooks/CrocoDash/tutorials/crocodash_tutorial"""
    return path.replace("gallery/", "").replace(".ipynb", "")


def auto_name(path):
    return Path(path).stem.replace("_", " ").title()


def main():
    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)

    names = config.get("names", {})
    run_list = config.get("run", [])

    rows = ["| Notebook | Status |", "|---|---|"]
    for nb_path in run_list:
        display = names.get(nb_path, auto_name(nb_path))
        link = notebook_link(nb_path)
        key = notebook_key(nb_path)
        badge_url = f"{SHIELDS_BASE}?url={RAW_BASE}/{key}.json&style=flat-square"
        rows.append(f"| [{display}]({link}) | ![status]({badge_url}) |")

    table = "\n".join(rows)
    injected = f"{START}\n{table}\n{END}"

    content = INDEX_FILE.read_text()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(content):
        print(f"ERROR: markers not found in {INDEX_FILE}", file=sys.stderr)
        sys.exit(1)

    INDEX_FILE.write_text(pattern.sub(injected, content))
    print(f"Badge table updated with {len(run_list)} notebooks.")


if __name__ == "__main__":
    main()
