---
title: Projects
description: Standalone CrocoDash projects. The tutorials teach the tools; each project is one problem to solve on a region of your own.
---

# Projects

The tutorials walk you through CrocoDash step by step. A project gives you a problem
instead, on a region you pick, and expects you to go back to the tutorials for the how.

Each project stands on its own — start anywhere.

| Project | The problem | Builds on |
|---|---|---|
| Design your domain | Get a region you care about from a bounding box to a case that runs | [grids](../grids.ipynb), [bathymetry](../bathymetry.ipynb), [case setup](../case_setup.ipynb), [forcings](../process_forcings.ipynb) |
| Force it differently | Change what drives the boundaries and surface, and show what it did to the solution | [configure forcings](../configure_forcings.ipynb) |
| Resolution study | Run one region at two resolutions and defend a choice with evidence | [grids](../grids.ipynb) |
| Make it stable | Find out why a case blows up and fix the cause, not the timestep | [bathymetry](../bathymetry.ipynb), [interior OBC segments](../advanced/interior_obc_segments.ipynb) |
| Add a component | Couple sea ice, waves, or BGC to a working ocean-only case | [MOM6 + CICE](../use_cases/mom6_cice_antarctica.ipynb) |
| Share and reproduce | Bundle your case, run someone else's, find where portability breaks | [CLI workflow](../advanced/cli_workflow.md) |

Keep the domain small — a few degrees on a side, a few days of simulation. A region you
can force and run beats one you can only describe.
