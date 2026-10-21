# Design decisions

Short records of the choices that shape Cairn. Each states the trade-off.

## D1. Source-only knowledge, with confidence labels
**Decision:** Odoo facts come only from source the operator provides; answers are labelled verified, inferred or unverified.
**Why:** Odoo APIs differ across versions; confident answers from training data are the main failure mode.
**Cost:** more "unverified" answers until coverage grows.

## D2. Immutable snapshots with shared objects
**Decision:** a refresh creates a new snapshot; extracted data is stored by file hash and shared.
**Why:** projects built against an older checkout must still query the knowledge that matches it, without paying to re-read unchanged files.
**Alternative rejected:** mutating one live index (loses history, makes rollbacks unsafe).

## D3. Deterministic indexing, model for judgment
**Decision:** structure is extracted by parsers (Python AST, XML), with the model writing only semantic notes.
**Why:** exact, cheap, testable, reproducible.

## D4. Consent gate for growth
**Decision:** skills, imports, promotions and rollbacks are proposals until approved.
**Why:** keeps the agent clean and every addition traceable. Hooks add a second line of defence.

## D5. Plain files over a vector database in v1
**Decision:** JSON objects and Markdown notes, searched with exact queries.
**Why:** transparent, diffable, exportable, and sufficient for structured code facts. Embeddings can be added if retrieval proves insufficient.

## D6. Layer isolation
**Decision:** projects read core memory read-only; nothing moves up without promotion.
**Why:** client or project specifics must never leak into general knowledge.

## D7. Guardrails, not a sandbox
**Decision:** permissions and hooks are documented as risk reduction, with a recommendation to run on a dev machine.
**Why:** honesty about what they can and cannot guarantee.

## D8. Public repository built from an allowlist
**Decision:** the public repo contains only explicitly allowlisted files, produced from a private working repo.
**Why:** the working repo holds memory derived from source that may be proprietary or confidential.
