#!/usr/bin/env python3
"""Discover publications and queue incomplete entries for recollection."""
from phraise_tools.common import parser, run_cli
from phraise_tools.metadata import Client
from phraise_tools.update import find_updates


def main(argv=None):
    cli = parser(__doc__)
    cli.add_argument('--max-pages', type=int, default=20, help='Maximum OpenAlex pages (default: 20)')
    args = cli.parse_args(argv)
    if args.max_pages < 1:
        cli.error('--max-pages must be positive')
    return run_cli(lambda a: find_updates(
        a.root, Client(a.root, reporter=a.reporter), a.max_pages, a.reporter,
        a.dry_run), args)


if __name__ == '__main__':
    raise SystemExit(main())
