# Running CrocoDash from the CLI

CrocoDash cases can be set up entirely from the command line using a YAML config file, no Python scripting required.

The workflow is three steps:

```bash
# 1. Get a starter config
crocodash template --output my_case.yaml

# 2. Edit it (fill in paths, grid files, compset, etc.)
vim my_case.yaml

# 3. Create the case
crocodash create --config my_case.yaml
```

The config names the case's grid files rather than describing the grid: write them
once with CrocoDash's `Grid`, `Topo` and `VGrid` (the starter config shows how), or
reuse another case's. Leave out the `forcings:` section and `create` asks for the
forcings on a terminal: first which optional ones to add, then each input.

Add `--machine glade` to `template` to pre-fill known dataset paths for GLADE (Derecho/Casper):

```bash
crocodash template --output my_case.yaml --machine glade
```

---

## Starter Yaml

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

To copy a case instead, `crocodash create --from /path/to/my_case` (a caseroot or a
bundle) asks for the new case's caseroot, inputdir, machine and so on, offering the old
case's. The new case keeps your own changes to the old one and reuses its forcing files
where they still match.

To change only the forcings of an existing case, `crocodash configure --caseroot
/path/to/my_case` asks for them again, offering the current values.

---

## Submitting forcing extraction to a PBS queue

Forcing extraction (`crocodash process`) can be slow enough that it shouldn't run
on a login node. Get a starter PBS submission script with `--kind pbs`:

```bash
crocodash template --output submit_forcings.pbs
```

Fill in your project code and caseroot, then `qsub submit_forcings.pbs`.

---

## All subcommands

| Command | Purpose |
|---|---|
| `crocodash template` | Write a starter case file (`--kind case`, default: `.yaml` config, `.ipynb` notebook, or `.py` script) or a PBS submission script (`--kind pbs`) |
| `crocodash create` | Create a case from a YAML config (`--config`), or from another case or a bundle (`--from`) |
| `crocodash dump` | Reconstruct YAML from an existing case |
| `crocodash configure` | Configure an existing case's forcings again |
| `crocodash process` | Run the forcing extraction for an existing case (`--all`, or per-component flags) |
| `crocodash bundle` | Package a case for sharing; `crocodash create --from` reads it |
