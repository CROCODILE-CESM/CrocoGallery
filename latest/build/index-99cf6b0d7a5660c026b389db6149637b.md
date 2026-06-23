# CROCODILE Workshop 2026

Welcome to the 2026 CROCODILE workshop! This section collects all hands-on
materials for the workshop sessions. Each session links directly to the relevant
tutorial or notebook in the gallery — no separate install needed.

## Agenda

<!-- Replace the src URL with: File → Share → Publish to web → Embed → copy URL -->
<iframe
  src="https://docs.google.com/document/d/e/2PACX-1vTT0OYZkaimKQAfdpB2u5OyqLKdJ2TrB2trDu4bbHAFC2lPGYzZJ9fAzOYYVsdIFBHqRizsZwa1MMFe/pub?embedded=true"
  width="100%"
  height="520"
  frameborder="0"
  style="border:1px solid #e0e0e0; border-radius:4px;">
  <a href="https://docs.google.com/document/d/PLACEHOLDER">
    Workshop Agenda (Google Doc)
  </a>
</iframe>

## Before you start

Make sure you have the following ready before the workshop:

1. **Conda environment** — the `CrocoDash` environment must be installed.
   See the [installation guide](https://crocodile-cesm.github.io/CrocoDash/latest/installation.html).
2. **CESM install** — a compatible CESM source tree. On Derecho the shared
   install is at `~/work/installs/CROCESM_workshop_2025` (path TBC for 2026).
3. **Input data paths** — GEBCO bathymetry and a CESM project allocation
   (`ncgd0011` for NCAR users).
4. **JupyterHub access** — log in to [JupyterHub on Casper](https://jupyterhub.hpc.ucar.edu)
   and start a server with the `CrocoDash` kernel.

## Sessions

### Session 1 — CrocoDash: Regional Ocean Model Setup

Work through the [Getting Started tutorial](crocodash_tutorial.ipynb) to build
a regional MOM6 domain, configure a CESM case, prepare forcing data, and submit
a run.

**Discussion questions after Session 1:**

- What domain would you model for your own research? What resolution and depth
  would you choose?
- Try swapping the compset to add CICE (`GR_JRA`). What files change in the case
  directory?
- What happens if you change `min_depth` in `Topo`? Try 5 m vs. 50 m and plot
  the result.

**Going further (self-guided):**

| Topic | Notebook |
|---|---|
| Arctic / Antarctic domains | [Grids for New Projections](../crocodash/features/new_projections.ipynb) |
| Sea ice (CICE) or BGC (MARBL) | [Coupled Models](../crocodash/features/coupling.ipynb) |
| Tides | [Add Tides](../crocodash/features/add_tides.ipynb) |
| River runoff | [Add Runoff](../crocodash/features/add_runoff.ipynb) |
| NWA12 real-world example | [Use Case: NWA12](../crocodash/use_cases/three_boundary.ipynb) |

---

*More sessions will appear here as the workshop agenda is finalised.*
*Check back or watch the [CrocoGallery repo](https://github.com/CROCODILE-CESM/CrocoGallery) for updates.*
