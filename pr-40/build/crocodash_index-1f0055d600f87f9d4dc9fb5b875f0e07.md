---
title: CrocoDash
description: The Python toolkit for configuring and deploying regional MOM6 ocean models in CESM. Grid generation, boundary conditions, forcing data, and coupling — all in one place.
---

<div class="cd-dev-banner">
  <strong>🚧 This page is under active development.</strong>
  Some features shown here may not be reproducible with the latest tagged release of CrocoDash,
  but can be found on branches in the
  <a href="https://github.com/CROCODILE-CESM/CrocoDash">CrocoDash GitHub repository ↗</a>.
</div>

<div class="cd-hero">
  <div class="cd-hero__eyebrow">CROCODILE Ecosystem</div>
  <h1 class="cd-hero__title">CrocoDash</h1>
  <p class="cd-hero__desc">
    The Python toolkit for configuring, customizing, and setting up regional MOM6 ocean models in CESM.
    From grid generation to boundary conditions — all in one place.
  </p>
  <div class="cd-hero__actions">
    <a class="cd-btn cd-btn--primary" href="notebooks/CrocoDash/tutorials/crocodash_tutorial">Get Started →</a>
    <a class="cd-btn cd-btn--outline" href="https://github.com/CROCODILE-CESM/CrocoDash">GitHub ↗</a>
  </div>
</div>

## What It Produces

<div class="cd-showcase-grid">
  <div class="cd-showcase-item">
    <img src="images/CrocoDash/grid_example.png" alt="Regional grid generation" />
    <p>Regional Grid Generation</p>
  </div>
  <div class="cd-showcase-item">
    <img src="images/CrocoDash/bathymetry.png" alt="Bathymetry and topography" />
    <p>Git-Logged Bathymetry Editing</p>
  </div>
  <div class="cd-showcase-item">
    <img src="images/CrocoDash/obc_forcing.png" alt="Open boundary condition forcing" />
    <p>Boundary Condition Generation</p>
  </div>
  <div class="cd-showcase-item">
    <img src="images/CrocoDash/SSH_speed.png" alt="Sea surface height and speed model output" />
    <p>Model Output</p>
  </div>
</div>

## What CrocoDash Can Do (Beyond General Setup)

<div class="cd-features-grid">
  <div class="cd-feature">
    <div class="cd-feature__icon">🔗</div>
    <h3>Coupling</h3>
    <p>Add BGC and CICE coupled components to your regional ocean configuration.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">🗺️</div>
    <h3>Grid Customization</h3>
    <p>Subset global grids or build custom regional grids for any ocean domain.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">📦</div>
    <h3>Data Products</h3>
    <p>Manage boundary conditions, initial conditions, and forcing data from a variety of data sources.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">🌊</div>
    <h3>Additional Physics</h3>
    <p>Add tides, runoff, chlorophyll, and other components with a single function call.</p>
  </div>
</div>

## Notebook Status

Live CI status for every notebook — badges update automatically after each nightly run.

| Notebook | Status |
|---|---|
| [CrocoDash Tutorial](notebooks/CrocoDash/tutorials/crocodash_tutorial) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_tutorials_crocodash_tutorial.json&style=flat-square) |
| [Add Grids](notebooks/CrocoDash/features/grids/add_grids) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_grids_add_grids.json&style=flat-square) |
| [Subset Global Grid](notebooks/CrocoDash/features/grids/subset_global) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_grids_subset_global.json&style=flat-square) |
| [Add CICE](notebooks/CrocoDash/features/coupling/add_cice) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_coupling_add_cice.json&style=flat-square) |
| [Add Data Products](notebooks/CrocoDash/features/data_handling/add_data_products) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_data_handling_add_data_products.json&style=flat-square) |
| [Too Much Data](notebooks/CrocoDash/features/data_handling/too_much_data) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_data_handling_too_much_data.json&style=flat-square) |
| [Add Chlorophyll](notebooks/CrocoDash/features/add_chl) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_add_chl.json&style=flat-square) |
| [Add Runoff](notebooks/CrocoDash/features/add_rof) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_add_rof.json&style=flat-square) |
| [Add Runoff Product](notebooks/CrocoDash/features/add_runoff_product) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_add_runoff_product.json&style=flat-square) |
| [Add Tides](notebooks/CrocoDash/features/add_tides) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_features_add_tides.json&style=flat-square) |
| [MOM6 + CICE Antarctica](notebooks/CrocoDash/use_cases/mom6_cice_antarctica) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_use_cases_mom6_cice_antarctica.json&style=flat-square) |
| [Three Boundary from T232](notebooks/CrocoDash/use_cases/three_boundary_from_t232) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_use_cases_three_boundary_from_t232.json&style=flat-square) |
| [CrocoDash Projects](notebooks/CrocoDash/projects/CrocoDash) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_projects_CrocoDash.json&style=flat-square) |
| [CICE Antarctica Project](notebooks/CrocoDash/projects/sample_crocodash_projects/CICE_antarctica) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_projects_sample_crocodash_projects_CICE_antarctica.json&style=flat-square) |
| [CICE Arctic Project](notebooks/CrocoDash/projects/sample_crocodash_projects/CICE_arctic) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_projects_sample_crocodash_projects_CICE_arctic.json&style=flat-square) |
| [DROF Project](notebooks/CrocoDash/projects/sample_crocodash_projects/DROF) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_projects_sample_crocodash_projects_DROF.json&style=flat-square) |
| [NWA Project](notebooks/CrocoDash/projects/sample_crocodash_projects/NWA) | ![status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/CROCODILE-CESM/CrocoGallery/badges/CrocoDash_projects_sample_crocodash_projects_NWA.json&style=flat-square) |

## Explore the Content

<div class="cd-nav-cards">
  <a class="cd-nav-card" href="notebooks/CrocoDash/tutorials/crocodash_tutorial">
    <h3>Tutorial</h3>
    <p>End-to-end walkthrough from installation to a running regional model.</p>
  </a>
  <a class="cd-nav-card" href="notebooks/CrocoDash/features/coupling/add_bgc">
    <h3>Feature Notebooks</h3>
    <p>Deep dives into specific CrocoDash capabilities — BGC, CICE, tides, runoff, and more.</p>
  </a>
  <a class="cd-nav-card" href="notebooks/CrocoDash/use_cases/three_boundary">
    <h3>Use Cases</h3>
    <p>Real-world configurations and advanced setups for specific ocean regions.</p>
  </a>
</div>
