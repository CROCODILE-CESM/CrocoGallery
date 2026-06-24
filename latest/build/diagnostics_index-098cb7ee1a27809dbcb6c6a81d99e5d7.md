---
title: Diagnostics
description: Diagnostics and analysis for regional MOM6 ocean models using mom6-tools.
---

<div class="croco-subspace-header croco-subspace-header--diagnostics">
  <div class="croco-subspace-header__icon">📊</div>
  <h1>Diagnostics</h1>
  <p>
    Analyze and visualize regional MOM6 model output using mom6-tools — the recommended
    diagnostics package for the CROCODILE ecosystem.
  </p>
  <a class="cd-btn cd-btn--outline" href="https://github.com/NCAR/mom6-tools">mom6-tools on GitHub ↗</a>
</div>

## What You Can Do

<div class="cd-features-grid">
  <div class="cd-feature">
    <div class="cd-feature__icon">📋</div>
    <h3>Time-Series Diagnostics</h3>
    <p>Track volume-mean temperature, salinity, and scalar metrics over the course of your model run.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">🌊</div>
    <h3>Surface & Layer Fields</h3>
    <p>Diagnose SSH, SST, MLD, and other surface and layer fields from MOM6 output.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">🔗</div>
    <h3>OBC Diagnostics</h3>
    <p>Inspect open boundary condition quality and variability to evaluate forcing inputs.</p>
  </div>
  <div class="cd-feature">
    <div class="cd-feature__icon">📐</div>
    <h3>Budget Analysis</h3>
    <p>Heat and salt budget diagnostics for your regional domain.</p>
  </div>
</div>

## Explore the Notebooks

<div class="cd-nav-cards">
  <a class="cd-nav-card" href="diagnostics/mom6_tools">
    <h3>Getting Started with mom6-tools</h3>
    <p>Install mom6-tools and run your first diagnostics on regional MOM6 output.</p>
  </a>
</div>

## Legacy: CUPiD Diagnostics

CUPiD was the previous diagnostics framework used in this project. It is no longer actively developed for regional MOM6 use, but the documentation is preserved below for reference.

<details>
<summary>CUPiD documentation (legacy)</summary>

<div class="cd-nav-cards">
  <a class="cd-nav-card" href="diagnostics/CUPiD_intro">
    <h3>CUPiD Introduction</h3>
    <p>Overview of CUPiD and how it fits into the regional MOM6 diagnostics workflow.</p>
  </a>
  <a class="cd-nav-card" href="diagnostics/CUPiD_for_regional_MOM6">
    <h3>CUPiD for Regional MOM6</h3>
    <p>Applying CUPiD diagnostics specifically to regional MOM6 model output.</p>
  </a>
  <a class="cd-nav-card" href="diagnostics/CUPiD_in_CESM_Workflow">
    <h3>CUPiD in the CESM Workflow</h3>
    <p>Integrating CUPiD into your end-to-end CESM case post-processing pipeline.</p>
  </a>
  <a class="cd-nav-card" href="diagnostics/standalone_CUPiD">
    <h3>Standalone CUPiD</h3>
    <p>Running CUPiD outside of CESM for standalone MOM6 or custom configurations.</p>
  </a>
  <a class="cd-nav-card" href="diagnostics/CUPiD_output">
    <h3>Understanding CUPiD Output</h3>
    <p>A guide to reading and interpreting CUPiD diagnostic output files and plots.</p>
  </a>
  <a class="cd-nav-card" href="diagnostics/contributing_to_CUPiD">
    <h3>Contributing to CUPiD</h3>
    <p>How to add new diagnostics, notebooks, or datasets to the CUPiD framework.</p>
  </a>
</div>

</details>
