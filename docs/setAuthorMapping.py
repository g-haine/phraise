#!/usr/bin/env python3
"""Print proposed author mappings as JSON; review and merge them manually."""
from phraise_tools.common import parser, run_cli
from phraise_tools.generate import author_suggestions


def main(argv=None):
    return run_cli(lambda a: author_suggestions(a.root), parser(__doc__).parse_args(argv))


if __name__ == '__main__':
    raise SystemExit(main())
