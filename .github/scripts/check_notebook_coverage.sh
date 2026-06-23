#!/bin/bash
# Checks that every CrocoDash notebook known to crocogallery is explicitly
# listed in .github/notebooks.yml as either 'run' or 'skip'.
# Exits non-zero if any notebook is missing from the config.
#
# To add a notebook to CI:   add it to the 'run' list in .github/notebooks.yml
# To exclude a notebook:     add it to the 'skip' list with a reason

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONFIG_FILE="$REPO_ROOT/.github/notebooks.yml"

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "ERROR: $CONFIG_FILE not found"
  exit 1
fi

python3 - "$REPO_ROOT" "$CONFIG_FILE" <<'EOF'
import sys
import yaml
from pathlib import Path

repo_root = Path(sys.argv[1])
config_file = Path(sys.argv[2])

# All CrocoDash notebooks via the package API
sys.path.insert(0, str(repo_root))
from crocogallery import list_notebooks

gallery_notebooks = {
    str(path.relative_to(repo_root)): nb_id
    for nb_id, path in list_notebooks().items()
    if path.relative_to(repo_root).parts[0] == "crocodash"
}

# All notebooks covered by the config
with open(config_file) as f:
    config = yaml.safe_load(f)

covered = set()
for nb in config.get("run", []):
    covered.add(nb)
for entry in config.get("skip", []):
    covered.add(entry["path"])

missing = sorted(set(gallery_notebooks) - covered)
extra = sorted(covered - set(gallery_notebooks))

ok = True
if missing:
    print("ERROR: notebooks not listed in .github/notebooks.yml:")
    print("  Add each to 'run' to include in CI, or to 'skip' with a reason.")
    for nb in missing:
        print(f"  - {nb}  # id: {gallery_notebooks[nb]}")
    ok = False

if extra:
    print("WARNING: notebooks.yml references paths that no longer exist:")
    for nb in extra:
        print(f"  - {nb}")
    ok = False

if ok:
    print(f"All {len(gallery_notebooks)} CrocoDash notebooks are covered in .github/notebooks.yml.")

sys.exit(0 if ok else 1)
EOF
