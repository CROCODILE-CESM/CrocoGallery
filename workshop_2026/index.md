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
The first thing we're doing at the workshop is setting up all the tools for CROCODILE. If you have the time, please try to do these ahead of the workshop so the first practicum goes smoothly:

1. `Make sure you can log in to the super computer:` 
  a. Go to `OnDemand`: [https://ondemand.hpc.ucar.edu/] and log in with your NCAR account. You should have gotten an email with the setup steps. 
  b. Click on "Interactive Apps" -> and select "Jupyter"
  c. Select the following options in the portal. "Casper PBS Batch" "10GB" "2 hours"


2. `Let's create a version controlled workspace for CROCODILE tools:` We've setup a template git repository to use for CROCODILE tools. Create your own repository for the workshop from our template [CrocodileWorkspace](https://github.com/CROCODILE-CESM/Bask): [https://github.com/CROCODILE-CESM/CrocodileWorkspace]. 
  a. Cick the green ['Use this template -> Create a new repository'](https://github.com/new?template_name=CrocodileWorkspace&template_owner=CROCODILE-CESM) button in the top right corner. 
  b. Select the name of your repo, we recommend "Bask", which is the name for a group of crocodiles. That's what we'll use for the tutorial names. My repo is [https://github.com/manishvenu/Bask]
  c. Keep it Public & Click the "Create Repository" option

3. `Let's install the CROCODILE tools:` Let's use our new repo to install CROCODILE tools!
  a. As supercomputer users, we get access to 2 TB of space on our $WORK directories on the NCAR supercomputer. We recommend installing the repository in your work directory. But first, we need to open a terminal. Click into your OnDemand "My Interactive Sessions" area from Step 1, start your session with the green button. 
  b. Once you open the session, scroll to the bottom of the page, and click the "Terminal" card.
  c. Now, the terminal session should be open! Let's install the CROCODILE tools, find a folder you want to put the tools in, we recommend your work directory, so:
  ```
  $ cd $WORK
  ```
  d. We then need to copy our workspace onto our computer, which we can do with the common git command "git clone". This allows us to version our workspace, which means, we can push out regional models back from this workspace to Github. They'll be reproducible and online! Here's my git command, replace it with your username and repo name!
  ```
  $ git clone https://github.com/manishvenu/Bask
  $ git clone https://github.com/<YOUR USERNAME>/<YOUR WORKSPACE NAME>
  ```
  e. The last step is to install the packages and environments we need to run everything. Inside of the CROCODILE workspace, there is an install script "./install.sh" that install everything you need with command line flags. You can manage several different things, like installing only crocodash, our regional setup tool, with "./install.sh --crocodash" or the CESM, with "./install.sh --CESM". You can look at all the available flags with "./install.sh -h". However, since we want to setup the whole system with some special workshop paths, we have a special flag for the workshop, which installs everything:
  ```
  $ cd $WORK/<YOUR WORKSPACE DIRECTORY NAME>
  $ ./install.sh --workshop 
  ```

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
