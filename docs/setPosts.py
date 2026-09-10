#!/usr/bin/env python3
"""Generate publication posts and archive orphan BibTeX files."""
from phraise_tools.common import parser, run_cli
from phraise_tools.generate import generate_posts
from phraise_tools.metadata import Client


def main(argv=None):
    return run_cli(lambda a: generate_posts(a.root, Client(a.root)), parser(__doc__).parse_args(argv))


if __name__ == '__main__':
    raise SystemExit(main())
