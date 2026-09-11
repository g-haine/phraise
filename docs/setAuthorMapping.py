#!/usr/bin/env python3
"""Inspect unknown authors and optionally apply unambiguous mappings."""
import json

from phraise_tools.common import parser, run_cli
from phraise_tools.generate import (apply_safe_author_mappings,
                                    author_mapping_plan,
                                    format_author_mapping_plan)


def process(args):
    if args.apply_safe:
        action = 'Simulating' if args.dry_run else 'Applying'
        args.reporter.step(f'{action} author mappings with no detected ambiguity')
        applied, plan = apply_safe_author_mappings(
            args.root, args.reporter, args.dry_run)
    else:
        applied, plan = 0, author_mapping_plan(args.root)
    if args.json:
        return json.dumps({'applied': 0 if args.dry_run else applied,
                           'would_apply': applied if args.dry_run else 0,
                           'dry_run': args.dry_run, **plan},
                          ensure_ascii=False, indent=2)
    report = format_author_mapping_plan(plan, applied, args.dry_run)
    return f'Dry run:\n{report}' if args.dry_run else report


def main(argv=None):
    cli = parser(__doc__)
    cli.add_argument('--apply-safe', action='store_true',
                     help='Add unique new authors with no plausible existing match')
    cli.add_argument('--json', action='store_true',
                     help='Print the analysis as JSON instead of a human report')
    return run_cli(process, cli.parse_args(argv))


if __name__ == '__main__':
    raise SystemExit(main())
