---
title: Welcome to the 2026 CROCODILE Workshop!
---

<div class="ws-hero">
  <div class="cd-hero__eyebrow">CROCODILE · Workshop 2026</div>
  <h1 class="cd-hero__title">Regional ocean modeling!</h1>
  <p class="cd-hero__desc">
    Hands-on MOM6-in-CESM: build a grid, force it, run it, and look at the output with us!
  </p>
  <div class="cd-hero__actions">
    <a class="cd-btn cd-btn--primary" href="#agenda">View the agenda ↓</a>
    <a class="cd-btn cd-btn--outline" href="../crocodash/tutorial">Start the tutorials</a>
  </div>
</div>

<div class="ws-stats">
  <div class="ws-stat">
    <div class="ws-stat__label">When</div>
    <div class="ws-stat__value">September 28 - October 3</div>
  </div>
  <div class="ws-stat">
    <div class="ws-stat__label">Where</div>
    <div class="ws-stat__value">NCAR Mesa Lab</div>
  </div>
  <div class="ws-stat">
    <div class="ws-stat__label">Format</div>
    <div class="ws-stat__value">Talks & Hacking</div>
  </div>
  <div class="ws-stat">
    <div class="ws-stat__label">Bring</div>
    <div class="ws-stat__value">Laptop + GLADE account</div>
  </div>
</div>

:::{important} Before you arrive
The first thing we'll do at the workshop is set up all the CROCODILE tools together. If you have time beforehand, working through these three steps will help the first practicum go smoothly.

1. **Log in to the supercomputer.** Go to [OnDemand](https://ondemand.hpc.ucar.edu/) and log in with your NCAR account (you should have received an email with setup instructions). Click **Interactive Apps → Jupyter**, and launch a session with queue `Casper PBS Batch`, memory `10GB`, walltime `2 hours`.

   🖼️ *Screenshot: OnDemand's "Interactive Apps" menu → the Jupyter launch form with the three settings filled in*

2. **Create a version-controlled workspace.** We've set up a template repository, [CrocodileWorkspace](https://github.com/CROCODILE-CESM/CrocodileWorkspace), with everything you'll need for the workshop.
   - Click the green ["Use this template → Create a new repository"](https://github.com/new?template_name=CrocodileWorkspace&template_owner=CROCODILE-CESM) button in the top right corner.
   - Name your repo — we recommend `Bask` (the name for a group of crocodiles), since that's what we'll use for the tutorial names. For reference, the instructor's copy is at [github.com/manishvenu/Bask](https://github.com/manishvenu/Bask).
   - Keep it **Public** and click **Create Repository**.

   🖼️ *Screenshot: GitHub's "Use this template" button, and the repo creation form filled in*

3. **Install the CROCODILE tools.**
   - Open a terminal: from your OnDemand session (Step 1), go to **My Interactive Sessions**, start it with the green button, then click the **Terminal** card at the bottom of the page.
   - Move to your `$WORK` directory — supercomputer users get 2 TB of space there, which is a good place to install:

     ```
     cd $WORK
     ```
   - Clone your new workspace repo. This keeps it version-controlled, so you can push your regional models back to GitHub — reproducible and online:

     ```
     git clone https://github.com/<YOUR USERNAME>/<YOUR WORKSPACE NAME>

     # e.g.
     git clone https://github.com/manishvenu/Bask
     ```
   - Run the installer. `install.sh` takes flags for installing individual pieces (`--crocodash` for our regional setup tool, `--CESM` for CESM itself — run `./install.sh -h` for the full list), but for the workshop, one flag installs everything you'll need:

     ```
     cd $WORK/<YOUR WORKSPACE DIRECTORY NAME>
     ./install.sh --workshop
     ```

   🖼️ *Screenshot: terminal output of "./install.sh --workshop" completing successfully*

Stuck? [Open an issue](https://github.com/CROCODILE-CESM/CrocodileWorkspace/issues) on
CrocodileWorkspace and we'll sort it before day one.
:::

(agenda)=
## Agenda

<div class="ws-agenda">
  <div class="ws-agenda__bar">
    <span>📅 Workshop Agenda (live document, updated as we go)</span>
    <a href="https://docs.google.com/document/d/1zLcMDwWS8vMNpXOzU1JkSlXAePDdutCHVwG48DkeLNA/edit?usp=sharing"
       target="_blank" rel="noopener">Open in Google Docs ↗</a>
  </div>
  <iframe
    src="https://docs.google.com/document/d/e/2PACX-1vTT0OYZkaimKQAfdpB2u5OyqLKdJ2TrB2trDu4bbHAFC2lPGYzZJ9fAzOYYVsdIFBHqRizsZwa1MMFe/pub?embedded=true&rm=minimal"
    title="2026 CROCODILE Workshop Agenda"
    loading="lazy">
  </iframe>
</div>
