"""Top-level `python -m crocogallery` command line.

Two verbs: `inject` rewrites notebooks in place, `template` writes a fresh
starter file. `inject` is deliberately explicit -- it edits files in place,
so it should never be what a bare, mistyped invocation does.
"""

import argparse
import sys

from .inject_paths import _parse_set, inject
from .template import DEFAULT_TEMPLATE_NOTEBOOK_ID, uses_notebook, write_template


def _add_path_args(parser):
    """Path-table flags shared by both subcommands."""
    parser.add_argument(
        "--machine",
        default=None,
        help="Which machine's paths to use (e.g. derecho).",
    )
    parser.add_argument(
        "--paths-json",
        default=None,
        help="Your own paths file, either {machine: {KEY: path}} or flat {KEY: path}. "
        "Layered over the bundled known_paths.json; add --no-defaults to use it alone.",
    )
    parser.add_argument(
        "--set",
        dest="sets",
        action="append",
        metavar="KEY=VALUE",
        help="Add or override one placeholder, e.g. --set MYGRID=/glade/.../grid.nc. Repeatable.",
    )
    parser.add_argument(
        "--no-defaults",
        action="store_true",
        help="Ignore the bundled known_paths.json and use only --paths-json/--set.",
    )


def _inject(args):
    changed = inject(
        targets=args.targets,
        reverse=args.reverse,
        machine=args.machine or "derecho",
        json_path=args.paths_json,
        extra_paths=_parse_set(args.sets),
        use_defaults=not args.no_defaults,
    )
    print(f"{len(changed)} notebook(s) modified.")


def _template(args):
    from . import list_notebooks

    if args.list_notebooks:
        for nb_id in sorted(list_notebooks()):
            print(nb_id)
        return

    if not args.output:
        args.subparser.error("--output is required unless --list-notebooks is given.")

    if args.notebook != DEFAULT_TEMPLATE_NOTEBOOK_ID and not uses_notebook(
        args.output, args.kind
    ):
        print(
            "[info] --notebook is ignored for pbs/yaml output; "
            "those templates are standalone files."
        )

    output = write_template(
        args.output,
        notebook_id=args.notebook,
        machine=args.machine,
        kind=args.kind,
        json_path=args.paths_json,
        extra_paths=_parse_set(args.sets),
    )
    print(f"Template written to: {output}")
    if args.machine is None and args.paths_json is None and not args.sets:
        print("Tip: rerun with --machine derecho to pre-fill known dataset paths.")


def build_parser():
    parser = argparse.ArgumentParser(prog="crocogallery")
    subparsers = parser.add_subparsers(dest="command", required=True)

    inject_parser = subparsers.add_parser(
        "inject",
        help="Rewrite notebooks in place, swapping <KEY> placeholders for real paths.",
    )
    inject_parser.add_argument(
        "targets",
        nargs="*",
        help="Notebooks or directories to process. Default: every notebook in the gallery.",
    )
    inject_parser.add_argument(
        "--reverse",
        action="store_true",
        help="Reverse the path injection (real paths back to <KEY>).",
    )
    _add_path_args(inject_parser)
    inject_parser.set_defaults(func=_inject)

    template_parser = subparsers.add_parser(
        "template",
        help="Write a starter case file (notebook, script, yaml) or a PBS script.",
    )
    template_parser.add_argument(
        "--kind",
        choices=["case", "pbs"],
        default="case",
        help=(
            "Kind of template to write. 'case' (default) writes a case definition "
            "-- format picked by --output's suffix (.yaml for a config, .ipynb for "
            "a notebook, .py for a script). 'pbs' writes a PBS batch script."
        ),
    )
    template_parser.add_argument(
        "--output",
        default=None,
        help="Output path. Required unless --list-notebooks is given.",
    )
    template_parser.add_argument(
        "--notebook",
        default=DEFAULT_TEMPLATE_NOTEBOOK_ID,
        help=f"Gallery notebook ID to render (default: {DEFAULT_TEMPLATE_NOTEBOOK_ID}).",
    )
    template_parser.add_argument(
        "--list-notebooks",
        action="store_true",
        default=False,
        dest="list_notebooks",
        help="Print all available gallery notebook IDs and exit.",
    )
    _add_path_args(template_parser)
    template_parser.set_defaults(func=_template, subparser=template_parser)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        args.func(args)
    except (KeyError, FileNotFoundError) as e:
        # KeyError.__str__ reprs its argument, turning embedded newlines into
        # literal "\n" and mangling the multi-line "available options" listing.
        print(e.args[0] if e.args else str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
