# Introduction to CUPiD

## Task 1: Clone CUPiD and Install Environments

CUPiD is available from the NCAR organization on [github.com](https://github.com/NCAR/CUPiD).
It requires conda to manage a few different python environments.
On the NCAR super computer, you can run

```bash
module load conda
```

and use the version of conda managed by the system administrators.
If you need to install conda on a different computer,
we recommend [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)
(but this tutorial assumes you already have access to conda).
We also recommend installing `mamba`,
which is basically a parallelized version of `conda`
(and is part of the NCAR `conda` module).
Instructions for installing CUPiD are available [on the CUPiD website](https://ncar.github.io/CUPiD/#installing),
but we will cover the key steps here.

### 1.1: Clone the repository from github

Running the following command will create a subdirectory named `CUPiD` in your current working directory:

```bash
git clone https://github.com/NCAR/CUPiD.git
```

The rest of this tutorial will refer to the location you installed CUPiD as `${CUPID_ROOT}`.
To be able to copy and paste blocks of commands directly,
so let's add the variable to your environment.

Most of you are using `bash` or `zsh`,
which have been the default shell on Linux and Unix computers for a while now.
To set the environment variable run

```bash
cd CUPiD
export CUPID_ROOT=`pwd -P`
```

If you have changed your shell to `csh` or `tcsh`,
you will want to run the following instead:

```
cd CUPiD
setenv CUPID_ROOT `pwd -P`
```

If you do not know for a fact that you changed your shell,
you can probably assume you are using `bash`.
To know for sure, though, run

```
echo $SHELL
```

### 1.2: Install two conda environments

CUPiD needs a python environment with specific packages installed to run the CUPiD tools,
while the diagnostic notebooks provided with CUPiD need a different set of packages.

To run CUPiD itself we use the `(cupid-infrastructure)` environment:

```bash
cd ${CUPID_ROOT}
mamba env create -f environments/cupid-infrastructure.yml
```

This step may take a while.
When it completes you can verify it was successful by running

```bash
conda activate cupid-infrastructure
which cupid-diagnostics
```

If the environment installed correctly,
`which` will return a path to `cupid-diagnostics`.
If the environment did not install correctly,
`which` will return an error like `which: no cupid-diagnostics in [long list of directories]`.

The other environment provided by CUPiD is `(cupid-analysis)`.
It can be installed by running:

```
mamba env create -f environments/cupid-analysis.yml
```

This may also take a while,
but when it finishes you will be ready to run CUPiD!

## CUPiD Configuration

While the CUPiD environments install, let's talk about how CUPiD works.
The next exercise in this tutorial will be using CUPiD to create diagnostics for a CESM case that has already been run.
After you have completed Task 1 and created the `(cupid-infrastructure)` environment,
Task 2 will involve running the `cupid-diagnostics` command.

```
(cupid-infrastructure) $ cupid-diagnostics --help
Usage: cupid-diagnostics [OPTIONS] [CONFIG_PATH]

  Main engine to set up running all the notebooks.

  Args:     CONFIG_PATH: str, path to configuration file (default config.yml)

  Returns:     None

  Called by ``cupid-diagnostics``.

Options:
  -s, --serial          Do not use LocalCluster objects
  -atm, --atmosphere    Run atmosphere component diagnostics
  -ocn, --ocean         Run ocean component diagnostics
  -lnd, --land          Run land component diagnostics
  -ice, --seaice        Run sea ice component diagnostics
  -glc, --landice       Run land ice component diagnostics
  -rof, --river-runoff  Run river runoff component diagnostics
  -h, --help            Show this message and exit.
```

Notice that `cupid-diagnostics` has a few options to allow you to run a subset of the default diagnostics,
but the `CONFIG_PATH` argument (which defaults to `config.yml`) is the important argument.
This YAML file (YAML is a recursive acronym, standing for ["YAML Ain't Markup Language"](https://yaml.org/);
you have encountered it when dealing with conda environment files as well)
contains all the details about what CUPiD should do.

This can also be found on the CUPiD webpage, on the [Configuration File](https://ncar.github.io/CUPiD/config.html) page.

