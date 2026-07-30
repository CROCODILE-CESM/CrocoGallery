---
title: mom6-tools
description: Python-based diagnostics for MOM6 ocean model output using mom6-tools.
---

# mom6-tools

[mom6-tools](https://github.com/NCAR/mom6-tools) is the recommended way to diagnose regional MOM6 output in the CROCODILE ecosystem. It provides a set of Python-based tools for analyzing, visualizing, and quality-controlling MOM6 ocean model output.

## Getting Started

Install mom6-tools from GitHub or PyPI:

```bash
pip install mom6-tools
```

Or install the development version:

```bash
git clone https://github.com/NCAR/mom6-tools
cd mom6-tools
pip install -e .
```

## What mom6-tools Provides

- **Time-series diagnostics** — volume-mean temperature, salinity, and other scalar metrics over the model run
- **Surface and layer diagnostics** — SSH, SST, MLD, and other surface fields
- **OBC diagnostics** — inspect open boundary condition quality and variability
- **Vertical structure** — analyze temperature/salinity profiles and stratification
- **Budget diagnostics** — heat and salt budget analysis for regional domains

## Links

- [GitHub: NCAR/mom6-tools](https://github.com/NCAR/mom6-tools)
- [Documentation](https://mom6-tools.readthedocs.io)
