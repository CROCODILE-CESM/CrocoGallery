# Running CUPiD within CESM

CUPiD has been included in the CESM workflow,
which means you can run CUPiD from a CESM case directory with the familiar `case.submit` command.
For this exercise, we will run the notebooks Aidan put together on the case you ran with Manish.

Steps:

1. Show all CUPiD env variables in case root (` ./xmlquery -p CUPID`)
1. Show snippets from `case.cupid` and `cesm_postprocessing.sh` to explain what CUPiD will do
1. make a bunch of `xmlchange` calls (`CUPiD_ROOT`? also set run length, only run ocean notebooks, maybe increase `MEM_PER_TASK`)
1. `./case.submit --job case.cupid`


## Task 3:

### Task 3.1: Explore how CUPiD is Incorporated in a CESM Case

As you saw in previous tutorials, CESM uses XML files to manage the environment in which your case is run.
Each file contains variables pertaining to a different phase of the case generation process:

```bash
$ ls -1 env_*
env_archive.xml
env_batch.xml
env_build.xml
env_case.xml
env_mach_pes.xml
env_mach_specific.xml
env_postprocessing.xml
env_run.xml
env_workflow.xml
```

We are interested in the CUPiD variables,
which are all defined in `env_postprocessing.xml`.
XML variables plain-text files so we could inspect them directly,
but let's use the provided `xmlquery` tool instead.

<span style="background-color:#CF9812">🚨 POP QUIZ #1!! 🚨</span>

> How do you use `xmlquery` to see all the variables that contain `CUPID` in their name (along with their values)?


<details>
<summary>(Solution to quiz #1)</summary>

```
$ ./xmlquery -p CUPID
Results in group cupid_analysis
	CUPID_BASELINE_CASE: b.e23_alpha17f.BLT1850.ne30_t232.092
	CUPID_BASELINE_ROOT: /glade/derecho/scratch/mlevy/archive/CAcurrent.002/..
	CUPID_BASE_NYEARS: 100
	CUPID_BASE_STARTDATE: 0001-01-01
	CUPID_EXAMPLE: key_metrics
	CUPID_NYEARS: 1
	CUPID_STARTDATE: 0001-01-01
	CUPID_TS_DIR: /glade/derecho/scratch/mlevy/archive/CAcurrent.002/..

Results in group cupid_config
	CUPID_GEN_DIAGNOSTICS: TRUE
	CUPID_GEN_HTML: TRUE
	CUPID_GEN_TIMESERIES: TRUE
	CUPID_ROOT: /glade/work/mlevy/codes/CESM/cesm3_0_alpha07c_CROCO/tools/CUPiD

Results in group cupid_environments
	CUPID_ANALYSIS_ENV: cupid-analysis
	CUPID_INFRASTRUCTURE_ENV: cupid-infrastructure

Results in group cupid_run_components
	CUPID_MEM_PER_TASK: 10
	CUPID_NTASKS: 1
	CUPID_RUN_ADF: FALSE
	CUPID_RUN_ALL: TRUE
	CUPID_RUN_ATM: FALSE
	CUPID_RUN_GLC: FALSE
	CUPID_RUN_ICE: FALSE
	CUPID_RUN_LND: FALSE
	CUPID_RUN_OCN: FALSE
	CUPID_RUN_ROF: FALSE
	CUPID_TASKS_PER_NODE: 128
```
</details>

### Task 3.2: Configure and Run CUPiD

The first variable to talk about is `CUPID_ROOT`.
CUPiD is distributed with CESM in the `tools/CUPiD` subdirectory,
but you may wish to use a more recent version of CUPiD.
This could be handy if, for example,
you are taking a tutorial and the first exercises were cloning CUPiD,
installing environments from this clone and then running a few examples.
In that case, you want to run

```bash
./xmlchange CUPID_ROOT=${CUPID_ROOT}
```

Also, as we saw in the last section of this tutorial,
we want to run the `regional_ocean` example and use 100 GB of memory.
These are set by the `CUPID_EXAMPLE` and `CUPID_MEM_PER_TASK` variables, respectively.

<span style="background-color:#CF9812">🚨 POP QUIZ #2!! 🚨</span>

> How do we use `xmlchange` to set `CUPID_EXAMPLE = regional_ocean` and `CUPID_MEM_PER_TASK = 100`?

<details>
<summary>(Solution to quiz #2)</summary>

```bash
./xmlchange CUPID_EXAMPLE=regional_ocean,CUPID_MEM_PER_TASK=100
```
</details>
<p>

Lastly, we don't need to generate time series files or build a webpage

```bash
./xmlchange CUPID_GEN_TIMESERIES=FALSE,CUPID_GEN_HTML=FALSE
```

When you are ready to run CUPiD, you can tell `case.submit` that you want to run the `case.cupid` job in the workflow.
Make sure you are logged in to Derecho (not Casper) and then run:

```bash
./case.submit --job case.cupid
```

This will add a job to the development queue on derecho,
and hopefully will start running quickly.
When it finishes, output will be in the [???] subdirectory of your case.