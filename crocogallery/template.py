"""Render gallery notebooks into starter files.

The gallery owns the template *sources* -- the notebooks themselves, the
known_paths.json table, and the loose assets (submit_forcings.pbs,
starter_case.yaml) -- so it also owns the rendering. Downstream CLIs
(e.g. `crocodash template`) are thin wrappers over write_template().
"""

import re
from pathlib import Path

from .inject_paths import (
    gallery_root,
    inject_into_text,
    resolve_paths,
)

DEFAULT_TEMPLATE_NOTEBOOK_ID = "crocodash.tutorial"

# known_paths.json keys that hold placeholder tokens rather than real dataset
# paths -- injecting them would swap an obvious <KEY> for something equally
# uninformative (e.g. "Checkout"), so they are always left for hand editing.
NON_PATH_KEYS = {"CESM", "inputdir", "casedir"}

# Loose template files that live in the gallery next to the notebooks.
TEMPLATE_ASSETS = {"pbs": "submit_forcings.pbs", "yaml": "starter_case.yaml"}


def find_template_asset(name):
    """Locate a loose template asset anywhere under the gallery root.

    Searched rather than derived from a notebook's parent directory: the
    assets and the tutorial notebook do not necessarily live in the same
    folder, and deriving the location silently breaks when either moves.
    """
    matches = [
        p
        for p in sorted(gallery_root().rglob(name))
        if not any(part in {"_build", "__pycache__"} for part in p.parts)
    ]
    if not matches:
        raise FileNotFoundError(
            f"No template asset named {name!r} found in the gallery."
        )
    return matches[0]


def template_paths(machine=None, json_path=None, extra_paths=None):
    """Path table for template rendering, minus the hand-edit placeholders.

    A machine of None means "leave every <KEY> alone".
    """
    if machine is None and json_path is None and not extra_paths:
        return {}
    paths = resolve_paths(
        machine=machine or "derecho",
        json_path=json_path,
        extra_paths=extra_paths,
        use_defaults=machine is not None,
    )
    return {k: v for k, v in paths.items() if k not in NON_PATH_KEYS}


def comment_out_magics(source):
    """Comment out IPython magic/shell lines (jupytext convention) so
    extracted code cells are valid, runnable Python."""
    return "\n".join(
        "# " + line if re.match(r"^\s*[%!]", line) else line
        for line in source.split("\n")
    )


def _read_notebook(notebook_id):
    from . import get_notebook_path
    import nbformat

    return nbformat.read(get_notebook_path(notebook_id), as_version=4)


def render_notebook(notebook_id, paths):
    """Return an nbformat notebook with paths injected into code cells."""
    nb = _read_notebook(notebook_id)
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.source = inject_into_text(cell.source, paths)
    return nb


def render_script(notebook_id, paths):
    """Return the notebook as a jupytext-style `# %%` Python script."""
    nb = _read_notebook(notebook_id)
    blocks = []
    for cell in nb.cells:
        if cell.cell_type == "code":
            code = comment_out_magics(inject_into_text(cell.source, paths))
            blocks.append("# %%\n" + code)
        elif cell.cell_type == "markdown":
            commented = "\n".join(
                f"# {line}" if line else "#" for line in cell.source.split("\n")
            )
            blocks.append("# %% [markdown]\n" + commented)
    return "\n\n".join(blocks)


def render_asset(asset_kind, paths):
    """Return a loose template asset ('pbs' or 'yaml') with paths injected."""
    asset = find_template_asset(TEMPLATE_ASSETS[asset_kind])
    return inject_into_text(asset.read_text(), paths)


def write_template(
    output,
    notebook_id=DEFAULT_TEMPLATE_NOTEBOOK_ID,
    machine=None,
    kind="case",
    json_path=None,
    extra_paths=None,
):
    """Write a starter template to `output`.

    The output suffix picks the format: .yaml/.yml a config, .pbs a batch
    script, .ipynb a notebook, anything else a `# %%` Python script.
    kind="pbs" forces the batch script regardless of suffix.
    """
    import nbformat

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    paths = template_paths(machine, json_path, extra_paths)

    is_pbs = kind == "pbs" or output.suffix == ".pbs"
    if is_pbs:
        output.write_text(render_asset("pbs", paths))
        output.chmod(output.stat().st_mode | 0o111)
    elif output.suffix in (".yaml", ".yml"):
        output.write_text(render_asset("yaml", paths))
    elif output.suffix == ".ipynb":
        nbformat.write(render_notebook(notebook_id, paths), output)
    else:
        output.write_text(render_script(notebook_id, paths))
    return output


def uses_notebook(output, kind="case"):
    """Whether this output would be rendered from --notebook.

    The pbs and yaml templates are standalone assets, so --notebook is
    meaningless for them; callers use this to warn instead of silently
    ignoring the flag.
    """
    output = Path(output)
    return not (kind == "pbs" or output.suffix in (".pbs", ".yaml", ".yml"))
