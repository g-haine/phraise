#!/usr/bin/env python3
"""Generate author and year pages and their indexes."""
from phraise_tools.common import parser, run_cli
from phraise_tools.generate import generate_pages


def main(argv=None):
    return run_cli(lambda a: generate_pages(a.root), parser(__doc__).parse_args(argv))


if __name__ == '__main__':
    raise SystemExit(main())
