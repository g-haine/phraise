#!/usr/bin/env python3
"""One-shot synchronization of tracked PHRAISE site artifacts with BibReview."""
from __future__ import annotations

from bibreview.site import apply_rendered_artifacts, plan_rendered_artifacts

from validate_bibreview_site_persistence import (
    DOCS,
    MANAGED_ROOTS,
    _assert_expected_counts,
    _render_artifacts,
)


def main() -> None:
    posts, indexes = _render_artifacts(DOCS)
    _assert_expected_counts(posts, indexes)
    plan = plan_rendered_artifacts(
        DOCS,
        posts + indexes,
        managed_roots=MANAGED_ROOTS,
    )
    print("Tracked PHRAISE site synchronization plan")
    print(f"  {plan.summary()}")
    for path in plan.writes:
        print(f"  write: {path.relative_to(DOCS).as_posix()}")
    for path in plan.deletes:
        print(f"  delete: {path.relative_to(DOCS).as_posix()}")
    apply_rendered_artifacts(plan)
    print("Tracked PHRAISE site synchronization applied")


if __name__ == "__main__":
    main()
