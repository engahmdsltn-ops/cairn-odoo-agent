# Roadmap

Each milestone ends with passing tests and a review before the next begins. Check a box only when it is merged and tested.

- [ ] **M0. Scaffold and guardrails:** repo layout, core rules, permission settings, hook scripts, tooling skeleton, fixtures
- [ ] **M1. Knowledge engine:** snapshots with shared objects, structural indexer, query, verify, coverage, read log, same-version refresh
- [ ] **M2. Agent versioning:** semantic versions, checkpoints, granular rollback
- [ ] **M3. Skill governance and manual:** consent gate, per-skill help files, generated manual
- [ ] **M4. Portability:** export with a checklist, quarantined import with scanning, promotion
- [ ] **M5. Projects and runtime:** project bootstrap, per-project compose, container control, install and upgrade, debug loop, git operations
- [ ] **M6. Build skills and quality:** scaffolding, customization, front-end, migration, tests, quality gate, complexity and performance analysis
- [ ] **M7. Functional layer and spec slot:** functional packs, fit-gap, spec placeholder
- [ ] **M8. Hardening:** manual, doctor checks, threat-model review
- [ ] **M9. Publish readiness:** allowlist-based public export and pre-publish audit

## Non-goals

- Replacing human review of production changes
- Operating on production databases or containers
- Shipping Odoo source or derived indexes
