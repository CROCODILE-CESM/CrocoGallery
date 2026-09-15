---
title: DART Data Assimilation
description: Ensemble data assimilation for regional MOM6 in CESM using DART (Data Assimilation Research Testbed). Observation preparation, filter configuration, assimilation cycling, and diagnostics.
---

<div class="croco-subspace-header croco-subspace-header--dart">
  <div class="croco-subspace-header__icon">🎯</div>
  <h1>DART Data Assimilation</h1>
  <p>
    Ensemble data assimilation for regional MOM6 in CESM using DART: the Data Assimilation
    Research Testbed from NSF NCAR. Constrain your model with observations
    to produce improved ocean state estimates.
  </p>
  <a class="cd-btn cd-btn--outline" href="tutorial1_real_observations.ipynb">Get Started →</a>
</div>

## What You Can Do


<div class="cd-features-grid">
  <div class="cd-feature">
    <div class="cd-feature__icon">📡</div>
    <h3>Observation Preparation</h3>
    <p>Convert CrocoLake observations (Argo, GLODAP) into DART's
    obs_sequence format.
    Or create synthetic observations for Observation System Simulation Experiments</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">🔢</div>
    <h3>Ensemble Filter</h3>
    <p>Configure DART's Ensemble Filters, adaptive inflation and
    localization for regional ocean domains.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">🔄</div>
    <h3>Assimilation Cycling</h3>
    <p>Run forecast–assimilate–update cycles via the DART–CESM interface, fully
    integrated with the standard CESM job-submission workflow.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">📊</div>
    <h3>Diagnostics</h3>
    <p>Assess assimilation quality with observation-space RMSE/spread diagnostics and
    state-space increment maps.</p>
  </div>
</div>

<p>&nbsp;</p>

## The Tutorial Series

This tutorial series includes three notebooks, designed to be worked through in order.
Each notebook's output feeds into the next. Only interested in real observations? 
Feel free to skip the synthetic observations notebook and jump straight to cycling DART-CESM.

<div class="cd-nav-cards">
  <a class="cd-nav-card" href="tutorial1_real_observations.ipynb">
    <h3>1. Working with Real Observations</h3>
    <p>Turn real Argo profiles from CrocoLake into DART obs_seq files with dartobsgen.
     You leave with a directory of observations ready to assimilate.</p>
  </a>
  <a class="cd-nav-card" href="tutorial2_synthetic_observations.ipynb">
    <h3>2. Synthetic Observations</h3>
    <p>Sample a model state with DART's perfect_model_obs at the Tutorial 1 locations
    plus random ones you design. You leave with a synthetic observing network for an OSSE.</p>
  </a>
  <a class="cd-nav-card" href="tutorial3_cycling_dart_cesm.ipynb">
    <h3>3. Cycling DART–CESM</h3>
    <p>Build a multi-instance regional MOM6 ensemble in CESM, assimilate your
    observations every 24 hours, and diagnose the results. You leave with a running DA
    experiment. </p>
  </a>
</div>
