---
title: Projects
description: Open-ended, self-directed CrocoDash projects for the workshop. The tutorials teach the tools; the projects are where you use them on a problem of your own.
---

<div class="cd-hero">
  <div class="cd-hero__eyebrow">CrocoDash · Workshop 2026</div>
  <h1 class="cd-hero__title">Projects</h1>
  <p class="cd-hero__desc">
    The tutorials walk you through CrocoDash one step at a time. The projects hand you a
    problem instead of a script: pick one, work it on your own region, and leave the
    workshop with a case that is yours.
  </p>
  <div class="cd-hero__actions">
    <a class="cd-btn cd-btn--primary" href="#pick-a-project">Pick a project ↓</a>
    <a class="cd-btn cd-btn--outline" href="../crocodash_tutorial.ipynb">Back to the tutorial</a>
  </div>
</div>

## How projects differ from the tutorials

|  | Tutorials & Use Cases | Projects |
|---|---|---|
| **Gives you** | The steps, in order, with the code | A goal and a definition of done |
| **Domain** | Ours | Yours |
| **Outcome** | You understand the API | You have a case, a result, and a story about it |
| **When stuck** | Read the next cell | Read the tutorial, ask a human, open an issue |

Projects deliberately **do not restate** the tutorial material. Each one lists the pages
it builds on and assumes you have run them. If a project asks you to "build the grid",
that means [`grids.ipynb`](../grids.ipynb) — go there, don't wait for the code here.

(pick-a-project)=
## Pick a project

Projects are independent — you do not need to do them in order. Each one starts from a
region **you** choose (or the one you brought with you).

<div class="cd-nav-cards">
  <a class="cd-nav-card" href="design_your_domain.md">
    <h3>1 · Design Your Domain</h3>
    <p>Go from a region on a map to a case that runs. The backbone project — most others start from its output.</p>
  </a>
  <a class="cd-nav-card" href="forcing_experiments.md">
    <h3>2 · Force It Differently</h3>
    <p>Swap products, add tides, runoff, or BGC, and find out what your boundaries and surface actually do to your solution.</p>
  </a>
  <a class="cd-nav-card" href="resolution_study.md">
    <h3>3 · Resolution &amp; Vertical Grid Study</h3>
    <p>Run the same region at more than one horizontal or vertical resolution and defend a choice with evidence.</p>
  </a>
  <a class="cd-nav-card" href="make_it_stable.md">
    <h3>4 · Make It Stable</h3>
    <p>Take a case that blows up and make it run. Timestep, bathymetry, sponges, boundaries — diagnose before you change.</p>
  </a>
  <a class="cd-nav-card" href="add_a_component.md">
    <h3>5 · Add a Component</h3>
    <p>Bring sea ice, waves, or biogeochemistry into your regional case and check the coupling did what you expected.</p>
  </a>
  <a class="cd-nav-card" href="share_and_reproduce.md">
    <h3>6 · Share &amp; Reproduce</h3>
    <p>Bundle your case, hand it to someone else, and reproduce theirs. The project that tests whether any of this travels.</p>
  </a>
</div>

## Working a project

1. **Scope it small.** A domain you can force and run inside the workshop beats one you
   can only describe. A few degrees on a side and a few days of simulation is plenty.
2. **Write down what you expect before you run it.** The project is more interesting when
   the model disagrees with you.
3. **Keep the case reproducible.** Config in a YAML, notes in the case directory —
   see [Running CrocoDash from the CLI](../advanced/cli_workflow.md).
4. **Finish the definition of done.** Each project ends with a short checklist. That is
   the bar, not "I ran something".

## Other things worth building

Not every good project needs its own page. If none of the six fit, these are fair game
and we will help you scope them:

- Extend [nesting](../advanced/nesting_demo.ipynb) to a third level, or nest inside a
  domain a neighbour built.
- Use [interior OBC segments](../advanced/interior_obc_segments.ipynb) to carve a strait,
  channel, or island out of your domain.
- Rebuild one of the [use cases](../use_cases/three_boundary.ipynb) somewhere else in the
  world and report what broke.
- Contribute the result back to this gallery as a new use case.

## Getting unstuck

- The relevant tutorial page, first — most project blockers are a step you skipped.
- [CrocoDash issues](https://github.com/CROCODILE-CESM/CrocoDash/issues) for anything that
  looks like a bug rather than a misunderstanding.
- Any of us, in the room. That is what the workshop is for.
