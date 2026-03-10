import sys
import ast
import inspect
import nbformat
from pathlib import Path
import CrocoDash

def get_crocodash_signatures():
    """Build a map of function_name -> signature from CrocoDash"""
    sigs = {}
    for name, obj in inspect.getmembers(CrocoDash, callable):
        try:
            sigs[name] = inspect.signature(obj)
        except (ValueError, TypeError):
            pass
    return sigs

def extract_crocodash_calls(notebook_path):
    """Extract all CrocoDash function calls from a notebook"""
    nb = nbformat.read(notebook_path, as_version=4)
    calls = []
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        try:
            tree = ast.parse(cell.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    # catch CrocoDash.some_function() style calls
                    if isinstance(node.func, ast.Attribute):
                        calls.append((notebook_path, node.func.attr, node))
        except SyntaxError:
            pass
    return calls

def check_notebooks(gallery_path):
    sigs = get_crocodash_signatures()
    errors = []

    for nb_path in Path(gallery_path).rglob("*.ipynb"):
        calls = extract_crocodash_calls(nb_path)
        for path, func_name, node in calls:
            if func_name not in sigs:
                errors.append(f"{path}: '{func_name}' not found in CrocoDash")

    if errors:
        print("❌ Signature check failures:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print("✅ All notebook CrocoDash calls look valid")

if __name__ == "__main__":
    check_notebooks(sys.argv[1])