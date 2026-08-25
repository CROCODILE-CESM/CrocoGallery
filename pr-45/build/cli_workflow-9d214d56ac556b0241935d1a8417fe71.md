# Running CrocoDash from the CLI

CrocoDash cases can be set up entirely from the command line using a YAML config file — no Python scripting required.

The workflow is three steps:

```bash
# 1. Get a starter config
crocodash template --output my_case.yaml

# 2. Edit it (fill in paths, domain, compset, etc.)
vim my_case.yaml

# 3. Create the case
crocodash create --config my_case.yaml
```

Add `--machine derecho` to `template` to pre-fill known dataset paths for Derecho/GLADE:

```bash
crocodash template --output my_case.yaml --machine derecho
```

---

## Starter config

The template gives you a fully annotated YAML with all available options:

```{literalinclude} starter_case.yaml
:language: yaml
```

---

## Round-tripping an existing case

If you already have a CrocoDash case and want to reproduce or modify it, `dump` reconstructs the YAML from the case's state files:

```bash
crocodash dump --caseroot /path/to/my_case > my_case.yaml
```

Edit the output and re-run with `crocodash create --config my_case.yaml --override`.

---

## Submitting forcing extraction to a PBS queue

Forcing extraction (`crocodash process`) can be slow enough that it shouldn't run
on a login node. Get a starter PBS submission script with `--kind pbs`:

```bash
crocodash template --output submit_forcings.pbs --kind pbs --machine derecho
```

Fill in your project code and caseroot, then `qsub submit_forcings.pbs`.

---

## All subcommands

| Command | Purpose |
|---|---|
| `crocodash template` | Write a starter case file (`--kind case`, default: `.yaml` config, `.ipynb` notebook, or `.py` script) or a PBS submission script (`--kind pbs`) |
| `crocodash create` | Create a case from a YAML config |
| `crocodash dump` | Reconstruct YAML from an existing case |
| `crocodash bundle` | Package a case for sharing |
| `crocodash fork` | Create a new case from a bundle with guided editing |
| `crocodash duplicate` | Copy an existing case to a new location |
