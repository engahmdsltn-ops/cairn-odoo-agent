# Architecture

> Describes the design. Components are marked planned until their milestone in [ROADMAP.md](../ROADMAP.md) is complete.

## 1. Principles

1. **Provenance:** a stored fact has `file:line`, version, snapshot id and file hash, or it is not stored.
2. **Index first, source on a miss:** answer from the index; on a miss read the source, answer, and extend the index.
3. **Immutability:** snapshots are never edited; a refresh creates a new one.
4. **Isolation:** versions, projects, and layers do not leak into each other.
5. **Consent:** growth (skills, imports, promotions, rollbacks) happens only after an explicit yes.
6. **Determinism where possible:** parsing, hashing, diffing and packaging are tested scripts; the model handles judgment and conversation.

## 2. Layers

| | Core | Project |
|---|---|---|
| Memory | per Odoo version, per snapshot | map of that project's addons |
| Skills | approved, general | project-local |
| Reads the other layer | no | reads core memory, read only |
| Moves between layers | only by an approved promotion | |

## 3. Snapshots and shared objects

A snapshot is an immutable manifest of one source checkout: `path -> file hash -> object`. Extracted structure and semantic notes are stored **by file hash**, so unchanged files are shared between snapshots and only changed files are re-extracted. Projects pin a snapshot and move only on request.

```
memory/<version>/
  snapshots/<id>/manifest.jsonl, read-log.jsonl, meta.yaml
  objects/   (keyed by file hash, shared)
  notes/     (keyed by file hash, shared)
  changes/   (records of what changed between snapshots)
  CURRENT    (pointer)
```

## 4. Read tracker

Each manifest line has a status (`unread`, `indexed`, `read`, `skipped`) and a depth (`structure` for script-parsed, `read` for agent-understood). An append-only read log records what was read, which lines, and why. Coverage is computed per addon and overall.

## 5. Lookup procedure

1. Resolve version and snapshot (project pin, else current).
2. Query the index. A hit is answered as **verified** with `file:line`.
3. A miss triggers a source read, an answer, and an index and manifest update.
4. Reasoning beyond the code is labelled **inferred**; no source means **unverified**.

## 6. Knowledge classes

| Class | Origin | Label |
|---|---|---|
| Source facts | Odoo source | source, file:line, snapshot |
| Functional (source-derived) | tests, tours, demo data, settings | source-derived |
| External | docs, playbooks | doc or practitioner |
| Project facts | the project's addons | project, file:line |
| Lessons | operator corrections | approved proposal |

## 7. Governance

- **Consent gate:** a skill or promotion is proposed with its purpose, files touched and risks, and written only after approval. A skill without a valid help file cannot be approved.
- **Quarantine:** imports land in a quarantine folder, are scanned, shown, and activated only on approval. Imported text is data, never instructions.
- **Versioning:** the agent itself is a git repository with semantic versions and checkpoints before every growth step; rollback uses revert or path checkout.

## 8. Quality model

Generated code follows the pinned version's conventions (read from its index), clean-code rules, and explicit complexity and query-count analysis for non-trivial solutions. A quality gate runs static checks and tests and produces a report mapped to ISO/IEC 25010 characteristics. Wording is "aligned with", never "compliant".

## 9. Runtime safety

Container and database actions apply only to containers declared in the active project file with a development environment. Destructive actions always ask. Secrets live in environment files and never reach memory, logs or exports.
