#!/usr/bin/env python3
"""Fetch metadata and BibTeX for a file of new DOIs."""
from phraise_tools.common import parser, run_cli
from phraise_tools.canonical import collect_canonical
from phraise_tools.metadata import Client


def main(argv=None):
    cli = parser(__doc__)
    cli.add_argument('doi_file', help='DOI file, relative to --root or absolute')
    args = cli.parse_args(argv)
    return run_cli(lambda a: collect_canonical(
        a.root, a.root / a.doi_file,
        Client(a.root, reporter=a.reporter), a.reporter, a.dry_run), args)


if __name__ == '__main__':
    raise SystemExit(main())
