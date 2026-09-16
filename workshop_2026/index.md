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
The first thing we'll do at the workshop is set up all the CROCODILE tools. If you have time beforehand, working through these three steps will help the first practicum go smoothly. It should take about 30 minutes. If you get stuck on anything, don't spend more than a few minutes, jump to the note at the end for how to get help and open an issue before day one.

1. **Log in to the supercomputer.** Go to [OnDemand](https://ondemand.hpc.ucar.edu/), NCAR's web portal for the supercomputer, and log in with your NCAR account. Check your inbox for an NCAR account setup email if you haven't logged in before. Click **Interactive Apps → Jupyter**. In the launch form, select the `Casper PBS Batch` queue — this is the compute pool interactive sessions run on — with `10GB` memory and a `2 hours` walltime. Click **Launch** and wait for the session to start; this submits a real batch job to a compute node, so it can take a minute or two while it waits on the scheduler.

   ![OnDemand's Interactive Apps menu](../static/workshop_2026/OnDemandJupyterClick.png)
   ![Jupyter launch form with Casper PBS Batch, 10GB, and 2 hours filled in](../static/workshop_2026/OnDemandLaunchForm.png)

2. **Create a version-controlled workspace.** We've set up a template repository, [CrocodileWorkspace](https://github.com/CROCODILE-CESM/CrocodileWorkspace), with everything you'll need for the workshop.
   - Click the green ["Use this template → Create a new repository"](https://github.com/new?template_name=CrocodileWorkspace&template_owner=CROCODILE-CESM) button in the top right corner.
   - Name your repo — we recommend `Bask` (the name for a group of crocodiles), since that's what we'll use for the tutorial names. For reference, a copy is at [github.com/manishvenu/Bask](https://github.com/manishvenu/Bask).
   - Keep it **Public** and click **Create Repository**. It needs to be public so the supercomputer can clone it in the next step without setting up SSH keys or a personal access token.

   ![GitHub's "Use this template" button](../static/workshop_2026/TemplateCreate.png)
   ![The repo creation form filled in](../static/workshop_2026/TemplateSpecify.png)

3. **Install the CROCODILE tools.**
   - Open a terminal: from your OnDemand session (Step 1), go to **My Interactive Sessions**, enter the session with the green button, then click the **Terminal** card at the bottom of the page.

   ![OnDemand's Terminal Layout](../static/workshop_2026/TerminalLayout.png)
   - Go to the terminal and move to your `$WORK` directory. We get 2 TB of space there, which is a good place to install:

     ```bash
     cd $WORK
     ```
   - Clone your new workspace repo. You don't need any git experience beyond copy-pasting this command — it downloads your repo onto the supercomputer and keeps it version-controlled, so you can push your regional models back to GitHub, reproducible and online:

     ```bash
     git clone https://github.com/<YOUR USERNAME>/<YOUR WORKSPACE NAME>

     # e.g.
     git clone https://github.com/manishvenu/Bask
     ```
   - Run the installer. `install.sh` sets up everything the workshop needs: CESM, model2obs, and the conda environments for CrocoDash and the other CROCODILE tools. It takes about 10-15 minutes, you'll know it's done when the terminal returns to a normal prompt with no errors in the output. (It also takes flags for installing pieces individually — `--crocodash`, `--CESM`, run `./install.sh -h` for the full list — but for the workshop, one flag down below installs everything):

     ```bash
     cd $WORK/<YOUR WORKSPACE DIRECTORY NAME>
     ./install.sh --workshop
     ```

   ![Terminal output of ./install.sh --workshop completing successfully](../static/workshop_2026/install-workshop-terminal.png)

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
