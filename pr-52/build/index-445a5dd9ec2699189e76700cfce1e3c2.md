---
title: model2obs
description: Model–observation comparisons for regional MOM6 using CrocoLake, a cloud-optimized Parquet observational database for fast access to observational data.
---

<div class="croco-subspace-header croco-subspace-header--model2obs">
  <div class="croco-subspace-header__icon">🔬</div>
  <h1>model2obs</h1>
  <p>
    Model–observation comparisons for regional MOM6 using CrocoLake, a cloud-optimized,
    Parquet-based observational database for fast access to observational data.
  </p>
  <a class="cd-btn cd-btn--outline" href="tutorial_MOM6-CL-comparison-Hawaii.ipynb">Get Started →</a>
  <a class="cd-btn cd-btn--outline" href="https://github.com/CROCODILE-CESM/model2obs">model2obs on GitHub ↗</a>
</div>

## What You Can Do


<div class="cd-features-grid">
  <div class="cd-feature">
    <div class="cd-feature__icon">🗄️</div>
    <h3>CrocoLake Access</h3>
    <p>Query a cloud-optimized Parquet database of QCed in-situ observations
    (Argo, GLODAP, Spray Gliders) without downloading large files.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">📍</div>
    <h3>Model-observation comparison</h3>
    <p>Use model2obs to interpolate MOM6 output onto the time and space of the observations,
    using DART's forward operators under the hood.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">📈</div>
    <h3>Visualization</h3>
    <p>Visualize CrocoLake data and model–observation differences on interactive maps and
    profile plots.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">💪️</div>
    <h3>Heavy lifting</h3>
    <p>Work with larger-than-memory CrocoLake datasets, and use parallel execution capacity of model2obs to speed up interpolation on large-domain runs.</p>
  </div>
</div>

<p>&nbsp;</p>

## The Tutorial Series

This tutorial series includes three notebooks. The first two notebooks show how to interpolate MOM6 output onto CrocoLake observations' space using model2obs: start small and serial to learn the machinery (first notebook), then scale up to a parallel, large-domain run (second notebook). The third notebook guides you through how to use CrocoLake-like datasets which are larger-than-memory.

If you don't remember how to get started with the packages installation, see the [Before you arrive instructions](../workshop_2026/index.md).

<div class="cd-nav-cards">
  <a class="cd-nav-card" href="tutorial_MOM6-CL-comparison-Hawaii.ipynb">
    <h3>1. Small Domain, Serial</h3>
    <p>Interpolate a short CESM-MOM6 run around the Hawaiian islands onto CrocoLake
    observations. You leave knowing the basic model2obs workflow and how to plot the
    results on an interactive map.</p>
  </a>
  <a class="cd-nav-card" href="tutorial1_MOM6-CL-comparison-parallel.ipynb">
    <h3>2. Large Domain, Parallel</h3>
    <p>Run the same workflow but in parallel, on a larger NorthWest Atlantic domain. You leave able to compare large-domain runs against
    observations efficiently.</p>
  </a>
  <a class="cd-nav-card" href="tutorial3_CrocoLake_map_temperature.ipynb">
    <h3>3. Exploring CrocoLake</h3>
    <p>Read and filter CrocoLake's Parquet files with pandas and dask, and map
    temperature measurements in the North West Atlantic. You leave able to handle
    larger-than-memory observational datasets.</p>
  </a>
</div>
