# Validation scope

The initial split passed native skill validation and local reference checks. Its development review considered 24 routing prompts, followed by targeted fixes and two additional routing checks. Synthetic trials exercised multiple goals, correction propagation, preservation of one intervening human edit, scoped forgetting, a six-month cost decision, and a tracker with tested calculations. A separate agent recovered state from a saved synthetic vault.

Those were selected forward tests, not a complete benchmark or proof of production reliability. The original broader single-skill evaluation was not rerun in full against the split. Personal installation and real-vault continuity evidence remain outside this repository.

The repeatable repository check is `python3 scripts/check.py`. It checks the current files only. Live account operations, concurrent writers, crash recovery, Obsidian rendering, and probabilistic auto-selection are outside its scope.

When changing a workflow, record the fixture, runtime revision, actual response/artifacts, observed behavior, and limits. Keep synthetic data separate from user records. A later revision needs relevant new checks rather than inheriting a blanket pass claim.

The [2026-09-16 writing review](writing-review.md) records the current source revision’s structural checks and three narrow synthetic forward tests, with [raw evidence](writing-review-evidence.md).
