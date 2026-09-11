#!/usr/bin/env python3
"""Inspect unknown authors and optionally apply unambiguous mappings."""
import json

from phraise_tools.common import parser, run_cli
from phraise_tools.generate import (apply_safe_author_mappings,
                                    author_mapping_plan,
                                    format_author_mapping_plan)


def process(args):
    if args.apply_safe:
        args.reporter.step('Applying author mappings with no detected ambiguity')
        applied, plan = apply_safe_author_mappings(args.root, args.reporter)
    else:
        applied, plan = 0, author_mapping_plan(args.root)
    if args.json:
        return json.dumps({'applied': applied, **plan}, ensure_ascii=False, indent=2)
    return format_author_mapping_plan(plan, applied)


def main(argv=None):
    cli = parser(__doc__)
    cli.add_argument('--apply-safe', action='store_true',
                     help='Add unique new authors with no plausible existing match')
    cli.add_argument('--json', action='store_true',
                     help='Print the analysis as JSON instead of a human report')
    return run_cli(process, cli.parse_args(argv))


if __name__ == '__main__':
    raise SystemExit(main())
