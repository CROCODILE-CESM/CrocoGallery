# Using CUPiD to Diagnose Regional MOM6 runs

![CUPiD Logo](../../images/CUPiD_logo.png)

CESM3 includes a python-based postprocessing tool, CESM Unified Postprocessing and Diagnostics ([CUPiD](https://ncar.github.io/CUPiD/)).
Development is guided by its vision statement:

> CUPiD is a “one stop shop” that enables and integrates timeseries file generation, data standardization, diagnostics, and metrics from all CESM components.
>
> This collaborative effort aims to simplify the user experience of running diagnostics by calling post-processing tools directly from CUPiD,
running all component diagnostics from the same tool as either part of the CIME workflow or independently,
and sharing python code and a standard conda environment across components.

## CUPiD for Regional MOM6

As the vision statement states, CUPiD is a broad package designed to pull many independent tasks together.
For postprocessing, CUPiD is automating the process of converting CESM output to the standard format required for the Coupled Model Intercomparison Project ([CMIP](https://wcrp-cmip.org/)).

This tutorial is going to focus on the diagnostic side of CUPiD.
CUPiD is designed to make it easy for users to run existing notebooks to look at output from all components of CESM,
but we will focus on a set of MOM6 notebooks meant to analyze regional runs.
Participants will install CUPiD and then familiarize themselves with it by

1. looking at diagnostics from an existing regional MOM6 run in stand-alone mode,
1. running the same diagnostics on their own regional MOM6 run, and
1. learning how to add their own diagnostic notebooks to the CUPiD suite.

We will touch briefly on generating time series files from CESM history files as well.
