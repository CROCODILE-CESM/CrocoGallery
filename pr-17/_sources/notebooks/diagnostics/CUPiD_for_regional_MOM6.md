# Using CUPiD to Diagnose Regional MOM6 runs

![CUPiD Logo](../../images/CUPiD/logo.png)

CESM3 includes a python-based postprocessing tool, CESM Unified Postprocessing and Diagnostics ([CUPiD](https://ncar.github.io/CUPiD/)).
Development is guided by its vision statement:

> CUPiD is a “one stop shop” that enables and integrates timeseries file generation, data standardization, diagnostics, and metrics from all CESM components.
>
> This collaborative effort aims to simplify the user experience of running diagnostics by calling post-processing tools directly from CUPiD,
running all component diagnostics from the same tool as either part of the CIME workflow or independently,
and sharing python code and a standard conda environment across components.

## CUPiD for Regional MOM6

IMAGE/GIF NEEDED HERE

CUPiD is a broad package designed to pull many independent tasks together and standardize common parts of a postprocessing workflow.
For postprocessing, CUPiD is automating the process of converting CESM output to the standard format required for the Coupled Model Intercomparison Project ([CMIP](https://wcrp-cmip.org/)).

This tutorial is going to focus on the diagnostic side of CUPiD and tools for accessing and manipulating MOM6 output.
CUPiD is designed to make it easy for users to run existing notebooks to look at output from all components of CESM,
but we will focus on a set of MOM6 notebooks meant to analyze regional runs.
Participants will install CUPiD and then familiarize themselves with it by

1. looking at diagnostics from an existing regional MOM6 run in stand-alone mode (no CESM integration),
2. running the same diagnostics on their own regional MOM6 run (with CESM integration), and
3. learning how to add their own diagnostic notebooks to the CUPiD suite.

We will touch briefly on generating time series files from CESM history files as well.

## Your Turn!
As we progress through this tutorial, thin about what kinds of diagnostics might be helpful for general regions and your specific regions of interest. 

### Ideas for New Notebooks
This is a brief list of some possible topics/notebooks to contribute from a regional ocean perspective. Add your own!
- **Comparison to Other Model Output/Reanalysis Products:** compare model output to other model output or a reanalysis product ([Global Atmspheric Observations Example](https://github.com/NCAR/CUPiD/blob/main/nblibrary/atm/Global_PSL_NMSE_compare_obs_lens.ipynb)). CUPiD is already setup with this in mind with the `base_case` global parameters.
- **Transport through Passages:** MOM6 lets you define transects to calculate transport through different passages. These transects are defined in the `diag_table` so a notebook would need to chek if any transects are defined and then visualize/analyze them appropriately. Comparing to observations could be tricky and very helpful!
- **Region Aware Diagnostics:** Different regions might benefit from a different standard sets of diagnostics. Even simple adjustments like choosing a different projection for plotting or looking at sea ice in the arctic. 