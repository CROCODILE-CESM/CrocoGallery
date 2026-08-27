from .inject_paths import build_parser, main, _parse_set

args = build_parser().parse_args()
main(
    reverse=args.reverse,
    machine=args.machine,
    targets=args.targets,
    json_path=args.paths_json,
    extra_paths=_parse_set(args.sets),
    use_defaults=not args.no_defaults,
)
