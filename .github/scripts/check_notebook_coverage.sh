#!/bin/bash
# Checks that every notebook under gallery/notebooks/CrocoDash/ is explicitly
# listed in .github/notebooks.yml as either 'run' or 'skip'.
# Exits non-zero if any notebook is missing from the config.
#
# To add a notebook to CI:   add it to the 'run' list in .github/notebooks.yml
# To exclude a notebook:     add it to the 'skip' list with a reason

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

NOTEBOOK_DIR="$REPO_ROOT/gallery/notebooks/CrocoDash"
CONFIG_FILE="$REPO_ROOT/.github/notebooks.yml"

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "ERROR: $CONFIG_FILE not found"
  exit 1
fi

# Find all CrocoDash notebooks on disk
mapfile -t ALL_NOTEBOOKS < <(
  find "$NOTEBOOK_DIR" -name "*.ipynb" \
    -not -path "*/.ipynb_checkpoints/*" \
    | sort
)

# Extract all paths covered by the config (both run and skip)
mapfile -t COVERED_NOTEBOOKS < <(
  python3 -c "
import yaml, sys
with open('$CONFIG_FILE') as f:
    config = yaml.safe_load(f)
for nb in config.get('run', []):
    print(nb)
for entry in config.get('skip', []):
    print(entry['path'])
"
)

MISSING=()
for nb in "${ALL_NOTEBOOKS[@]}"; do
  rel_path="${nb#"$REPO_ROOT"/}"
  found=false
  for covered in "${COVERED_NOTEBOOKS[@]}"; do
    if [[ "$covered" == "$rel_path" ]]; then
      found=true
      break
    fi
  done
  if [[ "$found" == false ]]; then
    MISSING+=("$rel_path")
  fi
done

if [[ ${#MISSING[@]} -gt 0 ]]; then
  echo "ERROR: The following notebooks are not listed in .github/notebooks.yml."
  echo "  Add each to the 'run' section to include in CI, or to 'skip' with a reason."
  for nb in "${MISSING[@]}"; do
    echo "  - $nb"
  done
  exit 1
fi

echo "All CrocoDash notebooks are covered in .github/notebooks.yml."
