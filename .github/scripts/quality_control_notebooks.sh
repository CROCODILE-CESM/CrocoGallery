#!/bin/bash

# Exceptions for /glade paths
GLADE_EXCEPTIONS=(
  "gallery/notebooks/CrocoDash/projects"
  "gallery/notebooks/projects"
  "gallery/notebooks/CrocoDash/features"
  "gallery/notebooks/CrocoDash/tutorials"
  "gallery/notebooks/diagnostics/cupid_output"
)

## Function to filter out exceptions (files & folders)
filter_exceptions() {
  local matches="$1"
  shift
  local exceptions=("$@")
  for ex in "${exceptions[@]}"; do
    matches=$(echo "$matches" | grep -v "$ex" || true)
  done
  echo "$matches"
}

echo "Checking for hardcoded '/glade' paths..."
matches=$(grep -rnw --include="*.ipynb" -e "/glade" gallery/notebooks || true)
matches=$(filter_exceptions "$matches" "${GLADE_EXCEPTIONS[@]}")

if [[ -n "$matches" ]]; then
  echo "❌ Found hardcoded '/glade' paths in the following files:"
  echo "$matches"
  echo "Please remove or parameterize them."
  exit 1
else
  echo "✅ No '/glade' paths found."
fi
