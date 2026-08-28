#!/bin/bash
# Checks that notebooks do not contain hardcoded /glade paths.
# Paths that legitimately contain /glade (e.g. Derecho-specific note cells)
# are listed in GLADE_EXCEPTIONS below.

GLADE_EXCEPTIONS=(
  "crocodash/configure_forcings.ipynb"   # Derecho-specific note cells (TPXO/CHL/GLOFAS/MARBL default paths)
  "crocodash/advanced/nesting_demo.ipynb"
  "crocodash/projects"   # Workshop project briefs; participant-specific /glade paths are expected
  "crocodash/use_cases"
  "workshop_2026"
  "crococamp"          # CrocoCamp notebooks are NCAR-specific; /glade paths are expected
  "dart/tutorial1_real_observations.ipynb"   # Derecho-specific DART build path in the setup cell
)

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
matches=$(grep -rnw --include="*.ipynb" -e "/glade" \
  crocodash/ crococamp/ tools/ workshop_2026/ dart/ 2>/dev/null || true)
matches=$(filter_exceptions "$matches" "${GLADE_EXCEPTIONS[@]}")

if [[ -n "$matches" ]]; then
  echo "❌ Found hardcoded '/glade' paths in the following files:"
  echo "$matches"
  echo "Please remove or parameterize them."
  exit 1
else
  echo "✅ No unexpected '/glade' paths found."
fi
