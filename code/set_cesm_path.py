import json
import os
import sys
from pathlib import Path


path_in = Path(__file__).parent / "data_paths.json"
path_out = Path(__file__).parent / "data_paths_loc.json"
# Get CESM path from the first argument if provided, else from the CESMROOT environment variable
if len(sys.argv) > 1:
    cesm_path = sys.argv[1]
else:
    try:
        cesm_path = os.environ["CESMROOT"]
    except KeyError:
        print(
            "Error: No argument provided and CESMROOT environment variable is not set.",
            file=sys.stderr,
        )
        sys.exit(1)

# Load existing JSON
with open(path_in) as f:
    data = json.load(f)

# Update and save
data["CESM"] = cesm_path
with open(path_out, "w") as f:
    json.dump(data, f, indent=2)
