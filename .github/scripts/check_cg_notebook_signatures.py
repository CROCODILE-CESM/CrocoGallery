"""
Notebook API compatibility checker for CrocoDash.

This script checks that Jupyter notebooks in CrocoGallery are calling
CrocoDash and mom6_bathy functions (CrocoDash directly wraps mom6_bathy for grid generation) correctly — verifying that function
names exist and are called with valid arguments.

Largely generated with Claude, so feel free to change the script.

Usage:
    python check_notebook_signatures.py <path_to_gallery>

Example:
    python .github/scripts/check_notebook_signatures.py gallery/notebooks/
"""

import importlib
import sys
import ast
import inspect
import nbformat
from pathlib import Path

# Object name prefixes to ignore when scanning for function calls.
# These are common libraries that are not CrocoDash and should not be checked.
IGNORE_PREFIXES = {
    "plt",
    "ax",
    "fig",
    "np",
    "pd",
    "os",
    "sys",
    "utils",
    "xr",
    "ds",
    "shutil",
}

# Explicit list of CrocoDash submodules to scan for callable signatures.
# Add new modules here as CrocoDash grows.
CROCODASH_MODULES = [
    "CrocoDash.case",
    "CrocoDash.raw_data_access.datasets.seawifs",
    "CrocoDash.raw_data_access.datasets.glofas",
    # add others as needed
]

# Explicit list of mom6_bathy submodules to scan for callable signatures.
MOM6_BATHY_MODULES = [
    "mom6_bathy.grid",
    "mom6_bathy.topo",
    "mom6_bathy.vgrid",
    # add others as needed
]


def get_crocodash_signatures():
    """Build a map of function/method name -> inspect.Signature from CrocoDash and mom6_bathy.

    Imports each module explicitly (since both packages have empty __init__.py files
    and inspect.getmembers on the top-level package would find nothing). Also recurses
    into classes to pick up instance methods like Grid.subgrid_from_supergrid.

    Returns:
        dict: mapping of callable name (str) -> inspect.Signature
    """
    sigs = {}
    for modname in CROCODASH_MODULES + MOM6_BATHY_MODULES:
        module = importlib.import_module(modname)
        for name, obj in inspect.getmembers(module, callable):
            # get signature for module-level functions and classes
            try:
                sigs[name] = inspect.signature(obj)
            except (ValueError, TypeError):
                pass
            # recurse into classes to capture instance methods
            if inspect.isclass(obj):
                for method_name, method in inspect.getmembers(obj, callable):
                    if not method_name.startswith("__"):  # skip dunder methods
                        try:
                            sigs[method_name] = inspect.signature(method)
                        except (ValueError, TypeError):
                            pass
    return sigs


def notebook_uses_crocodash(nb):
    """Check if a notebook references CrocoDash anywhere in its code cells.

    Used as a fast way to skip notebooks that don't use CrocoDash at all,
    avoiding unnecessary AST parsing. Handles both direct imports and common
    patterns like `case.some_method()`.

    Args:
        nb: parsed nbformat notebook object

    Returns:
        bool: True if any code cell references CrocoDash
    """
    for cell in nb.cells:
        if cell.cell_type == "code" and (
            "CrocoDash" in cell.source or "case." in cell.source
        ):
            return True
    return False


def extract_crocodash_calls(notebook_path):
    """Parse a notebook and extract all non-ignored attribute-style function calls.

    For each call like `obj.method(arg1, kwarg=val)`, captures:
    - the method name
    - number of positional args
    - set of keyword arg names
    - whether **kwargs unpacking was used

    Skips notebooks that don't reference CrocoDash at all (see notebook_uses_crocodash).
    Skips .ipynb_checkpoints directories.
    Ignores calls on objects in IGNORE_PREFIXES (e.g. plt.show, np.array).

    Args:
        notebook_path (Path): path to the .ipynb file

    Returns:
        list of tuples: (path, func_name, pos_args, kw_args, has_var_kw, ast_node)
    """
    nb = nbformat.read(notebook_path, as_version=4)

    if not notebook_uses_crocodash(nb):
        print(f"⏭️  Skipping {notebook_path} — no CrocoDash usage found")
        return []

    calls = []
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        try:
            tree = ast.parse(cell.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Attribute):
                        obj_name = (
                            node.func.value.id
                            if isinstance(node.func.value, ast.Name)
                            else None
                        )
                        if obj_name and obj_name not in IGNORE_PREFIXES:
                            pos_args = len(node.args)
                            kw_args = {
                                kw.arg for kw in node.keywords if kw.arg is not None
                            }
                            # detect **kwargs unpacking — kw.arg is None when **something is used
                            has_var_kw = any(kw.arg is None for kw in node.keywords)
                            calls.append(
                                (
                                    notebook_path,
                                    node.func.attr,
                                    pos_args,
                                    kw_args,
                                    has_var_kw,
                                    node,
                                )
                            )
        except SyntaxError:
            pass
    return calls


def check_call_args(func_name, sig, pos_args, kw_args, has_var_kw):
    """Validate a function call against its signature.

    Checks three things:
    1. No unknown keyword arguments (unless the function accepts **kwargs)
    2. Not too many positional arguments (unless the function accepts *args)
    3. All required arguments appear to be covered

    Note: if the call uses **kwargs unpacking we skip validation entirely since
    we can't statically determine what keys are inside.

    Args:
        func_name (str): name of the function (for error messages)
        sig (inspect.Signature): the function's signature
        pos_args (int): number of positional args in the call
        kw_args (set): set of keyword argument names in the call
        has_var_kw (bool): whether the call uses **kwargs unpacking

    Returns:
        str | None: error description string, or None if the call looks valid
    """
    # can't validate statically if **kwargs is being unpacked into the call
    if has_var_kw:
        return None

    params = sig.parameters
    errors = []

    param_names = list(params.keys())
    # strip 'self' — it's never passed explicitly in notebook calls
    if param_names and param_names[0] == "self":
        param_names = param_names[1:]

    # required params: no default, not *args or **kwargs
    required = [
        p
        for p in param_names
        if params[p].default is inspect.Parameter.empty
        and params[p].kind
        not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)
    ]

    # valid keyword arg names (excludes *args and **kwargs params themselves)
    valid_kw = {
        p
        for p in param_names
        if params[p].kind
        not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)
    }
    has_var_positional = any(
        p.kind == inspect.Parameter.VAR_POSITIONAL for p in params.values()
    )  # Does this have *args? If so we can skip the positional arg count check since it can take any number.
    has_var_keyword = any(
        p.kind == inspect.Parameter.VAR_KEYWORD for p in params.values()
    )  # Does this have **kwargs? If so we can skip the unknown keyword arg check since it can take any keys.

    # unknown keyword args — only check if the function doesn't swallow them with **kwargs
    if not has_var_keyword:
        unknown_kw = kw_args - valid_kw
        if unknown_kw:
            errors.append(f"unknown keyword args: {unknown_kw}")

    # too many positional args — only check if the function doesn't accept *args
    if not has_var_positional:
        max_pos = len(param_names)
        if pos_args > max_pos:
            errors.append(f"too many positional args: got {pos_args}, max {max_pos}")

    # missing required args — roughly check positional + keyword coverage
    covered = set(param_names[:pos_args]) | kw_args
    missing_required = [r for r in required if r not in covered]
    if missing_required:
        errors.append(f"possibly missing required args: {missing_required}")

    return "; ".join(errors) if errors else None


def check_notebooks(gallery_path):
    """Main entry point. Scans all notebooks in gallery_path and reports API errors.

    For each notebook:
    - Skips .ipynb_checkpoints
    - Skips notebooks with no CrocoDash usage
    - Checks all CrocoDash function calls exist and are called correctly

    Exits with code 1 if any errors are found, 0 otherwise.

    Args:
        gallery_path (str): path to the notebook gallery directory
    """
    sigs = get_crocodash_signatures()
    errors = []

    for nb_path in Path(gallery_path).rglob("*.ipynb"):
        if ".ipynb_checkpoints" in nb_path.parts:
            continue
        calls = extract_crocodash_calls(nb_path)
        for path, func_name, pos_args, kw_args, has_var_kw, node in calls:
            # check the function exists in CrocoDash at all
            if func_name not in sigs:
                errors.append(f"{path}: '{func_name}' not found in CrocoDash")
                continue  # no point checking args if function doesn't exist

            # check the function is called with valid arguments

            arg_error = check_call_args(
                func_name, sigs[func_name], pos_args, kw_args, has_var_kw
            )
            if arg_error:
                errors.append(f"{path}: '{func_name}' called incorrectly — {arg_error}")

    if errors:
        print("❌ Signature check failures:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print("✅ All notebook CrocoDash calls look valid (rudimentarily checked)")


if __name__ == "__main__":
    check_notebooks(sys.argv[1])
